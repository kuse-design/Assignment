total = 0
product = 1
largest = 0
smallest = 0

for number in range(4):
    user_input = int(input( "Enter a number: "))
    total = total + user_input 
    product = product * user_input

    if user_input > largest:
        largest = user_input
    if user_input < smallest:
        smallest = user_input

average = total/4
print( "the total number is :",total)
print( "the product of the numbers is : ", product)
print("the average is : ", average)
print( "the largest number is : ", largest)
print( "the smallest number is : ", smallest)
