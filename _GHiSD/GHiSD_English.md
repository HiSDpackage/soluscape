---
layout: single
permalink: /GHiSD/GHiSD_English
title: "Generalized High-index Saddle Dynamics"
sidebar:
    nav: Theory
toc: true
toc_sticky: true
mathjax: true
---

# 1 Description of $k$-saddle in Non-Gradient Autonomous Dynamical Systems

In the HiSD algorithm, we deal with the energy functional
$E(\boldsymbol{x})$ that is twice Fréchet differentiable. In this case,
$\boldsymbol{F}(\boldsymbol{x}) = -\nabla E(\boldsymbol{x})$ serves as
the natural force of the system. The GHiSD algorithm, on the other hand,
aims to search for index-$k$ saddle points in more general
($d$-dimensional) non-gradient autonomous dynamical systems:

$$
\boldsymbol{\dot{x}} = \boldsymbol{F}(\boldsymbol{x}),\quad \boldsymbol{x} \in \mathbb{R}^d,\quad \boldsymbol{F} \in \mathcal{C}^r(\mathbb{R}^d,\mathbb{R}^d),\quad r \geq 2
\tag{1}
$$ 

First, we need to clarify what the index of a
saddle point refers to in non-gradient systems.

In the context of dynamical systems, we denote the Jacobian matrix of
$\boldsymbol{F}(\boldsymbol{x})$ as
$\mathbb{J}(\boldsymbol{x}) = \nabla \boldsymbol{F}(\boldsymbol{x})$;
and the inner product in $\mathbb{R}^n$ as
$\langle \boldsymbol{x},\boldsymbol{y} \rangle = \boldsymbol{x}^{\top}\boldsymbol{y}$.
For $\boldsymbol{\hat{x}}$ that satisfies
$\boldsymbol{F}(\boldsymbol{\hat{x}}) = \boldsymbol{0}$, we can refer to
it as an equilibrium point or stationary point.

Considering the system near the equilibrium point, let
$\boldsymbol{x} = \boldsymbol{\hat{x}} + \boldsymbol{y}$ and substitute
it into (1), then perform a Taylor expansion:

$$
\boldsymbol{\dot{y}} = \boldsymbol{\dot{x}} = \boldsymbol{F}(\boldsymbol{x}) = \boldsymbol{F}(\boldsymbol{\hat{x}}) + \mathbb{J}(\boldsymbol{\hat{x}})\boldsymbol{y} + \mathcal{O}(\|\boldsymbol{y}\|^2)
$$

Noting that $\boldsymbol{F}(\boldsymbol{\hat{x}}) = 0$, and retaining
only the principal linear term of the above equation, we obtain the
associated linear system near the equilibrium point:

$$
\boldsymbol{\dot{y}} = \mathbb{J}(\boldsymbol{\hat{x}})\boldsymbol{y}
$$

Consider classifying the (generalized) right eigenvectors of
$\mathbb{J}(\boldsymbol{\hat{x}})$ according to the sign of the real
part of the corresponding eigenvalues. Specifically:

-   $$
    \{\boldsymbol{w}_1,\ldots,\boldsymbol{w}_{k_u}\} \subset \mathbb{C}^d
    $$correspond to eigenvalues with positive real parts, associated with
    the unstable subspace of the equilibrium point
    $$
    \mathcal{W}^u(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_1,\ldots,\boldsymbol{w}_{k_u}\} \cap \mathbb{R}^d
    $$.It is called unstable because perturbations in these directions near
    the equilibrium point will grow exponentially, moving away from the
    equilibrium point.

-   $$
    \{boldsymbol{w}_{k_u+1},\ldots,\boldsymbol{w}_{k_u+k_s}\} \subset \mathbb{C}^d
    $$correspond to eigenvalues with negative real parts, associated with
    the stable subspace of the equilibrium point
    $$
    \mathcal{W}^s(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_{k_u+1},\ldots,\boldsymbol{w}_{k_u+k_s}\} \cap \mathbb{R}^d
    $$.It is called stable because perturbations in these directions near
    the equilibrium point will decay exponentially, moving towards the
    equilibrium point.
   
    
-   $$
    \{\boldsymbol{w}_{k_u+k_s+1},\ldots,\boldsymbol{w}_{k_u+k_s+k_c}\} \subset \mathbb{C}^d
    $$
    correspond to eigenvalues with zero real parts, associated with the
    center subspace of the equilibrium point
    $$
    \mathcal{W}^c(\boldsymbol{\hat{x}}) = \text{span}_\mathbb{C}\{\boldsymbol{w}_{k_u+k_s+1},\ldots,\boldsymbol{w}_{k_u+k_s+k_c}\} \cap \mathbb{R}^d
    $$
    .
    Perturbations in these directions do not exhibit exponential growth
    or decay, but instead have periodic oscillations or other more
    complex dynamic behaviors.

The above $k_u+k_s+k_c=d$ and according to the primary decomposition
theorem, $\mathbb{R}^d$ can be decomposed into a direct sum
$$
\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^s(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^c(\boldsymbol{\hat{x}})
$$
.
Specifically,

-   If all the eigenvalues of $\mathbb{J}(\boldsymbol{\hat{x}})$ have
    non-zero real parts, i.e.,
    $\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}}) \oplus \mathcal{W}^s(\boldsymbol{\hat{x}})$,
    such an equilibrium point is called hyperbolic, and these types of
    equilibrium points are our main research objects.

-   If all the eigenvalues of $\mathbb{J}(\boldsymbol{\hat{x}})$ have
    positive real parts, i.e.,
    $\mathbb{R}^d = \mathcal{W}^u(\boldsymbol{\hat{x}})$, then
    $\boldsymbol{\hat{x}}$ is called a source point.

-   If all the eigenvalues of $\mathbb{J}(\boldsymbol{\hat{x}})$ have
    negative real parts, i.e.,
    $\mathbb{R}^d = \mathcal{W}^s(\boldsymbol{\hat{x}})$, then
    $\boldsymbol{\hat{x}}$ is called a sink point.

We can make a correspondence between the concepts in gradient systems
and the above concepts: In gradient systems, given a twice Fréchet
differentiable energy functional $E(\boldsymbol{x})$, the natural force
is $\boldsymbol{F}(\boldsymbol{x})=-\nabla E(\boldsymbol{x})$, and thus
the Hessian matrix of the energy function is
$\mathbb{G}(\boldsymbol{x}) =\nabla^2E(\boldsymbol{x})=-\nabla\boldsymbol{F}(\boldsymbol{x})=-\mathbb{J}(\boldsymbol{x})$.

We refer to the dimension of the unstable subspace of an equilibrium
point, $k_u$, (corresponding to the dimension of the maximum negative
definite subspace of the Hessian matrix of a critical point in gradient
systems) as its index. Similar to what is mentioned in the HiSD
documentation, sometimes we also call sink points (corresponding to
energy minima) as index-$0$ saddle points, and source points
(corresponding to energy maxima) as index-$d$ saddle points.
Therefore, we sometimes uniformly refer to index-$k$ equilibrium points
as index-$k$ saddle points. In the following sections, we will introduce
how to search for index-$k$ saddle points(for short,$k$-saddle,the same
applies to the following sections) in non-gradient autonomous dynamical
systems.

# 2 $\boldsymbol{x}$ Dynamics

The overall idea for constructing the dynamics of $\boldsymbol{x}$ is
similar to that of HiSD. Near an equilibrium point, the force's effect
is to approach the equilibrium point in the direction of the stable
subspace and to move away from it in the direction of the unstable
subspace. Therefore, intuitively, we can still allow
$\boldsymbol{\dot{x}}$ to maintain the direction of the system force in
the stable subspace and choose the opposite direction to the system
force in the unstable subspace, i.e.,

$$
\boldsymbol{\dot{x}} = -\mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})} \boldsymbol{F}(\boldsymbol{x}) + \left( \boldsymbol{F}(\boldsymbol{x}) - \mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})} \boldsymbol{F}(\boldsymbol{x}) \right) = \left( \mathbb{I} - 2\mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})} \right) \boldsymbol{F}(\boldsymbol{x})
$$

Note that in the dynamics above, since we do not know the unstable
subspace $\mathcal{W}^{\mathrm{u}}(\boldsymbol{\hat{x}})$ of the
$k$-saddle, we consider using the current point's unstable subspace
$\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$ as an approximation (more
accurately, the $k$-dimensional subspace of
$\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$, since in practical
calculations, an orthonormal basis formed by $k$ vectors is used to
approximate it, but we refer to it as
$\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$ in the following text). The
definition of the unstable subspace for non-equilibrium points is the
same as that at equilibrium points, although its physical significance
is not as clear.

Based on the given dynamics, our next goal is to find a way to
approximate the space $\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$, or
more directly, to find a way to approximate the transformation
$\mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})}$. To
characterize the projection transformation, we generally consider
finding an orthogonal basis
$\boldsymbol{v}_1, \boldsymbol{v}_2, \ldots, \boldsymbol{v}_k$ for this
space, which allows us to obtain

$$
\mathcal{P}_{\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})} = \sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^{\top}
$$

Thus,

$$
\boldsymbol{\dot{x}} = \left( \mathbb{I} - 2 \sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^\top \right) \boldsymbol{F}(\boldsymbol{x})
\tag{2}
$$


# 3 Finding an Orthogonal Basis for $\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$

## 3.1 A concise and efficient discrete algorithm

To find an approximate orthogonal basis for
$\mathcal{W}^{\mathrm{u}}(\boldsymbol{x})$, we can consider finding an
approximation of the eigenvectors corresponding to the eigenvalues with
positive real parts of $\mathbb{J}(\boldsymbol{x})$, especially when
solving for the $k$-saddle, which can be regarded as finding an
approximation of the $k$ eigenvectors corresponding to the largest real
parts(of the eigenvalue,the same applies to the following sections).

It is noted that the dynamics
$\boldsymbol{\dot{v}} = \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}$
causes the direction of $\boldsymbol{v}$ to exponentially approach the
direction of the eigenvectors corresponding to the largest real part
eigenvalues of $\mathbb{J}(\boldsymbol{x})$ (if there are multiple
eigenvalues with the same largest real part, their eigenvectors form a
space $\mathcal{W}$, and the direction of $\boldsymbol{v}$ exponentially
approaches the projection onto $\mathcal{W}$).

For the space formed by the eigenvectors corresponding to the $k$
eigenvalues with largest real parts, the intuitive idea is that after
iteratively obtaining an approximation of the eigenvector corresponding
to the eigenvalue with the largest real part using the above method, we
can remove the projection in this direction in the space, and continue
to use the same method in the remaining subspace to obtain the
eigenvector corresponding to the largest real part in the subspace,
which is the next largest in the original space. This idea can be
similarly extended from two to $k$ vectors, which is equivalent to
performing an orthogonalization operation on these vectors (since we are
only concerned with the direction, standard orthogonalization can be
applied), leading to a concise discrete algorithm: 

$$
\begin{cases}
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i^{(m)} \hspace{1em} i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\end{cases}
\tag{3}
$$

where
$\text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)$
represents the standard orthogonalization process, usually using the
Gram-Schmidt orthogonalization method. Additionally, similar to HiSD,
combining the dimer method allows for the approximation of
$\mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i^{(m)}$ as: 

$$
\begin{cases}
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \dfrac{\boldsymbol{F}(\boldsymbol{x} + l \boldsymbol{v}_i^{(m)}) - \boldsymbol{F}(\boldsymbol{x} - l \boldsymbol{v}_i^{(m)})}{2l} \quad i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\end{cases}
$$

Then, combining the discretization of $\boldsymbol{x}$
dynamics, we obtain:

$$
\begin{cases}
\boldsymbol{x}^{(m+1)} = \boldsymbol{x}^{(m)} + \alpha \left( \boldsymbol{F}(\boldsymbol{x}^{(m)}) - 2 \displaystyle\sum_{j=1}^{k} \left\langle \boldsymbol{F}(\boldsymbol{x}^{(m)}), \boldsymbol{v}_j^{(m)} \right\rangle \boldsymbol{v}_j^{(m)} \right) \\
\tilde{\boldsymbol{v}}_i^{(m+1)} = \boldsymbol{v}_i^{(m)} + \beta \dfrac{\boldsymbol{F}(\boldsymbol{x}^{(m+1)} + l \boldsymbol{v}_i^{(m)}) - \boldsymbol{F}(\boldsymbol{x}^{(m+1)} - l \boldsymbol{v}_i^{(m)})}{2l}\quad i = 1, \cdots, k \\
\left[ \boldsymbol{v}_1^{(m+1)}, \cdots, \boldsymbol{v}_k^{(m+1)} \right] = \text{orth} \left( \left[ \tilde{\boldsymbol{v}}_1^{(m+1)}, \cdots, \tilde{\boldsymbol{v}}_k^{(m+1)} \right] \right)
\end{cases}
\tag{4}
$$


## 3.2 Dynamics of $\mathcal{W}^u(\boldsymbol{x})$ and Direct Discretization

By taking the limit $\beta \rightarrow 0$ in the discrete form
(3) (including the orthogonalization
process), we can obtain the continuous ODE:

$$
\boldsymbol{\dot{v}}_i = \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i + \sum_{j=1}^{i} \xi^{(i)}_j \boldsymbol{v}_j
$$

Noting the orthonormal constraint:

$$
\left\langle \boldsymbol{v}_i, \boldsymbol{v}_j \right\rangle = \delta_{ij} \quad i, j = 1, \ldots, k
$$

Differentiating with respect to $t$ gives:

$$
\left\langle \boldsymbol{\dot{v}}_i, \boldsymbol{v}_j \right\rangle + \left\langle \boldsymbol{v}_i, \boldsymbol{\dot{v}}_j \right\rangle = 0 \quad i, j = 1, \ldots, k
$$

Substituting in, we can obtain:

$$
\xi_{i}^{(i)} = -\langle \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i, \boldsymbol{v}_i \rangle
$$

$$
\xi_{j}^{(i)} = -\langle \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i, \boldsymbol{v}_j \rangle - \langle \boldsymbol{v}_i, \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_j \rangle \quad j = 1, \cdots, i-1
$$

Combining this with equation
(2), we can obtain the dynamics of the
entire problem:

$$
\begin{cases} 
\dot{\boldsymbol{x}} = \left( \mathbb{I} - 2 \displaystyle \sum_{j=1}^{k} \boldsymbol{v}_j \boldsymbol{v}_j^\top \right) \boldsymbol{F}(\boldsymbol{x}),\\
\dot{\boldsymbol{v}}_i = \left( \mathbb{I} - \boldsymbol{v}_i \boldsymbol{v}_i^\top \right) \mathbb{J}(\boldsymbol{x}) \boldsymbol{v}_i - \displaystyle \sum_{j=1}^{i-1} \boldsymbol{v}_j \boldsymbol{v}_j^\top \left( \mathbb{J}(\boldsymbol{x}) + \mathbb{J}^\top(\boldsymbol{x}) \right) \boldsymbol{v}_i, \quad i = 1, \cdots, k
\end{cases}
$$

The proof of the linear stability of this dynamics can be found in Reference [1].

In fact, after obtaining this dynamics, we can directly discretize it to obtain a new numerical algorithm. However, this algorithm has a larger computational load compared to the previous discrete format because, in the actual computation process, the orthogonality of the discretization format still needs to be maintained through Gram-Schmidt orthogonalization. Moreover, in the Reference [2], it is proven that the actual effects of the two discretization formats are not significantly different. Therefore, considering the computational load, we often directly use the simpler discrete format (4).

# 4 Construction of the Solution Landscape

The goal of the HiSD series of algorithms is not only to search for
$k$-saddle but also to provide the search relationships between saddle
points of different indexs, thereby completing the construction of the
solution landscape and making our search more systematic and giving us a
deeper understanding of the relationships between saddle points. Below
we will present the downward search algorithm for searching from
higher-index saddle points to lower-index saddle points and the upward
search algorithm for searching from lower-index saddle points to
higher-index saddle points.

## Downward Search Algorithm

We present an algorithm that starts from a $\hat{k}$-saddle to search
for a $\hat{k}-1$-saddle and further searches for lower-index saddle
points down to the $0$-saddle(sink point), while recording the search
relationships. The core step is to search for an $m$-saddle($m < k$)
from a $k$-saddle(generally, adjacent index saddle points are searched
each time, but this also supports skipping indexs, so we are describing
a more general case here). The basic idea is to perturb the $k$-saddle
along an unstable direction to obtain the initial point for iteration,
and then select $m$ directions from the remaining $k-1$ unstable
directions orthogonal to this direction as the initial unstable subspace
directions for iteration. As a result, the selected perturbation
direction will move along the positive direction of the system force
during iteration, and since it is an unstable direction,
$\boldsymbol{x}$ will escape the current saddle point and evolve towards
the $m$-saddle.

## Upward Search Algorithm

The downward search method allows us to systematically search for
lower-index saddle points from higher-index saddle points. Conversely,
we can also start from lower-index saddle points to search for
higher-index saddle points (and then search downwards from the
higher-index saddle points to find more saddle points). The core step of
this algorithm is to search for an $m$-saddle($m > k$) from a
$k$-saddle. Similar to the idea above, we will perturb the $k$-saddle
along a stable direction to obtain the initial point for iteration, and
then take this direction along with the original $k$ unstable directions
and add $m-k-1$ other stable directions as the initial directions for
iteration. As a result, the selected perturbation direction will move
along the negative direction of the system force during iteration, and
since it is a stable direction, $\boldsymbol{x}$ will escape the current
saddle point and evolve towards the $m$-saddle.

# 5 Summary

We have introduced the GHiSD method for systematically searching for
$k$-saddle in non-gradient systems, which can be regarded as an
extension of the HiSD algorithm to more general problems. The ideas of
$\boldsymbol{x}$ moving along the opposite direction of the force in the
unstable subspace and along the direction of the force in its
complementary space, as well as the use of dimer approximation, all play
a very important role. Finally, we also introduced the way to construct
the solution landscape using the GHiSD algorithm, which gives us a
deeper understanding of the relationships between saddle points with
different indexs and makes our search more systematic and comprehensive.

# 6 References

1. Yin, J., Yu, B., & Zhang, L. (2020). Searching the solution landscape by generalized high-index saddle dynamics. _Science China Mathematics_, ​**64**(8). [https://doi.org/10.1007/s11425-020-1737-1](https://doi.org/10.1007/s11425-020-1737-1)

2. Zhang, L., Zhang, P., & Zheng, X. (2024). Understanding high-index saddle dynamics via numerical analysis. _Communications in Mathematical Sciences_, ​**23**(2). [https://doi.org/10.4310/CMS.241217235844](https://doi.org/10.4310/CMS.241217235844)

