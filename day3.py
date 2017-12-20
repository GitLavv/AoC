target = 312051
path = [0,0]
number = 1

def checkIfTarget():
    if number == target:
        print(abs(path[0]) + abs(path[1]))

for i in range(1,1000): #i is amount of movements to go in a direction
    if i % 2 == 1:
        for x in range(0,i): #RIGHT
            path[0] += 1
            number += 1
            checkIfTarget()

        for y in range(0,i): #UP
            path[1] += 1
            number += 1
            checkIfTarget()
    else:
        for x in range (0,i): #LEFT
            path[0] -= 1
            number += 1
            checkIfTarget()

        for y in range (0,i): #DOWN
            path[1] -= 1
            number += 1
            checkIfTarget()

