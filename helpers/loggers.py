from colorama import Fore

def log_base(message):
    print(f"{Fore.BLUE}{message}{Fore.RESET}")

def log_answer(message):
    print(f"{Fore.GREEN}{message}{Fore.RESET}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {message} {Fore.RESET}")