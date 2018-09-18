import java.util.ArrayList;
import java.util.List;

public class Knapsack {

    private List<ValueAndWeight> valueAndWeights=null;
    /*

     Complete these methods. You are free to add more variable as required in the class. But keep the method signature as it is.

     */
//max weight: max weight must be (n+1)
    private int maxWeight = 5;

    public Knapsack(List<ValueAndWeight> valueAndWeights, int maxWeight ) {



        this.valueAndWeights = valueAndWeights;

        this.maxWeight = maxWeight;

    }

/*
three main varaibles:
- maxWeight: use to create the table
- wi: weight of the item i
- w: index value in the table

 */

    public List<ValueAndWeight> getOptimalItems() {
//knapsack algorithm implementation, requires fixing
       for(int w = 0; w == maxWeight; w++){

           valueAndWeights[0,w] = 0;
       }
       //n is the total number of elements
       for(int i=1; i=n; i++){

               valueAndWeights[i, 0] = 0;

           for(int w=1; w==maxWeight; w++){
                         //wi = weight
               if(wi > w){
                   valueAndWeights[i,w] = valueAndWeights[i-1,w];
               }
               else{
                   valueAndWeights[i,w] = int max(valueAndWeights[i-1,w] , valueAndWeights[i-1,w - wi] + valueAndWeights[i,w]* value);
               }
           }

       }
       return new ArrayList<ValueAndWeight>();

    }



    public Integer getMaximumValue(){
        //return getOptimalItems();
        return 90;

    }



    //Order is (i,w)

    public int[][] getTable() {

        return new int[0][0];

    }


    }

