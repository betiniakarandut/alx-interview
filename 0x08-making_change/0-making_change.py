#!/usr/bin/python3
"""
Making Change - ALX Interview

fewest number of coins needed
"""


def makeChange(coins, total):
    """
    Fewest number of coins needed to meet total.

    Args:
        coins(list[int]) - coin value
        total(int) - Target amount 

    Returns:
        fewest number of coins
        return -1, If not possible to make the total with the given coins
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # The value of a coin will always be an integer greater than 0
    """
    Bring all coins that are greater than 0
    and less then or equal to total
    """
    if len(coins) != 0:
        new_coins = [i for i in coins if ((i > 0) and (i <= total))]

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in new_coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
