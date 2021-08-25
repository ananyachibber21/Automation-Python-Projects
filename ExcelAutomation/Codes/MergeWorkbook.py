import pandas as pd

excel_files = ['C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel1.xlsx','C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel2.xlsx']
merge = pd.DataFrame()
for file in excel_files:
  df = pd.read_excel(file, skiprows = 1)
  merge = merge.append(df, ignore_index = True)
  
merge.to_excel('C:/Users/HP/Documents/PythonProjects/ExcelAutomation/BlankBook.xlsx')
