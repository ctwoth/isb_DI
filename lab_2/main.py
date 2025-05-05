from typing import TextIO

from consts import*
import tests


def write_test_result(file: TextIO, test_name: str, p_val: float) -> None:
    """
    Writing test results into file buffer.
    If the P-value is ≥ 0.01,
    then the sequence is considered random.

    :param file:
    :param test_name:
    :param p_val:
    :return:
    """
    file.write("Test: " + test_name + '\n')
    file.write("P-value: " + str(p_val) + '\n')
    file.write("Conclusion: " + ("Passed" if p_val >= 0.01 else "Failed") + '\n\n\n')


def sequence_testing(results_path: str, sequence: str) -> None:
    """
    Testing sequence using three NIST tests, and writing results into file.

    :param results_path:
    :param sequence:
    :return:
    """
    with open(results_path, 'w+', encoding="utf-8") as file:

        file.write("testing sequence: " + sequence + "\n\n")
        rez1 = tests.test1(sequence)
        rez2 = tests.test2(sequence)
        rez3 = tests.test3(sequence)

        write_test_result(file, "Frequency bitwise test.", rez1)
        write_test_result(file, "Identical consecutive bits test.", rez2)
        write_test_result(file, "Longest sequence of units in a block test.", rez3)


def main() -> None:
    sequence_testing(JAVA_RESULT_PATH, JAVA_SEQUENCE)
    sequence_testing(CPP_RESULT_PATH, CPP_SEQUENCE)


if __name__ == '__main__':
    main()