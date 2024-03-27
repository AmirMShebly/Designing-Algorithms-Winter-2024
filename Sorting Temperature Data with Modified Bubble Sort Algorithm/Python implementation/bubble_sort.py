def bubble_sort_temperatures(temperature_data):
    n = len(temperature_data)
    stage = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if temperature_data[j] > temperature_data[j + 1]:
                temperature_data[j], temperature_data[j + 1] = temperature_data[j + 1], temperature_data[j]
                swapped = True
                stage += 1
        if not swapped:
            break

    print("Algorithm stopped at stage", stage)
    return temperature_data



temperature_data = [-7, -12, 24, 15, 3, -1, 14, 6]
sorted_temperature_data = bubble_sort_temperatures(temperature_data)
print("Sorted temperature data:", sorted_temperature_data)

