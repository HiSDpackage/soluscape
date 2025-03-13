# Overview

`solscape` is a python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems. It simplifies the process of saddle point searching, offers flexible parameter settings and many visualization tools.

## Features

- **Multiple Algorithm Implementations**:
  - `HiOSD`: High-index optimization-based shrinking dimer method for gradient systems.
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

For more detailed usage, please refer to the documentation file.

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

Here are some example Jupyter Notebook files to help you get started quickly:

- `Ex_1_Butterfly.ipynb`
- `Ex_2_MullerBrownPotential.ipynb`
- `Ex_3_Cubic.ipynb`
- `Ex_4_PhaseField.ipynb`

## Contact

If you are interested in solscape or want to contribute, feel free to contact us!

**Author**: Lei ZHANG
**Email**: pkuzhangl@pku.edu.cn

**Author**: Yuyang LIU
**Email**: liuyuyang@stu.pku.edu.cn

---

Thank you for using solscape! Feedback and suggestions are always welcome!