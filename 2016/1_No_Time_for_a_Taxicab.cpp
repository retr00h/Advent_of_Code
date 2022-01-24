/*
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and
the clock's oscillator is regulated by stars. Unfortunately, the stars have
been stolen... by the Easter Bunny. To save Christmas, Santa needs you to
retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get - the instructions on the
Easter Bunny Recruiting Document the Elves intercepted start here, and
nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence:
either turn left (L) or right (R) 90 degrees, then walk forward the given
number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so
you take a moment and work out the destination. Given that you can only
walk on the street grid of the city (https://en.wikipedia.org/wiki/Taxicab_geometry),
how far is the shortest path to the destination?

For example:
  - Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5
  blocks away.
  - R2, R2, R2 leaves you 2 blocks due South of your starting position,
  which is 2 blocks away.
  R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?
*/

#include <iostream>
#include <vector>
#include <fstream>

//#define debug = true

using namespace std;

class Move {
  private:
    int direction;
    int distance;
  public:
    Move(int dir, int dist) {
      direction = dir;
      distance = dist;
    }

    int getDirection() const {return direction;}
    int getDistance() const {return distance;}
};

void readInput(vector<Move> &moves) {
  /*
   * line: string variable used in the do-while loop to process the line that has been read
   * move: string value used to store the unprocessed move
   * distStr: string variable used to store a move's distance value
   * i: int variable used to store the index of the first ',' char found in the line variable
   */
  string line, move, distStr;
  int i;
  ifstream f("../2016/input/1_No_Time_for_a_Taxicab.txt");
  getline(f, line);

  /*
   * Find the first occurrence of ',', extract the move (from the start of the string to the i position),
   * store the distance value in the distStr variable, then update line (starting from i+2 because i+1 is the ' ' whitespace
   * so the first actual character of the next move is i+2), add the new move to the list, repeat.
   */
  do {
    i = line.find(',');
    move = line.substr(0, i);
    distStr = move.substr(1, move.size());
    line = line.substr(i + 2, line.length());
    moves.emplace_back(move[0] == 'R' ? 90 : -90, stoi(distStr));
  } while (i != string::npos);
  f.close();
}

int partOne(vector<Move> &moves) {
  int currentBearing = 0;
  int stepsN = 0, stepsS = 0, stepsW = 0, stepsE = 0;

  for (int i = 0; i < moves.size(); i++) {
    currentBearing += moves[i].getDirection();
    if (currentBearing == 360) currentBearing = 0;
    else if (currentBearing == -90) currentBearing = 270;
    #ifdef debug
      cout << moves[i].getDirection() << " " << moves[i].getDistance() << endl;
      cout << "Current Bearing: " << currentBearing << endl;
    #endif
    switch (currentBearing) {
      case 0: stepsN += moves[i].getDistance(); break;
      case 180: stepsS += moves[i].getDistance(); break;
      case 90: stepsE += moves[i].getDistance(); break;
      case 270: stepsW -= moves[i].getDistance(); break;
      default: break;
    }
    #ifdef debug
      cout << "Steps North: " << stepsN << endl;
      cout << "Steps South: " << stepsS << endl;
      cout << "Steps West: " << stepsW << endl;
      cout << "Steps East: " << stepsE << endl;
      cout << endl;
    #endif
  }

  return abs(stepsN - stepsS) + abs(stepsW - stepsE);
}

int main() {
  vector<Move> moves{};
  readInput(moves);

  #ifdef debug
    vector<Move> testMoves{};
    testMoves.emplace_back(Move(90, 2));
    testMoves.emplace_back(Move(-90, 3));
    int test1 = partOne(testMoves);
    cout << "Test 1: " << test1 << endl;

  testMoves = vector<Move>();
    testMoves.emplace_back(Move(90, 2));
    testMoves.emplace_back(Move(90, 2));
    testMoves.emplace_back(Move(90, 2));
    int test2 = partOne(testMoves);
    cout << "Test 2: " << test2 << endl;

    testMoves = vector<Move>();
    testMoves.emplace_back(Move(90, 5));
    testMoves.emplace_back(Move(-90, 5));
    testMoves.emplace_back(Move(90, 5));
    testMoves.emplace_back(Move(90, 3));
    int test3 = partOne(testMoves);
    cout << "Test 3: " << test3 << endl;
  #endif

  #ifndef debug
    cout << "Part One: " << partOne(moves) << endl;
  #endif
  return 0;
}