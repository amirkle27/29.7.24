#a#
def my_ascending  (a: int = 0, b: int = 0) ->  None:
    """Receives 2 ints and prints the numbers in an ascending order"""

    (print (b, a) if a > b else print (a, b))


#b#
def my_details (a: str) -> None:
    """Receives a string and prints the first, the middle and the last cell"""

    cen = len(a) // 2
    print(f"The first letter of your string is: {a[0]}, the middle letter is {a[cen]} and your last letter is {a[-1]}")


#c#

def say_bool (a: bool = False) -> None:
    """Receives a boolian parameter, then prints "yes" if the parameter is True and "no" if it's False"""

    print("yes" if a == True else "no")



#d#

def print_zugi (numbers: list [int]) -> None:
    """Receives a list of ints and prints "even" for even numbers and "odd" for odd numbers"""

    for i in range (0, len(numbers)):
        if numbers [i] % 2 == 0 :
            print(f"{numbers[i]} is even")
        else:
            print(f"{numbers[i]} is odd")

#e#

import statistics
def my_statistics (grades: list = [int]) -> None:
    if not grades:
        return
    "Receives a list of grades and prints the highest, lowest, number of grades and average."

    above_ninty: list = []
    below_five: list = []
    for i in range (0,len(grades)):
        if grades [i] > 90:
            above_ninty.append(grades[i])
        elif grades [i] < 55:
            below_five.append(grades[i])

    print(f"The highest grade is {max(grades)} \
    \nthe lowest grade is {min(grades)} \
    \nthe average of all the grades is {statistics.mean(grades):.2f} \
    \nYou had {len(above_ninty)} grades above 90! \
    \nAnd {len(below_five)} grades under 55...\
    \nIn total, you had {len(grades)} grades all in all")





