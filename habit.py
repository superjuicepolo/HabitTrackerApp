from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List


class Habit:
    """
    Class representing a habit with properties like name, periodicity, and completion status.
    """

    class PeriodicityType(Enum):
        """
        Enumeration for different periodicities of habits.
        """
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"
        YEARLY = "yearly"

    def __init__(self,
                 habit_name: str,
                 period: PeriodicityType,
                 date_of_creation: datetime,
                 habit_broken: Optional[bool]=None,
                 completeness_array: Optional[List[bool]]=None
                 ):
        """ Initialize a Habit object.

                Parameters:
                - habit_name (str): The name of the habit.
                - period (PeriodicityType): The periodicity of the habit.
                - date_of_creation (datetime): The date and time when the habit was created.
                - habit_broken: (optional) The status of whether the habit is broken or not.
                - completeness_array (list): (optional) An array to store the completion status of the habit.

                The method calculates the initial last_deadline using the next_deadline method.
        """

        self.__habit_name = habit_name
        self.__period = period
        self.__habit_broken = habit_broken
        self.__date_of_creation = date_of_creation
        self.__completeness_array = completeness_array if completeness_array is not None else []
        self.__last_deadline = self.next_deadline(date_of_creation)


    def complete(self, completion_date: datetime):
        """ Mark the habit as complete up to the specified completion date.

         Parameters:
            - completion_date (datetime): The date up to which the habit is considered complete.
        """

        #Iterate through deadlines until the completion date is reached
        current_deadline = self.__last_deadline
        while True:
            next_deadline=self.next_deadline(current_deadline)

            # Check if the current deadline is greater than or equal to the completion date
            if current_deadline>= completion_date:
                # Update the last_deadline to the next one
                self.__last_deadline = next_deadline

                # Mark the habit as complete
                self.__completeness_array.append(True)

                # Update the habit_broken if its undefined
                if self.__habit_broken is None:
                    self.update_is_habit_broken()

                # Exit the loop
                break
            else:
                # Append False for each iteration until the completion date is reached
                self.__completeness_array.append(False)
            current_deadline = next_deadline

    def update_is_habit_broken(self):
        """ Update the habit_broken attribute based on the first element of completeness_array.

        if len(self.__completeness_array) < 1:
            return
        self.__habit_broken = not self.__completeness_array[0]
        """

    def is_habit_broken(self) -> bool:
        """
        Check if the habit is considered broken based on its completeness array.
        Returns:
            bool: True if the habit is broken, False otherwise.
        """
        # Consider a habit broken if its first completeness entry is False (indicating failure).
        return self.__completeness_array and not self.__completeness_array[0]

    def next_deadline(self,date):

        """ Calculate the next deadline based on the habits periodicity.

         Parameters:
         - date (datetime): The current deadline

         Returns:
        - datetime or None: The next deadline or None if the periodicity is not recognized.
        """

        if self.__period == Habit.PeriodicityType.DAILY:
            # If the habit is daily, add one day to the current deadline
            return date + timedelta(days=1)
        if self.__period == Habit.PeriodicityType.WEEKLY:
            # If the habit is weekly, add one week to the current deadline
            return  date + timedelta(weeks=1)
        if self.__period == Habit.PeriodicityType.MONTHLY:
            # If the habit is monthly, add approximately 30 days to the current deadline
            return  date + timedelta (days=30)
        if self.__period == Habit.PeriodicityType.YEARLY:
            # If the habit is yearly, replace the year with the next one
            return date.replace(year=date.year+1)
        else:
            # If the periodicity is not recognized, return None
            return None



    def get_streak(self):
        """ Calculate the longest streak of consecutive completions for the habit.
        Returns:
        int: The length of the longest streak of consecutive completions.
        """
        counter = 0
        longest_streak = 0
        for x in self.__completeness_array:
            if x == True:
                counter = counter + 1
            elif x == False:
                longest_streak = max(counter, longest_streak)
                counter = 0

        # Update longest streak considering the last streak at the end of the array.
        longest_streak = max(counter, longest_streak)
        return longest_streak

    def set_habit_name(self, name: str):
        if type(name) == str:

            """
            Set a new name for the habit.

            Parameters:
            - name (str): The new name for the habit.
            """

            self.__habit_name = name

    def get_habit_name(self) -> str:
        """
        Retrieve the current name of the habit.

        Returns:
        - str: The name of the habit.
        """
        return self.__habit_name

    def set_period(self, time_span):
        """ Set a new time span (period) for the habit."""
        self.__period = time_span

    def get_period(self):
        """ Retrieve the current time span (period) of the habit."""
        return self.__period


    def get_date_of_creation(self):
        """ Retrieve the date and time when the habit was created."""
        return self._date_of_creation


    def set_date_of_creation(self, date):
        """ Set a new date and time for the habit's creation."""
        self._date_of_creation = date

    def break_habit(self):
        """Method to mark the habit as broken."""
        self.habit_broken = True

    def get_completeness_array(self):
        """ Retrieve the completeness array of the habit."""
        return self._completeness_array


    def set_completeness_array(self, array):
        """ Set a new completeness array for the habit."""
        self._completeness_array = array


    def get_last_deadline(self):
        """ Retrieve the last deadline of the habit."""
        return self._last_deadline


    def set_last_deadline(self, deadline):
        """ Set a new last deadline for the habit."""
        self._last_deadline = deadline

    def __str__(self):
        """
        Return a string representation of the Habit.

        Returns:
        - str: String representation of the Habit object.
        """

        return f"Habit Information:\n" \
               f"Name: {self.__habit_name}\n" \
               f"Period: {self.__period}\n" \
               f"Date of Creation: {self.__date_of_creation}\n" \
               f"Habit Broken: {self.__habit_broken}\n" \
               f"Completeness Array: {self.__completeness_array}\n" \
               f"Last Deadline: {self.__last_deadline}"
