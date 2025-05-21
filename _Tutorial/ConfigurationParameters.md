---
layout: single
permalink: /Tutorial/ConfigurationParameters
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
## Configuration Parameters
The configuration parameters for the `soluscape` package are divided into different categories, each focusing on a specific part of the algorithm. Below is an overview of the different categories and the associated parameters.

### System Parameters
These parameters are related to the system setup and its general properties: `Dim`, `EnergyFunction`, `Grad`, `AutoDiff`, `NumericalGrad`, `DimerLength`, `SymmetryCheck` and `GradientSystem`.

**`Dim` (Optional)**  
**Description**  
System dimension specification.  

**Data Type**  
`int` (positive) 

**Behavior**  
- Default: Inferred from `InitialPoint`  
- Manual override must match dimensions of:  
  - `InitialPoint`  
  - `InitialSearchDirection`  

--- 

**`EnergyFunction` (Conditional Required)** 
**Description**  
Specifies the energy function for gradient systems.  

**Data Type**  
- Python function: `Callable[[np.ndarray], float]`
  - **Input**: `np.ndarray` with shape `(d, 1)` (column vector)
- Symbolic expression: `str`
  - **Specification**: Use `x1, x2, ..., xd` as variables & Supports full `sympy` syntax

**Example**  
```python
EnergyFunction = '''
0.4*x1**2 - 0.2*x1*x2 + 0.25*x2**2 
- 5*(atan(x1-5) + atan(x2-5))
'''
```

--- 

**`Grad` (Conditional Required)**  
**Description**  
Specifies the gradient function for gradient systems or vector field for non-gradient systems.  

**Requirements**  
- For gradient systems: $\nabla$E   
- For non-gradient systems: Direct specification of F in $\dot{x}$ = -F(x)  

**Data Types**  
- Python function: `Callable[[np.ndarray], np.ndarray]`
  - **Input/Output**: `np.ndarray` with shape `(d, 1)` (column vector)  
- Symbolic expression list: `list[str]` (e.g., `["2*x1", "cos(x2)"]`) 

**Example**  
```python
# Gradient system
Grad = ["2*x1", "2*x2"]

# Non-gradient system 
Grad = ["x2", "-x1 - 0.1*x2"]
```

---

**`AutoDiff` (Optional)**  
**Description**  
Enables automatic differentiation of the energy function.  

**Data Type**  
`bool`  

**Options**  
- `True`: Requires `EnergyFunction` parameter  
- `False`: Requires manual specification of `Grad` parameter  

**Behavior**  
- Defaults to `True` if `EnergyFunction` is provided  
- Defaults to `False` if `Grad` is provided  

---

**`NumericalGrad` (Optional)**  
**Description**  
Enables numerical gradient approximation.  

**Applicability**  
Only active when `Grad` is unspecified  

**Data Type**  
`bool`  

**Options**  
- `True`: Use finite difference approximation  
- `False`: (Default) Use analytical gradient from `EnergyFunction`  

--- 

**`DimerLength` (Optional)**  
**Description**  
Displacement length for numerical gradient approximations.  

**Data Type**  
`float` (positive)

**Default**  
`1e-5`  

---

**`SymmetryCheck` (Optional)**  
**Description**  
Verifies gradient system properties via Hessian symmetry.  

**Data Type**  
`bool`

**Behavior**  
- `True`: (default) Auto-detect
- `False`: Bypass checks (improves performance)  

--- 

**`GradientSystem` (Optional)**  
**Description**  
Explicit declaration of gradient system nature.  

**Usage**  
Override automatic detection when known a priori.  

**Data Type**  
`bool`  

**Behavior**  
- missing: Auto-detect

--- 

### Hessian Parameters
These parameters are related to the Hessian matrix: `ExactHessian` and `HessianDimerLength`.

**`ExactHessian` (Optional)**  
**Description**  
Controls Hessian matrix computation method.  

**Data Type**  
`bool`  

**Options**  
- `True`: Analytical Hessian from symbolic gradient  
- `False`: (Default) Dimer-based approximation  

**Requirement**  
Requires `Grad` as symbolic expressions  

--- 

**`HessianDimerLength` (Optional)**  
**Description**  
Displacement length for numerical Hessian-Vector product approximations. 

**Data Type**  
`float` (positive) 

**Default**  
`1e-5`  

--- 

### Eigen Parameters
These parameters control how the eigen pairs (eigenvalues and eigenvectors) are computed: `EigenMethod`, `EigenMaxIter`, `EigenStepSize` and `PrecisionTol`.

**`EigenMethod` (Optional)**  
**Description**  
Eigensolver selection for stability analysis.  

**Data Type**  
`str`

**Options**  

| Method   | System Type      | Description                          |
|----------|------------------|--------------------------------------|
| `lobpcg` | Gradient (Default) | Locally Optimal Block PCG           |
| `euler`  | Gradient & Non-gradient | Explicit Euler Discretization       |
| `power`  | Non-gradient (Default) | Power Method              |

--- 

**`EigenMaxIter` (Optional)**  
**Description**  
Maximum iterations for eigenpair computation.  

**Data Type**  
`int` (positive) 

**Default**  
`10`  

--- 

**`EigenStepSize` (Optional)**  
**Description**  
Discretization step for Euler/power methods.  

**Data Type**  
`float` (positive)

**Default**  
`1e-7`  

--- 

**`PrecisionTol` (Optional)**  
**Description**  
Precision tolerance for eigenvalues. (We treat eigenvalues as 0 if its absolute value less than tolerance.)  

**Data Type**  
`float` (non-negative) 

**Default**  
`1e-5`   

--- 

**`EigvecUnified` (Optional)**  
**Description**  
Ensures eigenvectors corresponding to multiple eigenvalues are unified across different computational devices.

**Explanation**  
Due to significant differences in the implementation of fundamental algorithms (e.g., LAPACK) across hardware platforms, eigenvectors for multiple eigenvalues may vary substantially between devices, even though they all form valid bases for the same eigenspace. When set to `True`, this parameter activates Gaussian elimination to obtain the Row-Echelon Form (REF), followed by Gram-Schmidt orthogonalization. This process standardizes the basis vectors of the eigenspace, thereby improving cross-device search stability.

*Note: Outputs may still vary between devices due to differences in rounding error simulation.*

**Data Type**  
`bool`

**Default**  
`False`   

--- 

### Acceleration Parameters
These parameters are related to improving the speed and efficiency of the algorithm:
`BBStep`, `Acceleration`, `NesterovChoice`, `NesterovRestart` and `Momentum`.

**`BBStep` (Optional)**  
**Description**  
Enables Barzilai-Borwein adaptive step sizing.  

**Data Type**  
`bool`  

**Default**  
`False`  

**Trade-off**  
- May accelerate convergence  
- Can cause instability in stiff systems  

---

**`Acceleration` (Optional)**  
**Description**  
Convergence acceleration technique.

**Data Type**  
`str`

**Options**  
- `none`: (Default) No acceleration  
- `heavyball`: Momentum-based acceleration  
- `nesterov`: Nesterov-accelerated dynamics  

--- 

**`NesterovChoice` (Optional)**  
**Description**  
Specifies the acceleration parameter sequence for Nesterov's method.  

**Data Type**  
`int`

**Options**  
- `1` : (default) $\gamma_{n}=\frac{n}{n+3}$.
- `2` : $\gamma_{n}=\frac{\theta_{n}-1}{\theta_{n+1}}$, with $\theta_{n+1}=\frac{1+\sqrt{1+4\theta_{n}^{2}}}{2}$, $\theta_{0}=1$.

**Default**  
`1`  

--- 

**`NesterovRestart` (Optional)**  
**Description**  
Iteration interval for Nesterov momentum reset.  

**Data Type**  
`int` (positive) | `None`  

**Behavior**  
- `None`: Disables momentum restart  
- Integer `n`: Resets momentum every `n` iterations  

**Default**  
`None`  

--- 

**`Momentum` (Optional)**  
**Description**  
Momentum coefficient for heavy ball acceleration.  

**Data Type**  
`float` (non-negative) 

**Default**  
`0.0`  

**Constraints**  
- `0.0 ≤ Momentum < 1.0`  
- `0.0`: Equivalent to no acceleration  

--- 

### Solver Parameters
These parameters are related to the solver process and control the behavior of the HiSD process: `InitialPoint`, `Tolerance`, `SearchArea`, `TimeStep`, `MaxIter`, `SaveTrajectory`, `Verbose` and `ReportInterval`.

**`InitialPoint` (Required)**
**Description**  
The starting coordinates for saddle point search.  

**Data Types**  
`list` | `numpy.ndarray` (1D array)  

**Example**  
`initial_point = [0.5, -1.2]`

---

**`Tolerance` (Optional)**  
**Description**  
Convergence threshold for saddle point iterations.  

**Data Type**  
`float` (positive)

**Default**  
`1e-6`  

**Stopping Criterion**  
‖gradient vector‖$_2$ < Tolerance  

--- 

**`SearchArea` (Optional)**  
**Description**  
Maximum exploration radius from initial point.  

**Data Type**  
`float` (positive)  

**Default**  
`1e3`  

**Effect**  
Terminates search if ‖x - x$_0$‖$_2$ > SearchArea  

--- 

**`TimeStep` (Optional)**  
**Description**  
Temporal discretization interval for dynamics.  

**Data Type**  
`float` (positive)

**Default**  
`1e-4` 

--- 

**`MaxIter` (Optional)**  
**Description**  
Maximum number of HiSD iterations permitted.  

**Data Type**  
`int` (positive) 

**Default**  
`1000`  

--- 

**`SaveTrajectory` (Optional)**  
**Description**  
Records full optimization path during computation.  

**Data Type**  
`bool`  

**Default**  
`True`  

--- 

**`Verbose` (Optional)**  
**Description**  
Controls real-time progress reporting.  

**Output**  
Prints iteration count and gradient norm.

**Data Type**  
`bool`  

**Default**  
`False`  

--- 

**`ReportInterval` (Optional)**  
**Description**  
Iteration frequency for console output when `Verbose=True`.  

**Data Type**  
`int` (positive) 

**Default**  
`100`  

--- 

### Landscape Parameters
These parameters are related to constructing and navigating the solution landscape: `MaxIndex`, `MaxIndexGap`, `SameJudgement`, `InitialEigenVectors`, `PerturbationMethod`, `PerturbationRadius`, `PerturbationNumber` and `EigenCombination`.

**`MaxIndex` (Optional)**
**Description**  
Maximum saddle index (k) to compute.  
- Index 0: Uses standard SD (Steepest Descent) method  
- Index ≥1: Uses HiSD (High-index Saddle Dynamics) method  

**Data Type**  
`int` (non-negative)  

**Default**  
`6`  

**Constraints**  
`0 ≤ max_index ≤ Dim`

--- 

**`MaxIndexGap` (Optional)** 
**Description**  
Maximum allowed index difference between parent and child saddle points during hierarchical search.  

**Data Type**  
`int` (positive)  

**Default**  
`1`  

**Example**  
If `MaxIndexGap = 2`:  
- Parent (index 4) → Children (indices 2, 3)  
- Parent (index 3) → Children (indices 1, 2)  

--- 

**`SameJudgement` (Optional)**  
**Description**  
Saddle point equivalence criterion.  

**Data Types**  
- `float` (positive): Threshold for 2-norm distance (default: 1e-3)  
- `Callable[[np.ndarray, np.ndarray], bool]`: Custom comparison function
  - **Input**: `np.ndarray` with shape `(d, 1)` (column vector)

**Example**  
```python
# Custom similarity check
def custom_judge(a, b):
    return np.linalg.norm(a - b) < 0.5 and abs(a[0] - b[0]) < 0.1
```

---

**`InitialEigenVectors` (Optional)**  
**Description**  
Initial guess for Hessian eigenvectors.

**Data Types**  
- `None`: (Default) Auto-initialize with k smallest eigenvectors  
- Manual input: `np.ndarray` of shape (d, k)  
where d is the dimension and k equals MaxIndex.

**Requirement**  
Column vectors must be orthonormal  

--- 

**`PerturbationMethod` (Optional)**  
**Description**  
Statistical distribution for saddle point exploration.  

**Data Type**  
`str`  

**Options**  

| Value | Description |  
|-------|-------------|  
| `uniform` (Default) | Uniform sampling |  
| `gaussian` | Normally distributed displacements |  

--- 

**`PerturbationRadius` (Optional)**  
**Description**  
Displacement magnitude for saddle perturbations.  

**Data Type**  
`float` (positive) 

**Default**  
`1e-4`  

--- 

**`PerturbationNumber` (Optional)**  
**Description**  
Number of directional probes per saddle point.  

**Note**  
Actual probes = `2 × PerturbationNumber` (bidirectional)  

**Data Type**  
`int` (positive) 

**Default**  
`2`  

--- 

**`EigenCombination` (Optional)**  
**Description**  
Strategy for eigenvector utilization in perturbations.  

**Data Type**  
`str`  

**Options**  

| Value | Computational Cost | Completeness |  
|-------|--------------------|--------------|  
| `all` (Default) | High | Exhaustive |  
| `min` | Low | Partial |  


