"""
Main module for working with bot
"""
from entities.address_book import AddressBook
from api.commands import add_birthday, add_contact, change_contact, get_birthdays, show_all, show_birthday, show_phone
from helpers.helpers import parse_input
from helpers.loggers import log_answer, log_base, log_error

def main():
    """
    Main handler for bot commands
    """
    book = AddressBook()
    log_base("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            log_answer("Good bye!")
            return

        if command == "hello":
            log_answer("How can I help you?")
        elif command == "add":
            log_answer(add_contact(args, book))
        elif command == "change":
            log_answer(change_contact(args, book))
        elif command == "phone":
            log_answer(show_phone(args, book))
        elif command == "all":
            log_answer(show_all(book))
        elif command == "add-birthday":
            log_answer(add_birthday(args, book))
        elif command == "show-birthday":
            log_answer(show_birthday(args, book))
        elif command == "birthdays":
            log_answer(get_birthdays(book))
        else:
            log_error("Invalid command.")

if __name__ == "__main__":
    main()
