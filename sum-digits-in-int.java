import java.util.Scanner;

public class lolita {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("enter the number between 0 and 999:");
        int n = input.nextInt();
        if (n > 999 || n < 0){
            System.out.print("error");
        }
        else{
            int sum =0; //counter
            while (n != 0){
                sum += n%10;
                n = n/10;
            }
            System.out.print(sum);


        }
