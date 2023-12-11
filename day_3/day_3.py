import numpy as np

# f = open("test1.txt", "r").readlines()
# f = open("input1.txt", "r").readlines()
f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")

for (i, line) in enumerate(f):
  f[i] = line.strip('\n')

numLines = len(f)
lineSize = len(f[0])
digits = [str(i) for i in range(10)]
nonSymbols = ['.'] + digits
numbers = []
numMatrix = [[-1 for _ in range(len(f[0]))] for _ in range(len(f))]

# def check(i, j, offset):
#   b1 = '.' if j == 0 else f[i + offset][j - 1]
#   b2 = f[i + offset][j]
#   b3 = '.' if j == (len(f[i+offset]) - 1) else f[i + offset][j + 1]
#   return (b1 not in nonSymbols or b2 not in nonSymbols or b3 not in nonSymbols)

def findNum(line, startInd):
  digit = ''
  numInd = -1
  for j in range(startInd, len(line), 1):
    if line[j] in digits:
      if digit == '':
        numInd = j
        numMatrix[i][j] = len(numbers)
      digit += line[j]
    elif digit != '':
      break
  
  if digit != '':
    numbers.append(int(digit))
    return int(digit), numInd
  return -1, numInd

# def checkLine(i, end, digit):
#   length = len(str(digit))
#   valid = False
#   for j in range(end - length, end, 1):
#     if i > 0:
#       valid = valid or check(i, j, -1)
#     if i < numLines - 1:
#       valid = valid or check(i, j, 1)
#     valid = valid or check(i, j, 0)
  
  return valid

def parse_line(i):
  line = list(f[i])
  ans = 0
  j = 0
  while (True):
    digit, j = findNum(line, j)
    if digit == -1:
      break
    j = j + len(str(digit))
    # print(f"{digit=}, {j=}")
    # if (checkLine(i, j, digit)):
    #   if i < 10:
    #     print(digit)
    #   ans += digit

  return ans

def checkAst(i, j):
  totalNums = set()
  for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
      if (i + x) >= 0 and (i + x) < lineSize and (j + y) >= 0 and (j + y) < numLines:
        if (f[i][j] != -1):
          totalNums.add(numbers[numMatrix[i+x][j+y]])

  if (len(totalNums) == 2):
    prod = 1
    for elem in totalNums:
      print(elem)
      prod *= elem
    return prod
  return 0

def asterisk():
  total = 0

  for (i, line) in enumerate(f):
    for (j, c) in enumerate(line):
      if f[i][j] == '*':
        if(checkAst(i, j) != 0):
          total += checkAst(i, j)

  return total

ans = 0
symbols = set()
for (i, line) in enumerate(f):
  parse_line(i)

print(asterisk())

# print(ans)
# 2632