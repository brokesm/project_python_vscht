"""
This module merely calculates the sum of all even elements in a given Fibonacci series and prints it
"""

CURRENT = 0
NEXT = 1
SUMM = 0
while NEXT <= 5000000:
    if NEXT % 2 == 0:
        SUMM = SUMM + NEXT
    PREVIOUS = NEXT
    NEXT = NEXT + CURRENT
    CURRENT = PREVIOUS
print(SUMM)
