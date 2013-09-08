#import the debugger
import debug
#import the built-in random functions to 'rol the dice'
from random import randint


def roll(num, ROS):
    """A function to roll for Shadowrun
    
    Parameters
    ----------
    num: Int
    refers to the size of the pool
    ROS: Boolean
    refers to whether or not the die is supposed to explode
    """
    #A variable to determine whether or not I want the debugger running
    debug = False
    #a tracker for the number of successes
    successes = 0
    #a tracker for the number of ones
    ones = 0
    #a tracker to figure out if there was a glitch
    glitch = False
    #a tracker for both the total number of Rolls to make and the current roll
    numRolls=num
    curRoll=0

    #Go through the rolling
    while curRoll < numRolls:
        #roll the dice
        roll = randint(1,6)
        #debug if neccessary
        #debug.debugRoller(debug, roll, False)

        #determine if the roll counts as a success
        if roll >= 5:
            #add to the number of successes
            successes += 1

            #see if the roll exploded
            if roll == 6 and ROS:
                #if it exploded, add to the number of rolls to do
                numRolls +=1
                #debug if neccessary
                #debug.debugRoller(debug, None, True)

        #if the roll is a one, add to the number of ones
        elif roll == 1:
            ones += 1
        #count which roll we're on
        curRoll +=1

    #see if there is a glitch
    if (ones/2) >= (num/2):
        glitch = True

    #build a tuple to contain the number of successes and if there is a glitch
    result = successes,glitch
    #retunr the tuple
    return result
