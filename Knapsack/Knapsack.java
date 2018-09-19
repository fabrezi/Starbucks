package edu.kennesaw.aa;

//package main.com.manh.farid;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Knapsack {

    private int[][] weightTable;
    private int noOfItems;

    private List<ValueAndWeight> valueAndWeights=null;
    /*
     Complete these methods. You are free to add more variable as required in the class. But keep the method signature as it is.
     */
    private int maxWeight = 5;

    public Knapsack(List<ValueAndWeight> valueAndWeights, int maxWeight) {
        this.valueAndWeights = valueAndWeights;
        this.noOfItems = valueAndWeights.size();
        this.maxWeight = maxWeight;

        weightTable = new int[valueAndWeights.size() + 1][maxWeight + 1];
    }

    public List<ValueAndWeight> getOptimalItems() {

        for(int i = 0; i <= maxWeight; i++) {
            weightTable[0][i] = 0;
        }

        for(int i = 1; i <= noOfItems; i++) {
            weightTable[i][0] = 0;
        }

        for(int i = 1; i <= noOfItems; i++) {
            for (int w = 1; w <= maxWeight; w++) {
                int weightAtI = valueAndWeights.get(i- 1).getWeight();
                int benefitAtI = valueAndWeights.get(i - 1).getValue();
                int benefitAtIMinusW = weightTable[i - 1][w];
                if(weightAtI <= w)  { // item i can be part of the soluiton
                   int benefitAtIMinusWMinuwWI = weightTable[i - 1][w - weightAtI];
                   if(benefitAtI + benefitAtIMinusWMinuwWI > benefitAtIMinusW)  {
                       weightTable[i][w] = benefitAtI + benefitAtIMinusWMinuwWI;
                   } else {
                       weightTable[i][w] = benefitAtIMinusW;
                   }
                } else {
                   weightTable[i][w] = benefitAtIMinusW;
                }
            }
        }
        System.out.println(this);

        int i = noOfItems - 1;
        int k = maxWeight - 1;

        ArrayList<ValueAndWeight> optimalItems = new ArrayList<>();

        while( i > 0 && k > 0) {
            int weightAtI = valueAndWeights.get(i).getWeight();
            if(weightTable[i][k] != weightTable[i-1][k]) {
                // mark the i item as in the knapsack
                optimalItems.add(valueAndWeights.get(i));
                i = i -1;
                k = k - weightAtI;
            } else {
                i = i -1;
            }
        }

        //System.out.println(optimalItems.toArray());
        return optimalItems;
    }

    public Integer getMaximumValue(){
        return weightTable[noOfItems][maxWeight];
    }

    //Order is (i,w)
    public int[][] getTable() {
        return weightTable;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for(int[] arr: weightTable) {
            sb.append(Arrays.toString(arr)).append("\n");
        }

        return sb.toString();
    }

    /*

        return weightTable[i][k];
     */
}
