import random

# DATA


suites = "♥ ♦ ♣ ♠".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
games = ["2 YOU! Pick someone to drink.",
         "3 ME! Drink up baby",
         "4 FLOOR!",
         "5 GUYS!",
         "6 CHICKS!",
         "7 HEAVEN!",
         "8 Pick a DATE!",
         "9 Bust a RHYME!",
         "10 Categories!",
         "JACK Never have I ever!",
         "Queen Question shhh....",
         "KING Make a new rule!",
         "ACE Waterfall!"]


# CLASSES


class Deck():

    def __init__(self):
        self.cards = [(s, r) for s in suites for r in ranks]

    def shuffle_deck(self):
        random.shuffle(self.cards)
        print("Shuffling deck...")

    def has_cards(self):
        if self.cards:
            return True


class Player():

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def draw_card(self):
        try:
            return self.deck.cards.pop()
        except IndexError:
            return


# FUNCTIONS


def how_many_players():
    try:
        number_of_players = int(input("How many players? "))
        if number_of_players == 1:
            print("You can't play with one person you fucking alcoholic.")
            return how_many_players()
        if number_of_players >= 26:
            print("What's the fucking point playing with that many people? Try again.")
            return how_many_players()
        if number_of_players > 10:
            really = input(str(number_of_players) + " players? Are you sure? y/n ")
            if really == "y":
                return number_of_players
            if really == "n":
                return how_many_players()
            else:
                print("I'll take that as a no.")
                return how_many_players()
        return number_of_players
    except ValueError:
        print("Input must be an integer...")
        return how_many_players()


def create_players(num_of_players):
    current_players = []

    for i in range(num_of_players):

        player_name = ""

        while player_name == "":
            player_name = input("Player" + str(i + 1) + "," + " What is your name? ")
            if player_name == "":
                print("Please enter a name for the player.")

        players[i] = Player(player_name, kings_deck)
        current_players.append(players[i])
    print("")

    return current_players


def card_picture(card):
    symbol = card[0]
    backspace = ""
    if len(card[1]) > 1:
        backspace = "\b"
    rank_index = ranks.index(card[1])
    space1 = space2 = space3 = space4 = space5 = space6 = space7 = space8 = space9 = space10 = space11 = space12 = space13 = space14 = space15 = space16 = space17 = space18 = space19 = space20 = ""
    if rank_index == 0:
        # 2
        space5 = space11 = symbol
        space6 = space12 = "\b"
    elif rank_index == 1:
        # 3
        space5 = space8 = space11 = symbol
        space6 = space9 = space12 = "\b"
    elif rank_index == 2:
        # 4
        space1 = space3 = space10 = space12 = symbol
        space2 = space11 = space16 = space19 = "\b"
    elif rank_index == 3:
        # 5
        space1 = space3 = space13 = space15 = space8 = symbol
        space2 = space14 = space16 = space20 = space18 = "\b"
    elif rank_index == 4:
        # 6
        space4 = space7 = space10 = space5 = space8 = space11 = symbol
        space6 = space9 = space12 = space17 = space18 = space19 = "\b"
    elif rank_index == 5:
        # 7
        space1 = space3 = space5 = space7 = space9 = space13 = space15 = symbol
        space2 = space16 = space6 = space8 = space18 = space14 = space20 = "\b"
    elif rank_index == 6:
        # 8
        space1 = space3 = space5 = space7 = space9 = space11 = space13 = space15 = symbol
        space2 = space16 = space6 = space8 = space18 = space12 = space14 = space20 = "\b"
    elif rank_index == 7:
        # 9
        space1 = space3 = space4 = space6 = space8 = space10 = space12 = space13 = space15 = symbol
        space2 = space16 = space5 = space17 = space9 = space11 = space19 = space14 = space20 = "\b"
    elif rank_index == 8:
        # 10
        space1 = space3 = space4 = space6 = space7 = space9 = space10 = space12 = space13 = space15 = symbol
        space2 = space16 = space5 = space17 = space8 = space18 = space11 = space19 = space14 = space20 = "\b"
    elif rank_index == 9:
        # jack
        space2 = symbol
        space7 = space9 = space18 = space6 = space16 = "\b"
        space5 = "J"
        space8 = "ʘuʘ"
    elif rank_index == 10:
        # queen
        space2 = symbol
        space7 = space9 = space18 = space6 = space16 = "\b"
        space5 = "Q"
        space8 = "ʘ*ʘ"
    elif rank_index == 11:
        # king
        space2 = symbol
        space7 = space9 = space18 = space6 = space16 = "\b"
        space5 = "K"
        space8 = "ʘOʘ"
    elif rank_index == 12:
        # ace
        space8 = symbol
        space9 = "\b"

    print('┌─────────┐')
    print('|{} {}       |'.format(card[1], backspace))
    print('│   {} {} {} {}   │'.format(space1, space2, space3, space16))
    print('│   {} {} {} {}   │'.format(space4, space5, space6, space17))
    print('│   {} {} {} {}   │'.format(space7, space8, space9, space18))
    print('│   {} {} {} {}   │'.format(space10, space11, space12, space19))
    print('│   {} {} {} {}   │'.format(space13, space14, space15, space20))
    print('|       {} {}|'.format(card[1], backspace))
    print('└─────────┘')


# SET UP


# Welcome
print("\nLet's play Kings!\n")

# Create Deck
kings_deck = Deck()

# Asking for amount of players
number_of_players = how_many_players()

# Making a list of players according to amount
players = [("p", i) for i in range(number_of_players)]

# Assigning players to the Player Class and creating a list
current_players = create_players(number_of_players)

# Shuffling deck
kings_deck.shuffle_deck()

# PLAY


print("Press Enter to draw a card.\n")

king_count = 0
rounds = 0
card_count = 52

while kings_deck.has_cards():

    print("Round " + str(rounds + 1) + "!")

    for player in current_players:

        if card_count == 0:
            continue

        input(player.name.capitalize() + ", draw a card.")
        print("\n")
        card = player.draw_card()
        card_picture(card)
        card_count -= 1

        try:
            card_index = ranks.index(card[1])
        except TypeError:
            continue

        print(games[card_index])

        if card[1] == "K":
            king_count += 1

            if king_count != 4 and king_count < 3:
                print("You place the King in the middle. " + str(4 - king_count) + " Kings left!")
            elif king_count == 3:
                print("ONLY 1 KING LEFT!")

        if king_count == 4:
            print("THAT'S THE LAST KING! CHUG A BEER PUSSY!")
            king_count = 0

        if card_count == 30 or card_count == 20 or card_count == 10 or card_count == 5:
            print("\n" + str(card_count) + " cards left!")

        elif card_count == 1:
            print("\nLAST CARD!")

        print("")

    rounds += 1

print("GAME OVER!!!!")
