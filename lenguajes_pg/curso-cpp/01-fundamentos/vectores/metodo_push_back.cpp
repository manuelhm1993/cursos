#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> records {25, 45, 60, 35};

    // Agrega un nuevo elemento al final del vector
    records.push_back(105);

    // Devuelve el último elemento del vector
    cout << "El último elemento del vector es: " << records.back() << endl;

    int i = 0;

    for(int record: records) {
        cout << "Record #" << ++i << ": " << record << endl;
    }

    return 0;
}