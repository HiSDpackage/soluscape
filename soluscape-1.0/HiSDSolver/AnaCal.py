# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings
import sympy
from sympy import *

warnings.filterwarnings("ignore")


def EnergyFunctionAnalysis(instance):
	"""
	Function to analyze the energy function using symbolic tools.
	"""
	N = instance.Dim
	FunctionString = instance.EnergyFunction
	for i in range(N):
		code = "x{0} = sympy.Symbol('x{0}')"
		exec(
			code.format(i + 1)
		)  # Dynamically create symbolic variables (x1, x2, ..., xN)
	Y = FunctionString

	# Create a list of symbolic variables
	vars = sympy.symbols(" ".join([f"x{i + 1}" for i in range(N)]))
	# Convert the symbolic energy function to a numerical function using lambdify
	lambdified_energy = sympy.lambdify(vars, Y, "numpy")
	return lambdified_energy


def EnergyFunctionCalculate(instance, x):
	"""
	Function to calculate energy based on input vector x using the predefined energy function.
	"""
	x = x.reshape(
		-1,
	)
	energyfunc = instance.EnergyFunctionSolve
	output = energyfunc(*x)
	return output


def AutoDerivative(instance):
	"""
	Function for automatic differentiation using symbolic tools.
	"""
	N = instance.Dim
	FunctionString = instance.EnergyFunction
	output = [0 for i in range(N)]
	code = """
for i in range({0}):
	codeinside = "x{{0}} = sympy.Symbol('x{{0}}')"
	exec(codeinside.format(i+1))
Y = {1}
for i in range({0}):
	codeinside = "output[i] = sympy.diff(Y, x{{0}})"
	exec(codeinside.format(i+1))
	"""
	exec(
		code.format(N, FunctionString)
	)  # Execute the code for symbolic differentiation
	vars = sympy.symbols(" ".join([f"x{i + 1}" for i in range(N)]))
	# Lambdify the list of symbolic derivatives into numerical functions
	lambdified_output = [
		sympy.lambdify(vars, grad_expr, "numpy") for grad_expr in output
	]
	return output, lambdified_output


def AutoGrad(instance, x):
	"""
	Function to calculate the gradient using the predefined lambdified gradient functions.
	"""
	x = x.reshape(
		-1,
	)
	grad = [lambdified_grad(*x) for lambdified_grad in instance.GradFunction_numpy]
	return np.array(grad).reshape(-1, 1)  # Return the gradient as a column vector


def ExactGradAnalysis(instance, Gradstrlist):
	"""
	Function to analyze gradients using a list of gradient expressions.
	"""
	N = instance.Dim
	for i in range(N):
		code = "x{0} = sympy.Symbol('x{0}')"
		exec(code.format(i + 1))
	vars = sympy.symbols(" ".join([f"x{i + 1}" for i in range(N)]))
	output = []
	for i in range(N):
		Y = Gradstrlist[i]
		output.append(Y)

	# Lambdify the list of symbolic gradients into numerical functions
	lambdified_output = [
		sympy.lambdify(vars, grad_expr, "numpy") for grad_expr in output
	]
	return output, lambdified_output


def AutoGradNum(instance, x):
	"""
	Function to compute gradients numerically using finite differences
	"""
	L = instance.DimerLength
	N = instance.Dim

	x = x.reshape(
		-1,
	)

	# Create a matrix for perturbations (increment of L along each axis)
	delta = np.zeros((N, N), dtype=np.float64)
	np.fill_diagonal(delta, L)

	xup = x + delta
	xdown = x - delta

	# Use map to calculate the energy for perturbed x values
	energy_up = np.array(list(map(instance.EnergyFunction, xup)))
	energy_down = np.array(list(map(instance.EnergyFunction, xdown)))

	# Compute the gradient using the finite difference formula
	grad = (energy_up - energy_down) / (2 * L)

	return grad.reshape(-1, 1)
