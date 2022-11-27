#program that uses a return statement

import random #imports random module
def get_anwer(answer_number):
    if answer_number==1:
        return 'so close'
    elif answer_number==2:
        return 'It is most probable'
    elif answer_number==3:
        return 'It is decidely so'
    elif answer_number==4:
        return 'This just might be it'
    elif answer_number==5:
        return 'Sorry try again'
    elif answer_number==6:
        return 'wrong answer'
    elif answer_number==7:
        return 'Nope, You got it wrong'
    elif answer_number==8:
        return 'Outlook not so good'
    elif answer_number==9:
        return 'very doubtful'
    
rand_number=random.randint(1,9) #creates a random number and stores it in rand_number
answer=get_anwer(rand_number)    #calls functions and stores the retuen value of function
print(rand_number) #prints the random number
print(answer)  #prints the return value


   