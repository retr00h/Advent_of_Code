/*
 * --- Day 3: Squares With Three Sides ---
 *
 * Now that you can think clearly, you move deeper into the labyrinth of
 * hallways and office furniture that makes up this part of Easter Bunny HQ.
 * Yhis must be a graphic design department; the walls are covered in
 * specifications for triangles.
 *
 * Or are they?
 *
 * The design document gives the side lengths of each triangle it describes,
 * but... 5 10 25? Some of these aren't triangles. You can't help but mark the
 * impossible ones.
 *
 * In a valid triangle, the sum of any two sides must be larger than the
 * remaining side. For example, the "triangle" given above is impossible,
 * because 5 + 10 is not larger than 25.
 *
 * In your puzzle input, how many of the listed triangles are possible?
 *
 *
 * --- Part Two ---
 *
 * Now that you've helpfully marked up their design documents, it occurs to
 * you that triangles are specified in groups of three vertically. Each set of
 * three numbers in a column specifies a triangle. Rows are unrelated.
 * For example, given  the following specification, numbers with the same
 * hundreds digit would be part of the same triangle:
 *   101 301 501
 *   102 302 502
 *   103 303 503
 *   201 401 601
 *   202 402 602
 *   203 403 603
 * In your puzzle input, and instead reading by columns, how many of the
 * listed triangles are possible?
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


vector<vector<int>> readInput() {
  vector<vector<int>> numbers{};
  ifstream f("../2016/input/3_Squares_With_Three_Sides.txt");
  int a, b, c;
  while (f >> a >> b >> c) {
    vector<int> arr = {a, b, c};
    numbers.emplace_back(arr);
  }
  f.close();
  return numbers;
}

int partOne(vector<vector<int>> numbers) {
  int counter = 0;
  for (int i = 0; i < numbers.size(); i++) {
    int a = numbers[i][0];
    int b = numbers[i][1];
    int c = numbers[i][2];

    if (a + b > c and a + c > b and b + c > a) ++counter;
  }
  return counter;
}

int partTwo(vector<vector<int>> numbers) {
  int counter = 0;
  for (int i = 0; i < numbers.size() - 2; i+= 3) {
    for (int j = 0; j < 3; j++) {
      int a = numbers[i][j];
      int b = numbers[i+1][j];
      int c = numbers[i+2][j];
      if (a + b > c and a + c > b and b + c > a) ++counter;
    }
  }
  return counter;
}

int main() {
  vector<vector<int>> numbers = readInput();
  cout << "Part One: " << partOne(numbers) << endl; // 1050
  cout << "Part Two: " << partTwo(numbers) << endl; // 1921
  return 0;
}