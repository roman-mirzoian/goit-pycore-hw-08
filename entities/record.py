from datetime import datetime
from helpers.constants import DATE_FORMAT

class Field:
    """
    Base class for all contact fields.
    Contains the attribute 'value' to store the field's data.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Class for storing the contact's name.
    Name is required; its presence is validated upon creation.
    """
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError('Name should be exist')
        super().__init__(name)

class Phone(Field):
    """
    Class for storing a phone number.
    Validates that the number consists of exactly 10 digits upon creation.
    """
    def __init__(self, phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError('Number length should be 10 digits')
        super().__init__(phone)

class Birthday(Field):
    """
    Class for storing a birthday in proper format.
    """
    def __init__(self, value: str):
        try:
            birthday = datetime.strptime(value, DATE_FORMAT).date()
            super().__init__(birthday.strftime(DATE_FORMAT))
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    """
    Class for storing a single contact.
    Contains a Name object and a list of Phone objects.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None

    def get_phone_values(self):
        return list(map(lambda p: p.value, self.phones))

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, old_phone: str, new_phone: str):
        phone_as_strings = self.get_phone_values()
        if old_phone in phone_as_strings:
            phone_index = phone_as_strings.index(old_phone)
            self.phones[phone_index] = Phone(new_phone)
    def find_phone(self, phone: str):
        phone_as_strings = self.get_phone_values()
        if phone in phone_as_strings:
            return phone
        return None
    def add_birthday(self, date: str):
        self.birthday = Birthday(date)
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
