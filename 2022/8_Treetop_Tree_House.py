# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid.
# The Elves explain that a previous expedition planted these trees as a reforestation effort.
# Now, they're curious if this would be a good location for a tree house (https://en.wikipedia.org/wiki/Tree_house).
#
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this,
# you need to count the number of trees that are visible from outside the grid when looking directly along a row
# or column.
#
# The Elves have already launched a quadcopter (https://en.wikipedia.org/wiki/Quadcopter) to generate
# a map with the height of each tree (your puzzle input). For example:
#
# 30373
# 25512
# 65332
# 33549
# 35390
#
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
#
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
#
# All of the trees around the edge of the grid are visible - since they are already on the edge, there are
# no trees to block the view. In this example, that only leaves the interior nine trees to consider:
#
# - The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since
#   other trees of height 5 are in the way.)
# - The top-middle 5 is visible from the top and right.
# - The top-right 1 is not visible from any direction; for it to be visible, there would need to only
#   be trees of height 0 between it and an edge.
# - The left-middle 5 is visible, but only from the right.
# - The center 3 is not visible from any direction; for it to be visible, there would need to be only
#   trees of at most height 2 between it and an edge.
# - The right-middle 3 is visible from the right.
# - In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
#
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible
# in this arrangement.
#
# Consider your map; how many trees are visible from outside the grid?

from os import path
import sys
from numpy import transpose, flip

tree_map = []
visible_map = []

with open(path.join(sys.path[0], "input\\8_Treetop_Tree_House.txt")) as f:
    for line in f:
        line = line.strip()
        tree_map.append([int(x) for x in line])
        visible_map.append([False for x in line])


def is_greater(el, l):
    for x in l:
        if el <= x:
            return False
    return True

def part_one(tree_map, visible_map):
    transposed_tree_map = transpose(tree_map)
    for i in range(0, len(tree_map)):
        for j in range(0, len(tree_map[0])):
            if i == 0 or i == len(tree_map) or j == 0 or j == len(tree_map[0]):
                visible_map[i][j] = True
            else:
                if is_greater(tree_map[i][j], tree_map[i][:j]):
                    visible_map[i][j] = True
                    continue
                if is_greater(tree_map[i][j], tree_map[i][j+1:]):
                    visible_map[i][j] = True
                    continue
                if is_greater(tree_map[i][j], transposed_tree_map[j][:i]):
                    visible_map[i][j] = True
                    continue
                if is_greater(tree_map[i][j], transposed_tree_map[j][i+1:]):
                    visible_map[i][j] = True
                    continue

    visible = 0
    for i in range(0, len(visible_map)):
        for j in range(0, len(visible_map[0])):
            if visible_map[i][j]:
                visible += 1
    return visible


print("Part One: " + str(part_one(tree_map, visible_map))) # 1679


# --- Part Two ---
#
#
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their
# tree house: they would like to be able to see a lot of trees.
#
# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if
# you reach an edge or at the first tree that is the same height or taller than the tree under consideration.
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)
#
# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree
# house has large eaves (https://en.wikipedia.org/wiki/Eaves) to keep it dry, so they wouldn't be able
# to see higher than the tree house anyway.
#
# In the example above, consider the middle 5 in the second row:
# - Looking up, its view is not blocked; it can see 1 tree (of height 3).
# - Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# - Looking right, its view is not blocked; it can see 2 trees.
# - Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height
#   5 that blocks its view).
#
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
# For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
#
# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
# - Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# - Looking left, its view is not blocked; it can see 2 trees.
# - Looking down, its view is also not blocked; it can see 1 tree.
# - Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
#
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
#
# Consider each tree on your map. What is the highest scenic score possible for any tree?

from math import prod

def score(val, dir):
    dist = 0
    for el in dir:
        if el < val:
            dist += 1
        elif el == val:
            dist += 1
            break
        else:
            break
    return dist


def part_two(tree_map):
    transposed_tree_map = transpose(tree_map)
    scenic_score = 0
    for i in range(0, len(tree_map)):
        for j in range(0, len(tree_map[0])):
            if i != 0 and j != 0 and i != len(tree_map) and j != len(tree_map[0]):
                left = tree_map[i][:j]
                right = tree_map[i][j+1:]
                up = transposed_tree_map[j][:i]
                down = transposed_tree_map[j][i+1:]
                left.reverse()
                up = flip(up)

                score_left = score(tree_map[i][j], left)
                score_right = score(tree_map[i][j], right)
                score_up = score(tree_map[i][j], up)
                score_down = score(tree_map[i][j], down)
                tree_score = score_left * score_right * score_up * score_down
                if tree_score > scenic_score:
                    scenic_score = tree_score
    return scenic_score


print("Part Two: " + str(part_two(tree_map))) # 536625
