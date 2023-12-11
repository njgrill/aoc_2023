# f = open("test1.txt", "r").readlines()
# f = open("input1.txt", "r")
# f = open("test2.txt", "r")
f = open("input2.txt", "r")

def parse_line(line):
  line = line.strip('\n')
  line = line.split(": ")[1]
  lines = line.split("; ")
  counts = {"blue" : 0, "red" : 0, "green" : 0}
  newLines = []
  for l in lines:
    spl = l.split(", ")
    newSpl = []
    for a in spl:
      newSpl.append(a.split(" "))
    newLines.append(newSpl)
  for draw in newLines:
    for color in draw:
      counts[color[1]] = max(int(color[0]), counts[color[1]])
  return (counts["blue"] * counts["red"] * counts["green"])

ans = 0
for (i, line) in enumerate(f):
  ans += parse_line(line)

print(ans)