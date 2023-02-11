#-- Info --#

"""
Credits: MatsuTheBear 
Program Version: 1.1b
Python Version: 3.10.7

TOS 

- The software is provided as is. I don't take responsability in any damage caused by any wrong usage of the software
- You can use the software free to use, both for personal and professional use (this includes Twitch, Youtube, Facebook, etc...)
- You can edit the code as you like. If you upload modified code, you have to link the github of the original code 
- You are not allowed to sell the code, even if you modify it

Changelogs can be viewed in the Github page


Info for users

- Variables you have to modify are inside the "CONSTANTS" section below. Everything else is automated. 
- If you don't care about the Log strings during running time (useful for checking errors), set it to False
"""

#--Imports 
import random
import os 
import sys 

#-- Constants --#

#Characters pull rate -> 70 = 70% -> sum must be 100 
Char_Rarity_R = 70
Char_Rarity_S = 25 
#Char_Rarity_SSS = 5 -> not used 

Gear_Rarity_R = 70
Gear_Rarity_S = 25 
#Gear_Rarity_SSS = 5  -> not used 

Coins_R = 500
Coins_S = 2500
Coins_SSS = 10000

Rerolls = 5 

Dir_ = sys.path[0] #You can put another dir if you like

Log_Check = True #Put this at true if you want to test the program without using a macro software

#-- Functions --#
def setFilesToEmpty(): 

    if Log_Check:
        print("OK | setFilesToEmpty(): function called  ")

    with open(os.path.join(Dir_,"files/message.txt"), "w"): pass 
    with open(os.path.join(Dir_,"files/reward.txt"), "w"): pass 

    if Log_Check:
            print("OK | setFilesToEmpty(): function closed ")

    return 0

def setGacha():
    if Log_Check:
            print("OK | setGacha(): function started ")
    try:
        setup = os.path.join(Dir_, "files/setup.txt")
        with open(setup) as input_file:
            setupStrings = input_file.readlines()
            setupStrings = [setupString.rstrip() for setupString in setupStrings]
        # Reads N strings for the setup txt file, and based on the presence of "txt" or not, it creates folders or txt files. 
        for i in range(len(setupStrings)-1):
            if (setupStrings[i] != ""):
                output_result = os.path.join(Dir_, setupStrings[i])
            if os.path.exists(output_result) == False:
                if "txt" in setupStrings[i]:
                    with open(os.path.join(Dir_,output_result),"w"): pass 
                else:
                    os.mkdir(os.path.join(Dir_,output_result))
    except Exception as e:
        if Log_Check:
            print("ERROR | setGacha(): " + str(e))
            return 1
    if Log_Check:
            print("OK | setGacha(): function closed  ")
    return 0

def setRecovery(username, typeReward):
    if Log_Check:
            print("OK | setRecovery(): function called ")
    userDir = os.path.join(Dir_, ("users/" + typeReward + "/" + username + ".txt"))
    if not os.path.exists(userDir):
        if Log_Check:
            print("ERROR | setRecovery(): user does not exist")
        return None 
    try:
        with open(userDir, "r") as userFile:
            userRewards = userFile.readlines()
            userRewards = [userReward.rstrip() for userReward in userRewards] #Cleanup of strings 

        recoveryDir = os.path.join(Dir_, ("files/recovery.txt"))
        with open(recoveryDir, "a") as recoveryFile:
            for i in range(len(userRewards) - 1):
                recoveryFile.write("!gift " + username + " " + typeReward + " " + userRewards[i])
    except Exception as e:
        print("ERROR | setRecovery(): " + str(e)) #Try-catch 
        return 1

    if Log_Check:
        print("OK | setRecovery(): function closed ")
    return 0

def setReward(username, typeReward, reward, rarity):

    if Log_Check:
        print("OK | setReward(): function called  ")  

    try:
        with open(os.path.join(Dir_, "files/reward.txt"),"w") as fileReward:
            fileReward.write("!gift " + username + " " + typeReward + " " + reward)

        user_file = os.path.join(Dir_ , ("users/" + typeReward + "/"+ username + ".txt"))
        if (os.path.exists(user_file)):
            with open(user_file,"a") as file_user:
                file_user.write(reward + "\n")
        else:
            with open(user_file,"w") as file_user:
                file_user.write(reward + "\n")

        with open(os.path.join(Dir_, "files/message.txt"),"w") as fileMessage:
            fileMessage.write("Congratulations " + username + "! You got a " + rarity + " rarity " + typeReward +"!")

        if Log_Check:
            print("OK | setReward(): reward setted correctly, function closed  ")
    except Exception as e:
        if Log_Check:
            print("ERROR | setReward(): " + str(e))
    return 0

def setCoins(username, rarity):

    if Log_Check:
        print("OK | setCoins(): function called  ")

    coins = 0 
    match(rarity):
        case ('r'):
            coins = Coins_R
        case('s'):
            coins = Coins_S
        case('sss'):
            coins = Coins_SSS

    with open(os.path.join(Dir_, "files/reward.txt"),"w") as fileReward:
        fileReward.write("!currency add " + username + " " + str(coins))
    with open(os.path.join(Dir_, "files/message.txt"),"w") as fileMessage:
        fileMessage.write("Oh no " + username + "! You did not get a " + typeReward + ", but you got instead " + str(coins) + " coins!")

    if Log_Check:
        print("OK | setCoins(): function ended  ")

    return 0



def getRarity(chanceR, chanceS):

    if Log_Check:
        print("OK | getRarity(): function called  ")

    """
    I'm assuming the sum of all the chances is 100. If not, the program will of course have problems. 
    There are different thresholds, and if-immediate is the fastest option for this case 
    """
    chanceNum = random.randint(1,100) 
    if Log_Check:
        print("OK | getRarity() returned value: " + str(chanceNum) + ", function closed ") 
    if chanceNum <= chanceR:
        return 'r'
    elif chanceNum <= chanceR + chanceS:
        return 's'
    else:
        return 'sss'

def getReward(username, rarity, typeReward):

    if Log_Check:
        print("OK | getReward(): function called  ")

    typeDir = ""
    match(typeReward):
        case ("avatar"):
            typeDir = os.path.join(Dir_, ("avatars/" + rarity + ".txt"))
        case ("gear"):
            typeDir = os.path.join(Dir_, ("gears/" + rarity + ".txt"))
        case _:
            if Log_Check:
                print("ERROR | getReward(): TypeReward is not avatar or gear, returning None... ")
            return None #In case of errors, the function returns null
    try:
        with open(typeDir, "r") as rewardsFile:
            rewards = rewardsFile.readlines()
            rewards = [reward.rstrip() for reward in rewards] #Cleanup of strings 
    except Exception as e:
        if Log_Check:
            print("ERROR | getReward(): " + str(e)) #Try-catch 


    userDir = os.path.join(Dir_, ("users/" + typeReward + "/" + username + ".txt"))
    if not os.path.exists(userDir):
        with open(userDir, "w"): pass

    with open(userDir, "r") as userFile:
        userRewards = userFile.readlines()
        userRewards = [userReward.rstrip() for userReward in userRewards] #Cleanup of strings 

        if Log_Check:
            print("OK | getReward(): strings obtained: typeReward " + typeReward + " and user " + username +" ")

        try:
            for i in range(0,Rerolls):
                #Gets random reward from pull
                resultReward = random.choice(rewards)
                #Checks if the user has already it 
                if resultReward not in userRewards:
                    if Log_Check:
                        print("OK | getReward(): Found a reward, function closed  ") #Try-catch 
                    return resultReward #Return automatically exits from the function
            if Log_Check:
                print("OK | getReward(): no rewards found, giving coins instead, function closed  ") #Try-catch 
            return "Coins"
        except Exception as e:
            if Log_Check:
                print("ERROR | getReward(): " + str(e)) #Try-catch 
            return None #Error if the file is empty


#-- Main --#
if __name__ == "__main__":
    if len(sys.argv) >= 3 :
        username = sys.argv[1]
        typeReward = sys.argv[2]

        if Log_Check:
            print("OK | Main: got arguments: " + username + " " + typeReward) 
        if typeReward == "recovery":
            setRecovery(username, "avatar")
            setRecovery(username, "gear")
        else:    
            rarity = ""
            match(typeReward):
                case ("avatar"):
                    rarity = getRarity(Char_Rarity_R,Char_Rarity_S)
                case ("gear"):
                    rarity = getRarity(Gear_Rarity_R,Gear_Rarity_S)
            reward = getReward(username, rarity, typeReward)
            setFilesToEmpty()

            if reward is not None:
                if reward != "Coins":
                    if Log_Check:
                        print("OK | Main: got reward " + reward + ", starting setReward...")
                    setReward(username, typeReward, reward, rarity)
                else:
                    if Log_Check:
                        print("OK | Main: got coins, starting SetCoins...")
                    setCoins(username, rarity)
            else:
                if Log_Check:
                    print("ERROR | Main: reward is None, expected Coins or Reward. Check getReward()  ")
    else:
        if Log_Check:
            print("WARNING | Main: no arguments given. Starting setGacha()")
        setGacha()
            








        

