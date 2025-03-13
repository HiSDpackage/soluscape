---
layout: single
permalink: /Tutorial/Execution Interface
title: ""
sidebar:
    nav: Tutorial
toc: true
toc_sticky: true
mathjax: true

---
# HiSD Package Version 1
<!--
 *        Version:  1.0.0
 *        Created:  2024-12-25
 *        Last Modified:  2025-03-08
 *
 *         Author:  Yuyang LIU <liuyuyang@stu.pku.edu.cn>
 *      Copyright:  Copyright (c) 2024-2025, Lei ZHANG, Yuyang LIU. All rights reserved.
-->

A Python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems.

## Execution Interface

### `.run()`
**Description**  
Initiates the solution landscape computation process.  

**Parameters**  
None  

**Usage**  
```python
landscape_instance = Landscape(**kwargs)
landscape_instance.run()  # Starts computation
```

**Output**  
Access search trajectory by `instance.detailrecord`. Each row of it is data for one successful search. sequentially contains ID of end saddle point, ID of start saddle point, ndarray of each step position and  ndarray of each step time position.

Access saddle point data by `instance.SaddleList`. Each row of it is data for one saddle point. sequentially contains ID of the saddle point, position of the saddle point, Morse Index of the saddle point, the eigenvectors of negative eigenvalues and  set of father saddles.

--- 

### `.RestartFromPoint(RestartPoint, MaxIndex)`
**Description**  
Restarts computation from specified coordinates  

**Parameters**  
| Name | Type | Constraints | Description |
|------|------|-------------|-------------|
| `RestartPoint` | `list` or `numpy.ndarray` (1D) | Must match system dimension | Initial position vector |
| `MaxIndex` | `int` | `0 �� max_index �� dim` | Maximum saddle index to compute |

**Usage**  
```python
landscape.RestartFromPoint(RestartPoint=np.array([[0.2], [-0.8]]), MaxIndex=2)
```

--- 

### `.RestartFromSaddle(BeginID, Perturbation, MaxIndex)`
**Description**  
Restarts computation from existing saddle point  

**Parameters**  
| Name | Type | Constraints | Description |
|------|------|-------------|-------------|
| `BeginID` | `int` | `0 �� begin_id < len(SaddleList)` | Valid saddle point ID |
| `Perturbation` | `numpy.ndarray` (1D) | Must match system dimension | Initial perturbation vector |
| `MaxIndex` | `int` | `0 �� max_index �� dim` | Maximum saddle index to compute |

**Usage**  
```python
landscape.RestartFromSaddle(BeginID=3, Perturbation=1e-3 * np.array([[-1], [0.5]]), MaxIndex=2)
```

--- 

### `.DrawTrajectory(**kwargs)`

You can draw the search path in the figure by calling 
```
xxx.DrawHeatmap(**kwargs)
```

when the system is 1-dimension or 2-dimension. However, when the system is 1-dimension, the x-axis of the figure refers to the iterations.

The initial point is referred by the marker circle, and the final point is refered by the marker pentagon. You can also change the figure parameters by type in.

`WhetherDetailedTraj` is a bool to choose whether to draw every points during the trajectory on the figure. The default value is `False` meaning we just draw the saddle points on the figure. Attention! It cannot be `True` when the `WhetherSaveDetail` parameter is `False` because there is no detailed data saved.

`WhetherContour` is a bool to choose whether to draw the contour figure of the energy function.

`WhetherContourf` is a bool to choose whether to fill the contour figure by color. It is not valid if `WhetherContour = False`.

`ContourGridNum` is a positive integer deciding how many equidistant grid intervals are devided between the minimum and maximum of search points' components along one axis while drawing the contour figure.

`ContourGridOut` is a non-negative integer controlling the number of equidistant grid intervals set out of the interval between the minimum and maximum of search points' components along one axis while drawing the contour figure.

`Title` is a string referring to the figure's title.

`TrajectorySet` is a dictionary containing the parameters you want to set when drawing the search trajectory.

`SaddlePointSet` is a dictionary referring to the parameters of drwaing the saddle points. You need to clearly set the markers, the colors and the labels for the saddle points with different saddle index separately, or you can just use the default value.

`GridSet` is a dictionary including your demands when drawing the background grid. 

`1DSamples` is a positive integer referring to the number of data points in the range when drawing in 1D system.

`1DSamplesOut` is a non-negative integer referring to the number of data points out the range when drawing in 1D system.

`1DFunctionDraw` is a dictionary containing the parameters you want to set when drawing the function curve in 1D system.

`WhetherSave` and `SaveFigurePath` are parameters to choose whether to save the figure and where to save.

--- 

### `.DrawConnection(**kwargs)`

You can also draw the connection of saddle points by calling 
```
xxx.DrawConnection(**kwargs)
```

As the command above, you can change the figure parameters, too.

`Title` is a string referring to the figure's title.

`SaddlePointSet` is a dictionary referring to the parameters of drwaing the saddle points. You need to clearly set the markers, the colors and the labels for the saddle points with different saddle index separately, or you can just use the default value.

`TrajectorySet` is a dictionary containing the parameters you want to set when drawing the search trajectory.

`WhetherSave` and `SaveFigurePath` are parameters to choose whether to save the figure and where to save.

--- 

### `.Save(filepath, fileformat)`

You can save the process of calculation by calling 
```
xxx.Save(filepath, fileformat)
```

The output file will be `filepath.json`(default), `filepath.pickle` or `filepath.mat` according to the specified format, which contains a dictionary with items named `SaddleID`, `Position`, `MorseIndex` and `FatherSet`. You can find all the information of saddle points in these items, including the number index, the position, the saddle index, and the list of father saddle points. Each saddle point has the same order index in all these items.
