"""
Main module for working with bot
"""
from db.db import load_data, save_data
from api.commands import add_birthday, add_contact, change_contact, get_birthdays, show_all, show_birthday, show_phone
from helpers.helpers import parse_input
from helpers.loggers import log_answer, log_base, log_error

def main():
    """
    Main handler for bot commands
    """
    book = load_data()
    log_base("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
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
                log_error(f"Invalid command: {command}")
    except KeyboardInterrupt:
        save_data(book)
        print("\nGood bye!")

if __name__ == "__main__":
    main()
