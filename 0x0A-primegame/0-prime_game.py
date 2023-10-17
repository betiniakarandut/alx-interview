#!/usr/bin/python3
"""Module for prime game"""


def isWinner(x, nums):
    """Determines the winner of the game

    Args:
        x[int] - number of rounds to play
        nums[list[int:n]] - array of n

    Returns:
        name of winner[str]
    """
    if not nums or x < 1:
        return None
    Maria = 0
    ben = 0
    # get primes up to max num
    n = max(nums)
    primes = set(range(2, n + 1))
    for i in range(2, int(n**5) + 1):
        primes -= set(range(i * i, n + 1, i))
    for n in nums[:x]:
        primes_count = sum([p <= n for p in primes])
        ben += primes_count % 2 == 0
        Maria += primes_count % 2 == 1
    if Maria == ben:
        return None
    return 'Maria' if Maria > ben else 'Ben'
