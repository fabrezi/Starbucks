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
