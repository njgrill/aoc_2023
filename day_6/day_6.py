import math

f = open("input2.txt", "r", newline='').read()
# f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")

def inBetween(s1, s2):
  return f.split(s1)[1].split(s2)[0]

def parseInput():
  times, distances = f.split('\n')
  distances = distances.split('\n')[0]
  times = list(map(int, (times.split()[1:])))
  distances = list(map(int, distances.split()[1:].join()))

  return times, distances

def parseInput2():
  times, distances = f.split('\n')
  distances = distances.split('\n')[0]
  times = [int("".join(times.split()[1:]))]
  distances = [int("".join(distances.split()[1:]))]

  return times, distances

def task1():
  ts, ds = parseInput()
  ans = 1
  # (t-x)x > d
  # x^2 - tx + d < 0
  # x = (t +- sqrt(t^2 - 4d))/2
  for t, d in zip(ts, ds):
    x1 = int((t + (math.sqrt(t**2 - 4*d))) // 2)
    x2 = int(math.ceil((t - (math.sqrt(t**2 - 4*d))) / 2))
    if ((t-x1)*x1) == d:
      x1 -= 1
    if ((t-x2)*x2) == d:
      x2 += 1
    ans *= (x1 - x2 + 1)
  return ans

def task2():
  ts, ds = parseInput2()
  ans = 1
  # (t-x)x > d
  # x^2 - tx + d < 0
  # x = (t +- sqrt(t^2 - 4d))/2
  for t, d in zip(ts, ds):
    x1 = int((t + (math.sqrt(t**2 - 4*d))) // 2)
    x2 = int(math.ceil((t - (math.sqrt(t**2 - 4*d))) / 2))
    if ((t-x1)*x1) == d:
      x1 -= 1
    if ((t-x2)*x2) == d:
      x2 += 1
    ans *= (x1 - x2 + 1)
  return ans

print(task2())