# Overview

`soluscape` is a python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems. It simplifies the process of saddle point searching, offers flexible parameter settings and many visualization tools.

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
   git clone https://github.com/HiSDpackage/soluscape
   cd soluscape-1.0
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

Below is a basic workflow for using soluscape-1.0:

1. **Add path**:
   Use the following Python code to add the directory to the system path:

   ```python
   import sys
   sys.path.append('/path/to/soluscape-1.0')
   ```

   Replace `'/path/to/soluscape-1.0'` with the actual path where the `soluscape-1.0` directory is located.

2. **Import**:
   ```python
   from soluscape import Landscape
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

Here are some example Jupyter Notebook files in `gallery` directory to help you get started quickly:

- `Ex_1_Butterfly.ipynb`
- `Ex_2_MullerBrownPotential.ipynb`
- `Ex_3_Cubic.ipynb`
- `Ex_4_PhaseField.ipynb`

## Contact

If you are interested in `soluscape` or want to contribute, please feel free to contact us!

## Authors

- **Lei ZHANG**

  Boya Distinguished Professor

  Beijing International Center for Mathematical Research (BICMR),

  Center for Quantitative Biology (CQB),
  
  Center for Machine Learning Research (CMLR), Peking University.

  - Email: [pkuzhangl@pku.edu.cn](mailto:pkuzhangl@pku.edu.cn)  
  - Website: [Lei Zhang's Homepage](http://faculty.bicmr.pku.edu.cn/~zhanglei/)

- **Yuyang LIU**
  
  Ph.D. Candidate

  School of Mathematical Science (SMS), Peking Univertsity.

  - Email: [liuyuyang@stu.pku.edu.cn](mailto:liuyuyang@stu.pku.edu.cn)  
  - Website: [Yuyang Liu's Homepage](https://liuonly1121.github.io/)

- <span style="font-size: 0.7em;">**Zixiang XIAO** (Main website author): [xiaozixiang@stu.pku.edu.cn](mailto:xiaozixiang@stu.pku.edu.cn)</span>  
- <span style="font-size: 0.7em;">**Hua SU**: [suhua@pku.edu.cn](mailto:suhua@pku.edu.cn)</span>  
- <span style="font-size: 0.7em;">**Jin ZHAO**: [zjin@cnu.edu.cn](mailto:zjin@cnu.edu.cn)</span>

###Lei ZHANG

  Boya Distinguished Professor

  Beijing International Center for Mathematical Research (BICMR),

  Center for Quantitative Biology (CQB),
  
  Center for Machine Learning Research (CMLR), Peking University.

  - Email: [pkuzhangl@pku.edu.cn](mailto:pkuzhangl@pku.edu.cn)  
  - Website: [Lei Zhang's Homepage](http://faculty.bicmr.pku.edu.cn/~zhanglei/)

###Yuyang LIU
  
  Ph.D. Candidate

  School of Mathematical Science (SMS), Peking Univertsity.

  - Email: [liuyuyang@stu.pku.edu.cn](mailto:liuyuyang@stu.pku.edu.cn)  
  - Website: [Yuyang Liu's Homepage](https://liuonly1121.github.io/)

###Zixiang XIAO (Main website author): [xiaozixiang@stu.pku.edu.cn](mailto:xiaozixiang@stu.pku.edu.cn)</span>  
###Hua SU: [suhua@pku.edu.cn](mailto:suhua@pku.edu.cn)</span>  
###Jin ZHAO: [zjin@cnu.edu.cn](mailto:zjin@cnu.edu.cn)</span>


<!--
---

## Acknowledgements

Special thanks to the following contributors:

Their contributions have been invaluable in the development of this package.

-->

### Related Work

The theoretical foundation of our software package is derived from the following research articles:

1. Zhang, L. (2023). Construction of solution landscapes for complex systems. _Mathematica Numerica Sinica_, ​**45**(3), 267-283. https://doi.org/10.12286/jssx.j2023-1121

2. Yin, J., Zhang, L., & Zhang, P. (2019). High-index optimization-based shrinking dimer method for finding high-index saddle points. _SIAM Journal on Scientific Computing_, ​**41**(6), A3576-A3595. https://doi.org/10.1137/19M1253356

3. Yin, J., Yu, B., & Zhang, L. (2020). Searching the solution landscape by generalized high-index saddle dynamics. _Science China Mathematics_, ​**64**(8). https://doi.org/10.1007/s11425-020-1737-1

4. Zhang, L., Zhang, P., & Zheng, X. (2024). Understanding high-index saddle dynamics via numerical analysis. _Communications in Mathematical Sciences_, ​**23**(2). https://doi.org/10.4310/CMS.241217235844

5. Luo, Y., Zhang, L., & Zheng, X. (2025). Accelerated high-index saddle dynamics method for searching high-index saddle points. _Journal of Scientific Computing_, ​**102**(3). https://doi.org/10.1007/s10915-024-02760-6

---

Thank you for using `soluscape`! We welcome any feedback or suggestions you may have.
