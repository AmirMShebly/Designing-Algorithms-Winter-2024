package com.tabrizu;

import java.util.Arrays;

public class App 
{
    public static void main( String[] args )
    {
        int[] grades = {85, 92, 78, 90, 65, 88, 70, 95, 83};
        int[] result = insertionSortGrades(grades);
        
        System.out.println("Sorted Grades: " + Arrays.toString(result));
    }

    public static int[] insertionSortGrades(int[] arr) {
        int comparisons = 0;
        
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
                comparisons++;
            }
            arr[j + 1] = key;
        }
        
        System.out.println("Comparisons: " + comparisons);
        return arr;
    }
}
