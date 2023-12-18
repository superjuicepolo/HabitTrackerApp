from datetime import datetime
from typing import List
from habit import Habit

def input_period() -> Habit.PeriodicityType:
    period_option = input("Choose daily(1), weekly(2), monthly(3) or yearly(4) to define time span:")
    # Initialize period with a default value in case the input is not as expected
    period = None
    if period_option == "1":
        print("Daily habit")
        period = Habit.PeriodicityType.DAILY
    elif period_option == "2":
        print("Weekly habit")
        period = Habit.PeriodicityType.WEEKLY
    elif period_option == "3":
        print("Monthly habit")
        period = Habit.PeriodicityType.MONTHLY
    elif period_option == "4":
        print("Yearly habit")
        period = Habit.PeriodicityType.YEARLY
    return period


def create_new_habit():
    # Create a new habit based on user input.
    print("To create habit,write habit name:")
    habit_name = input()
    period = input_period()
    habit_broken = False
    print("Input the date and time in which the habit was created:")
    date_of_creation = datetime(year=int(input("year: ")), month=int(input("month: ")), day=int(input("day: ")), hour=int(input("hour: ")))
    completeness_array = []

    # Create a new Habit object with the provided details
    habit = Habit(
        habit_name=habit_name,
        period= period,
        habit_broken=habit_broken,
        date_of_creation=date_of_creation,
        completeness_array=completeness_array
    )
    return habit

def choose_habit_in_list_of_habits(list_of_habits: List[Habit]):
    index_of_habit = input("""Choose index habit in list_of_habits: """)
    habit_with_which_we_are_working = list_of_habits[int(index_of_habit) - 1]
    return habit_with_which_we_are_working

def work_with_habit(habit: Habit):
    print(f"history of our habit array is: {habit.get_completeness_array()}")
    option_of_user = input("""
    Enter 1 if you want to complete habit
    Enter 2 if you want to get streak habit

    option: """)
    print(f"user option: {option_of_user}")
    if option_of_user == "1":
        # User chooses to complete the habit
        completion_date = datetime.now()
        habit.complete(completion_date)
    elif option_of_user == "2":
        # User chooses to get the streak of the habit
        our_streak = habit.get_streak()
        print(f"our_streak: {our_streak}\n")


def print_habits(list_of_habits: List[Habit]):
    # User chooses to print the list of habits
    for index, habit_in_list in enumerate(list_of_habits):
        print(f"habit{index + 1}: {habit_in_list}")

    # Way 2:
    #print("\n".join(map(lambda x: f"habit{x[0] + 1}: {x[1]}", enumerate(list_of_habits))))

def get_longest_streak(list_of_habits: List[Habit]):
    # User chooses to get the longest streak among all habits
    longest_streak = 0
    for index, habit_in_list in enumerate(list_of_habits):
        streak = habit_in_list.get_streak()
        print(f"streak of habit{index + 1}: {streak}")
        longest_streak = max(longest_streak, streak)
    print(f"The longest streak among all habits is: {longest_streak}")

def print_streak_for_all_habits_in_list(list_of_habits: List[Habit]):
    # User chooses to show streaks of all habits
    for index, habit_in_list in enumerate(list_of_habits):
        print(f"streak of habit{index + 1}: {habit_in_list.get_streak()}")

def print_habits_with_same_periodicity_in_list(list_of_habits: List[Habit]):
    # User chooses to get the list of habits with the same periodicity
    target_periodicity = input("Enter the periodicity (daily/weekly/monthly/yearly): ").strip().lower()
    habits_with_same_periodicity = [habit for habit in list_of_habits if
                                    habit.get_period() == Habit.PeriodicityType[target_periodicity.upper()]]

    print(f"Target periodicity: {target_periodicity}")
    print(f"Habits with {target_periodicity} periodicity:")

    if habits_with_same_periodicity:
        # If habits with the specified periodicity are found, print them
        for index, habit in enumerate(habits_with_same_periodicity):
            print(f"Habit {index + 1} - Name: {habit.get_habit_name()}, Period: {habit.period.value}")
    else:
        print(f"No habits found with {target_periodicity} periodicity")


def edit_habit(habit: Habit):
    print(f"Editing habit: {habit}")

    edit_option = input("""
Enter 1 to edit habit name
Enter 2 to edit period
Enter 3 to edit time
Enter 4 to go back to the main menu

Option: """)

    if edit_option == "1":
        # User chooses to edit the habit name
        new_name = input("Enter new habit name:")
        habit.set_habit_name(name=new_name)
        print("Habit name updated.")
    elif edit_option == "2":
        # User chooses to edit the period
        new_period = input("Enter new period (daily/weekly): ")
        habit.set_period(new_period)
        print("Period updated")
    elif edit_option == "3":
        # User chooses to edit the time span
        new_time_span = int(input("Enter new time span (in minutes): "))
        habit.time_span = new_time_span
        print("Time span updated. ")
    elif edit_option == "4":
        pass  # Go back to the main menu
    else:
        print("Invalid option. Pleas try again.")


def choose_number_and_remove_one(str_var: str) -> int:
    return int(input(str_var)) - 1


def choose_file_name():
    default_habit_file_path = "../../Downloads/habits.pkl"
    file_path = input("Enter file name without extention(write 'd' if want to use default one): ")
    return default_habit_file_path if file_path == "d" else file_path + ".pkl"