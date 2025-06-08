from datetime import datetime, timedelta

current_date = datetime.datetime.now()

def display_current_datetime():
    global current_date

    print(f"Current date and time: {current_date.strftime("%Y-%m-%d")} {current_date.strftime("%H:%M:%S")}")


def calculate_future_date():
    global current_date
    global days

    extra_days = datetime.timedelta(days)

    future_date = current_date + extra_days

    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date()

