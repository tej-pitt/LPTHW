import random

counter = 0
guess = 0
number = random.randint(0,99)
print "Let's play a game!"
print ('Enter and guess  a number between 1 and 99')


while counter < 5 and guess != number:
    guess = input("Enter a number: "  )
    
    if guess < number:
        print ('a bit high')
    elif guess > number:
        print ('a bit low')
    counter +=1 
    
         	
if guess == number:
    print ('you guess right!!')
    print ('you guessed in ' + counter + ' guesses' )

else:
	print "No more guesses , you lost!"
	print "The number was: %d" % number
            
            





