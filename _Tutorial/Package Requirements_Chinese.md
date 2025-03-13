---
layout: single
permalink: /Tutorial/Package Requirements_Chinese
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

## 依赖包
### 概述
该组件需要安装以下 Python 包。使用前请验证是否已安装。

### 内置包
以下标准库模块是必需的（无需安装）：
```python
import copy
import sys
import warnings
import inspect
import json
import itertools
import math
import pickle
```

### 第三方依赖
所需的外部包及其版本要求：

| 包名称       | 所需版本 | 安装命令           |
|---------------|------------------|---------------------------------|
| NumPy         | 2.2.3  | `pip install numpy==2.2.3`     |
| SciPy         | 1.15.2 | `pip install scipy==1.15.2`     |
| SymPy         | 1.13.3 | `pip install sympy==1.13.3`       |
| Matplotlib    | 3.10.0 | `pip install matplotlib==3.10.0` |
| NetworkX      | 3.4.2  | `pip install networkx==3.4.2`     |

### 完整环境设置
```bash
pip install "numpy>=2.2.3" \
    "scipy>=1.15.2" \
    "sympy>=1.13.3" \
    "matplotlib>=3.10.0" \
    "networkx>=3.4.2"
```

### 版本验证
使用以下命令检查已安装的版本：
```python
import numpy, scipy, sympy, matplotlib, networkx

print(f"NumPy: {numpy.__version__}")       # Should show 2.2.3
print(f"SciPy: {scipy.__version__}")       # Should show 1.15.2
print(f"SymPy: {sympy.__version__}")       # Should show 1.13.3
print(f"Matplotlib: {matplotlib.__version__}")  # Should show 3.10.0
print(f"NetworkX: {networkx.__version__}") # Should show 3.4.2
```
