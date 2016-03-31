import random

#print your welcome message here
print """Lets play an amazing multiplier game! ,
Are you good with your tables ? Lets test and see! """
#initialize num and counter
num = 0
counter = 0
#while loop for limiting no of guesses 
while counter < 5:
    for num in range(0,10):
    #for loop for specifying number of random multiplications generated.
        number1 = random.randint(1,20)
        number2 = random.randint(1,10)
        answer = number1 * number2
        print "What is", number1, "x", number2, "?"
        guess = input("Answer: ")
        #if loop for guess is wrong or right
        if guess != answer:
            print "No, try again"
            counter += 1
            print "you have %d chances remaining" % (5-counter)#specifies number of chances left
            if counter == 5:
            #nested if for limiting chances for wrong attempt.
                print "Your chances are over! Learn your tables!"
                break 
                
            else:
                print "Answer the next one correctly." 
                                
        #outer if loop if answer is right                  
        elif guess == answer:
            print "You genius Ramanujan. Next one!"
        #default    
        else: 
             "Man learn to type a number."
      
             
        
        
