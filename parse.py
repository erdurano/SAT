from openpyxl import load_workbook
import datetime as dt


def parse_duration_str(xlduration_str):
    dur_pieces = xlduration_str.split(" ")

    if 'min' in dur_pieces[-1]:
        return dt.timedelta(minutes=int(dur_pieces[-2]))

    if 'hour' in dur_pieces[-1]:
        if '.' in dur_pieces[-2]:
            nums = dur_pieces[-2].split('.')
            return dt.timedelta(hours=int(nums[0]), minutes=int(nums[1]))
        else:
            return dt.timedelta(hours=int(dur_pieces[-2]))

    if 'day' in dur_pieces[-1]:
        return dt.timedelta(days=int(dur_pieces[-2]))


# TODO : Develop the function for outputting a list of dictionary that contains
# ONLY TEST ITEMS
def parse_SAT_doc(worksheet):
    for index, row in enumerate(worksheet.iter_rows(values_only=True)):
        if 'Class' in row:
            header_vert_index = index
            header_horiz_index = row.index('Class')
            break
    return (header_vert_index, header_horiz_index)


test_sheet = load_workbook(
    filename='./example/5_NB67_SAT_Schedule_Rev_3.xlsx'
    ).active

xldate = test_sheet.cell(row=48, column=10).value
xlhour = test_sheet.cell(row=48, column=11).value
xlduration_str = test_sheet.cell(row=48, column=12).value
xlhour_delta = dt.timedelta(hours=xlhour.hour, minutes=xlhour.minute)
start_time_dt = xldate + xlhour_delta
end_time_dt = start_time_dt + parse_duration_str(xlduration_str)


if __name__ == "__main__":
    print(start_time_dt)
    print(end_time_dt)
    for index, row in enumerate(test_sheet.iter_rows(values_only=True)):
        print("Class" in row)
        print(row)
        print(index)
