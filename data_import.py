import pandas as pd

xls = pd.ExcelFile('nba_draft.xlsx')
sam = pd.read_excel(xls, 'sam')
adam = pd.read_excel(xls, 'adam')
stats = pd.read_excel(xls, 'stats')

sam.to_pickle('sam.pkl')
adam.to_pickle('adam.pkl')
stats.to_pickle('stats.pkl')


print("Done")