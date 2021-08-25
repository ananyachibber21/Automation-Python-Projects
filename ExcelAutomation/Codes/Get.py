import openpyxl

excel_Files = ['C:\Users\HP\Documents\Python Projects\ExcelAutomation\Excel1.xlsx','C:\Users\HP\Documents\Python Projects\ExcelAutomation\Excel2.xlsx']
values = []
for file in excel_Files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook('Sales Order')
    cell_value = worksheet('G11').values
    values.append(cell_value)

    print(cell_value)
