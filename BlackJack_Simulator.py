import random


# deal_card function
# random number between 1 and 10
def deal_card():
    n = random.randint(1, 10)
    return n


# get_dealer_score function
# random score between 16 and 21
def get_dealer_score():
    return random.randint(16, 21)


# get_player_score function
# add random number between 1 and 10 to player score
def get_player_score(player_score):
    player_score = player_score + deal_card()
    return player_score


# main function
def main():
    # initialize player score
    player_score = 0
    # hand of two cards
    player_score = get_player_score(player_score)
    player_score = get_player_score(player_score)
    # dealer score
    dealer_score = get_dealer_score()

    print("Your hand of two cards has a total value of", player_score)
    player_choice = input("Would you like to take another card? (y/n)")
    game = ""
    while player_choice == "y":
        player_score = get_player_score(player_score)
        if player_score > 21:
            print("You Busted with a total of", player_score)
            game = "lose"
            break
        print("Your hand now has a total of", player_score)
        player_choice = input("Would you like to take another card? (y/n)")

    if game == "lose":
        print("\n**You Lose!**")
    else:
        print("You have stopped taking more cards with a hand value of", player_score)
        print("The dealer was dealt a hand with a value of", dealer_score)
        if player_score <= dealer_score:
            print("\n**You Lose!**")
        else:
            print("**You Win**")


# ask the user to play
game_loop = input("Would you like to play a game of Blackjack? (y/n)")
while game_loop == "y":
    main()
    game_loop = input("Would you like to play another game? (y/n)")
else:
    print("Thank You for playing!")
