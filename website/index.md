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
# HiSD Package: solscape-1.0

A Python package for constructing solution landscapes using High-index Saddle Dynamics (HiSD). This toolkit enables numerical computation of saddle points and their hierarchical organization in dynamical systems. This package simplifies the process of saddle point searching, offering flexible parameter settings and many visualization tools.

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
   git clone https://github.com/LiuOnly1121/HiSD_Package.git
   cd HiSD
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

Below is a basic workflow for using HiSD:

1. **Initialization**:
   ```python
   import Landscape
   mylandscape = Landscape.Landscape(**kwargs)
   ```

2. **Run the computation**:
   ```python
   mylandscape.run()
   ```

3. **Plot graphs**:
   ```python
   mylandscape.DrawHeatmap(**kwargs)
   mylandscape.DrawConnection(**kwargs)
   ```

4. **Save results**:
   ```python
   mylandscape.Save(**kwargs)
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
- `numpy`
- `scipy`
- `sympy`
- `matplotlib`
- `networkx`

## Examples

Here are some examples to help you get started quickly:

- `Ex_1_Butterfly.ipynb`
- `Ex_2_MullerBrownPotential.ipynb`
- `Ex_3_Cubic.ipynb`
- `Ex_4_PhaseField.ipynb`


