# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import copy
import warnings
from .HiSDSolverCheckParam import *
from .HiSDIter import *

warnings.filterwarnings("ignore")


class Solver:
	def __init__(self, **kwargs):
		"""
		Validate parameters passed during initialization.
		"""
		HiSDCheckParam(self, **kwargs)

	def run(self):
		"""
		Solve for a specific saddle point.
		"""
		self.flag = True  # Initialize flags and timers

		# Check SaddleIndex and decide the method
		if self.SaddleIndex != 0:
			self.x, self.x_pre, self.v = HiSDInitialization(self)
			self.CalMethod = HiSDIteration
		else:
			self.x = copy.deepcopy(self.InitialPoint)
			self.x_pre = copy.deepcopy(self.InitialPoint)
			self.CalMethod = SDIteration
		return self.CalMethod(self)
