#include <iostream>
using namespace std;

int main() {
    const int kMinNum = 1;
    const int kMaxNum = 10;

    for(int i=kMinNum;i<=kMaxNum;i++) {
        cout << "Tabla del número " << i << ":\n";
        for(int j=kMinNum;j<=kMaxNum;j++) {
            cout << i << " x " << j << " = " << (i*j) << endl;
        }
        cout << "\n";
    }

    return 0;
}