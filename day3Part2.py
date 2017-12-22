input = 312051
data = {(0,0):1}
complete = False
current = 1
path = (0,0)

def totalAround():
    global path
    total = data.get((path[0]+1, path[1]), 0)           #RIGHT
    total += data.get((path[0]+1, path[1]+1), 0)       #RIGHT UP
    total += data.get((path[0], path[1]+1), 0)         #UP
    total += data.get((path[0]-1, path[1]+1), 0)       #LEFT UP
    total += data.get((path[0]-1, path[1]), 0)         #LEFT
    total += data.get((path[0]-1, path[1]-1), 0)       #LEFT DOWN
    total += data.get((path[0], path[1]-1), 0)         #DOWN
    total += data.get((path[0]+1, path[1]-1), 0)       #DOWN RIGHT
    return total

def exit():
  print current
  return

for i in range(0,9):
        if i % 2 == 1:
            for x in range(0,i): #RIGHT
                path = (path[0] + 1, path[1])
                current = totalAround()
                data[path] = current
                complete = (current > input)
                if (complete):
                    print current
                    exit()

            for y in range(0,i): #UP
                path = (path[0], path[1] + 1)
                current = totalAround()
                data[path] = current
                complete = (current > input)
                if (complete):
                    print current
                    exit()

        else:
            for x in range (0,i): #LEFT
                path = (path[0] - 1, path[1])
                current = totalAround()
                data[path] = current
                complete = (current > input)
                if (complete):
                    print current
                    exit()


            for y in range (0,i): #DOWN
                path = (path[0], path[1] - 1)
                current = totalAround()
                data[path] = current
                complete = (current > input)
                if (complete):
                    print current
                    exit()
