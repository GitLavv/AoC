input = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
inputArray = input.split()
arraySize = len(inputArray)
intArray = [int(x) for x in inputArray]
arrayOfPrevious = []

inputArray = intArray
complete = False
cycles = 0
steps = 0
add = 0
currentMax = 0

def toAdd():
  global add, steps, currentMax
  steps = currentMax
  add = 1

while not complete:
    maxBlock = intArray.index(max(intArray))
    currentMax = max(intArray)
    toAdd()
    intArray[maxBlock] = 0

    for i in range(1,currentMax+1):
      intArray[(maxBlock + i) % arraySize] += add

    cycles += 1
    complete = intArray in arrayOfPrevious
    arrayOfPrevious.append(intArray[:])

indices = [i for i, x in enumerate(arrayOfPrevious) if x == intArray]
print indices
print "%s current " %intArray
print ("%s max " %max(inputArray))
print ("%s cycles" % cycles)
