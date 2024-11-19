"""
This module calculates the sum of all numbers divisible by 3 or 5 that are less than 1234
"""

SUMM = 0

for number in range(1234):
    if number % 3 == 0 or number % 5 == 0:
        SUMM = SUMM + number

print(SUMM)
