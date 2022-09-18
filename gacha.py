#--- Info ---#
'''
Credits : @MatsuTheBear
Program Version : 1.1 
Python Version : 3.10.7
TOS: 
    * YOU CAN use this program FREE TO USE
    * You CAN edit the code and improve it, or modify it for your necessities
    * You HAVE to credit me for the original code. 
    * Using this program, you accept that the author is not responsible for anything that could 
      happen. 

Check the documentation.pdf in the same directory to learn how the software works. The code IS 
documented well enough to let people with basic programming knowledge to understand how everything
works, but if you have any questions please DM me on Twitter @ MatsuTheBear

Keep in mind that everything you need to modify is in the COSTANTS section, everything else is automated
'''

#---Imports
import random #allows the generation of random numbers
import os #it's needed to interact with the OS libraries
import sys #allows the program to get the argument from CMD

#--- Costants 

# Percentage of X rank characters (example: rank R characters have a 70 percent chance of being pulled)
RARITY_R = 70 
RARITY_S = 25 
RARITY_SSS = 5 

#Number of coins/points the user will receive if the pull is unsuccessful
COIN_R = 500 
COIN_S = 2500
COIN_SSS = 10000

#Files of rarities (absolute path will be assigned later)
F_RARITY_R = 'tiers/r.txt'
F_RARITY_S = 'tiers/s.txt'
F_RARITY_SSS = 'tiers/sss.txt'

CHARACTER = "PUT YOUR CHARACTER HERE" #What users are pulling, default is "bear" for my channels
USERNAME = sys.argv[1] #username given from arguments of CMD + BAT
REROLLS = 5 #Number of rerolls the program will do if the character pulled was the same

#--- Variables 
characters = [] #Array of characters available from the file that will be selected
user_characters = [] #Array of characters the user has

check = True #Checks if the user has already the character pulled 

rank = '' #Rank of the character pulled
result = '' #result given from the random choice of rarity + character of said rarity
f_rank_selected = '' #File of the rank selected from the random rank choice

coins = 0 #default value of coins if no character is available

if __name__ == "__main__":
    #Generating an array of strings, then pulling one string randomly
    rarity =  ['R'] * RARITY_R + ['S'] * RARITY_S + ['SSS'] * RARITY_SSS
    rank = random.choice(rarity)
    match rank:
        case 'R': 
            f_rank_selected = os.path.join(sys.path[0], F_RARITY_R)
        case 'S': 
            f_rank_selected = os.path.join(sys.path[0], F_RARITY_S)
        case 'SSS': 
            f_rank_selected = os.path.join(sys.path[0], F_RARITY_SSS)
        case _:
            print("Error. No file found!\n")
    #File corrisponding the rank selected will be opened
    with open(f_rank_selected) as file:
        characters = file.readlines()
        characters = [character.rstrip() for character in characters] #Allows me to remove spaces and \n
    #Gets all the characters the user has
    user_file = os.path.join(sys.path[0], "users/") + USERNAME + ".txt" #user file where all the data is stored (characters obtained)
    #Try-Except: checks if i can open the user file, if not it creates a new one automatically
    try:
        file = open(user_file, "r")
        file.close
    except Exception as e:
        file = open(user_file, "w")
        file.close()
    with open(user_file,'r') as file:
        user_characters = file.readlines()
        user_characters = [user_character.rstrip() for user_character in user_characters]

    for i in range (REROLLS):
        #Having our array ready, we can have a new random number that will help us do the job
        try:
            result = characters[(random.randint(0,len(characters)-1))]
             #5 Checks if the character we pulled is already in the user list
            if result not in user_characters:
                check = False #this means i HAVE found a new character that the user does not have. 
                with open(user_file,"a") as file:
                    file.write(result + "\n")
                break #allows me to exit the cycle
        except Exception as e: 
            #The file is empty
            with open(user_file,"w") as file:
                file.write(result)
            break
    #Check if the flag check is true (so that means after the rerolls i did NOT found a new character to give to the user)
    with open(os.path.join(sys.path[0], 'result.txt'),"w")  as file:
        if check:
            match rank:
                case 'R':
                    coins = str(COIN_R)
                case 'S':
                    coins = str(COIN_S)
                case 'SSS':
                    coins = str(COIN_SSS)
            file.write("!currency add " + USERNAME + " " + coins)
        else:
            file.write("!gift " + USERNAME + " avatar " + result)
    #Depending on the result, 
    with open(os.path.join(sys.path[0], 'text-message.txt'),"w")  as file:
        #Check = True -> The user had already all the bears pulled even after N rerolls
        if check:
            file.write("Sorry " + USERNAME + "! You got " + coins + " coins instead of a " + CHARACTER + "!")
        else:
            file.write("Congratulations " + USERNAME + "! You got an " + rank + " rank  " + CHARACTER + "!")
    
    
