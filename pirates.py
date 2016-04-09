from sys import exit
from random import randint
#making a base class to enter a scene
class Scene(object):
    def enter(self):
        print "this scene is not configured yet , subclass and implement enter()"
        exit(1)
#make an Engine class and use the methods from Map        
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()  
            
        while True:
            print "<<<<<! P I R A T E   W A R S !>>>>>>>>"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
#class Death for different funny quotes after you die.   
class Death(Scene):
    tips = ["you died. You kinda suck at this!",
            "your grandma would have been proud, if she was smarter.......",
            "such a loser!",
            "i have a pet monkey and hes better than you at this!"
            ]
    def enter(self):
        print Death.tips[randint(0,len(self.tips)-1)]
        exit(1)
         
#opening scene of corridor with events        
class Corridor(Scene):
    def enter(self):
       print " The Pirates from the Black Pearl have invaded your ship and destroyed it." 
       print "Your entire crew is dead." 
       print  "your mission is to get the canon bomb from pirate weapon armory."
       print "place it on the bridge , blow it up and escape with a life boat"
       print "you are running to the weapon armory when a bunch of  pirates attack you with swords!." 
       print "what you gonna do? "
        
       action = raw_input("> ")
        
       if action == "shoot":
            print "the pirates possess better weapons and outnumber you , they easily kill you!"
            return 'death'
            
       elif action == "dodge":
            print "you could perhaps dodge one but you cant avoid them swords forever , so you die!"
            return 'death'
        
       elif action == "joke":
            print " A pirate always likes a good joke! "
            print " you tell them a joke on how once Jack sparrow got drunk and ended up in the British colony."
            print " the pirates cannot help burst laughing and get distracted. " 
            print " you sneak out. "
            return 'pirate_weapon_armory'
       else:
            print "DOES NOT COMPUTE!"
            return 'corridor'
#armory class            
class Pirate_Weapon_Armory(Scene):
    def enter(self):
        print "you do a dive roll into the weapon armory. "
        print " you find a bomb in a corner container. theres a keypad lock attached to it."
        print "the combination requires 2 digits with 5 guesses max."
        code = "%d%d" % (randint(1,3),randint(1,3))
        guess = raw_input("## ")
        chances = 0
        
        while guess != code and chances < 6:
            print "BZZZEEDDDD! Wrong!"
            guess = raw_input("[keypad]## ")
            chances +=1
            
        if guess == code:
            print "the container clicks open and you get the bomb! awesome!"
            print " you escape to the bridge!"
            return 'bridge'
        else:
            print "the lock buzzes and the bomb imploeds! you die!"
            return 'death'
            
#Bridge scene with decisions       
class Bridge(Scene):
    def enter(self):
        print "you burst onto the bridge "
        print "some pirates await you on the bridge with their black masks and pirate hats , what you gonna do?"
        
        action = raw_input("> ")
        
        if action == "throw bomb":
            print "they catch the bomb and defuse it. then you die!"
            return 'death'
            
        elif action == "place the bomb":
            print "you place the bomb sneakily and point your gun at it ! arrrrr! "
            print "you then jump back on the ship deck , pointing your gun at the bomb."
            print "you set the timer on  the bomb and lock out the door, so the pirates are trapped inside."
            return 'lifeboat'
        else: 
            print "CANT COMPUTE!"
            return 'bridge'
            
#Final scene with decision
class LifeBoat(Scene):
    def enter(self):
        print "you run towards the lifeboat deck! theres not much time left till the bomb implodes! Hurry!"
        print "some lifeboats could be damaged and some are good."
        print "there are 5 to select from , just select 1."
        print " which do you take?"

        good_boat = randint(1,5)
        guess = raw_input("[#life boat]> ")

        if int(guess) != good_boat:
            print "you jump into the boat , and steer it clear for some distance , before you make a horrific discovery!"
            print "your boat has a hole. you sink and die!"
            return 'death'

        else: 
            print "you select the right boat and steer away from the ship."
            print "after some time you enjoy the fireworks and win! "
            return 'finished'

            
#scenes stored in a dictionary for reference        
class Map(object):

    scenes = {
    'corridor' : Corridor(),
    'pirate_weapon_armory':Pirate_Weapon_Armory(),
    'bridge': Bridge(),
    'lifeboat' : LifeBoat(),
    'death': Death() 
    }
#start_scene  method 
    def __init__(self,start_scene):
        self.start_scene = start_scene
        
#method for getting next scene        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
#defining the opening scene        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
 #making an instance of Map class, handing to Engine and making the game play.       
a_map = Map('corridor')
a_game = Engine(a_map)
a_game.play()

