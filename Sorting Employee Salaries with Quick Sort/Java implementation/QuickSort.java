package com.tabrizu;

public class QuickSort {
    
    private int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int bound = low - 1;

        for (int i = low; i < high; i++) {
            if (arr[i] < pivot) {
                bound ++;
                int tmp = arr[i];
                arr[i] = arr[bound];
                arr[bound] = tmp;
            }
        }
        int tmp = arr[bound + 1];
        arr[bound + 1] = arr[high];
        arr[high] = tmp;

        return bound + 1;
    }

    private void quickSort(int[] arr, int low, int high) {
        if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
        }
    }

    public void sort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }
}
