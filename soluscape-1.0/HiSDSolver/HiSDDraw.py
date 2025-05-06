# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import numpy as np
import copy
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# Functions in this file are not used in the construction of solution landscape!


def DrawXPicture(instance, **kwargs):
	"""
	Function to draw the search trajectory and contour plot for only one saddle point.
	"""
	if ("Contour" not in kwargs) or (not isinstance(kwargs["Contour"], bool)):
		kwargs["Contour"] = True
	if "ContourGridNum" not in kwargs:
		kwargs["ContourGridNum"] = 20
	if "ContourGridOut" not in kwargs:
		kwargs["ContourGridOut"] = 5
	if ("Contourf" not in kwargs) or (not isinstance(kwargs["Contourf"], bool)):
		kwargs["Contourf"] = True
	if ("WhetherMarker" not in kwargs) or (
		not isinstance(kwargs["WhetherMarker"], bool)
	):
		kwargs["WhetherMarker"] = True
	if ("Title" not in kwargs) or (not isinstance(kwargs["Title"], str)):
		kwargs["Title"] = "The Search Trajectory"
	if "TrajectorySet" not in kwargs:
		if kwargs["WhetherMarker"]:
			kwargs["TrajectorySet"] = {
				"marker": ".",
				"markersize": 0.1,
				"markerfacecolor": "yellow",
				"linewidth": 0.2,
				"linestyle": "-",
				"color": "blue",
				"label": "Search Trajectory",
			}
		else:
			kwargs["TrajectorySet"] = {
				"linewidth": 0.2,
				"linestyle": "-",
				"color": "blue",
				"label": "Search Trajectory",
			}
	kwargs["TrajectorySetFirst"] = copy.deepcopy(kwargs["TrajectorySet"])
	temp = kwargs["TrajectorySet"].pop("label", None)
	if "InitialPointSet" not in kwargs:
		kwargs["InitialPointSet"] = {
			"marker": "o",
			"color": "red",
			"label": "Initial Point",
		}
	if "FinalPointSet" not in kwargs:
		kwargs["FinalPointSet"] = {
			"marker": "*",
			"color": "red",
			"label": "Final Point",
		}
	if "GridSet" not in kwargs:
		kwargs["GridSet"] = {
			"visible": True,
			"linestyle": "--",
			"linewidth": 0.1,
			"color": "gray",
		}
	if instance.Dim > 2:
		print(
			"[WARNING] Search path visualization is not supported for dimensions > 2. "
			"Use `DrawGradientPicture()` instead."
		)
	elif instance.Dim == 2:
		plt.figure()
		if kwargs["Contour"] and instance.EnergyFunction is not None:
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
					zvalue[i, j] = instance.EnergyFunctionCal(tempx)
			if kwargs["Contourf"]:
				plt.contourf(xgrid, ygrid, zvalue)
			plt.contour(xgrid, ygrid, zvalue)
		elif instance.EnergyFunction is None:
			print(
				"[WARNING] Energy function not provided. Contour plot cannot be generated. "
			)
		for i in range(instance.x_record.shape[0] - 1):
			x_values = [instance.x_record[i, 0], instance.x_record[i + 1, 0]]
			y_values = [instance.x_record[i, 1], instance.x_record[i + 1, 1]]
			if i == 0:
				plt.plot(x_values, y_values, **kwargs["TrajectorySetFirst"])
			else:
				plt.plot(x_values, y_values, **kwargs["TrajectorySet"])
		plt.plot(
			instance.x_record[0, 0],
			instance.x_record[0, 1],
			**kwargs["InitialPointSet"]
		)
		plt.plot(
			instance.x_record[-1, 0],
			instance.x_record[-1, 1],
			**kwargs["FinalPointSet"]
		)
		plt.title(kwargs["Title"])
		plt.legend()
		plt.grid(**kwargs["GridSet"])
		plt.show()
	elif instance.Dim == 1:
		plt.figure()
		if kwargs["Contour"] and instance.EnergyFunction is not None:
			yminbound = instance.DataBoundary[0][0]
			ymaxbound = instance.DataBoundary[0][1]
			ybound = ymaxbound - yminbound
			if ybound == 0:
				ybound = 1
			yboundonestep = ybound / kwargs["ContourGridNum"]
			xaxis = np.arange(-1 / 2, instance.IterNum - 1 / 2, 1)
			yaxis = np.arange(
				yminbound - yboundonestep * kwargs["ContourGridOut"],
				ymaxbound + yboundonestep * kwargs["ContourGridOut"],
				yboundonestep,
			)
			xgrid, ygrid = np.meshgrid(xaxis, yaxis)
			zvalue = np.zeros_like(xgrid)
			for i in range(xgrid.shape[0]):
				for j in range(xgrid.shape[1]):
					tempx = np.array([[ygrid[i, j]]])
					zvalue[i, j] = instance.EnergyFunctionCal(tempx)
			if kwargs["Contourf"]:
				plt.contourf(xgrid, ygrid, zvalue)
			plt.contour(xgrid, ygrid, zvalue)
		elif instance.EnergyFunction is None:
			print(
				"[WARNING] Energy function not provided. Contour plot cannot be generated. "
			)
		plt.plot(instance.x_record, **kwargs["TrajectorySet"])
		plt.title(kwargs["Title"])
		plt.xlabel("Iteration")
		plt.ylabel("Position")
		plt.legend()
		plt.grid(**kwargs["GridSet"])
		plt.show()


def DrawGradientPicture(instance, **kwargs):
	"""
	Function to draw the gradient norm curve.
	"""
	if "CurveSet" not in kwargs:
		kwargs["CurveSet"] = {"label": "Gradient Norm"}
	if ("Title" not in kwargs) or (not isinstance(kwargs["Title"], str)):
		kwargs["Title"] = "The Gradient Norm Curve"
	if ("XLabel" not in kwargs) or (not isinstance(kwargs["XLabel"], str)):
		kwargs["XLabel"] = "Iteration"
	if ("YLabel" not in kwargs) or (not isinstance(kwargs["YLabel"], str)):
		kwargs["YLabel"] = "Gradient Norm"
	if "GridSet" not in kwargs:
		kwargs["GridSet"] = {
			"visible": True,
			"linestyle": "--",
			"linewidth": 0.1,
			"color": "gray",
		}
	plt.figure()
	plt.plot(instance.gnorm_record, **kwargs["CurveSet"])
	plt.title(kwargs["Title"])
	plt.xlabel(kwargs["XLabel"])
	plt.ylabel(kwargs["YLabel"])
	plt.legend()
	plt.grid(**kwargs["GridSet"])
	plt.show()
