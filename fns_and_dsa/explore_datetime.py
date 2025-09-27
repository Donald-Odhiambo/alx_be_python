# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.now()  # save current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """Calculate the future date after adding given days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # save future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
