import pandas as pd
import numpy as np
import openpyxl

#import csv as dataframe for keyword searching
df = pd.read_csv('/Users/at-h/Desktop/github/ameliat-h.github.io/final project scripts/buildingpermits_clean_4_7_MR.csv', sep=',')

#identify csv columns
df.columns
df.head()
type(df.columns)
print(df)

#identifying "green" keywords

results = df[df['Comments'].str.contains('sustainable sites') |
df['Comments'].str.contains('site selection') |
df['Comments'].str.contains('development density') |
df['Comments'].str.contains('brownfield') |
df['Comments'].str.contains('alternative transport') |
df['Comments'].str.contains('low emitting') |
df['Comments'].str.contains('alternative parking') |
df['Comments'].str.contains('stormwater quantity') |
df['Comments'].str.contains('stormwater quality') |
df['Comments'].str.contains('heat island') |
df['Comments'].str.contains('waste water management') |
df['Comments'].str.contains('light pollution') |
df['Comments'].str.contains('water efficiency') |
df['Comments'].str.contains('water efficient landscaping') |
df['Comments'].str.contains('innovative waste water') |
df['Comments'].str.contains('water use reduction') |
df['Comments'].str.contains('energy atmosphere') |
df['Comments'].str.contains('optimize') |
df['Comments'].str.contains('enhanced refrigeration') |
df['Comments'].str.contains('green power') |
df['Comments'].str.contains('maintain existing walls') |
df['Comments'].str.contains('building reuse') |
df['Comments'].str.contains('construction waste') |
df['Comments'].str.contains('materials reuse') |
df['Comments'].str.contains('recycled content') |
df['Comments'].str.contains('rapidly renewable') |
df['Comments'].str.contains('certified wood') |
df['Comments'].str.contains('indoor environment') |
df['Comments'].str.contains('outdoor air') |
df['Comments'].str.contains('increased vent') |
df['Comments'].str.contains('low emitting adhesives') |
df['Comments'].str.contains('low emitting paints') |
df['Comments'].str.contains('low emitting flooring') |
df['Comments'].str.contains('low emitting composite wood') |
df['Comments'].str.contains('composite wood') |
df['Comments'].str.contains('controlability lighting') |
df['Comments'].str.contains('controlability thermal') |
df['Comments'].str.contains('thermal comfort design') |
df['Comments'].str.contains('thermal comfort verification') |
df['Comments'].str.contains('innovation and design') |
df['Comments'].str.contains('air quality') |
df['Comments'].str.contains('alternative energy') |
df['Comments'].str.contains('carbon neutral') |
df['Comments'].str.contains('clean water') |
df['Comments'].str.contains('conserve energy') |
df['Comments'].str.contains('cradle to cradle') |
df['Comments'].str.contains('daylight') |
df['Comments'].str.contains('eco friendly') |
df['Comments'].str.contains('efficiency') |
df['Comments'].str.contains('efficient') |
df['Comments'].str.contains('energy efficiency') |
df['Comments'].str.contains('environment') |
df['Comments'].str.contains('environmental') |
df['Comments'].str.contains('environmental quality') |
df['Comments'].str.contains('geothermal') |
df['Comments'].str.contains('green') |
df['Comments'].str.contains('green architecture') |
df['Comments'].str.contains('green infrastructure') |
df['Comments'].str.contains('greywater') |
df['Comments'].str.contains('harvest') |
df['Comments'].str.contains('high-performance') |
df['Comments'].str.contains('human health') |
df['Comments'].str.contains('increase ventilation') |
df['Comments'].str.contains('inexpensive material') |
df['Comments'].str.contains('integrated pest management') |
df['Comments'].str.contains('isolative') |
df['Comments'].str.contains('life cycle') |
df['Comments'].str.contains('light pollution') |
df['Comments'].str.contains('lighting control') |
df['Comments'].str.contains('local') |
df['Comments'].str.contains('low emitting') |
df['Comments'].str.contains('Low energy usage') |
df['Comments'].str.contains('low water usage') |
df['Comments'].str.contains('native') |
df['Comments'].str.contains('natural') |
df['Comments'].str.contains('natural ventilation') |
df['Comments'].str.contains('noise pollution') |
df['Comments'].str.contains('permeable pavement') |
df['Comments'].str.contains('pest') |
df['Comments'].str.contains('photovoltaic') |
df['Comments'].str.contains('public transportation') |
df['Comments'].str.contains('rainwater') |
df['Comments'].str.contains('rainwater retention') |
df['Comments'].str.contains('reclaimed') |
df['Comments'].str.contains('recycled') |
df['Comments'].str.contains('recycling materials') |
df['Comments'].str.contains('reduce consumption') |
df['Comments'].str.contains('reduce hazard') |
df['Comments'].str.contains('reduce pollution') |
df['Comments'].str.contains('Reducing waste') |
df['Comments'].str.contains('reduction') |
df['Comments'].str.contains('reflective coating') |
df['Comments'].str.contains('renewable') |
df['Comments'].str.contains('renewable energy') |
df['Comments'].str.contains('renewable technologies') |
df['Comments'].str.contains('renewal') |
df['Comments'].str.contains('resilience') |
df['Comments'].str.contains('resilient') |
df['Comments'].str.contains('resource-efficient') |
df['Comments'].str.contains('responsible materials') |
df['Comments'].str.contains('retention system') |
df['Comments'].str.contains('reuse') |
df['Comments'].str.contains('safe water') |
df['Comments'].str.contains('shared parking') |
df['Comments'].str.contains('skylight') |
df['Comments'].str.contains('smart') |
df['Comments'].str.contains('smart-grid') |
df['Comments'].str.contains('soil compaction') |
df['Comments'].str.contains('solar') |
df['Comments'].str.contains('solar electric') |
df['Comments'].str.contains('solar thermal') |
df['Comments'].str.contains('sustainability') |
df['Comments'].str.contains('sustainable') |
df['Comments'].str.contains('thermal comfort') |
df['Comments'].str.contains('thermal heating') |
df['Comments'].str.contains('toxic material') |
df['Comments'].str.contains('waste reduction') |
df['Comments'].str.contains('water resistant') |
df['Comments'].str.contains('zero net energy') |
df['Comments'].str.contains('zero-waste') |
df['Comments'].str.contains('low-emitting materials') |
df['Comments'].str.contains('construction indoor air quality management plan') |
df['Comments'].str.contains('indoor air quality assessment') |
df['Comments'].str.contains('thermal comfort') |
df['Comments'].str.contains('interior lighting') |
df['Comments'].str.contains('daylight') |
df['Comments'].str.contains('quality views') |
df['Comments'].str.contains('acoustic performance') |
df['Comments'].str.contains('air quality management plan') |
df['Comments'].str.contains('building life-cycle impact reduction') |
df['Comments'].str.contains('sensitive land protection') |
df['Comments'].str.contains('high priority site') |
df['Comments'].str.contains('surrounding density and diverse uses') |
df['Comments'].str.contains('access to quality transit') |
df['Comments'].str.contains('bicycle facilities') |
df['Comments'].str.contains('reduced parking footprint') |
df['Comments'].str.contains('green vehicles') |
df['Comments'].str.contains('outdoor water use reduction') |
df['Comments'].str.contains('indoor water use reduction') |
df['Comments'].str.contains('cooling tower water use') |
df['Comments'].str.contains('water metering') |
df['Comments'].str.contains('optimize energy performance') |
df['Comments'].str.contains('advanced energy metering') |
df['Comments'].str.contains('demand response') |
df['Comments'].str.contains('renewable energy production') |
df['Comments'].str.contains('enhanced refrigerant management') |
df['Comments'].str.contains('minimum energy performance') |
df['Comments'].str.contains('building-level energy metering') |
df['Comments'].str.contains('optimize energy performance') |
df['Comments'].str.contains('advanced energy metering') |
df['Comments'].str.contains('renewable energy production') |
df['Comments'].str.contains('indoor water use reduction') |
df['Comments'].str.contains('outdoor water use reduction') |
df['Comments'].str.contains('building-level water metering') |
df['Comments'].str.contains('heat island reduction') |
df['Comments'].str.contains('light pollution reduction') |
df['Comments'].str.contains('rainwater management') |
df['Comments'].str.contains('protect or restore habitat') |
df['Comments'].str.contains('reduced parking footprint') |
df['Comments'].str.contains('bicycle facilities') |
df['Comments'].str.contains('access to quality transit') |
df['Comments'].str.contains('optimize energy') |
df['Comments'].str.contains('collection of recyclables') |
df['Comments'].str.contains('low-emitting materials') |
df['Comments'].str.contains('rainwater management') |
df['Comments'].str.contains('regional materials') |
df['Comments'].str.contains('certified wood') |
df['Comments'].str.contains('recycled materials') |
df['Comments'].str.contains('material reuse') |
df['Comments'].str.contains('increased ventilation') |
df['Comments'].str.contains('low-emitting') |
df['Comments'].str.contains('pollutant source control') |
df['Comments'].str.contains('brownfield redevelopment') |
df['Comments'].str.contains('public transportation access') |
df['Comments'].str.contains('low-emitting and fuel-efficient vehicles') |
df['Comments'].str.contains('protect or restore habitat') |
df['Comments'].str.contains('innovative wastewater technologies')]

df.shape
results.shape
results.head()
type(results)

results['DESCRIPTION'].unique()

results.head(40)

# results[results['Comments'].str.contains('Sweetgreen')]
# #for kicks, trying to see how many rows come up just by searching for "green":
# green = df['Comments'].str.contains('green')
#
# #for some reason below only results the boolean values? not full row data
# just_green.to_csv("buildingpermits_clean_4_7_MR_green search only_4_7.csv")

#printing to new csv with rows that contain keywords
# results.to_csv("bldgpermits_clean_search_results.csv",sep=',',encoding='utf8')

#results to csv was printing wonky formatting in table, but export to xlsx works!km
writer = pd.ExcelWriter('keyword_results_4_17.xlsx')
results.to_excel(writer,'results')
writer.save()







###attempts at other methods below!

#tried below based on: https://stackoverflow.com/questions/26577516/pandas-test-if-string-contains-one-of-the-substrings-in-a-list
# df[df.columns.str.contains('wink|sticky')]

# print(searchfor)
# df[df['Comments'].str.contains("searchfor)]

# df[df.columns.contains('|'.join(searchfor))]

# help from here: https://davidhamann.de/2017/06/26/pandas-select-elements-by-string/

#returns a table with only the rows where the "comments" column includes the term 'wink'
# df[df['Comments'].str.contains('wink')]


#but when trying to return searches for multiple terms with Eric's suggested code, doesn't work (below): error: "truth value of a Series is ambiguous":
# df[df['Comments'] == 'wink' or df['Comments'] == 'sticky']
# tries | instead of or, also doesn't work
# df[df['Comments'] == 'wink' | df['Comments'] == 'sticky']

#searches for restaurants in the categories of businesses
# businesses[businesses['categories'] == 'Restaurants']
#
# df[df['Comments'] == 'glue']
#
# df[df.columns.contains('|'.join(searchfor))]
# df['Comments'].str.contains('excited')
#
# searchfor = ['glue', 'low']
# results = df.['Comments'].str.contains('|'.join(searchfor))
# results.head

# ['Comments'].str.contains('|'.join(searchfor)

# df.groupby('ID')[('Comments')].str.contains('|'.join(searchfor)).head

# We can use the `.groupby()` method to collapse a DataFrame on the values stored in a given column. For those of you who know SQL, this should be somewhat familiar; for each unique value stored in the date column, we're executing a given method, in this case, `.describe()`. The output of this operation is a table in which each row represents a date, and each column is a summary statistic of the `count` column.
# df.groupby(results.head)['ID'].describe
# results.to_csv("keyword search results.csv")
