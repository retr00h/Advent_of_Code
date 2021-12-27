# --- Day 8: Matchsticks ---
#
#
# Space on the sleigh is limited this year, and so Santa will be bringing his
# list as a digital copy. He needs to know how much space it will take up
# when stored.
#
# It is common in many programming languages to provide a way to escape
# special characters in strings. For example, C (https://en.wikipedia.org/wiki/Escape_sequences_in_C), JavaScript (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String), Perl (https://perldoc.perl.org/perlop#Quote-and-Quote-like-Operators), Python (https://docs.python.org/2.0/ref/strings.html),
# and even PHP (https://www.php.net/manual/en/language.types.string.php#language.types.string.syntax.double) handle special characters in very similar ways.
#
# However, it is important to realize the difference between the number of
# characters in the code representation of the string literal and the number
# of characters in the in-memory stirng itself.
#
# For example:
#  - "" is 2 characters of code (the two double quotes), but the string contains zero characters.
#  - "abc" is 5 characters of code, but 3 characters in the string data.
#  - "aaa\"aaa" is 10 characters of code, but the string itself contains
#  six "a" characters and a single, escaped quote character, for a total
#  of 7 characters in the string data.
#  -"\x27" is 6 characters of code, but the string itself contains just
#  one - an apostrophe ('), escaped using hexadecimal notation.
#
# Santa's list is a file that contains many double-quoted string literals,
# one on each line. The only escape sequences used are \\ (which represents a
# single backslash), \", which represents a lone double-quote character), and
# \x plus two hexadecimal characters (which represents a single character
# with that ASCII code).
#
# Disregarding the whitespace in the file, what is the number of characters
# of code for string literals minus the number of characters in memory for
# the values of the strings in total for the entire file?
#
# For example, given the four strings above, the total number of characters
# of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters
# in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

from os import path
import sys
import re

lines = list[str]()
charactersTest: list[int] = [
  24, 28, 9, 5, 23, 32, 23, 38, 22, 30, 37, 35, 32, 8, 32, 17, 10, 8, 18, 22, 25,
  10, 6, 20, 30, 16, 40, 35, 34, 31, 11, 31, 25, 21, 10, 32, 21, 24, 13, 20, 6, 21,
  9, 7, 25, 31, 4, 20, 33, 16, 21, 8, 26, 21, 24, ]
charactersInMemoryTest: list[int] = [
  22, 18, 7, 3, 18, 24, 20, 32, 16, 25, 32, 32, 28, 6, 25, 14, 8, 6, 16, 18, 20, 8,
  1, 18, 26, 14, 31, 31, 25, 27, 6, 23, 23, 15, 7, 25, 18, 20, 10, 16, 3, 14, 7, 5,
  17, 28, 2, 17, 27, 13, 19, 6, 19, 16, 19, ]
print(len(charactersTest))
print(len(charactersInMemoryTest))

with open(path.join(sys.path[0], "input\\8_Matchsticks.txt")) as f:
  for line in f:
    line = line.strip()
    lines.append(line)

def partOne(lines: list[str]) -> int:
  codeChars, memoryChars = 0, 0
  backslash, quote, hexChar = "\\\\", "\\\"", "\\\\x[a-f0-9]{2}"

  counter = 0
  codeCharsErrors, memoryCharsErrors = 0, 0
  for line in lines:
    backslashes = re.findall(backslash, line)
    quotes = re.findall(quote, line[1:-1])
    hexChars = re.findall(hexChar, line)
    lineLen = len(line)
    charsInMem = lineLen - 2 - len(quotes) - (3 * len(hexChars)) - int((len(backslashes) - len(quotes) - len(hexChars)) / 2)
    if (counter < len(charactersTest) and (charactersTest[counter] != lineLen or charactersInMemoryTest[counter] != charsInMem)):
      print("Line: " + line)
      print("Backslashes: " + str(backslashes))
      print("Quotes: " + str(quotes))
      print("HexChars: " + str(hexChars))
      print("Line length: " + str(lineLen))
      print("Characters in memory: " + str(charsInMem))
      print("Correct line length: " + str(charactersTest[counter]))
      print("Correct characters in memory: " + str(charactersInMemoryTest[counter]))
      print()
      if (charactersTest[counter] != lineLen): codeCharsErrors += 1
      else: memoryCharsErrors += 1
    codeChars += lineLen
    memoryChars += charsInMem
    counter += 1
  print("Code chars errors: " + str(codeCharsErrors * 100 / len(charactersTest)) + "%")
  print("Memory chars errors: " + str(memoryCharsErrors * 100 / len(charactersInMemoryTest)) + "%")
  return codeChars - memoryChars

print("Part One: " + str(partOne(lines)))