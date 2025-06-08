from datetime import datetime, timedelta

def display_current_datetime():
    date = datetime.now()
    print("Current date and time:", date.strftime("%Y-%m-%d %H:%M:%S"))
    return date

def calculate_future_date(current_date, number_of_days):
    future_date = current_date + timedelta(days=number_of_days)
    return future_date

current_date = display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = calculate_future_date(current_date, number_of_days)
print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

