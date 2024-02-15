/*
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the
gondola lift will take you up to the water source, but this is as far as he
can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the
engine, but nobody can figure out which one. If you can add up all the part
numbers in the engine schematic, it should be easy to work out which
part is missing.

The engine schematic (your puzzle input) consists of a visual
representation of the engine. There are lots of numbers and symbols you
don't really understand, but apparently any number adjacent to a symbol,
even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example schematic:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of
all the part numbers in the engine schematic?

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, yuo jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still
wrong? Fortunately, the gondola has a phone labeled "help", so you pick it
up and the engineers answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving
with the other. You're going so slowly that you haven't even left the
station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all
up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

In this schematic, there are two gears. The first is in the top left; it
has part numbers 467 and 35, so its gear ratio is 16345. The second gear is
in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not
a gear because it is only adjacent to one part number). Adding up all of
the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
*/

#include <iostream>
#include <fstream>
#include <regex>
#include <set>

class Position {
    private:
        static int lineLength;
        const int value;
        const int start;
        const int end;
    
    public:
        static void setLineLength(int l) {
            lineLength = l;
        }

        Position(int v, int s, int e) : value(v), start(s), end(e) {}

        int getValue() {
            return value;
        }
            
        int getStart() {
            return start;
        }

        int getEnd() {
            return end;
        }

        int getRow() {
            return start / lineLength;
        }

        int getStartCol() {
            return start % lineLength;
        }

        int getEndCol() {
            return end % lineLength;
        }

        bool isNeighbor(int row, int col) {
            if (row == getRow() || row == getRow() - 1 || row == getRow() + 1) {
                return col >= getStartCol() - 1 && col <= getEndCol() + 1;
            }
            return false;
        }

        bool isNeighbor(Position other) {
            return isNeighbor(other.getRow(), other.getStartCol());
        }

        bool operator!=(const Position other) {
            return !(this->start == other.start && this->end == other.end);
        }
};

int Position::lineLength = -1;

int partOne() {
    std::string mat = "", line;
    std::ifstream f;
    int lineLength = -1, result = 0;
    f.open("input/3_Gear_Ratios.txt");
    while (!f.eof()) {
        f >> line;
        if (lineLength == -1) lineLength = line.length();
        mat += line;
    }
    f.close();

    Position::setLineLength(lineLength);
    
    std::regex reDigits("\\d+");
    std::regex reSymbols("[^0-9.]+");
    std::sregex_iterator iterDigits(mat.begin(), mat.end(), reDigits);
    std::sregex_iterator iterSymbols(mat.begin(), mat.end(), reSymbols);
    std::sregex_iterator end;

    std::set<char> symbols;
    std::vector<Position> symbolsPositions;

    while (iterSymbols != end) {
        symbols.insert(mat[iterSymbols->position()]);
        symbolsPositions.emplace_back(Position(iterSymbols->str()[0], iterSymbols->position(), iterSymbols->position()));
        ++iterSymbols;
    }

    while (iterDigits != end) {
        int start = iterDigits->position(), end = start + iterDigits->length() - 1;
        bool isNeighbor = false;
        Position digitPos = Position(std::stoi(iterDigits->str()), start, end);
        for (Position pos : symbolsPositions) {
            if (digitPos.isNeighbor(pos)) {
                isNeighbor = true;
                break;
            }
        }
        if(isNeighbor) result += std::stoi(iterDigits->str());
        ++iterDigits;
    }
    return result;
}

int partTwo() {
    std::string mat = "", line;
    std::ifstream f;
    int lineLength = -1, result = 0;
    f.open("input/3_Gear_Ratios.txt");
    while (!f.eof()) {
        f >> line;
        if (lineLength == -1) lineLength = line.length();
        mat += line;
    }
    f.close();

    Position::setLineLength(lineLength);
    
    std::regex reDigits("\\d+");
    std::regex reSymbols("[*]+");
    std::sregex_iterator iterDigits(mat.begin(), mat.end(), reDigits);
    std::sregex_iterator iterSymbols(mat.begin(), mat.end(), reSymbols);
    std::sregex_iterator end;

    std::vector<Position> digitsPositions;

    while (iterDigits != end) {
        int start = iterDigits->position(), end = start + iterDigits->length() - 1;
        digitsPositions.emplace_back(Position(std::stoi(iterDigits->str()), start, end));
        ++iterDigits;
    }

    while (iterSymbols != end) {
        Position pos = Position(iterSymbols->str()[0], iterSymbols->position(), iterSymbols->position());
        bool neighborFound = false;
        for (Position p1 : digitsPositions) {
            if (neighborFound) break;
            for (Position p2 : digitsPositions) {
                if (p1 != p2 && p1.isNeighbor(pos) && p2.isNeighbor(pos)) {
                    neighborFound = true;
                    result += p1.getValue() * p2.getValue();
                    break;
                } 
            }
        }
        ++iterSymbols;
    }
    return result;
}

int main() {
    std::cout << "Part one: " << partOne() << std::endl;
    std::cout << "Part Two: " << partTwo() << std::endl;
    return 0;
}