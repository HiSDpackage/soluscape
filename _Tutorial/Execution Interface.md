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
# HiSD Package: solscape V-1.0
<!--
*        Version:  1.0.0
*        Created:  2024-12-25
*        Last Modified:  2025-03-13
*
*         Author:  Yuyang LIU <liuyuyang@stu.pku.edu.cn>
*      Copyright:  Copyright (c) 2024-2025, Lei ZHANG, Yuyang LIU. All rights reserved.
-->

      
A Python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems.
      
---
      
## Execution Interface

### `.Run()`
**Description**  
Initiates the solution landscape computation process.  

**Parameters**  
None  

**Usage**  
```python
landscape = Landscape(
    MaxIndex=3, 
    AutoDiff=True, 
    EnergyFunction="1*(x1**2-1)**2+2*(x2**2-1)**2+3*(x3**2-1)**2", 
    InitialPoint=np.array([0, 0, 0])
)
landscape.Run()  # Starts computation
```

**Output**  
Access search trajectory by `instance.DetailRecord`. Each row of it is data for one successful search. sequentially contains ID of end saddle point, ID of start saddle point, ndarray of each step position and  ndarray of each step time position.

Access saddle point data by `instance.SaddleList`. Each row of it is data for one saddle point. sequentially contains ID of the saddle point, position of the saddle point, Morse Index of the saddle point, the eigenvectors of negative eigenvalues and  set of father saddles.

See `Output Objects` for more details.

--- 

### `.RestartFromPoint(RestartPoint, MaxIndex)`
**Description**  
Restarts computation from specified coordinates.  

**Parameters**  

| Name | Type | Constraints | Description |
|------|------|-------------|-------------|
| `RestartPoint` | `list` or `numpy.ndarray` (1D) | Must match system dimension | Initial position vector |
| `MaxIndex` | `int` | `0 ≤ max_index ≤ dim` | Maximum saddle index to compute |

**Usage**  
```python
landscape.RestartFromPoint(
    RestartPoint=np.array([[0.2], [-0.8]]), 
    MaxIndex=2
)
```

--- 

### `.RestartFromSaddle(BeginID, Perturbation, MaxIndex)`
**Description**  
Restarts computation from existing saddle point.  

**Parameters**  

| Name | Type | Constraints | Description |
|------|------|-------------|-------------|
| `BeginID` | `int` | `0 ≤ begin_id < len(SaddleList)` | Valid saddle point ID |
| `Perturbation` | `numpy.ndarray` (1D) | Must match system dimension | Initial perturbation vector |
| `MaxIndex` | `int` | `0 ≤ max_index ≤ dim` | Maximum saddle index to compute |

**Usage**  
```python
landscape.RestartFromSaddle(
    BeginID=3, 
    Perturbation=1e-3 * np.array([[-1], [0.5]]), 
    MaxIndex=2
)
```

--- 

### `.DrawTrajectory(**kwargs)`  
**Description**  
Visualizes search trajectories and energy landscapes for systems. Supports contour overlays, style customization, and high-D projections.

**Parameters**  

| Name | Type | Constraints | Description & Default Value|
|------|------|-------------|-------------|
| `DetailedTraj` | `bool` | Requires saved trajectory data | Show full iteration path <br>(default: `False`) |
| `Contour` | `bool` | 2D systems only | Enable contour lines <br>(default: `True`) |
| `Contourf` | `bool` | `Contour=True` | Enable color-filled contours <br>(default: `True`) |
| `ContourGridNum` | `int` | `≥ 1` | Main grid divisions per axis <br>(default: `50`) |
| `ContourGridOut` | `int` | `≥ 0` | Extended grid divisions per axis <br>(default: `10`) |
| `Title` | `str` |  | Figure title text <br>(defalut: `"The Search Trajectory"`) |
| `TrajectorySet` | `dict` |  | Set the trajectory style <br>(default: `{"linewidth": 0.4, "linestyle": "-", "color": "blue", "label": "Search Trajectory"}`) |
| `SaddlePointSet` | `list[dict]` |  | Set the saddle point style <br>(default: `[{"marker": "o", "color": colors[20 * i + 20], "label": f"Index {i} Saddle Point"} for i in range(instance.MaxIndex + 1)]`) |
| `GridSet` | `dict` |  | Set the grid style <br>(default: `{"visible": True, "linestyle": "--", "linewidth": 0.1, "color": "gray"}`) |
| `1DSamples` | `int` | `≥ 1` (1D only) | Function sampling density <br>(default: `1e3`) |
| `1DSamplesOut` | `int` | `≥ 0` (1D only) | Extended sampling range <br>(default: `1e2`) |
| `1DFunctionDraw` | `dict` | 1D only | Set the 1D function style <br>(default: `{"linewidth": 2, "linestyle": "-", "color": "red", "label": "Function Curve"}`) |
| `WhetherSave` | `bool` |  | Save to file <br>(default: `False`) |
| `SaveFigurePath` | `str` | File extension determines format | Output path <br>(default: `"Landscape_figure.png"`) |
| `Projection` | `None` or `callable` | Required for dim > 2 | Projection function <br>(Signature: `((n*dim) array) → ((n*2) array)`) |

**Usage**  
```python
# 2D system without detailed trajectory
landscape.DrawTrajectory(
    Contour=True,
    Contourf=True,
    WhetherSave=True,
    ContourGridNum=100,
    ContourGridOut=25, 
    SaveFigurePath="landscape.png"
)

# high-D system with detailed trajectory
import numpy as np
def proj_func(input):
    output = np.hstack((1.0 * input[:, [0]]+ 1.5 * input[:, [1]], 1.0 * input[:, [0]]+ 2.5 * input[:, [2]]))
    return output

landscape.DrawTrajectory(
    DetailedTraj=True,
    ContourGridNum=100,
    ContourGridOut=25, 
    Projection=proj_func
)
```

**Visualization Rules**  
**Dimensionality Handling**:
- 1D: X-axis = iteration count, Y-axis = function value
- 2D: Natural coordinates
- ≥3D: Requires `Projection` to 2D plane

**Data Requirements**  
- Detailed trajectories require `SaveTrajectory=True` in `.Run()` call

**Output**  
- Matplotlib figure (interactive display)  
- Image file when `WhetherSave=True` (PNG/PDF/SVG based on path)

---

### `.DrawConnection(**kwargs)`  
**Description**  
Visualizes connectivity between saddle points in the solution landscape. Displays markers for saddle nodes and search paths connecting them. Supports custom styling of points and connection lines.

**Parameters**  

| Name | Type | Default Value | Description |
|------|------|-------------|-------------|
| `Title` | `str` | `"The Connection of Saddle Points"` | Figure title text |
| `SaddlePointSet` | `list[dict]` | `[{"node_shape": "o", "node_color": colors[i], "label": f"Index {i} Saddle Point"}for i in range(instance.MaxIndex + 1)]` | Set the saddle point style |
| `TrajectorySet` | `dict` | `{"width": 0.4, "style": "solid", "edge_color": "blue", "label": "Search Trajectory"}` | Set the connection path style |
| `WhetherSave` | `bool` | `False` | Save to file |
| `SaveFigurePath` | `str` | `"Landscape_Connection_figure.png"` | Output path <br>(file extension determines format) |

**Usage**  
```python
# Draw solution landscape
landscape.DrawConnection(
    Title="Solution Landscape",
    WhetherSave=True,
    SaveFigurePath="landscape.png"
)
```

--- 

### `.Save(filepath, fileformat)`  
**Description**  
Persists calculation results to persistent storage with specified serialization format.  

**Parameters**  

| Name | Type | Constraints | Description |
|------|------|-------------|-------------|
| `filepath` | `str` | Valid filesystem path | Target path without extension |
| `fileformat` | `str` | `"json" \| "pickle" \| "mat"` <br>(default: `"json"`) | Serialization format |

**Usage**  
```python
landscape.Save(filepath="/output/results", fileformat="pickle")
```

**File Output**  
Generates:  
- `filepath.json` (JSON text format)  
- `filepath.pickle` (Python binary serialization)  
- `filepath.mat` (MATLAB-compatible binary)  

Contains dictionary with aligned indices for:  
1. `SaddleID`: Unique identification numbers  
2. `Position`: Spatial coordinates (N-dimensional array)  
3. `MorseIndex`: Number of negative eigenvalues
4. `FatherSet`: Ancestry relationships (list-formatted references)  

**Index Consistency**  
All data structures maintain identical ordering:  
`SaddleID[n]` ↔ `Position[n]` ↔ `MorseIndex[n]` ↔ `FatherSet[n]`


