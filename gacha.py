#--- INFO ---#
"""""""""
Credits : @MatsuTheBear
Program Version : 1.1
Python Version : 3.10.7
TOS: 
    * YOU CAN use this program FREE TO USE
    * You CAN edit the code and improve it, or modify it for your necessities
    * You HAVE to credit me for the original code if you re-publish the modified version
    * Using this program, you accept that the author is not responsible for anything that could 
      happen. 

Check the documentation.pdf in the same directory to learn how the software works. The code IS 
documented well enough to let people with basic programming knowledge to understand how everything
works, but if you have any questions please DM me on Twitter @ MatsuTheBear

Keep in mind that everything you need to modify is in the COSTANTS section, everything else is automated

CHANGELOGS:

* Version 1.1 
-Fixed I/O problems
-Creation of Folders - Files automated
-More functions, less code on main 
-Function for setup, if needed
-Function for giving all avatars automatically, if everything falls apart
-Implementation of Gears - to be tested

* Version 1.0 
"""
#---IMPORTS ---#
import random #allows the generation of random numbers
import os #it"s needed to interact with the OS libraries
import sys #allows the program to get the argument from CMD


#--COSTANTS ---#

########################################    MODIFY HERE   #########################################################
# Percentage of X rank characters (example: rank R characters have a 70 percent chance of being pulled)
RARITY_R = 70 
RARITY_S = 25 
RARITY_SSS = 5 

#Number of coins/points the user will receive if the pull is unsuccessful
COIN_R = 500 
COIN_S = 2500
COIN_SSS = 10000

REROLLS = 5
###################################################################################################################
#Directory
DIRECTORY_ = sys.path[0]
#--Functions 

def gachasetup():
    """""""""
    Input: None 
    Output: int 

    GachaSetup: function that creates all files and folders if is called. The directory should be 
    as shown in the document. Best to use if everything falls apart or you are not sure there 
    are files missing
    """
    #Creation of tiers/users folders
    """""""""
    This part is kinda simple to understand: it reads all the folders and txt files that the directory
    should have from a "setup" file. If the line read does not contain "txt" in it, is a folder, 
    else is a file. This function only creates empty files.
    """
    setup = os.path.join(DIRECTORY_, "txt-files/setup.txt")
    with open(setup) as input_file:
        strings = input_file.readlines()
        strings = [string.rstrip() for string in strings]
    # Reads N strings for the setup txt file, and based on the presence of "txt" or not, it creates folders or txt files. 
    for i in range(len(strings)-1):
        if (strings[i] != ""):
            output_result = os.path.join(DIRECTORY_, strings[i])
        if os.path.exists(output_result) == False:
            if "txt" in strings[i]:
                with open(os.path.join(DIRECTORY_,output_result),"w"): pass 
            else:
                os.mkdir(os.path.join(DIRECTORY_,output_result))
    return 0

def getTier(chance_R,chance_S,chance_SSS):
    """
    Input: int,int,int - Each corresponding to the % of getting a particular rank
    Output: string 
    getTier: The function will return a random rank based on the chances chosen
    """
    chance_total = chance_R + chance_S + chance_SSS
    result = random.randint(1, chance_total)
    threshold = chance_R
    if result <= threshold:
        return "r"    
    threshold = threshold + chance_S
    if result <= threshold:
        return "s"
    return "sss"

def getReward(username,rank,type):
    """
    Input: string, string, int
    Output: string
    getReward: function that given the username and the directory (directory of avatar/gear + rank), returns the reward (avatar or gear). Returns empty string 
    if an error occurred
    """
    check = True
    directory = ""
    result = ""
    rank += ".txt"
    #Check the type given by as argument
    if type == "avatar":
        directory = os.path.join(DIRECTORY_, ("avatar-tiers/" + rank))
    elif type == "gear":
        directory = os.path.join(DIRECTORY_, ("gear-tiers/" + rank))
    else:
        #The type given is incorrect, thus giving later an error message
        return result
    #Reads all the characters in the file of the rank gotten, given as input
    with open(directory) as file:
        characters = file.readlines()
        characters = [character.rstrip() for character in characters] #Allows me to remove spaces and \n 
    user_file = os.path.join(DIRECTORY_ , ("users/" + typeReward + "/"+ username + ".txt"))

    #If the user exists, it will pass, else it will create a new file
    if os.path.exists(user_file) == False:
        with open(user_file, "w"): pass
    #Checks if the user has already the character
    with open(user_file,"r") as file:
        user_characters = file.readlines()
        user_characters = [user_character.rstrip() for user_character in user_characters]
        #If the length of the list of avatar characters(available to pull, not the user ones) is 0, that means the file is empty
        if len(characters) > 0:
            for i in range (REROLLS):
                #Having our array ready, we can have a new random number that will help us do the job
                position = random.randint(0,len(characters)-1)
                result = characters[position]
                #5 Checks if the character we pulled is already in the user list
                if result not in user_characters:
                    check = False #this means i HAVE found a new character that the user does not have. 
                    break #allows me to exit the cycle
        if check:
            result = "Coins"
    return result

def resetFiles():
    """
    Input: None
    Output: int
    resetFiles: resets result and message files to avoid I/O problems. 
    """
    #To be sure there are no old data read, file are resetted every time
    with open(os.path.join(DIRECTORY_, "txt-files/result.txt"),"w") as file: pass 
    with open(os.path.join(DIRECTORY_, "txt-files/message.txt"),"w") as file: pass 
    return 0

#--- MAIN ---#
if __name__ == "__main__":
    #This is mostly used for rare cases. If you launch the program, no error will be visible, but helps also with setup if something is missing
    if (len(sys.argv) <= 2):
        gachasetup()
        with open(os.path.join(DIRECTORY_, "txt-files/result.txt"),"w") as fileReward:
            fileReward.write("Error: not enough arguments") 
    else:
        #Reset of files
        resetFiles()
        #Data from cmd argv
        """
        argv is the list of arguments given from CMD or Terminal
        argv[0] = gacha.py
        argv[1] = username
        argv[2] = Type of reward, "avatar" or "gear"
        """
        username = sys.argv[1] 
        typeReward = sys.argv[2]
        #Gets rank + result
        rank = getTier(RARITY_R,RARITY_S,RARITY_SSS)
        reward = getReward(username,rank,typeReward)
        with open(os.path.join(DIRECTORY_, "txt-files/result.txt"),"w") as fileReward:
            if reward != "":
                if reward != "Coins":
                    """
                    If the reward is not "Coins", that means the function getReward found an avatar/gear to give to the user
                    """
                    if (typeReward == "avatar"):
                        fileReward.write("!gift " + username + " avatar " + reward)
                    elif (typeReward == "gear"):
                        fileReward.write("!gift " + username + " gear " + reward)
                    """
                    Writes the result on the user file too, so next time it does not give back again the same result accidentally
                    """
                    user_file = os.path.join(DIRECTORY_ , ("users/" + typeReward + "/"+ username + ".txt"))
                    with open(user_file,"a") as file_user:
                        file_user.write(reward + "\n")

                    with open(os.path.join(DIRECTORY_, "txt-files/message.txt"),"w") as fileMessage:
                        fileMessage.write("Congratulations " + username + "! You got a " + rank + " rank " + typeReward +"!")
                else:
                    coins = 0
                    """
                    Match - Catch do NOT work with TouchPortal on macOS for some reason??? I gave up at this point 

                    Also! Based on the rank, it will get back 
                    """
                    if (rank == "r"):
                        coins = COIN_R
                    elif (rank == "s"):
                        coins = COIN_S
                    else:
                        coins = COIN_SSS
                    
                    fileReward.write("!currency add " + username + " " + str(coins))
                    with open(os.path.join(DIRECTORY_, "txt-files/message.txt"),"w") as fileMessage:
                        fileMessage.write("Oh no " + username + "! You did not get a" + typeReward + ", but you got instead " + coins + "coins!")
            else:
                fileReward.write("Error: no avatar/gear was available to be pulled for the rank selected: " + rank)