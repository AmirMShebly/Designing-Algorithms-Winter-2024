package com.tabrizu;
import java.util.Arrays;


public class App 
{
    public static int[] maxSubarraySum(int[] arr) {
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;
        int startIndex = 0;
        int endIndex = 0;

        for (int i = 0; i < arr.length; i++) {
            currentSum += arr[i];

            if (currentSum > maxSum) {
                maxSum = currentSum;
                endIndex = i;
            }

            if (currentSum < 0) {
                currentSum = 0;
                startIndex = i + 1;
            }
        }

        if (maxSum == Integer.MIN_VALUE) {
            maxSum = Integer.MIN_VALUE;
            for (int value : arr) {
                maxSum = Math.max(maxSum, value);
            }
            int maxIndex = 0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == maxSum) {
                    maxIndex = i;
                    break;
                }
            }
            startIndex = maxIndex;
            endIndex = maxIndex;
        }

        return Arrays.copyOfRange(arr, startIndex, endIndex + 1);
    }


    public static void main( String[] args )
    {
        int[] arr = {7, -2, 4, -1, 9, -6, 5, 4};
        int[] maxSubarray = maxSubarraySum(arr);
        int maxSum = 0;
        for (int value : maxSubarray) {
            maxSum += value;
        }
        System.out.println("Maximum sum of a contiguous subarray: " + maxSum);
        System.out.print("The subarray with the maximum sum: [");
        for (int i = 0; i < maxSubarray.length; i++) {
            System.out.print(maxSubarray[i]);
            if (i < maxSubarray.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
