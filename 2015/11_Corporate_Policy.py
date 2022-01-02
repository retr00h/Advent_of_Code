# --- Day 11: Corporate Policy ---
#
#
# Santa's previous password expired, and he needs help choosing a new one.
#
# To help him remember his new password after the old one expires, Santa has
# devised a method of coming up with a password based on the previous one.
# Corporate policy dictates that passwords must be exactly eight lowercase
# letters (for security reasons), so he finds his new password by
# incrementing his old password string repeatedly until it is valid.
#
# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so
# on. Increase the rightmost letter one step; if it was z, it wraps around to
# a, and repeat with the next letter to the left until one doesn't wrap
# around.
#
# Unfortunately for Santa, a new Security-Elf recently started, and he has
# imposed some additional passwords requirements:
#  - Passwords must include one increasing straight of at least three
#  letters, like abc, bcd, cde, and so on, up to xyz. They kannot skip
#  letters; abd doesn't count.
#  - Passwords may not contain the letters i, o or l, as these letters can
#  be mistaken for other characters and are therefore confusing.
#  - Passwords must contain at least two different, non-overlapping pairs
#  of letters, like aa, bb, or zz.
#
# For example:
#  - hijklmmn meets the first requirement (because it contains the straight
#  hij) but fails the second requirement (because it contains i and l).
#  - abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
#  - abbcegjk fails the third requirement, because it only has one double letter (bb).
#  - The next password after abcdefgh is abcdffaa.
#  - The next password after ghijklmn is ghjaabcc, because you eventually
#  skip all the passwords that start with ghi..., since i is not allowed.
#
# Given Santa's current password (your puzzle input), what should his next password be?
#
# Your puzzle input is hepxcrrq.

password = "hepxcrrq"

def partOne(oldPassword: str) -> str:
  def incrementPassword(p: str) -> str:
    increments = {'a' : 'b', 'b' : 'c', 'c' : 'd', 'd' : 'e', 'e' : 'f', 'f' : 'g', 'g' : 'h',
      'h' : 'i', 'i' : 'j', 'j' : 'k', 'k' : 'l', 'l' : 'm', 'm' : 'n', 'n' : 'o', 'o' : 'p',
      'p' : 'q', 'q' : 'r', 'r' : 's', 's' : 't', 't' : 'u', 'u' : 'v', 'v' : 'w', 'w' : 'x',
      'x' : 'y', 'y' : 'z', 'z' : 'a'}
    newPassword = list(p)
    i = len(newPassword) - 1
    newPassword[i] = increments[newPassword[i]]
    j = i
    while (j > 0 and newPassword[j] == 'a'):
      newPassword[j - 1] = increments[newPassword[j - 1]]
      j -= 1
    p = ""
    for c in newPassword: p += c
    return p
  
  def criteria1(p: str):
    l = ["abc", "bcd", "cde", "def", "fgh", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]
    for crit in l:
      if (crit in p): return True
    return False
  
  def criteria2(p: str): return "i" not in p and "o" not in p and "l" not in p

  def criteria3(p: str):
    l = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "jj", "kk", "mm", "nn", "pp",
      "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy", "zz"]
    counter = 0
    for crit in l:
      if (crit in p):
        counter += 1
        if (counter == 2): return True
    return False
  
  newPassword = incrementPassword(oldPassword)
  while (not (criteria2(newPassword) and criteria1(newPassword) and criteria3(newPassword))):
    newPassword = incrementPassword(newPassword)
  return newPassword

print("Part One: " + str(partOne(password))) # hepxxyzz

# --- Part Two ---
#
#
# Santa's password expired again. What's the next one?

print("Part Two: " + str(partOne(partOne(password)))) # heqaabcc