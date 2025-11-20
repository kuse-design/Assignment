amount_number = int(input(" Enter your amount: "))
year_number = int(input( "Enter number of year : ")) 
interest_number = int(input( "Enter number of interest : "))
for year_number in range(0, year_number):
   amount_number += (amount_number *(interest_number/100))
   print (f"{year_number +1}  {interest_number} {amount_number}")
 

