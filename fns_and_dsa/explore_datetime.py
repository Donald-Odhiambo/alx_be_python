# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time"""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """Calculate the future date after adding the specified number of days"""
    future_date = datetime.now() + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()
