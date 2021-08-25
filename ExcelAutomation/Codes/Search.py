import pandas as pd
import numpy as np
excel_files = ['C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel1.xlsx','C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel2.xlsx']
for file in excel_files:
    df = pd.read_excel(file)
    pencil = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    print(file)
    print(pencil)
