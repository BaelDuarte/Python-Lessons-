import random
start_program = input('welcome to ultimate XX jaguar which student among these four will erase the board: BRUTAL RANDOMIZER, want to start? (y/n): ')
if start_program == 'y':
    print('*explosion sounds*')
    user_input = input('insert the first student name: ')
    user_input2 = input('insert the second student name: ')
    user_input3 = input('insert the tird student name: ')
    user_input4 = input('insert the fourth student name: ')
    collection = [user_input, user_input2, user_input3, user_input4]
    print('*explosion sounds again*')
    print('the choiced studant is {}!!! congratulations!'.format(random.choice(collection)))
    print('*more explosion sounds*')
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')