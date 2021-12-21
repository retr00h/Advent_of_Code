# --- Day 7: Some Assembly Required ---
#
#
# This year, Santa brought little Bobby Tables a set of wires and
# bitwise logic gates (https://en.wikipedia.org/wiki/Bitwise_operation)! Unfortunately, little Bobby is a little under the
# recommended age range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and carry a 16-bit (https://en.wikipedia.org/wiki/16-bit)
# signal (a number from 0 to 65535). A signal is probided to each wire by a
# gate, another wire, or some specific value. Each wire can only get a signal
# from one source, but can provide its signal to multiple destinations. A
# gate provides no signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts
# together: x AND y -> z means to connect wires x and y to an AND gate, and
# then connect its output to wire z.
#
# For example:
#  - 123 -> z means that the signal 123 is provided to wire x.
#  - x AND y -> z means that the bitwise AND (https://en.wikipedia.org/wiki/Bitwise_operation#AND) of wire x and wire y is
#  provided to wire z.
#  - p LSHIFT 2 -> q means that the value from wire p is left-shifted (https://en.wikipedia.org/wiki/Logical_shift) by 2
#  and then provided to wire q.
#  - NOT e -> f means that the bitwise complement (https://en.wikipedia.org/wiki/Bitwise_operation#NOT) of the value from wire e
#  is provided to wire f.
#
# Other possible gates include OR (bitwise OR (https://en.wikipedia.org/wiki/Bitwise_operation#OR)) and RSHIFT (right-shift (https://en.wikipedia.org/wiki/Logical_shift)). If,
# for some reason, you'd like to emulate the circuit instead, almost all
# programming languages (for example, C (https://en.wikipedia.org/wiki/Bitwise_operations_in_C), JavaScript (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators), or Python (https://wiki.python.org/moin/BitwiseOperators)) provide
# operators for these gates.
#
# For example, here is a simple circuit:
#   123 -> x
#   456 -> y
#   x AND y -> d
#   x OR y -> e
#   x LSHIFT 2 -> f
#   y RSHIFT 2 -> g
#   NOT x -> h
#   NOT y -> i
#
# After it is run, these are the signals on the wires:
#   d: 72
#   e: 507
#   f: 492
#   g: 114
#   h: 65412
#   i: 65079
#   x: 123
#   y: 456
#
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

from os import access, path
import sys
from typing import Tuple

instructions = list[str]()

with open(path.join(sys.path[0], "input\\7_Some_Assembly_Required.txt")) as f:
  for line in f:
    line = line.strip()
    instructions.append(line)

def partOne(instructions: list[str]) -> int:

  # Extracts operands in an instructions
  def findOperands(instruction: str) -> Tuple[str, str]:
    if (instruction.startswith("NOT")): instruction = instruction[4:]
    operands = instruction.split(" -> ")
    return operands[0], operands[1]

  # Dictionary object used as memory
  memory = dict[str, int]()
  
  # Compute each instruction
  while (len(instructions) != 0):
    newInstructions = list[str]()
    for instruction in instructions:
      if (instruction.startswith("NOT")):
        operands = instruction[4:].split(" -> ")
        leftOperand = operands[0]
        targetRegister = operands[1]
        if (leftOperand.isdigit()): memory.update({targetRegister : 65535 - int(leftOperand)})
        else:
          if (leftOperand in memory): memory.update({targetRegister : 65535 - int(memory.get(leftOperand))})
          else: newInstructions.append(instruction)
      else:
        operands = instruction.split(" -> ")
        targetRegister = operands[1]
        operands = operands[0]
        if ("AND" in operands):
          operands = operands.split(" AND ")
          op1, op2 = operands[0], operands[1]
          if (op1.isdigit()):
            if (op2.isdigit()): memory.update({targetRegister : int(op1) & int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(op1) & memory.get(op2)})
            else: newInstructions.append(instruction)
          elif (op1 in memory):
            if (op2.isdigit()): memory.update({targetRegister : int(memory.get(op1)) & int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(memory.get(op1)) & int(memory.get(op2))})
            else: newInstructions.append(instruction)
          else: newInstructions.append(instruction)
        elif ("OR" in operands):
          operands = operands.split(" OR ")
          op1, op2 = operands[0], operands[1]
          if (op1.isdigit()):
            if (op2.isdigit()): memory.update({targetRegister : int(op1) | int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(op1) | memory.get(op2)})
            else: newInstructions.append(instruction)
          elif (op1 in memory):
            if (op2.isdigit()): memory.update({targetRegister : int(memory.get(op1)) | int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(memory.get(op1)) | int(memory.get(op2))})
            else: newInstructions.append(instruction)
          else: newInstructions.append(instruction)
        elif ("LSHIFT" in operands):
          operands = operands.split(" LSHIFT ")
          op1, op2 = operands[0], operands[1]
          if (op1.isdigit()):
            if (op2.isdigit()): memory.update({targetRegister : int(op1) << int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(op1) << memory.get(op2)})
            else: newInstructions.append(instruction)
          elif (op1 in memory):
            if (op2.isdigit()): memory.update({targetRegister : int(memory.get(op1)) << int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(memory.get(op1)) << int(memory.get(op2))})
            else: newInstructions.append(instruction)
          else: newInstructions.append(instruction)
        elif ("RSHIFT" in operands):
          operands = operands.split(" RSHIFT ")
          op1, op2 = operands[0], operands[1]
          if (op1.isdigit()):
            if (op2.isdigit()): memory.update({targetRegister : int(op1) >> int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(op1) >> memory.get(op2)})
            else: newInstructions.append(instruction)
          elif (op1 in memory):
            if (op2.isdigit()): memory.update({targetRegister : int(memory.get(op1)) >> int(op2)})
            elif (op2 in memory): memory.update({targetRegister : int(memory.get(op1)) >> int(memory.get(op2))})
            else: newInstructions.append(instruction)
          else: newInstructions.append(instruction)
        else:
          if (operands.isdigit()): memory.update({targetRegister : int(operands)})
          elif (operands in memory): memory.update({targetRegister : int(memory.get(operands))})
          else: newInstructions.append(instruction)
    instructions = newInstructions
  
  return memory

print("Part One: " + str(partOne(instructions).get("a"))) # 3176


# --- Part Two ---
#
#
# Now, take the signal you got on wire a, override wire b to that signal, and
# reset the other wires (including wire a). What new signal is ultimately
# provided to wire a?

from re import match

def partTwo(instructions: list[str]) -> int:
  for i in range(0, len(instructions)):
    if (instructions[i].find("-> b") + 4 == len(instructions[i])):
      instructions[i] = str(partOne(instructions).get("a")) + " -> b"
      break
  
  return partOne(instructions)

print("Part Two: " + str(partTwo(instructions).get("a"))) # 14710