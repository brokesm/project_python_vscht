import random


class MyDungeon():

    border = "▓"
    space = "."
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def generateDungeon(self,numberOfTunnels):
        matrix = []
        directions = ["N","E","S","W"]
        for y in range(self.y):
            width = [self.border for element in range(self.x)]
            matrix.append(width)
        
        positionX = 1
        positionY = 1
        for tunnel in range(numberOfTunnels):
            randomDirection = random.choice(directions)

            if randomDirection == "W":
                randomTunnelLength = random.randint(0,self.x - positionX - 1)
                for step in range(randomTunnelLength):
                    matrix[positionY][positionX + step] = self.space
                    if step == randomTunnelLength - 1:
                        positionX = positionX + step

            if randomDirection == "E":
                randomTunnelLength = random.randint(0, positionX - 1)
                for step in range(randomTunnelLength):
                    matrix[positionY][positionX - step] = self.space
                    if step == randomTunnelLength - 1:
                        positionX = positionX - step

            if randomDirection == "N":
                randomTunnelLength = random.randint(0, positionY - 1)
                for step in range(randomTunnelLength):
                    matrix[positionY - step][positionX] = self.space
                    if step == randomTunnelLength - 1:
                        positionY = positionY - step

            if randomDirection == "S":
                randomTunnelLength = random.randint(0,self.y - positionY - 1)
                for step in range(randomTunnelLength):
                    matrix[positionY + step][positionX] = self.space
                    if step == randomTunnelLength - 1:
                        positionY = positionY + step

        if __name__ == "__main__":
            for row in range(self.y):
                print("".join(matrix[row]))

        return matrix
            
            

newDungeon = MyDungeon(10,10)
newDungeon.generateDungeon(40)
