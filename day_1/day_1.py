f = open("input1.txt", "r")

digits = set([str(i) for i in range(10)] + ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
digDict = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

total = 0
for line in f:
	min = 9999999
	minVal = ""
	for digit in digits:
		if (line.find(digit) >= 0 and line.find(digit) < min):
			min = line.find(digit)
			minVal = line[min:min+len(digit)]
	if len(minVal) == 1:
		total += 10 * int(minVal)
	else:
		total += 10 * digDict[minVal]

	max = -1
	maxVal = ""
	for digit in digits:
		for i in range(0, len(line)):
			if (line.find(digit, i) > max):
				max = line.find(digit, i)
				maxVal = line[max:max+len(digit)]
	if len(maxVal) == 1:
		total += int(maxVal)
	else:
		total += digDict[maxVal]
	# print(total)

print(total)
