import random

class Deck:
    """
    Purpose:
    Creates and manages a deck of cards.

    Parameters:
    size(int): The total number of cards in the deck.

    Variables:
    self.card_list: Stores the numbers representing the cards.
    self.current_card: Tracks the number of cards dealt.
    self.size: Stores the total number of cards.

    Logic:
    1. Creates a list of cards.
    2. Shuffles the cards.
    3. Keeps track of the cards that have been dealt.
    """

    def __init__(self, size):
        """
        Purpose:
        Initializes and shuffles the deck.

        Parameters:
        size(int): The total number of cards.

        Variables:
        self.card_list: Stores the shuffled cards.
        self.current_card: Starts the card counter at 0.
        self.size: Stores the deck size.

        Logic:
        1. Creates a list of numbers from 0 to size - 1.
        2. Shuffles the list.
        3. Initializes the card counter.

        Return:
        None
        """
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        """
        Purpose:
        Deals one card from the deck.

        Parameters:
        None

        Variables:
        self.current_card: Tracks the number of cards dealt.

        Logic:
        1. Checks if all cards have been dealt.
        2. Reshuffles the deck if no cards remain.
        3. Increases the card counter.
        4. Returns the next card.

        Return:
        int: The number representing the dealt card.
        """
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!!')

        self.current_card += 1
        return self.card_list[self.current_card - 1]


ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'J', 'Q', 'K', 'A']

suits = ['clubs', 'diamonds', 'hearts', 'spades']


def show_card(card):
    """
    Purpose:
    Converts a card number into its rank and suit.

    Parameters:
    card(int): The number representing the card.

    Variables:
    rank: Stores the rank of the card.
    suit: Stores the suit of the card.

    Logic:
    1. Uses the remainder to determine the card rank.
    2. Uses integer division to determine the card suit.
    3. Combines the rank and suit into a string.

    Return:
    str: The card's rank and suit.
    """
    rank = ranks[card % 13]
    suit = suits[card // 13]
    return rank + ' of ' + suit


my_deck = Deck(52)

# Deal five cards to the player
hand = []

for i in range(5):
    hand.append(my_deck.deal())

# Display the player's hand
print("Your Poker hand:")

for i in range(5):
    print(i + 1, show_card(hand[i]))

# Ask which cards the player wants to replace
choice = input("Enter the card numbers you want to replace (1-5): ")

# Replace the selected cards with new cards
if choice.strip() != "":
    for number in choice.split(','):
        position = int(number.strip())
        hand[position - 1] = my_deck.deal()

# Display the final hand
print("\nYour new Poker hand:")

for i in range(5):
    print(i + 1, show_card(hand[i]))
