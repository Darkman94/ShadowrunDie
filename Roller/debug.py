def debugRoller(isOn, num, hasEdge):
    """A Tool to debug the Rolls of the dice
    
    Parameters
    ----------
    isOn: Boolean
    determines whether or not the rolling debugger is on
    Num: Int
    refers to the result, is None if one seeks to just determine if the roller thinks its supposed to have edge
    hasEdge: Boolean
    refers to whether or not the die exploded
    """
    msg = ''
    if num is not None:
        msg += str(num)
    if hasEdge:
        msg += 'I think Im supposed to have edge'
    if isOn:
        print msg


def debugKnownCommentBuilder(commentId, already_done, isOn = True):
    """A tool to debug the known comments log
    
    Parameters
    ----------
    isOn: Boolean
    determines whether or not the rolling debugger is on
    commentId: String
    refers to the comment ID read from the text file, None if testing the set
    already_done: Set
    refers to the set
    """
    if already_done is None and isOn:
        print commentId
    elif isOn:
        print '================================================================'
        print already_done


def debugBuildReply(isOn, pool, hasEdge):
    """debug the reply builder
    
    Parameters
    ----------
    isOn: Boolean
    determines whether or not the rolling debugger is on
    pool: Int
    refers to the size of the pool being responded to
    has edge: Boolean
    refers to whether or not edge was spent on the roll
    """
    msg = ''
    if isOn:
        msg += 'I think someone wants me to roll with a dice pool of %d' % pool
        if hasEdge:
            msg += ' I think they have edge'
    print msg


def debugCommentLogger(isOn, commentId):
    """debug the comment logger responsible for building the local logs
    
    Parameters
    ----------
    isOn: Boolean
    determines whether or not the rolling debugger is on
    commentId: String
    refers to the comment ID read from the text file, None if testing the set
    """
    if isOn:
        print commentId
        print '\n'



