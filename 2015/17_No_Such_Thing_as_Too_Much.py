# --- Day 17: No Such Thing as Too Much ---
#
#
# The elves bought too much eggnog again - 150 liters this time. To fit it
# all into your refrigerator, you'll need to move it into smaller containers.
# You take an inventory of the capacities of the available containers.
#
# For example, suppose you have containers of size 20, 15, 10, 5, and 5
# liters. If you need to store 25 liters, there are four ways to do it:
#  - 15 and 10
#  - 20 and 5 (the first 5)
#  - 20 and 5 (the second 5)
#  - 15, 5 and 5
#
# Filling all containers entirely, how many different combinations of
# containers can exactly fit all 150 liters of eggnog?

from os import path
import sys
from itertools import combinations

containers = list[int]()

with open(path.join(sys.path[0], "input\\17_No_Such_Thing_as_Too_Much.txt")) as f:
  for line in f:
    line = line.strip()
    containers.append(int(line))

def partOne(containers: list[int], liters: int) -> int:
  containerList, res = [], 0
  for i in range(1, len(containers)):
    for t in combinations(containers, i):
      containerList.append(t)
  
  for l in containerList:
    if (sum(l) == liters): res += 1
  return res

print("Part One: " + str(partOne(containers, 150))) # 4372


# --- Part Two ---
#
#
# While playing with all the containers in the kitchen, another load
# of eggnog arrives! The shipping and receiving department is requesting as many
# containers as you can spare.
#
# Find the minimum number of containers that can exactly fit all 150 liters
# of eggnog. How many different ways can you fill that number of containers
# and still hold exactly 150 litres?
#
# In the example above, the minimum number of containers was two. There were
# three ways to use that many containers, and so the answer there would be 3.

from itertools import permutations

def partTwo(containers: list[int], liters: int) -> int:
  containerList, min, t = [], None, None
  for i in range(1, len(containers)):
    for t in combinations(containers, i):
      containerList.append(t)
  
  for l in containerList:
    provisionalMin: int
    if (sum(l) == liters):
      provisionalMin = len(l)
      if (min == None or provisionalMin < min):
        min = provisionalMin
        t = l
  res = 0
  for p in permutations(t): res += 1
  return res

print("Part Two: " + str(partTwo(containers, 150))) # 24