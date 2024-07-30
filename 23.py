import random
start_program = input('welcome to ultimate four studants apresentation ordinator, want to start? (y/n): ')
if start_program == 'y':
    user_input = input('insert the first student name: ')
    user_input2 = input('insert the second student name: ')
    user_input3 = input('insert the tird student name: ')
    user_input4 = input('insert the fourth student name: ')
    collection = [user_input, user_input2, user_input3, user_input4]
    print('the order for the students is {}'.format(random.sample(collection, k=4)))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')





