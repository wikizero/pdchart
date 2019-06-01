
#### pdchart 简介
pdchart可以快速将你的dataframe、series数据进行可视化，并且图表比pandas原生支持的图表更精美、灵活、强大.

pdchart是属于pandas的一款扩展工具，基于pandas、pyecharts基础上开发，要更好的使用pdchart您首先要对这两款工具有一定了解，pdchart的参数配置基本是基于pyecharts封装.

[pandas 官网](http://pandas.pydata.org/)

[pyecharts 官网](https://pyecharts.org/#/zh-cn/intro)

下面简单介绍下我们应该如何使用pdchart.

PS: 下面的例子都是在jupyter book上展示.


```python
# 引入pdchart、并初始化测试数据集
import pandas as pd
import pdchart
%matplotlib inline

df = pd.DataFrame({
    'sum': [100, 380, 289, 460, 150],
    'size': [123, 180, 250, 90, 150],
    'year': [1990, 1994, 1998, 2000, 2004],
    'type': ['ie', 'firefox', 'safari', 'chrome', 'edge']
})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sum</th>
      <th>size</th>
      <th>year</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>100</td>
      <td>123</td>
      <td>1990</td>
      <td>ie</td>
    </tr>
    <tr>
      <th>1</th>
      <td>380</td>
      <td>180</td>
      <td>1994</td>
      <td>firefox</td>
    </tr>
    <tr>
      <th>2</th>
      <td>289</td>
      <td>250</td>
      <td>1998</td>
      <td>safari</td>
    </tr>
    <tr>
      <th>3</th>
      <td>460</td>
      <td>90</td>
      <td>2000</td>
      <td>chrome</td>
    </tr>
    <tr>
      <th>4</th>
      <td>150</td>
      <td>150</td>
      <td>2004</td>
      <td>edge</td>
    </tr>
  </tbody>
</table>
</div>



#### 折线图 - Line


```python
# 查看sum
df['sum'].pdchart.line().render_notebook()

# 这是series直接支持plot
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="fdf7cb0e46de4596ae47ccd537136f34" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_fdf7cb0e46de4596ae47ccd537136f34 = echarts.init(
            document.getElementById('fdf7cb0e46de4596ae47ccd537136f34'), 'white', {renderer: 'canvas'});
        var option_fdf7cb0e46de4596ae47ccd537136f34 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "line",
            "name": "sum",
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data": [
                [
                    "0",
                    100
                ],
                [
                    "1",
                    380
                ],
                [
                    "2",
                    289
                ],
                [
                    "3",
                    460
                ],
                [
                    "4",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            },
            "lineStyle": {
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum"
            ],
            "selected": {
                "sum": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "0",
                "1",
                "2",
                "3",
                "4"
            ]
        }
    ],
    "title": {
        "text": "Line"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_fdf7cb0e46de4596ae47ccd537136f34.setOption(option_fdf7cb0e46de4596ae47ccd537136f34);
    });
</script>





```python
# 您还可以这样，指定x、y轴
df.pdchart.line(x='type', y=['sum', 'size']).render_notebook()

# 这是dataframe支持plot
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="af3b89fce73142af8bcb6d126ad2bf05" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_af3b89fce73142af8bcb6d126ad2bf05 = echarts.init(
            document.getElementById('af3b89fce73142af8bcb6d126ad2bf05'), 'white', {renderer: 'canvas'});
        var option_af3b89fce73142af8bcb6d126ad2bf05 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "line",
            "name": "sum",
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data": [
                [
                    "ie",
                    100
                ],
                [
                    "firefox",
                    380
                ],
                [
                    "safari",
                    289
                ],
                [
                    "chrome",
                    460
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            },
            "lineStyle": {
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        },
        {
            "type": "line",
            "name": "size",
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data": [
                [
                    "ie",
                    123
                ],
                [
                    "firefox",
                    180
                ],
                [
                    "safari",
                    250
                ],
                [
                    "chrome",
                    90
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            },
            "lineStyle": {
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum",
                "size"
            ],
            "selected": {
                "sum": true,
                "size": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "ie",
                "firefox",
                "safari",
                "chrome",
                "edge"
            ]
        }
    ],
    "title": {
        "text": "Line"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_af3b89fce73142af8bcb6d126ad2bf05.setOption(option_af3b89fce73142af8bcb6d126ad2bf05);
    });
</script>





```python
# 支持pyecharts中的图表配置
from pyecharts.globals import ThemeType # 引入主题

df.pdchart.line(x='type', y=['sum', 'size'], 
                init_opts={'theme': ThemeType.LIGHT},
                y_opts={'sum':{'is_smooth':True}, 'size':{'is_step':True}}).render_notebook()

# 更多的配置参数以请参考pyecharts文档
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="a70da813e9584e0b94e2e7a2a226076e" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_a70da813e9584e0b94e2e7a2a226076e = echarts.init(
            document.getElementById('a70da813e9584e0b94e2e7a2a226076e'), 'light', {renderer: 'canvas'});
        var option_a70da813e9584e0b94e2e7a2a226076e = {
    "series": [
        {
            "type": "line",
            "name": "sum",
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": true,
            "step": false,
            "data": [
                [
                    "ie",
                    100
                ],
                [
                    "firefox",
                    380
                ],
                [
                    "safari",
                    289
                ],
                [
                    "chrome",
                    460
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            },
            "lineStyle": {
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        },
        {
            "type": "line",
            "name": "size",
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": true,
            "data": [
                [
                    "ie",
                    123
                ],
                [
                    "firefox",
                    180
                ],
                [
                    "safari",
                    250
                ],
                [
                    "chrome",
                    90
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            },
            "lineStyle": {
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum",
                "size"
            ],
            "selected": {
                "sum": true,
                "size": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "ie",
                "firefox",
                "safari",
                "chrome",
                "edge"
            ]
        }
    ],
    "title": {
        "text": "Line"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_a70da813e9584e0b94e2e7a2a226076e.setOption(option_a70da813e9584e0b94e2e7a2a226076e);
    });
</script>




#### 柱状图 - Bar


```python
df.pdchart.bar(x='year', y=['sum', 'size']).render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="c337b36f2d244c8bb3ee6e347c1faf4f" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_c337b36f2d244c8bb3ee6e347c1faf4f = echarts.init(
            document.getElementById('c337b36f2d244c8bb3ee6e347c1faf4f'), 'white', {renderer: 'canvas'});
        var option_c337b36f2d244c8bb3ee6e347c1faf4f = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "sum",
            "data": [
                100,
                380,
                289,
                460,
                150
            ],
            "barCategoryGap": "20%",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            }
        },
        {
            "type": "bar",
            "name": "size",
            "data": [
                123,
                180,
                250,
                90,
                150
            ],
            "barCategoryGap": "20%",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum",
                "size"
            ],
            "selected": {
                "sum": true,
                "size": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                1990,
                1994,
                1998,
                2000,
                2004
            ]
        }
    ],
    "title": {
        "text": "Bar"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_c337b36f2d244c8bb3ee6e347c1faf4f.setOption(option_c337b36f2d244c8bb3ee6e347c1faf4f);
    });
</script>




#### 散点图 - Scatter


```python
df.pdchart.scatter(x='type', y=['sum', 'size']).render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="5c17caf7215a48e2b220e9f6c94e78f0" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_5c17caf7215a48e2b220e9f6c94e78f0 = echarts.init(
            document.getElementById('5c17caf7215a48e2b220e9f6c94e78f0'), 'white', {renderer: 'canvas'});
        var option_5c17caf7215a48e2b220e9f6c94e78f0 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "scatter",
            "name": "sum",
            "symbolSize": 10,
            "data": [
                [
                    "ie",
                    100
                ],
                [
                    "firefox",
                    380
                ],
                [
                    "safari",
                    289
                ],
                [
                    "chrome",
                    460
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "right",
                "margin": 8,
                "fontSize": 12
            }
        },
        {
            "type": "scatter",
            "name": "size",
            "symbolSize": 10,
            "data": [
                [
                    "ie",
                    123
                ],
                [
                    "firefox",
                    180
                ],
                [
                    "safari",
                    250
                ],
                [
                    "chrome",
                    90
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "right",
                "margin": 8,
                "fontSize": 12
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum",
                "size"
            ],
            "selected": {
                "sum": true,
                "size": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "ie",
                "firefox",
                "safari",
                "chrome",
                "edge"
            ]
        }
    ],
    "title": {
        "text": "Scatter"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_5c17caf7215a48e2b220e9f6c94e78f0.setOption(option_5c17caf7215a48e2b220e9f6c94e78f0);
    });
</script>




#### 涟漪散点图 - effectScatter


```python
df.pdchart.scatter(x='type', y=['sum', 'size'], effect=True).render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="55d902c189724be099e0f075da76db42" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_55d902c189724be099e0f075da76db42 = echarts.init(
            document.getElementById('55d902c189724be099e0f075da76db42'), 'white', {renderer: 'canvas'});
        var option_55d902c189724be099e0f075da76db42 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "effectScatter",
            "name": "sum",
            "showEffectOn": "render",
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "symbolSize": 10,
            "data": [
                [
                    "ie",
                    100
                ],
                [
                    "firefox",
                    380
                ],
                [
                    "safari",
                    289
                ],
                [
                    "chrome",
                    460
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            }
        },
        {
            "type": "effectScatter",
            "name": "size",
            "showEffectOn": "render",
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            },
            "symbolSize": 10,
            "data": [
                [
                    "ie",
                    123
                ],
                [
                    "firefox",
                    180
                ],
                [
                    "safari",
                    250
                ],
                [
                    "chrome",
                    90
                ],
                [
                    "edge",
                    150
                ]
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            }
        }
    ],
    "legend": [
        {
            "data": [
                "sum",
                "size"
            ],
            "selected": {
                "sum": true,
                "size": true
            },
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "ie",
                "firefox",
                "safari",
                "chrome",
                "edge"
            ]
        }
    ],
    "title": {
        "text": "Effectscatter"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_55d902c189724be099e0f075da76db42.setOption(option_55d902c189724be099e0f075da76db42);
    });
</script>




#### 饼图 - Pie


```python
df.set_index('type')['sum'].pdchart.pie().render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="8955e7425e584d20a6b7b45ee330e472" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_8955e7425e584d20a6b7b45ee330e472 = echarts.init(
            document.getElementById('8955e7425e584d20a6b7b45ee330e472'), 'white', {renderer: 'canvas'});
        var option_8955e7425e584d20a6b7b45ee330e472 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "pie",
            "clockwise": true,
            "data": [
                {
                    "name": "ie",
                    "value": 100
                },
                {
                    "name": "firefox",
                    "value": 380
                },
                {
                    "name": "safari",
                    "value": 289
                },
                {
                    "name": "chrome",
                    "value": 460
                },
                {
                    "name": "edge",
                    "value": 150
                }
            ],
            "radius": [
                "0%",
                "75%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "fontSize": 12
            }
        }
    ],
    "legend": [
        {
            "data": [
                "ie",
                "firefox",
                "safari",
                "chrome",
                "edge"
            ],
            "selected": {},
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "title": {
        "text": "Pie"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_8955e7425e584d20a6b7b45ee330e472.setOption(option_8955e7425e584d20a6b7b45ee330e472);
    });
</script>




#### 词云图 - wordCloud


```python
# 上面的测试数据太少，初始化新数据
words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
]

new_df = pd.DataFrame(words, columns=['name', 'num'])
new_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam S Club</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Macys</td>
      <td>6181</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Amy Schumer</td>
      <td>4386</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jurassic World</td>
      <td>4055</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Charter Communications</td>
      <td>2467</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df.pdchart.wordCloud(label='name', value='num').render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min', 'echarts-wordcloud':'https://assets.pyecharts.org/assets/echarts-wordcloud.min'
        }
    });
</script>

    <div id="0cfcb3ee33454c8c96eea416c62c89a4" style="width:900px; height:500px;"></div>


<script>
    require(['echarts', 'echarts-wordcloud'], function(echarts) {
        var chart_0cfcb3ee33454c8c96eea416c62c89a4 = echarts.init(
            document.getElementById('0cfcb3ee33454c8c96eea416c62c89a4'), 'white', {renderer: 'canvas'});
        var option_0cfcb3ee33454c8c96eea416c62c89a4 = {
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "wordCloud",
            "shape": "circle",
            "rotationRange": [
                -90,
                90
            ],
            "rotationStep": 45,
            "girdSize": 20,
            "sizeRange": [
                12,
                60
            ],
            "data": [
                {
                    "name": "Sam S Club",
                    "value": 10000,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(36,148,118)"
                        }
                    }
                },
                {
                    "name": "Macys",
                    "value": 6181,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,73,128)"
                        }
                    }
                },
                {
                    "name": "Amy Schumer",
                    "value": 4386,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(124,119,57)"
                        }
                    }
                },
                {
                    "name": "Jurassic World",
                    "value": 4055,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(158,97,65)"
                        }
                    }
                },
                {
                    "name": "Charter Communications",
                    "value": 2467,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(71,23,154)"
                        }
                    }
                },
                {
                    "name": "Chick Fil A",
                    "value": 2244,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(123,110,96)"
                        }
                    }
                },
                {
                    "name": "Planet Fitness",
                    "value": 1868,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(136,41,64)"
                        }
                    }
                },
                {
                    "name": "Pitch Perfect",
                    "value": 1484,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,58,140)"
                        }
                    }
                },
                {
                    "name": "Express",
                    "value": 1112,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(16,65,136)"
                        }
                    }
                },
                {
                    "name": "Home",
                    "value": 865,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(122,88,84)"
                        }
                    }
                },
                {
                    "name": "Johnny Depp",
                    "value": 847,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(76,136,20)"
                        }
                    }
                },
                {
                    "name": "Lena Dunham",
                    "value": 582,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(104,67,109)"
                        }
                    }
                },
                {
                    "name": "Lewis Hamilton",
                    "value": 555,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(12,63,35)"
                        }
                    }
                },
                {
                    "name": "KXAN",
                    "value": 550,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(44,103,147)"
                        }
                    }
                },
                {
                    "name": "Mary Ellen Mark",
                    "value": 462,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(15,25,118)"
                        }
                    }
                },
                {
                    "name": "Farrah Abraham",
                    "value": 366,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(97,99,7)"
                        }
                    }
                },
                {
                    "name": "Rita Ora",
                    "value": 360,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,52,13)"
                        }
                    }
                },
                {
                    "name": "Serena Williams",
                    "value": 282,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(1,52,56)"
                        }
                    }
                },
                {
                    "name": "NCAA baseball tournament",
                    "value": 273,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(106,157,40)"
                        }
                    }
                },
                {
                    "name": "Point Break",
                    "value": 265,
                    "textStyle": {
                        "normal": {
                            "color": "rgb(144,69,34)"
                        }
                    }
                }
            ]
        }
    ],
    "legend": [
        {
            "data": [],
            "selected": {},
            "show": true
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "title": {
        "text": "Wordcloud"
    },
    "toolbox": {
        "show": true,
        "orient": "horizontal",
        "itemSize": 15,
        "itemGap": 10,
        "left": "80%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
};
        chart_0cfcb3ee33454c8c96eea416c62c89a4.setOption(option_0cfcb3ee33454c8c96eea416c62c89a4);
    });
</script>




#### 时序图 - timeline


```python
# 加载新的测试数据集
mdf = pd.DataFrame({
    'year': [str(i) + '年' for i in
             [2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004]],
    'size': [490, 250, 271, 650, 190, 250, 289, 600, 290, 250, 181, 208, 190, 250, 291, 390],
    'sum': [190, 350, 278, 450, 290, 290, 289, 600, 390, 150, 181, 258, 290, 550, 391, 280],
    'type': ['firefox', 'firefox', 'firefox', 'firefox', 'safari', 'safari', 'safari', 'safari', 'chrome', 'chrome',
             'chrome', 'chrome', 'edge', 'edge', 'edge', 'edge']
})

mdf.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>size</th>
      <th>sum</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001年</td>
      <td>490</td>
      <td>190</td>
      <td>firefox</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002年</td>
      <td>250</td>
      <td>350</td>
      <td>firefox</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003年</td>
      <td>271</td>
      <td>278</td>
      <td>firefox</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004年</td>
      <td>650</td>
      <td>450</td>
      <td>firefox</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2001年</td>
      <td>190</td>
      <td>290</td>
      <td>safari</td>
    </tr>
  </tbody>
</table>
</div>




```python
mdf.pdchart.bar(x='type', y=['size', 'sum'], timeline='year').render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="af05f6e5a94743b79d214ccd7748c9ed" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_af05f6e5a94743b79d214ccd7748c9ed = echarts.init(
            document.getElementById('af05f6e5a94743b79d214ccd7748c9ed'), 'white', {renderer: 'canvas'});
        var option_af05f6e5a94743b79d214ccd7748c9ed = {
    "baseOption": {
        "series": [
            {
                "type": "bar",
                "name": "size",
                "data": [
                    650,
                    600,
                    208,
                    390
                ],
                "barCategoryGap": "20%",
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8,
                    "fontSize": 12
                }
            },
            {
                "type": "bar",
                "name": "sum",
                "data": [
                    450,
                    600,
                    258,
                    280
                ],
                "barCategoryGap": "20%",
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8,
                    "fontSize": 12
                }
            }
        ],
        "timeline": {
            "axisType": "category",
            "orient": "horizontal",
            "autoPlay": false,
            "loop": true,
            "rewind": false,
            "show": true,
            "inverse": false,
            "bottom": "-5px",
            "data": [
                "2001\u5e74",
                "2002\u5e74",
                "2003\u5e74",
                "2004\u5e74"
            ]
        },
        "xAxis": [
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "minInterval": 0,
                "splitLine": {
                    "show": false,
                    "lineStyle": {
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                },
                "data": [
                    "firefox",
                    "safari",
                    "chrome",
                    "edge"
                ]
            }
        ],
        "yAxis": [
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "minInterval": 0,
                "splitLine": {
                    "show": false,
                    "lineStyle": {
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                }
            }
        ]
    },
    "options": [
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        490,
                        190,
                        290,
                        190
                    ]
                },
                {
                    "data": [
                        190,
                        290,
                        390,
                        290
                    ]
                }
            ],
            "title": {
                "text": "Bar"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        250,
                        250,
                        250,
                        250
                    ]
                },
                {
                    "data": [
                        350,
                        290,
                        150,
                        550
                    ]
                }
            ],
            "title": {
                "text": "Bar"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        271,
                        289,
                        181,
                        291
                    ]
                },
                {
                    "data": [
                        278,
                        289,
                        181,
                        391
                    ]
                }
            ],
            "title": {
                "text": "Bar"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        650,
                        600,
                        208,
                        390
                    ]
                },
                {
                    "data": [
                        450,
                        600,
                        258,
                        280
                    ]
                }
            ],
            "title": {
                "text": "Bar"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        }
    ]
};
        chart_af05f6e5a94743b79d214ccd7748c9ed.setOption(option_af05f6e5a94743b79d214ccd7748c9ed);
    });
</script>





```python
mdf.pdchart.line(x='type', y=['size', 'sum'], timeline='year').render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="cdc42957c5784f4eb15869292bca4af4" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_cdc42957c5784f4eb15869292bca4af4 = echarts.init(
            document.getElementById('cdc42957c5784f4eb15869292bca4af4'), 'white', {renderer: 'canvas'});
        var option_cdc42957c5784f4eb15869292bca4af4 = {
    "baseOption": {
        "series": [
            {
                "type": "line",
                "name": "size",
                "symbolSize": 4,
                "showSymbol": true,
                "smooth": false,
                "step": false,
                "data": [
                    [
                        "firefox",
                        650
                    ],
                    [
                        "safari",
                        600
                    ],
                    [
                        "chrome",
                        208
                    ],
                    [
                        "edge",
                        390
                    ]
                ],
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8,
                    "fontSize": 12
                },
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                },
                "areaStyle": {
                    "opacity": 0
                }
            },
            {
                "type": "line",
                "name": "sum",
                "symbolSize": 4,
                "showSymbol": true,
                "smooth": false,
                "step": false,
                "data": [
                    [
                        "firefox",
                        450
                    ],
                    [
                        "safari",
                        600
                    ],
                    [
                        "chrome",
                        258
                    ],
                    [
                        "edge",
                        280
                    ]
                ],
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8,
                    "fontSize": 12
                },
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                },
                "areaStyle": {
                    "opacity": 0
                }
            }
        ],
        "timeline": {
            "axisType": "category",
            "orient": "horizontal",
            "autoPlay": false,
            "loop": true,
            "rewind": false,
            "show": true,
            "inverse": false,
            "bottom": "-5px",
            "data": [
                "2001\u5e74",
                "2002\u5e74",
                "2003\u5e74",
                "2004\u5e74"
            ]
        },
        "xAxis": [
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "minInterval": 0,
                "splitLine": {
                    "show": false,
                    "lineStyle": {
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                },
                "data": [
                    "firefox",
                    "safari",
                    "chrome",
                    "edge"
                ]
            }
        ],
        "yAxis": [
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "minInterval": 0,
                "splitLine": {
                    "show": false,
                    "lineStyle": {
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                }
            }
        ]
    },
    "options": [
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        [
                            "firefox",
                            490
                        ],
                        [
                            "safari",
                            190
                        ],
                        [
                            "chrome",
                            290
                        ],
                        [
                            "edge",
                            190
                        ]
                    ]
                },
                {
                    "data": [
                        [
                            "firefox",
                            190
                        ],
                        [
                            "safari",
                            290
                        ],
                        [
                            "chrome",
                            390
                        ],
                        [
                            "edge",
                            290
                        ]
                    ]
                }
            ],
            "title": {
                "text": "Line"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        [
                            "firefox",
                            250
                        ],
                        [
                            "safari",
                            250
                        ],
                        [
                            "chrome",
                            250
                        ],
                        [
                            "edge",
                            250
                        ]
                    ]
                },
                {
                    "data": [
                        [
                            "firefox",
                            350
                        ],
                        [
                            "safari",
                            290
                        ],
                        [
                            "chrome",
                            150
                        ],
                        [
                            "edge",
                            550
                        ]
                    ]
                }
            ],
            "title": {
                "text": "Line"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        [
                            "firefox",
                            271
                        ],
                        [
                            "safari",
                            289
                        ],
                        [
                            "chrome",
                            181
                        ],
                        [
                            "edge",
                            291
                        ]
                    ]
                },
                {
                    "data": [
                        [
                            "firefox",
                            278
                        ],
                        [
                            "safari",
                            289
                        ],
                        [
                            "chrome",
                            181
                        ],
                        [
                            "edge",
                            391
                        ]
                    ]
                }
            ],
            "title": {
                "text": "Line"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "size",
                        "sum"
                    ],
                    "selected": {
                        "size": true,
                        "sum": true
                    },
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        [
                            "firefox",
                            650
                        ],
                        [
                            "safari",
                            600
                        ],
                        [
                            "chrome",
                            208
                        ],
                        [
                            "edge",
                            390
                        ]
                    ]
                },
                {
                    "data": [
                        [
                            "firefox",
                            450
                        ],
                        [
                            "safari",
                            600
                        ],
                        [
                            "chrome",
                            258
                        ],
                        [
                            "edge",
                            280
                        ]
                    ]
                }
            ],
            "title": {
                "text": "Line"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        }
    ]
};
        chart_cdc42957c5784f4eb15869292bca4af4.setOption(option_cdc42957c5784f4eb15869292bca4af4);
    });
</script>





```python
mdf.pdchart.pie(label='type', value='size', timeline='year', 
                 val_opts={'rosetype': 'radius', 'radius': ["30%", "55%"]}).render_notebook()
```




<script>
    require.config({
        paths: {
            'echarts':'https://assets.pyecharts.org/assets/echarts.min'
        }
    });
</script>

    <div id="9dfca9f6e94c4846beb65e43ab925266" style="width:900px; height:500px;"></div>


<script>
    require(['echarts'], function(echarts) {
        var chart_9dfca9f6e94c4846beb65e43ab925266 = echarts.init(
            document.getElementById('9dfca9f6e94c4846beb65e43ab925266'), 'white', {renderer: 'canvas'});
        var option_9dfca9f6e94c4846beb65e43ab925266 = {
    "baseOption": {
        "series": [
            {
                "type": "pie",
                "clockwise": true,
                "data": [
                    {
                        "name": "firefox",
                        "value": 650
                    },
                    {
                        "name": "safari",
                        "value": 600
                    },
                    {
                        "name": "chrome",
                        "value": 208
                    },
                    {
                        "name": "edge",
                        "value": 390
                    }
                ],
                "radius": [
                    "30%",
                    "55%"
                ],
                "center": [
                    "50%",
                    "50%"
                ],
                "roseType": "radius",
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8,
                    "fontSize": 12
                }
            }
        ],
        "timeline": {
            "axisType": "category",
            "orient": "horizontal",
            "autoPlay": false,
            "loop": true,
            "rewind": false,
            "show": true,
            "inverse": false,
            "bottom": "-5px",
            "data": [
                "2001\u5e74",
                "2002\u5e74",
                "2003\u5e74",
                "2004\u5e74"
            ]
        }
    },
    "options": [
        {
            "legend": [
                {
                    "data": [
                        "firefox",
                        "safari",
                        "chrome",
                        "edge"
                    ],
                    "selected": {},
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        {
                            "name": "firefox",
                            "value": 490
                        },
                        {
                            "name": "safari",
                            "value": 190
                        },
                        {
                            "name": "chrome",
                            "value": 290
                        },
                        {
                            "name": "edge",
                            "value": 190
                        }
                    ]
                }
            ],
            "title": {
                "text": "Pie"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "firefox",
                        "safari",
                        "chrome",
                        "edge"
                    ],
                    "selected": {},
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        {
                            "name": "firefox",
                            "value": 250
                        },
                        {
                            "name": "safari",
                            "value": 250
                        },
                        {
                            "name": "chrome",
                            "value": 250
                        },
                        {
                            "name": "edge",
                            "value": 250
                        }
                    ]
                }
            ],
            "title": {
                "text": "Pie"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "firefox",
                        "safari",
                        "chrome",
                        "edge"
                    ],
                    "selected": {},
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        {
                            "name": "firefox",
                            "value": 271
                        },
                        {
                            "name": "safari",
                            "value": 289
                        },
                        {
                            "name": "chrome",
                            "value": 181
                        },
                        {
                            "name": "edge",
                            "value": 291
                        }
                    ]
                }
            ],
            "title": {
                "text": "Pie"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        },
        {
            "legend": [
                {
                    "data": [
                        "firefox",
                        "safari",
                        "chrome",
                        "edge"
                    ],
                    "selected": {},
                    "show": true
                }
            ],
            "series": [
                {
                    "data": [
                        {
                            "name": "firefox",
                            "value": 650
                        },
                        {
                            "name": "safari",
                            "value": 600
                        },
                        {
                            "name": "chrome",
                            "value": 208
                        },
                        {
                            "name": "edge",
                            "value": 390
                        }
                    ]
                }
            ],
            "title": {
                "text": "Pie"
            },
            "tooltip": {
                "show": true,
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "borderWidth": 0
            }
        }
    ]
};
        chart_9dfca9f6e94c4846beb65e43ab925266.setOption(option_9dfca9f6e94c4846beb65e43ab925266);
    });
</script>




#### 3D 图表 

开发中......


更多的图表后续会陆续支持起来，谢谢支持！
