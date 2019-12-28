from collections import defaultdict
from typing import List


def longest_arithmetic_sequence_length(a: List[int]) -> int:
    dp = defaultdict(lambda: 1)
    dp[(a[1] - a[0], 1)] = 2
    for i in range(2, len(a)):
        for j in range(i):
            interval = a[i] - a[j]
            dp[(interval, i)] = 2 if (interval, j) not in dp else dp[(interval, j)] + 1
    return max(dp.values())
