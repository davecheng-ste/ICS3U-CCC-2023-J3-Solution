"""
File: best_day.py
Author: Dave Cheng
Date: 2024-05-10
Description: A program that finds the day(s) with the maximum number of 
             people available to attend an event.
"""


def find_best_day(n, availability):
    """
    Finds the day(s) with the maximum number of people available to attend an event.

    Parameters:
        n (int): The number of people attending the event.
        availability (list): A list of strings representing the availability of 
                             each person. Each string in the list should consist
                             of characters indicating the availability for each
                             of the five days, "Y" meaning available, and "."
                             meaning not available.
    
    Returns:
        list: A list containing the day number(s) with the maximum number of
              available people.
    """

    # Initialize local variables to track best day(s)
    max_count = 0
    best_days = []  # Use list to keep track of available day(s)

    # Iterate through each day 1 through 5
    for day in range(5):
        count = 0
        # Count the number of people available on this day
        for person in availability:
            if person[day] == "Y":
                count += 1
        # Update best_days if current day has more availble people
        if count > max_count:
            max_count = count
            best_days = [day + 1]
        # If equal to max_count, append the day to best_days
        elif count == max_count:
            best_days.append(day + 1)

    return best_days


# Get input of people interested
people = int(input())

# Initialize list to store each person's availability
availability = []

# For each person interested, get availability string and add to list
for _ in range(people):
    availability.append(input().strip())

# Call function to find best day(s)
best_days = find_best_day(people, availability)

# Output the result -  Iterate over list of best_days
for i in range(len(best_days)):
    # Handle multiple days in list, separate with comma
    if i != len(best_days) - 1:
        print(best_days[i], end=",")
    else:
        # Last or only item in list
        print(best_days[i])
