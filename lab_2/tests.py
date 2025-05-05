import math
from scipy.special import gammainc

from consts import *


def test1(sequence: str) -> float:
    """
    Frequency bitwise test.
    If the sequence being tested is sufficiently random,
    then the P-value is close enough to 1.

    :param sequence:
    :return p-value:
    """
    summ = 0

    for bit in sequence:
        if bit == '1':
            summ += 1
        else:
            summ -= 1

    summ = summ / math.sqrt(len(sequence))

    return math.erfc(abs(summ) / math.sqrt(2))


def test2(sequence: str) -> float:
    """
    Identical consecutive bits test.
    The purpose of this test is to determine
    how often the "1" changes to "0" and back.

    :param sequence:
    :return p-value:
    """
    seq_len = len(sequence)
    zeta = sequence.count('1')/seq_len

    if abs(zeta - 0.5) >= 2 / math.sqrt(seq_len):
        return 0.0

    Vn = 0
    for i in range(seq_len - 1):
        if sequence[i] != sequence[i+1]:
            Vn += 1

    numerator = abs(Vn - 2 * seq_len * zeta * (1 - zeta))
    denominator = 2 * math.sqrt(2 * seq_len) * zeta * (1 - zeta)

    return math.erfc(numerator/denominator)


def test3(sequence: str) -> float:
    """
    The original long sequence is split into blocks of length BLOCK_LENGTH.
    Inside the block searching the longest sequence of units аnd it
    is compared with the reference sequence using xi^2;

    :param sequence:
    :return p-value:
    """
    v = [0, 0, 0, 0]
    seq_len = len(sequence)
    block_num = seq_len // BLOCK_LENGTH

    for i in range(block_num):
        block = sequence[i * BLOCK_LENGTH : (i+1) * BLOCK_LENGTH]
        maxx = 0
        cur = 0

        for bit in block:
            if bit == '1':
                cur += 1
                maxx = max(maxx, cur)
            else:
                cur = 0

        if   maxx <= 1: v[0] += 1
        elif maxx == 2: v[1] += 1
        elif maxx == 3: v[2] += 1
        else          : v[3] += 1

    xi = 0.0
    for i in range(4):
        xi += pow(v[i] - block_num * PI[i], 2) / (block_num * PI[i])

    return gammainc(1.5, xi / 2)