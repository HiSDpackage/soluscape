# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import scipy.sparse.linalg as linalg
import warnings
from .HessianMatrix import (
    SingleHessianVectorProduct,
    BatchHessianVectorProduct,
    Hessian,
)
import time

warnings.filterwarnings("ignore")


def lobpcg(instance, x, v, **kwargs):
    """
    Function implementing the LOBPCG (Locally Optimal Block Preconditioned Conjugate Gradient) algorithm.
    """
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
    if values[-1] >= 0:
        whetherkindex = False
    return vectors, whetherkindex


def lobpcg_exacthessian(instance, x, v, **kwargs):
    """
    Function using exact Hessian for LOBPCG.
    """
    if "max_iter" not in kwargs:
        max_iter = instance.EigenMaxIter
    N = instance.Dim
    H = Hessian(instance, x) # Exact Hessian matrix
    values, vectors = linalg.lobpcg(A=H, X=v, maxiter=max_iter, largest=False)
    whetherkindex = True
    if values[-1] >= 0:
        whetherkindex = False
    return vectors, whetherkindex


def euler(instance, x, v, **kwargs):
    """
    Explicit Euler method for solving eigenvalue problem (non-exact Hessian).
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def euler_exacthessian(instance, x, v, **kwargs):
    """
    Explicit Euler method with exact Hessian.
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def euler_nonGrad(instance, x, v, **kwargs):
    """
    Explicit Euler method for non-gradient systems.
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def euler_nonGrad_exacthessian(instance, x, v, **kwargs):
    """"
    Explicit Euler method with exact Hessian for non-gradient systems.
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def power_nonGrad(instance, x, v, **kwargs):
    """
    Power iteration method for non-gradient systems.
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def power_nonGrad_exacthessian(instance, x, v, **kwargs):
    """
    Power iteration method with exact Hessian for non-gradient systems.
    """
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
    if max(values) >= 0:
        whetherkindex = False
    return v, whetherkindex


def GiveEigenvector(instance, x, k):
    """
    Function to compute the first k eigenvectors of the Hessian matrix.
    """
    H = Hessian(instance, x)
    eigenvalue, eigenvector = np.linalg.eigh((H + np.transpose(H)) / 2.0) # To calculate the eigen pairs of symmetric part
    order = np.argsort(eigenvalue)
    eigenvector = eigenvector[:, order]
    return eigenvector[:, 0:k]


def FindIndex(instance, x):
    """
    Function to find indices of negative, positive, and zero eigenvalues.
    """
    eps = instance.PrecisionTol  # Consider the absolute eigenvalues smaller than this as zero
    H = Hessian(instance, x)
    if instance.GradSym:
        eigenvalue, eigenvectors = np.linalg.eigh((H + np.transpose(H)) / 2.0)
    else:
        eigenvalue, eigenvectors = np.linalg.eig(H)
        eigenvalue = np.real(eigenvalue)
        eigenvectors = np.real(eigenvectors)
    negativenum = np.sum(eigenvalue < -eps)
    positivenum = np.sum(eigenvalue > eps)
    zeronum = instance.Dim - negativenum - positivenum
    negative_indices = np.where(eigenvalue < -eps)[0]
    negativevectors = eigenvectors[:, negative_indices]
    return negativenum, zeronum, positivenum, negativevectors
