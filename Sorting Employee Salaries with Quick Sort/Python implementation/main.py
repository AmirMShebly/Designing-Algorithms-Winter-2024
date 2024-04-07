
class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[high]
        boundary = low - 1

        for i in range(low, high):
            if arr[i] <= pivot:
                boundary += 1
                arr[boundary], arr[i] = arr[i], arr[boundary]

        arr[boundary + 1], arr[high] = arr[high], arr[boundary + 1]
        return boundary + 1

    def quicksort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quicksort(arr, low, pivot - 1)
            self.quicksort(arr, pivot + 1, high)

    def sort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)
        return arr


salaries = [50000, 70000, 120000, 80000, 40000, 90000, 60000]
quicksort = QuickSort()
sorted_arr = quicksort.sort(salaries)
print(sorted_arr)
