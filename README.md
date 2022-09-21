# GachaForStreamAvatars
## _A python code that allow streamers to enhance StreamAvatars_

Welcome in everyone! This code will allow you to have a gacha system for your streams. Everything is automated, you just need to modify some values and you are ready to go! Everything you need to know is listed here, but for any questions you can DM me on Twitter @ [MatsuTheBear](https://www.twitter.com/matsuthebear)

# The setup documentation can be found [here](https://docs.google.com/document/d/1s2L_c_BogA7PO-dNZSuwOFGtCvfCFEBSfk6tUzW9PeA/edit?usp=sharing) (available also in the same directory on Setup.pdf)
# Requirements 
* A macro control program that __can launch .bat files, get data from channel points and set Twitch usernames as arguments for said .bat file__ (Touch Portal was used)
* Python 3.10+
* Windows (the code is not yet tested on Linux/Mac OS)
* StreamAvatars (of course)

# Directory
The directory of the file should be as shown here: 
```
├───tiers
│   └───r.txt
│   └───s.txt
│   └───sss.txt
└───users
└───gacha.py
└───result.txt
└───run.bat
└───text.message.txt
```
__Tiers__ : folder containing three (3) files, each containing a different "rank". They are R,S and SSS, and each one contains, for each row, the name of the file

Example: in my S.txt file, there are 4 rank S bears. For each bear, there is an assigned row
```
CursedBear
DemonBear
HeartBear
PatchedBear
```

__Users__ : folder containing all users that have redeemed the gacha feature. For each user, a txt file is created. In each txt file, there are all the characters a user pulled. The structure is equal to rank txt files

__gacha__ : python file containing the code

__result__: txt file containing the !command (!gift avatar or !currency add) that will be displayed in Twitch chat

__run__ : bat file that is used to pass the Twitch username as argument for the python file

__text_message__ : txt file containing the message that will be displayed in Twitch chat

# VALUES YOU HAVE TO MODIFY
__These are all the values you need to modify in order to personalize your channel. You don't have to edit anything else (unless you want to modify particular things, like the name of the files__)

__RARITY_R, RARITY_S, RARITY_SSS__ :  % of getting a X rank character (default 70, 25, 5, corresponding to 70%, 25% and 5%)

__COIN_R, COIN_S, COIN_SSS__ : Number of coins/points the user will receive if the pull is unsuccessful (default 500, 2500, 10000)

__CHARACTER__ : name of your characters (in my case "bear")

__REROLLS__ : number of "pulls" the program will do before giving coins to the user

# FAQ
__What is the licence of this software?__ 

* You can use this software free to use, __forever__ , without having to pay or tip me. 
* It is not required (but suggested) to credit me if you use the software or edit it. 
* You CANNOT sell the code
* You cannot claim the original code as your own.

__Why there are so many txt files?__ 

I found out that it's easier for me to manage everything by dividing all the data in multiple files, insteaf of having everything on one single file. 

__Can I use your bear avatars?__ 

No

__StreamAvatars has a Loot feature, and there is a Gacha tutorial for that, why you wrote this code?__ 

Is it true that StreamAvatars has a loot feature, that you can check [here](https://docs.streamavatars.com/stream-avatars/content-creating/creating-lootboxes), but there are some reason why I opted for custom code: 
* StreamAvatars' lootbox feature works only with gears/accessories (as far as I know)
* Lootbox's feature works best for Bosses/Battle Royales
* You still have to write down the code if you want to gift avatars/gear, so why not use a macro software for that?
* StreamAvatars can't check if someone has ALREADY an avatar or a weapon/gear (This was my main reason to create the code)
* My code allows people to swap the rarity of avatars easily, just cut and paste the row in a different file and you are ready!

__Can i contact you if I have any problems or questions to ask?__ 

__Yes!__ Please do so on my DMs at my [Twitter page](https://www.twitter.com/matsuthebear)

# Planned Updates 
## Version 1.1 (mid October)
* Gears feature included
* Remake of the Setup page, including the setup for BikuBot, LioranBoard and more 
* Compatibility with Linux / Mac OS Operating Systems 

## Version 1.2 (November)
* Have the entire code as a Class
* Compatibility with Youtube Gaming
* Creation of all missing files + folder automated 
* Clean up of the code
* Java Version (tbd - not planned immediately)
