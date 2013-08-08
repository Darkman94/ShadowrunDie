#import praw to deal with reddit
import praw
#import re to deal with regular expressions
import re
#import the comment logger, to deal with the logs
import logger
#import the method to build replies
import build_reply

def runBot():
    #build the reddit agent, and login
    #Input your User Agent here
    r = praw.Reddit(user_agent = '')
    #input your login info here
    r.login('', '')

    #find all the comments already analyzed
    already_done = logger.buildKnownComments()

    #perpetually check the comments
    while True:
        #go into the subreddit and get all the comments
        #Put your subreddit here
        subreddit = r.get_subreddit('test')
        comments = subreddit.get_comments()

        #loop through all the comments
        for comment in comments:

            #check to see if we've already analyzed a given comment, and ignore it if we have
            if comment.id not in already_done:
                #search through the comment's text for a roll command
                text = comment.body
                rolls = re.findall(r'ROLL \d\dE?', text)
                reply_text = ''

                for roll in rolls:
                    #build the reply
                    if roll is not None and roll.endswith('E') :
                        reply_text += build_reply.buildComment(True, roll[5:7])
                        reply_text += '\n'
                        reply_text += '\n'

                    elif roll is not None:
                        reply_text += build_reply.buildComment(False, roll[5:7])
                        reply_text += '\n'
                        reply_text += '\n'

                if reply_text != '':
                    comment.reply(reply_text)
                #add the comment's ID to both the log of the current run, and the log of all runs
                already_done.add(comment.id)
                logger.logComment(comment.id)

if __name__ == '__main__':
	runBot()
