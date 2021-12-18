# --- Day 2: I Was Told There Would Be No Math ---
#
#
# The elves are running low on wrapping paper, and so they need to submit an
# order for more. They have a list of the dimension (length l, width w, and
# height h) of each present, and only want to order exactly as much as they
# need.
#
# Fortunately, every present is a box (a perfect right rectangular prism (https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid)),
# which makes calculating the required wrapping paper for each gift a little
# easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
# The elves also need a little extra paper for each present: the area of the
# smallest side.
#
# For example:
#  - A present with dimensions 2x3x4 requires 2x6 + 2x12 + 2x8 = 52 square
#  feet of wrapping paper plus 6 square feet of slack, for a total of 58
#  square  feet.
#  - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42
#  square feet of wrapping paper plus 1 square foot of slack, for a total
#  of 43 square feet.
#
# All numbers in the elves' list are in feet. How many total square feet of
# wrapping paper should they order?

from os import path
import sys

lList: list[int] = []
wList: list[int] = []
hList: list[int] = []

with open(path.join(sys.path[0], "input\\2_I_Was_Told_There_Would_Be_No_Math.txt")) as f:
  for line in f:
    line = line.strip()
    x = line.split('x')
    l, w, h = int(x[0]), int(x[1]), int(x[2])
    lList.append(l)
    wList.append(w)
    hList.append(h)

def partOne(inputL: list[int], inputW: list[int], inputH: list[int]) -> int:
  res = 0
  for i in range(0, len(inputL)):
    l, w, h = inputL[i], inputW[i], inputH[i]
    lw = l * w
    wh = w * h
    hl = h * l
    res += (2 * (lw + wh + hl)) + min(lw, wh, hl)
  
  return res

print("Part One: " + str(partOne(lList, wList, hList))) # 1606483


# --- Part Two ---
#
#
# The elves are also running low on ribbon. Ribbon is all the same width, so
# they only have to worry about the length they need to order, which they
# would again like to be exact.
#
# The ribbon required to wrap a present is the shortest distance around its
# sides, or the smallest perimeter of any one face. Each present also
# requires a bow made out of ribbon as well; the feet of ribbon required for
# the perfect bow is equal to the cubic feet of volume of the present. Don't
# ask how they tie the bow, though; they'll never tell.
#
# For example:
#  - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon
#  to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a
#  total of 34 feet.
#  - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon
#  to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a
#  total of 14 feet.
#
# How many feet of ribbon should they order?

def partTwo(inputL: list[int], inputW: list[int], inputH: list[int]) -> int:

  def findPerimeter(l: int, w: int, h: int) -> int:
    lw = 2 * (l + w)
    wh = 2 * (w + h)
    hl = 2 * (h + l)

    return min(lw, wh, hl)

  res = 0
  for i in range(0, len(inputL)):
    l, w, h = inputL[i], inputH[i], inputW[i]
    perimeter = findPerimeter(l, w, h)
    bow = l * w * h
    res += perimeter + bow
  
  return res

print("Part Two: " + str(partTwo(lList, wList, hList))) # 3842356