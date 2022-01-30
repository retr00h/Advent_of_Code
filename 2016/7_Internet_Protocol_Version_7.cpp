/*
 * --- Day 7: Internet Protocol Version 7 ---
 *
 * While snooping around the local network of EBHQ, you compile a list of
 * IP addresses (https://en.wikipedia.org/wiki/IP_address) (they're IPv7, of course; IPv6 (https://en.wikipedia.org/wiki/IPv6) is too much limited). You'd
 * like to figure out which IPs support TLS (transport-layer snooping).
 *
 * An IP supports TPS if it has an Autonomous Bridge Bypass Annotation, or
 * ABBA. An ABBA is any four-character sequence which consists of a pair of
 * two different characters followed by the reverse of that pair, such as xyyx
 * or abba. However, the IP must also not have an ABBA within any hypernet
 * sequences, which are contained by square brackets.
 *
 * For example:
 *  - abba[mnop]qrst supports TLS [abba outside square brackets).
 *  - abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
 *  even though xyyx is outside square brackets).
 *  - aaaa[qwer]tyui does not support tPS (aaaa is invalid; the interior
 *  characters must be different).
 *  - ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
 *  even though it's within a larger string).
 *
 * How many IPs in your puzzle input support TLS?
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Address {
  private:
    vector<string> brackets;
    vector<string> nonBrackets;
  public:
    Address(const vector<string> &br, const vector<string> &nonBr);
    vector<string> getBrackets() const { return brackets; }
    vector<string> getNonBrackets() const { return nonBrackets; }
};

Address::Address(const vector<string> &br, const vector<string> &nonBr) {
  brackets = br;
  nonBrackets = nonBr;
}

void readInput(vector<Address> &addresses) {
  ifstream f("../2016/input/7_Internet_Protocol_Version_7.txt");
  string line;

  while (f >> line) {
    vector<string> brackets{};
    vector<string> nonBrackets{};
    int start = 0;
    for (int i = 0; i < line.length(); i++) {
      if (line[i] == '[') {
        nonBrackets.emplace_back(line.substr(start, i));
        start = i + 1;
      } else if (line[i] == ']') {
        brackets.emplace_back(line.substr(start, i - 1));
        start = i + 1;
      } else if (i == line.length() - 1) {
        nonBrackets.emplace_back(line.substr(start));
      }
    }
    addresses.emplace_back(Address(brackets, nonBrackets));
  }
}

int partOne(const vector<Address> &addresses) {
  int counter = 0;
  for (const Address &address : addresses) {
    bool bracketsOk = false;
    bool nonBracketsOk = false;

    for (const string &bracket : address.getBrackets()) {
      for (int i = 0; i <= bracket.length() - 4; i++) {
        string s = bracket.substr(i, i+4);
        if (not (s[0] + s[1] == s[3] + s[2] and s[0] != s[1] and s[2] != s[3])) {
          bracketsOk = true;
          break;
        }
      }
      if (bracketsOk) break;
    }
    for (const string &nonBracket : address.getNonBrackets()) {
      for (int i = 0; i <= nonBracket.length() - 4; i++) {
        string s = nonBracket.substr(i, i+4);
        if (s[0] + s[1] == s[3] + s[2] and s[0] != s[1] and s[2] != s[3]) {
          nonBracketsOk = true;
          break;
        }
      }
      if (nonBracketsOk) break;
    }

    if (bracketsOk and nonBracketsOk) counter++;
  }
  return counter;
}

int main() {
  vector<Address> addresses{};
  vector<Address> test{};
  test.emplace_back(Address({"mnop"}, {"abba", "qrst"} ));
  test.emplace_back(Address({"bddb"}, {"abcd", "xyyx"}));
  test.emplace_back(Address({"qwer"}, {"aaaa", "tyui"}));
  test.emplace_back(Address({"asdfgh"}, {"ioxxoj", "zxcvbn"}));
  readInput(addresses);

  cout << "Part One: " << partOne(addresses) << endl;
  return 0;
}