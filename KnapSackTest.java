import java.util.ArrayList;

public class KnapSackTest {

    /*

     Please don't modify this class. you are free to add more test cases in a different class as needed.

     */



    @Test

    public void testKnapSack(){





        ArrayList<ValueAndWeight> valueAndWeights = new ArrayList<ValueAndWeight>();

        valueAndWeights.add(new ValueAndWeight(2,3));

        valueAndWeights.add(new ValueAndWeight(3,4));

        valueAndWeights.add(new ValueAndWeight(4,5));

        valueAndWeights.add(new ValueAndWeight(5,6));



        Knapsack knapSack = new Knapsack(valueAndWeights,5 );



        Assert.assertEquals(knapSack.getMaximumValue().intValue(),90);

        ArrayList<ValueAndWeight> solution = Knapsack.getOptimalItems();

        Assert.assertTrue(solution.size()==2);

        Assert.assertTrue(solution.contains(new ValueAndWeight(40,4)));

        Assert.assertTrue(solution.contains(new ValueAndWeight(50,3)));



        int[][] table = knapSack.getTable();

        Assert.assertEquals(table[4][10], 90);

        Assert.assertEquals(table[4][3], 50);









    }

}
}
