//calculate factorial through recursion calls
public class minsk {
    public static void main(String[] args) {
        int n = 10;

        System.out.println("the factorial is:" + factorial(n));
    }
    public static long factorial(int n){
        if(n==0)
            return 1;
        else
            return n * factorial(n-1);
    }
}



import java.util.Scanner;
//add positive integers from n + (n-1) +...0
public class hello {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("enter a digit:");
        int n = input.nextInt();
        System.out.println("the sum:" + zarb(n));
    }
    public static int zarb(int n){
        if(n==0)
            return 0;
        else
            return n + zarb(n-1);
    }


}
