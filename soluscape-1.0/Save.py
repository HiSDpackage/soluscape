# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import warnings
import json
from scipy.io import savemat
import pickle

warnings.filterwarnings("ignore")


def SaveLandscape(instance, filepath, fileformat):
	"""
	Save the data in specific format.
	"""
	if fileformat == "json":
		filepath = filepath + ".json"
		output = {
			"SaddleID": [row[0] for row in instance.SaddleList],
			"Position": [row[1].tolist() for row in instance.SaddleList],
			"MorseIndex": [row[2] for row in instance.SaddleList],
			"FatherSet": [row[4] for row in instance.SaddleList],
		}
		# Write into the file
		with open(filepath, "w") as file:
			json.dump(output, file)
	elif fileformat == "mat":
		output = {
			"SaddleID": [row[0] for row in instance.SaddleList],
			"Position": [row[1].tolist() for row in instance.SaddleList],
			"MorseIndex": [row[2] for row in instance.SaddleList],
			"FatherSet": [row[4] for row in instance.SaddleList],
		}
		filepath = filepath + ".mat"
		savemat(filepath, output)
	elif fileformat == "pickle":
		filepath = filepath + ".pickle"
		output = {
			"SaddleID": [row[0] for row in instance.SaddleList],
			"Position": [row[1].tolist() for row in instance.SaddleList],
			"MorseIndex": [row[2] for row in instance.SaddleList],
			"FatherSet": [row[4] for row in instance.SaddleList],
		}
		with open(filepath, "wb") as f:
			pickle.dump(output, f)
	else:
		raise ValueError(
			f"Invalid format specification: Acceptable values are ['json', 'mat', 'pickle']., got {fileformat}."
		)
