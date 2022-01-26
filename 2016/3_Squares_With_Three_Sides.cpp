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
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define debug true

void readInput(vector<vector<int>> numbers) {
  ifstream f("../2016/3_Squares_With_Three_Sides.txt");
  int a, b, c;
  while (f >> a >> b >> c) {
    vector<int> arr{a, b, c};
    numbers.emplace_back(arr);
  }
}

int partOne(vector<vector<int>> numbers) {
  int counter = 0;
  for (int i = 0; i < numbers.size(); i++) {
     int a = numbers[i][0];
     int b = numbers[i][1];
     int c = numbers[i][2];
    #ifdef debug
    cout << a << " " << b << " " << c << endl;
    #endif
     bool ok = true;
     if (a + b <= c) ok = false;
     else if (a + c <= b) ok = false;
     else if (b + c <= a) ok = false;
     if (ok) counter++;
  }
  return counter;
}

int main() {
  vector<vector<int>> numbers{};
  readInput(numbers);
  #ifdef debug
    vector<int> test{};
    test.emplace_back(5);
    test.emplace_back(10);
    test.emplace_back(25);
    vector<vector<int>> test2{};
    test2.emplace_back(test);
    cout << "Test: " << partOne(test2) << endl;
  #endif

  #ifndef debug
    cout << "Part One: " << partOne(numbers) << endl;
  #endif
  return 0;
}