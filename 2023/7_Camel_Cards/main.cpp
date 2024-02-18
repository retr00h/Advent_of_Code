/*
 * --- Part One ---
 * 
 * Your all-expenses-paid trip turns out to be a one-way, five-minute ride in
 * an airship (https://en.wikipedia.org/wiki/Airship). (At least it's a cool airship!)
 * It drops you off at the edge of a vast desert and descends back to Island Island.
 * 
 * "Did you bring the parts?"
 * 
 * You turn around to see an Elf completely covered in white clothing, wearing
 * goggles, and riding a large camel (https://en.wikipedia.org/wiki/Dromedary).
 * 
 * "Did you bring the parts?" she asks again, louder this time. You aren't
 * sure what parts she's looking for; you're here to figure out why the sand
 * stopped.
 * 
 * "The parts! For the sand, yes! Come with me; I wil show you" She beckons
 * you onto the camel.
 * 
 * After riding a bit across the sands of Desert Island, you can see what look
 * like very large rocks covering half of the horizon. The Elf explains that
 * the rocks are all along the part of Desert Island that is directly above
 * Island Island, making it hard to even get there. Normally, they use big
 * machines to move hte rocks and filter the sand, but hte machines have
 * broken down because Desert Island recently stopped receiving the parts they
 * need to fix the machines.
 * 
 * You've already assumed it'll be your job to figure out why the parts
 * stopped because when she asks if you can help. You agree automatically.
 * 
 * Because the journey will take a few days, she offers to teach you the game
 * of Camel Cards. Camel Cards is sort of similar to poker (https://en.wikipedia.org/wiki/List_of_poker_hands)
 * except it's designed to be easier to play while riding a camel.
 * 
 * In Camel Cards, you get a list of hands, and your goal is to order them
 * based on the strength of each hand. A hand consists of five cards labeled
 * one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of
 * each card follows this order, where A is the highest and 2 is the lowest.
 * 
 * Every hand is exactly one type. From strongest to weakest, they are:
 *  - Five of a kind, where all five cards have the same label: AAAAA
 *  - Four of a kind, where four cards have the same label and one card has
 *    a different label: AA8AA
 *  - Full house, where three cards have the same label, and the remaining
 *    two cards share a different label: 23332
 *  - Three of a kind, where three cards have the same label, and the
 *    remaining two cards are each different from any other card in the
 *    hand: TTT98
 *  - Two pair, where two cards share one label, two other cards share a
 *    second label, and the remaining card has a third label: 23432
 *  - One pair, where two cards share one label, and the other three cards
 *    have a different label from the pair and each other: A23A4
 *  - High card, where all cards' labels are distinct: 23456
 * 
 * Hands are primarily ordered based on type; for example, every full house is
 * stronger than any three of a kind.
 * 
 * If two hands have the same type, a second ordering rule takes effect. Start
 * by comparing hte first card in each hand. If these cards are different, the
 * hand with the stronger first card is considered stronger. If hte first card
 * in each hand have the same label, however, then move on to considering the
 * second card in each hand. If they differ, the hand with the higher second
 * card wins; otherwise, continue with the thrid carc in each hand, then the
 * fourth, then the fifth.
 * 
 * So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger
 * because its first card is stronger. Similarly, 77888 and 77788 are both a
 * full house, but 77888 is stronger because its third card is stronger (and
 * both hands have the same first and second card).
 * 
 * To play Camel Cards, you are given a list of hands and their corresponding
 * bid (your puzzle input). For example:
 *    32T3K 765
 *    T55J5 684
 *    KK677 28
 *    KTJJT 220
 *    QQQJA 483
 * 
 * This example shows five hands; each hand is followed by its bid amount.
 * Each hand wins an amount equal to its bid multiplied by its rank, where the
 * weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up
 * to the strongest hand. Because there are five hands in this example, the
 * strongest hand will have rank 5 and its bid will be multiplied by 5.
 * 
 * So, the first step is to put hte hands in order of strength:
 *  - 32T3K is the only one pair and the other hands are all a stronger
 *    type, so it gets rank 1.
 *  - KK677 and KTJJT are both two pair. Their first cards both have the
 *    same label, but the second card of KK677 is stronger (K vs T), so
 *    KTJJT gets rank 2 and KK677 gets rank 3.
 *  - T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first
 *    card, so it gets rank 5 and T55J5 gets rank 4.
 * 
 * Now, you can determine the total winnings of this set of hands by adding up
 * the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2
 * + 28 * 3 + 684 * 4 + 486 * 5). So the total winnings in this example are
 * 6440.
 * 
 * Find the rank of every hand in your set. What are the total winnings?
 * 
 * --- Part Two ---
 */

#include <iostream>
#include <fstream>
#include <regex>
#include <set>
#include <algorithm>

class Card {
    private:
        // Consider hashmap instead of std::string::find()
        static const std::string RELATIVE_STRENGTH;
        char label;
        int relativeStrength;
    public:
        Card() {}

        Card(const char &c) {
            label = c;
            relativeStrength = RELATIVE_STRENGTH.find(label);
        }

        const char getLabel() const {
            return label;
        }

        // check
        bool operator < (const Card &other) const {
            return relativeStrength < other.relativeStrength;
        }

        // check
        bool operator > (const Card &other) const {
            return relativeStrength > other.relativeStrength;
        }
};

const std::string Card::RELATIVE_STRENGTH = "AKQJT98765432";

enum HandType {
    UNDEFINED, FIVE_OF_A_KIND, FOUR_OF_A_KIND, FULL_HOUSE,
    THREE_OF_A_KIND, TWO_PAIR, ONE_PAIR, HIGH_CARD
};

class Hand {
    private:
        Card *cards;
        int next = 0;
        int bid;
        HandType type;
    public:
        Hand() {
            cards = new Card[5];
            type = HandType::UNDEFINED;
        }

        Hand(const int &b) {
            bid = b;
        }

        ~Hand() {
            delete[] cards;
        }

        const void addCard(const Card &c) {
            if (next >= 5) throw std::length_error("Hand is full");
            cards[next++] = c;
        }

        const std::string getLabels() const {
            std::string labels;
        }

        const std::string getUniqueLabels() const {
            std::string labels;
            for (int i = 0; i < 5; i++) labels += cards[i].getLabel();
            return labels;
        }

        const int getNUniqueLabels() const {
            return getUniqueLabels().size();
        }

        const void updateType() {
            if (next < 5) throw std::length_error("Cannot define the type of a non full hand");
            if (type != HandType::UNDEFINED) throw std::length_error("Hand type is already defined");

            std::string uniqueLabels = getUniqueLabels();
            std::string labels = getLabels();
            switch (uniqueLabels.size()) {
                case 1:
                    // All cards have the same label -> FIVE_OF_A_KIND
                    type = HandType::FIVE_OF_A_KIND;
                    break;
                case 2:
                    // If there are 4 cards with label A and
                    // 1 card with label B, FOUR_OF_A_KIND, else
                    // FULL_HOUSE
                    bool firstFound = false, secondFound = false;
                    for (char i = 1; i < labels.size(); i++) {
                        if (labels[i] != uniqueLabels[0]) {
                            if (firstFound && secondFound) break;
                            else if (firstFound) secondFound = true;
                            else firstFound = true;
                        }
                    }
                    if (firstFound && secondFound) type = HandType::FULL_HOUSE;
                    else type = HandType::FOUR_OF_A_KIND;
                    break;
                case 3:
                    // THREE_OF_A_KIND: three cards label A label +
                    //                  two different cards
                    // TWO_PAIR: two cards label A + 
                    //           two cards label B +
                    //           one card label C
                    char counter[3] = {0, 0, 0};
                    for (char i = 1; i < labels.size(); i++) {
                        if (labels[i] == uniqueLabels[0]) counter[0]++;
                        else if (labels[i] == uniqueLabels[1]) counter[1]++;
                        else counter[2]++;
                    }
                    std::sort(std::begin(counter), std::end(counter));
                    if (counter[0] == counter[1] == 1) type = HandType::THREE_OF_A_KIND;
                    else type = HandType::TWO_PAIR;
                    break;
                case 4:
                    type = HandType::ONE_PAIR;
                    break;
                case 5:
                    type = HandType::HIGH_CARD;
                    break;
                default:
                    break;
            }
        }


// Every hand is exactly one type. From strongest to weakest, they are:
//  - Five of a kind, where all five cards have the same label: AAAAA
//  - Four of a kind, where four cards have the same label and one card has
//    a different label: AA8AA
//  - Full house, where three cards have the same label, and the remaining
//    two cards share a different label: 23332
//  - Three of a kind, where three cards have the same label, and the
//    remaining two cards are each different from any other card in the
//    hand: TTT98
//  - Two pair, where two cards share one label, two other cards share a
//    second label, and the remaining card has a third label: 23432
//  - One pair, where two cards share one label, and the other three cards
//    have a different label from the pair and each other: A23A4
//  - High card, where all cards' labels are distinct: 23456
// 
// Hands are primarily ordered based on type; for example, every full house is
// stronger than any three of a kind.
// 
// If two hands have the same type, a second ordering rule takes effect. Start
// by comparing hte first card in each hand. If these cards are different, the
// hand with the stronger first card is considered stronger. If hte first card
// in each hand have the same label, however, then move on to considering the
// second card in each hand. If they differ, the hand with the higher second
// card wins; otherwise, continue with the thrid carc in each hand, then the
// fourth, then the fifth.
// 
// So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger
// because its first card is stronger. Similarly, 77888 and 77788 are both a
// full house, but 77888 is stronger because its third card is stronger (and
// both hands have the same first and second card).

};

int partOne() {
    std::ifstream f;
    std::string line;
    std::set<Hand> hands;
    f.open("input/7_Camel_Cards.txt");
    while(!f.eof()) {
        int bid;
        f >> line;
        f >> bid;
        Hand h(bid);
        for (int i = 0; i < 5; i++) h.addCard(Card(line[i]));
        hands.insert(h);
    }
    f.close();

    return -1;
}

int partTwo() {
    
    return -1;
}

int main() {
    std::cout << "Part One: " << partOne() << std::endl;
    std::cout << "Part Two: " <<  partTwo() << std::endl;
    return 0;
}