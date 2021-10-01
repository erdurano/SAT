from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Status(Enum):
    NOT_STARTED = 'Not Started'
    ACTIVE = 'Active'
    PASSED = 'Passed'
    FAILED = 'Failed'


@dataclass
class TestItem():
    sfi: Optional[str] = None
    item_name: Optional[str] = None
    class_attendance: Optional[str] = None
    flag_attendance: Optional[str] = None
    owner_attendance: Optional[str] = None
    record_status: Optional[str] = None
    responsible_dept: Optional[str] = None
    date: Optional[str] = None
    start_hour: Optional[str] = None
    est: Optional[str] = None
    status: str = 'Passive'
    # self.__status: Status = Status.NOT_STARTED


class Schedule():

    def __init__(self) -> None:
        self.__agenda_items: list = []

    @property
    def agenda_items(self) -> list:
        return self.__agenda_items

    @agenda_items.setter
    def agenda_items(self, items: list[TestItem]) -> None:
        self.__agenda_items = items

    def add_item(self, agenda_item: TestItem) -> None:
        self.__agenda_items.append(agenda_item)

    def reset_items(self):
        self.__agenda_items = []


if __name__ == '__main__':
    print(Status.NOT_STARTED.value)
