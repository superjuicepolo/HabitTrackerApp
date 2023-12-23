from habits_app_functions import *
from database import *

# Sample habit objects
habit1 = Habit(
    habit_name="Waking up early",
    period= Habit.PeriodicityType.DAILY,
    habit_broken=False,
    date_of_creation=datetime.now(),
    completeness_array = [False, True, True, True, False, True, False, True, True, True, True, True, False, True, True,
                          False, True, True, False, True, False, True, True, True, False, False, True, False, False])


habit2 = Habit(
    habit_name= "Meditation",
    period= Habit.PeriodicityType.DAILY,
    habit_broken= False,
    date_of_creation=datetime.now(),
    completeness_array=[True, True, True, False, False, True, False, True, True, False, True, True, False, True, True,
                          False, True, True, True, True, False, True, True, True, False, False, True, True, False])

habit3 = Habit(
    habit_name= "Learning German",
    period= Habit.PeriodicityType.WEEKLY,
    habit_broken= False,
    date_of_creation=datetime.now(),
    completeness_array=[ True, True, False, True])

habit4 = Habit(
    habit_name= "Eating healthy meal",
    period= Habit.PeriodicityType.DAILY,
    habit_broken= False,
    date_of_creation=datetime.now(),
    completeness_array=[True, True, True, True, True, False, True, True, False, False, True, True, True, True, True,
                        False, True, False, True, True, True, False, True, True, False, True, False, True, True])

habit5 = Habit(
    habit_name= "Doing exercise",
    period= Habit.PeriodicityType.WEEKLY,
    habit_broken = False,
    date_of_creation = datetime.now(),
    completeness_array=[True, True, False, True])




if __name__ == '__main__':

    list_of_habits = [habit1, habit2, habit3, habit4, habit5]
    while True:
        try:
            # Displaying the main menu for user interaction
            main_option = input("""
Enter 1 if you want to print the list of habits
Enter 2 if you want to choose existing habit
Enter 3 if you want to add habit
Enter 4 if you want to delete habit
Enter 5 if you want to show streaks of all habits
Enter 6 if you want to get the longest streak of all habits
Enter 7 if you want to get the list of habits with same periodicity
Enter 8 if you want to edit habit
Enter 9 if you want to quit the program
Enter 10 if you want to save
Enter 11 if you want to load habits

option: """)

            if main_option == "2":
                # User selects an existing habit to work with
                habit_with_which_we_are_working = choose_habit_in_list_of_habits(list_of_habits)
                # Display the completeness array of the selected habit
                work_with_habit(habit=habit_with_which_we_are_working)

            elif main_option == "3":
                # User chooses to add a new habit
                new_habit = create_new_habit()  # Create a new habit using the create_new_habit function
                list_of_habits.append(new_habit)  # Add the new habit to the list_of_habits
                print("New habit added")

            elif main_option == "4":
                # User chooses to remove a habit
                index_of_habit = choose_number_and_remove_one("Choose index of habit to remove: ")
                list_of_habits.pop(index_of_habit)  # Remove the habit at the specified index from the list_of_habits

            elif main_option == "1":
                print_habits(list_of_habits)

            elif main_option == "5":
                print_streak_for_all_habits_in_list(list_of_habits)

            elif main_option == "6":
                get_longest_streak(list_of_habits)

            elif main_option == "7":
                print_habits_with_same_periodicity_in_list(list_of_habits)

            elif main_option == "8":
                # User chooses to edit a habit
                index_of_habit = choose_number_and_remove_one("Choose index of habit to edit: ")

                if 0 <= index_of_habit < len(list_of_habits):
                    # Check if the index is valid
                    habit_to_edit = list_of_habits[index_of_habit]

                    edit_habit(habit_to_edit)
                else:
                    print("Invalid index. No habit found")

            elif main_option == "9":
                # User chooses to quit the program
                print("Quitting the program. Goodbye!")
                break  # Exit the loop and end the program

            elif main_option == "10":
                save_habits_to_file(filename=choose_file_name(), habits=list_of_habits)

            elif main_option == "11":
                list_of_habits = load_habits_from_file(filename=choose_file_name())

            # The rest of your code for handling other options

        except Exception as e:
            # Display any exceptions that occur during the program execution
            print(f"Exception: {e}")




