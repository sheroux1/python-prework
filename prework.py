# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is theinput of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Take user_name as a value and says hello."""
    print("hello_" + user_name + "!") # The '_' formatting seems odd, but it was in the prompt
# If USERNAME is supposed to be all caps, this print value would read ("hello_" + user_name.upper() + "!") instead

# Question 2:
# Write a python function, first_odds that prints the odd number from 1-100 and returns nothing

def first_odds():
    """Prints all odd numbers from 1-100."""
    number = 1
    while number <100:
        if number % 2 == 1:
            print(number)
        number += 1


# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Takes a list as input and returns the highest number in that list."""
    a_list.sort()
    return a_list[-1]


# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4,
#  but not divisible by 100, unless it is also divisible by 400. 
#  The return should be a boolean Type (True/false).

def is_leap_year(a_year):
    """Check is a_year is a leap year as defined by: IS divisible by 4, NOT divisible by 100 UNLESS ALSO divisible by 400."""
    """Returns Boolean True/False"""
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 4 == 00 and a_year % 100 == 0 and a_year % 400 == 0:
        return True
    else: 
        return False


# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be a boolean Type.

def is_consecutive(a_list):
    """Takes a list of integers and loops through to see if they are consecutive."""
    cons_bool = bool()
    comparison_list = a_list[1:] # Copy a_list starting at the second index for comparison
    last_number = a_list[0] # so we can iterate through two lists at once while only using one list in the loop
    for current_number in comparison_list:
        if current_number-1 == last_number: # Bulk of the work, checks to see if they incremented or not. 
            cons_bool = True
            last_number += 1
            continue
        elif current_number == last_number: # Checks to see if two numbers in sequence are the same, eg 1,2,3,3, returns False
            cons_bool = False
            break
        else:
            cons_bool = False
            break
    return cons_bool
