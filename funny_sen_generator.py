import random 


verb_list = ["runs","skips","eats","jumps","jogs","dances","sings","kisses","drinks"]
adj_list = ["fair","valiant","cute","soft","gentle","funny","high","stinky","amazing"]
noun_list = ["  Police comissioner"," Catwoman"," Joker"," Batman"," Robin"," Comedian","Riddler"]
adverb_list = ["sadly","joyfully","affectionately","insanely","voraciously","angrily"]

 

def random_word(list_of_words):
    return random.choice(list_of_words)
        

for i in range(0,10):        
    verb = random_word(verb_list)
    adjective1 = random_word(adj_list)
    noun1 = random_word(noun_list)
    adjective2 = random_word(adj_list)
    noun2 = random_word(noun_list)
    adv = random_word(adverb_list)
    print "The %s  %s , %s with the %s %s so %s " % (adjective1 , noun1 , verb , adjective2 , noun2 , adv)
i += 1  
