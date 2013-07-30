// left.cpp -- string functions with a default argument
#include <iostream>

const int AR_SIZE = 80;

char *left(const char *str, int n = 1);

int main() {
    using namespace std;
    char sample[AR_SIZE];

    cout << "Enter a string: \n";
    cin.get(sample, AR_SIZE);
    char *ps = left(sample, 4);
    cout << ps << endl;
    delete []ps;  // free old string
    ps = left(sample);
    cout << ps << endl;
    delete []ps;  // free new string

    return 0;
}

// this function returns a pointer to a new string consisting of the first n characters in the str
// string.
char *left(const char *str, int n) {
    if (n < 0)
        n = 0;
    char *p = new char[n+1];
    int i;

    for (i = 0; i < n && str[i]; ++i)
        p[i] = str[i];  // copy characters

    while (i <= n)
        p[i++] = '\0';  // set rest of string to '\0'

    return p;
}
