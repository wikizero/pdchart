# demo

import pandas as pd
import pdchart

f = pd.DataFrame({
    'pig': [60, 180, 489, 675, 1776],
    'horse': [49, 250, 281, 600, 1900]
}, index=[1990, 1997, 2003, 2009, 2014])

print(f)

f.pdchart.line().render('static/line.html')
f.pdchart.bar().render('static/bar.html')
f.pdchart.scatter(effect=True).render('static/scatter.html')
f.pdchart.pie(y='horse').render('static/pie.html')
