#include <iostream>
#include <vector>

using namespace std;

pair<vector<int>, int> insertionSortGrades(vector<int> grades) {
    int comparisons = 0;
    int n = grades.size();

    for (int i = 1; i < n; ++i) {
        int key = grades[i];
        int j = i - 1;

        while (j >= 0 && grades[j] > key) {
            grades[j + 1] = grades[j];
            comparisons++;
            j--;
        }
        grades[j + 1] = key;
    }

    return make_pair(grades, comparisons);
}

int main() {
    vector<int> grades = {85, 92, 78, 90, 65, 88, 70, 95, 83};
    pair<vector<int>, int> result = insertionSortGrades(grades);

    cout << "Sorted Grades: ";
    for (int grade : result.first) {
        cout << grade << " ";
    }
    cout << endl;

    cout << "Comparisons: " << result.second << endl;

    return 0;
}

