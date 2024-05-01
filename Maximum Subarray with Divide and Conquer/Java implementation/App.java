package com.tabrizu;


public class App 
{
    public static int[] maxCrossingSubarray(int[] arr, int low, int mid, int high) {
        int leftSum = Integer.MIN_VALUE;
        int maxLeft = mid;
        int tempSum = 0;

        for (int i = mid; i >= low; i--) {
            tempSum += arr[i];
            if (tempSum > leftSum) {
                leftSum = tempSum;
                maxLeft = i;
            }
        }

        int rightSum = Integer.MIN_VALUE;
        int maxRight = mid + 1;
        tempSum = 0;

        for (int i = mid + 1; i <= high; i++) {
            tempSum += arr[i];
            if (tempSum > rightSum) {
                rightSum = tempSum;
                maxRight = i;
            }
        }

        return new int[]{maxLeft, maxRight, leftSum + rightSum};
    }

    public static int[] maxSubarray(int[] arr, int low, int high) {
        if (low == high) {
            return new int[]{low, high, arr[low]};
        }

        int mid = (low + high) / 2;

        int[] leftResult = maxSubarray(arr, low, mid);
        int[] rightResult = maxSubarray(arr, mid + 1, high);
        int[] crossResult = maxCrossingSubarray(arr, low, mid, high);

        if (leftResult[2] >= rightResult[2] && leftResult[2] >= crossResult[2]) {
            return leftResult;
        } else if (rightResult[2] >= leftResult[2] && rightResult[2] >= crossResult[2]) {
            return rightResult;
        } else {
            return crossResult;
        }
    }

    public static void main( String[] args )
    {
        int[] arr = {7, -2, 4, -1, 9, -6, 5, 4};
        int[] result = maxSubarray(arr, 0, arr.length - 1);
        int maxSum = result[2];
        int start = result[0];
        int end = result[1];
        System.out.println("Maximum sum of a contiguous subarray: " + maxSum);
        System.out.print("The subarray with the maximum sum: [");
        for (int i = start; i <= end; i++) {
            System.out.print(arr[i]);
            if (i < end) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
