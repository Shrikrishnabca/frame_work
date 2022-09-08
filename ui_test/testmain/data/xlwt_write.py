from xlwt import Workbook
def write_data(data):
    wb=Workbook()
    sheet1=wb.add_sheet("Sheet1",True)
    sheet1.write(0,0,data)
    wb.save("hello.xls")
