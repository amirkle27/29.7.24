import func_with_return

#a#
print(" a ".center(30, "#"))
print()

avg1 = (func_with_return.my_avg([90,99]))
print(avg1)

#b#
print(" b ".center(30, "#"))
print()

head1: str = func_with_return.my_headline("python has concurred the world")
for i in range (2):
    print(head1)
    print()

#c#
print(" c ".center(30, "#"))
print()

num1: list = [1,2]
num2: list = [3,4,5,6]
num3: list = [7,8,9]
res_con: list = func_with_return.concat_list(num1,num2,num3)
print(res_con)

#d#
print(" d ".center(30, "#"))
print()

help(func_with_return.my_avg)
help(func_with_return.my_headline)
help(func_with_return.concat_list)


#3#
print(" 3 ".center(30, "!"))
print()

print(func_with_return.say_bool (2==2))
print(func_with_return.say_bool (2>5))


#4#
print(" 4 ".center(30, "!"))
print()

odd_or_even = func_with_return.print_zugi([1,2,3,4,5,6,7,8,9,0,110,101,503,-202,-11])
print(odd_or_even)


#5#
print(" 5 ".center(30, "!"))
print()

print(func_with_return.get_int ("what's your number?"))
