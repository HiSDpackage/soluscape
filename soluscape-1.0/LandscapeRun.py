# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import warnings
from itertools import combinations

warnings.filterwarnings("ignore")


def LandscapeRun(instance):
	"""
	Do the downward search automatically of HiSD to construct the solution landscape
	"""
	tempList = []  # Temporary list to hold intermediate saddle points
	k = instance.MaxIndex
	np.random.seed(1121)

	# Searching for saddle points starting from MaxIndex
	while k >= 0:
		instance.calHiSD.SaddleIndex = k
		if instance.InitialEigenVectors is not None:
			instance.calHiSD.InitialEigenVectors = instance.InitialEigenVectors[:, 0:k]
		print("\n")
		print(f"From initial point search index-{k}:\n" + "-" * 30)
		print("\n")
		instance.calHiSD.run()
		if instance.calHiSD.flag:
			whetherinlist, smallestind = checkwhetherexist(
				instance, instance.calHiSD.x, instance.calHiSD.finalindex
			)
			if whetherinlist:
				xold = instance.SaddleList[smallestind][1]
				xnew = instance.calHiSD.x
				gold = instance.calHiSD.Grad(xold)
				gnew = instance.calHiSD.Grad(xnew)
				if np.linalg.norm(gold) > np.linalg.norm(gnew):
					instance.SaddleList[smallestind][1] = instance.calHiSD.x
				if instance.Continue:
					tempList.append(
						[
							instance.SaddleList[smallestind][0],
							instance.SaddleList[smallestind][1],
							instance.SaddleList[smallestind][2],
							instance.SaddleList[smallestind][3],
						]
					)
				if instance.BeginID != -1 and (
					instance.BeginID not in instance.SaddleList[smallestind][4]
				):
					instance.SaddleList[smallestind][4].append(instance.BeginID)
					if instance.SaveTrajectory:
						instance.DetailRecord.append(
							[
								smallestind,
								instance.BeginID,
								instance.calHiSD.x_record,
								instance.calHiSD.timestep_record,
							]
						)
					else:
						instance.DetailRecord.append([smallestind, instance.BeginID])
				print("Search an existing saddle point.")
			else:  # Save the saddle point and its information
				instance.SaddleList.append(
					[
						instance.saddleind,
						instance.calHiSD.x,
						instance.calHiSD.finalindex,
						instance.calHiSD.negvecs,
						[instance.BeginID],
					]
				)
				tempList.append(
					[
						instance.saddleind,
						instance.calHiSD.x,
						instance.calHiSD.finalindex,
						instance.calHiSD.negvecs,
					]
				)
				if instance.SaveTrajectory:
					instance.DetailRecord.append(
						[
							instance.saddleind,
							instance.BeginID,
							instance.calHiSD.x_record,
							instance.calHiSD.timestep_record,
						]
					)
				else:
					instance.DetailRecord.append([instance.saddleind, instance.BeginID])
				instance.saddleind = instance.saddleind + 1
			if instance.calHiSD.finalindex > instance.MaxIndex:
				instance.MaxIndex = instance.calHiSD.finalindex
				print("Warning! 'MaxIndex' updated due to a larger saddle point index.")
			break
		k = k - 1
	if k == -1:
		raise RuntimeError("No more saddle points found in the search area!")

	while tempList:
		tempsearchinitial = tempList.pop(0)
		for j in range(
			tempsearchinitial[2] - 1,
			max(0, tempsearchinitial[2] - instance.MaxIndexGap) - 1,
			-1,
		):
			if j > 0:
				# Try all combinations of eigenvectors
				all_combinations = list(combinations(range(tempsearchinitial[2]), j))
				for r in range(len(all_combinations)):
					if instance.EigenCombination == "min":
						if r != 0:
							continue
					instance.calHiSD.SaddleIndex = j
					instance.calHiSD.InitialEigenVectors = tempsearchinitial[3][
						:, all_combinations[r]
					]

					# Generate perturbations
					PerturbationList = []
					for p in range(instance.PerturbationNumber):
						pertemp = instance.PerMethod(
							instance.Dim, instance.PerturbationRadius
						)
						PerturbationList.append(pertemp)
						PerturbationList.append(-pertemp)
					for per in PerturbationList:
						instance.calHiSD.InitialPoint = tempsearchinitial[1] + per
						print("\n")
						print(
							f"From saddle point (index-{tempsearchinitial[2]}, ID-{tempsearchinitial[0]}) search index-{j}:\n"
							+ "-" * 30
						)
						print("\n")
						instance.calHiSD.run()
						if not instance.calHiSD.flag:
							continue
						whetherinlist, smallestind = checkwhetherexist(
							instance, instance.calHiSD.x, instance.calHiSD.finalindex
						)
						if instance.calHiSD.finalindex > j:
							print(
								"Sorry! Because of the relaxed abort criteria, we find a saddle point with higher index."
							)
							continue
						if whetherinlist:  # If the point is already in the list
							xold = instance.SaddleList[smallestind][1]
							xnew = instance.calHiSD.x
							gold = instance.calHiSD.Grad(xold)
							gnew = instance.calHiSD.Grad(xnew)
							if np.linalg.norm(gold) > np.linalg.norm(gnew):
								instance.SaddleList[smallestind][1] = instance.calHiSD.x
							if (
								tempsearchinitial[0]
								not in instance.SaddleList[smallestind][4]
							):
								instance.SaddleList[smallestind][4].append(
									tempsearchinitial[0]
								)
								if instance.SaveTrajectory:
									instance.DetailRecord.append(
										[
											smallestind,
											tempsearchinitial[0],
											instance.calHiSD.x_record,
											instance.calHiSD.timestep_record,
										]
									)
								else:
									instance.DetailRecord.append(
										[smallestind, tempsearchinitial[0]]
									)
						else:  # Add the new saddle point
							instance.SaddleList.append(
								[
									instance.saddleind,
									instance.calHiSD.x,
									instance.calHiSD.finalindex,
									instance.calHiSD.negvecs,
									[tempsearchinitial[0]],
								]
							)
							if instance.SaveTrajectory:
								instance.DetailRecord.append(
									[
										instance.saddleind,
										tempsearchinitial[0],
										instance.calHiSD.x_record,
										instance.calHiSD.timestep_record,
									]
								)
							else:
								instance.DetailRecord.append(
									[instance.saddleind, tempsearchinitial[0]]
								)
							tempList.append(
								[
									instance.saddleind,
									instance.calHiSD.x,
									instance.calHiSD.finalindex,
									instance.calHiSD.negvecs,
								]
							)
							instance.saddleind = instance.saddleind + 1

			else:
				# No eigenvectors, perturbation only
				instance.calHiSD.SaddleIndex = j
				instance.calHiSD.InitialEigenVectors = None
				# Generate perturbations
				PerturbationList = []
				for p in range(instance.PerturbationNumber):
					pertemp = instance.PerMethod(
						instance.Dim, instance.PerturbationRadius
					)
					PerturbationList.append(pertemp)
					PerturbationList.append(-pertemp)
				for per in PerturbationList:
					instance.calHiSD.InitialPoint = tempsearchinitial[1] + per
					print("\n")
					print(
						f"From saddle point (index-{tempsearchinitial[2]}, ID-{tempsearchinitial[0]}) search index-{j}:\n"
						+ "-" * 30
					)
					print("\n")
					instance.calHiSD.run()
					if not instance.calHiSD.flag:
						continue
					whetherinlist, smallestind = checkwhetherexist(
						instance, instance.calHiSD.x, instance.calHiSD.finalindex
					)
					if instance.calHiSD.finalindex > j:
						print(
							"Sorry! Because of the relaxed abort criteria, we find a saddle point with higher index."
						)
						continue
					if whetherinlist:  # Update if point already exists in list
						xold = instance.SaddleList[smallestind][1]
						xnew = instance.calHiSD.x
						gold = instance.calHiSD.Grad(xold)
						gnew = instance.calHiSD.Grad(xnew)
						if np.linalg.norm(gold) > np.linalg.norm(gnew):
							instance.SaddleList[smallestind][1] = instance.calHiSD.x
						if (
							tempsearchinitial[0]
							not in instance.SaddleList[smallestind][4]
						):
							instance.SaddleList[smallestind][4].append(
								tempsearchinitial[0]
							)
							if instance.SaveTrajectory:
								instance.DetailRecord.append(
									[
										smallestind,
										tempsearchinitial[0],
										instance.calHiSD.x_record,
										instance.calHiSD.timestep_record,
									]
								)
							else:
								instance.DetailRecord.append(
									[smallestind, tempsearchinitial[0]]
								)
					else:  # Add the new saddle point
						instance.SaddleList.append(
							[
								instance.saddleind,
								instance.calHiSD.x,
								instance.calHiSD.finalindex,
								instance.calHiSD.negvecs,
								[tempsearchinitial[0]],
							]
						)
						if instance.SaveTrajectory:
							instance.DetailRecord.append(
								[
									instance.saddleind,
									tempsearchinitial[0],
									instance.calHiSD.x_record,
									instance.calHiSD.timestep_record,
								]
							)
						else:
							instance.DetailRecord.append(
								[instance.saddleind, tempsearchinitial[0]]
							)
						tempList.append(
							[
								instance.saddleind,
								instance.calHiSD.x,
								instance.calHiSD.finalindex,
								instance.calHiSD.negvecs,
							]
						)
						instance.saddleind = instance.saddleind + 1


def checkwhetherexist(instance, x, index):
	"""
	Check if a saddle point already exists.
	"""
	for i in range(len(instance.SaddleList)):
		if instance.SameJudgementMethod(x, instance.SaddleList[i][1]) and (
			index == instance.SaddleList[i][2]
		):
			return True, i
	return False, None
