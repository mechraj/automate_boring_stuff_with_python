#A game of tictactoe
#steps : 
#Create a dictionary to represent to tictactoe board
#Create a function to print tictactoe borad everytimr it is updated.
#Create a loop which asks users X and O to enter in a space.


#Creating a dictionary to represent a tictactoe board

the_board={'top-L':' ','top-M':' ','top-r':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'bot-L':' ', 'bot-M':' ', 'bot-R':' '
            }

# creating function to print the board
def printboard(board):
    print((board['top-L'])+' | '+(board['top-M'])+' | '+ (board['top-R']))
    print('- + - + -')
    print((board['mid-L'])+' | '+(board['mid-M'])+' | '+ (board['mid-R']))
    print('- + - + -')
    print((board['bot-L'])+' | '+(board['bot-M'])+' | '+ (board['bot-R']))
