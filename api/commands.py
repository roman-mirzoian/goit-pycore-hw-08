from entities.address_book import AddressBook
from helpers.helpers import get_not_found_record_message
from entities.record import Record
from api.validators import input_error
from helpers.constants import WEEK_DAYS_LIMIT

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        all_record_phones = record.get_phone_values()
        if phone in all_record_phones:
            return f"Contact {name} already has this phone number."
        
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        message = get_not_found_record_message(name)
    else:
        record.edit_phone(old_phone, new_phone)

    return message

@input_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    message = "Contact deleted."
    if record is None:
        message = get_not_found_record_message(name)
    else:
        book.delete(name)

    return message

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        return get_not_found_record_message(name)
    else:
        all_record_phones = record.get_phone_values()
        return f"Contact {name} has next phones: {', '.join(all_record_phones)}"
    
@input_error
def remove_phone(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if record is None:
        return get_not_found_record_message(name)
    else:
        all_record_phones = record.get_phone_values()
        if not phone in all_record_phones:
            return f"Contact {name} doesn't have this phone"
        
        record.remove_phone(phone)
        return f"Contact {name} phone was removed."

def show_all(book: AddressBook):
    records = book.get_all_records()
    if not records or len(list(records.keys())) < 1:
        return "No contacts saved."
    
    result = "Contact list:\n"
    for _, record in records.items():
        result += f"    {record}\n"
    return result.strip()

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        return get_not_found_record_message(name)
    else:
        record.add_birthday(birthday)
        return "New birthday date was added"
    
@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        return get_not_found_record_message(name)
    else:
        return record.birthday
    
def get_birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if len(upcoming_birthdays) < 1:
        return f"No upcoming birthdays in near {WEEK_DAYS_LIMIT} days"
    
    result = 'The next user should be congrats:\n'
    for birthday in upcoming_birthdays:
        result += f"    {birthday.get('name')} at {birthday.get('congratulation_date')}\n"
    return result.strip()