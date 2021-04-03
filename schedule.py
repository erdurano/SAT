from parse import parse_SAT_doc


class TestItem():
    # Constructor class for managing test items.
    def __init__(self, item_dict):
        self.sfi = item_dict["sfi"]
        self.item_name = item_dict["item_name"]
        self.class_attendance = item_dict["class_att"]
        self.flag_attendance = item_dict["flag_att"]
        self.owner_attendance = item_dict["owner_att"]
        self.to_be_followed = item_dict["rec_stat"]
        self.responsible = item_dict["resp_dept"]
        self.start_dt = item_dict["start_datetime"]
        self.finnish_dt = item_dict["estimated_finish"]


class Schedule():
    # A class for creating and managing test item graphics
    def __init__(self, xldata):
        for item_dict in xldata:
            test_item = TestItem(item_dict)
            print(test_item.item_name,
                  test_item.start_dt,
                  test_item.finnish_dt)


if __name__ == '__main__':
    filename = './example/5_NB67_SAT_Schedule_Rev_3.xlsx'

    xldata = parse_SAT_doc(filename)

    schedule = Schedule(xldata)
