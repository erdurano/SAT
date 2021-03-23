import datetime as dt
from openpyxl import load_workbook

workbook = load_workbook(filename='./example/5_NB67_SAT_Schedule_Rev_3.xlsx')

test_sheet = workbook.active

xldate = test_sheet["J19"].value
xlhour = test_sheet["K19"].value
xlhour_delta = dt.timedelta(hours=xlhour.hour, minutes=xlhour.minute)
xltime = xldate + xlhour_delta


if __name__ == "__main__":
    print(xltime)
