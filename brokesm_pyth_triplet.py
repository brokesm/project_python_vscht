a = 1
b = 1
c = 1

def pythagoreanTriple():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a*a + b*b == c*c and a+b+c == 1000 and a*b*c != 0:
                    return print(a*b*c)
                
pythagoreanTriple()




