#include <iostream>
using namespace std;

int* bubbleSortTemperatures(int temperatureData[], int size) {
    int stage = 0;

    for (int i = 0; i < size; i++) {
        bool swapped = false;
        for (int j = 0; j < size - i - 1; j++) {
            if (temperatureData[j] > temperatureData[j + 1]) {
                swap(temperatureData[j], temperatureData[j + 1]);
                swapped = true;
                stage++;
            }
        }
        if (!swapped) {
            break;
        }
    }

    cout << "Algorithm stopped at stage " << stage << endl;
    return temperatureData;
}

int main() {
    int temperatureData[] = {-7, -12, 24, 15, 3, -1, 14, 6};
    int size = sizeof(temperatureData) / sizeof(temperatureData[0]);
    bubbleSortTemperatures(temperatureData, size);

    cout << "Sorted temperature data: ";
    for (int i = 0; i < size; i++) {
        cout << temperatureData[i] << " ";
    }
    cout << endl;

    return 0;
}

