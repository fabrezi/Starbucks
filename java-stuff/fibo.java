//find nth fibo number
//recursion applied

public class eu01 {

    static int fibo(int n){
        if (n <= 1){
            return n;
        }
        else{
            return (fibo(n-1) + fibo(n-2));
        }
    }

    public static void main(String[] args){
        int n = 10;
        System.out.println(fibo(n));
    }

