scoreOne = float(input("Enter first score: "))
scoreTwo = float(input("Enter second score: "))
scoreThree = float(input("Enter third score: "))

sum_scores = scoreOne + scoreTwo + scoreThree
average = sum_scores / 3

print("Average is:", average)

if 90 <= average <= 100:
    print("Grade is A")
elif average >= 80:
    print("Grade is B")
elif average >= 70:
    print("Grade is C")
elif average >= 60:
    print("Grade is D")
else:
    print("Grade is F")
