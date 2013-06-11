#A Tool to debug the Rolls of the dice
#isOn determines whether or not the rolling debugger is on
#Num refers to the result, is None if one seeks to just determine if the roller thinks its supposed to have edge
#hasEdge, refers to whether or not the die exploded
def debugRoller(isOn, num, hasEdge):
    msg = ''
    if num is not None:
        msg += str(num)
    if hasEdge:
        msg += 'I think Im supposed to have edge'
    if isOn:
        print msg

#A tool to debug the known comments log
#isOn determines whether or not the rolling debugger is on
#commentId refers to the comment ID read from the text file, None if testing the set
#already_done refers to the set
def debugKnownCommentBuilder(commentId, already_done, isOn = True):
    if already_done is None and isOn:
        print commentId
    elif isOn:
        print '================================================================'
        print already_done

#debug the reply builder
#isOn determines whether or not the rolling debugger is on
#pool refers to the size of the pool being responded to
#has edge refers to whether or not edge was spent on the roll
def debugBuildReply(isOn, pool, hasEdge):
    msg = ''
    if isOn:
        msg += 'I think someone wants me to roll with a dice pool of %d' % pool
        if hasEdge:
            msg += ' I think they have edge'
    print msg

#debug the comment logger responsible for building the local logs
#isOn determines whether or not the rolling debugger is on
#commentId refers to the comment ID read from the text file, None if testing the set
def debugCommentLogger(isOn, commentId):
    if isOn:
        print commentId
        print '\n'



