#crie um programa que leia um nome e mostre o mesmo em letras maiusculas,minusculas,
#eu numero de letras(sem espacos) e qunatas letras tem o primeiro nome

full_name = input('insert a name: ')
print('the name in uppers is: {}'.format(full_name.upper()))
print('the name in lowers is: {} '.format(full_name.lower()))
full_name = full_name.split()
full_name_without = ''.join(full_name)
print('the number of letters in the name is: {}'.format(len(full_name_without)))
first_name = full_name[0]
print('the number of letters in the first name is {}'.format(len(first_name)))


