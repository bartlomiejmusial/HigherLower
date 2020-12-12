import art
from game_data import data
from random import choice
from replit import clear


def random_account():
    return choice(data)


def more_followers(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return 1
    else:
        return 0


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def game():

    end = False
    score = 0
    account1 = random_account()
    account2 = random_account()
    while account1 == account2:
        account2 = random_account()
    while(not end):
        clear()
        print(art.logo)
        print(f"Compare A: {format_data(account1)}")
        print(art.vs)
        print(f"Against B: {format_data(account2)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        more = more_followers(account1, account2) 
        if guess == 'A' and more == 1:
            score += 1
            print(f"You're right! Current score: {score}")
            account2 = random_account()
            while account1 == account2:
                account2 = random_account()
        elif guess == 'B' and more == 0:
            score += 1
            print(f"You're right! Current score: {score}")
            account1 = account2
            account2 = random_account()
            while account1 == account2:
                account2 = random_account()
        else:
            clear()
            print(art.game_over)
            print(f"Sorry, that's wrong.")
            print(f"Final score: {score}")
            print(f"\n\t{account1['name']} - {account1['follower_count']} followers")
            print(f"\t{account2['name']} - {account2['follower_count']} followers")
            end = True
            again = input("\nDo you want to play again? Type 'y' if yes or 'n' if no: ")
            if again == 'y':
                game()
            clear()
            
game()
