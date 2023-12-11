from collections import defaultdict
from collections import OrderedDict
import bisect

f = open("input2.txt", "r", newline='').read()
# f = open("test2.txt", "r").readlines()
# f = open("input2.txt", "r")

def inBetween(s1, s2):
  return f.split(s1)[1].split(s2)[0]

def parseCards():
  cards = f.split('\n')
  for (i, card) in enumerate(cards):
    cards[i] = card.split(': ')[1].split(' | ')
    cards[i][0] = set(cards[i][0].split())
    cards[i][1] = cards[i][1].split()

  return cards

def task1():
  total = 0
  cards = parseCards()
  for card in cards:
    print(card)
    matches = -1
    for val in card[1]:
      if val in card[0]:
        matches += 1
    if matches >= 0:
      total += (pow(2, matches))
  return total

def task2():
  total = 0
  cards = parseCards()
  cardCounts = [1 for _ in range(len(cards))]
  for (cardInd, card) in enumerate(cards):
    total += cardCounts[cardInd]
    matches = 0
    for val in card[1]:
      if val in card[0]:
        matches += 1
    for i in range(matches):
      cardCounts[cardInd + i + 1] += cardCounts[cardInd]
      
  return total

# print(task1())
print(task2())