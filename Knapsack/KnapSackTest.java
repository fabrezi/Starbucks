package edu.kennesaw.aa;

import java.util.ArrayList;

public class KnapSackTest {

    /*

     Please don't modify this class. you are free to add more test cases in a different class as needed.

     */


    public static void main(String[] args) {
        KnapSackTest knapSackTest = new KnapSackTest();
        knapSackTest.testKnapSack();
    }


    public void testKnapSack(){





        ArrayList<ValueAndWeight> valueAndWeights = new ArrayList<ValueAndWeight>();

        valueAndWeights.add(new ValueAndWeight(2,3));

        valueAndWeights.add(new ValueAndWeight(3,4));

        valueAndWeights.add(new ValueAndWeight(4,5));

        valueAndWeights.add(new ValueAndWeight(5,6));



        Knapsack knapSack = new Knapsack(valueAndWeights,5 );

        ArrayList<ValueAndWeight> solution = (ArrayList<ValueAndWeight>) knapSack.getOptimalItems();

        assertTrue(solution.size()==1);

        assertTrue(solution.get(0).getWeight() == (new ValueAndWeight(5,6)).getWeight());;
        assertTrue(solution.get(0).getValue() == (new ValueAndWeight(5,6)).getValue());;

        //assertTrue(solution.contains(new ValueAndWeight(50,3)));



        int[][] table = knapSack.getTable();

        assertEquals(table[4][5], 7);

        assertEquals(table[4][3], 4);

    }

    void assertEquals(int value, int expected) {
        if(value != expected) {
            System.err.println("Value not equal to expected. Failed");
        } else {
            System.out.println("Value equal to expected. Pass");
        }
    }

    void assertTrue(boolean result){
        if(!result) {
            System.err.println("Result not True. Failed");
        } else {
            System.out.println("Result True. Pass");
        }
    }


}
