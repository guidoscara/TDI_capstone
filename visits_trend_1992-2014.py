import json

## numpy and pandas to deal with data
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

## bokeh for plot
from bokeh.plotting import figure, show, output_file
from bokeh.charts import Bar, output_file, show
from bokeh.embed import file_html
from bokeh.models.tickers import SingleIntervalTicker

## download 1992 to 2014 library data. No API from 2011 or earlier
library_administrative_1992 = pd.read_csv('Libraries_csv/PUPLDF92.csv')  ## ATTEND POPU_UNDUP
library_administrative_1993 = pd.read_csv('Libraries_csv/PUPLDF93.csv')  ## ATTEND POPU_UNDUP
library_administrative_1994 = pd.read_csv('Libraries_csv/PUPLDF94.csv')  ## ATTEND POPU_UNDUP
library_administrative_1995 = pd.read_csv('Libraries_csv/PUPLDF95.csv')  ## ATTEND POPU_UNDUP
library_administrative_1996 = pd.read_csv('Libraries_csv/PUPLDF96.csv')  ## ATTEND POPU_UNDUP
library_administrative_1997 = pd.read_csv('Libraries_csv/PUPLDF97.csv')  ## ATTEND POPU_UNDUP
library_administrative_1998 = pd.read_csv('Libraries_csv/PUPLDF98.csv')  ## Visits POPU_UND
library_administrative_1999 = pd.read_csv('Libraries_csv/PUPLDF99.csv')  ## Visits POPU_UND

library_administrative_2000 = pd.read_csv('Libraries_csv/pupldf00.csv')  ## Visits POPU_UND
library_administrative_2001 = pd.read_csv('Libraries_csv/pupld01b.csv')  ## Visits POPU_UND
library_administrative_2002 = pd.read_csv('Libraries_csv/pupld02b.csv')  ## Visits POPU_UND
library_administrative_2003 = pd.read_csv('Libraries_csv/pupld03a.csv')  ## Visits POPU_UND
library_administrative_2004 = pd.read_csv('Libraries_csv/pupld04a.csv')  ## Visits POPU_UND
library_administrative_2005 = pd.read_csv('Libraries_csv/pupld05a.csv')  ## Visits POPU_UND
library_administrative_2006 = pd.read_csv('Libraries_csv/pupld06a.csv')  ## Visits POPU_UND
library_administrative_2007 = pd.read_csv('Libraries_csv/pupld07.csv')   ## Visits POPU_UND
library_administrative_2008 = pd.read_csv('Libraries_csv/pupld08a.csv')  ## Visits POPU_UND
library_administrative_2009 = pd.read_csv('Libraries_csv/pupld09a.csv')  ## Visits POPU_UND

library_administrative_2010 = pd.read_csv('Libraries_csv/pupld10a.csv')  ## Visits POPU_UND
library_administrative_2011 = pd.read_csv('Libraries_csv/pupld11b.csv')  ## Visits POPU_UND

library_administrative_2012 = pd.read_json("https://data.imls.gov/resource/emrn-9353.json?$limit=100000")
library_administrative_2013 = pd.read_json("https://data.imls.gov/resource/izgv-y38u.json?$limit=100000")
library_administrative_2014 = pd.read_json("https://data.imls.gov/resource/76da-i3z6.json?$limit=100000")



## pruning missing records and creating an object with mean visits_vs_population per year
tmp = library_administrative_1992[library_administrative_1992.ATTEND>0]
library_administrative_1992_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014 = round((library_administrative_1992_pruned.ATTEND / library_administrative_1992_pruned.POPU_UNDUP).mean(),2)

tmp = library_administrative_1993[library_administrative_1993.ATTEND>0]
library_administrative_1993_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014 = [visits_vs_users_1992_2014] + [round((library_administrative_1993_pruned.ATTEND / library_administrative_1993_pruned.POPU_UNDUP).mean(),2)]

tmp = library_administrative_1994[library_administrative_1994.ATTEND>0]
library_administrative_1994_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1994_pruned.ATTEND / library_administrative_1994_pruned.POPU_UNDUP).mean(),2)])

tmp = library_administrative_1995[library_administrative_1995.ATTEND>0]
library_administrative_1995_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1995_pruned.ATTEND / library_administrative_1995_pruned.POPU_UNDUP).mean(),2)])

tmp = library_administrative_1996[library_administrative_1996.ATTEND>0]
library_administrative_1996_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1996_pruned.ATTEND / library_administrative_1996_pruned.POPU_UNDUP).mean(),2)])

tmp = library_administrative_1997[library_administrative_1997.ATTEND>0]
library_administrative_1997_pruned = tmp[tmp.POPU_UNDUP>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1997_pruned.ATTEND / library_administrative_1997_pruned.POPU_UNDUP).mean(),2)])

tmp = library_administrative_1998[library_administrative_1998.VISITS>0]
library_administrative_1998_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1998_pruned.VISITS / library_administrative_1998_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_1999[library_administrative_1999.VISITS>0]
library_administrative_1999_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_1999_pruned.VISITS / library_administrative_1999_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2000[library_administrative_2000.VISITS>0]
library_administrative_2000_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2000_pruned.VISITS / library_administrative_2000_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2001[library_administrative_2001.VISITS>0]
library_administrative_2001_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2001_pruned.VISITS / library_administrative_2001_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2002[library_administrative_2002.VISITS>0]
library_administrative_2002_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2002_pruned.VISITS / library_administrative_2002_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2003[library_administrative_2003.VISITS>0]
library_administrative_2003_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2003_pruned.VISITS / library_administrative_2003_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2004[library_administrative_2004.VISITS>0]
library_administrative_2004_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2004_pruned.VISITS / library_administrative_2004_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2005[library_administrative_2005.VISITS>0]
library_administrative_2005_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2005_pruned.VISITS / library_administrative_2005_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2006[library_administrative_2006.VISITS>0]
library_administrative_2006_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2006_pruned.VISITS / library_administrative_2006_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2007[library_administrative_2007.VISITS>0]
library_administrative_2007_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2007_pruned.VISITS / library_administrative_2007_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2008[library_administrative_2008.VISITS>0]
library_administrative_2008_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2008_pruned.VISITS / library_administrative_2008_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2009[library_administrative_2009.VISITS>0]
library_administrative_2009_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2009_pruned.VISITS / library_administrative_2009_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2010[library_administrative_2010.VISITS>0]
library_administrative_2010_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2010_pruned.VISITS / library_administrative_2010_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2011[library_administrative_2011.VISITS>0]
library_administrative_2011_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2011_pruned.VISITS / library_administrative_2011_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2012[library_administrative_2012.VISITS>0]
library_administrative_2012_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2012_pruned.VISITS / library_administrative_2012_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2013[library_administrative_2013.VISITS>0]
library_administrative_2013_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2013_pruned.VISITS / library_administrative_2013_pruned.POPU_UND).mean(),2)])

tmp = library_administrative_2014[library_administrative_2014.VISITS>0]
library_administrative_2014_pruned = tmp[tmp.POPU_UND>0]

visits_vs_users_1992_2014.extend([round((library_administrative_2014_pruned.VISITS / library_administrative_2014_pruned.POPU_UND).mean(),2)])

years = np.linspace(1992,2014,23).astype(int)

overall_visits = pd.DataFrame(visits_vs_users_1992_2014, years)
overall_visits.columns = ['Visit/Population']


p2 = Bar(overall_visits, values='Visit/Population', color="navy", legend=False, title="National Average Visits / Population")


p2.xaxis.axis_label = "Years"
p2.xaxis.axis_label_text_color = "#aa6666"
p2.xaxis.axis_label_standoff = 30

output_file('overall_visits.html')

p2.yaxis.axis_label = "Visit / Population"
p2.yaxis.axis_label_text_font_style = "italic"

show(p2)

