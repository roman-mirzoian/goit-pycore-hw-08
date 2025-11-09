def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def get_not_found_record_message(name: str) -> str:
    return f"Contact with name {name} was not found"