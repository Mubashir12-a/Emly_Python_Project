from Gameloop import gameLoop
from CL_Colors import *

#Variables Used:
#---------------------------------------------
Player_Mood = ''
ReturnDicision = ['RETURN', 'R', 'r']


# Function used to ask playerDecision:

#___________________________________________________________________
def IsPlayerReady():
    global Player_Mood
    
    print(f"{Magenta}Do you want to start the Game---")
    Player_Mood = input(f"{Yellow}Y/N OR RETURN/R/r: {White}")
#____________________________________________________________________
    

    

while(True):
    IsPlayerReady();
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    #Dev use only:
    if Player_Mood == 'm':
        exit(0)
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    
    if Player_Mood == 'Y' or Player_Mood == 'y':
        gameLoop()
        break
    
    if Player_Mood in ReturnDicision:
        exit(0)
        
        
print(White)