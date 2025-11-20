#total =  number_one + number_two
number_one = int(input("Enter first number or 0 to stop : "))
number_two = int(input("Enter second number or 0 to stop : "))
total = 0
while number_one and number_two != 0:
    total += number_one +  number_two 
    total = (input("Do you wish to perform this operation again or 0 to stop : "))
        
 
print(total)
