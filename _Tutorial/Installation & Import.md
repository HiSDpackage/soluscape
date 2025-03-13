---
layout: single
permalink: /Tutorial/Installation & Import
title: ""
sidebar:
    nav: Tutorial
toc: true
toc_max_level: 3
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

## Installation & Import

#### Step 1: Download the Code
First, download the code from GitHub:
- **GitHub Repository**: [https://github.com/HiSDpackage/solscape](https://github.com/HiSDpackage/solscape)

#### Step 2: Add the `solscape-1.0` Directory to the System Path
After downloading the code, you need to add the path of the `solscape-1.0` directory to the system path. This will allow you to access the package from anywhere on your system.

Use the following Python code to add the directory to the system path:

```python
import sys
sys.path.append('/path/to/solscape-1.0')
```

Replace `'/path/to/solscape-1.0'` with the actual path where the `solscape-1.0` directory is located.

#### Step 3: Import the Main Class
Once the path is set, you can import the main class `Landscape` from the `solscape` package as follows:

```python
from solscape import Landscape
```

This will allow you to use the `Landscape` class and other functionalities provided by the package.
