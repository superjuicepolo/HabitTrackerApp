import pickle
from typing import List
from habit import Habit


def save_habits_to_file(filename: str, habits: List[Habit]):
    """
        Save a list of Habit objects to a file using pickle serialization.

        Parameters:
            filename (str): The name of the file where the habits will be saved.
            habits (List[Habit]): A list of Habit objects to be saved.

        Returns:
            None
        """
    try:
        with open(filename, 'wb') as file:
            pickle.dump(habits, file)
    except Exception as e:
        print(f'Error saving habits to {filename}: {e}')



def load_habits_from_file(filename: str):
    """
        Load a list of Habit objects from a file using pickle deserialization.

        Parameters:
            filename (str): The name of the file from which the habits will be loaded.

        Returns:
            List[Habit]: A list of Habit objects loaded from the file.
        """
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f'Error loading habits from {filename}: {e}') # Return an empty list if there's an error or the file doesn't exist

