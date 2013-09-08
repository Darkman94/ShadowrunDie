#import the roller to roll the dice
import roller
#import the debugger
import debug


def buildComment(hasEdge, stringPool):
    """A method to build the comment to reply with
    
    Parameters
    ----------
    hasEdge: Boolean
    indicates if the person spent edge on the roll
    stringPool: String
    refers to the Pool Size as a String
    """

    #a variable to turn the debugger on and off
    debug = False

    #convert the pool size into a number
    pool = int(float(stringPool))

    #run the bebugger if neccessary
    #debug.debugBuildReply(debug, pool, hasEdge)

    #get the result of the roll
    result = roller.roll(pool, hasEdge)

    #start to build the reply, placing in the number of successes
    reply_text = 'You got %d successes' % result[0]

    #if the person had a glitch, indicate it in the repsonse
    if result[1]:
        reply_text += ', You also got a glitch'

    #add contact info to flag me if the bot is failing
    reply_text += r' If you think I screwed up contact /u/Mindflayer94'

    #return the reply
    return reply_text
