#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time 
import sys
from time import sleep 

def restart():
    restart = input("Would you like to restart the game?")
    if restart == "yes" or restart == "y":
        startGame()
    elif restart == "n" or restart == "no":
        print ("Game terminated. Goodbye.")
    else:
        print("Please type yes or no!")
        
def startGame():

    while True:
    
        a = input("Start Playing the Game? (yes/no) : ")

        if a.lower().strip() == "yes":
            global b
            b = input("What is your name? :" )
            print()
            print()
            time.sleep(1)
            print('Hello, %s. Welcome to Text Adventure. Let us begin the story!' %b)
            print()
            print()
            
            
            time.sleep(3)
            
            
            n = """It's another sunny day in Songdo campus, Yonsei University.
    You feel very refreshed as you walk past chattering students and the dorms. 
    You spot professor Brad Moses walking your way."""
            
            for char in n:
                sleep(0.03)
                sys.stdout.write(char)
                sys.stdout.flush()
                
            time.sleep(1)
            print()
            print()
            print("""Professor Brad: [Hey %s ! Would you like to go to Baskin Robbins for some ice cream?
    I hear they have some good flavors on sale!]""" % b)
            
            time.sleep(1)
            
            
            print()
            print()
            print("""You: [Sure professor, as long as you're the one paying!]""")
            
            
            time.sleep(1)
            
            print()
            print()
            d = """Inside Baskin Robbins, you look around for any flavor on sale you like. 
    You spot two candidates : Cookies n’ Cream, and Rainbow Sorbet """
            
            for char in d:
                sleep(0.03)
                sys.stdout.write(char)
                sys.stdout.flush()
                
            time.sleep(1)
                
            print()
            print()
            
            while True:
                
                c = input("Which will you choose? If you want Cookies n’ Cream, type '1'. If you prefer Rainbow Sorbet, type '2' >>> ")

                if c == '1':
                    cookies_cream()



                elif c == '2':
                    rainbow_sorbet()
                
                else: 
                    print("Type 1 or 2!")
                    time.sleep(2)
                    
        elif a.lower().strip() == "no":
            print("OK! Later then :) ")
            print()
            print()
            time.sleep(3)
            restart()
        else:
            print("Please type yes or no!")

        
def rainbow_sorbet():
    print()
    print()
    time.sleep(1)
    
    ice ="""You eat one spoonful of the ice cream, but all of a sudden everything starts to go hazy."""

    for char in ice:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)
    print()
    print()
    limb ="""Your limbs go numb and everything slowly fades to black."""

    for char in limb:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)
    print()
    print()
    dot = """. . . . """

    for char in dot:
        sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(3)
    print()
    print()
    
    a = """The moment you regain consciousness, you notice that the ground beneath you is unsteady. It seems to be swaying.... You look around, and realize that you're tied up!"""
    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
        
    time.sleep(1)
                              
    b = """[Am I kidnapped?]
There are people in front of you with guns and knives, and they seem to be speaking some sort of 
strange language you don't understand. Suddenly, you spot the professor among the group."""
    for char in b:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
        
    time.sleep(1)
                          
    c = """[Professor! Thank god, I think we were somehow kidnapped, are you alr...... Why are you not tied up?
And that hook.......don't tell me...!]"""
    
    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print()
    print()
    
        
    time.sleep(1)
                          
                              
    d = """Professor: [Ha ha ha! You still believe I'm professor Brad?? I'm not your professor, I'm a Somali pirate and these are my crew!]"""
    for char in d:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
      
    time.sleep(1)

    e = """You can't believe what you're hearing. They're pirates? Taking a closer look, you realize you're still near the shores of Incheon.
The ice cream was likely spiked, and after the panic you begin to assess the situation. What should you do??"""
    for char in e:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)

    d = input("Fight (a), or stay put (b)?  (Type a if you choose to fight, or b) >>> " )
    if d == "a":
        print()
        print()
        time.sleep(1)
        f = """You stand up. The pirates begin to stare at you in confusion. You smile and dash forward."""
        for char in f:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
            
        
        print()
        print()
        g = """. . . . . . . . . . ."""
        
        for char in g:
            sleep(0.06)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        time.sleep(2)
        print()
        print()
        
        print("""10 minutes later""")
        
        time.sleep(2)

        print()
        print()
        
        h = """Pirate: [How... How is this possible!! We didn't even see you!]"""
        
        for char in h:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        
        print()
        print()
        time.sleep(1)
        
        i = """[Seems like you were all underestimating me. I happen to know some Kung Fu!]"""
        
        for char in i:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
            
        time.sleep(1)
        
        print()
        print()
        
        j = """You immobilize your enemies with your fists in a flash. 
Everyone is unconscious except pirate Brad, who is looking at you in horror."""
        for char in j:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        time.sleep(1)
        
        print()
        print()
        
        k = """Brad: [Wait! Please, save me! I'm actually innocent! Give me a chance to explain!]"""
        
        for char in k:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        print()
        while True:
            
            k = input("Save him? (yes/no) >>> ")
            if k.lower().strip() == "yes":
                save_him()
            elif k.lower().strip() == "no" :
                knockout()
            else:
                print("Type yes or no!") 
                time.sleep(2)


    else:
        print()
        print()
        time.sleep(1)
        end = """ Pirate: [Ha! ha! ha! Your organs will sell for a high price in the Chinese market!]

The ship gets further and further away from Incheon...... Oh uh....
    .
    .
    .

The end            :(   """
        
        for char in end:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

        print()
        time.sleep(3)
        restart()
        


def knockout():
    print()
    print()
    time.sleep(2)
    l = """You punch him in the head and knock him out. Hmph, why should you listen to this trash?"""
    
    for char in l:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(1)  
    print()
    print()
    
    m = """You search for things that might be useful for the escape from the pockets of the pirates. 
After taking some things you find a flare gun and blast it into the sky."""
    
    for char in m:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(1)  
    print()
    print()
    
    print("""BANG!!""")
    time.sleep(1)  
    print()
    print()
    
    
    n = """A nearby fishing boat sees the flare and manages to rescue you.
However, their way of staring at you makes you realize that they seem to be suspicous of you. 
Maybe they think you're one of the pirates.........
           
           
           
['I have a bad feeling about this......']'"""
    
    for char in n:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(1)

    print()
    print()
          
    o = """When you reach the shore, you see police cars waiting for you."""
    
    for char in o:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(1)  
    
    print()
    print()
    
    p = """So they were suspicious after all! Oh no!"""
    
    for char in p:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(1)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    print()
    print()
    
    q = """A few weeks later, you are scheduled to be standing in the courtroom, charged for piracy."""
    
    for char in q:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(1)  
    print()
    print()
    
    r = """Seems like the possessions of the pirates that were discoverd from your cloths won't work in your favor at all. 
Oh no, maybe it was wiser to just leave everything where they were...."""
    
    for char in r:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(1)  
    print()
    print()
    
    s = """What should you do, should you plead guilty and try to lessen your sentence? """
    
    for char in s:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(1)  
    print()
    print()
    
    while True:
        m = input("Plead guilty or not? Press 1 if you wish to plead guilty, and 2 if you wish to deny charges >>> " )
        if m == "1":
            plead_guilty()
            time.sleep(2)
        elif m == "2":
            not_plead_guilty()
            time.sleep(2)
        else:
            print("Type 1 or 2 !")
            time.sleep(1)
        
                        
def plead_guilty():
    print()
    print()
    
    t = """ You and your lawyer decide to plead guilty, and calmly wait for the sentence."""
    
    for char in t:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    print()
    
    u = """After a few days of trial, a miracle occured - The court's final decision was to let you go!"""
    
    for char in u:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(1)  
    print()
    print()
    
    v = """It seems like decisive evidence was lacking. You are somehow released, and you walk back to the dorms, singing happily."""
    
    for char in v:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(1)  
    print()
    print()
    
    w = """You visit a convenience store nearby to buy some snacks. However, from the TV screen inside the store, A reporter is delivering some familiar news......"""
    
    for char in w:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(2)  
    print()
    print()
    
    x = """Reporter: [According to sources exclusive to JABC, it has been confirmed that there is one suspect among the Somali pirates who managed to escape after the trial. 
The police are investing all resourses to ensure that the suspect is caught before public order is disrupted. 
They are also considering whether to release the personal information and photo of the suspect, and an announcement regarding the decision is scheduled to be made in 3 days.]"""
    
    for char in x:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)  

    print()
    print()
    
    y = """['What? Why are they still looking for me??? I thought I was proven innocent and released! Did they somehow find more evidence and they want to put me back in jail?
If the police release my personal information my life is going to be ruined! I need to somehow destroy their data!  """
    
    for char in y:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(2)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    time.sleep(1)  
    print()
    print(".")
    time.sleep(3)
    print()
    
    z = """Few hours later, in the middle of the night. You are in front of the police headquarters. Using your stealth skills you slip past the policemen unnoticed, and 
    
find a door with a sign that says 'KEEP OUT! Authorized Personnel Only'. You use your super ninja skills to unlock the door and enter the room. It is just as you expected.
           
You see a single computer, and many thick books with the names of various famous cases that occured before. You turn the computer on. 
           
Two files on the desktop catch your eye: The data labed 'Somali Pirates', and .............."""
    
    for char in z:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(3)
    
    print()
    print()
    
    a = """ ['What's this? An unpublished rough draft of the next season of Nar*to! It seems like the police chief is friends with the author!']"""
    
    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    
    time.sleep(2)  
    print()
    print()
    
    b = """You suddenly hear footsteps. Some people approaching, oh no! It's just a matter of seconds before they arrive at the door. You only have time for one choice. What will you do??"""
    
    for char in b:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
    time.sleep(2)  
    print()
    print()
    
    
    v = input("Should you destroy the evidence, or steal the rough draft of Narito? 1 if you wish to destroy the data, and 2 if you want the draft " )
    if v == "1":
        time.sleep(1)
        print()
        print()
        
        c = """Heck, of course maintaining your innocence is more important! You double click the file containing the data."""
        
        for char in c:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        print()
        print()
        
                 
        print("""[Password:              ]""")
        
        time.sleep(2)  
        print()
        print()
        print(".")
        time.sleep(1)  
        print()
        print(".")
        time.sleep(1)  
        print()
        print(".")
        print()
        print()
        print("WHAT!")
        
        print()
        print()
        
        d = """This has a password! Of course they would have passwords! Realizing that they're nearly here, You try your birthday, but of course it doesn't work."""
        
        for char in d:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        
        time.sleep(2)  
        print()
        print()
        
        e = """My wrong attempt triggers an alarm, and the whole police station goes on lockdown."""
        
        for char in e:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        
        time.sleep(2)  
        print()
        print()
        
        f = """Police: [Freeze! you are caught red-handed trying to access classified police evidence]
.
.
.
.
.
.
               
               
               
               
Uh oh, Guess I'm going to jail again..."""
        
        for char in f:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        time.sleep(2)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        
        
                 
                 
        print("Thank you for playing :D ")
        time.sleep(3)
        restart()
   

    elif v == "2":
        time.sleep(1)
        print()
        print()
        
        g = """You read it and it’s amazing. Thankfully the policemen went inside the romm next to mine."""
        
        for char in g:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

        print()
        print()
        time.sleep(2)
        
        h = """Halfway through, you hear someone pulling up on the driveway. """
        
        for char in h:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

        print()
        print()
        time.sleep(2)
        
        i = """"It’s the police chief! He must be here to check up on the data.  
You manage to escape through the window just in time. You make it out safe, but fail to destroy the evidence."""
        
        
        for char in i:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        print()
        print()
        time.sleep(2)
        
        
        c = """[What should I do? Am I going to go back to jail when I just got out??] 
You panic, but soon realize the news might not be talking about you. There are plenty of other pirates who were on that ship right?"""
        
        for char in c:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        time.sleep(2)
        print()
        print()
        
        d = """As I begin to calm down and feel better, I hear a soft 'click' right behind me and I freeze at the sound."""
        
        
        for char in d:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        time.sleep(2)
        print()
        print()
        
        
        e = """[There you are. you will pay for putting all of us in jail! Let's see if your Kung Fu works on bullets, hahaha!]
He's the real escapee they were talking about! And this tims he's here with a gun! """
        
        for char in e:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
            
        print()
        print()
        time.sleep(2)
        
        f = """['I don't think I can dodge the bullets at a range this close. What should I do??']'"""
        
        while True:
            time.sleep(2)
            print()
            ab = input(" 1 if you wish to try negotiating with him, and 2 if you choose to run away >>> ")
            
            if ab == "1":
                negotiate()
            
            elif ab == "2":
                runaway()
            else:
                print("Please type 1 or 2!") 
                time.sleep(2)
        
        
    
        
    
    else:
        time.sleep(2)
        print()
        print()
        print("Congratulations, you unlocked the secret ending! As a prize, you get nothing. Now go away")
        
        restart()
 


    


def negotiate():
    
    et = """[Alright, how about this? I'll give you some money, and we can leave each other alone. Good enough?]
             
I try to see if negotiating works with him."""
    
    
    for char in et:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()    
    
    print()
    print()
    time.sleep(2)
    
        
    bc = """[Ha ha ha! Do you think I'll be tempted by money?? My loyalty to my comrades will never waver as long as I- ]
[10****************0 won.]
[We have a deal.]
Luckily you still have the lotto prize you won last year! 
            
            
            
You return safely to Songdo with the help of the pirate and live happiy every after.         
...           


Although now I'm completely broke. Haha"""
    
    for char in bc:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush() 
    
    
    time.sleep(3)
        
        
    print()
    print()
    
    print("Thank you for playing the game!")
    print()
    print()
    time.sleep(3)
    
    restart()
        

        
def runaway():
    print()
    print()
    eg = """[Look! What's that??] you point up at the sky.
    
[What! Is it an incoming attack? ..... No I don't see anything, what are you - ]
            
The pirate turns his head around, only to realize that he is alone.
            
[Noooooo! I fell for such a stupid trick!]"""
    
    
    
    for char in eg:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush() 
    
    time.sleep(2)
    print()
    print()
    
    
    bm = """You manage to escape successfuly. Thak god he's so gullible. 
[I'm finally free! Time to go back to Songdo to get some res-]
[Freeze! Don't move!]"""
    
    for char in bm:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print()
    print()
    time.sleep(2)
        
    
    gp = """You turn around and see two policemen aiming their guns at you. One of them talks into his walkie-talkie.
[We found the suspect!. Requesting for backup, the suspect is....]
You don't make the rest of the words, because you are too busy realizing one absurdity - so I WAS the one they were looking for after all! Oh no!  """
    
    for char in gp:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush() 
        
    time.sleep(2)
    
    print()
    print()
       
    gf = """You are captured by the police....... Again. Uh, oh, how can I get out this time? """
    
    for char in gf:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print()
    print()
    time.sleep(3)
        
    
    print("""Thank you for playing the game!""")
    print()
    time.sleep(3)
    restart()
        
    
        
def not_plead_guilty():
    print()
    print()
    time.sleep(2)
    
    j = """By some crazy chance things actually start to look pretty good. The court fails to acquire decisive evidence proving your guilt.
You start to believe that your innocence can be proven when........."""
    
    for char in j:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(2)
    print()
    print()
    
           
    k = """Suddenly, just before the court adjorns, a mystery individual barges into the court. 
[I have evidence proving that the suspect is guilty!]"""
    
    for char in k:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(2)
    print()
    print()
    
           
    l = """Who on earth - wait is that the not-professor who was supposed to be in jail??? Did he escape??? 
No - he must have been bailed out! Oh no! 
The not-professor Brad: [Look through the suspect's phone contacts! My phone number should be there. 
That's proof that he and I are comrades! My nickname in the Somali pirates was 'professor!']
           
['No way I would have - oh no, I do have his number from when he was still a professor! How can that backfire!??']"""
    
    for char in l:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print()
    print()
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print()
    print()
        
    v = """A while later, you are sentenced to a lifetime in jail including charges for falsehood
Too bad, maybe letting him go was the better choice after all?   ....     :0 """
    
    for char in v:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print()
    print()
    time.sleep(2)
        
        
    print("Thank you for playing the game!")
    print()
    time.sleep(3)
    
    restart()
                    
                        
def save_him():
    print()
    print()
    time.sleep(2)
    a ="""Due to a strange sudden impulse you decide to withold your last blow from the not-professor. Realizing that you've decided to spare him, he begins to lay out his story"""

    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    zoo ="""Professor Brad: [Okay, now that you've knocked out all of these guys you need to listen to me. I'm really sorry about kidnapping you, that was uncool.
But I've also been held hostage by these guys for several months now! I mean, I am one of them but I had to convince them I was joining their little possee because I needed the money...]"""

    for char in zoo:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    c ="""You: [Money for what??] You yell out in exasperated bewilderment."""

    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    d ="""Professor Brad: [For my pet poodle back home... pet care's gotten real expensive these days, like seriously.]"""

    for char in d:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    e ="""Unable to tell if he's joking or not, you ultimately decide to forgive him and drive the pirate ship to shore.
And with the stash of pirate cash they found, decide to head over to Severance Hospital together for his poodle's surgery."""
    for char in e:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    f ="""After safely arriving at the hospital the two of you head over to the waiting room. While you wait for your number to be called, you decide to go get something to drink"""

    for char in f:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    chosen_shop = input("There are two coffee shops in front of you, Starbucks and Coffee Bean. Which shop do you choose? >>> ")
    while True:
        if chosen_shop.lower().strip() == "starbucks":
            choose_starbucks()
        if chosen_shop.lower().strip() == "coffee bean":
            choose_coffeebean()
        else:
            chosen_shop = input("Oops! Gotta enter in one of the two shops. Check spelling mistakes!")

def choose_starbucks():
    a="""While waiting in line, a passer-by does a double-take at your face and slowly approaches you."""

    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    zoot= """Random Passerby: [Excuse me... were you the one who stepped off the suspicious-looking pirate ship at the Incheon port today..?] The man asked in an inquiring tone."""

    for char in zoot:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    c = """You: [Uhh...no. That definitely wasn't me.]"""

    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    d ="""Random Passerby: [Really? 'Cause there's currently a search going on for two alleged pirates and you look awfully similar to the police sketch]"""

    for char in d:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    e ="""You: [Uhh...]"""

    for char in e:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    f ="""Random Passerby: [Yup, it's definitely you. Hello, is this the police?]"""

    for char in f:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    g ="""Next thing you know, you are surrounded by a barricade of police. One thing led to another and you're now currently awaiting trial on charges of piracy and intense booty-collecting.
Standing in court, you realize that the odds are criminally against your favor (pun intended). It would have to take a miracle to have you sentenced not guilty. So how do you plead? Guilty, or not guilty?"""

    for char in g:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)
    print()
    print()
    while True:
        
        plead = input("Type in 1 for guilty, or 2 for not guilty >>> ")
        if plead == "1":
            plead_guilty()
        if plead == "2":
            not_plead_guilty()
        else:
            plead = input("An invalid input! Enter in either 1 or 2 >>> ")


def choose_coffeebean():
    a ="""While waiting in line, a random passer-by does a double-take at your face and slowly approaches you."""

    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    zap ="""Professor Brad sees this stranger walking towards you, and noticing that their phone is ready to dial the police, he suddenly jumps at the stranger."""

    for char in zap:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    c ="""Professor Brad: [Argh! Get out of here while you can! This person's about to call the police!]"""

    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    whattodo = input("What do you do in this situation? 1, escape without him, or 2, help him fight off the stranger and escape together? >>> ")
    while True:
        if whattodo == 1:
            time.sleep(3)
            escape_without()
        if whattodo == 2:
            time.sleep(3)
            go_back()
        else:
            whattodo = input("An invalid input! Enter in either 1 or 2")

def escape_without():
    a = """You: [I'm... I'm so sorry!]"""

    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    app ="""You frantically run towards the exit, but while passing by Dunkin' Donuts you accidentally bump into a bunch of off-duty police officers on lunch break.
The police officer you bumped into slowly turns around and is startled to see your face."""

    for char in app:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    c = """Police Officer: [Hey... I know your face! You ain't getting away this time. Men! It's the sneaky little pirate!]"""

    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    d ="""In an unfortunate turn of events, you eventually end up waiting for trial on charges of piracy and intense booty-collecting"""

    for char in d:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    e ="""Standing in court, you realize that the odds are criminally against your favor (pun intended). It would have to take a miracle to have you sentenced not guilty.
So how do you plead? Guilty, or not guilty?"""

    for char in e:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)
    plead = input("Type in 1 for guilty, or 2 for not guilty:  ")
    while True:
        if plead == "1":
            plead_guilty()
        if plead == "2":
            not_plead_guilty()
        else:
            input("An invalid input! Enter in either 1 or 2")
            time.sleep(2)
    


def go_back():
    a ="""Remembering all the brief but wacky times you shared together, you can't bring yourself to part with Professor Brad so heartlessly. You lunge at the strager and knock him to the ground"""

    for char in a:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()
    print()
    time.sleep(1)
    bam ="""You: [I can't leave you here like this! Come on, let's get out of here together! And bring your poodle!]"""

    for char in bam:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print()
    print()
    time.sleep(1)
    c ="""Just in time to catch the shuttle bus back to Songdo, the two of you arrive at the International Campus without being caught.
Professor Brad is distraught that he couldn't get his poodle to surgery, but you remember that you have pretty competent vet friend.
You decide to hook the Professor with an appointment and proceed to return to your cozy dorm."""

    for char in c:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print()
    print()
    time.sleep(1)
    d = """You: [Man... what a crazy day.]"""

    for char in d:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print()
    print()
    time.sleep(1)
    print("<fin>")
    print()
    print()
    time.sleep(2)
    restart = input("Would you like to restart the game?")
    if restart == "yes" or restart == "y":
        startGame()
    if restart == "n" or restart == "no":
        print ("Game terminated. Goodbye.")
    

def cookies_cream():
    print()

    beg = """The moment you bite into the ice cream, a blue blob zooms past you quickly.
You realise that your ice cream has been snatched away from your hand."""
    for char in beg:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)

    print()
    print()
    while True:

        corh = input('Will you chase after the blue blob (1) or will you go home (2) ?')
        if corh == '1':
            chase()
        if corh == '2':
            home()
        else:
            input('Invalid input! Type 1 or 2.')
            time.sleep(0.5)
            print()

def home():
    print()
    sad = 'You go home sadly like a wimp.'
    for char in sad:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    restart()
 
def chase():
    print()
    glance = """You walk around the neighbourhood to try to find who stole your ice cream.

Walking past a green garbage can, you see a familiar shade of blue.

The closer you get to the blue blob, the more you realise that the living being is… fluffy?"""
    for char in glance:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)
    print()
    print()
        
        
    realise = 'It’s Cookie Monster eating your ice cream.'
    for char in realise:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    time.sleep(2)

    print()
    print()
    while True:

        game = input("""Sigh and leave because he's eating it OR fight him. Type 'leave' or 'fight'. """)
        if game == 'leave':
            go_home()
        if game == 'fight':
            game_on()
        else:
            game = input('Invalid input! Check for spelling mistakes.')
            time.sleep(2)
           

def go_home():
    print()
    print()
    print("You walk back home like a wimp. Would you like to restart the game?")
    restart()

def game_on():
    print()
    print()
    gamebegin = 'Cookie Monster challenges you to a duel! Get ready for an intense game of Tic-Tac-Toe!'

    for char in gamebegin:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print()
    print()
    time.sleep(2)
    

        # Tic Tac Toe

    def drawBoard(board):

        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def inputPlayerLetter():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst():
        
        if random.randint(0, 1) == 0:
            return 'Cookie Monster'
        else:
            return 'You'

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(bo, le):
        
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(board):
        
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    def isSpaceFree(board, move):
        
        return board[move] == ' '

    def getPlayerMove(board):
        
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(board, movesList):
        
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(board, computerLetter):
        
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, computerLetter, i)
                if isWinner(boardCopy, computerLetter):
                    return i

        
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, playerLetter, i)
                if isWinner(boardCopy, playerLetter):
                    return i

        
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        
        if isSpaceFree(board, 5):
            return 5

        
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def isBoardFull(board):
        
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True


    while True:
        
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print(turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'You':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    angry = """Hooray! You have won the game!"""

                    for char in angry:
                        sleep(0.03)
                        sys.stdout.write(char)
                        sys.stdout.flush()

                    time.sleep(1)
                    print()
                    print()

                    print('*KAPOW*')
                    time.sleep(1)
                    print()
                    print()

                    angry1 = """In a fit of violent rage, Cookie Monster punches you in the stomach! He is angry because you won!
    Just then, you lose consciousness...


    ..."""

                    for char in angry1:
                        sleep(0.03)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        
                    break
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)

                        time.sleep(1)

                        tie = "The game is a tie!"

                        for char in tie:
                            sleep(0.03)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                        print()
                        print()
                        time.sleep(2)
                        print('*KAPOW*')
                        print()
                        print()
                        time.sleep(1)

                        tie2 = """In a fit of confused rage, Cookie Monster punches you in the stomach! He is angry because nobody won!
    Just then, you lose consciousness...


    ..."""
                        for char in tie2:
                            sleep(0.03)
                            sys.stdout.write(char)
                            sys.stdout.flush()

                        break

                    
                    else:
                        turn = 'Cookie Monster'

            else:
                
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)

                    time.sleep(2)
                    print()
                    print()

                    print('*KAPOW*')
                    time.sleep(1)
                    print()
                    print()
                    happy = """Cookie Monster has beaten you! And in a fit of euphoric glory, he punches you in the stomach. Just then, you lose consciousness...


    ..."""
                    for char in happy:
                        sleep(0.03)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        
                    break
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)

                        time.sleep(1)

                        tie = "The game is a tie!"

                        for char in tie:
                            sleep(0.03)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                        print()
                        print()
                        time.sleep(2)
                        print('*KAPOW*')
                        print()
                        print()
                        time.sleep(1)

                        tie2 = """In a fit of confused rage, Cookie Monster punches you in the stomach! He is angry because nobody won!
    Just then, you lose consciousness...


    ..."""
                        for char in tie2:
                            sleep(0.03)
                            sys.stdout.write(char)
                            sys.stdout.flush()

                        break


                    else:
                        turn = 'You'


        break


    time.sleep(2)
    print()
    print()

    sesame = """You wake up to a high-pitched, annoying voice talking in a distance. Groggily, you open your eyes and sit up.

You jump up because this isn’t your house!

This is Sesame Street! In the distance, you see Elmo talking to Cookie Monster and Big Bird."""

    for char in sesame:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()
    print()
    while True:

        sneak_conf = input("""Sneak around to find a way out OR confront Elmo by talking it out. Type "sneak" or "confront".""")
        if sneak_conf == "confront":
            talk()
        if sneak_conf == "sneak":
            elmo()
        else:
            sneak_conf = input("Invalid input! Check for spelling mistakes.")
            time.sleep(2)

def talk():
    print()
    print("""%s: [Cookie Monster! Do you know that you are a big fat meanie? You stole my ice cream.
I need an explanation for your disappointing behaviour.]""" %b)


    time.sleep(1)
    print()
    print()

    print("Cookie Monster: [How dare you talk back at THE Cookie Monster!]")


    time.sleep(1)
    print()
  
    print("Cookie Monster: [I was going to let you go easily, but you have made me mad. You will be my cookie-baking slave for eternity!]")


    time.sleep(1)
    print()
    print()

    print("""You lose. You become Cookie Monster's cookie-baking slave.""")
    restart()

 
def elmo():
    print()
    print()
    run = """You walk away from Elmo and the others.
You realise that you still have your phone with you so you grab an Uber to take you to the nearest airport, which happens to be LAX.


*tip-toes away from the Sesame Street guys*"""

    for char in run:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()
    print()

    at_lax = """*At LAX*

You're finally at LAX! This is great. You are in disbelief that the Sesame Street characters only pretend to be nice on TV,
but are you really surprised? It's Hollywood after all."""

    for char in at_lax:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()
    print()
    while True:
        
        airport = input('You take a flight back to ICN or decide to fly out to JFK to explore more of the US while you’re there. Type ICN or JFK')
        if airport == "ICN":
            icn_home()
        if airport == "JFK":
            jfk_ex()
        else:
            input('Invalid input! Type ICN or JFK! It is case-sensitive.')
            time.sleep(0.5)

def icn_home():
    safe = """You're back at Incheon and you get back home safely at Songdo! Hooray!"""

    for char in safe:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)
    print('Congrats, you finished! You can restart the game to explore different stories!')
    print()
    print()

    restart()
    

def jfk_ex():
    print()
    print()
    nyc = 'You get a ticket to JFK. You are now waiting for a flight to New York City.'

    for char in nyc:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)
    print()
    print()

    print("PA: [This is the final boarding call for Flight 1885 to JFK. Please proceed to Gate 4 immediately. Thank you.]")

    time.sleep(2)
    print()
    print()

    arrive = """...

You are now in New York! You have the option to visit Times Square or the Statue of Liberty."""

    for char in arrive:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    while True:
        des = input("Type (1) for Times Square or (2) for Statue of Liberty.")
        if des == "1":
            times_sq()
        if des == "2":
            stat_lib()
        else:
            input('Invalid! Gotta enter 1 or 2.')
            time.sleep(1)
            print()

def times_sq():
    print()
    busy = """You feel like a busy New Yorker. It is bustling with life, tall skyscrapers and endless billboards.
You wonder what it would be like to live there..."""

    for char in busy:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()

    sike = """SIKE!

After 5 days, you realise you'd go broke if you stay any longer. You book a flight back to ICN and you're back home safely at Songdo. Hooray!"""

    for char in sike:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    restart()

def stat_lib():
    print()
    tour = "You feel like a typical New York tourist. It is all fun and games until..."

    for char in tour:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()
    print()

    broke = """After 5 days, you realise you'd go broke if you stay any longer. You book a flight to ICN and you're back home safely at Songdo. Hooray!"""

    for char in broke:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print()
    print()

    restart()
      
def restart():
  restart = input("Would you like to restart the game?")
  if restart == "yes" or restart == "y":
    startGame()
  if restart == "n" or restart == "no":
    print ("Game terminated. Goodbye.")
    
        


startGame()

restart()


# In[ ]:




