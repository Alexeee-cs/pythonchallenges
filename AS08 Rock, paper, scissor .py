import random
action = ['rock','paper','scissor']
decision = random.choice(action)
user_action = input("Please choose your move (rock/paper/scissor): ")
user_move = user_action.lower()
if user_move == 'rock':
    if decision == 'rock':
        print('tie')
    elif decision == 'paper':
        print('you lost')
    else:
        print('you win')
elif user_move == 'paper':
    if decision == 'rock':
        print('you win')
    elif decision == 'paper':
        print('tie')
    else:
        print('you lost')
elif user_move == 'scissor':
    if decision == 'rock':
        print('you lost')
    elif decision == 'paper':
        print('you win')
    else:
        print('tie')
else:
    print("INVALID move")

print("The computer played:",decision)
print("You played:",user_move)
