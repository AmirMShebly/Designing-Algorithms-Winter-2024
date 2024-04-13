package com.tabrizu;


public class App 
{
    public static void main( String[] args )
    {
        int[] salaries = {50000, 70000, 40000, 90000, 60000};
        QuickSort sorter = new QuickSort();
        sorter.sort(salaries);
        for (int i = 0; i < salaries.length; i++) {
            System.out.println(salaries[i]);
        }
    }


    
}
