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


def parse_times(date=None, start_hour=None, duration=None):
    xldate = date
    xlhour = start_hour
    xlduration_str = duration

    if (xldate and xlhour):
        xlhour_delta = dt.timedelta(hours=xlhour.hour, minutes=xlhour.minute)
        start_time_dt = xldate + xlhour_delta
    else:
        start_time_dt = None

    if xlduration_str is None:
        end_time_dt = None
    else:
        end_time_dt = start_time_dt + parse_duration_str(xlduration_str)

    return {
        'start_datetime': start_time_dt,
        'estimated_finish': end_time_dt
    }


# TODO : Develop the function for outputting a list of dictionaries that
# contains ONLY TEST ITEMS
def parse_SAT_doc(file_path):
    worksheet = load_workbook(file_path).active

    test_agenda = []
    cls_title_row = None

    for index, row in enumerate(worksheet.iter_rows(values_only=True)):
        if ('Class' in row) and (cls_title_row is None):
            cls_title_row = index
            cls_title_column = row.index('Class')

        if cls_title_row is not None:

            test_row = {
                "sfi": row[cls_title_column - 2],
                "item_name": row[cls_title_column - 1],
                "class_att": row[cls_title_column],
                "flag_att": row[cls_title_column + 1],
                "owner_att": row[cls_title_column + 2],
                "rec_stat": row[cls_title_column + 3],
                "resp_rept": row[cls_title_column + 4],
            }

            time_frame = parse_times(
                row[cls_title_column + 5],
                row[cls_title_column + 6],
                row[cls_title_column + 7],
            )
            test_row.update(time_frame)

            test_agenda.append(test_row)
    return test_agenda


if __name__ == "__main__":
    filename = './example/5_NB67_SAT_Schedule_Rev_3.xlsx'

    print(parse_SAT_doc(filename))
