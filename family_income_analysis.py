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


## download 2014 library data
library_administrative_2014 = pd.read_json("https://data.imls.gov/resource/76da-i3z6.json?$limit=100000")

## get the 2014 Household income
income_2014 = pd.read_csv("Census_csv/est14ALL_mod.csv")

a = income_2014.Name.str.replace(' County','').str.upper()  ## str.replace get rid of ' County' and str.upper modify the text to upper case
income_2014.Name = a

b = income_2014.Median_Household_Income.str.replace(',','')
income_2014.Median_Household_Income = b.convert_objects(convert_numeric=True)

## adding the state to the county name
income_2014_fix = pd.DataFrame(income_2014.Name + " " + income_2014.Postal_Code)
income_2014_fix.columns = ['County']
income_2014_fix['Income'] = income_2014.Median_Household_Income


library_administrative_2014_reduced = pd.DataFrame(library_administrative_2014.county + " " + library_administrative_2014.state)
library_administrative_2014_reduced.columns = ['County']
library_administrative_2014_reduced['Visits'] = library_administrative_2014.visits


## removing rows with negative visits
library_administrative_2014_reduced = library_administrative_2014_reduced[library_administrative_2014_reduced.Visits>0]


q = library_administrative_2014_reduced.groupby('County').sum()

income_and_library_administrative_2014 = pd.merge(left=q.reset_index(), right=income_2014_fix, left_on='County', right_on='County', how='left')

income_and_library_administrative_2014 = income_and_library_administrative_2014.dropna()
income_and_library_administrative_2014.Income = income_and_library_administrative_2014.Income.astype(np.int64)


output_file('county.html')
p = figure(title="Income vs Visits in 2014")
p.circle(x=income_and_library_administrative_2014.Income/1000, y=income_and_library_administrative_2014.Visits,  color="navy", size=2)
html = file_html(p, "Income vs Visits")

p.xaxis.axis_label = "Median Household Income (in thousands $)"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 30

p.yaxis.axis_label = "Number of Visits per County"
p.yaxis.axis_label_text_font_style = "italic"

show(p)
