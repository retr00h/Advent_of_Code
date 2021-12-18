# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
#
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location,
# and then an elf at the North Pole calls him via radio and tells him where
# to move next. Moves are always exactly one house to the north (^), south (v
# ), east (>), or west (<). After each move, he delivers another present to
# the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a litlte off, and Santa ends up visiting some
# houses more than once. How many houses receive at least one present?
#
# For example:
#  - > delivers presents to 2 houses: one at the starting locations, and one
#  to the east.
#  - ^>v< delivers presents to 4 houses in a square, including twice to the
#  house at his starting/ending location.
#  - ^v^v^v^v^V delivers a bunch of presents to some very lucky children at
#  only 2 houses.

from os import path
import sys

movesList: list[chr] = []

with open(path.join(sys.path[0], "input\\3_Perfectly_Spherical_Houses_in_a_Vacuum.txt")) as f:
  for line in f:
    line = line.strip()
    for c in line:
      movesList.append(c)

def partOne(input: list[chr]) -> int:
  coords = set((0, 0))
  i, j = 0, 0

  for c in input:
    if (c == '<'): j -= 1
    elif (c == '>'): j += 1
    elif (c == '^'): i -= 1
    else: i += 1
    coords.add((i, j))
  
  return len(coords)

print("Part One: " + str(partOne(movesList))) # 2592


# --- Part Two ---
#
#
# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to
# the same starting house), then take turns moving based on instructions from
# the elf, who is eggnoggedly reading from the same script as the previous
# year.
#
# This year, how many houses receive at least one present?

# For example:
#  - ^v delivers presents to 3 houses, because Santa goes north, and then
#  Robo-Santa goes south.
#  - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end
#  up back where they started.
# - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
# direction and Robo-Santa going the other.

def partTwo(input: list[chr]) -> int:
  coords = set()
  coords.add((0, 0))
  # I don't know why but the algorithm doesn't work correctly when coords = set((0, 0))

  i, j = 0, 0
  rI, rJ = 0, 0

  for k in range(0, len(input)):
    c = input[k]
    santa = k % 2 == 0

    if (c == '<'):
      if (santa): j -= 1
      else: rJ -= 1
    elif (c == '>'):
      if (santa): j += 1
      else: rJ += 1
    elif (c == '^'):
      if(santa): i -= 1
      else: rI -= 1
    else:
      if(santa): i += 1
      else: rI += 1

    if (santa):
      coords.add((i, j))
    else:
      coords.add((rI, rJ))

  return len(coords)

print("Part Two: " + str(partTwo(movesList))) # 2360