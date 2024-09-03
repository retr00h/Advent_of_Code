/*
 * --- Day 1: Trebuchet?! ---
 *
 * Something is wrong with global snow production, and you've been selected to
 * take a look. The Elves have even given you a map; on it, they've used stars
 * to mark the top fifty locations that are likely to be having problems. 
 *
 * You've been doing this long enough to know that to restore snow operations,
 * you need to check all fifty stars by December 25th.
 *
 * Collect stars by solving puzzles. Two puzzles will be made available on
 * each day in the Advent calendar; the second puzzle is unlocked when you
 * complete the first. Each puzzle grants one star. Good luck!
 *
 * You try to ask why they can't just use a weather machine (https://adventofcode.com/2015/day/1) ("not powerful 
 * enough") and where they're even sending you ("the sky") and why your map
 * looks mostly blank ("you sure ask a lot of questions") and hang on did you
 * just say the sky ("of course, where do you think snow comes from") when you
 * realize that the Elves are already loading you into a trebuchet (https://en.wikipedia.org/wiki/Trebuchet) ("please
 * hold still, we need to strap you in").
 *
 * As they're making the final adjustments, they discover that their
 * calibration document (your puzzle input) has been amended by a very young
 * Elf who was apparently just excited to show off her art skills.
 * Consequently, the Elves are having trouble reading the values on the
 * document.
 *
 * The newly-improved calibration document consists of lines of text; each
 * line originally contained a specific calibration value that the Elves now
 * need to recover. On each line, the calibration value can be found by
 * combining the first digit and the last digit (in that order) to form a
 * single two-digit number.
 *
 * For example:
 *
 * 1abc2
 * par3stu8vwx
 * a1b2c3d4e5f
 * treb7chet
 *
 * In this example, the calibration values of these four lines are 12, 38, 15,
 * and 77. Adding these together produces 142.
 *
 * Consider your entire calibration document. What is the sum of all of the
 * calibration values?
 *
 */

using System.Text;

const string PATH = "C:\\Users\\fabio\\OneDrive\\Desktop\\Advent_of_Code\\2023\\input\\1_Trebuchet.txt";


StreamReader reader = new StreamReader(PATH);

List<string> lines = new List<String>();
while (!reader.EndOfStream) {
    lines.Add(reader.ReadLine());
}
reader.Close();


int partOne(List<string> input) {
    int sum = 0;
    foreach (string line in input) {
        int i = 0, j = line.Length - 1;
        while (!System.Char.IsNumber(line[i])) {
            i++;
        }
        while (!System.Char.IsNumber(line[j])) {
            j--;
        }
        int char1 = line[i] - '0';
        int char2 = line[j] - '0';
        sum += 10 * char1 + char2;
    }
    
    return sum;
}

Console.WriteLine("Part One: " + partOne(lines));

/*
 * --- Part Two ---
 *
 * Your calculation isn't quite right. It looks like some of the digits are
 * actually spelled out with letters: one, two, three, four, five, six, seven,
 * eight, and nine also count as vaild "digits".
 *
 * Equipped with this new information, you now need to find the real first and
 * last digit on each line. For example:
 *
 * two1nine
 * eightwothree
 * abcone2threexyz
 * xtwone3four
 * 4nineeightseven2
 * zoneight234
 * 7pqrstsixteen
 *
 * In this exmaple, the calibration vlaues are 29, 83, 13, 24, 42, 14, and 76.
 * Adding these together produces 281.
 *
 * What is the sum of all of the calibration values?
 *
 */

int partTwo(List<string> input) {
    string[] numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"];
    int sum = 0;
    foreach (string line in input) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < line.Length; i++) {
            if (System.Char.IsNumber(line[i])) {
                sb.Append(line[i]);
                continue;
            }
            for (int n = 0; n < numbers.Length; n++) {
                if (line.Substring(i).StartsWith(numbers[n])) {
                    sb.Append(n);
                    break;
                }
            }
        }
        string finalString = sb.ToString();

        int j = 0, k = finalString.Length - 1;
        while (!System.Char.IsNumber(finalString[j])) {
            j++;
        }
        while (!System.Char.IsNumber(finalString[k])) {
            k--;
        }
        int char1 = finalString[j] - '0';
        int char2 = finalString[k] - '0';
        sum += 10 * char1 + char2;
    }
    
    return sum;
}

Console.WriteLine("Part Two: " + partTwo(lines));

// one, two, six, ten, zero, four, five, nine, three, seven, eight