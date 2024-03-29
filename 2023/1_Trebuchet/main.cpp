/*
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to
take a look. The Elves have even given you a map; on it, they've used stars
to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations,
you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful
enough") and where they're even sending you ("the sky") and why your map
looks mostly blank ("you sure ask a lot of questions") and hang on did you
just say the sky ("of course, where do you think snow comes from") when you
realize that the Elves are already loading you into a trebuchet ("please
hold still, we need to strap you in").

As they're making the final adjustments, they discover that their
calibration document (your puzzle input) has been amended by a very young
Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the
document.

The newly-improved calibration document consists of lines of text; each
line originally contained a specific calibration value that the Elves now
need to recover. On each line, the calibration value can be found by
combining the first digit and the last digit (in that order) to form a
single two-digit number.

For example:
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15,
and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the
calibration values?

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six,
seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
*/

#undef TEST
// #define TEST

#include <iostream>
#include <fstream>

int partOne() {
    int sum = 0;
    std::string line;
    std::ifstream f;
    f.open("input/1_Trebuchet.txt");
    while (!f.eof()) {
        int first = -1, last = -1;
        f >> line;
        for (int i = 0; i < line.length(); i++) {
            char c1 = line[i] - '0', c2 = line[line.length() - 1 - i] - '0';
            if (first == -1 && c1 >= 0 && c1 <= 9) {
                first = 10 * c1;
            }
            if (last == -1 && c2 >= 0 && c2 <= 9) {
                last = c2;
            }
            if (first != -1 && last != -1) break;
        }
        sum += (first + last);
    }
    f.close();
    return sum;
}

int partTwo() {
    static std::string conv[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int sum = 0;
    std::string line;
    std::ifstream f;
    size_t pos;
    f.open("input/1_Trebuchet.txt");
    while (!f.eof()) {
        int first = -1, last = -1;
        std::string tmp, correctLine = "";
        f >> line;
        
        for (int i = 0; i < line.length(); i++) {
            if (isalpha(line[i])) {
                for (int j = 0; j < 3; j++) {
                    tmp = line.substr(i, 3 + j);
                    for (int k = 0; k < 9; k++) {
                        if (tmp == conv[k]) {
                            correctLine += std::to_string(k + 1);
                            break;
                        }
                    }
                }
            } else {
                correctLine += line[i];
            }
        }
        
        for (int i = 0; i < correctLine.length(); i++) {
            char c1 = correctLine[i] - '0', c2 = correctLine[correctLine.length() - 1 - i] - '0';
            if (first == -1 && c1 >= 0 && c1 <= 9) {
                first = 10 * c1;
            }
            if (last == -1 && c2 >= 0 && c2 <= 9) {
                last = c2;
            }
            if (first != -1 && last != -1) break;
        }
        sum += (first + last);
    }
    f.close();
    return sum;
}

int main() {
    std::cout << "Part one: " << partOne() << std::endl;
    std::cout << "Part two: " << partTwo() << std::endl;
    return 0;
}