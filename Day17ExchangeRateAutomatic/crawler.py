import openpyxl

workbook = openpyxl.load_workbook('匯率即時更新.xlsx') #open .xlsx file
sheet = workbook['即時匯率'] #choose worksheet

mxR = sheet.max_row #get max row of this sheet
print(mxR)
