---
layout: single
permalink: /AHiSD/AHiSD_Chinese
title: "加速高阶鞍点动力学(AHiSD)"
sidebar:
    nav: Theory_Chinese
toc: false
toc_sticky: false
mathjax: true
---

这一章我们简单介绍两种HiSD的动量加速算法，其相关理论和数值实验结果详见参考文献[1]。

第一种是重球加速法 

$$
\begin{cases}
\boldsymbol{x}^{(n+1)} = \boldsymbol{x}^{(n)} + \beta_n \left( \mathbb{I} - 2 \displaystyle \sum_{i=1}^{k} \boldsymbol{v}_i^{(n)} {\boldsymbol{v}_i^{(n)}}^\top \right) \boldsymbol{F}(\boldsymbol{x}^{(n)}) + \gamma (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)}), \\
\left\{\boldsymbol{v}_i^{(n+1)}\right\}_{i=1}^{k} = \text{EigenSol} \left\{ \mathbb{G}(\boldsymbol{x}^{(n+1)}), \left\{\boldsymbol{v}_i^{(n)}\right\}_{i=1}^{k} \right\}.
\end{cases}
$$

第二种是Nesterov加速法 

$$
\begin{cases}
\boldsymbol{w}^{(n)} = \boldsymbol{x}^{(n)} + \gamma_n (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)}),\\
\boldsymbol{x}^{(n+1)} = \boldsymbol{w}^{(n)} + \beta_n \left( \mathbb{I} - 2 \displaystyle \sum_{i=1}^{k} \boldsymbol{v}_i^{(n)} {\boldsymbol{v}_i^{(n)}}^\top \right) \boldsymbol{F}(\boldsymbol{w}^{(n)}),\\
\left\{\boldsymbol{v}_i^{(n+1)}\right\}_{i=1}^{k} = \text{EigenSol} \left\{ \mathbb{G}(\boldsymbol{x}^{(n+1)}), \left\{\boldsymbol{v}_i^{(n)}\right\}_{i=1}^{k} \right\}.
\end{cases}
$$ 

其中

-    $\text{EigenSol}$ 为特征向量求解器，既可以使用HiSD动力学的直接离散化，也可以使用LOBPCG等算法来处理。

-   步长$\beta_n$与HiSD算法中类似，可以考虑用Euler格式、线搜索方法和BB步长法来处理

-   动量加速 $\gamma (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)})$ 是加速的核心，其中重球加速中$\gamma\in[0,1)$一般取为常数，而Nesterov加速 $\gamma_n$ 有多种选择，例如
      
    $$
    \gamma_n = \frac{n}{n+3}
    $$
    
    或者
    
    $$
    \gamma_n = \theta_{n+1}^{-1} (\theta_n - 1) \quad \theta_{n+1} = \frac{1 + \sqrt{1 + 4\theta_n^2}}{2}, \theta_0 = 1
    $$
    
    数值实验中两种选择的效果一般相差不大，所以我们一般选用形式更简单的前者

# 参考文献

1. Luo, Y., Zhang, L., & Zheng, X. (2025). Accelerated high-index saddle dynamics method for searching high-index saddle points. _Journal of Scientific Computing_, ​**102**(3). [https://doi.org/10.1007/s10915-024-02760-6](https://doi.org/10.1007/s10915-024-02760-6)
