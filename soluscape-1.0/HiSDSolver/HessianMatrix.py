# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings
import sympy

warnings.filterwarnings("ignore")


def SingleHessianVectorProduct(instance, x, v):
	"""
	Function to compute the Hessian-Vector Product using the central finite difference method.
	"""
	L = instance.HessianDimerLength
	x = x.reshape(
		-1,
	)
	v = v.reshape(
		-1,
	)
	return ((instance.Grad(x + L * v) - instance.Grad(x - L * v)) / (2.0 * L)).reshape(
		-1,
	)


def BatchHessianVectorProduct(instance, x, v):
	"""
	Function to compute Hessian-Vector Products for a batch of vectors.
	"""
	hvp = lambda z: SingleHessianVectorProduct(instance, x, z)
	hvpmat = map(hvp, list(np.transpose(v)))
	result = []
	for item in hvpmat:
		result.append(item)
	output = np.array(result)
	return np.transpose(output)  # Return the result with the original shape


def Hessian(instance, x):
	"""
	Compute the Hessian matrix for gradient systems or Jacobi matrix for non-gradient systems.
	"""
	N = instance.Dim
	if instance.ExactHessian:
		return Hessian_exact(instance, x)
	else:
		return BatchHessianVectorProduct(instance, x, np.eye(N))


def Hessian_Analysis_withIfsym(instance):
	"""
	Function to analyze the Hessian matrix with symmetry check.
	"""
	N = instance.Dim
	Gradlist = instance.GradFunction_sympy
	vars = sympy.symbols(" ".join([f"x{i + 1}" for i in range(N)]))
	testsymmatrix = []
	HessianMatrix = []
	for i in range(N):
		row = []
		testrow = []
		for j in range(N):
			second_derivative = sympy.diff(Gradlist[i], sympy.symbols(f"x{j + 1}"))
			testrow.append(second_derivative)
			row.append(sympy.lambdify(vars, second_derivative, "numpy"))
		HessianMatrix.append(row)
		testsymmatrix.append(testrow)

	issym = True
	# Check if the Hessian matrix is symmetric by comparing off-diagonal elements
	for i in range(N):
		for j in range(i):
			temp = testsymmatrix[i][j].equals(testsymmatrix[j][i])
			issym = issym and temp
			if not issym:
				break
		if not issym:
			break
	return HessianMatrix, issym  # Return the Hessian matrix and the symmetry flag


def Hessian_Analysis(instance):
	"""
	Function to compute the Hessian matrix without symmetry check.
	"""
	N = instance.Dim
	Gradlist = instance.GradFunction_sympy
	vars = sympy.symbols(" ".join([f"x{i + 1}" for i in range(N)]))
	HessianMatrix = []
	for i in range(N):
		row = []
		for j in range(N):
			# Compute the second derivative (Hessian) for each gradient
			second_derivative = sympy.diff(Gradlist[i], sympy.symbols(f"x{j + 1}"))
			row.append(sympy.lambdify(vars, second_derivative, "numpy"))
		HessianMatrix.append(row)
	return HessianMatrix


def Hessian_exact(instance, x):
	"""
	Function to compute the exact Hessian matrix from a pre-defined function.
	"""
	N = instance.Dim
	HessianExpression = instance.HessianFunction
	x = x.reshape(
		-1,
	)
	hessian_value = np.array(
		[[HessianExpression[i][j](*x) for j in range(N)] for i in range(N)]
	)
	return hessian_value
