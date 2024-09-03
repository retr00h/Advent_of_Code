/*
 * --- Day 2: Cube Conundrum ---
 *
 * You're launched high into the atmosphere! The apex of your trajectory just
 * barely reaches the surface of a large island floating in the sky. You
 * gently land in a fluffy pile of leaves. It's quite cold, but you don't see
 * much snow. An Elf runs over to greet you.
 *
 * The Elf explains that you've arrived at Snow Island and apologizes for the
 * lack of snow. He'll be hapyp to explain the situation, but it's a bit of a
 * walk, so you have some time. They don't get many visitors up here; would
 * you like to play a game in the meantime?
 *
 * As you walk, the Elf shows you a small bag and some cubes which are either
 * red, green, or blue. Each time you play this game, he will hide a secret
 * number of cubes of each color in the bag, and your goal is to figure out
 * information about the number of cubes.
 *
 * To get information, once a bag has been loaded with cubes, the Elf will
 * reach into the bag, grab a handful of random cubes, show them to you, and
 * then put them back in the bag. He'll do this a few times per game.
 *
 * You play several games and record the information from each game (your
 * puzzle input). Each game is listed with its ID nubmer (like the 11 in
 * Game 11: ...) followed by a semicolon-separated list of subsets of cubes
 * that were revealed from the bag (like 3 red, 5 green, 4 blue).
 *
 * For example, the record of a few games might look like this:
 *
 * Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
 * Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
 * Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
 * Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
 * Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
 *
 * In game 1, three sets of cubes are revealed from the bag (and then put back
 * again). The first set is 3 blue cubes and 4 red cubes; the second set is 1
 * red cube, 2 green cubes and 6 blue cubes; the third set is only 2 green
 * cubes.
 *
 * The Elf would first like to know which games would have been possible if
 * the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
 *
 * In the example above, games 1, 2, and 5 would have been possible if the bag
 * had been loaded with that configuration. However, game 3 would have been
 * impossible because at one point the Elf showed you 20 red cubes at once;
 * similarly, game 4 would also have been impossible because the Elf showed
 * you 15 blue cubes at once. If yuo add up the IDs of the games that would
 * have been possible, you get 8.
 *
 * Determine which games would have been possible if the bag had been loaded
 * with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
 * of the IDs of those games?
 *
 */

class Subset {
    private static int RED_CUBES = 12;
    private static int GREEN_CUBES = 13;
    private static int BLUE_CUBES = 14;
    
    private int red;
    private int green;
    private int blue;
    public Subset(int red, int green, int blue) {
        this.red = red;
        this.green = green;
        this.blue = blue;
    }
    public Subset(string description) {
        string[] cubes = description.Trim().Split(separator: ',');
        foreach (string c in cubes) {
            string[] quantityAndColor = c.Trim().Split(' ');
            int quantity = Int32.Parse(quantityAndColor[0]);
            switch (quantityAndColor[1].ToLower()) {
                case "red":
                    this.red = quantity;
                    break;
                case "green":
                    this.green = quantity;
                    break;
                case "blue":
                    this.blue = quantity;
                    break;               
            }
        }
    }

    public bool isValid() {
        return red <= RED_CUBES && green <= GREEN_CUBES && blue <= BLUE_CUBES;
    }
}

class Game {
    private int id;
    private Subset[] subsets;
    public Game(string description) {
        string[] idAndSubsets = description.Split(separator: ':');
        this.id = Int32.Parse(idAndSubsets[0].Trim().Split(' ')[1]);
        string[] subsets = idAndSubsets[1].Trim().Split(separator: ';');
        this.subsets = new Subset[subsets.Length];
        for (int i = 0; i < subsets.Length; i++) {
            this.subsets[i] = new Subset(description: subsets[i]);
        }
    }
    public bool isValid() {
        bool valid = true;
        foreach (Subset s in subsets) {
            if (!s.isValid()) {
                valid = false;
                break;
            }
        }
        return valid;
    }

    public int getId() {
        return id;
    }
}


public class Program {
    static int partOne(List<string> input) {
        int sum = 0;
        foreach (string line in input) {
            Game game = new Game(line);
            if (game.isValid()) sum += game.getId();
        }
        return sum;
    }
    static void Main() {
        const string PATH = "C:\\Users\\fabio\\OneDrive\\Desktop\\Advent_of_Code\\2023\\input\\2_Cube_Conundrum.txt";
        StreamReader reader = new StreamReader(PATH);

        List<string> lines = new List<string>();
        while (!reader.EndOfStream) {
            lines.Add(reader.ReadLine());
        }
        reader.Close();

        Console.WriteLine("Part One: " + partOne(lines));
    }
}
