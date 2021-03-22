import pylightxl as xl
import datetime as dt

db = xl.readxl(fn='./example/5_NB67_SAT_Schedule_Rev_3.xlsx')

test_sheet = db.ws(db.ws_names[0])

xldate = test_sheet.address(address="J19")
xlhour = test_sheet.address(address="K19")
xltime = xldate + xlhour

def _from_xl_time(xltime):
    _epoch = dt.datetime(1900, 1, 1)
    time_delta = dt.timedelta(days=xltime-2)
    return _epoch + time_delta


date = _from_xl_time(xltime)

print(date)
