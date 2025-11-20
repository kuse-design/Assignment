import java.util.Scanner;
public class StrenghtChecker{
public static void main(String[]args){

Scanner input = new Scanner(System.in);
System.out.print("Enter your  six digit password : ");
String checker = input.nextLine();
int length = checker.length();

if (length <= 6){
System.out.println("password is weak");
}
if  ( length > 6 && length < 10){
System.out.println("Password is medium");
}
if (length >= 10){
System.out.println("password is strong");
}
if (length < 1){
System.out.println("password is invalid");
}
}
}
