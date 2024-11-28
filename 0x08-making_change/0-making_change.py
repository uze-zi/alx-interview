#!/usr/bin/python3
"""Module: 8-making_change"""


def makeChange(coin, total):
    coin = sorted(coin, reverse=True)
    remaining = total
    count = 0

    for c in coin:
        if c > remaining:
            continue

        while remaining >= c:
            remaining -= c
            count += 1

    if remaining > 0:
        return -1

    return count
