#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> records;

    int n_records = 0;
    int item = 0;

    cout << "Ingrese el número de elementos del vector: "; cin >> n_records;

    for(int i = 0; i < n_records; i++) {
        cout << (i + 1) << ". Ingrese el valor del elemento: "; cin >> item;

        records.push_back(item);
    }

    cout << "------------- Mostrando elementos del vector -------------" << endl;
    cout << "Records: ";
    
    for(int record: records) {
        cout << record << " ";
    }
    
    cout << "\n";

    return 0;
}