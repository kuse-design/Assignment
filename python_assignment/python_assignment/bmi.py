weight = float(input("Enter weight(kg) : "))
height = float(input("Enter height : "))

bmi = weight/(height*height)
print("your body mass index(bmi) is : ", bmi )

if(bmi < 18.5 ):
    print("you are underweight")

elif(bmi >= 18.5 and bmi <= 24.9 ):
    print("you are normal")

elif(bmi >= 25 and bmi <= 29.9):
    print("you are overweight")

elif(bmi > 30):
    print("you are obese")
