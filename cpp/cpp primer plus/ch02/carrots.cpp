// carrots.cpp -- food processing program
// uses and displays a variables
#include <iostream>

int main() {
    using namespace std;

    int carrots;  // declares an integer variable

    carrots = 25;  // assign a value to the variable
    cout << "I have ";
    cout << carrots;  // displays the variable
    cout << " carrots.";
    cout << endl;
    carrots -= 1;  // modify the variable
    cout << "Crunch, crunch. Now I have " << carrots << " carrots." << endl;

    return 0;
}
