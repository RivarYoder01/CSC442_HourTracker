# import unittest
import datetime
import sys

DASH = "||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||"

"""
class HourTrackerTest(unittest.TestCase):

    def test_correct_hours(self):
        print(f"\t\033[1mCorrect Hours\033[0m") # Correct Hours

        menu_input = '1'
        start_time = "2025-08-03 09:00:00"
        end_time = "2025-08-03 17:00:00"
        expected_hours = 8.0
        
        output = main([menu_input, start_time, end_time]) 
        
        self.assertEqual(output, expected_hours)
"""

def clear_report(weekly_hours, hours_reported):
    print(DASH)
    print("||                      CLEAR REPORT                       ||")
    print(DASH)

    try:
        with open("weekly_report.txt", "w") as file:
            file.write("")
        print(f"\tReport cleared successfully.")

        weekly_hours.clear() # Clear the weekly hours after saving
        hours_reported.clear()  # Clear the reported hours after saving
    except FileNotFoundError:
        print(f"\tError: The report file does not exist. Please end the week first.")
    except Exception as e:
        print(f"\tAn error occurred while clearing the report: {e}")

    return None


def see_report():
    print(DASH)
    print("||                      SEE REPORT                         ||")
    print(DASH)

    try:
        with open("weekly_report.txt", "r") as file:
            report = file.read()
            if report:
                print(report)
            else:
                print(f"\tNo report available. Please enter hours worked first.")
    except FileNotFoundError:
        print(f"\tError: The report file does not exist. Please end the week first.")
    except Exception as e:
        print(f"\tAn error occurred while reading the report: {e}")

    return None


def end_week(weekly_hours, hours_reported):
    """
    Saves the weekly hours and reported hours to a file and returns the total hours worked.

    :param weekly_hours: List of hours worked each day
    :param hours_reported: List of formatted reports for each day
    :return: Total hours worked
    """

    print(DASH)
    print("||                      END WEEK                           ||")
    print(DASH)

    total_hours = sum(weekly_hours)
    hours = int(total_hours)
    minutes = int(round((total_hours - hours) * 60))

    try:
        with open("weekly_report.txt", "a") as file:
            file.write(f"Weekly Report\n")
            for report in hours_reported:
                file.write(f"{report}\n")
            file.write(f"Total Time Worked: {hours} hours and {minutes} minutes\n")
            file.write("\n")

        weekly_hours.clear() # Clear the weekly hours after saving
        hours_reported.clear()  # Clear the reported hours after saving

        print(f"\tTotal Time Worked: {hours} hours and {minutes} minutes")
        print(f"\tWeekly report saved to 'weekly_report.txt'.")
    except FileNotFoundError:
        print(f"\tError: The file could not be found. Please check the file path.")
    except Exception as e:
        print(f"\tAn error occurred while saving the report: {e}")

    return total_hours


def calc_hours(weekly_hours, hours_reported):
    """
    https://www.geeksforgeeks.org/python/python-strftime-function/
    https://community.alteryx.com/t5/Alteryx-Designer-Desktop-Discussions/Convert-time-in-decimal-e-g-7-6-hours-to-Time-in-hours-and/td-p/1169193
    :return:
    """

    print(DASH)
    print("||                      ENTER HOURS                        ||")
    print(DASH)

    correct_format = 0
    start_time = "1970-01-01 00:00:00"  # Default start time
    end_time = "1970-01-01 10:10:00"

    """
    while correct_format == 0:
        start_time = input(f"Enter \033[1mstart\033[0m time (YYYY-MM-DD HH:MM:SS): ")

        try:
            datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            correct_format = 1
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    while correct_format == 1:
        end_time = input("Enter \033[1mend\033[0m time (YYYY-MM-DD HH:MM:SS): ")

        try:
            datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            correct_format = 2
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    """

    try:
        start = datetime.datetime.strptime(start_time , "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

        if end < start:
            print("End time cannot be before start time.")
            return None

        total_time = (end - start).total_seconds() / 3600.0  # Convert seconds to hours
        hours = int(total_time)
        minutes = int(round((total_time - hours) * 60))

        print(f"\tTime worked: {hours} hours, {minutes} minutes")

        report = f"Start: {start_time}, End: {end_time}, Hours Worked: {hours}, Minutes Worked: {minutes}"
        hours_reported.append(report)
        weekly_hours.append(total_time)

    except Exception as e:
        print(f"An error occurred while calculating hours: {e}")

    return weekly_hours, hours_reported


def main():

    hours_reported = []
    weekly_hours = []
    run = True

    while run:
        print(DASH)
        print("||                      TRACKLY                            ||")
        print(DASH)

        print("|| 1. Enter Hours Worked                                   ||")
        print("|| 2. End Week                                             ||")
        print("|| 3. See Report                                           ||")
        print (DASH)
        print("|| 9. Clear Report                                         ||")
        print("|| 0. Exit                                                 ||")
        print(DASH)

        menu_choice = input(f"\tChoose an option (1-5): ")

        if menu_choice == '1':
            calc_hours(weekly_hours, hours_reported)
        elif menu_choice == '2':
            end_week(weekly_hours, hours_reported)
        elif menu_choice == '3':
            see_report()
        elif menu_choice == '9':
            clear_report(weekly_hours, hours_reported)
        elif menu_choice == '0':
            print(DASH)
            print(f"\tExiting the Hour Tracker. Goodbye!")
            print(DASH)
            run = False
        else:
            print(f"\tInvalid choice. Please select a valid option (1-5).")

    sys.exit(0)


if __name__ == "__main__":
    main()