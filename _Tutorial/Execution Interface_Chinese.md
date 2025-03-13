---
layout: single
permalink: /Tutorial/Execution Interface_Chinese
title: ""
sidebar:
    nav: Tutorial_Chinese
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
      
这是一个用高阶鞍点动力学（High-index Saddle Dynamics,HiSD）构建解景观的Python包。该工具包支持在动力系统中数值计算鞍点及其层次结构。

---    
      
## 执行接口

### `.Run()`
**描述**  
启动解景观计算过程。

**参数**  
无  

**用法**  
```python
landscape = Landscape(
    MaxIndex=3, 
    AutoDiff=True, 
    EnergyFunction="1*(x1**2-1)**2+2*(x2**2-1)**2+3*(x3**2-1)**2", 
    InitialPoint=np.array([0, 0, 0])
)
landscape.Run()  # Starts computation
```

**输出**  
通过 `instance.DetailRecord` 访问搜索轨迹。它的每一行都是一次成功搜索的数据，依次包含终点鞍点的 ID、起点鞍点的 ID、每一步位置的 ndarray 以及每一步时间位置的 ndarray。

通过 `instance.SaddleList` 访问鞍点数据。它的每一行都是一个鞍点的数据，依次包含鞍点的 ID、鞍点的位置、鞍点的莫尔斯指数、负特征值的特征向量以及父鞍点集合。

更多详情请参见 `输出对象`。

--- 

### `.RestartFromPoint(RestartPoint, MaxIndex)`
**描述**  
从指定坐标重新启动计算。

**参数**  
| 名称 | 类型 | 约束条件 | 描述 |
|------|------|-------------|-------------|
| `RestartPoint` | `list` or `numpy.ndarray` (1D) | 必须与系统维度匹配 | 初始位置向量 |
| `MaxIndex` | `int` | `0 ≤ max_index ≤ dim` | 要计算的最大鞍点阶数 |

**用法**  
```python
landscape.RestartFromPoint(
    RestartPoint=np.array([[0.2], [-0.8]]), 
    MaxIndex=2
)
```

--- 

### `.RestartFromSaddle(BeginID, Perturbation, MaxIndex)`
**描述**  
从现有鞍点重新启动计算。 

**参数**  
| 名称 | 类型 | 约束条件 | 描述 |
|------|------|-------------|-------------|
| `BeginID` | `int` | `0 ≤ begin_id < len(SaddleList)` | 有效的鞍点 ID |
| `Perturbation` | `numpy.ndarray` (1D) | 必须与系统维度匹配 | 初始扰动向量 |
| `MaxIndex` | `int` | `0 ≤ max_index ≤ dim` | 要计算的最大鞍点索引 |

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
**描述**  
可视化系统的搜索轨迹和能量景观。支持等高线叠加、样式自定义以及高维投影。

**参数**  
| 名称 | 类型 | 约束条件 | 描述及默认值 |
|------|------|-------------|-------------|
| `DetailedTraj` | `bool` | 需要保存的轨迹数据 | 显示完整迭代路径 <br>（默认值：`False`） |
| `Contour` | `bool` | 仅适用于 2D 系统 | 启用等高线 <br>（默认值：`True`） |
| `Contourf` | `bool` | `Contour=True` | 启用填充颜色的等高线 <br>（默认值：`True`） |
| `ContourGridNum` | `int` | `≥ 1` | 每轴的主网格分割数 <br>（默认值：`50`） |
| `ContourGridOut` | `int` | `≥ 0` | 每轴的扩展网格分割数 <br>（默认值：`10`） |
| `Title` | `str` |  | 图表标题文本 <br>（默认值：`"The Search Trajectory"`） |
| `TrajectorySet` | `dict` |  | 设置轨迹样式 <br>（默认值：`{"linewidth": 0.4, "linestyle": "-", "color": "blue", "label": "Search Trajectory"}`） |
| `SaddlePointSet` | `list[dict]` |  | 设置鞍点样式 <br>（默认值：`[{"marker": "o", "color": colors[20 * i + 20], "label": f"Index {i} Saddle Point"} for i in range(instance.MaxIndex + 1)]`） |
| `GridSet` | `dict` |  | 设置网格样式 <br>（默认值：`{"visible": True, "linestyle": "--", "linewidth": 0.1, "color": "gray"}`） |
| `1DSamples` | `int` | `≥ 1`（仅适用于 1D） | 函数采样密度 <br>（默认值：`1e3`） |
| `1DSamplesOut` | `int` | `≥ 0`（仅适用于 1D） | 扩展采样范围 <br>（默认值：`1e2`） |
| `1DFunctionDraw` | `dict` | 仅适用于 1D | 设置 1D 函数样式 <br>（默认值：`{"linewidth": 2, "linestyle": "-", "color": "red", "label": "Function Curve"}`） |
| `WhetherSave` | `bool` |  | 保存到文件 <br>（默认值：`False`） |
| `SaveFigurePath` | `str` | 文件扩展名决定格式 | 输出路径 <br>（默认值：`"Landscape_figure.png"`） |
| `Projection` | `None` 或 `callable` | 适用于 dim > 2 | 投影函数 <br>（签名：`((n*dim) array) → ((n*2) array)`） |

**用法**  
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

**可视化规则**  
**维度处理**:
- 1D: X-axis = iteration count, Y-axis = function value
- 2D: Natural coordinates
- ≥3D: Requires `Projection` to 2D plane

**数据要求**  
- Detailed trajectories require `SaveTrajectory=True` in `.Run()` call

**输出**  
- Matplotlib figure (interactive display)  
- Image file when `WhetherSave=True` (PNG/PDF/SVG based on path)

---

### `.DrawConnection(**kwargs)`  
**描述**  
可视化解景观中鞍点之间的连接性。显示鞍点节点和连接它们的搜索路径的标记。支持点和连接线的自定义样式。

**参数**  
| 名称 | 类型 | 默认值 | 描述 |
|------|------|-------------|-------------|
| `Title` | `str` | `"The Connection of Saddle Points"` | 图表标题文本 |
| `SaddlePointSet` | `list[dict]` | `[{"node_shape": "o", "node_color": colors[i], "label": f"Index {i} Saddle Point"}for i in range(instance.MaxIndex + 1)]` | 设置鞍点样式 |
| `TrajectorySet` | `dict` | `{"width": 0.4, "style": "solid", "edge_color": "blue", "label": "Search Trajectory"}` | 设置连接路径样式 |
| `WhetherSave` | `bool` | `False` | 保存到文件 |
| `SaveFigurePath` | `str` | `"Landscape_Connection_figure.png"` | 输出路径 <br>（文件扩展名决定格式） |

**用法**  
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
**描述**  
将计算结果以指定的序列化格式持久化存储。

**参数**  
| 名称 | 类型 | 约束条件 | 描述 |
|------|------|-------------|-------------|
| `filepath` | `str` | 有效的文件系统路径 | 目标路径（不带扩展名） |
| `fileformat` | `str` | `"json" \| "pickle" \| "mat"` <br>（默认值：`"json"`） | 序列化格式 |

**用法**  
```python
landscape.Save(filepath="/output/results", fileformat="pickle")
```

**文件输出**  
生成：  
- `filepath.json`（JSON 文本格式）  
- `filepath.pickle`（Python 二进制序列化）  
- `filepath.mat`（MATLAB 兼容的二进制格式）  

包含字典，对齐以下索引：  
1. `SaddleID`：唯一标识号  
2. `Position`：空间坐标（N 维数组）  
3. `MorseIndex`：负特征值的数量  
4. `FatherSet`：祖先关系（列表格式的引用）  

**索引一致性**  
所有数据结构保持相同的顺序：  
`SaddleID[n]` ↔ `Position[n]` ↔ `MorseIndex[n]` ↔ `FatherSet[n]`


