# DateTime:

# Create a Python script that displays the current date and time.
# Write a function that takes two dates as input and calculates the difference in days between them.
# Implement a program that converts a given timestamp to a human-readable date and time format.

from datetime import datetime, timedelta

# Task 1: Display the current date and time
def display_current_datetime():
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime)

# Task 2: Calculate the difference in days between two dates
def calculate_date_difference(date1, date2):
    # Assuming date1 and date2 are in the format 'YYYY-MM-DD'
    date_format = "%Y-%m-%d"
    
    # Convert string dates to datetime objects
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    
    # Calculate the difference in days
    difference = abs((datetime2 - datetime1).days)
    return difference

# Task 3: Convert timestamp to human-readable date and time
def convert_timestamp(timestamp):
    # Assuming the timestamp is in seconds
    # Convert timestamp to datetime object
    datetime_object = datetime.fromtimestamp(timestamp)
    
    # Format the datetime object for human-readable output
    formatted_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

# Test the functions
if __name__ == "__main__":
    # Task 1
    print("Task 1:")
    display_current_datetime()
    print("\n")

    # Task 2
    print("Task 2:")
    date1 = "2022-01-01"
    date2 = "2022-02-15"
    difference_days = calculate_date_difference(date1, date2)
    print(f"Days between {date1} and {date2}: {difference_days} days")
    print("\n")

    # Task 3
    print("Task 3:")
    timestamp = 1644081023  # Replace with your timestamp
    human_readable_datetime = convert_timestamp(timestamp)
    print(f"Timestamp {timestamp} in human-readable format: {human_readable_datetime}")

# In this script:

# Task 1 uses datetime.now() to get the current date and time.
# Task 2 defines calculate_date_difference function that takes two date strings, converts them to datetime objects, and calculates the absolute difference in days.
# Task 3 defines convert_timestamp function that takes a timestamp (assumed to be in seconds) and converts it to a human-readable date and time format using datetime.fromtimestamp() and strftime.