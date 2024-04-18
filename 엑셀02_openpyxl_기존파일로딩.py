import openpyxl as op 

# "c:\\work\\test.xlsx" or r"c:\work\test.xlsx"
wb = op.load_workbook("test.xlsx")

#새로운 시트 추가 
ws = wb.create_sheet("직원명부")

wb.save("test2.xlsx")

