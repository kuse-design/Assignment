numOne = int(input("Enter first number: "))
numTwo = int(input("Enter second number: "))
numThree = int(input("Enter third number: "))


sum_nums = numOne + numTwo + numThree
product = numOne * numTwo * numThree
average = sum_nums / 3  

print("Your sum is:", sum_nums)
print("Your product is:", product)
print("Your average is:", average)

if numOne > numTwo and numOne > numThree:
    print(numOne, "is the largest")
if numTwo > numOne and numTwo > numThree:
    print(numTwo, "is the largest")
if numThree > numOne and numThree > numTwo:
    print(numThree, "is the largest")


if numOne < numTwo and numOne < numThree:
    print(numOne, "is the smallest")
if numTwo < numOne and numTwo < numThree:
    print(numTwo, "is the smallest")
if numThree < numOne and numThree < numTwo:
    print(numThree, "is the smallest")
