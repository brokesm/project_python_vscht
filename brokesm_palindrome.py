forwardFlow = []
backwardFlow = []
palindromes = []
eightDigitNumber = 99999999


while eightDigitNumber > 10000000 and len(palindromes) < 1:
    backwardFlow = []
    for digit in str(eightDigitNumber):
        backwardFlow.append(digit)
    forwardFlow = backwardFlow[::-1]
    if False not in [i == j for i, j in zip(backwardFlow, forwardFlow)]:
        palindrome = int("".join(backwardFlow))
        for fourDigitNumber in range(1000,10000):
            result = int(palindrome) / fourDigitNumber
            if int(palindrome) % fourDigitNumber == 0 and len(str(int(result))) == 4:
                print(palindrome)
                palindromes.append(palindrome)
                break
    eightDigitNumber = eightDigitNumber - 1
    



    
    







