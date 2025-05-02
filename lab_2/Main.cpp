#include <iostream>
#include <fstream>
#include "NIST.h"


using namespace std;


void print_test_result(ostream& stream, string test_name, double p_val) {
    stream << "Test: " << test_name << '\n';
    stream << "P-value: " << p_val << '\n';
    stream << "Conclusion: " << ((p_val >= 0.01) ? "Passed" : "Failed");
    stream << "\n\n";
}

void sequence_testing(string results_path, string sequence){
	ofstream file;
	file.open(results_path);

	file << "testing sequence: " << sequence << "\n\n";

	double rez1 = test1(sequence);
	double rez2 = test2(sequence);
	double rez3 = test3(sequence);

	print_test_result(file, "Frequency bitwise test.", rez1);
	print_test_result(file, "Identical consecutive bits test.", rez2);
	print_test_result(file, "Longest sequence of units in a block test.", rez3);

	file.close();
}


int main() {
	sequence_testing(JAVA_RESULT_PATH, JAVA_SEQUENCE);
	sequence_testing(CPP_RESULT_PATH, CPP_SEQUENCE);
	
	return 0;
}
