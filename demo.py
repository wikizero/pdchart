# demo

import pandas as pd
import pdchart
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Grid

f = pd.DataFrame({
    'pig': [60, 180, 489, 675, 1776],
    'horse': [49, 250, 281, 600, 1900],
    'type': ['ie', 'firefox', 'safari', 'chrome', 'edge']
}, index=[1990, 1997, 2003, 2009, 2014])

print(f)

# basic
# f.pdchart.line(x='type', y=['pig', 'horse']).render('static/line.html')
# f.pdchart.bar().render('static/bar.html')
# f.pdchart.scatter(effect=True).render('static/scatter.html')
# f.pdchart.pie(label='horse').render('static/pie.html')
# f.pdchart.wordCloud(label='type', value='pig').render('static/wordCloud.html')


# grid
# line = f.pdchart.line(x='type', y=['pig', 'horse'],
#                       init_opts={'theme': ThemeType.LIGHT},
#                       y_opts={'pig': {'is_smooth': True}, 'horse': {'is_step': True}})
# bar = f.set_index('type').pig.pdchart.bar(global_opts={'title_opts': opts.TitleOpts(title="Grid-Line", pos_top="48%"),
#                                                        'legend_opts': opts.LegendOpts(pos_top="48%")})
# grid = (
#     Grid()
#         .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
#         .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
# )
# grid.render('static/grid.html')


f = pd.DataFrame({
    'year': [str(i) + '年' for i in
             [2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004, 2001, 2002, 2003, 2004]],
    'horse': [490, 250, 271, 650, 190, 250, 289, 600, 290, 250, 181, 208, 190, 250, 291, 390],
    'pig': [190, 350, 278, 450, 290, 290, 289, 600, 390, 150, 181, 258, 290, 550, 391, 280],
    'type': ['firefox', 'firefox', 'firefox', 'firefox', 'safari', 'safari', 'safari', 'safari', 'chrome', 'chrome',
             'chrome', 'chrome', 'edge', 'edge', 'edge', 'edge']
})

# print(f)
# f.pdchart.bar(x='type', y=['horse', 'pig'], timeline='year').render('static/pie.html')

# f.pdchart.pie(label='type', value='horse', timeline='year',
#               val_opts={'rosetype': 'radius', 'radius': ["30%", "55%"]}).render('static/pie.html')

import matplotlib

# df = pd.DataFrame({
#     'sum': [100, 380, 289, 460, 150],
#     'size': [123, 180, 250, 90, 150],
#     'year': [1990, 1994, 1998, 2000, 2004],
#     'type': ['ie', 'firefox', 'safari', 'chrome', 'edge']
# })
# df.pdchart.line(x='year', y=['sum', 'size'],
#                 init_opts={'theme': ThemeType.LIGHT},
#                 y_opts={'sum':{'is_smooth':True}, 'size':{'is_step':True}}).render('static/line.html')

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
print(new_df)