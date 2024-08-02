#faca um  codigo que leia um nome de uma pessoa e retorne se ela possui silva no nome

# sourcery skip: simplify-boolean-comparison
name = input('insert a name: ')
checker = 'Silva' in name
if checker == True:
    print('the inserted name has Silva')
else:
    print('the inserted name hasn`t Silva')