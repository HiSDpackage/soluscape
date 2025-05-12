# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings

warnings.filterwarnings("ignore")


def gaussianper(Dim, PerturbationRadius):
	"""
	Generate Gaussian-distributed random vector and normalize it.
	"""
	v = np.random.randn(Dim)
	v_normalized = PerturbationRadius * v / np.clip(np.linalg.norm(v), 1e-10, None)
	return v_normalized.reshape(-1, 1)


def uniformper(Dim, PerturbationRadius):
	"""
	Generate uniform-distributed random vector and normalize it.
	"""
	v = np.random.uniform(-1, 1, Dim)
	v_normalized = PerturbationRadius * v / np.clip(np.linalg.norm(v), 1e-10, None)
	return v_normalized.reshape(-1, 1)
