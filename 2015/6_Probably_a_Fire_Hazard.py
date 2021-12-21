# --- Day 6: Probably a Fire Hazard ---
#
#
# Because your neighbors keep defeating you in the holiday house decorating
# contest year after year, you've decided to deploy one million lights in a
# 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has
# mailed you instructions on how to display the ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the
# lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
# instructions include whether to turn on, turn off, or toggle various
# inclusive ranges given as coordinate pairs. Each coordinate pair represents
# opposite corners of a rectangle, inclusive; a coordinate pair like
# 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights
# all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your
# lights by doing the instructions Santa sent you in order.
#
# For example:
#  - turn on 0,0 through 999,999 would turn on (or leave on) every light.
#  - toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
#  turning off the ones that were on and turning on the ones that were
#  off.
#  - turn off 499,499 through 500,500 would turn off (or leave off) the
#  middle four lights.
#
# After following instructions, how many lights are lit?

from os import path
import sys

instructions = list[str]()
startCoords = list[(int, int)]()
endCoords = list[(int, int)]()

with open(path.join(sys.path[0], "input\\6_Probably_a_Fire_Hazard.txt")) as f:

  def findCoords(l):
    startX, startY = int(l[0].split(',')[0]), int(l[0].split(',')[1])
    startCoords.append((startX, startY))
    endX, endY = int(l[1].split(',')[0]), int(l[1].split(',')[1])
    endCoords.append((endX, endY))

  for line in f:
    line = line.strip()
    if (line.startswith("turn on")):
      l = line[8:].split(" through ")
      instructions.append("on")
      findCoords(l)
    elif (line.startswith("turn off")):
      l = line[9:].split(" through ")
      instructions.append("off")
      findCoords(l)
    else:
      l = line[7:].split(" through ")
      instructions.append("tog")
      findCoords(l)

def partOne(instructions: list[str], startCoords: list[(int, int)], endCoords: list[(int, int)]) -> int:
  mat = list[list[bool]]()
  for i in range(0, 1000):
    row = list[bool]()
    for j in range(0, 1000):
      row.append(False)
    mat.append(row)

  for k in range(0, len(instructions)):
    instruction = instructions[k]
    if (instruction == "on"):
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          mat[i][j] = True
    elif (instruction == "off"):
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          mat[i][j] = False
    else:
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          mat[i][j] = not mat[i][j]
  
  return sum([row.count(True) for row in mat])

print("Part One: " + str(partOne(instructions, startCoords, endCoords))) # 569999


# --- Part Two ---
#
#
# You just finish implementing your winning light pattern when you realize
# you mistranslated Santa's message from Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each
# light can have a brightness of zero or more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness
# of those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness
# of those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of
# those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's
# instructions?
#
# For example:
#  - turn on 0,0 through 0,0 would increase the total brightness by 1.
#  toggle 0,0 through 999,999 would increase the total brightness by
#  2000000.

def partTwo(instructions: list[str], startCoords: list[(int, int)], endCoords: list[(int, int)]) -> int:
  mat = list[list[int]]()
  for i in range(0, 1000):
    row = list[int]()
    for j in range(0, 1000):
      row.append(0)
    mat.append(row)

  for k in range(0, len(instructions)):
    instruction = instructions[k]
    if (instruction == "on"):
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          mat[i][j] += 1
    elif (instruction == "off"):
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          if (mat[i][j] > 0): mat[i][j] -= 1
    else:
      for i in range(startCoords[k][0], endCoords[k][0] + 1):
        for j in range(startCoords[k][1], endCoords[k][1] + 1):
          mat[i][j] += 2
  
  return sum([sum(row) for row in mat])

print("Part Two: " + str(partTwo(instructions, startCoords, endCoords))) # 17836115