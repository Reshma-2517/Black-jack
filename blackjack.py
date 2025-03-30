#import random module to select deck of cards randomly
import random
deck_of_cards = [1,2,3,4,5,6,7,8,9,10,11,11,11]

#Drawing two cards and adding them to sum up
your_card1 = random.choice(deck_of_cards)
your_card2 = random.choice(deck_of_cards)
card_sum = your_card1 + your_card2
print(f"Your score is {card_sum}")

#Computer draws a card
computer_card = random.choice(deck_of_cards)
print(f"Computer's card is {computer_card}")

#checking your card sum status and calling the function
def progress():
    if card_sum > 21:
        print("Bust")
        exit()

    elif card_sum == 21:
        print("You win !!!!")
        exit()
progress()

#Choosing whether to stand or hit.You can continuously hit until you win ,lose or bust
def choices():
    choice = input("Would you like to hit or stand? :").lower()

    #if the choice is hit
    if choice == "hit":
        your_card3 = random.choice(deck_of_cards)
        global card_sum
        new_score = your_card3 + card_sum
        print(f"Your new card is {your_card3} and your total score is {new_score}")
        #checking new_score status
        if new_score > 21:
            print("Bust")
            exit()
        elif new_score == 21:
            print("You win")
            exit()
        else:
            card_sum = new_score
            choices()
    else:
        #if the choice is stand
        print("Your total score is: " , card_sum)
        computer_score = computer_card

        #computer also has the right to hit until it's wish or until the condition satisfies.so we are putting it in a loop 
        while computer_score < 18:
            computer_card1 = random.choice(deck_of_cards)
            computer_score += computer_card1
            print("computer score is: ", computer_score)

        #checking the status of both your card sum and computer card sum by comparing
        if computer_score > card_sum:
            print("You lose")
            exit()
        elif computer_score < card_sum:
            print("You win")
            exit()
        else:
            print("Push")
            exit()
choices()  
