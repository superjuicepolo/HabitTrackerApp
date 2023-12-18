import pickle
from typing import List
from habit import Habit


def save_habits_to_file(filename: str, habits: List[Habit]):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(habits, file)
    except Exception as e:
        print(f'Error saving habits to {filename}: {e}')


# This function loads array of Habits from file
def load_habits_from_file(filename: str):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f'Error loading habits from {filename}: {e}')

