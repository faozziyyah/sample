import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
        #return "You and the computer have both chosen {}. It's a tie.".format(computer)

    #r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)
        #return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

    return (-1, user, computer)
    #return "You have chosen {} and the computer has chosen {}. You lost!".format(user, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
        elif result == 1:
            player_wins += 1
            print('You have chosen {} and the computer has chosen {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You have chosen {} and the computer has chosen {}. You lost!\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games. what a champ :0'.format(n))
    else:
        print('unfortunately, the computer has won the best of {} games. Try again.'.format(n))

if __name__ == '__main__':
    play_best_of(3)