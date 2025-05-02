#include "NIST.h"


void print_test_result(ostream& stream, string test_name, double p_val) {
    stream << "Test:" << test_name << '\n';
    stream << "P-value" << p_val << '\n';
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


double test2(string sequence) {
    double zeta = 0;
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
    int v[] = { 0,0,0,0 };

    for (int start = 0; start < sequence.size(); start += BLOCK_LENGTH) {
        int max_len = 0, cur_len = 0;

        for (int i = start; i < start + BLOCK_LENGTH; ++i) {
            if (sequence[i] == '1')
                cur_len++;

            else {
                max_len = max(max_len, cur_len);
                cur_len = 0;
            }
        }

        if (max_len <= 1) v[0]++;
        else if (max_len == 2) v[1]++;
        else if (max_len == 3) v[2]++;
        else if (max_len >= 4) v[3]++;
    }

    double xi = 0;
    for (int i = 0; i < 4; ++i) {
        xi += pow(v[i] - 16 * PI[i], 2)/(16*PI[i]);
    }

    return boost::math::gamma_p(1.5, xi/2);
}
