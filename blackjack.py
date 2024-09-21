import random

# logo
logo = """
            Welcome to BlackJack
            _____                           
           |A .  | _____                   
           | /.\ ||A ^  | _____             
           |(_._)|| / \ ||A _  | _____     
           |  |  || \ / || ( ) ||A_ _ |     
           |____V||  .  ||(_'_)||( v )|     
                  |____V||  |  || \ / |     
                         |____V||  .  |     
                                |____V|     
"""

# variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_score(hand):
    """
    Takes a list of cards and checks/calculates score
    """
    score = sum(hand)
    # Adjust for aces if busting
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score

def draw(cards):
    return random.choice(cards)

def deal(hand, num_cards):
    """
    Deals specified number of random cards to the given hand
    """
    for _ in range(num_cards):
        card = draw(cards)
        hand.append(card)

def stand(hand, score):
    """
    Skips the current hand's turn and displays the score
    """
    print(f'{hand} stands with score of {score}')

def play_blackjack():
    # dealer and user score/hand
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0

    # game start
    print(logo)
    print()
    
    #deals user card and checks user score
    deal(player_hand, 2)
    player_score = check_score(player_hand)

    #deals dealer card and checks 
    deal(dealer_hand, 2)
    dealer_score = check_score(dealer_hand)

    #displays currents hands and cards for both user/dealer
    print(f'Your cards are {player_hand}, current score {player_score}')
    print(f"Dealer's first card is {dealer_hand[0]}")

    #if all of the above is true then continue on with this sectionn code
    while True:
        # player hit/stand loop
        option = input("Type H to hit or S to Stand: ")
        print(option)

        if option.lower() == 'h':
            deal(player_hand, 1)
            player_score = check_score(player_hand)
            print(f'Your cards are {player_hand}, current score is {player_score}')

            if player_score > 21:
                print("Bust! You lose.")
                break

        elif option.lower() == 's':
            stand("Player", player_score)
            break

    if player_score < 21:
        while dealer_score < 17:
            deal(dealer_hand, 1)
            dealer_score = check_score(dealer_hand)
            print(f"Dealer's cards are {dealer_hand}, dealer score {dealer_score}")

            if dealer_score > 21:
                print("Dealer busts! You win!")
                break

        if dealer_score < 21:
            if dealer_score > player_score:
                print("Dealer wins!")
            elif dealer_score < player_score:
                print("You win!")
            else:
                print("It's a tie!")

while True:
    play = input("Do you want to play blackjack? (y or n): ")
    if play.lower() == "y":
        play_blackjack()
    else:
        break





