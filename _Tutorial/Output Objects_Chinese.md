---
layout: single
permalink: /Tutorial/Output Objects_Chinese
title: ""
sidebar:
    nav: Tutorial_Chinese
toc: true
toc_sticky: true
mathjax: true

---
# HiSD Package: soluscape V-1.0
<!--
*        Version:  1.0.0
*        Created:  2024-12-25
*        Last Modified:  2025-03-13
*
*         Author:  Yuyang LIU <liuyuyang@stu.pku.edu.cn>
*      Copyright:  Copyright (c) 2024-2025, Lei ZHANG, Yuyang LIU. All rights reserved.
-->
      
一个基于高阶鞍点动力学（HiSD）构建解景观的Python工具包。该工具包支持动力系统中鞍点的数值计算及其层级结构分析，简化了鞍点搜索流程，提供灵活的参数设置和丰富的可视化功能。

      
## 输出对象

### `.SaddleList`
**描述**  
发现的鞍点集合，包含拓扑元数据。

**类型**  
`list[list]`

**节点结构**  
```python
[
  [
    ID: int,               # Index 0 - Unique identifier
    Position: np.ndarray,  # Index 1 - Coordinate vector (d-dim)
    Morse Index: int,      # Index 2 - Number of negative eigenvalues
    Unstable Directions: np.ndarray,  # Index 3 - Eigenvectors (d x k)
    Parent IDs: list[int]   # Index 4 - Ancestor saddle IDs (where -1 indicates initial point)
  ]
  ... # Other saddle points
]
```

**访问**  
```python
# Get all index-1 saddles
index1_saddles = [node for node in landscape.SaddleList if node[2] == 1]

# Get position of saddle ID 5
saddle5_pos = landscape.SaddleList[5][1]
```

---

### `.DetailRecord`
**描述**  
完整的搜索轨迹数据。

**类型**  
`list[list]`  

**记录结构**  
```python
[
  [
    End ID: int,            # Index 0 - Terminating saddle ID
    Start ID: int,          # Index 1 - Originating saddle ID
    Path Positions: np.ndarray,  # Index 2 - Trajectory points (N x d)
    Path Times: np.ndarray       # Index 3 - Temporal coordinates (N x 1)
  ]
  ... # Other search trajectory
]
```

**访问**  
```python
# Plot first search path
first_search = landscape.DetailRecord[0]
plt.plot(first_search[2][:,0], first_search[2][:,1])
```



