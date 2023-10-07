import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#printing the cards and score
def print_details(player_cards,computer_cards):
    print("--------current details---------")
    player_score=sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    computer_score=sum(computer_cards)
    print(f"Computers first card is : {computer_cards[0]}")
    print("--------------------------------")

#printing final scores
def find_winner(player_cards,computer_cards):
    print("**********final details***********")
    player_score=sum(player_cards)
    computer_score=sum(computer_cards)
    while computer_score<16:
        computer_cards.append(random.choice(cards))
        computer_score=sum(computer_cards)
    
    print(f"Your final cards: {player_cards}, players final score: {player_score}")
    print(f"Computer's final cards: {computer_cards}, computer's final score: {computer_score}")

    print("**********************************")

    if computer_score==player_score:
        print("Its a draw")
    elif player_score>21:
        print("Your score is greater than 21, you lose :(")
    elif computer_score>21:
        print("Computers score is greater than 21, you win!")
    elif player_score>computer_score:
        print("You win. Your score is higher, congratulations!")
    elif computer_score>player_score:
        print("You lose :( Computer's score is higher")
    


start_game=input("Do you want to play a game of BlackJack? Type 'yes' or 'no': ").lower()
os.system('cls')
while start_game=='yes':
    print(logo)
    #selecting 2 random player cards
    player_cards=[]
    for i in range(2):
        player_cards.append(random.choice(cards))
    #selecting 2 random computer cards
    computer_cards=[]
    for i in range(2):
        computer_cards.append(random.choice(cards))

    #print the inital game info
    print_details(player_cards,computer_cards)
    

    #do you want another card-hit or do you want to keep your original cards-stand
    hit_stand=False

    hit_stand=input("Do you want to hit or stand? Type 'hit' or 'stand': ").lower()
    while hit_stand=='hit':
        player_cards.append(random.choice(cards))
        print_details(player_cards,computer_cards)
        player_score=sum(player_cards)
        if player_score>21:
            find_winner(player_cards,computer_cards)
            break
        else:
            hit_stand=input("Do you want to hit or stand? Type 'hit' or 'stand': ").lower()
    if hit_stand=="stand":
       find_winner(player_cards,computer_cards)

    
    start_game=input("Do you want to play a game of BlackJack? Type 'yes' or 'no': ").lower()
    os.system('cls')