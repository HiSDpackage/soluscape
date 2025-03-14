---
layout: single
permalink: /Tutorial/PackageRequirements
title: ""
sidebar:
    nav: Tutorial
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
      
A Python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems.It simplifies the process of saddle point searching, offers flexible parameter settings and many visualization tools.
      

---

## Package Requirements
### Overview
This component requires the following Python packages to be installed. Verify installations before usage.

### Built-in Packages
The following standard library modules are required (no installation needed):
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

### Third-party Dependencies
Required external packages with version specifications:

| Package       | Required Version | Installation Command           |
|---------------|------------------|---------------------------------|
| NumPy         | 2.2.3  | `pip install numpy==2.2.3`     |
| SciPy         | 1.15.2 | `pip install scipy==1.15.2`     |
| SymPy         | 1.13.3 | `pip install sympy==1.13.3`       |
| Matplotlib    | 3.10.0 | `pip install matplotlib==3.10.0` |
| NetworkX      | 3.4.2  | `pip install networkx==3.4.2`     |

### Full Environment Setup
```bash
pip install "numpy>=2.2.3" \
    "scipy>=1.15.2" \
    "sympy>=1.13.3" \
    "matplotlib>=3.10.0" \
    "networkx>=3.4.2"
```

### Version Verification
Check installed versions using:
```python
import numpy, scipy, sympy, matplotlib, networkx

print(f"NumPy: {numpy.__version__}")       # Should show 2.2.3
print(f"SciPy: {scipy.__version__}")       # Should show 1.15.2
print(f"SymPy: {sympy.__version__}")       # Should show 1.13.3
print(f"Matplotlib: {matplotlib.__version__}")  # Should show 3.10.0
print(f"NetworkX: {networkx.__version__}") # Should show 3.4.2
```
