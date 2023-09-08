#include <iostream>
#include <climits>
#include <cfloat>

using namespace std;

int main() {

	// int my_uninitialized_variable;

	cout << "Hello World\n";
	cout << INT_MIN << endl;
	cout << FLT_MAX << endl;
	// cout << my_uninitialized_variable << endl;

	//Scalar types
	int i = 0;
	int j{ 2 };
	char ch = 'a';
	bool flag = false;	//true or false

	float f = 3.14159f;
	double d = 521.342;
	cout << f << endl;

	//Vector types
	int arr[5];
	int arr1[5] = { 0, 1, 2, 3, 4 };
	int arr2[5]{ 5, 4, 3, 2, 1 };

	cout << arr[0] << endl;
	cout << arr1[2] << endl;
	cout << arr2[0] << endl;

}