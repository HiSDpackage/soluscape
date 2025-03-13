---
layout: single
permalink: /index_Chinese
title: "HiSD: 基于Python的高阶鞍点计算算法包"
excerpt: "A quick start guide."
sidebar:
    nav: docs_Chinese
toc: true
toc_sticky: true
mathjax: true

---
# HiSD 软件包 1.0 版本

HiSD 是一款专为高效寻找系统中鞍点而设计的算法工具。本软件包简化了鞍点搜索流程，提供灵活的参数设置和可视化功能。

## 功能特性

- ​**多算法实现**:
  - `HiOSD`: 梯度系统的高指数优化收缩二聚体法
  - `GHiSD`: 非梯度系统的广义高指数鞍点动力学方法
- ​**多加速算法实现**:
  - `HiSD`: 基础鞍点搜索算法
  - `NHiSD`: 带Nesterov加速的HiSD
  - `HHiSD`: 带Heavy Ball加速的HiSD
- ​**灵活特性**:
  - 支持多种输入形式（梯度函数或能量函数，表达式字符串或函数句柄）
  - 自动校验参数合法性
  - 模块化类设计便于扩展
  - 便捷绘制搜索轨迹、热力图和鞍点连接图
  - 可保存重要计算结果
  - 支持处理函数系统
  - 可根据指定标准自动合并相同鞍点

## 安装指南

1. 克隆仓库：
   ```bash
   git clone https://github.com/LiuOnly1121/HiSD_Package.git
   cd HiSD
   ```

2. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

## 快速入门

以下是使用HiSD的基本工作流:

1. **初始化**:
   ```python
   import Landscape
   mylandscape = Landscape.Landscape(**kwargs)
   ```

2. **执行计算**:
   ```python
   mylandscape.run()
   ```

3. **可视化绘图**:
   ```python
   mylandscape.DrawHeatmap(**kwargs)
   mylandscape.DrawConnection(**kwargs)
   ```

4. **保存结果**:
   ```python
   mylandscape.Save(**kwargs)
   ```

更多详细用法请参阅说明文档（见“教程”网页）。

## 依赖项

HiSD 依赖以下Python库：

内置包：
- `copy`
- `sys`
- `warnings`
- `inspect`
- `json`
- `itertools`
- `math`
- `pickle`

第三方包：
- `numpy`
- `scipy`
- `sympy`
- `matplotlib`
- `networkx`

## 示例

以下示例可帮助快速上手（见[“示例”网页](https://hisdpackage.github.io/attempt/Background/Background_Chinese)）:

- `Ex_1_Butterfly.ipynb`
- `Ex_2_MullerBrownPotential.ipynb`
- `Ex_3_Cubic.ipynb`
- `Ex_4_PhaseField.ipynb`

