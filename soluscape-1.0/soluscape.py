# Copyright (c) Lei ZHANG, Yuyang LIU
# Author: Yuyang LIU (liuyuyang@stu.pku.edu.cn)
# Contributors: Jin ZHAO, Hua SU.

import warnings
from LandscapeCheckParam import LandscapeCheckParam
from LandscapeRun import LandscapeRun
from Trajectory import DrawSearchTrajectory
from Connection import DrawLandscapeConnection
from Save import SaveLandscape
import numpy as np

warnings.filterwarnings("ignore")


class Landscape:
    def __init__(self, **kwargs):
        """
        Initialize the Landscape class by validating parameters.
        """
        LandscapeCheckParam(self, **kwargs)

    def Run(self):
        """
        Run the landscape process.
        """
        print("\n")
        print("Start running:\n"+'-'*30)
        print("\n")
        LandscapeRun(self)

    def RestartFromPoint(self, RestartPoint, MaxIndex):
        """
        Restart the landscape process.
        """
        RestartPoint = np.array(RestartPoint).reshape(-1,1)
        self.calHiSD.InitialPoint = RestartPoint
        self.InitialPoint = RestartPoint
        self.MaxIndex = MaxIndex
        self.BeginID = -1
        LandscapeRun(self)

    def RestartFromSaddle(self, BeginID, Perturbation, MaxIndex):
        """
        Run the landscape process.
        """
        RestartPoint = self.SaddleList[BeginID][1]+np.array(Perturbation).reshape(-1,1)
        self.calHiSD.InitialPoint = RestartPoint
        self.InitialPoint = RestartPoint
        self.MaxIndex = MaxIndex
        self.BeginID = BeginID
        LandscapeRun(self)

    def DrawTrajectory(self, **kwargs):
        """
        Draw the heatmap and search trajectory of the landscape.
        """
        DrawSearchTrajectory(self, **kwargs)

    def DrawConnection(self, **kwargs):
        """
        Draw the connection map of the landscape.
        """
        DrawLandscapeConnection(self, **kwargs)

    def Save(self, filepath, fileformat="json"):
        """
        Save the landscape data to a file in the specified format.
        """
        SaveLandscape(self, filepath, fileformat)
