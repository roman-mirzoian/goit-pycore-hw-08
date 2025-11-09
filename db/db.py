"""
Functions for working with saving data as db
"""
from pathlib import Path
import pickle
from entities.address_book import AddressBook

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "address_book.pkl"

def save_data(book, filename=FILE_PATH):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename=FILE_PATH):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
