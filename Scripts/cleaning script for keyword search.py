import pandas as pd
import numpy as np

#import test csv as dataframe for keyword searching
df = pd.read_csv('/Users/at-h/Desktop/github/ameliat-h.github.io/final project scripts/buildingpermits_clean_4_7_MR.csv', sep=',')

#identify csv columns
df.columns
type(df.columns)
print(df)

results = df[df['COMMENTS'].str.contains('wink') | df['COMMENTS'].str.contains('glue')]

results.to_csv("keyword search results.csv")

#terms to search for:
air quality	smart	renewable	Resilience
carbon neutral	smart-grid	green infrastructure	adapt
conserve energy	efficient	human health	sustainability
eco friendly	reuse	environmental	lighting control
Energy efficiency	reclaimed	efficiency	zero net energy
environmental quality	cradle to cradle	integrated pest management	environment
geothermal	recycled	high-performance	greywater
green	natural	waste reduction	Photovoltaic
green architecture	zero-waste	safe water	thermal heating
harvest	high-performance	clean water	solar
increase ventilation	responsible materials	native	solar thermal
inexpensive material		local
isolative		daylight
Life cycle		skylight
light pollution
low emitting
Low energy usage
low water usage
natural ventilation
noise pollution
permeable pavement
pest
public transportation
rainwater
rainwater retention
recycling materials
reduce consumption
reduce hazard
reduce pollution
Reducing waste
reduction
reflective coating
renewable energy
renewable technologies
renewal
resilient
resource-efficient
retention system
shared parking
soil compaction
solar
solar electric
sustainable
thermal comfort
toxic material
water resistant


###attempts at other methods below!

#tried below based on: https://stackoverflow.com/questions/26577516/pandas-test-if-string-contains-one-of-the-substrings-in-a-list
# df[df.columns.str.contains('wink|sticky')]

# print(searchfor)
# df[df['COMMENTS'].str.contains("searchfor)]

# df[df.columns.contains('|'.join(searchfor))]

# help from here: https://davidhamann.de/2017/06/26/pandas-select-elements-by-string/

#returns a table with only the rows where the "comments" column includes the term 'wink'
# df[df['COMMENTS'].str.contains('wink')]


#but when trying to return searches for multiple terms with Eric's suggested code, doesn't work (below): error: "truth value of a Series is ambiguous":
# df[df['COMMENTS'] == 'wink' or df['COMMENTS'] == 'sticky']
# tries | instead of or, also doesn't work
# df[df['COMMENTS'] == 'wink' | df['COMMENTS'] == 'sticky']

#searches for restaurants in the categories of businesses
# businesses[businesses['categories'] == 'Restaurants']
#
# df[df['COMMENTS'] == 'glue']
#
# df[df.columns.contains('|'.join(searchfor))]
# df['COMMENTS'].str.contains('excited')
#
# searchfor = ['glue', 'low']
# results = df.['COMMENTS'].str.contains('|'.join(searchfor))
# results.head

# ['COMMENTS'].str.contains('|'.join(searchfor)

# df.groupby('ID')[('COMMENTS')].str.contains('|'.join(searchfor)).head

# We can use the `.groupby()` method to collapse a DataFrame on the values stored in a given column. For those of you who know SQL, this should be somewhat familiar; for each unique value stored in the date column, we're executing a given method, in this case, `.describe()`. The output of this operation is a table in which each row represents a date, and each column is a summary statistic of the `count` column.
# df.groupby(results.head)['ID'].describe
# results.to_csv("keyword search results.csv")
