# 2019-05-30
from fnmatch import fnmatch

import pandas as pd
from pyecharts import charts
from pyecharts import options as opts


class BaseAccessor(object):
    def __init__(self, pandas_obj):
        self.df = pandas_obj
        self.chart_xy = {}
        self.chart_basic = {}

    def plot_xy(self, x=None, y=None, kind='line', mdf=None, **kwargs):
        """
        直角坐标系图表
        :param x: 用于指定x轴标签，默认为dataframe的index
        :param y: 用于指定y轴数据，支持str、list、tuple，默认整个为dataframe
        :param kind: 图表类型
        :param mdf: 默认self.df, 可以传自定义的frame
        :param kwargs: 配置选项
        :return:
        """
        if kind not in self.chart_xy:
            raise NotImplementedError

        if mdf is None:
            mdf = self.df

        # 获取配置
        init_opts = kwargs.get('init_opts', {})
        y_opts = kwargs.get('y_opts', {})
        default_global_opts = {'title_opts': {'text': kind.title()}, 'toolbox_opts': opts.ToolboxOpts(is_show=True)}
        global_opts = kwargs.get('global_opts', default_global_opts)

        # 初始化图表
        c = self.chart_xy.get(kind)(opts.InitOpts(**init_opts))

        # x轴标签
        x_data = mdf[x].astype('str').tolist() if x else mdf.index.astype('str').tolist()
        c = c.add_xaxis(x_data)

        # y轴值
        y_data = mdf
        if isinstance(y, (list, tuple)):
            y_data = mdf[y]
        elif isinstance(y, str):
            y_data = mdf[[y]]

        for k, col in y_data.iteritems():
            # 支持通配符的模式匹配配置选项
            _opts = {}
            for opts_key, opts_val in y_opts.items():
                if fnmatch(k, opts_key):
                    _opts.update(opts_val)
            # 添加y轴的值
            c.add_yaxis(k, col.tolist(), **_opts)

        # 默认配置
        c = c.set_global_opts(**global_opts)

        return c

    def plot_basic(self, label=None, value=None, kind='pie', mdf=None, **kwargs):
        # 基本图表
        if kind not in self.chart_basic:
            raise NotImplementedError

        if mdf is None:
            mdf = self.df

        # 获取配置
        init_opts = kwargs.get('init_opts', {})
        val_opts = kwargs.get('val_opts', {})
        default_global_opts = {'title_opts': {'text': kind.title()}, 'toolbox_opts': opts.ToolboxOpts(is_show=True)}
        global_opts = kwargs.get('global_opts', default_global_opts)

        # 初始化图表
        c = self.chart_basic.get(kind)(opts.InitOpts(**init_opts))

        # x default is self.df.index,
        label_data = mdf.index.astype('str').tolist() if label is None else mdf[label].astype('str').tolist()

        # y default is self.df first column
        value_data = mdf.iloc[:, 0].tolist() if value is None else mdf[value].tolist()

        c = c.add('', [list(item) for item in zip(label_data, value_data)], **val_opts)

        # default setting
        c = c.set_global_opts(**global_opts)

        # pie setting
        # c = c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        return c

    def plot_func(self, func, *args, **kwargs):
        timeline = kwargs.pop('timeline') if 'timeline' in kwargs else None

        if timeline:
            timeline_init_opts = kwargs.get('timeline_init_opts', {})
            timeline_schema = kwargs.get('timeline_schema', {})
            tl = charts.Timeline(**timeline_init_opts)
            tl.add_schema(**timeline_schema)

            for k, _frame in self.df.groupby(timeline):
                _frame = _frame.drop(columns=timeline)
                tl.add(func(mdf=_frame, *args, **kwargs), k)
            return tl

        return func(*args, **kwargs)

    def line(self, x=None, y=None, **kwargs):
        # 折线图
        return self.plot_func(self.plot_xy, x=x, y=y, kind='line', **kwargs)

    def bar(self, x=None, y=None, **kwargs):
        # 柱状图
        return self.plot_func(self.plot_xy, x=x, y=y, kind='bar', **kwargs)

    def scatter(self, x=None, y=None, effect=False, **kwargs):
        # 涟漪散点图 & 散点图
        if effect:
            return self.plot_func(self.plot_xy, x=x, y=y, kind='effectScatter', **kwargs)
        else:
            return self.plot_func(self.plot_xy, x=x, y=y, kind='scatter', **kwargs)

    def pie(self, label=None, value=None, **kwargs):
        # 饼图
        return self.plot_func(self.plot_basic, label=label, value=value, kind='pie', **kwargs)

    def wordCloud(self, label=None, value=None, **kwargs):
        # 词云图
        return self.plot_func(self.plot_basic, label=label, value=value, kind='wordCloud', **kwargs)


@pd.api.extensions.register_dataframe_accessor('pdchart')
class PdChartFrameAccessor(BaseAccessor):
    def __init__(self, pandas_obj):
        self.df = pandas_obj

        self.chart_xy = {
            'line': charts.Line,
            'bar': charts.Bar,
            'scatter': charts.Scatter,
            'effectScatter': charts.EffectScatter,
        }

        self.chart_basic = {
            'pie': charts.Pie,
            'wordCloud': charts.WordCloud
        }

        super(BaseAccessor, self).__init__()


@pd.api.extensions.register_series_accessor('pdchart')
class PdChartSeriesAccessor(BaseAccessor):
    def __init__(self, pandas_obj):
        self.df = pandas_obj.to_frame()

        self.chart_xy = {
            'line': charts.Line,
            'bar': charts.Bar,
            'scatter': charts.Scatter,
            'effectScatter': charts.EffectScatter,
        }

        self.chart_basic = {
            'pie': charts.Pie,
            'wordCloud': charts.WordCloud
        }
        super(BaseAccessor, self).__init__()

