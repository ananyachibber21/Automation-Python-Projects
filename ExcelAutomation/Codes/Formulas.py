import openpyxl

excel_files = ['C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel1.xlsx','C:/Users/HP/Documents/PythonProjects/ExcelAutomation/Excel2.xlsx']
for file in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb["SalesOrders"]
    worksheet['G46'] = '=AVERAGE(G3:G45)'
    wb.save(file)
