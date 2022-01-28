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
#include <tuple>

using namespace std;

class Room {
  private:
    string encryptedName;
    int sectorID;
    string checksum;

    static string removeCharacter(string &s, char &c) {
      string newS;
      for (char ch : s) if (ch != c) newS += ch;
      return newS;
    }

    static tuple<char*, int*, int> findMCandOcc(string s) {
      /*
       * this method creates:
       *  - an array containing the characters that appear in s, ordered from the most common to the least one
       *  - an array contaiing the occurrences of each character (same order as the other array)
       *  - the size of the arrays (it's the same)
       */
      int n = 0;
      string foundLetters = "";
      for (char c : s) {
        if (foundLetters.find(c) == string::npos) {
          foundLetters += c;
          n++;
        }
      }
      char* mostCommon = static_cast<char*>(malloc(n * sizeof(char)));
      int* occurrences = static_cast<int*>(malloc(n * sizeof(int)));

      for (int i = 0; i < n; i++) {
        char c;
        int maxOccurrences = 0;
        for (int j = 0; j < s.length(); j++) {
          int occ = 0;
          for (int k = 0; k < s.length(); k++) {
            if (s[j] == s[k]) occ++;
          }
          if (occ > maxOccurrences) {
            maxOccurrences = occ;
            c = s[j];
          }
        }
        mostCommon[i] = c;
        occurrences[i] = maxOccurrences;
        s = removeCharacter(s, c);
      }

      return tuple<char*, int*, int>(mostCommon, occurrences, n);
    }

  public:
    Room(const string &encName, const int &id, const string &chksm) {
      for (char c : encName) if (c != '-') encryptedName += c;
      sectorID = id;
      checksum = chksm;
    }
    int getSectorID() const { return sectorID; }

    static string findNextChars(const char *mostCommon, const int *occurrences, int &counter, const int &size) {
      /*
       * find the next possible characters, for example let
       * mostCommon = ['a', 'b', 'z', 'y', 'x']
       * occurrences = [5, 3, 1, 1, 1]
       * counter = 2
       * size = 5
       *
       * the next characters that can be in the checksum are 'z', 'y', abd 'z', because they appear
       * the same number of times
       */
      string nextChars = "";
      nextChars += mostCommon[counter];
      int lastOccurrence = occurrences[counter++];
      while (counter < size and lastOccurrence == occurrences[counter]) nextChars += mostCommon[counter++];
      return nextChars;
    }

    static string remove(const string &s, const char &c) {
      // removes character c from string s
      string newS = "";
      for (char ch : s) if (ch != c) newS += ch;
      return newS;
    }

    bool isReal() const {
      bool real = true;
      tuple<char*, int*, int> t = findMCandOcc(encryptedName);
      char* mostCommon = get<0>(t);
      int* occurrences = get<1>(t);
      int size = get<2>(t);

      /*
       * variables used to remember what's the next character of the checksum
       * to be checked and what's the next character of mostCommon (and occurrences)
       */
      int checksumCounter = 0, occurrencesCounter = 0;

      while (real and checksumCounter < 5 and occurrencesCounter < size) {
        /*
         * while the string is not invalid (yet or at all), find the next possible characters
         *
         * if only one character is found, check if it is the next one in the checksum
         * if it is the next one, increment checksumCounter, else break and return false
         *
         * if more than one character are found, check if any of them is the next checksum character
         * until either there are no more characters to check or the checksum is complete
         * everytime a character is in possibleNextChars and is the next checksum character, remove it
         * from possibleNextChars
         * if the next character of the checksum is not found in the possible next characters, break and
         * return false
         */
        string possibleNextChars = findNextChars(mostCommon, occurrences, occurrencesCounter, size);
        if (possibleNextChars.length() == 1) {
          if (possibleNextChars.find(checksum[checksumCounter]) == string::npos) {
            real = false;
            break;
          }
          checksumCounter++;
        } else {
          while (possibleNextChars.length() > 0 and checksumCounter < 5) {
            if (possibleNextChars.find(checksum[checksumCounter]) == string::npos) {
              real = false;
              break;
            } else {
              // if the character is found
              possibleNextChars = remove(possibleNextChars, checksum[checksumCounter++]);
            }
          }
        }
      }
      free(mostCommon);
      free(occurrences);
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

  cout << "Test: " << partOne(testRooms) << endl; // 1514
  cout << "Part One: " << partOne(rooms) << endl; // 173787
  return 0;
}