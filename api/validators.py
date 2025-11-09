from helpers.loggers import log_error

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return log_error(f"Enter correct inputs please: {e}")
        except IndexError:
            return log_error("Enter correct user name.")
        except KeyError:
            return log_error("This contact does not exist.")

    return inner
