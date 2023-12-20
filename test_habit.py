import unittest
from datetime import datetime
from habit import Habit


class TestHabit(unittest.TestCase):

    def test_habit_creation(self):
        # Prueba para crear un objeto Habit
        habit = Habit(habit_name="Test Habit", period=Habit.PeriodicityType.DAILY,
                      date_of_creation=datetime.now(), habit_broken=False,
                      completeness_array=[])

        # Asegúrate de que el objeto Habit se haya creado correctamente
        self.assertEqual(habit.get_habit_name(), "Test Habit")
        self.assertEqual(habit.get_period(), Habit.PeriodicityType.DAILY)
        self.assertFalse(habit.is_habit_broken())
        self.assertEqual(habit.get_completeness_array(), [])