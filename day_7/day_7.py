import math
from collections import defaultdict
from functools import cmp_to_key

f = open("input2.txt", "r", newline='').read()
# f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")
charToVal = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 1, 'Q' : 12, 'K' : 13, 'A' : 14}
valid = set(['5', '41', '32', '311', '221', '2111', '11111'])

def inBetween(s1, s2):
  return f.split(s1)[1].split(s2)[0]

def parseInput():
  allHands = f.split('\n')
  hands = []
  vals = []
  for h in allHands:
    hands.append(h.split()[0])
    vals.append(int(h.split()[1]))

  return hands, vals

def compartor(h1, h2):
  h1Dict = defaultdict(int)
  h2Dict = defaultdict(int)
  for c in h1:
    h1Dict[c] += 1
  for c in h2:
    h2Dict[c] += 1
  j1Val = h1Dict['J']
  j2Val = h2Dict['J']
  del h1Dict['J']
  del h2Dict['J']
  vals1 = list(sorted(h1Dict.values(), reverse=True))
  vals2 = list(sorted(h2Dict.values(), reverse=True))

  if len(vals1) > 0:
    vals1[0] += j1Val
  else:
    vals1 = [5]
  if len(vals2) > 0:
    vals2[0] += j2Val
  else:
    vals2 = [5]

  assert("".join([str(c) for c in vals1]) in valid)
  assert("".join([str(c) for c in vals2]) in valid)
  h1Nums = [charToVal[c] for c in h1]
  h2Nums = [charToVal[c] for c in h2]
  if (vals1[0] == 5 or vals2[0] == 5):
    if (vals2[0] < 5):
      return 1
    elif (vals1[0] < 5):
      return -1
    # Both 5-of-a-kind
    ans = -1 if h1Nums <= h2Nums else 1
    print(f"{h1=}, {h2=}, {ans=}")
    return ans
  # if j1Val > 0:
  #   if h1Dict['J'] <= vals1[1]:
  #     vals1[0] += h1Dict['J']
  #   else:
  #     vals1[1] += h1Dict['J']
  #   vals1.remove(h1Dict['J'])
  # if 'J' in h2Dict:
  #   if h2Dict['J'] <= vals2[1]:
  #     vals2[0] += h2Dict['J']
  #   else:
  #     vals2[1] += h2Dict['J']
  #   vals2.remove(h2Dict['J'])

  # if (vals1[0] == 5 and vals2[0] == 5):
  #   return -1 if h1Nums[0] <= h2Nums[0] else 1

  if vals1[0] != vals2[0]:
    return -1 if vals1[0] <= vals2[0] else 1
  elif vals1[1] != vals2[1]:
    return -1 if vals1[1] <= vals2[1] else 1
  
  return -1 if h1Nums <= h2Nums else 1

def task1():
  hands, vals = parseInput()
  handsToVals = dict(zip(hands, vals))
  sortedHands = sorted(hands, key=cmp_to_key(compartor))
  print(list(filter(lambda h : 'J' in h, sortedHands)))
  total = 0
  for (i, h) in enumerate(sortedHands):
    total += (i+1)*handsToVals[h]
  return total

print(task1())