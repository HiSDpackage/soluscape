---
layout: single
permalink: /Tutorial/Output Objects
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
## Output Objects

### `.SaddleList`
**Description**  
Collection of discovered saddle points with topological metadata. 

**Type**  
`list[list]`  

**Node Structure**  
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

**Access**  
```python
# Get all index-1 saddles
index1_saddles = [node for node in landscape.SaddleList if node[2] == 1]

# Get position of saddle ID 5
saddle5_pos = landscape.SaddleList[5][1]
```

---

### `.detailrecord`
**Description**  
Complete search trajectory data. 

**Type**  
`list[list]`  

**Record Structure**  
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

**Access**  
```python
# Plot first search path
first_search = landscape.detailrecord[0]
plt.plot(first_search[2][:,0], first_search[2][:,1])
```

---


