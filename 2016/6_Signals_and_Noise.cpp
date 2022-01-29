/*
 * --- Day 6: Signals and Noise ---
 *
 * Something is jamming your communications with Santa. Fortunately, your
 * signal is only partially jammed, and protocol in situations like this is to
 * switch to a simple repetition code (https://en.wikipedia.org/wiki/Repetition_code) to get the message through.
 *
 * In this model, the same message is sent repeatedly. You've recorded the
 * repeating message signal (your puzzle input), but the data seems quite
 * corrupted - almost too badly to recover. Almost.
 *
 * All you need to do is figure out which character is most frequent for each
 * position. For example, suppose you had recorded the following messages:
 *   eedadn
 *   drvtee
 *   eandsr
 *   raavrd
 *   atevrs
 *   tsrnev
 *   sdttsa
 *   rasrtv
 *   nssdts
 *   ntnada
 *   svetve
 *   tesnvt
 *   vntsnd
 *   vrdear
 *   dvrsen
 *   enarar
 *
 * The most common character in the first column is e; in teh second, a; in
 * the third, s, and so on. Combining these characters returns the error-
 * corrected message, easter.
 *
 * Given the recording in your puzzle input, what is the error-corrected
 * verison of the message being sent?
 *
 *
 * --- Part Two ---
 *
 * Of course, that would be the message - if you hadn't agreed to use a
 * modified repetition code instead.
 *
 * In this modified code, the sender instead transmits what looks like random
 * data, but for each character, the character they actually want to send is
 * slightly less likely than the others. Even after signal-jamming noise, you
 * can look at the letter distrubutions in each column and choose the least
 * common letter to reconstruct the original message.
 * In the above example, the least common character in the first column is a;
 * in the second, d, and so on. Repeating this process for the remaining
 * characters produces the original message, advent.
 *
 * Given the recording in your puzzle input and this new decoding methodology,
 * what is the original message that Santa is trying to send?
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void readInput(vector<string> &signals) {
  ifstream f("../2016/input/6_Signals_and_Noise.txt");
  string line;
  while (f >> line) {
    signals.emplace_back(line);
  }
}

string partOne(const vector<string> &signals) {
  string correctedSignal = "";
  for (int i = 0; i < signals[0].length(); i++) {
    int occurrences[26] = {0};
    for (const string& sig : signals) {
      int x = sig[i] - 'a';
      occurrences[x]++;
    }
    char c;
    int mostCommon = 0;
    for (int j = 0 ; j < 26; j++) {
      if (occurrences[j] > mostCommon) {
        mostCommon = occurrences[j];
        c = 'a' + j;
      }
    }
    correctedSignal += c;
  }
  return correctedSignal;
}

string partTwo(const vector<string> &signals) {
  string correctedSignal = "";
  for (int i = 0; i < signals[0].length(); i++) {
    int occurrences[26] = {0};
    for (const string& sig : signals) {
      int x = sig[i] - 'a';
      occurrences[x]++;
    }
    char c;
    int leastCommon = signals.size() + 1;
    for (int j = 0 ; j < 26; j++) {
      if (occurrences[j] != 0 and occurrences[j] < leastCommon) {
        leastCommon = occurrences[j];
        c = 'a' + j;
      }
    }
    correctedSignal += c;
  }
  return correctedSignal;
}

int main() {
  vector<string> signals{};
  readInput(signals);
  cout << "Part One: " << partOne(signals) << endl; // afwlyyyq
  cout << "Part Two: " << partTwo(signals) << endl; // bhkzekao
  return 0;
}