// Computes and prints n! for a given num. Uses several basic elements of C++.

#include <iostream>


int main()
{
    using namespace std;

    int factArg = 0;
    int fact(1);

    do {
        cout << "Factorial of: ";
        cin >> factArg;

        if (factArg < 0) {
            cout << "No negative values, please!" << endl;
        }
    } while (factArg < 0);

    int i = 2;
    while (i <= factArg) {
        fact *= i;
        i++;
    }

    cout << "The factorial of " << factArg << " is: " << fact << endl;
    return 0;
}