import java.util.Scanner;
public class CalculateAverage{
public static void main(String[]args){

Scanner input = new Scanner(System.in);
System.out.print(" Enter first score: ");
double scoreOne = input.nextDouble();

System.out.print(" Enter Second score: ");
double scoreTwo = input.nextDouble();

System.out.print(" Enter Third score: ");
double scoreThree = input.nextDouble();

double sum = scoreOne + scoreTwo + scoreThree;

double average = sum / 3;

if (average >= 90 && average <= 100){
System.out.println("Score is A");
}

 else if (average >= 80){
System.out.println("print B");
}
else if (average >= 70){
 System.out.println("print C" );
}
else if (average >= 60){
 System.out.println("print D" );
}
else{
System.out.println("print F" );
}
}
}
