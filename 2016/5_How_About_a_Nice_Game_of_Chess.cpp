/*
 * --- Day 5: How About a Nice Game of Chess? ---
 *
 * You are faced with a security door designed by Easter Bunny engineers that
 * seem to have acquired most of their sceurity knowledge by watching hacking
 * movies (https://en.wikipedia.org/wiki/WarGames).
 *
 * The eight-character password for the door is generated one character at a
 * time by finding the MD5 (https://en.wikipedia.org/wiki/MD5) hash of some Door ID (your puzzle input) and an
 * increasing integer index (starting with 0).
 *
 * A hash indicates the next character in the password if its hexadecimal (https://en.wikipedia.org/wiki/Hexadecimal)
 * representation starts with five zeroes. If it does, the sixth character in
 * the hash is the next character of the password.
 *
 * For example, if the Door ID is abc:
 *  - The first index which produces a hash that starts with five zeroes is
 *  3231929, which we find by hashing abc3231929; the sixth character of
 *  the hash, and thus the first character of the password, is 1.
 *  - 5017308 produces the next interesting hash, which starts with
 *  000008f82...,, so the second character of the password is 8.
 *  - The third time a hahs starts with five zeroes is abc5278568,
 *  discovering the character f.
 *
 * In this example, after continuing this search for a total of eight times, the
 * password is 18f47a30.
 *
 * Given the actual Door ID, what is the password?
 *
 * Your puzzle input is abbhdwsy.
 *
 *
 * --- Part Two ---
 *
 * As the door slides open, you are presented with a second door that uses a
 * slightly more inspired security mechanism. Clearly unimpressed by the last
 * version (in what move is the password decrypted in order?!), the Easter
 * Bunny engineers have worked out a better solution (https://www.youtube.com/watch?v=NHWjlCaIrQo&t=25).
 *
 * Instead of simply filling in the password from left to right, the hash now
 * also indicates the position within the password to fill. You still look for
 * hashes that begin with five zeroes; however, now, the sixth character
 * represents the position (0-7), and the seventh character is the character
 * to put in that position.
 *
 * A hash result of 000001f means that f is the second character in the
 * password. Use only the first result for each position, and ignore invalid
 * positions.
 *
 * For example, if the Door ID is abc:
 *  - The first interesting hash is from abc3231929, which produces
 *  0000015...; so, 5 goes in possition 1: _5______.
 *  - In the previous method, 5017308 produced an interesting hash; however,
 *  it is ignored, because it specifies an invalid position (8).
 *  - The second interesting hash is at index 5357525, which produces
 *  000004e...; so, e goes in position 4: _5__e___.
 *
 * You almost choke on your popcorn as the final characters falls into place,
 * producing the password 05ace8e3.
 *
 * Given the actual Door ID and this new method, what is the password? Be
 * extra proud of your solution if it uses a cinematic "decrypting" animation.
 */

#include <iostream>
#include "md5.h"
#include <chrono>
#include <algorithm>

using namespace std;

string partOne(const string &input) {
  int index = 0;
  string next, hash, password;
  while (password.length() != 8) {
    do {
      next = input + std::to_string(index++);
      hash = md5(next);
    } while (hash.find("00000") != 0);
    password += hash[5];
  }
  return password;
}

string replace(const string &s, const char &c, const int &pos) {
  string newS = "";
  for (int i = 0; i < s.length(); i++) {
    if (i == pos) newS += c;
    else newS += s[i];
  }
  return newS;
}

void partTwo(const string &input) {
  int index = 0;
  string next, hash, password = "________";
  while (!all_of(password.begin(), password.end(), [](char c) -> bool {return c != '_';})) {
    do {
      next = input + to_string(index++);
      hash = md5(next);
    } while (hash.find("00000") != 0);
    int pos = hash[5] - '0';
    if (pos >= 0 and pos <= 7 and password[pos] == '_') {
      password = replace(password, hash[6], pos);
      cout << password << endl;
    }
  }
}

int main() {
  string input = "abbhdwsy";
  auto begin = chrono::high_resolution_clock::now();
  cout << "Part One: " << partOne(input); // b42f1987
  auto end = chrono::high_resolution_clock::now();
  auto elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
  cout << " in " << elapsed.count() * 1e-9 << " seconds." << endl;

  begin = chrono::high_resolution_clock::now();
  partTwo(input); // 424a0197
  end = chrono::high_resolution_clock::now();
  elapsed = chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
  cout << "Part Two completed in " << elapsed.count() * 1e-9 << " seconds." << endl;

  return 0;
}