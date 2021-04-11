from parse import parse_SAT_doc
import datetime as dt


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
        self.scheduleItems = []
        self.activeItems = []
        self.upcomingItems = []
        self.completedItems = []
        for item_dict in xldata:
            test_item = TestItem(item_dict)
            self.scheduleItems.append(test_item)

        self.sortItemsByStatus()

    def sortItemsByStatus(self):
        now = dt.datetime.now()
        # print(self.scheduleItems)
        for item in self.scheduleItems:
            if item.finnish_dt is None:
                if item.start_dt >= now:
                    self.upcomingItems.append(item)
                if item.start_dt <= now:
                    self.completedItems.append(item)
            else:
                if item.start_dt <= now <= item.finnish_dt:
                    self.activeItems.append(item)
                elif item.start_dt >= now:
                    self.upcomingItems.append(item)
                elif item.start_dt <= now:
                    self.completedItems.append(item)


if __name__ == '__main__':
    filename = './example/5_NB67_SAT_Schedule_Rev_3.xlsx'

    xldata = parse_SAT_doc(filename)

    schedule = Schedule(xldata)
