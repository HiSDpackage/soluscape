---
layout: single
permalink: /AHiSD/AHiSD_English
title: "Accelerated High-index Saddle Dynamics"
sidebar:
    nav: Theory
toc: false
toc_sticky: false
mathjax: true
---

In this chapter, we briefly introduce two momentum-accelerated
algorithms of HiSD. The relevant theories and numerical experimental
results can be found in Reference [1].

The first one is the heavy-ball acceleration: 

$$
\begin{cases}
\boldsymbol{x}^{(n+1)} = \boldsymbol{x}^{(n)} + \beta_n \left( \mathbb{I} - 2 \sum_{i=1}^{k} \boldsymbol{v}_i^{(n)} {\boldsymbol{v}_i^{(n)}}^\top \right) \boldsymbol{F}(\boldsymbol{x}^{(n)}) + \gamma (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)}) \\
\left\{\boldsymbol{v}_i^{(n+1)}\right\}_{i=1}^{k} = \text{EigenSol} \left\{ \mathbb{G}(\boldsymbol{x}^{(n+1)}), \left\{\boldsymbol{v}_i^{(n)}\right\}_{i=1}^{k} \right\}
\end{cases}
$$

The second one is the Nesterov's acceleration: 

$$
\begin{cases}
\boldsymbol{w}^{(n)} = \boldsymbol{x}^{(n)} + \gamma_n (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)})\\
\boldsymbol{x}^{(n+1)} = \boldsymbol{w}^{(n)} + \beta_n \left( \mathbb{I} - 2 \sum_{i=1}^{k} \boldsymbol{v}_i^{(n)} {\boldsymbol{v}_i^{(n)}}^\top \right) \boldsymbol{F}(\boldsymbol{w}^{(n)})\\
\left\{\boldsymbol{v}_i^{(n+1)}\right\}_{i=1}^{k} = \text{EigenSol} \left\{ \mathbb{G}(\boldsymbol{x}^{(n+1)}), \left\{\boldsymbol{v}_i^{(n)}\right\}_{i=1}^{k} \right\}
\end{cases}
$$

Where:

-   $\text{EigenSol} \left\{ \mathbb{G}(\boldsymbol{x}^{(n+1)}), \left\{\boldsymbol{v}_i^{(n)}\right\}_{i=1}^{k} \right\}$
    is the eigenvector solver, which can use the direct discretization
    of HiSD dynamics or algorithms like LOBPCG.

-   The step size $\beta_n$ is similar to that in the HiSD algorithm
    and can be handled using Euler's method, line search methods, and
    the BB step size method.

-   The momentum acceleration term
    $\gamma (\boldsymbol{x}^{(n)} - \boldsymbol{x}^{(n-1)})$ is the core
    of the acceleration. In the heavy-ball acceleration,
    $\gamma \in [0,1)$ is generally taken as a constant, while in the
    Nesterov's acceleration, $\gamma_n$ has several options, such as
    
    $$
    \gamma_n = \frac{n}{n+3}
    $$
    
     or

    
    $$
    \gamma_n = \theta_{n+1}^{-1} (\theta_n - 1) \quad \theta_{n+1} = \frac{1 + \sqrt{1 + 4\theta_n^2}}{2}, \theta_0 = 1
    $$
    
    In numerical experiments, the effects of these two choices are
    generally not significantly different, so we usually choose the
    simpler former form.
    
# References

1. Luo, Y., Zhang, L., & Zheng, X. (2025). Accelerated high-index saddle dynamics method for searching high-index saddle points. _Journal of Scientific Computing_, ​**102**(3). [https://doi.org/10.1007/s10915-024-02760-6](https://doi.org/10.1007/s10915-024-02760-6)
