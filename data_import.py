import pandas as pd

xls = pd.ExcelFile('nba_draft.xlsx')
sam = pd.read_excel(xls, 'sam')
stats = pd.read_excel(xls, 'stats')

sam.to_pickle('sam.pkl')
stats.to_pickle('stats.pkl')
