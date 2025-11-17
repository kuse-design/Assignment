import java.util.Scanner;
public class Combination{
public static void main (String[]args){

Scanner input = new Scanner(System.in);


System.out.print("Enter first number : ");
int numOne = input.nextInt();


System.out.print("Enter second number : ");
int numTwo = input.nextInt();


System.out.print("Enter third number : ");
int numThree = input.nextInt();

int sum = numOne+numTwo+numThree;
System.out.println ("Your sum is : " + sum);

int product = numOne*numTwo*numThree;
System.out.println ("Your product is : " + product);

int average = sum/3;
System.out.println ("Your average is : " + average);

 if ( numOne > numTwo && numOne > numThree){
System.out.println( numOne + " is the largest " );
}
if( numTwo > numOne && numTwo > numThree){
    System.out.println( numTwo + " is the largest ");
}
if( numThree > numOne && numThree > numTwo){
    System.out.println( numThree + " is largest " );
}

if ( numOne < numTwo && numOne < numThree){
System.out.print( numOne + " is the smallest ");
}
if (numTwo < numOne && numTwo < numThree){
System.out.print( numTwo + " is the smallest ");
}
if ( numThree < numOne && numThree < numTwo){
System.out.println( numThree + " is the smallest ");
}
}
}


