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
*/

import java.io.FileInputStream;
import java.util.Scanner;

public class Trebuchet {
    static void partOne() {
        try {
            Scanner sc = new Scanner(new FileInputStream("./2023/1_Trebuchet/input/1_Trebuchet.txt"));
            String line;
            int result = 0;
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                line = line.replaceAll("[a-zA-Z]+", "");
                if (line.length() == 1) {
                    line += line.charAt(0);
                } else if (line.length() != 2) {
                    line = "" + line.charAt(0) + line.charAt(line.length() - 1);
                }
                result += Integer.parseInt(line);
            }
            System.out.println(result);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    static void partTwo() {
        try {
            Scanner sc = new Scanner(new FileInputStream("./2023/1_Trebuchet/input/1_Trebuchet.txt"));
            String line;
            int result = 0;
            String[] definitions = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
            String[] substitutions = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
            while (sc.hasNextLine()) {
                line = sc.nextLine();

                // For each definition, search it in the line, until no definition is found
                boolean finish = false;
                while (!finish) {
                    finish = true;
                    int[] posFound = {-1,-1,-1,-1,-1,-1,-1,-1,-1};
                    for (int i = 0; i < definitions.length; i++) {
                        int pos = line.indexOf(definitions[i]);
                        if (pos != -1) finish = false;
                        posFound[i] = pos;
                    }

                    // Find the earliest occurrence of a definition
                    int posToSubstitute = -1;
                    int minValue = Integer.MAX_VALUE;
                    for (int i = 0; i < posFound.length; i++) {
                        if (posFound[i] != -1 && posFound[i] < minValue) {
                            minValue = posFound[i];
                            posToSubstitute = i;
                        }
                    }
                    // Substitute
                    if (posToSubstitute != -1) {
                        line = line.replaceFirst(definitions[posToSubstitute], substitutions[posToSubstitute]);
                    }
                }

                line = line.replaceAll("[a-zA-Z]+", "");
                if (line.length() == 1) {
                    line += line.charAt(0);
                } else if (line.length() != 2) {
                    line = "" + line.charAt(0) + line.charAt(line.length() - 1);
                }
                result += Integer.parseInt(line);
            }
            System.out.println(result);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        partOne();
        partTwo();
    }
}
