from collections import defaultdict
import bisect

f = open("input.txt", "r", newline='').read()
# f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")

# for (i, line) in enumerate(f):
#   f[i] = line.strip('\n')

def get_seeds():
  return list(map(int, f.split("seeds: ")[1].split('\n')[0].split(' ')))

def get_seeds_two():
  parsedList = list(map(int, f.split("seeds: ")[1].split('\n')[0].split(' ')))
  intervals = [(parsedList[2*i], parsedList[2*i] + parsedList[2*i + 1] - 1) for i in range(len(parsedList) // 2)]
  intervals = sorted(intervals, key=lambda x: x[0])
  newIntervals = [intervals[0]]
  for i in range(1, len(intervals), 1):
    intervalStart, intervalEnd = intervals[i]
    newIntStart, newIntEnd = newIntervals[-1]
    if (intervalStart <= newIntEnd):
      newIntervals[-1] = (newIntStart, max(intervalEnd, newIntEnd))
    else:
      newIntervals.append(intervals[i])
  print(f"{newIntervals=}")
  return newIntervals

def get_maps():
  res = []
  maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
  for m in maps:
    rows = f.split(f"{m} map:\n")[1].split('\n\n')[0].split('\n')
    rows = [list(map(int, row.split(' '))) for row in rows if ' ' in row]
    res.append(rows)
  
  return res

# Returns prefix array of maps
def process_map(m):
  prefixMap = defaultdict(int)
  for row in m:
    new, old, r = row
    prefixMap[old] += (new - old)
    prefixMap[old + r] -= (new - old)
  prefixMap = dict(sorted(prefixMap.items()))

  vals = list(prefixMap.values())
  for i in range(len(vals)):
    if i > 0:
      vals[i] += vals[i-1]
  return list(prefixMap.keys()), vals

# Returns prefix array of maps
def process_map_rev(m):
  prefixMap = defaultdict(int)
  for row in m:
    old, new, r = row
    prefixMap[old] += (new - old)
    prefixMap[old + r] -= (new - old)
  prefixMap = dict(sorted(prefixMap.items()))

  vals = list(prefixMap.values())
  for i in range(len(vals)):
    if i > 0:
      vals[i] += vals[i-1]
  return list(prefixMap.keys()), vals

def newSeed(keys, vals):
  def f(s):
    if s < keys[0]:
      return s
    if s > keys[-1]:
      return s
    ind = bisect.bisect_right(keys, s) - 1
    return s + vals[ind]
  return f

# allSeeds = get_seeds()
# allMaps = list(map(process_map, get_maps()))
# print(allSeeds)
# print(allMaps)

# for keys, vals in allMaps:
#   mapFunc = newSeed(keys, vals)
#   allSeeds = list(map(mapFunc, allSeeds))
#   # print(allSeeds)

# print(min(allSeeds))

# Part 2
def newSeed2(keys, vals):
  def f(s):
    if s < keys[0]:
      return s
    if s > keys[-1]:
      return s
    ind = bisect.bisect_right(keys, s) - 1
    return ind
  return f

# Processing
allSeeds = get_seeds_two()
allMaps = list(map(process_map, get_maps()))
revMaps = list(map(process_map_rev, get_maps()))
interestingSeeds = set()

# Get interesting seeds
for i in range(len(allMaps)-1, -1, -1):
  keys, vals = allMaps[i]
  newInteresting = list(interestingSeeds)
  mapFunc = newSeed(*revMaps[i])
  interestingSeeds = set(keys + list(map(mapFunc, newInteresting)))
interestingSeeds = list(sorted(interestingSeeds))

# Map interesting seeds to final seeds
finalSeeds = [elem for elem in interestingSeeds]
for keys, vals in allMaps:
  mapFunc = newSeed(keys, vals)
  finalSeeds = list(map(mapFunc, finalSeeds))
finalMap = (interestingSeeds, [])

# Map input seed ranges to range of indices over interesting seeds
newSeedFunc = newSeed2(*finalMap)
allSeedsIntervals = map(lambda x: (newSeedFunc(x[0]), newSeedFunc(x[1])), allSeeds)

# Expand allSeedsIntervals into individual indices in interestingSeeds
interestingInputSeeds = []
for start, end in allSeedsIntervals:
  for i in range(start, end+1, 1):
    interestingInputSeeds.append(i)

# Map interesting input seeds to final values and take min
output = [finalSeeds[i] for i in interestingInputSeeds]
print(min(output))