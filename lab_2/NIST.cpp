#include "NIST.h"


void print_test_result(ostream& stream, string test_name, double p_val) {
    stream << "Test:" << test_name;
    stream << "P-value" << p_val;
    stream << "Conclusion:" << ((p_val >= 0.01) ? "Passed" : "Failed");
    stream << "\n\n";
}


double test1(string sequence) {
    double summ = 0;

    for (int i = 0; i < sequence.size(); ++i) {
        if (sequence[i] == '1')
            summ++;
        else
            summ--;
    }

    summ = summ / sqrt(sequence.size());

    return erfc(fabs(summ) / sqrt(2));
}


double test2(string sequence) {    double zeta = 0;
    size_t seq_len = sequence.size();

    for (int i = 0; i < seq_len; ++i) {
        if (sequence[i] == '1')
            zeta++;
    }
    zeta /= seq_len;

    if (fabs(zeta - 0.5) >= 2 / sqrt(seq_len))
        return 0;

    int Vn = 0;

    for (int i = 0; i < seq_len - 1; ++i) {
        if (sequence[i] != sequence[i+1])
            Vn++;
    }

    return erfc(fabs(Vn - 2 * seq_len * zeta * (1 - zeta)) / 
                (2 * sqrt(2 * seq_len) * zeta * (1 - zeta)));
}


double test3(string sequence) {
    return 0;
}
