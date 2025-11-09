"""
This module is the internal logic of the assistant, how data is stored, 
what kind of data it is, and what can be done with it.
"""
from datetime import datetime, timedelta
from collections import UserDict
from helpers.constants import DATE_FORMAT, WEEK_DAYS_LIMIT
from entities.record import Record

class AddressBook(UserDict):
    """
    Class for managing a collection of contact records.
    """
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def find(self, name: str) -> Record | None:
        return self.data.get(name)
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        today = datetime.today().date()
        users: dict[str, Record] = self.data
        congratulation_dates = []

        for _, user in users.items():
            if user.birthday is None:
                continue
            user_birthday = user.birthday.value
            user_name = user.name.value

            birthday_year = datetime.strptime(user_birthday, DATE_FORMAT).date()
            birthday_this_year = birthday_year.replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            elif (birthday_this_year - today).days > WEEK_DAYS_LIMIT:
                continue
            
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            
            congratulation_dates.append({ "name": user_name, "congratulation_date": birthday_this_year.strftime(DATE_FORMAT) })
            
        return congratulation_dates
    def get_all_records(self) -> dict[str, Record]:
        return self.data
