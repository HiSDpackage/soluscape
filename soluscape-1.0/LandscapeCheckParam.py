# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings
from inspect import isfunction
from HiSDSolver import HiSDSolver
from Perturbation import *

warnings.filterwarnings("ignore")


def LandscapeCheckParam(instance, **kwargs):
	print("HiSD Solver Configuration:\n" + "-" * 30)
	print("[HiSD] Current parameters (initialized):")
	instance.calHiSD = HiSDSolver.Solver(
		**kwargs
	)  # Generate a solver to find a saddle point
	instance.Dim = instance.calHiSD.Dim
	instance.InitialPoint = instance.calHiSD.InitialPoint + 1e-3
	instance.calHiSD.InitialPoint = instance.calHiSD.InitialPoint + 1e-3
	instance.SearchArea = instance.calHiSD.SearchArea
	instance.SaddleList = []
	instance.DetailRecord = []
	instance.saddleind = 0
	instance.GapAllowed = 1e-3
	instance.BeginID = -1
	instance.Continue = False
	print("\n")
	print("Landscape Configuration:\n" + "-" * 30)
	print("[Landscape] Current parameters (initialized):")
	param_name_list = [
		"MaxIndex",
		"SameJudgementMethod",
		"PerturbationMethod",
		"PerturbationRadius",
		"InitialEigenVectors",
		"PerturbationNumber",
		"SaveTrajectory",
		"MaxIndexGap",
		"EigenCombination",
	]
	param_value_list = [
		6,
		lambda a, b: SameJudgeTwoNorm(instance, a, b),
		"uniform",
		1e-4,
		None,
		2,
		True,
		1,
		"all",
	]
	for i in range(len(param_name_list)):
		param_value_aftercheck = auto_checking_parameter(
			instance, param_name_list[i], kwargs, param_value_list[i]
		)
		setattr(instance, f"{param_name_list[i]}", param_value_aftercheck)
	if instance.PerturbationMethod == "gaussian":
		instance.PerMethod = gaussianper
	elif instance.PerturbationMethod == "uniform":
		instance.PerMethod = uniformper


def auto_checking_parameter(instance, param_name, kwargs, param_value):
	"""
	Validate and return the appropriate parameter value.
	"""
	if param_name not in kwargs:
		print(
			f"Parameter `{param_name}` not specified - using default value {param_value}."
		)
		return param_value
	else:
		if param_name == "MaxIndex":
			if isinstance(kwargs["MaxIndex"], int) and kwargs["MaxIndex"] >= 0:
				if kwargs["MaxIndex"] > instance.Dim:
					print(
						f"[Config Sync] `MaxIndex` ({kwargs['MaxIndex']}) exceeds problem dimension {instance.Dim}. Using dimension as upper bound."
					)
					return instance.Dim
				else:
					return kwargs["MaxIndex"]
			else:
				raise ValueError(
					f"Invalid `MaxIndex` value: expected non-negative integer, got {kwargs['MaxIndex']} (type={type(kwargs['MaxIndex']).__name__})."
				)
		if param_name == "InitialEigenVectors":
			tempv0 = np.array(kwargs["InitialEigenVectors"])
			if (
				tempv0.ndim > 2
				or tempv0.shape[0] != instance.Dim
				or tempv0.shape[1] != instance.MaxIndex
			):
				raise ValueError(
					f"Invalid `InitialEigenVectors` value: expected (d, k)-shaped matrix, got {kwargs['InitialEigenVectors']} (type={type(kwargs['InitialEigenVectors']).__name__})."
					f"where d = {instance.Dim} (problem dimension) and k = {instance.MaxIndex} (MaxIndex). "
				)
			return tempv0
		if param_name == "SameJudgementMethod":
			if (
				isinstance(kwargs["SameJudgementMethod"], float)
				and kwargs["SameJudgementMethod"] >= 0.0
			):
				instance.GapAllowed = kwargs["SameJudgementMethod"]
				return lambda a, b: SameJudgeTwoNorm(instance, a, b)
			elif isfunction(kwargs["SameJudgementMethod"]):
				return kwargs["SameJudgementMethod"]
			else:
				raise ValueError(
					f"Invalid `SameJudgementMethod` value: expected non-negative float or callable, got {kwargs['SameJudgementMethod']} (type={type(kwargs['SameJudgementMethod']).__name__})."
				)
		if param_name == "PerturbationRadius":
			if (
				isinstance(kwargs["PerturbationRadius"], float)
				and kwargs["PerturbationRadius"] > 0
			):
				# Check for positive real number
				return kwargs["PerturbationRadius"]
			else:
				raise ValueError(
					f"Invalid `PerturbationRadius` value: expected positive float, got {kwargs['PerturbationRadius']} (type={type(kwargs['PerturbationRadius']).__name__})."
				)
		if param_name == "PerturbationMethod":
			if kwargs["PerturbationMethod"] not in ["gaussian", "uniform"]:
				raise ValueError(
					f"Invalid `PerturbationMethod` value: expected one of 'gaussian' or 'uniform', got {kwargs['PerturbationMethod']} (type={type(kwargs['PerturbationMethod']).__name__})."
				)
			else:
				return kwargs["PerturbationMethod"]
		if param_name == "PerturbationNumber":
			if (
				isinstance(kwargs["PerturbationNumber"], int)
				and kwargs["PerturbationNumber"] >= 0
			):
				return kwargs["PerturbationNumber"]
			else:
				raise ValueError(
					f"Invalid `PerturbationNumber` value: expected non-negative integer, got {kwargs['PerturbationNumber']} (type={type(kwargs['PerturbationNumber']).__name__})."
				)
		if param_name == "EigenCombination":
			if kwargs["EigenCombination"] not in ["all", "min"]:
				raise ValueError(
					f"Invalid `EigenCombination` value: expected one of 'all' or 'min', got {kwargs['EigenCombination']} (type={type(kwargs['EigenCombination']).__name__})."
				)
			else:
				return kwargs["EigenCombination"]
		if param_name == "MaxIndexGap":
			if isinstance(kwargs["MaxIndexGap"], int) and kwargs["MaxIndexGap"] > 0:
				return kwargs["MaxIndexGap"]
			else:
				raise ValueError(
					f"Invalid `MaxIndexGap` value: expected positive integer, got {kwargs['MaxIndexGap']} (type={type(kwargs['MaxIndexGap']).__name__})."
				)


def SameJudgeTwoNorm(instance, a, b):
	"""
	Check if two vectors are sufficiently close based on the 2-norm.
	"""
	return np.linalg.norm(a - b) < instance.GapAllowed
