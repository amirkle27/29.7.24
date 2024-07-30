#a#

def my_avg (num: list = []) -> float:

    """Gets 2 int numbers and returns a float average wit 3 digits after the dot."""
    import statistics
    return (f"{statistics.mean(num):.3f}")


#b#

def my_headline (a: str) -> str:
    """Receives a string and returns the same string with uppers and a "!" at the end"""

    return a.upper()+"!"


#c#

def concat_list (a: list = [], b: list = [], c: list = []) -> list:
    """Receives 3 lists and returns one list that contains all lists together"""

    return a+b+c


#d#

#3#

def say_bool (a: bool) -> str:
    """Receives a boolian statement and returnes a string - "yes" for True, "no" for False"""

    if a == True:
        return "Yes"
    else:
        return "No"


#4#

def print_zugi (a: list = [int]) -> list [str]:
    """Receives a list of ints and returns a list of strings - "even" for even numbers, "odd" for odds"""

    ans: list = []
    for i in range (0, len(a)):
        if a[i] % 2 ==0:
            ans.append("Even")
        else:
            ans.append("Odd")
    return ans


#5#


def get_int(massage=str) -> int:
    """Gets an input of a string massage and returns an int that was given by the user"""
    while True:
        try:
            x: int = int(input(f"{massage}"))
            return x
        except Exception:
            pass
