---
layout: single
permalink: /Tutorial/ConfigurationParameters_Chinese
title: ""
sidebar:
    nav: Tutorial_Chinese
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
      
一个基于高阶鞍点动力学（HiSD）构建解景观的Python工具包。该工具包支持动力系统中鞍点的数值计算及其层级结构分析，简化了鞍点搜索流程，提供灵活的参数设置和丰富的可视化功能。

---
## 配置参数

`soluscape` 包的配置参数分为不同的类别，每个类别专注于算法的特定部分。以下是不同类别及其相关参数的概述。

### 系统参数
这些参数与系统设置及其一般属性相关：`Dim`、`EnergyFunction`、`Grad`、`AutoDiff`、`NumericalGrad`、`DimerLength`、`SymmetryCheck` 和 `GradientSystem`。

**`Dim`（可选）​**  
**描述**  
系统维度规格。  

**数据类型**  
`int`（正整数）  

**行为**  
- 默认值：从 `InitialPoint` 推断  
- 手动覆盖必须与以下维度匹配：  
  - `InitialPoint`  
  - `InitialSearchDirection`  

--- 

**`EnergyFunction`（条件性必填）​**  
**描述**  
指定梯度系统的能量函数。  

**数据类型**  
- Python 函数：`Callable[[np.ndarray], float]`  
  - ​**输入**：形状为 `(d, 1)` 的 `np.ndarray`（列向量）  
- 符号表达式：`str`  
  - ​**规范**：使用 `x1, x2, ..., xd` 作为变量，并支持完整的 `sympy` 语法  

**示例**  
```python
EnergyFunction = '''
0.4*x1**2 - 0.2*x1*x2 + 0.25*x2**2 
- 5*(atan(x1-5) + atan(x2-5))
'''
```

--- 

**`Grad`（条件性必填）​**  
**描述**  
指定梯度系统的梯度函数或非梯度系统的向量场。  

**要求**  
- 对于梯度系统：$\nabla$E  
- 对于非梯度系统：直接指定 $\dot{x} = -F(x)$ 中的 F  

**数据类型**  
- Python 函数：`Callable[[np.ndarray], np.ndarray]`  
  - ​**输入/输出**：形状为 `(d, 1)` 的 `np.ndarray`（列向量）  
- 符号表达式列表：`list[str]`（例如 `["2*x1", "cos(x2)"]`）  

**示例**  
```python
# Gradient system
Grad = ["2*x1", "2*x2"]

# Non-gradient system 
Grad = ["x2", "-x1 - 0.1*x2"]
```

---

**`AutoDiff`（可选）​**  
**描述**  
启用能量函数的自动微分。  

**数据类型**  
`bool`  

**选项**  
- `True`：需要提供 `EnergyFunction` 参数  
- `False`：需要手动指定 `Grad` 参数  

**行为**  
- 如果提供了 `EnergyFunction`，则默认为 `True`  
- 如果提供了 `Grad`，则默认为 `False`  

---

**`NumericalGrad`（可选）​**  
**描述**  
启用数值梯度近似。  

**适用性**  
仅在未指定 `Grad` 时生效  

**数据类型**  
`bool`  

**选项**  
- `True`：使用有限差分近似  
- `False`：（默认）使用 `EnergyFunction` 的解析梯度  

--- 

**`DimerLength`（可选）​**  
**描述**  
数值梯度近似的位移长度。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-5`  

---

**`SymmetryCheck`（可选）​**  
**描述**  
通过 Hessian 对称性验证梯度系统属性。  

**数据类型**  
`bool`  

**行为**  
- `True`：（默认）自动检测  
- `False`：跳过检查（提高性能）  

--- 

**`GradientSystem`（可选）​**  
**描述**  
显式声明梯度系统的性质。  

**用法**  
当已知系统性质时，覆盖自动检测。  

**数据类型**  
`bool`  

**行为**  
- 未指定：自动检测  

--- 

### Hessian 参数
这些参数与 Hessian 矩阵相关：`ExactHessian` 和 `HessianDimerLength`。

**`ExactHessian`（可选）​**  
**描述**  
控制 Hessian 矩阵的计算方法。  

**数据类型**  
`bool`  

**选项**  
- `True`：从符号梯度计算解析 Hessian  
- `False`：（默认）基于 Dimer 的近似  

**要求**  
需要 `Grad` 为符号表达式  

--- 

**`HessianDimerLength`（可选）​**  
**描述**  
数值 Hessian-向量积近似的位移长度。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-5`  

--- 

### 特征参数
这些参数控制特征对（特征值和特征向量）的计算方式：`EigenMethod`、`EigenMaxIter`、`EigenStepSize` 和 `PrecisionTol`。

**`EigenMethod`（可选）​**  
**描述**  
用于稳定性分析的特征求解器选择。  

**数据类型**  
`str`  

**选项**  

| 方法      | 系统类型          | 描述                          |
|-----------|-------------------|-------------------------------|
| `lobpcg`  | 梯度系统（默认）   | 局部最优块预条件共轭梯度法     |
| `euler`   | 梯度 & 非梯度系统 | 显式欧拉离散化                 |
| `power`   | 非梯度系统（默认） | 幂法                          |

--- 

**`EigenMaxIter`（可选）​**  
**描述**  
特征对计算的最大迭代次数。  

**数据类型**  
`int`（正整数）  

**默认值**  
`10`  

--- 

**`EigenStepSize`（可选）​**  
**描述**  
欧拉/幂法的离散化步长。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-7`  

--- 

**`PrecisionTol`（可选）​**  
**描述**  
特征值的精度容差。（如果特征值的绝对值小于容差，则将其视为 0。）  

**数据类型**  
`float`（非负数）  

**默认值**  
`1e-5`   

--- 

### 加速参数
这些参数与提高算法的速度和效率相关：`BBStep`、`Acceleration`、`NesterovChoice`、`NesterovRestart` 和 `Momentum`。

**`BBStep`（可选）​**  
**描述**  
启用 Barzilai-Borwein 自适应步长调整。  

**数据类型**  
`bool`  

**默认值**  
`False`  

**权衡**  
- 可能加速收敛  
- 可能导致刚性系统不稳定  

---

**`Acceleration`（可选）​**  
**描述**  
收敛加速技术。  

**数据类型**  
`str`  

**选项**  
- `none`：（默认）无加速  
- `heavyball`：基于动量的加速  
- `nesterov`：Nesterov 加速动力学  

--- 

**`NesterovChoice`（可选）​**  
**描述**  
指定 Nesterov 方法的加速参数序列。  

**数据类型**  
`int`  

**选项**  
- `1`：（默认）$\gamma_{n}=\frac{n}{n+3}$。  
- `2`：$\gamma_{n}=\frac{\theta_{n}-1}{\theta_{n+1}}$，其中 $\theta_{n+1}=\frac{1+\sqrt{1+4\theta_{n}^{2}}}{2}$，$\theta_{0}=1$。  

**默认值**  
`1`  

--- 

**`NesterovRestart`（可选）​**  
**描述**  
Nesterov 动量重置的迭代间隔。  

**数据类型**  
`int`（正整数） | `None`  

**行为**  
- `None`：禁用动量重置  
- 整数 `n`：每 `n` 次迭代重置动量  

**默认值**  
`None`  

--- 

**`Momentum`（可选）​**  
**描述**  
Heavy ball 加速的动量系数。  

**数据类型**  
`float`（非负数）  

**默认值**  
`0.0`  

**约束**  
- `0.0 ≤ Momentum < 1.0`  
- `0.0`：等效于无加速  

--- 

### 求解器参数
这些参数与求解过程相关，控制 HiSD 过程的行为：`InitialPoint`、`Tolerance`、`SearchArea`、`TimeStep`、`MaxIter`、`SaveTrajectory`、`Verbose` 和 `ReportInterval`。

**`InitialPoint`（必填）​**  
**描述**  
鞍点搜索的起始坐标。  

**数据类型**  
`list` | `numpy.ndarray`（一维数组）  

**示例**  
`initial_point = [0.5, -1.2]`  

---

**`Tolerance`（可选）​**  
**描述**  
鞍点迭代的收敛阈值。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-6`  

**停止准则**  
‖梯度向量‖$_2$ < Tolerance  

--- 

**`SearchArea`（可选）​**  
**描述**  
从初始点出发的最大探索半径。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e3`  

**效果**  
如果 ‖x - x$_0$‖$_2$ > SearchArea，则终止搜索  

--- 

**`TimeStep`（可选）​**  
**描述**  
动力学的时间离散化间隔。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-4`  

--- 

**`MaxIter`（可选）​**  
**描述**  
允许的最大 HiSD 迭代次数。  

**数据类型**  
`int`（正整数）  

**默认值**  
`1000`  

--- 

**`SaveTrajectory`（可选）​**  
**描述**  
在计算过程中记录完整的优化路径。  

**数据类型**  
`bool`  

**默认值**  
`True`  

--- 

**`Verbose`（可选）​**  
**描述**  
控制实时进度报告。  

**输出**  
打印迭代次数和梯度范数。  

**数据类型**  
`bool`  

**默认值**  
`False`  

--- 

**`ReportInterval`（可选）​**  
**描述**  
当 `Verbose=True` 时，控制台输出的迭代频率。  

**数据类型**  
`int`（正整数）  

**默认值**  
`100`  

--- 

### 解景观参数
这些参数与构建和导航解景观相关：`MaxIndex`、`MaxIndexGap`、`SameJudgement`、`InitialEigenVectors`、`PerturbationMethod`、`PerturbationRadius`、`PerturbationNumber` 和 `EigenCombination`。

**`MaxIndex`（可选）​**  
**描述**  
要计算的鞍点最大阶数（k）。  
- 阶数 0：使用标准 SD（最速下降）方法  
- 阶数 ≥1：使用 HiSD（高阶鞍点动力学）方法  

**数据类型**  
`int`（非负数）  

**默认值**  
`6`  

**约束**  
`0 ≤ max_index ≤ Dim`  

--- 

**`MaxIndexGap`（可选）​**  
**描述**  
在层次搜索中，父鞍点与子鞍点之间允许的最大阶数差。  

**数据类型**  
`int`（正整数）  

**默认值**  
`1`  

**示例**  
如果 `MaxIndexGap = 2`：  
- 父鞍点（阶数 4）→ 子鞍点（阶数 2, 3）  
- 父鞍点（阶数 3）→ 子鞍点（阶数 1, 2）  

--- 

**`SameJudgement`（可选）​**  
**描述**  
鞍点等价性判断标准。  

**数据类型**  
- `float`（正数）：2-范数距离的阈值（默认：1e-3）  
- `Callable[[np.ndarray, np.ndarray], bool]`：自定义比较函数  
  - ​**输入**：形状为 `(d, 1)` 的 `np.ndarray`（列向量）  

**示例**  
```python
# Custom similarity check
def custom_judge(a, b):
    return np.linalg.norm(a - b) < 0.5 and abs(a[0] - b[0]) < 0.1
```

---

**`InitialEigenVectors`（可选）​**  
**描述**  
Hessian 特征向量的初始猜测。  

**数据类型**  
- `None`：（默认）自动初始化 k 个最小特征向量  
- 手动输入：形状为 (d, k) 的 `np.ndarray`  
其中 d 是维度，k 等于 MaxIndex。  

**要求**  
列向量必须正交归一化  

--- 

**`PerturbationMethod`（可选）​**  
**描述**  
鞍点探索的统计分布。  

**数据类型**  
`str`  

**选项**  

| 值            | 描述          |  
|---------------|---------------|  
| `uniform`（默认） | 均匀采样      |  
| `gaussian`     | 正态分布位移  |  

--- 

**`PerturbationRadius`（可选）​**  
**描述**  
鞍点扰动的位移幅度。  

**数据类型**  
`float`（正数）  

**默认值**  
`1e-4`  

--- 

**`PerturbationNumber`（可选）​**  
**描述**  
每个鞍点的方向探测次数。  

**注意**  
实际探测次数 = `2 × PerturbationNumber`（双向）  

**数据类型**  
`int`（正整数）  

**默认值**  
`2`  

--- 

**`EigenCombination`（可选）​**  
**描述**  
在扰动中利用特征向量的策略。  

**数据类型**  
`str`  

**选项**  

| 值            | 计算成本      | 完整性        |  
|---------------|---------------|---------------|  
| `all`（默认） | 高            | 全面          |  
| `min`         | 低            | 部分          |  


