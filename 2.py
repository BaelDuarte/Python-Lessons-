#make a program that sums two numbers
# sourcery skip: use-fstring-for-concatenation
first_number = int(input('enter the fist number: '))
second_number = int(input('enter the second number: '))
total = first_number + second_number
print("The sum result is " + str(total) + "!")
