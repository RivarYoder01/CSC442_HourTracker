#!/user.bin.env python3

# Run from tester.py

import datetime

DASH = "||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||"

def clear_report(weekly_hours, hours_reported):
    """
    Clears the weekly_report.txt file and resets the weekly_hours and hours_reported lists.

    :param weekly_hours:
    :param hours_reported:
    :return:
    """
    print(DASH)
    print("||                      CLEAR REPORT                       ||")
    print(DASH)

    try:
        with open("weekly_report.txt", "w") as file:
            file.write("")
    except FileNotFoundError:
        print(f"\tError: The report file does not exist. Please end the week first.")
    except Exception as e:
        print(f"\tAn error occurred while clearing the report: {e}")

    print(f"\tReport cleared successfully.")

    weekly_hours.clear()  # Clear the weekly hours after saving
    hours_reported.clear()  # Clear the reported hours after saving

    return None


def see_report():
    """
    Reads weekly_report.txt and prints the report to the user.
    :return:
    """

    print(DASH)
    print("||                      SEE REPORT                         ||")
    print(DASH)

    try:
        with open("weekly_report.txt", "r") as file:
            report = file.read() # read the report from the file
            if report: # Check if the report is not empty
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
    Adds the total hours from weekly hours and seperates the hours and minutes.
    If no hours were worked, return to menu.
    Opens weekly_report.txt and writes the report to it by looping through the hours_reported list.
    Clears the weekly_hours and hours_reported lists after saving the report.

    :param weekly_hours:
    :param hours_reported:
    :return: total_hours
    """

    print(DASH)
    print("||                      END WEEK                           ||")
    print(DASH)

    total_hours = sum(weekly_hours) # Calculate total hours worked in the week
    hours = int(total_hours) # Pull whole hours
    minutes = int(round((total_hours - hours) * 60)) # Separate remaining minutes

    if total_hours == 0: # No hours, return to menu
        print(f"\tNo hours worked this week.")
        print(f"\tPlease enter hours before ending the week.")
        return None

    try:
        with open("weekly_report.txt", "a") as file:
            file.write(f"Weekly Report\n")
            for report in hours_reported: # loop through report and write to file
                file.write(f"{report}\n")
            file.write(f"Total Time Worked: {hours} hours and {minutes} minutes\n") # writes total time worked
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


def calc_hours(weekly_hours, hours_reported, start_time, end_time):
    """
    Function takes the start and end times and ensures they are in the correct format and would produce a positive
    number when subtracted.
    Exits to menu if either of those conditions are not met.
    Calculates the total hours worked and formats a report.
    The report is stored in hours_reported and the total hours worked is stored in weekly_hours for later.

    SOURCE: https://www.geeksforgeeks.org/python/python-strftime-function/
    SOURCE: https://community.alteryx.com/t5/Alteryx-Designer-Desktop-Discussions/Convert-time-in-decimal-e-g-7-6-hours-to-Time-in-hours-and/td-p/1169193

    :param weekly_hours:
    :param hours_reported:
    :param start_time:
    :param end_time:
    :return: weekly_hours, hours_reported
    """

    print(DASH)
    print("||                      ENTER HOURS                        ||")
    print(DASH)

    correct_format = 0 # tracks if date and time formates are correct

    while correct_format == 0:
        try: # start_time is in the format YYYY-MM-DD HH:MM:SS
            datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            correct_format = 1
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            return None # back to menu
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None # back to menu

    while correct_format == 1:
        try: # end_time is in the format YYYY-MM-DD HH:MM:SS
            datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            correct_format = 2
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            return None # back to menu
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None # back to menu

    try: # convert start_time and end_time to datetime objects
        start = datetime.datetime.strptime(start_time , "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

        if end < start: # ensure end time is not before start time
            print("End time cannot be before start time.")
            return None

        total_time = (end - start).total_seconds() / 3600.0  # Convert seconds to hours
        hours = int(total_time) # store the whole hours
        minutes = int(round((total_time - hours) * 60)) # store the remaining minutes

        print(f"\tTime worked: {hours} hours, {minutes} minutes")

        report = f"Start: {start_time}, End: {end_time}, Hours Worked: {hours}, Minutes Worked: {minutes}"
        hours_reported.append(report) # add the report to hours_reported
        weekly_hours.append(total_time) # add the total time to weekly_hours

    except Exception as e:
        print(f"An error occurred while calculating hours: {e}")

    return weekly_hours, hours_reported


def main(menu_input, start_time, end_time):
    """
    Main takes in a list of menu inputs and start and end times.
    A for loop goes through the menu options.
    Passes start and end times into the calc_hours function.

    A while loop runs until '0' is passed through where it will return to the tester

    1. Enter Hours Worked
    2. End Week
    3. See Report
    9. Clear Report
    0. Exit

    :param menu_input:
    :param start_time:
    :param end_time:
    :return: weekly_hours
    """

    hours_reported = []
    weekly_hours = []
    run = True

    while run:
        for menu_choice in menu_input:
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


            if menu_choice == '1':
                calc_hours(weekly_hours, hours_reported, start_time, end_time)
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
                print()
                print()
                run = False
            else:
                print(f"\tInvalid choice. Please select a valid option (1-5).")

    return weekly_hours


if __name__ == "__main__":
    main(menu_input, start_time, end_time)