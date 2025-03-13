---
layout: single
permalink: /
title: "solscape-1.0: Constructing Solution Landscapes Using High-index Saddle Dynamics (HiSD)"
excerpt: "A quick start guide."
sidebar:
    nav: docs
toc: true
toc_sticky: true
mathjax: true

---
# Overview

`solscape` is a python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems. It simplifies the process of saddle point searching, offers flexible parameter settings and many visualization tools.


## Features

- **Multiple Algorithm Implementations**:
  - `HiSD`: High-index saddle dynamics for gradient systems.
  - `GHiSD`: Generalized high-index saddle dynamics method for non-gradient systems.
- **Multiple Acceleration Algorithm Implementations**:
  - `HiSD`: Basic saddle point searching algorithm.
  - `NHiSD`: HiSD with Nesterov acceleration.
  - `HHiSD`: HiSD with Heavy Ball acceleration.
- **Flexible Features**:
  - Supports multiple input functions (gradient function or energy function, an expression string or a function handle).
  - Automatically validates parameter validity.
  - Modular class design for easy extensions.
  - Easy-to-use plotting for search trajectories, heatmaps, and saddle point connection graphs.
  - Convenient saving of important computation results.
  - Can deal with function systems.
  - Can automatically merge the same saddle points according to specific criteria.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HiSDpackage/solscape
   cd solscape-1.0
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

Below is a basic workflow for using solscape-1.0:

1. **Add path**:
   Use the following Python code to add the directory to the system path:

   ```python
   import sys
   sys.path.append('/path/to/solscape-1.0')
   ```

   Replace `'/path/to/solscape-1.0'` with the actual path where the `solscape-1.0` directory is located.

2. **Import**:
   ```python
   from solscape import Landscape
   ```

3. **Initialization**:
   ```python
   landscape = Landscape(**kwargs)
   ```

4. **Run the computation**:
   ```python
   landscape.Run()
   ```

5. **Plot graphs**:
   ```python
   landscape.DrawTrajectory(**kwargs)
   landscape.DrawConnection(**kwargs)
   ```

6. **Save results**:
   ```python
   mylandscape.Save(filepath, fileformat)
   ```

7. **Restart**:
   ```python
   landscape.RestartFromPoint(RestartPoint, MaxIndex)
   landscape.RestartFromSaddle(BeginID, Perturbation, MaxIndex)
   ```

For more detailed usage, please refer to the [documentation](https://github.com/HiSDpackage/solscape/blob/main/doc/Documentation.pdf) file.(You can also check in the ["Tutorial"](https://hisdpackage.github.io/solscape/Tutorial/Tutorial_overview) section on the left)

## Dependencies

HiSD depends on the following Python libraries:

Build-in packages:
- `copy`
- `sys`
- `warnings`
- `inspect`
- `json`
- `itertools`
- `math`
- `pickle`

Third-party packages:
- `numpy-2.2.3`
- `scipy-1.15.2`
- `sympy-1.13.3`
- `matplotlib-3.10.0`
- `networkx-3.4.2`

## Examples

Here are some example Jupyter Notebook files in `gallery` directory ([within the GitHub repository](https://github.com/HiSDpackage/solscape))  to help you get started quickly:(You can also check in the ["Examples"](https://hisdpackage.github.io/solscape/Examples/Examples_overview) section on the left)

- `Ex_1_Butterfly.ipynb`
- `Ex_2_MullerBrownPotential.ipynb`
- `Ex_3_Cubic.ipynb`
- `Ex_4_PhaseField.ipynb`

## Contact

If you are interested in `solscape` or want to contribute, please feel free to contact us!

### Authors

- **Lei Zhang**  
  - Email: [pkuzhangl@pku.edu.cn](mailto:pkuzhangl@pku.edu.cn)  
  - Website: [Lei Zhang's Homepage](http://faculty.bicmr.pku.edu.cn/~zhanglei/)

- **Yuyang Liu**  
  - Email: [liuyuyang@stu.pku.edu.cn](mailto:liuyuyang@stu.pku.edu.cn)  
  - Website: [Yuyang Liu's Homepage](https://liuonly1121.github.io/)

---

### Acknowledgements

Special thanks to the following contributors:
- **Zixiang Xiao** (Main website author): [xiaozixiang@stu.pku.edu.cn](mailto:xiaozixiang@stu.pku.edu.cn)
- **Hua Su**: [suhua@pku.edu.cn](mailto:suhua@pku.edu.cn)
- **Jin Zhao**: [zjin@cnu.edu.cn](mailto:zjin@cnu.edu.cn)

Their contributions have been invaluable in the development of this package.

---

Thank you for using `solscape`! We welcome any feedback or suggestions you may have.
