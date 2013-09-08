#import the debugger
import debug

#TODO: Figure out why it doesn't always work
def buildKnownComments(filename = r'DATA/log.txt'):
    """A method to build the comments that the Die Roller has already swept through on a previous launch
    
    Parameters
    ----------
    filename: String
    refers to the name of the log file
    """
    #a variable to contain whether or not I want the bebugger running
    debug = True
    #build an empty set to contain the comments
    already_done = set()
    #open up the log to read
    txt = open(filename, 'r')
    #iterate through the lines in the log file
    for line in txt:
        #add the lines(each of which should refer to a unique comment id) to the set containg the already analyzed code
        already_done.add(line.strip())
        #debug the lines being read in the file reader
        #debug.debugKnownCommentBuilder(debug,line,None)
        print line
    #debug the set
    #debug.debugKnownCommentBuilder(commentID =  None,already_done = already_done)
    print already_done
    #return the set, now filled with all the comments already analyzed
    return already_done

#TODO: Check if this is the issue with the repetition of die rolls
def logComment(commentId, filename= r'DATA/log.txt'):
    """A Method to throw a comment into the log file
    
    Parameters
    ----------
    commentId: String
    is the id of the comment that has already been comepleted, to be put into the log
    filename: String
    is the name of the log file
    """
    #a varibale to determine whether or not to run the debugger
    debug = True
    #open up the file for appending
    txt = open(filename, 'a')
    #write the id to the log
    txt.write(commentId)
    #add a new line
    txt.write('\n')
    #debug.debugCommentLogger(debug, commentId)
    print commentId
    #print '/n'
