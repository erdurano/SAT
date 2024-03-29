from dataclasses import dataclass, field
from datetime import datetime, time
from enum import Enum
from typing import Optional


class Status(Enum):
    NOT_STARTED = "Not Started"
    ACTIVE = "Active"
    PASSED = "Passed"
    FAILED = "Failed"
    COMMENTED = "Commented"


@dataclass
class TestItem:
    sfi: Optional[str] = None
    item_name: Optional[str] = None
    class_attendance: Optional[str] = None
    flag_attendance: Optional[str] = None
    owner_attendance: Optional[str] = None
    record_status: Optional[str] = None
    responsible_dept: Optional[str] = None
    date: Optional[datetime] = None
    start_hour: Optional[time] = None
    est: Optional[time] = None
    status: Status = Status.NOT_STARTED
    responsible_name: Optional[str] = ""

    def dt(self):
        if self.date and self.start_hour:
            return datetime(
                self.date.year,
                self.date.month,
                self.date.day,
                self.start_hour.hour,
                self.start_hour.minute,
            )
        else:
            return datetime(0, 0, 0, 0, 0)


@dataclass
class Schedule:
    agenda_items: list[TestItem] = field(default_factory=list)
    responsible_selection: list[str] = field(default_factory=list)
    hull_number: str = ""
    owner_firm: str = ""

    def add_item(self, agenda_item: TestItem) -> None:
        self.agenda_items.append(agenda_item)

    def reset_items(self) -> None:
        self.agenda_items = []
        self.hull_number = ""
        self.owner_firm = ""
        self.responsible_selection = []
