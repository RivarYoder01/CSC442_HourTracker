"""
Runs 7 unit tests by passing a list of menu inputs and start and end times to the main function from hourTrackerTester.py.
Verifies the output against the hours worked in the expected output.

tests include:
- Correct Hours
- Incorrect Format
- Negative Hours
- End Week WITH Hours
- End Week WITHOUT Hours
- See Report
- Clearing Report
"""

import unittest
from hourTrackerTester import main

# SOURCE: silly robot simulator

class HourTrackerTest(unittest.TestCase):

    def test_correct_hours(self):
        print(f"\t\033[1mCorrect Hours\033[0m")  # Correct Hours

        menu_input = ['1', '0'] # Enter hours worked, exit
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:00:00"
        expected_hours = [8.0]

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_incorrect_format(self):
        print(f"\t\033[1mIncorrect Hours\033[0m")  # Incorrect Hours

        menu_input = ['1', '0'] # Enter hours worked, exit
        start_time = "08-03-2025 09:00:00"
        end_time = "2025-08-03 17:00:00"
        expected_hours = []

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_negative_hours(self):
        print(f"\t\033[1mNegative Hours\033[0m")  # Negative Hours

        menu_input = ['1', '0'] # Enter hours worked, exit
        start_time = "2025-08-03 17:00:00"
        end_time = "2025-08-03 09:00:00"
        expected_hours = []

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_ending_week_with_hours(self):
        print(f"\t\033[1mEnd Week WITH Hours\033[0m")  # End Week WITH Hours

        menu_input = ['1', '1', '1', '2', '0'] # Enter hours worked three times, end week, exit
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:30:00"
        expected_hours = []

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_ending_week_without_hours(self):
        print(f"\t\033[1mEnd Week WITHOUT Hours\033[0m")  # End Week WITHOUT Hours

        menu_input = ['2', '0'] # End week, exit
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:30:00"
        expected_hours = []

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_see_report(self):
        print(f"\t\033[1mSee Report\033[0m")    # See Report

        menu_input = ['1', '1', '1', '3', '0'] # Enter hours worked three times, see report, exit
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:30:00"
        expected_hours = [8.5, 8.5, 8.5]

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)

    def test_clearing_report(self):
        print(f"\t\033[1mClearing Report\033[0m")  # Clearing Report WITH ended week

        menu_input = ['1', '2', '9', '0'] # Enter hours worked, end week, clear report, exit
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:30:00"
        expected_hours = []

        output = main(menu_input, start_time, end_time)

        self.assertEqual(output, expected_hours)