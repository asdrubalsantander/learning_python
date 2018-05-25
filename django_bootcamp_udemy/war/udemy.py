from random import shuffle
from time import sleep
import os

SUITS = '♣ ♦ ♥ ♠'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
VALUES = [i for i in range(14)]


class Deck:
    """A deck in the game War.

    Attributes:
        deck: A list of tuples that represent the card suite, rank and value.
    """
    def __init__(self):
        self.deck = [(suite, rank, value) for suite in SUITS for rank, value in zip(RANKS, VALUES)]

    def shuffle_deck(self):
        """Shuffle the deck of the current object."""
        shuffle(self.deck)

    def split_deck(self):
        """Returns the deck split in half."""
        return self.deck[:26], self.deck[26:]


class Hand:
    """A hand of cards used for each player in the game War.

    Attributes:
        cards: A list of cards made by spliting the deck in half.
    """
    def __init__(self, cards):
        self.cards = cards

    def remove_card(self, war_count):
        """Return the proper amount of cards depending on the count of wars."""
        lost_cards = []
        if war_count == 0:
            lost_cards.append(self.cards.pop(0))
        else:
            for i in range(war_count * 5):
                lost_cards.append(self.cards.pop(0))

        return lost_cards

    def add_card(self, card):
        """Add card or cards to the hand.cards"""
        self.cards.extend(card)


class Player:
    """A player for the game War.

    Attributes:
        name: A string representing the name of the player
        hand: An object Hand representing the hand of the player"""
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self, war_count):
        """Prints the card played suit and rank, and return the value of that card.
         This method takes in consideration the count of war."""
        print("{} plays: {}  {}".format(self.name, self.hand.cards[war_count * 4][0], self.hand.cards[war_count * 4][1]))
        return self.hand.cards[war_count * 4][2]

    def check_cards(self, amount_to_check=1):
        """Return a Boolean depending on the amount_to_check.
        Note: Minimum value that returns True it's 4 that way don't overflow if the final battle it's a war."""
        return len(self.hand.cards) > amount_to_check

#############
# GAME PLAY #
#############


def print_score(player, bot):
    """A simple print of the current amount of card in each player's hand"""
    print("{} hand: {} - {} hand: {}".format(player.name, len(player.hand.cards), bot.name, len(bot.hand.cards)))


def battle(player, bot, war_count):
    """The battle that takes one card of each hand, and tests their value.
    If there is a draw this method returns 1.
    The winning player will receive the loser's cards.
    The flag war_count will define how many cards will be in the bet and what cards will be taking into the battle"""
    player_card_played = player.play_card(war_count)
    bot_card_played = bot.play_card(war_count)

    if player_card_played > bot_card_played:
        bet_cards = bot.hand.remove_card(war_count)
        bet_cards.extend(player.hand.remove_card(war_count))
        player.hand.add_card(bet_cards)
        print("{} won this Battle!".format(player.name))
    elif bot_card_played > player_card_played:
        bet_cards = player.hand.remove_card(war_count)
        bet_cards.extend(bot.hand.remove_card(war_count))
        bot.hand.add_card(bet_cards)
        print("{} won this Battle!".format(bot.name))
    else:
        print("WAR!")
        return 1

    return 0


def main():
    deck = Deck()

    deck.shuffle_deck()

    deck_first_half, deck_second_half = deck.split_deck()

    player_hand = Hand(deck_first_half)
    bot_hand = Hand(deck_second_half)

    player = Player('Asdrubal', player_hand)
    bot = Player('Bot', bot_hand)

    war_count = 0

    os.system('clear')

    while True:
        print('')
        if not player.check_cards(4) or not bot.check_cards(4):
            break

        war = battle(player, bot, war_count)
        print('')
        print_score(player, bot)

        sleep(2)

        war_count = war_count + 1 if war else 0


if __name__ == '__main__':
    main()
