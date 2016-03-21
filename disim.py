import random

token = 0
number = random.randint(1,10)
print "Let's play a game!"
print ('Enter and guess  a number between 1 and 10')


while token < 3:
    user = input()
    user = int(user)
    token += 1
    if user < number:
        print ('a bit high')
    if user > number:
        print ('a bit low')
    if user == number:
        break
    if user in range(11,999999999):
	    print "Enter number only between 1 and 10."
         	
if user  == number:
        token = str(token)
        print ('you guess right!!')
        print ('you guessed in ' + token + ' guesses' )
        
elif user != number:
         number = str(number)
         print ('i was thinking of ' + number )
else:
         print ('invalid input')
            
            





