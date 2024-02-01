#!/usr/bin/python3
'''Change comes from within'''


def makeChange(coins, total):
    """
    determine fewest number of coins needed to meet a given amount total

    Parameters:
    coins (list): a list of the values of the coins in your possession
    total (int): given amount

    Return:
    0 if total is 0 or less
    -1 if total cannot be met by any number of coins you have
    """
    if total <= 0:
        return 0

    change = [0] + [total+1] * total
    for coin in coins:
        for i in range(coin, total + 1):
            change[i] = min(change[i], change[i - coin] + 1)

    return change[total] if change[total] != total + 1 else -1
