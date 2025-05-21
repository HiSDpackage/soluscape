# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings
from inspect import isfunction
from sympy import *
from .AnaCal import *
from .HessianMatrix import *
from .EigMethod import *

warnings.filterwarnings("ignore")


def HiSDCheckParam(instance, **kwargs):
	"""
	Initialize parameters and check validity.
	"""
	if "InitialPoint" not in kwargs:
		raise ValueError(
			"Missing required parameter: `InitialPoint` must be specified."
		)
	else:
		instance.InitialPoint = np.array(kwargs["InitialPoint"])
		if instance.InitialPoint.ndim > 2 or (
			instance.InitialPoint.ndim == 2
			and instance.InitialPoint.shape[0] > 1
			and instance.InitialPoint.shape[1] > 1
		):
			raise ValueError(f"Parameter `InitialPoint` requires 1D array.")
		else:
			if instance.InitialPoint.ndim == 1:
				instance.InitialPoint = instance.InitialPoint.reshape(-1, 1)
			if instance.InitialPoint.shape[1] > 1:
				instance.InitialPoint = np.transpose(instance.InitialPoint)
			if "Dim" in kwargs:
				if isinstance(kwargs["Dim"], int) and kwargs["Dim"] > 0:
					instance.Dim = kwargs["Dim"]
					if instance.InitialPoint.shape[0] != instance.Dim:
						raise ValueError(
							f"Dimension mismatch: `InitialPoint` has shape {instance.InitialPoint.shape[0]}*1, expected `Dim`={instance.Dim}."
						)
				else:
					raise ValueError(
						f"Invalid `Dim` value: expected positive integer, got {instance.Dim} (type={type(instance.Dim).__name__})."
					)
			else:
				instance.Dim = instance.InitialPoint.shape[0]
				print(
					f"[Config Sync] `Dim` parameter auto-adjusted to {instance.Dim} based on `InitialPoint` dimensionality."
				)

	# Validate 'NumericalGrad' parameter
	if "NumericalGrad" in kwargs:
		if isinstance(kwargs["NumericalGrad"], bool):
			instance.NumericalGrad = kwargs["NumericalGrad"]
		else:
			raise ValueError(
				f"Invalid `NumericalGrad` value: expected bool, got {kwargs['NumericalGrad']} (type={type(kwargs['NumericalGrad']).__name__})."
			)
	else:
		instance.NumericalGrad = False
		print(f"Parameter `NumericalGrad` not specified - using default value False.")

	instance.SymmetryCheck = False

	if "AutoDiff" not in kwargs:
		if "Grad" not in kwargs:
			instance.GradSym = True
			if "EnergyFunction" in kwargs:
				instance.AutoDiff = True
				print(
					f"Using `EnergyFunction` instead of `Grad` - enabling auto-differentiation mode."
				)
				instance.EnergyFunction = kwargs["EnergyFunction"]
			else:
				raise ValueError(
					"Missing required parameter(s): must provide either `Grad` or `EnergyFunction`."
				)
		else:
			if isfunction(kwargs["Grad"]):
				instance.GradSym = False
				instance.AutoDiff = False
				instance.Grad = kwargs["Grad"]
				instance.NumericalGrad = True
			elif isinstance(kwargs["Grad"], list):
				for list_str in kwargs["Grad"]:
					if not isinstance(list_str, str):
						raise ValueError(
							f"Invalid `Grad` value: expected list of string or callable, got {kwargs['Grad']} (type={type(kwargs['Grad']).__name__})."
						)
				instance.AutoDiff = False
				instance.GradFunction_sympy, instance.GradFunction_numpy = (
					ExactGradAnalysis(instance, kwargs["Grad"])
				)
				instance.SymmetryCheck = True
				instance.GradSym = False
				instance.Grad = lambda x: AutoGrad(instance, x)
			else:
				raise ValueError(
					f"Invalid `Grad` value: expected list of string or callable, got {kwargs['Grad']} (type={type(kwargs['Grad']).__name__})."
				)
	else:
		if isinstance(kwargs["AutoDiff"], bool):
			instance.AutoDiff = kwargs["AutoDiff"]
			if kwargs["AutoDiff"]:
				if "EnergyFunction" not in kwargs:
					raise ValueError(
						"Missing required parameter(s): must provide `EnergyFunction` when `AutoDiff` is enabled."
					)
				else:
					instance.GradSym = True
					instance.EnergyFunction = kwargs["EnergyFunction"]
			else:
				if "Grad" not in kwargs:
					raise ValueError(
						"Missing required parameter(s): must provide `Grad` when `AutoDiff` is disabled."
					)
				else:
					if isfunction(kwargs["Grad"]):
						instance.GradSym = False
						instance.AutoDiff = False
						instance.Grad = kwargs["Grad"]
						instance.NumericalGrad = True
					elif isinstance(kwargs["Grad"], list):
						for list_str in kwargs["Grad"]:
							if not isinstance(list_str, str):
								raise ValueError(
									f"Invalid `Grad` value: expected list of string or callable, got {kwargs['Grad']} (type={type(kwargs['Grad']).__name__})."
								)
						instance.AutoDiff = False
						instance.GradFunction_sympy, instance.GradFunction_numpy = (
							ExactGradAnalysis(instance, kwargs["Grad"])
						)
						instance.Grad = lambda x: AutoGrad(instance, x)
						instance.SymmetryCheck = True
						instance.GradSym = False
					else:
						raise ValueError(
							f"Invalid `Grad` value: expected list of string or callable, got {kwargs['Grad']} (type={type(kwargs['Grad']).__name__})."
						)
		else:
			raise ValueError(
				f"Invalid `AutoDiff` value: expected bool, got {kwargs['AutoDiff']} (type={type(kwargs['AutoDiff']).__name__})."
			)

	# Energy function validation
	if "EnergyFunction" not in kwargs:
		instance.EnergyFunction = None
	else:
		instance.EnergyFunction = kwargs["EnergyFunction"]
		if not isinstance(instance.EnergyFunction, str):
			if isfunction(instance.EnergyFunction):
				instance.EnergyFunctionCal = instance.EnergyFunction
			else:
				raise ValueError(
					f"Invalid `EnergyFunction` value: expected string or callable, got {kwargs['EnergyFunction']} (type={type(kwargs['EnergyFunction']).__name__})."
				)
		else:
			instance.EnergyFunctionSolve = EnergyFunctionAnalysis(instance)
			instance.EnergyFunctionCal = lambda x: EnergyFunctionCalculate(instance, x)

	# AutoGrad if necessary
	if instance.AutoDiff:
		if not isinstance(instance.EnergyFunction, str):
			if isfunction(instance.EnergyFunction):
				instance.Grad = lambda x: AutoGradNum(instance, x)
			else:
				raise ValueError(
					f"Invalid `EnergyFunction` value: expected string or callable, got {kwargs['EnergyFunction']} (type={type(kwargs['EnergyFunction']).__name__})."
				)
		else:
			if instance.NumericalGrad:
				instance.EnergyFunction = instance.EnergyFunctionCal
				instance.Grad = lambda x: AutoGradNum(instance, x)
			else:
				instance.GradFunction_sympy, instance.GradFunction_numpy = (
					AutoDerivative(instance)
				)
				instance.Grad = lambda x: AutoGrad(instance, x)

	# Check and apply default parameters
	param_name_list = [
		"EigenMethod",
		"TimeStep",
		"Momentum",
		"BBStep",
		"MaxIter",
		"DimerLength",
		"Verbose",
		"ReportInterval",
		"Tolerance",
		"Acceleration",
		"NesterovChoice",
		"SearchArea",
		"NesterovRestart",
		"EigenMaxIter",
		"HessianDimerLength",
		"EigenStepSize",
		"ExactHessian",
		"PrecisionTol",
		"EigvecUnified",
	]
	param_value_list = [
		"lobpcg",
		1e-4,
		0.0,
		False,
		1000,
		1e-5,
		False,
		100,
		1e-6,
		"none",
		1,
		1e3,
		None,
		10,
		1e-5,
		1e-5,
		False,
		1e-5,
		False,
	]

	for i in range(len(param_name_list)):
		param_value_aftercheck = auto_checking_parameter(
			instance, param_name_list[i], kwargs, param_value_list[i]
		)
		setattr(instance, f"{param_name_list[i]}", param_value_aftercheck)

	# Initialize additional parameters
	instance.SaddleIndex = 0
	instance.InitialEigenVectors = None
	instance.PrimaryInitialPoint = instance.InitialPoint
	instance.DataBoundary = [
		[instance.InitialPoint[i, 0], instance.InitialPoint[i, 0]]
		for i in range(instance.Dim)
	]

	if instance.NumericalGrad:
		instance.ExactHessian = False

	if "GradientSystem" in kwargs:
		if not isinstance(kwargs["GradientSystem"], bool):
			raise ValueError(
				f"Invalid `GradientSystem` value: expected bool, got {kwargs['GradientSystem']} (type={type(kwargs['GradientSystem']).__name__})."
			)
		else:
			instance.GradientSystem = kwargs["GradientSystem"]
			instance.SymmetryCheck = False
	else:
		print(
			"Parameter 'GradientSystem' not provided. Enabling automatic symmetry detection."
		)

	if "SymmetryCheck" in kwargs:
		if not isinstance(kwargs["SymmetryCheck"], bool):
			raise ValueError(
				f"Invalid `SymmetryCheck` value: expected bool, got {kwargs['SymmetryCheck']} (type={type(kwargs['SymmetryCheck']).__name__})."
			)
		if not kwargs["SymmetryCheck"]:
			instance.SymmetryCheck = False
	else:
		print(
			"Parameter 'SymmetryCheck' not provided. Defaulting to True with automatic detection."
		)
		instance.SymmetryCheck = True

	# Hessian matrix setup
	if instance.SymmetryCheck:
		instance.HessianFunction, instance.GradSym = Hessian_Analysis_withIfsym(
			instance
		)

	if hasattr(instance, "GradientSystem"):
		instance.GradSym = instance.GradientSystem

	if instance.ExactHessian and (not instance.SymmetryCheck):
		instance.HessianFunction = Hessian_Analysis(instance)

	print("\n")

	# Eigenvalue method setup
	if not instance.GradSym:
		print("Non-gradient system detected. Activating GHiSD algorithm.")
		if instance.EigenMethod == "lobpcg":
			print(
				"'lobpcg' incompatible with non-gradient systems. Reverting to 'power' method."
			)
			instance.EigenMethod = "power"
		if instance.EigenMethod == "power":
			if instance.ExactHessian:
				instance.EigVecMethod = (
					lambda x, v, **tempkwargs: power_nonGrad_exacthessian(
						instance, x, v, **tempkwargs
					)
				)
			else:
				instance.EigVecMethod = lambda x, v, **tempkwargs: power_nonGrad(
					instance, x, v, **tempkwargs
				)
		elif instance.EigenMethod == "euler":
			if instance.ExactHessian:
				instance.EigVecMethod = (
					lambda x, v, **tempkwargs: euler_nonGrad_exacthessian(
						instance, x, v, **tempkwargs
					)
				)
			else:
				instance.EigVecMethod = lambda x, v, **tempkwargs: euler_nonGrad(
					instance, x, v, **tempkwargs
				)
	else:
		print("Gradient system detected. Activating HiSD algorithm.")
		if instance.EigenMethod == "power":
			print(
				"'power' incompatible with gradient systems. Reverting to 'lobpcg' method."
			)
			instance.EigenMethod = "lobpcg"
		if instance.EigenMethod == "lobpcg":
			if instance.ExactHessian:
				instance.EigVecMethod = lambda x, v, **tempkwargs: lobpcg_exacthessian(
					instance, x, v, **tempkwargs
				)
			else:
				instance.EigVecMethod = lambda x, v, **tempkwargs: lobpcg(
					instance, x, v, **tempkwargs
				)
		elif instance.EigenMethod == "euler":
			if instance.ExactHessian:
				instance.EigVecMethod = lambda x, v, **tempkwargs: euler_exacthessian(
					instance, x, v, **tempkwargs
				)
			else:
				instance.EigVecMethod = lambda x, v, **tempkwargs: euler(
					instance, x, v, **tempkwargs
				)

	# Set acceleration method
	if instance.Acceleration != "heavyball":
		instance.Momentum = 0.0


def auto_checking_parameter(instance, param_name, kwargs, param_value):
	"""
	Function to check the validity of parameters and returns valid ones, raising errors for invalid inputs.
	"""
	if param_name not in kwargs:
		print(
			f"Parameter `{param_name}` not specified - using default value {param_value}."
		)
		return param_value
	else:
		if param_name == "EigenMethod":
			if kwargs["EigenMethod"] not in ["lobpcg", "euler", "power"]:
				raise ValueError(
					f"Invalid `EigenMethod` value: expected one of 'lobpcg', 'euler' or 'power', got {kwargs['EigenMethod']} (type={type(kwargs['EigenMethod']).__name__})."
				)
			else:
				return kwargs["EigenMethod"]
		if param_name == "Acceleration":
			if kwargs["Acceleration"] not in ["none", "heavyball", "nesterov"]:
				raise ValueError(
					f"Invalid `Acceleration` value: expected one of 'none', 'heavyball' or 'nesterov', got {kwargs['Acceleration']} (type={type(kwargs['Acceleration']).__name__})."
				)
			else:
				return kwargs["Acceleration"]
		if param_name == "TimeStep":
			if isinstance(kwargs["TimeStep"], float) and kwargs["TimeStep"] > 0.0:
				return kwargs["TimeStep"]
			else:
				raise ValueError(
					f"Invalid `TimeStep` value: expected positive float, got {kwargs['TimeStep']} (type={type(kwargs['TimeStep']).__name__})."
				)
		if param_name == "PrecisionTol":
			if (
				isinstance(kwargs["PrecisionTol"], float)
				and kwargs["PrecisionTol"] >= 0.0
			):
				return kwargs["PrecisionTol"]
			else:
				raise ValueError(
					f"Invalid `PrecisionTol` value: expected non-negative float, got {kwargs['PrecisionTol']} (type={type(kwargs['PrecisionTol']).__name__})."
				)
		if param_name == "Momentum":
			if isinstance(kwargs["Momentum"], float) and kwargs["Momentum"] >= 0.0:
				return kwargs["Momentum"]
			else:
				raise ValueError(
					f"Invalid `Momentum` value: expected non-negative float, got {kwargs['Momentum']} (type={type(kwargs['Momentum']).__name__})."
				)
		if param_name == "NesterovChoice":
			if kwargs["NesterovChoice"] in [1, 2]:
				return kwargs["NesterovChoice"]
			else:
				raise ValueError(
					f"Invalid `NesterovChoice` value: expected `1` or `2`, got {kwargs['NesterovChoice']} (type={type(kwargs['NesterovChoice']).__name__})."
				)
		if param_name == "NesterovRestart":
			if (
				isinstance(kwargs["NesterovRestart"], int)
				and kwargs["NesterovRestart"] > 0
			):
				return kwargs["NesterovRestart"]
			else:
				raise ValueError(
					f"Invalid `NesterovRestart` value: expected positive integer, got {kwargs['NesterovRestart']} (type={type(kwargs['NesterovRestart']).__name__})."
				)
		if param_name == "BBStep":
			if isinstance(kwargs["BBStep"], bool):
				return kwargs["BBStep"]
			else:
				raise ValueError(
					f"Invalid `BBStep` value: expected bool, got {kwargs['BBStep']} (type={type(kwargs['BBStep']).__name__})."
				)
		if param_name == "MaxIter":
			if isinstance(kwargs["MaxIter"], int) and kwargs["MaxIter"] > 0:
				return kwargs["MaxIter"]
			else:
				raise ValueError(
					f"Invalid `MaxIter` value: expected positive integer, got {kwargs['MaxIter']} (type={type(kwargs['MaxIter']).__name__})."
				)
		if param_name == "EigenMaxIter":
			if isinstance(kwargs["EigenMaxIter"], int) and kwargs["EigenMaxIter"] > 0:
				return kwargs["EigenMaxIter"]
			else:
				raise ValueError(
					f"Invalid `EigenMaxIter` value: expected positive integer, got {kwargs['EigenMaxIter']} (type={type(kwargs['EigenMaxIter']).__name__})."
				)
		if param_name == "HessianDimerLength":
			if (
				isinstance(kwargs["HessianDimerLength"], float)
				and kwargs["HessianDimerLength"] > 0
			):
				return kwargs["HessianDimerLength"]
			else:
				raise ValueError(
					f"Invalid `HessianDimerLength` value: expected positive float, got {kwargs['HessianDimerLength']} (type={type(kwargs['HessianDimerLength']).__name__})."
				)
		if param_name == "EigenStepSize":
			if (
				isinstance(kwargs["EigenStepSize"], float)
				and kwargs["EigenStepSize"] > 0
			):
				return kwargs["EigenStepSize"]
			else:
				raise ValueError(
					f"Invalid `EigenStepSize` value: expected positive float, got {kwargs['EigenStepSize']} (type={type(kwargs['EigenStepSize']).__name__})."
				)
		if param_name == "DimerLength":
			if isinstance(kwargs["DimerLength"], float) and kwargs["DimerLength"] > 0:
				return kwargs["DimerLength"]
			else:
				raise ValueError(
					f"Invalid `DimerLength` value: expected positive float, got {kwargs['DimerLength']} (type={type(kwargs['DimerLength']).__name__})."
				)
		if param_name == "Verbose":
			if isinstance(kwargs["Verbose"], bool):
				return kwargs["Verbose"]
			else:
				raise ValueError(
					f"Invalid `Verbose` value: expected bool, got {kwargs['Verbose']} (type={type(kwargs['Verbose']).__name__})."
				)
		if param_name == "ReportInterval":
			if (
				isinstance(kwargs["ReportInterval"], int)
				and kwargs["ReportInterval"] > 0
			):
				return kwargs["ReportInterval"]
			else:
				raise ValueError(
					f"Invalid `ReportInterval` value: expected positive integer, got {kwargs['ReportInterval']} (type={type(kwargs['ReportInterval']).__name__})."
				)
		if param_name == "Tolerance":
			if isinstance(kwargs["Tolerance"], float) and kwargs["Tolerance"] > 0:
				return kwargs["Tolerance"]
			else:
				raise ValueError(
					f"Invalid `Tolerance` value: expected positive float, got {kwargs['Tolerance']} (type={type(kwargs['Tolerance']).__name__})."
				)
		if param_name == "SearchArea":
			if isinstance(kwargs["SearchArea"], float) and kwargs["SearchArea"] > 0:
				return kwargs["SearchArea"]
			else:
				raise ValueError(
					f"Invalid `SearchArea` value: expected positive float, got {kwargs['SearchArea']} (type={type(kwargs['SearchArea']).__name__})."
				)
		if param_name == "ExactHessian":
			if isinstance(kwargs["ExactHessian"], bool):
				return kwargs["ExactHessian"]
			else:
				raise ValueError(
					f"Invalid `ExactHessian` value: expected bool, got {kwargs['ExactHessian']} (type={type(kwargs['ExactHessian']).__name__})."
				)
		if param_name == "EigvecUnified":
			if isinstance(kwargs["EigvecUnified"], bool):
				return kwargs["EigvecUnified"]
			else:
				raise ValueError(
					f"Invalid `EigvecUnified` value: expected bool, got {kwargs['EigvecUnified']} (type={type(kwargs['EigvecUnified']).__name__})."
				)
