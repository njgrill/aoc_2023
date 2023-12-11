import math
from collections import defaultdict
from functools import cmp_to_key

#################### HELPERS ####################
f = open("input1.txt", "r", newline='').read()

def inBetween(s1, s2):
  return f.split(s1)[1].split(s2)[0]

#################### HELPERS ####################
#################### PARSING ####################
def parseInput():
  return list(map(lambda x : list(map(int, x.split())), f.split('\n')))

def parseInput2():
  pass

#################### PARSING ####################
##################### BODY #####################
def allZeros(l):
  return l.count(0) == len(l)

def extrapHistory(h):
  extraps = [[elem for elem in h]]

  while(not allZeros(extraps[-1])):
    newExtraps = []
    for i in range(1, len(extraps[-1]), 1):
      newExtraps.append(extraps[-1][i] - extraps[-1][i-1])
    extraps.append(newExtraps)
  
  extraps[-1].append(0)
  for i in range(len(extraps)-2, -1, -1):
    extraps[i].append(extraps[i][-1] + extraps[i+1][-1])
  
  return extraps[0][-1]

def task1():
  histories = parseInput()
  total = 0
  for history in histories:
    total += extrapHistory(history)
  return total

def task2():
  _ = parseInput2()

##################### BODY #####################

print(task1())