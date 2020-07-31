
import java.util.Scanner;
public class MyClass {
    public static void main(String args[]) {
int y;
Scanner in =new Scanner(System.in);
System.out.println("Enter year=");
y=in.nextInt();
if((y%4==0 && y%100!=0)||(y%400==0))
 System.out.println("Leap Year ") ;
 else 
 System.out.println("Not a Leap Year ") ;
    }
}
