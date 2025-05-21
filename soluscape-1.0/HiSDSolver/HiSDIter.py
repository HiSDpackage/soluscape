# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import copy
import warnings
from .EigMethod import *

warnings.filterwarnings("ignore")


def HiSDInitialization(instance):
	"""
	Function for initializing variables for HiSD method.
	"""
	x = copy.deepcopy(instance.InitialPoint)
	x_pre = copy.deepcopy(instance.InitialPoint)
	if instance.InitialEigenVectors is not None:
		v = np.array(
			copy.deepcopy(instance.InitialEigenVectors)
		)  # Use provided eigenvectors
	else:
		v = GiveEigenvector(instance, x, instance.SaddleIndex)  # Compute eigenvector
	if v.ndim == 1:
		v = v.reshape(-1, 1)
	return x, x_pre, v


def HiSDIteration(instance):
	"""
	Main iteration for HiSD method for high-index saddle points.
	"""
	boundarytempsave = copy.deepcopy(instance.DataBoundary)
	xini = instance.PrimaryInitialPoint.reshape(
		-1,
	)
	tau = 0.5
	x = instance.x
	x_pre = instance.x_pre
	v = instance.v
	WhetherBB = instance.BBStep
	mom = instance.Momentum
	dt = instance.TimeStep
	x_record = copy.deepcopy(x.reshape(1, instance.Dim))
	gnorm_record = []
	timestep_record = [0]
	g = instance.Grad(x)
	gnorm_record.append(np.linalg.norm(g))

	# Check if Nesterov acceleration is used
	if instance.Acceleration == "nesterov":
		if instance.NesterovChoice == 2:
			NesterovTheta = 1
			NesterovTheta = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
		elif instance.NesterovChoice == 1:
			if instance.NesterovRestart is not None:
				plusbase = 0

		# Main iteration loop
		for j in range(1, instance.MaxIter + 1):
			if WhetherBB and j > 1:
				dt = BBStepSize(x, x_pre, g, g_pre, tau)
			timestep_record.append(dt)
			if instance.NesterovChoice == 2:
				NesterovThetaNew = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
				NesterovGamma = (NesterovTheta - 1) / NesterovThetaNew
				NesterovTheta = NesterovThetaNew
			elif instance.NesterovChoice == 1:
				if instance.NesterovRestart is not None:
					NesterovGamma = (j - plusbase) / (j - plusbase + 3)
				else:
					NesterovGamma = j / (j + 3)
			w_temp = x + NesterovGamma * (x - x_pre)
			gw = instance.Grad(w_temp)
			dxw = dt * (gw - 2.0 * np.matmul(v, np.matmul(v.T, gw)))
			x_temp = w_temp - dxw
			x_pre = x
			x = x_temp
			if WhetherBB:
				g_pre = g
			v, whetherkindex = instance.EigVecMethod(x, v)
			g = instance.Grad(x)
			if instance.Verbose:
				if j % instance.ReportInterval == 0:
					print(
						"Iteration: "
						+ str(j)
						+ f"|| Norm of gradient: {np.linalg.norm(g):.6f}"
					)
			xnow = x.reshape(
				-1,
			)
			x_record = np.append(x_record, x.reshape(1, instance.Dim), axis=0)
			if np.linalg.norm(xnow - xini) > instance.SearchArea:
				print(
					"[WARNING] Iteration diverged: Search point exceeds feasible region. Skipping to next search."
				)
				instance.flag = False
				instance.DataBoundary = boundarytempsave
				return
			instance.DataBoundary = [
				[
					min(instance.DataBoundary[i][0], x[i, 0]),
					max(instance.DataBoundary[i][1], x[i, 0]),
				]
				for i in range(instance.Dim)
			]
			gnorm_record.append(np.linalg.norm(g))
			if np.linalg.norm(g) < instance.Tolerance:
				if whetherkindex:
					break
				if j==1 or gnorm_record[-2]>=instance.Tolerance:
					whetherk = CheckIndexk(instance, x, instance.SaddleIndex)
					if whetherk:
						break
			if instance.NesterovRestart is not None:
				if j % instance.NesterovRestart == 0:
					if instance.NesterovChoice == 2:
						NesterovTheta = 1
						NesterovTheta = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
					elif instance.NesterovChoice == 1:
						plusbase = j
	else:
		for j in range(1, instance.MaxIter + 1):
			if WhetherBB and j > 1:
				dt = BBStepSize(x, x_pre, g, g_pre, tau)
			timestep_record.append(dt)
			dx = dt * (g - 2.0 * np.matmul(v, np.matmul(v.T, g)))
			x_temp = x - dx + mom * (x - x_pre)
			x_pre = x
			x = x_temp
			if WhetherBB:
				g_pre = g
			v, whetherkindex = instance.EigVecMethod(x, v)
			g = instance.Grad(x)
			if instance.Verbose:
				if j % instance.ReportInterval == 0:
					print(
						"Iteration: "
						+ str(j)
						+ f"|| Norm of gradient: {np.linalg.norm(g):.6f}"
					)
			xnow = x.reshape(
				-1,
			)
			x_record = np.append(x_record, x.reshape(1, instance.Dim), axis=0)
			if np.linalg.norm(xnow - xini) > instance.SearchArea:
				print(
					"[WARNING] Iteration diverged: Search point exceeds feasible region. Skipping to next search."
				)
				instance.flag = False
				instance.DataBoundary = boundarytempsave
				return
			instance.DataBoundary = [
				[
					min(instance.DataBoundary[i][0], x[i, 0]),
					max(instance.DataBoundary[i][1], x[i, 0]),
				]
				for i in range(instance.Dim)
			]
			gnorm_record.append(np.linalg.norm(g))
			if np.linalg.norm(g) < instance.Tolerance:
				if whetherkindex:
					break
				if j == 1 or gnorm_record[-2] >= instance.Tolerance:
					whetherk = CheckIndexk(instance, x, instance.SaddleIndex)
					if whetherk:
						break

	# Check for convergence and report results
	if j == instance.MaxIter:
		if gnorm_record[-1] >= instance.Tolerance:
			print(
				"[WARNING] Iteration not converged: Maximum iterations reached without convergence. Skipping to next search."
			)
			instance.flag = False
			instance.DataBoundary = boundarytempsave
			return
		negnum, zeronum, posnum, negvecs = FindIndex(instance, x)
		if negnum+zeronum >= instance.SaddleIndex:
			print(
				"[Note] Due to eigenvalue approximation inaccuracies during iterations, "
				"the search trajectory may reach a qualifying saddle point without triggering a report."
			)
		else:
			print(
				"[WARNING] Iteration not converged: Maximum iterations reached without convergence. Skipping to next search."
			)
			instance.flag = False
			instance.DataBoundary = boundarytempsave
			return
	else:
		negnum, zeronum, posnum, negvecs = FindIndex(instance, x)
	if zeronum != 0:
		print(
			f"[WARNING] Degenerate saddle point detected under precision tol={instance.PrecisionTol}: Hessian matrix may contain zero eigenvalue(s)."
		)
		print(
			f"Eigenvalue spectrum: negative={negnum}, zero={zeronum}, positive={posnum}. "
		)
	else:
		print(
			f"Non-degenerate saddle point identified: Morse index ={negnum} (number of negative eigenvalues)."
		)
	instance.finalindex = int(negnum)
	instance.negvecs = negvecs
	instance.IterNum = j
	instance.x = x
	instance.x_record = x_record
	instance.timestep_record = np.array(timestep_record).reshape(-1, 1)
	instance.timestep_record = np.cumsum(instance.timestep_record)
	instance.gnorm_record = gnorm_record


def SDIteration(instance):
	"""
	Main iteration for HiSD method for index-0 saddle points.
	"""
	xini = instance.PrimaryInitialPoint.reshape(
		-1,
	)
	boundarytempsave = copy.deepcopy(instance.DataBoundary)
	tau = 0.5
	x = instance.x
	x_pre = instance.x_pre
	WhetherBB = instance.BBStep
	mom = instance.Momentum
	dt = instance.TimeStep
	x_record = copy.deepcopy(x.reshape(1, instance.Dim))
	gnorm_record = []
	timestep_record = [0]
	g = instance.Grad(x)
	gnorm_record.append(np.linalg.norm(g))

	# Check if Nesterov acceleration is used
	if instance.Acceleration == "nesterov":
		if instance.NesterovChoice == 2:
			NesterovTheta = 1
			NesterovTheta = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
		elif instance.NesterovChoice == 1:
			if instance.NesterovRestart is not None:
				plusbase = 0

		# Main iteration loop
		for j in range(1, instance.MaxIter + 1):
			if WhetherBB and j > 1:
				dt = BBStepSize(x, x_pre, g, g_pre, tau)
			timestep_record.append(dt)
			if instance.NesterovChoice == 2:
				NesterovThetaNew = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
				NesterovGamma = (NesterovTheta - 1) / NesterovThetaNew
				NesterovTheta = NesterovThetaNew
			elif instance.NesterovChoice == 1:
				if instance.NesterovRestart is not None:
					NesterovGamma = (j - plusbase) / (j - plusbase + 3)
				else:
					NesterovGamma = j / (j + 3)
			w_temp = x + NesterovGamma * (x - x_pre)
			gw = instance.Grad(w_temp)
			dxw = dt * gw
			x_temp = w_temp - dxw
			x_pre = x
			x = x_temp
			if WhetherBB:
				g_pre = g
			g = instance.Grad(x)
			if instance.Verbose:
				if j % instance.ReportInterval == 0:
					print(
						"Iteration: "
						+ str(j)
						+ f"|| Norm of gradient: {np.linalg.norm(g):.6f}"
					)
			xnow = x.reshape(
				-1,
			)
			x_record = np.append(x_record, x.reshape(1, instance.Dim), axis=0)
			if np.linalg.norm(xnow - xini) > instance.SearchArea:
				print(
					"[WARNING] Iteration diverged: Search point exceeds feasible region. Skipping to next search."
				)
				instance.flag = False
				instance.DataBoundary = boundarytempsave
				return
			instance.DataBoundary = [
				[
					min(instance.DataBoundary[i][0], x[i, 0]),
					max(instance.DataBoundary[i][1], x[i, 0]),
				]
				for i in range(instance.Dim)
			]
			gnorm_record.append(np.linalg.norm(g))
			if np.linalg.norm(g) < instance.Tolerance:
				break
			if instance.NesterovRestart is not None:
				if j % instance.NesterovRestart == 0:
					if instance.NesterovChoice == 2:
						NesterovTheta = 1
						NesterovTheta = (1 + (1 + 4 * NesterovTheta**2) ** (1 / 2)) / 2
					elif instance.NesterovChoice == 1:
						plusbase = j
	else:
		for j in range(1, instance.MaxIter + 1):
			if WhetherBB and j > 1:
				dt = BBStepSize(x, x_pre, g, g_pre, tau)
			timestep_record.append(dt)
			dx = dt * g
			x_temp = x - dx + mom * (x - x_pre)
			x_pre = x
			x = x_temp
			if WhetherBB:
				g_pre = g
			g = instance.Grad(x)
			if instance.Verbose:
				if j % instance.ReportInterval == 0:
					print(
						"Iteration: "
						+ str(j)
						+ f"|| Norm of gradient: {np.linalg.norm(g):.6f}"
					)
			xnow = x.reshape(
				-1,
			)
			x_record = np.append(x_record, x.reshape(1, instance.Dim), axis=0)
			if np.linalg.norm(xnow - xini) > instance.SearchArea:
				print(
					"[WARNING] Iteration diverged: Search point exceeds feasible region. Skipping to next search."
				)
				instance.flag = False
				instance.DataBoundary = boundarytempsave
				return
			gnorm_record.append(np.linalg.norm(g))
			instance.DataBoundary = [
				[
					min(instance.DataBoundary[i][0], x[i, 0]),
					max(instance.DataBoundary[i][1], x[i, 0]),
				]
				for i in range(instance.Dim)
			]
			if np.linalg.norm(g) < instance.Tolerance:
				break
	if j == instance.MaxIter:
		print(
			"[WARNING] Iteration not converged: Maximum iterations reached without convergence. Skipping to next search."
		)
		instance.flag = False
		instance.DataBoundary = boundarytempsave
		return
	negnum, zeronum, posnum, negvecs = FindIndex(instance, x)
	if zeronum != 0:
		print(
			f"[WARNING] Degenerate saddle point detected under precision tol={instance.PrecisionTol}: Hessian matrix may contain zero eigenvalue(s)."
		)
		print(
			f"Eigenvalue spectrum: negative={negnum}, zero={zeronum}, positive={posnum}. "
		)
	else:
		print(
			f"Non-degenerate saddle point identified: Morse index ={negnum} (number of negative eigenvalues)."
		)
	instance.finalindex = int(negnum)
	instance.negvecs = negvecs
	instance.IterNum = j
	instance.x = x
	instance.x_record = x_record
	instance.timestep_record = np.array(timestep_record).reshape(-1, 1)
	instance.timestep_record = np.cumsum(instance.timestep_record)
	instance.gnorm_record = gnorm_record


def BBStepSize(x, x_pre, g, g_pre, tau=0.5):
	"""
	Step size update using BB method.
	"""
	dx = x - x_pre
	dg = g - g_pre
	bb_2 = np.abs((dx * dg).sum() / (dg * dg).sum())
	dt = np.min(np.array([bb_2, tau / np.sqrt((dg * dg).sum())]))
	return dt
