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
 */

#include <iostream>
#include "md5.h"
#include <chrono>

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

int main() {
  string input = "abbhdwsy";
  auto begin = std::chrono::high_resolution_clock::now();
  cout << "Part One: " << partOne(input); // b42f1987
  auto end = std::chrono::high_resolution_clock::now();
  auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
  cout << " in " << elapsed.count() * 1e-9 << " seconds." << endl;


  return 0;
}