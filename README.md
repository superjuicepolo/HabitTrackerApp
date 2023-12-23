Habit Tracking Application
Overview

The Habit Tracking Application is a user-friendly tool designed to help individuals monitor and manage their habits effectively. Whether you aim to develop daily routines or wish to track weekly tasks, this application offers a seamless experience to keep you on track.

Features Core Functionalities:

    Habit Creation: Users can effortlessly create habits by specifying essential details like the habit name, its periodicity (daily, weekly, monthly, yearly), and the date of inception.
    Progress Monitoring: Once a habit is added, users can mark their completion, helping in visualizing progress over time.
    Streak Analysis: Gain insights into your habits' consistency with streak tracking. Identify your longest streaks and understand patterns to improve consistency.
    Periodicity Analytics: The application offers analytics based on habit periodicity. Users can easily identify habits that share similar frequencies, aiding in better time management.

Additional Features:

    Data Persistence: The application ensures data integrity by allowing users to save their habits to a file and load them as required.
    User-Friendly Interface: With a straightforward menu-driven interface, users can navigate through functionalities effortlessly.

Directory Structure

    habit.py: Contains the core Habit class definition and related methods.
    habits_app_functions.py: Houses functions that manage user interactions and core application functionalities.
    database.py: Implements functionality to save and retrieve habit data using the pickle module.

How to Use

    Creating a New Habit: Launch the application and select the option to create a new habit. Provide the necessary details like habit name, periodicity, and date of creation.
    Managing Habits: Use the options available in the main menu to manage habits. Options include completing habits, editing them, deleting them, and more.
    Analytics: Utilize the analytics features to get insights into habits, streaks, and periodicities.

Testing

The application includes unit tests to ensure the validity and reliability of the habit tracking components. You can run these tests using unittest to verify the functionalities and ensure everything works as expected.

Technologies Used

    Programming Language: Python
    Libraries and Modules:
        datetime: For efficient date and time operations.
        pickle: For serialization and deserialization of Python objects.

About the Author

This application is a testament to the dedication and passion of Ander Rivera Tampanariu, who envisioned a tool that would empower individuals to cultivate positive habits and lead fulfilling lives.

