class TestItem:
    def __init__(self) -> None:
        self.__sfi: str = None
        self.__item_name: str = None
        self.__class_attendance: str = None
        self.__flag_attendance: str = None
        self.__owner_attendance: str = None
        self.__record_status: str = None
        self.__responsible_dept: str = None
        self.__date: str = None
        self.__start_hour: str = None
        self.__est: str = None

    @property
    def sfi(self):
        return self.__sfi

    @sfi.setter
    def sfi(self, text: str) -> None:
        self.__sfi = text

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, text: str) -> None:
        self.__item_name = text

    @property
    def class_attendance(self):
        return self.__class_attendance

    @class_attendance.setter
    def class_attendance(self, text: str) -> None:
        self.__class_attendance = text

    @property
    def flag_attendance(self):
        return self.__flag_attendance

    @flag_attendance.setter
    def flag_attendance(self, text: str) -> None:
        self.__flag_attendance = text

    @property
    def owner_attendance(self):
        return self.__owner_attendance

    @owner_attendance.setter
    def sfi(self, text: str) -> None:
        self.__sfi = text

    @property
    def record_status(self):
        return self.__record_status

    @record_status.setter
    def record_status(self, text: str) -> None:
        self.__record_status = text

    @property
    def responsible_dept(self):
        return self.__responsible_dept

    @responsible_dept.setter
    def responsible_dept(self, text: str) -> None:
        self.__responsible_dept = text

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, text: str) -> None:
        self.__date = text

    @property
    def start_hour(self):
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, text: str) -> None:
        self.__start_hour = text

    @property
    def est(self):
        return self.__est

    @est.setter
    def est(self, text: str) -> None:
        self.__est = text


class Schedule:

    def __init__(self) -> None:
        self.__agenda_items: list

    @property
    def agenda_items(self) -> None:
        return self.__agenda_items

    @agenda_items.setter
    def agenda_items(self, items: list(TestItem)) -> None:
        self.__agenda_items = items
