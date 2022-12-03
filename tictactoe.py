#program that simulates a tectactoe board
#steps
#1. create a dictionary to represent  tic tac toe board
#2. assign 'x' and '0' values to user
#3. update the dictionary everytime  user enters his move

#creating a dictionary to represent the board
theboard={'top-l':' ', 'top-m':' ','top-r':' ',
'mid-l':' ', 'mid-m':' ','mid-r':' ',
'bot-l':' ', 'bot-m':' ','bot-r':' ',}

# function that prints the board
def printboard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['bot-l']+'|'+board['bot-m']+'|'+board['bot-r'])

turn='X'
for i in range(9):
    printboard(theboard) #prints board
    print('User '+ turn+'. Make your move')
    move=input() 
    theboard[move]=turn #updates the board

    if turn=='X':
        turn='0'
    else:
        turn='X'

printboard(theboard)
