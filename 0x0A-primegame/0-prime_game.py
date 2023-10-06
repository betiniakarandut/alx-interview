#!/usr/bin/python3
"""Module for 0-prime_game.py"""


def isWinner(x, nums):
    """Determines the winner of the game

    Args:
        x[int] - number of rounds to play
        nums[list[int:n]] - array of n

    Returns:
        name of winner[str]
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize a list to store the results for each n
    results = [None] * (max(nums) + 1)

    def canWin(n):
        if n == 1:
            return False

        if results[n] is not None:
            return results[n]

        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                if not canWin(n - i):
                    results[n] = True
                    return True

        results[n] = False
        return False

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the player who won the most rounds
    if ben_wins > maria_wins:
        return "Ben"
    elif ben_wins < maria_wins:
        return "Maria"
    else:
        return None
