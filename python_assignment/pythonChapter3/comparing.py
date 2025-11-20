print(' Enter two integers, and i will tell you the rekationship yhey satisfy : ')

number_one = int(input('Enter a integer : '))
number_two = int(input('Enter a integer : '))


if number_one == number_two:
    print(number_one, 'is equal to', number_two)
else:
    print(number_one, 'is not equals to', number_two)

if number_one < number_two:
    print(number_one, 'is less than', number_two)
else:
    print(number_one, 'is greater than', number_two)

if number_one <= number_two:
    print(number_one, 'is less than or equals to' , number_two)
else: 
    print(number_one, 'is greater than or equals to', number_two)
