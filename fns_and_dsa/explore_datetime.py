# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """Displays the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()   # get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    """Calculates and displays the future date after adding given days."""
    current_date = datetime.now()   # current date
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main program
if __name__ == "__main__":
    # Show current date and time
    display_current_datetime()

    # Ask user for input
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
