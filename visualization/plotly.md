
# Plotly

Plotly是一个用于数据可视化的Python第三方库。它提供了一种交互式、高度可定制的方式来创建各种类型的图表和可视化。Plotly支持各种图表类型，包括线图、散点图、条形图、饼图、3D图等。

Plotly具有许多功能强大的特性，例如：

1. 交互式图表：Plotly生成的图表可以在Web浏览器中进行交互操作，包括缩放、平移、悬停提示等。这使得用户可以更好地探索和理解数据。

2. 可定制性：Plotly提供了广泛的参数和选项，允许用户自定义图表的外观和行为。用户可以调整颜色、线条样式、标签、轴设置等，以满足自己的需求。

3. 支持多种输出格式：Plotly可以将图表导出为静态图像或动态图形，包括PNG、JPEG、SVG、PDF和HTML等格式。

4. 多平台支持：Plotly可以在多个平台上使用，包括本地环境、Jupyter Notebook、Web应用程序等。

5. 可与其他库集成：Plotly可以与其他常用的Python库（如Pandas和NumPy）以及其他数据科学工具（如Jupyter Notebook和Dash）进行集成，以便更好地进行数据分析和可视化。

# 使用简介

## 1. 绘制折线图

``` python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from plotly import offline as py
import plotly.offline as py                    #保存图表，相当于plotly.plotly as py，同时增加了离线功能
# py.init_notebook_mode(connected=True)          #离线绘图时，需要额外进行初始化
import plotly.graph_objs as go                 #创建各类图表
import plotly.figure_factory as ff             #创建table

trace0 = go.Scatter(
      x = np.linspace(0, 1, 100),
      y = np.random.randn(100) + 5,
      mode = 'lines',
      name = 'line'   
)
trace1 = go.Scatter(
      x = np.linspace(0, 1, 100),
      y = np.random.randn(100),
      mode = 'lines + markers',
      name = 'line + marker'   
)
trace2 = go.Scatter(
      x = np.linspace(0, 1, 100),
      y = np.random.randn(100) - 5,
      mode = 'markers',
      name = 'marker'   
)
data = [trace0, trace1, trace2]

# py.iplot(data)
py.plot(data)
```

## 参考

[Plotly 绘制折线图 1](https://blog.csdn.net/paperplaneY/article/details/114317458)  
[Plotly 绘制折线图 2](https://www.jianshu.com/p/ea32777736b7)
