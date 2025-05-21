# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import scipy
import scipy.sparse.linalg as linalg
import warnings
from .HessianMatrix import *

warnings.filterwarnings("ignore")


def lobpcg(instance, x, v, **kwargs):
	"""
	Function implementing the LOBPCG (Locally Optimal Block Preconditioned Conjugate Gradient) algorithm.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	N = instance.Dim

	# Define matrix-vector and matrix-matrix multiplication functions
	matvec_fun = lambda z: SingleHessianVectorProduct(instance, x, z)
	matmat_fun = lambda z: BatchHessianVectorProduct(instance, x, z)
	H = linalg.LinearOperator(shape=(N, N), matvec=matvec_fun, matmat=matmat_fun)
	v = v.reshape(N, instance.SaddleIndex)
	values, vectors = linalg.lobpcg(A=H, X=v, maxiter=max_iter, largest=False)
	whetherkindex = True
	if values[-1] >= eps:
		whetherkindex = False
	return vectors, whetherkindex


def lobpcg_exacthessian(instance, x, v, **kwargs):
	"""
	Function using exact Hessian for LOBPCG.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	N = instance.Dim
	H = Hessian(instance, x)  # Exact Hessian matrix
	v = v.reshape(N, instance.SaddleIndex)
	values, vectors = linalg.lobpcg(A=H, X=v, maxiter=max_iter, largest=False)
	whetherkindex = True
	if values[-1] >= eps:
		whetherkindex = False
	return vectors, whetherkindex


def euler(instance, x, v, **kwargs):
	"""
	Explicit Euler method for solving eigenvalue problem (non-exact Hessian).
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	for _ in range(max_iter):
		hv = BatchHessianVectorProduct(instance, x, v)
		coef = np.triu(v.T @ hv)
		v -= (hv - v * np.diag(coef) - 2.0 * v @ np.triu(coef, k=1)) * ds
		v, _ = np.linalg.qr(v)
	hv = BatchHessianVectorProduct(instance, x, v)
	values = np.diag(v.T @ hv)
	# Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def euler_exacthessian(instance, x, v, **kwargs):
	"""
	Explicit Euler method with exact Hessian.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	H = Hessian(instance, x)
	for _ in range(max_iter):
		hv = np.dot(H, v)
		coef = np.triu(v.T @ hv)
		v -= (hv - v * np.diag(coef) - 2.0 * v @ np.triu(coef, k=1)) * ds
		v, _ = np.linalg.qr(v)
	hv = np.dot(H, v)
	values = np.diag(v.T @ hv)  # Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def euler_nonGrad(instance, x, v, **kwargs):
	"""
	Explicit Euler method for non-gradient systems.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	for _ in range(max_iter):
		hv = BatchHessianVectorProduct(instance, x, v)
		coef = v.T @ hv
		v -= (hv - v * np.diag(coef) - v @ np.triu(coef + coef.T, k=1)) * ds
		v, _ = np.linalg.qr(v)
	hv = BatchHessianVectorProduct(instance, x, v)
	values = np.diag(v.T @ hv)
	# Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def euler_nonGrad_exacthessian(instance, x, v, **kwargs):
	"""
	Explicit Euler method with exact Hessian for non-gradient systems.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	H = Hessian(instance, x)
	for _ in range(max_iter):
		hv = np.dot(H, v)
		coef = v.T @ hv
		v -= (hv - v * np.diag(coef) - v @ np.triu(coef + coef.T, k=1)) * ds
		v, _ = np.linalg.qr(v)
	hv = np.dot(H, v)
	values = np.diag(v.T @ hv)
	# Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def power_nonGrad(instance, x, v, **kwargs):
	"""
	Power iteration method for non-gradient systems.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	for _ in range(max_iter):
		hv = BatchHessianVectorProduct(instance, x, v)
		v -= hv * ds
		v, _ = np.linalg.qr(v)
	hv = BatchHessianVectorProduct(instance, x, v)
	values = np.diag(v.T @ hv)
	# Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def power_nonGrad_exacthessian(instance, x, v, **kwargs):
	"""
	Power iteration method with exact Hessian for non-gradient systems.
	"""
	eps = instance.PrecisionTol
	if "max_iter" not in kwargs:
		max_iter = instance.EigenMaxIter
	ds = instance.EigenStepSize
	H = Hessian(instance, x)
	for _ in range(max_iter):
		hv = np.dot(H, v)
		v -= hv * ds
		v, _ = np.linalg.qr(v)
	hv = np.dot(H, v)
	values = np.diag(v.T @ hv)
	# Calculate the eigenvalues
	whetherkindex = True
	if max(values) >= eps:
		whetherkindex = False
	return v, whetherkindex


def GiveEigenvector(instance, x, k):
	"""
	Function to compute the first k eigenvectors of the Hessian matrix.
	"""
	H = Hessian(instance, x)
	eigenvalues, eigenvectors = np.linalg.eigh((H + np.transpose(H)) / 2.0)  # To calculate the eigen pairs of symmetric part
	if instance.EigvecUnified:
		eigenvalues, eigenvectors = CanonicalizeEigens(eigenvalues, eigenvectors, k)
	order = np.argsort(eigenvalues)
	eigenvectors = eigenvectors[:, order]
	return eigenvectors[:, 0:k]


def CheckIndexk(instance, x, k):
	"""
	Function to check whether Hessian(x) has at least k negative and zero eigenvalues.
	"""
	eps = instance.PrecisionTol  # Consider the absolute eigenvalues smaller than this as zero
	H = Hessian(instance, x)
	if k == instance.Dim:
		if instance.GradSym:
			eigenvalues = scipy.linalg.eigvalsh((H + np.transpose(H)) / 2.0, subset_by_index = [0, k-1], driver='evr')
		else:
			eigenvalues = scipy.linalg.eigvals(H)
	else:
		if instance.GradSym:
			eigenvalues,_ = scipy.sparse.linalg.eigsh((H + np.transpose(H)) / 2.0, k=k, which='SR')
		else:
			eigenvalues,_ = scipy.sparse.linalg.eigs(H, k=k, which='SR')
	eigenvalues = np.sort(np.real(eigenvalues))
	if eigenvalues[k-1]<eps:
		return True
	else:
		return False


def FindIndex(instance, x):
	"""
	Function to find indices of negative, positive, and zero eigenvalues.
	"""
	eps = instance.PrecisionTol  # Consider the absolute eigenvalues smaller than this as zero
	H = Hessian(instance, x)
	if instance.GradSym:
		eigenvalues, eigenvectors = np.linalg.eigh((H + np.transpose(H)) / 2.0)
	else:
		eigenvalues, eigenvectors = np.linalg.eig(H)
		eigenvalues = np.real(eigenvalues)
		eigenvectors = np.real(eigenvectors)
	negativenum = np.sum(eigenvalues < -eps)
	positivenum = np.sum(eigenvalues > eps)
	zeronum = instance.Dim - negativenum - positivenum
	negative_indices = np.where(eigenvalues < -eps)[0]
	negativevectors = eigenvectors[:, negative_indices]
	if instance.EigvecUnified and int(negativenum) > 0:
		_, negativevectors = CanonicalizeEigens(eigenvalues[negative_indices], negativevectors, int(negativenum))
	return negativenum, zeronum, positivenum, negativevectors


def CanonicalizeEigens(eigenvalues, eigenvectors, index):
	"""
	Function to canonicalize eigenvectors for multiple eigenvalues.
	"""
	tol = 1e-8
	sort_indices = np.argsort(eigenvalues)
	sorted_eigenvalues = eigenvalues[sort_indices]
	sorted_eigenvectors = eigenvectors[:, sort_indices]

	n_rows, k_cols = eigenvectors.shape
	n_total_eigens = len(eigenvalues)

	processed_eigenvalues_list = []
	processed_eigenvector_blocks = []

	i = 0
	while i < index and i < n_total_eigens:
		current_group_index = [i]
		processed_eigenvalues_list.append(sorted_eigenvalues[i])
		for j in range(i + 1, n_total_eigens):
			if abs(sorted_eigenvalues[j]-sorted_eigenvalues[i]) <= tol:
				current_group_index.append(j)
				processed_eigenvalues_list.append(sorted_eigenvalues[i])
			else:
				i = j-1
				break
			i = j
		temp_matrix = sorted_eigenvectors[:, current_group_index].T
		if len(current_group_index)==1:
			if temp_matrix[0, 0]<=0:
				output_matrix = -temp_matrix
			else:
				output_matrix = temp_matrix
		else:
			output_matrix = CanonicalizeMatrix(temp_matrix)
		processed_eigenvector_blocks.append(output_matrix.T)
		i = i+1

	output_eigenvalues = np.array(processed_eigenvalues_list[:min(index, n_total_eigens)])
	output_eigenvectors = np.concatenate(processed_eigenvector_blocks, axis=1)
	output_eigenvectors = output_eigenvectors[:,:min(index, n_total_eigens)]
	return output_eigenvalues, output_eigenvectors


def CanonicalizeMatrix(input_matrix):
	"""
	Function to canonicalize row space.
	"""
	tol = 1e-8
	RREFmatrix = input_matrix.copy().astype(np.float64)
	row_k, col_n = RREFmatrix.shape
	pivot_row = 0

	for j in range(col_n):
		if pivot_row>=row_k:
			break

		i_max = pivot_row
		for i in range(pivot_row+1, row_k):
			if  abs(RREFmatrix[i, j]) > abs(RREFmatrix[i_max, j]):
				i_max = i

		pivot_val = RREFmatrix[i_max, j]

		if abs(pivot_val) < tol:
			continue

		RREFmatrix[[pivot_row, i_max]] = RREFmatrix[[i_max, pivot_row]]

		RREFmatrix[pivot_row, :] /= RREFmatrix[pivot_row, j]
		RREFmatrix[pivot_row, j] = 1.0

		for i in range(row_k):
			if i != pivot_row:
				factor = RREFmatrix[i, j]
				RREFmatrix[i, :] -= factor * RREFmatrix[pivot_row, :]
				RREFmatrix[i, j] = 0.0

		pivot_row += 1

	Schmidtmatrix = RREFmatrix.copy().astype(np.float64)
	ouput_matrix = np.zeros_like(Schmidtmatrix)

	num_independent_rows = 0
	for i in range(row_k):
		v = Schmidtmatrix[i, :].copy()

		for j in range(num_independent_rows):
			q_j = ouput_matrix[j, :]
			projection_coeff = np.dot(v, q_j)
			v -= projection_coeff * q_j

		norm_v = np.linalg.norm(v)

		if norm_v > tol:  # If the remaining vector is non-zero
			ouput_matrix[num_independent_rows, :] = v / norm_v
			num_independent_rows += 1

	return ouput_matrix