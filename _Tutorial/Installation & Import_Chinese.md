---
layout: single
permalink: /Tutorial/Installation & Import_Chinese
title: ""
sidebar:
    nav: Tutorial_Chinese
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
      
这是一个用高阶鞍点动力学（High-index Saddle Dynamics,HiSD）构建解景观的Python包。该工具包支持在动力系统中数值计算鞍点及其层次结构。

---    

## 安装与导入

#### 步骤1：下载代码
首先，从GitHub下载代码：
- **GitHub 仓库**: [https://github.com/HiSDpackage/solscape](https://github.com/HiSDpackage/solscape)

#### 步骤2：将 `solscape-1.0` 目录添加到系统路径中
下载代码后，您需要将 `solscape-1.0` 目录的路径添加到系统路径中。这将使您能够从系统的任何位置访问该软件包。

使用以下 Python 代码将该目录添加到系统路径中：

```python
import sys
sys.path.append('/path/to/solscape-1.0')
```

将 `'/path/to/solscape-1.0'` 替换为 `solscape-1.0` 目录实际所在的路径。

#### 步骤3：导入主类
路径设置完成后，您可以从 `solscape` 包中导入主类 `Landscape`，方法如下：

```python
from solscape import Landscape
```

这将使您能够使用 `Landscape` 类以及该包提供的其他功能。
