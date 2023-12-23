import unittest
from datetime import datetime
from habit import Habit


class TestHabit(unittest.TestCase):

    def setUp(self):
        # Initialize some habits for testing

        current_date_time = datetime.now()
        self.daily_habit = Habit("Read a book", Habit.PeriodicityType.DAILY,date_of_creation=current_date_time)
        self.weekly_habit = Habit("Go jogging", Habit.PeriodicityType.WEEKLY,date_of_creation=current_date_time)

    def test_habit_creation(self):
        # Check if habit creation works as expected
        self.assertEqual(self.daily_habit.get_habit_name(), "Read a book")
        self.assertEqual(self.daily_habit.get_period(), Habit.PeriodicityType.DAILY)

    def test_set_and_get_habit_name(self):
        # Check setting and getting habit name
        self.daily_habit.set_habit_name("Read a magazine")
        self.assertEqual(self.daily_habit.get_habit_name(), "Read a magazine")

    def test_set_and_get_period(self):
        # Check setting and getting habit period
        self.weekly_habit.set_period(Habit.PeriodicityType.DAILY)
        self.assertEqual(self.weekly_habit.get_period(), Habit.PeriodicityType.DAILY)

    def test_complete_habit(self):
        # Test the complete method
        # Initially, the habit should have an empty completeness array
        self.assertEqual(self.daily_habit.get_completeness_array(), [])

        # After completing, the completeness array should have a True value
        self.daily_habit.complete(datetime.now())
        self.assertEqual(self.daily_habit.get_completeness_array(), [True])

    def test_streak_calculation(self):
        # Test the streak calculation method
        # Assuming the completeness array, after multiple completions, should have streaks
        self.daily_habit.complete(datetime.now())
        self.daily_habit.complete(datetime.now())
        self.daily_habit.complete(datetime.now())

        # As we completed 3 times consecutively, the streak should be 3
        self.assertEqual(self.daily_habit.get_streak(), 3)

    def test_habit_breaking(self):
        # Initially, the habit should not be broken
        self.assertFalse(self.daily_habit.is_habit_broken())

        # Simulate habit breaking
        self.daily_habit.break_habit()

        # After breaking, the habit should be marked as broken
        self.assertTrue(self.daily_habit.is_habit_broken())

    def test_update_timestamp(self):
        # Store the initial last deadline
        initial_last_deadline = self.daily_habit.get_last_deadline()

        # Update the habit's completeness to simulate a completion
        completion_date = datetime.now()
        self.daily_habit.complete(completion_date)

        # Check if the last deadline has been updated
        updated_last_deadline = self.daily_habit.get_last_deadline()
        self.assertNotEqual(initial_last_deadline, updated_last_deadline)


if __name__ == "__main__":
    unittest.main()


