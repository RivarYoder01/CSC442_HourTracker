"""
main

    print welcome

    print menu
        enter hours ---> calcHours
        end week ---> endWeek
        see report ---> seeReport
        clear report ---> clearReport
        exit ---> sys.exit(0)

calcHours
    user enters start time
    user enters end time

    calculate hours worked

    format hours worked and total time
    return to menu

endWeek
    save report to .txt file
    give user total hours worked
    return to menu

seeReport
    read report from .txt file
    print report to user
    reutrn to menu

clearReport
    delete report file



TESTER

entering correct hours
entering incorrect hours (produces negative hours)
entering hours and ending week
ending week without hours
clearing report
clearing report with no hours

"""