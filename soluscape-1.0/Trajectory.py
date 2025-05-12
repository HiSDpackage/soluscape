# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import copy
import warnings
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from inspect import isfunction

warnings.filterwarnings("ignore")


def DrawSearchTrajectory(instance, **kwargs):
	instance.DataBoundary = instance.calHiSD.DataBoundary

	# Set default values for kwargs
	kwargs.setdefault("Contour", True)
	kwargs.setdefault("ContourGridNum", 50)
	kwargs.setdefault("ContourGridOut", 10)
	kwargs.setdefault("1DSamples", 1e3)
	kwargs.setdefault("1DSamplesOut", 1e2)
	kwargs.setdefault("WhetherSave", False)
	kwargs.setdefault("SaveFigurePath", "Landscape_figure.png")
	kwargs.setdefault("Contourf", True)
	kwargs.setdefault("Title", "The Search Trajectory")
	kwargs.setdefault("Projection", None)

	if ("DetailedTraj" not in kwargs) or (not isinstance(kwargs["DetailedTraj"], bool)):
		kwargs["DetailedTraj"] = False
	if not instance.SaveTrajectory:
		print(
			"[WARNING] Detailed trajectory plotting is unavailable when search trajectory saving is disabled."
		)
		kwargs["DetailedTraj"] = False

	# Set default trajectory and saddle points settings
	kwargs.setdefault(
		"TrajectorySet",
		{
			"linewidth": 0.4,
			"linestyle": "-",
			"color": "blue",
			"label": "Search Trajectory",
		},
	)
	kwargs["TrajectorySetFirst"] = copy.deepcopy(kwargs["TrajectorySet"])
	temp = kwargs["TrajectorySet"].pop("label", None)
	kwargs.setdefault(
		"1DFunctionDraw",
		{"linewidth": 2, "linestyle": "-", "color": "red", "label": "Function Curve"},
	)

	# Saddle point settings
	colors = list(mcolors.CSS4_COLORS.keys())

	kwargs.setdefault(
		"SaddlePointSet",
		[
			{
				"marker": "o",
				"color": colors[20 * i + 20],
				"label": f"Index {i} Saddle Point",
			}
			for i in range(instance.MaxIndex + 1)
		],
	)
	kwargs["SaddlePointSetFirst"] = copy.deepcopy(kwargs["SaddlePointSet"])
	for i in range(instance.MaxIndex + 1):
		temp = kwargs["SaddlePointSet"][i].pop("label", None)

	# Grid settings
	kwargs.setdefault(
		"GridSet",
		{"visible": True, "linestyle": "--", "linewidth": 0.1, "color": "gray"},
	)

	if instance.Dim > 2 or isfunction(kwargs["Projection"]):
		if isfunction(kwargs["Projection"]) and instance.Dim == 2:
			print(
				"[WARNING] Since the `Projection` parameter is valid, the trajectory is drawn after projection. \n"
				"Provide a function that accepts an (n, dim) ndarray as input and returns an (n, 2) ndarray as output."
			)
		if kwargs["Projection"] is None or not isfunction(kwargs["Projection"]):
			print(
				"[WARNING] Visualization of search paths is not supported for dimensions greater than 2. \n"
				"Please use the `Projection` parameter to project the data to 2D. \n"
				"Provide a function that accepts an (n, dim) ndarray as input and returns an (n, 2) ndarray as output."
			)
		else:
			plt.figure()

			print(
				"[WARNING] Contour plot and heatmap cannot be generated after projection because the projection function may not be injective."
			)

			WhetherSaddlePointDraw = [False for i in range(instance.MaxIndex + 1)]
			WhetherTrajectoryDraw = False

			# Plot saddle points and trajectories
			for i in range(len(instance.SaddleList)):
				if WhetherSaddlePointDraw[instance.SaddleList[i][2]]:
					projectpoint = kwargs["Projection"](
						instance.SaddleList[i][1].reshape(1, instance.Dim)
					)
					plt.scatter(
						projectpoint[0, 0],
						projectpoint[0, 1],
						**kwargs["SaddlePointSet"][instance.SaddleList[i][2]],
					)
				else:
					projectpoint = kwargs["Projection"](
						instance.SaddleList[i][1].reshape(1, instance.Dim)
					)
					plt.scatter(
						projectpoint[0, 0],
						projectpoint[0, 1],
						**kwargs["SaddlePointSetFirst"][instance.SaddleList[i][2]],
					)
					WhetherSaddlePointDraw[instance.SaddleList[i][2]] = True
			for i in range(len(instance.DetailRecord)):
				if instance.DetailRecord[i][1] == -1 or (
					instance.SaddleList[instance.DetailRecord[i][1]][2]
					<= instance.SaddleList[instance.DetailRecord[i][0]][2]
				):
					continue
				if kwargs["DetailedTraj"]:
					temprecordlist = copy.deepcopy(instance.DetailRecord[i][2])
					temprecordlist = np.append(
						temprecordlist,
						instance.SaddleList[instance.DetailRecord[i][0]][1].reshape(
							1, instance.Dim
						),
						axis=0,
					)

					projectrecordlist = kwargs["Projection"](temprecordlist)
					x_values = projectrecordlist[:, 0]
					y_values = projectrecordlist[:, 1]
					if WhetherTrajectoryDraw:
						plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
					else:
						plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])
						WhetherTrajectoryDraw = True
				else:
					if WhetherTrajectoryDraw:
						endpoint = kwargs["Projection"](
							instance.SaddleList[instance.DetailRecord[i][0]][1].reshape(
								1, instance.Dim
							)
						)
						beginpoint = kwargs["Projection"](
							instance.SaddleList[instance.DetailRecord[i][1]][1].reshape(
								1, instance.Dim
							)
						)
						x_values = [
							beginpoint[0, 0],
							endpoint[0, 0],
						]
						y_values = [
							beginpoint[0, 1],
							endpoint[0, 1],
						]
						plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
					else:
						endpoint = kwargs["Projection"](
							instance.SaddleList[instance.DetailRecord[i][0]][1].reshape(
								1, instance.Dim
							)
						)
						beginpoint = kwargs["Projection"](
							instance.SaddleList[instance.DetailRecord[i][1]][1].reshape(
								1, instance.Dim
							)
						)
						x_values = [
							beginpoint[0, 0],
							endpoint[0, 0],
						]
						y_values = [
							beginpoint[0, 1],
							endpoint[0, 1],
						]
						plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])
						WhetherTrajectoryDraw = True

			# Final plot settings
			plt.title(kwargs["Title"])
			plt.legend()
			plt.grid(**kwargs["GridSet"])
			if kwargs["WhetherSave"]:
				plt.savefig(kwargs["SaveFigurePath"], format="png")
			plt.show()
	elif instance.Dim == 2:
		plt.figure()

		# Draw contour if applicable
		if kwargs["Contour"] and instance.calHiSD.EnergyFunction is not None:
			xminbound = instance.DataBoundary[0][0]
			xmaxbound = instance.DataBoundary[0][1]
			xbound = xmaxbound - xminbound
			if xbound == 0:
				xbound = 1
			xboundonestep = xbound / kwargs["ContourGridNum"]
			yminbound = instance.DataBoundary[1][0]
			ymaxbound = instance.DataBoundary[1][1]
			ybound = ymaxbound - yminbound
			if ybound == 0:
				ybound = 1
			yboundonestep = ybound / kwargs["ContourGridNum"]
			xaxis = np.arange(
				xminbound - xboundonestep * kwargs["ContourGridOut"],
				xmaxbound + xboundonestep * kwargs["ContourGridOut"],
				xboundonestep,
			)
			yaxis = np.arange(
				yminbound - yboundonestep * kwargs["ContourGridOut"],
				ymaxbound + yboundonestep * kwargs["ContourGridOut"],
				yboundonestep,
			)
			xgrid, ygrid = np.meshgrid(xaxis, yaxis)
			zvalue = np.zeros_like(xgrid)
			for i in range(xgrid.shape[0]):
				for j in range(xgrid.shape[1]):
					tempx = np.array([[xgrid[i, j]], [ygrid[i, j]]])
					zvalue[i, j] = instance.calHiSD.EnergyFunctionCal(tempx)
			if kwargs["Contourf"]:
				plt.contourf(xgrid, ygrid, zvalue)
			plt.contour(xgrid, ygrid, zvalue)
		elif instance.calHiSD.EnergyFunction is None:
			print(
				"[WARNING] Energy function not provided. Contour plot cannot be generated. "
			)

		WhetherSaddlePointDraw = [False for i in range(instance.MaxIndex + 1)]
		WhetherTrajectoryDraw = False

		# Plot saddle points and trajectories
		for i in range(len(instance.SaddleList)):
			if WhetherSaddlePointDraw[instance.SaddleList[i][2]]:
				plt.scatter(
					instance.SaddleList[i][1][0],
					instance.SaddleList[i][1][1],
					**kwargs["SaddlePointSet"][instance.SaddleList[i][2]],
				)
			else:
				plt.scatter(
					instance.SaddleList[i][1][0],
					instance.SaddleList[i][1][1],
					**kwargs["SaddlePointSetFirst"][instance.SaddleList[i][2]],
				)
				WhetherSaddlePointDraw[instance.SaddleList[i][2]] = True
		for i in range(len(instance.DetailRecord)):
			if instance.DetailRecord[i][1] == -1 or (
				instance.SaddleList[instance.DetailRecord[i][1]][2]
				<= instance.SaddleList[instance.DetailRecord[i][0]][2]
			):
				continue
			if kwargs["DetailedTraj"]:
				temprecordlist = copy.deepcopy(instance.DetailRecord[i][2])
				temprecordlist = np.append(
					temprecordlist,
					instance.SaddleList[instance.DetailRecord[i][0]][1].reshape(
						1, instance.Dim
					),
					axis=0,
				)
				x_values = temprecordlist[:, 0]
				y_values = temprecordlist[:, 1]
				if WhetherTrajectoryDraw:
					plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
				else:
					plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])
					WhetherTrajectoryDraw = True
			else:
				if WhetherTrajectoryDraw:
					x_values = [
						instance.SaddleList[instance.DetailRecord[i][0]][1][0],
						instance.SaddleList[instance.DetailRecord[i][1]][1][0],
					]
					y_values = [
						instance.SaddleList[instance.DetailRecord[i][0]][1][1],
						instance.SaddleList[instance.DetailRecord[i][1]][1][1],
					]
					plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
				else:
					x_values = [
						instance.SaddleList[instance.DetailRecord[i][0]][1][0],
						instance.SaddleList[instance.DetailRecord[i][1]][1][0],
					]
					y_values = [
						instance.SaddleList[instance.DetailRecord[i][0]][1][1],
						instance.SaddleList[instance.DetailRecord[i][1]][1][1],
					]
					plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])
					WhetherTrajectoryDraw = True

		# Final plot settings
		plt.title(kwargs["Title"])
		plt.legend()
		plt.grid(**kwargs["GridSet"])
		if kwargs["WhetherSave"]:
			plt.savefig(kwargs["SaveFigurePath"], format="png")
		plt.show()

	elif instance.Dim == 1:
		# Plot for 1D case
		plt.figure()
		if kwargs["Contour"] and instance.calHiSD.EnergyFunction is not None:
			xminbound = instance.DataBoundary[0][0]
			xmaxbound = instance.DataBoundary[0][1]
			xbound = xmaxbound - xminbound
			if xbound == 0:
				xbound = 1
			xboundonestep = xbound / kwargs["1DSamples"]
			xaxis = np.arange(
				xminbound - xboundonestep * kwargs["1DSamplesOut"],
				xmaxbound + xboundonestep * kwargs["1DSamplesOut"],
				xboundonestep,
			)
			yvalue = np.zeros_like(xaxis)
			for i in range(len(xaxis)):
				yvalue[i] = instance.calHiSD.EnergyFunctionCal(xaxis[i])
		elif instance.EnergyFunction is None:
			print(
				"[WARNING] Energy function not provided. Contour plot cannot be generated. "
			)
		plt.plot(xaxis, yvalue, **kwargs["1DFunctionDraw"])

		# Plot saddle points and trajectory
		WhetherSaddlePointDraw = [False for i in range(instance.MaxIndex + 1)]
		WhetherTrajectoryDraw = False
		for i in range(len(instance.SaddleList)):
			if WhetherSaddlePointDraw[instance.SaddleList[i][2]]:
				plt.scatter(
					instance.SaddleList[i][1][0][0],
					instance.calHiSD.EnergyFunctionCal(instance.SaddleList[i][1][0][0]),
					**kwargs["SaddlePointSet"][instance.SaddleList[i][2]],
				)
			else:
				plt.scatter(
					instance.SaddleList[i][1][0][0],
					instance.calHiSD.EnergyFunctionCal(instance.SaddleList[i][1][0][0]),
					**kwargs["SaddlePointSetFirst"][instance.SaddleList[i][2]],
				)
				WhetherSaddlePointDraw[instance.SaddleList[i][2]] = True
		for i in range(len(instance.DetailRecord)):
			if instance.DetailRecord[i][1] == -1 or (
				instance.SaddleList[instance.DetailRecord[i][1]][2]
				<= instance.SaddleList[instance.DetailRecord[i][0]][2]
			):
				continue
			if WhetherTrajectoryDraw:
				x_values = [
					instance.SaddleList[instance.DetailRecord[i][0]][1][0][0],
					instance.SaddleList[instance.DetailRecord[i][1]][1][0][0],
				]
				y_values = [
					instance.calHiSD.EnergyFunctionCal(
						np.array(
							instance.SaddleList[instance.DetailRecord[i][0]][1][0][0]
						)
					),
					instance.calHiSD.EnergyFunctionCal(
						np.array(
							instance.SaddleList[instance.DetailRecord[i][1]][1][0][0]
						)
					),
				]
				plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
			else:
				x_values = [
					instance.SaddleList[instance.DetailRecord[i][0]][1][0][0],
					instance.SaddleList[instance.DetailRecord[i][1]][1][0][0],
				]
				y_values = [
					instance.calHiSD.EnergyFunctionCal(
						np.array(
							instance.SaddleList[instance.DetailRecord[i][0]][1][0][0]
						)
					),
					instance.calHiSD.EnergyFunctionCal(
						np.array(
							instance.SaddleList[instance.DetailRecord[i][1]][1][0][0]
						)
					),
				]
				plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])

		# Final plot settings
		plt.title(kwargs["Title"])
		plt.xlabel("x")
		plt.ylabel("f(x)")
		plt.legend()
		plt.grid(**kwargs["GridSet"])
		if kwargs["WhetherSave"]:
			plt.savefig(kwargs["SaveFigurePath"], format="png")
		plt.show()
