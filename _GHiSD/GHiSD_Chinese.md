---
layout: single
permalink: /GHiSD/GHiSD_Chinese
title: "​普适高阶鞍点动力学（GHiSD）"
sidebar:
    nav: Theory_Chinese
toc: true
toc_sticky: true
mathjax: true
---

# 1 非梯度自治动力系统中 $k$ 阶鞍点的描述

在 HiSD 算法中，我们处理的是二次 Fréchet 可微的能量泛函
$E(\boldsymbol{x})$，在这种情形下
$\boldsymbol{F}(\boldsymbol{x}) = -\nabla E(\boldsymbol{x})$
作为系统的自然力。GHiSD 算法则希望对于更一般的($d$维)非梯度自治动力系统

$$
\boldsymbol{\dot{x}} = \boldsymbol{F}(\boldsymbol{x}),\quad \boldsymbol{x} \in \mathbb{R}^d,\quad \boldsymbol{F} \in \mathcal{C}^r(\mathbb{R}^d,\mathbb{R}^d),\quad r \geq 2
\tag{1}
$$ 

也能做到搜索 $k$
阶鞍点，那么首先我们要说清楚在非梯度系统中鞍点的阶指的是什么。

在动力系统的问题中，我们用
$\mathbb{J}(\boldsymbol{x}) = \nabla \boldsymbol{F}(\boldsymbol{x})$
来表示 $\boldsymbol{F}(\boldsymbol{x})$ 的 Jacobi 矩阵；并用
$\langle \boldsymbol{x},\boldsymbol{y} \rangle = \boldsymbol{x}^{\top}\boldsymbol{y}$
来表示 $\mathbb{R}^n$ 中的内积；对于使得
$\boldsymbol{F}(\boldsymbol{\hat{x}}) = \boldsymbol{0}$ 的
$\boldsymbol{\hat{x}}$，我们可以称其为平衡点或驻点。

考虑平衡点附近的系统，令
$\boldsymbol{x} = \boldsymbol{\hat{x}} + \boldsymbol{y}$ 代入(1)并做 Taylor 展开可得

$$
\boldsymbol{\dot{y}} = \boldsymbol{\dot{x}} = \boldsymbol{F}(\boldsymbol{x}) = \boldsymbol{F}(\boldsymbol{\hat{x}}) + \mathbb{J}(\boldsymbol{\hat{x}})\boldsymbol{y} + \mathcal{O}(\|\boldsymbol{y}\|^2)
$$

注意到
$\boldsymbol{F}(\boldsymbol{\hat{x}}) = 0$，只保留上式的线性主项可得平衡点附近的关联线性系统

$$
\boldsymbol{\dot{y}} = \mathbb{J}(\boldsymbol{\hat{x}})\boldsymbol{y}
$$

考虑将 $\mathbb{J}(\boldsymbol{\hat{x}})$
的（广义）右特征向量按照对应特征值的实部的符号来分类，具体来说：

-   $$
    \{\boldsymbol{w}_1,\ldots,\boldsymbol{w}_{k_u}\} \subset \mathbb{C}^d
    $$
    对应实部为正的特征值，对应于平衡点的不稳定子空间 
    $$
    \mathcal{W}^u(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_1,\ldots,\boldsymbol{w}_{k_u}\} \cap \mathbb{R}^d
    $$
     ，称其不稳定是因为系统在平衡点附近在这些方向上的扰动会指数级增长从而远离平衡点。

-   $$
    \{\boldsymbol{w}_{k_u+1},\ldots,\boldsymbol{w}_{k_u+k_s}\} \subset \mathbb{C}^d
    $$
    对应实部为负的特征值，对应于平衡点的稳定子空间 
    $$
    \mathcal{W}^s(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_{k_u+1},\ldots,\boldsymbol{w}_{k_u+k_s}\} \cap \mathbb{R}^d
    $$
     ，称其稳定是因为系统在平衡点附近在这些方向上的扰动会指数级衰减从而靠近平衡点。

-   $$
    \{\boldsymbol{w}_{k_u+k_s+1},\ldots,\boldsymbol{w}_{k_u+k_s+k_c}\} \subset \mathbb{C}^d
    $$
    对应实部为$0$的特征值，对应于平衡点的中心子空间 
    $$
    \mathcal{W}^c(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_{k_u+k_s+1},\ldots,\boldsymbol{w}_{k_u+k_s+k_c}\} \cap \mathbb{R}^d
    $$
     ，系统在这些方向上的扰动不呈现指数增长或衰减，而是具有周期性振荡或其他更复杂的动态行为。

上面 $k_u+k_s+k_c=d$ 根据主分解定理，可以将 $\mathbb{R}^d$ 直和分解为
$\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^s(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^c(\boldsymbol{\hat{x}})$
。特别地，

-   如果$\mathbb{J}(\boldsymbol{\hat{x}})$的特征值实部均不为$0$，即$\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^s(\boldsymbol{\hat{x}})$，这样的平衡点被称为双曲的，这一类平衡点也是我们的主要研究对象。

-   如果$\mathbb{J}(\boldsymbol{\hat{x}})$的特征值实部均为正，即$\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}})$，则称$\boldsymbol{\hat{x}}$为源点。

-   如果$\mathbb{J}(\boldsymbol{\hat{x}})$的特征值实部均为负，即$\mathbb{R}^d = \mathcal{W}^s(\boldsymbol{\hat{x}})$，则称$\boldsymbol{\hat{x}}$为汇点。

我们可以将梯度系统中的概念与上述概念之间做一个对应：梯度系统中给定二次Fréchet可微的能量泛函$E(\boldsymbol{x})$，有自然力$\boldsymbol{F}(\boldsymbol{x})=-\nabla E(\boldsymbol{x})$，从而能量函数的Hessian矩阵$\mathbb{G}(\boldsymbol{x}) =\nabla^2E(\boldsymbol{x})=-\nabla\boldsymbol{F}(\boldsymbol{x})=-\mathbb{J}(\boldsymbol{x})$

我们将平衡点的不稳定子空间的维数$k_u$（对应于梯度系统中临界点的Hessian矩阵的最大负定子空间维数）称为它的阶，与HiSD文档中说的类似，有时我们也将汇点（对应于能量极小点）成为$0$阶鞍点，源点（对应于能量极大点）称为$d$阶鞍点，所以有时也统一地将$k$阶平衡点称为$k$阶鞍点。接下来的部分我们将介绍如何在非梯度自治动力系统中搜索$k$阶鞍点。

# 2 $\boldsymbol{x}$ 的动力学

$\boldsymbol{x}$的动力学构建的整体想法与HiSD类似，在平衡点附近的稳定子空间方向上，力的作用效果是靠近平衡点，而在不稳定子空间方向上则是远离平衡点。故直观上我们仍然可以让$\boldsymbol{\dot{x}}$在稳定子空间中保持系统力的方向，而在不稳定子空间中选择与系统力相反的方向，即

$$
\boldsymbol{\dot{x}} = -\mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})} \boldsymbol{F}(\boldsymbol{x}) + \left( \boldsymbol{F}(\boldsymbol{x}) - \mathcal{P}_{\mathcal{W}^u(\boldsymbol{x})} \boldsymbol{F}(\boldsymbol{x}) \right) = \left( \mathbb{I} - 2\mathcal{P}_{\mathcal{W}^u(\boldsymbol{x})} \right) \boldsymbol{F}(\boldsymbol{x})
$$

注意上面的动力学中由于我们不清楚$k$阶鞍点的不稳定子空间$\mathcal{W}^u(\boldsymbol{\hat{x}})$，所以考虑用当前点的不稳定子空间$\mathcal{W}^u(\boldsymbol{x})$来近似（更准确地说，其实是$\mathcal{W}^u(\boldsymbol{x})$的$k$维子空间，因为实际计算中使用$k$个向量构成的基底来近似，但后文统称为$\mathcal{W}^u(\boldsymbol{x})$）。其中非平衡点的不稳定子空间定义与前述平衡点处的一致，尽管其物理意义不如平衡点处清晰。

根据上面给出的动力学，我们可以知道下一步的目标是找到空间$\mathcal{W}^u(\boldsymbol{x})$的近似方式，更直接地说，是找到变换$\mathcal{P}_{\mathcal{W}^u(\boldsymbol{x})}$的近似方式。而要刻画投影变换，我们一般考虑找到该空间的一组正交基$\boldsymbol{v}_1,\boldsymbol{v}_2,\ldots,\boldsymbol{v}_k$，从而可以得到

$$
\mathcal{P}_{\mathcal{W}^u(\boldsymbol{x})}=\sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^{\top}
$$

进而

$$
\boldsymbol{\dot{x}} = \left( \mathbb{I} - 2 \sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^\top \right) \boldsymbol{F}(\boldsymbol{x})
\tag{2}
$$


# 3 寻找 $\mathcal{W}^u(\boldsymbol{x})$ 的正交基

## 3.1 一个简洁有效的离散算法

从定义出发，为了找到$\mathcal{W}^u(\boldsymbol{x})$的近似正交基，可以考虑寻找$\mathbb{J}(\boldsymbol{x})$实部为正的特征值对应的特征向量的近似，特别地，在求解$k$阶鞍点的过程中可以视为寻找实部最大的$k$个特征向量的近似。

注意到动力学$\boldsymbol{\dot{v}}=\mathbb{J}(\boldsymbol{x})\boldsymbol{v}$会使得$\boldsymbol{v}$的方向以指数速度趋近于$\mathbb{J}(\boldsymbol{x})$实部最大的特征值对应的特征向量方向（若同时有多个实部最大且相同的的特征值，它们的特征向量构成空间$\mathcal{W}$，则$\boldsymbol{v}$的方向以指数趋向于在$\mathcal{W}$上的投影）。

而对于找前$k$个实部较大的特征值对应的特征向量构成的空间，直观上的想法是，用上述迭代得到实部最大特征值对应特征向量的近似后，在空间中去掉在此方向上的投影，再在剩下的子空间中继续用上述方法求得子空间中的最大、原空间中的次大特征值对应的特征向量，这样的想法可以类似地从2个推广到$k$个。而这个过程换言之其实也就是对这些向量做正交化操作（由于我们只关心方向，所以可以做标准正交化），由此我们得到一个简洁的离散算法:

$$
\begin{cases}
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i^{(m)} \hspace{1em} i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\tag{3}
\end{cases}
$$

其中$\text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)$表示标准正交化过程，一般采用Gram-Schmidt正交化方法。此外，类似于HiSD，结合dimer方法可对$\mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i^{(m)}$做近似得到：

$$
\begin{cases}
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \dfrac{\boldsymbol{F}(\boldsymbol{x} + l \boldsymbol{v}_i^{(m)}) - \boldsymbol{F}(\boldsymbol{x} - l \boldsymbol{v}_i^{(m)})}{2l} \quad i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\end{cases}
$$

再结合$\boldsymbol{x}$的动力学离散化即得： 

$$
\begin{cases}
\boldsymbol{x}^{(m+1)} = \boldsymbol{x}^{(m)} + \alpha \left( \boldsymbol{F}(\boldsymbol{x}^{(m)}) - 2 \displaystyle\sum_{j=1}^{k} \left\langle \boldsymbol{F}(\boldsymbol{x}^{(m)}), \boldsymbol{v}_j^{(m)} \right\rangle \boldsymbol{v}_j^{(m)} \right) \\
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \dfrac{\boldsymbol{F}(\boldsymbol{x}^{(m+1)} + l \boldsymbol{v}_i^{(m)}) - \boldsymbol{F}(\boldsymbol{x}^{(m+1)} - l \boldsymbol{v}_i^{(m)})}{2l}\quad i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\end{cases}
\tag{4}
$$

## 3.2 $\mathcal{W}^u(\boldsymbol{x})$ 的动力学与直接离散化

将上述离散形式(3)（包括正交化过程）令$\beta \rightarrow0$可得连续化ODE形如：

$$
\boldsymbol{\dot{v}}_i=\mathbb{J}(\boldsymbol{x})\boldsymbol{v}_i+\displaystyle \sum_{j=1}^{i}\xi^{(i)}_j\boldsymbol{v}_j
$$

再注意到标准正交约束

$$
\left\langle \boldsymbol{v}_i,\boldsymbol{v}_j \right\rangle=\delta_{ij}\hspace{1em}i,j=1,\ldots,k
$$

关于$t$求导即得

$$
\left\langle \boldsymbol{\dot{v}}_i,\boldsymbol{v}_j \right\rangle+\left\langle \boldsymbol{v}_i,\boldsymbol{\dot{v}}_j \right\rangle=0 \hspace{1em}i,j=1,\ldots,k
$$

代入可求得

$$
\xi_{i}^{(i)} = -\langle \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i, \boldsymbol{v}_i \rangle
$$

$$
\xi_{j}^{(i)} = -\langle \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i, \boldsymbol{v}_j \rangle - \langle \boldsymbol{v}_i, \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_j \rangle \quad j = 1, \cdots, i-1
$$

由此结合(2)式可得整个问题的动力学:

$$
\begin{cases} 
\dot{\boldsymbol{x}} = \left( \mathbb{I} - 2 \displaystyle \sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^\top \right) \boldsymbol{F}(\boldsymbol{x}),\\
\dot{\boldsymbol{v}}_i = \left( \mathbb{I} - \boldsymbol{v}_i \boldsymbol{v}_i^\top \right) \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i - \displaystyle \sum_{j=1}^{i-1} \boldsymbol{v}_j \boldsymbol{v}_j^\top \left( \mathbb{J}(\boldsymbol{x}) + \mathbb{J}^\top(\boldsymbol{x}) \right) \boldsymbol{v}_i,\quad i = 1, \cdots, k
\end{cases}
$$ 

该动力学的线性稳定性证明详见参考文献[1]。

事实上，得到这个动力学以后我们可以对其做直接离散化而得到新的数值算法，但这种算法相比之前的离散格式计算量要更大，因为实际计算过程中，离散化格式的正交性保持仍然需要Gram-Schmidt正交化的修正。此外，参考文献[2]中证明了两种离散格式的实际效果相差不大，所以出于计算量的考虑，我们往往直接使用更简单的离散格式(4)。

# 4 解景观的构建

HiSD系列算法的目标不仅是搜索到$k$阶鞍点，我们还要给出各阶鞍点之间的搜索关系，从而完成解景观的构建，让我们的搜索更加系统，对鞍点之间的联系有更深刻的理解。下面我们将给出从高阶鞍点向低阶鞍点搜索的向下搜索算法以及从低阶鞍点向高阶鞍点搜索的向上搜索算法。

## 4.1 向下搜索算法

我们给出从$\hat{k}$阶鞍点出发，搜索$\hat{k}-1$阶鞍点并进一步搜索更低阶鞍点直至$0$阶鞍点（汇点）的算法，并记录搜索关系。
核心步骤是从$k$阶鞍点搜索$m(m<k)$阶鞍点（一般每次搜索相邻阶数的鞍点，不过也支持跳阶搜索，所以我们这里叙述的是更普遍的情形），其大致思想是将$k$阶鞍点沿一个不稳定方向扰动得到迭代的初始点，并从余下$k-1$个与该方向正交的不稳定方向选择$m$个作为迭代的初始不稳定子空间方向，从而被选出的扰动方向在迭代时力沿系统作用力正向，又由于其为不稳定方向，所以$\boldsymbol{x}$将会逃离当前鞍点并向$m$阶鞍点演化。

## 4.2 向上搜索算法

向下搜素法可以让我们从高阶鞍点系统地搜索低阶鞍点，反过来我们也可以从低阶鞍点出发搜索高阶鞍点（之后再从高阶鞍点向下搜素从而得到更多的鞍点）。
这个算法的核心步骤是从$k$阶鞍点搜索$m(m>k)$阶鞍点，那么类似于上面的想法，我们将$k$阶鞍点沿一个稳定方向扰动得到迭代的初始点，并将该方向和原有的$k$个不稳定方向再补上$m-k-1$个其他稳定方向作为迭代的初始方向，从而被选出的扰动方向在迭代时力沿系统作用力负向，又由于其为稳定方向，所以$\boldsymbol{x}$将会逃离当前鞍点并向$m$阶鞍点演化。

# 5 总结

我们介绍了非梯度系统中如何系统地搜索$k$阶鞍点的GHiSD方法，可以说是HiSD算法在更一般问题上的推广，其中$\boldsymbol{x}$在不稳定子空间上沿作用力反方向，在其补空间上沿作用力方向以及利用dimer近似等思想都起着非常重要的作用。最后我们还介绍了利用GHiSD算法构建解景观的方式，让我们对于各阶鞍点之间的联系有更深的理解，也让我们的搜索更加系统和全面。

# 6 参考文献

1. Yin, J., Yu, B., & Zhang, L. (2020). Searching the solution landscape by generalized high-index saddle dynamics. _Science China Mathematics_, ​**64**(8). [https://doi.org/10.1007/s11425-020-1737-1](https://doi.org/10.1007/s11425-020-1737-1)

2. Zhang, L., Zhang, P., & Zheng, X. (2024). Understanding high-index saddle dynamics via numerical analysis. _Communications in Mathematical Sciences_, ​**23**(2). [https://doi.org/10.4310/CMS.241217235844](https://doi.org/10.4310/CMS.241217235844)
