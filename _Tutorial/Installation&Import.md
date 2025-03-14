---
layout: single
permalink: /Tutorial/Installation&Import
title: ""
sidebar:
    nav: Tutorial
toc: false
toc_sticky: false
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

## Installation & Import

**Step 1: Download the Code**
First, download the code from GitHub:
- **GitHub Repository**: [https://github.com/HiSDpackage/soluscape](https://github.com/HiSDpackage/soluscape)

**Step 2: Add the `soluscape-1.0` Directory to the System Path**
After downloading the code, you need to add the path of the `soluscape-1.0` directory to the system path. This will allow you to access the package from anywhere on your system.

Use the following Python code to add the directory to the system path:

```python
import sys
sys.path.append('/path/to/soluscape-1.0')
```

Replace `'/path/to/soluscape-1.0'` with the actual path where the `soluscape-1.0` directory is located.

**Step 3: Import the Main Class**
Once the path is set, you can import the main class `Landscape` from the `soluscape` package as follows:

```python
from soluscape import Landscape
```

This will allow you to use the `Landscape` class and other functionalities provided by the package.
