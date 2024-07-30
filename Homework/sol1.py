import func_without_return

#a#
print(" a ".center(30, "#"))
(help(func_without_return.my_ascending))
func_without_return.my_ascending(-12, 7)
print()

#b#
print(" b ".center(30, "#"))
(help(func_without_return.my_details))
func_without_return.my_details("AI is the best")
print()

#c#
(help(func_without_return.say_bool))
print(" c ".center(30, "#"))
func_without_return.say_bool(True)
func_without_return.say_bool(False)
print()

#d#
(help(func_without_return.print_zugi))
print(" d ".center(30, "#"))
func_without_return.print_zugi([5,3,2,10,15,14,14])
print()

#e#
(help(func_without_return.my_statistics))
print(" e ".center(30, "#"))
grade: int = None
grades_list: list = []
while grade != -99:
    grade: int = int (input("Please enter your grade"))
    if grade < 0 or grade > 100:
        continue
    else:
        grades_list.append(grade)
func_without_return.my_statistics(grades_list)


#f#
print(" e ".center(30, "#"))
(help(func_without_return.my_ascending))
(help(func_without_return.my_details))
(help(func_without_return.say_bool))
(help(func_without_return.print_zugi))
(help(func_without_return.my_statistics))

