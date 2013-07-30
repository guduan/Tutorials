// strquote.cpp -- different designs
#include <iostream>
#include <string>

using namespace std;

// prototypes
string version1(const string &s1, const string &s2);
const string &version2(string &s1, const string &s2);  // has side effect
const string &version3(string &s1, const string &s2);  // bad design

int main() {
    string input;
    string copy;
    string result;

    cout << "Enter a string: ";
    getline(cin, input);
    copy = input;
    cout << "Your string was entered: " << input << endl;
    result = version1(input, "***");
    cout << "Your string enhanced: " << result << endl;
    cout << "Your original string: " << input << endl;

    result = version2(input, "###");
    cout << "Your string enhanced: " << result << endl;
    cout << "Your original string: " << input << endl;

    cout << "Resetting original string.\n";
    input = copy;
    result = version3(input, "@@@");
    cout << "Your string enhanced: " << result << endl;
    cout << "Your original string: " << input << endl;

    return 0;
}

string version1(const string &s1, const string &s2) {
    string temp;
    temp = s2 + s1 + s2;
    return temp;
}

const string &version2(string &s1, const string &s2) {
    s1 = s2 + s1 + s2;
    return s1;
}

const string &version(string &s1, const string &s2) {
    string temp;
    temp = s2 + s1 + s2;
    return temp;  // NEVER DO THIS! THIS IS RETURNING A TEMP VARIABLE!! Clang caught it!
}