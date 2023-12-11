from collections import defaultdict
from collections import OrderedDict
import bisect

f = open("input2.txt", "r", newline='').read()
# f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")

# for (i, line) in enumerate(f):
#   f[i] = line.strip('\n')

def inBetween(s1, s2):
  return f.split(s1)[1].split(s2)[0]

def getPath():
  return f.split('\n')[0]

def makeDict():
  d = dict()
  temp = f.split('\n\n')[1]
  lines = temp.split('\n')
  for line in lines:
    key, vals = line.split(' = ')
    lVal = vals[1:].split(',')[0]
    rVal = (vals.split(', ')[1])[:-1]
    d[key] = (lVal, rVal)
  return d

def getStartingKeys(d):
  return [key for key in d.keys() if (key[-1] == 'A')]

# path = getPath()
# pathDict = makeDict()

# i = 0
# steps = 0
# newKey = 'AAA'

# while(True):
#   steps += 1
#   direction = path[i % len(path)]
#   newKey = pathDict[newKey][0] if (direction == 'L') else pathDict[newKey][1]
#   if (newKey == 'ZZZ'):
#     break
#   i += 1

# print(steps)

# Part 2

path = getPath()
pathDict = makeDict()

i = 0
steps = 0
originalKeys = getStartingKeys(pathDict)
newKeys = getStartingKeys(pathDict)
cycles = OrderedDict(zip(newKeys, [0 for _ in range(len(newKeys))]))
finalCycles = OrderedDict(zip(newKeys, [0 for _ in range(len(newKeys))]))
numCycles = 0
# print(newKeys)

while(True):
  steps += 1
  direction = path[i % len(path)]
  newKeys = [pathDict[newKey][0] if (direction == 'L') else pathDict[newKey][1] for newKey in newKeys]
  for i in range(len(newKeys)):
    if (newKeys[i] == originalKeys[i]) and (newKeys[i] not in finalCycles):
      numCycles += 1
      finalCycles[newKeys[i]] = cycles[newKeys[i]]

  # print(newKeys)

  # b = True
  # for key in newKeys:
  #   if key[-1] != 'Z':
  #     b = False
  # if b:
  #   break
  i += 1

print(steps)