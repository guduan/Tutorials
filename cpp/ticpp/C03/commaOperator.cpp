// C03: commaOperator.cpp
#include <iostream>
using namespace std;

int main()
{
	int a = 0, b = 1, c = 2, d = 3, e = 4;

	a = (b++, c++, d++, e++);
	cout << "a = " << a << endl;
	// the parentheses are critical here. Without them, the statements will evaluate to:
	(a = b++), c++, d++, e++;
	cout << "a = " << a << endl;

	return 0;
}