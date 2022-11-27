#program for error handling

#function divides 100 by given argument
def spam(divideby): 
    try:    #since dividing number is prone to mathematical errors we use try statemnt
        return 100/divideby
    except ZeroDivisionError:   #exception for zero division error
        print("Dividing a number with zero results in infinity.")

print(spam(10))
print(spam(4))
print(spam(0))
print(spam(1000))