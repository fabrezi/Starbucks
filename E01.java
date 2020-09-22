public class lowry {

   public static void main(String[] args){
       var sum = 0;

       for (int i=1; i < 1000; i++){
           if(i%3 == 0 || i%5 == 0)
               //System.out.print(i + ",");
           sum = sum + i;
       }
       System.out.print(sum);
   }
}
