#include "NIST.h"


void print_test_result(ostream& stream, string test_name, double p_val) {
    stream << "Test:" << test_name;
    stream << "P-value" << p_val;
    stream << "Conclusion:" << ((p_val >= 0.01) ? "Passed" : "Failed");
    stream << "\n\n";
}


double test1(string sequence) {
    return 0;
}


double test2(string sequence) {
    return 0;
}


double test3(string sequence) {
    return 0;
}
