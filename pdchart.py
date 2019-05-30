# 2019-05-30
import pandas as pd
from pyecharts import charts


@pd.api.extensions.register_dataframe_accessor("pdchart")
class PdChartAccessor(object):
    def __init__(self, pandas_obj):
        self.df = pandas_obj

        self.chart_xy = {
            'line': charts.Line,
            'bar': charts.Bar,
            'scatter': charts.Scatter,
            'effectScatter': charts.EffectScatter,
        }

        self.chart_basic = {
            'pie': charts.Pie
        }

    def plot_xy(self, kind='line'):
        if kind not in self.chart_xy:
            raise NotImplementedError

        # init chart
        c = self.chart_xy.get(kind)()

        c = c.add_xaxis(self.df.index.astype('str').tolist())

        for k, col in self.df.iteritems():
            c.add_yaxis(k, col.tolist())

        # default setting
        c = c.set_global_opts(title_opts={"text": kind.title()})

        return c

    def plot_basic(self, x=None, y=None, kind='pie'):
        if kind not in self.chart_basic:
            raise NotImplementedError

        # init chart
        c = self.chart_basic.get(kind)()

        # x default is self.df.index, y default is self.df first column
        x = self.df.index.astype('str').tolist() if x is None else self.df[x].tolist()

        # TODO 如果优雅地获取第一列数据
        y = self.df.T.head(1).values[0].tolist() if y is None else self.df[y].tolist()

        c = c.add('', [list(item) for item in zip(x, y)])

        # default setting
        c = c.set_global_opts(title_opts={"text": kind.title()})

        # pie setting
        # c = c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        return c

    def line(self):
        return self.plot_xy(kind='line')

    def bar(self):
        # TODO 支持拆分 而不是嵌套 参考pandas api
        return self.plot_xy(kind='bar')

    def scatter(self, effect=False):
        # 散点图 & 涟漪散点图
        return self.plot_xy(kind='effectScatter') if effect else self.plot_xy(kind='scatter')

    def pie(self, x=None, y=None):
        return self.plot_basic(x=x, y=y, kind='pie')
