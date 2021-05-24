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

    
 //generate list of fibo to n
// n is static

public class fibo {

    public static void main(String[] args){
        int i, n, t1 = 0;
        int t2 = 1;
        int next_term = t1 + t2;
        int number_of_terms = 50;

        for (i=1; i <= number_of_terms; i++){
            System.out.println((i) + ": " + next_term);
            t1 = t2;
            t2 = next_term;
            next_term = t1 +  t2;
        }
    }

}
