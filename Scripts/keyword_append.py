import pandas as pd
import numpy as np
import openpyxl

#import csv as dataframe for keyword searching#CHANGE TO PRODUCT SCRIPT
df = pd.read_csv('/Users/at-h/Desktop/github/ameliat-h.github.io/final project scripts/data/keyword_results_4_24.csv', sep=',')
print(df)


# #import csv of search terms as dataframe
# df_keywords = pd.read_csv('/Users/at-h/Desktop/github/ameliat-h.github.io/final project scripts/data/kwords4_24.csv', sep=',')
# #second attempt to define keyword dataframe's values as array:
# keywords = np.asarray(df_keywords)
# print(keywords)

#define building permit dataframe's values as variable "source"
# source = np.asarray(df['Comments'])
# print(source)
#for w in the variable source:

#thoughts from phoebe for for loop: keep keywords one/cell, create additional column for each matched keywords
#try to build a for loop that looks for one keyword at a time, and then build a second loop that goes through everything again with the WHOLE list of loops

# for blank in blank
# then do another for blank in blank

#define as boolean after if statement, not match
#we might need a loop in a loop to keep searchign for additional search terms even if it finds more
match = []

for row in df['Comments']:
    # if df[df['Comments'].str.contains('green'):
    # if row == 'green':
    #the below causes green to be appended to EVERY row
    if df['Comments'].str.contains('green').any():
        match.append('green')
    else:
        match.append('')

df['match'] = match


df.head()

print (df)
#results to csv was printing wonky formatting in table, but export to xlsx works!km
writer = pd.ExcelWriter('kwords_appended_4_25.xlsx')
df.to_excel(writer,'df')
writer.save()
    #if row matches
    # if source.str.contains(keywords):
    #     w.append()
    #
    # str.contains('keyword_list'):
    # match.append(True)
#searching for match of keyword column in
# match = df_keywords[df_keywords['keyword'].str.contains('air quality')

#eric's beginning structure:
# keywords = ['','','']

# https://stackoverflow.com/questions/47291186/adding-values-to-new-pandas-dataframe-column-based-on-partial-string-contents-of
# shoes_df['brand'] = shoes_df.Product.str.extract(pat='(Nike|Adidas|Asics)',expand=False)
