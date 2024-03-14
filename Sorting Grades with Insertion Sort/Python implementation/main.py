
def insertion_sort_grades(grades):
    comparisons = 0

    for i in range(1, len(grades)):
        key = grades[i]
        j = i - 1
        while j >= 0 and key < grades[j]:
            grades[j + 1] = grades[j]
            j -= 1
            comparisons += 1
        grades[j + 1] = key

    return grades, comparisons


grades = [85, 92, 78, 90, 65, 88, 70, 95, 83]
sorted_grades, comparisons = insertion_sort_grades(grades)
print("Sorted Grades:", sorted_grades)
print("Comparisons:", comparisons)
