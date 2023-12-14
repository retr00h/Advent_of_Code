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
 */

import java.io.FileInputStream;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Gear_Ratios {
    public static void partOne() {
        // Symbol in position i * charsPerRow + offset -> numbers that "touch" 8-neighbors are to be considered
        try {
            Scanner sc = new Scanner(new FileInputStream("./2023/3_Gear_Ratios/input/3_Gear_Ratios.txt"));
            String data = "";
            int lineLength = -1;
            while (sc.hasNextLine()) {
                data += sc.nextLine();
                if (lineLength == -1) lineLength = data.length();
            }
            String tmp = data.replaceAll("[0-9.]+", "");
            Set<Character> symbols = new HashSet<Character>();
            List<Integer> positions = new ArrayList<Integer>();
            for (int i = 0; i < tmp.length(); i++) symbols.add(tmp.charAt(i));
            for (int i = 0; i < data.length(); i++) {
                if (symbols.contains(data.charAt(i))) {
                    positions.add(i);
                }
            }

            Pattern pattern = Pattern.compile("[0-9]+", Pattern.CASE_INSENSITIVE);
            Matcher matcher = pattern.matcher(data);

            int result = 0;
            while (matcher.find()) {
                int start = matcher.start();
                int end = matcher.end();
                boolean isNeighbor = false;

                int row = start / lineLength;
                int colStart = start % lineLength;
                int colEnd = end % lineLength;

                for (int pos : positions) {
                    int x = pos / lineLength;
                    int y = pos % lineLength;
                    if (x == row || x == row - 1 || x == row + 1) {
                        if (y >= colStart - 1 && y <= colEnd + 1) {
                            isNeighbor = true;
                            break;
                        }
                    }
                }

                if (isNeighbor) result += Integer.parseInt(matcher.group(0));
            }
            System.out.println(result);
        } catch (Exception ignored) {}
    }
    public static void main(String[] args) {
        partOne();
    }
}