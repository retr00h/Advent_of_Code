/*
 * --- Day 4: Security Through Obscurity ---
 *
 * Finally, you come across an information kiosk with a list of rooms. Of
 * course, the list is encrypted and full of decoy data, but the instructions
 * to decode the list are barely hidden nearby. Better remove the decoy data
 * first.
 *
 * Each room consists of an encrypted name (lowercase letters separated by
 * dashes) followed by a dash, a sector ID, and a checksum in square brackets.
 *
 * A room is real (not a decoy) if the checksum is the five most common
 * letters in the encrypted name, in order, with ties broken by
 * alphabetization. For example:
 *
 *  - aaa-bbb-z-y-x-123[abxyz] is a real room because the most common
 *  are a (5), b (3), and then a tie between x, y, and z, which
 *  are listed alphabetically.
 *  - a-b-c-d-e-f-g-h-987[abcde] is a real room because although all the letters
 *  are all tied (1 of each), the first five are listed alphabetically.
 *  - not-a-real-room-404[oarel] is a real room.
 *  - totally-real-room-200[decoy] is not.
 *
 * Of the real rooms from the list above, the sum of their sector IDs is 1514.
 *
 * What is the sum of the sector IDs of the real rooms?
 * */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Room {
  private:
    string encryptedName;
    int sectorID;
    string checksum;

    static char* findMostCommonOccurrences(const string &s) {
      string str = s;
      char* mostCommon = static_cast<char*>(malloc(5 * sizeof(char)));
      for (int i = 0; i < 5; i++) {
        int occ = 0;
        char mc;
        for (char a : str) {
          int o = 0;
          for (char b : str) if (a == b) o++;
          if (o > occ) {
            mc = a;
            occ = o;
          }
        }
        mostCommon[i] = mc;
        str = replace(str, mc);
      }
      return mostCommon;
    }


    static string replace(string &s, const char &c) {
      string newS;
      for (char ch : s) {
        if (ch != c) newS += ch;
      }
      return newS;
    }
  public:
    Room(const string &encName, const int &id, const string &chksm) {
      for (char c : encName) if (c != '-') encryptedName += c;
      sectorID = id;
      checksum = chksm;
    }
    int getSectorID() const { return sectorID; }

    bool isReal() const {
      for (char checksumChar : checksum) if (encryptedName.find(checksumChar) == string::npos) return false;

      string str = encryptedName;
      char* mostCommon = findMostCommonOccurrences(str);

      bool real = false;
      for (char c : checksum) for (int i = 0; i < 5; i++) if (c == mostCommon[i]) real = true;
      free(mostCommon);
      return real;
    }
};

vector<Room> readInput() {
  vector<Room> rooms{};
  string line;
  ifstream f("../2016/input/4_Security_Through_Obscurity.txt");

  while (f >> line) {
    int i = 0;
    while (!isdigit(line[i])) i++;
    int j = i;
    while (line[j] != '[') j++;

    string encName = line.substr(0, i-1);
    int secID = stoi(line.substr(i, j));
    string chksm = line.substr(j+1, line.size());

    rooms.emplace_back(Room(encName, secID, chksm.substr(0, chksm.size()-1)));
  }
  f.close();
  return rooms;
}

int partOne(const vector<Room> &rooms) {
  int sum = 0;
  for (const Room& room : rooms) {
    if (room.isReal()) sum += room.getSectorID();
  }
  return sum;
}

int main() {
  vector<Room> rooms = readInput();
  vector<Room> testRooms{};
  testRooms.emplace_back(Room("aaaaa-bbb-z-y-x", 123, "abxyz"));
  testRooms.emplace_back(Room("a-b-c-d-e-f-g-h", 987, "abcde"));
  testRooms.emplace_back(Room("not-a-real-room", 404, "oarel"));
  testRooms.emplace_back(Room("totally-real-room", 200, "decoy"));

  cout << "Test: " << partOne(testRooms) << endl;
  cout << "Part One: " << partOne(rooms) << endl; // 183904
  return 0;
}