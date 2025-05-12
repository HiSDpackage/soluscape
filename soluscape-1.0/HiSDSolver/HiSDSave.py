# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import json

# Functions in this file are not used in the construction of solution landscape!


def Save(instance, filepath):
	"""
	Function to save the data.
	"""
	filepath = filepath + ".json"
	output = {
		"SearchTrajectory": instance.x_record.tolist(),
		"GradientNorm": instance.gnorm_record,
		"IterNum": instance.IterNum,
		"FinalData": {
			"Position": instance.x.tolist(),
			"GradientNorm": instance.gnorm_record[-1],
			"MorseIndex": instance.finalindex,
		},
	}
	# Write into the file
	with open(filepath, "w") as file:
		json.dump(output, file)
