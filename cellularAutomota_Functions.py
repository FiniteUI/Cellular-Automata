ringOneCells = {
    "NW": (-1, -1),
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0)
}

cardinalDirections = {
    "N": ringOneCells['N'],
    "E": ringOneCells['E'],
    "S": ringOneCells['S'],
    "W": ringOneCells['W']
}

ordinalDirections = {
    "NW": ringOneCells['NW'],
    "NE": ringOneCells['NE'],
    "SE": ringOneCells['SE'],
    "SW": ringOneCells['SW']
}

ringTwoCells = {
    "NW2": (-2, -2),
    "NNW": (-1, -2),
    "N2": (0, -2),
    "NNE": (1, -2),
    "NE2": (2, -2),
    "NEE": (2, -1),
    "E2": (2, 0),
    "SEE": (2, 1),
    "SE2": (2, 2),
    "SSE": (1, 2),
    "S2": (0, 2), 
    "SSW": (-1, 2),
    "SW2": (-2, 2),
    "SWW": (-2, 1),
    "W2": (-2, 0),
    "NWW": (-2, 1)
}

ringThreeCells = {
    "NW3": (-3, -3),
    "NNW2": (-2, -3),
    "NNNW": (-1, -3),
    "N3": (0, -3),
    "NNNE": (1, -3),
    "NNE2": (2, -3),
    "NE3": (3, -3),
    "NEE2": (3, -2),
    "NEEE": (3, -1),
    "E3": (3, 0),
    "SEEE": (3, 1),
    "SEE2": (3, 2),
    "SE3": (3, 3),
    "SSE2": (2, 3),
    "SSSE": (1, 3),
    "S3": (0, 3),
    "SSSW": (-1, 3),
    "SSW2": (-2, 3),
    "SW3": (-3, 3),
    "SWW2": (-3, 2),
    "SWWW": (-3, 1),
    "W3": (-3, 0),
    "NWWW": (-3, -1),
    "NWW2": (-3, -2),
}

def getCellInDirection(x, y, ca, direction):
    directionX = x + direction[0]
    directionY = y + direction[1]
    return ca.getCell(directionX, directionY)

def getNeighborCount(x, y, ca, directions):
    neighborCount = 0
    for i in directions:
        value = getCellInDirection(x, y, ca, directions[i])
        neighborCount += value

    return neighborCount

def getTouchingNeighborCount(x, y, ca, directions):
    touchingNeighborCount = 0
    lastValue = 0
    for i in directions:
        value = getCellInDirection(x, y, ca, directions[i])
        
        if value == 1 and lastValue == 1:
            touchingNeighborCount += 1
        
        lastValue = value

    #now check the last one
    value = getCellInDirection(x, y, ca, directions[list(directions)[0]])
    if value == 1 and lastValue == 1:
            touchingNeighborCount += 1

    return touchingNeighborCount

def getMaxConsecutiveTouchingNeighborCount(x, y, ca, directions):
    pass

def fourDirections_fourOrMore(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)

    result = ca.getCell(x, y)
    if cardinalLiveNeighbors == 4 or cardinalLiveNeighbors == 0:
        result = 1

    return result

def fourDirections_threeOrMore(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)

    result = ca.getCell(x, y)
    if cardinalLiveNeighbors >= 3:
        result = 1
    elif cardinalLiveNeighbors <= 1:
        result = 0

    return result

def fourDirections_twoOrMore(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)

    result = ca.getCell(x, y)
    if cardinalLiveNeighbors > 2:
        result = 1
    elif cardinalLiveNeighbors < 2:
        result = 0

    return result

def conway(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_1(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 4:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_2(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3 or liveNeighbors == 4:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_3(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 5:
            result = 0

    return result

def conway_modified_4(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 3:
            result = 0

    return result

def conway_modified_5(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    #now, if alive with < 2 live neighbors, die
    #if alive with 2 or 3 live neighbors, live
    #if live with 4 or more live neighbors, die
    #if dead with 3 live neighbors, live again

    #otherwise stay the same
    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 0
        else:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 1
        elif liveNeighbors >= 4:
            result = 1
        else:
            result = 0

    return result

def conway_modified_6(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 8:
            result = 0

    return result

def conway_modified_7(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 3:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 7:
            result = 0

    return result

def conway_modified_8(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 0:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 7:
            result = 0

    return result

def conway_modified_9(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 0:
            result = 1
    else:
        if liveNeighbors < 2:
            result = 0
        elif liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_10(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors == 0:
            result = 1
    else:
        #if liveNeighbors < 2:
            #result = 0
        if liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_11(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors < 2:
            result = 1
    else:
        #if liveNeighbors < 2:
            #result = 0
        if liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_12(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors < 3:
            result = 1
    else:
        if liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_13(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue

    if cellValue == 0:
        if liveNeighbors < 4:
            result = 1
    else:
        if liveNeighbors >= 4:
            result = 0

    return result

def conway_modified_14(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = ordinalLiveNeighbors + cardinalLiveNeighbors

    result = cellValue

    if cellValue == 0:
        if liveNeighbors < 4:
            result = 1
    else:
        if liveNeighbors >= 4 or (cardinalLiveNeighbors == 0 and ordinalLiveNeighbors > 0):
            result = 0

    return result

def conway_modified_15(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = ordinalLiveNeighbors + cardinalLiveNeighbors

    result = cellValue

    if cellValue == 0:
        if liveNeighbors < 4:
            result = 1
    else:
        if liveNeighbors >= 4 or (cardinalLiveNeighbors == 0 and ordinalLiveNeighbors > 0) or (ordinalLiveNeighbors == 0 and cardinalLiveNeighbors > 0):
            result = 0

    return result

def custom_1(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)

    result = cellValue
    if cellValue == 0:
        if liveNeighbors == 8:
            result = 1
    else:
        if liveNeighbors == 0:
            result = 0
    
    return result

def custom_2(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = ordinalLiveNeighbors + cardinalLiveNeighbors

    result = cellValue
    if cellValue == 0:
        if cardinalLiveNeighbors == 4 or ordinalLiveNeighbors == 4:
            result = 1
    else:
        if cardinalLiveNeighbors < 4 and ordinalLiveNeighbors < 4:
            result = 0
    
    return result

def custom_3(x, y, ca):
    cellValue = ca.getCell(x, y)

    #grab all 8 direction values
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = ordinalLiveNeighbors + cardinalLiveNeighbors

    result = cellValue
    if cellValue == 0:
        if cardinalLiveNeighbors >= 3 or ordinalLiveNeighbors >= 3:
            result = 1
    else:
        if cardinalLiveNeighbors < 3 and ordinalLiveNeighbors < 3:
            result = 0
    
    return result

def custom_4(x, y, ca):
    cellValue = ca.getCell(x, y)

    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = ordinalLiveNeighbors + cardinalLiveNeighbors

    result = cellValue
    if cellValue == 0:
        if ordinalLiveNeighbors == 4:
            result = 1
    else:
        if cardinalLiveNeighbors < 3 and ordinalLiveNeighbors < 3:
            result = 0
    
    return result

def scroll(x, y, ca, direction):
    if getCellInDirection(x, y, ca, direction) == 1:
        result = 1
    else:
        result = 0
    
    return result

def scroll_N(x, y, ca):
    return scroll(x, y, ca, ringOneCells['N'])

def scroll_NE(x, y, ca):
    return scroll(x, y, ca, ringOneCells['NE'])

def scroll_E(x, y, ca):
    return scroll(x, y, ca, ringOneCells['E'])

def scroll_SE(x, y, ca):
    return scroll(x, y, ca, ringOneCells['SE'])

def scroll_S(x, y, ca):
    return scroll(x, y, ca, ringOneCells['S'])

def scroll_SW(x, y, ca):
    return scroll(x, y, ca, ringOneCells['SW'])

def scroll_W(x, y, ca):
    return scroll(x, y, ca, ringOneCells['W'])

def scroll_NW(x, y, ca):
    return scroll(x, y, ca, ringOneCells['NW'])

def custom_5(x, y, ca):
    result = ca.getCell(x, y)
    if getCellInDirection(x, y, ca, ringOneCells['N']) == 1:
        result = 1
    
    return result

def custom_6(x, y, ca):
    result = ca.getCell(x, y)
    if getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 0:
        result = 1
    
    return result

def custom_7(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    else:
        result = 1
    
    return result

def custom_8(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    elif ringTwoNeighbors == 0:
        result = 1
    else:
        result = ca.getCell(x, y)
    
    return result

def custom_9(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    elif ringTwoNeighbors == len(ringTwoCells):
        result = 1
    else:
        result = ca.getCell(x, y)
    
    return result

def custom_10(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringOneNeighbors == 2:
        result = 0
    elif ringOneNeighbors == 6:
        result = 1
    else:
        result = ca.getCell(x, y)
    
    return result

def custom_11(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    elif ringOneNeighbors == 1:
        result = 1
    else:
        result = ca.getCell(x, y)
    
    return result

def custom_12(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    elif ringOneNeighbors == 1:
        result = 1
    else:
        result = 0
    
    return result

def custom_13(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == len(ringOneCells):
        result = 0
    elif ringOneNeighbors == 1 or ringOneNeighbors == 3:
        result = 1
    else:
        result = 0
    
    return result

def custom_14(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 1:
        result = 1
    else:
        result = 0
    
    return result

def custom_15(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 2:
        result = 1
    else:
        result = 0
    
    return result

def custom_16(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 3:
        result = 1
    else:
        result = 0
    
    return result

def custom_17(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 4:
        result = 1
    else:
        result = 0
    
    return result

def custom_18(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 5:
        result = 1
    else:
        result = 0
    
    return result

def custom_19(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 6:
        result = 1
    else:
        result = 0
    
    return result

def custom_20(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 7:
        result = 1
    else:
        result = 0
    
    return result

def custom_21(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 8:
        result = 1
    else:
        result = 0
    
    return result

def custom_22(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors == 0:
        result = 1
    else:
        result = 0
    
    return result

def custom_23(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 1:
        result = 1
    else:
        result = 0
    
    return result

def custom_24(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 8 and ringOneNeighbors == 0:
        result = 1
    else:
        result = 0
    
    return result

def custom_25(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 2:
        result = 1
    else:
        result = 0
    
    return result

def custom_26(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 3:
        result = 1
    else:
        result = 0
    
    return result

def custom_27(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 4:
        result = 1
    else:
        result = 0
    
    return result

def custom_28(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 5:
        result = 1
    else:
        result = 0
    
    return result

def custom_29(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 6:
        result = 1
    else:
        result = 0
    
    return result

def custom_30(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 7:
        result = 1
    else:
        result = 0
    
    return result

def custom_31(x, y, ca):
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    
    if ringTwoNeighbors == 8:
        result = 1
    else:
        result = 0
    
    return result

def custom_32(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors <= 1:
        result = 1
    else:
        result = 0
    
    return result

def custom_33(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors <= 2:
        result = 1
    else:
        result = 0
    
    return result

def custom_34(x, y, ca):
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    
    if ringOneNeighbors <= 3:
        result = 1
    else:
        result = 0
    
    return result

def custom_35(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        result = 0

    return result

def custom_36(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 1:
            result = 1
        else:
            result = 0

    return result

def custom_37(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 2:
            result = 1
        else:
            result = 0

    return result

def custom_38(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 3:
            result = 1
        else:
            result = 0

    return result

def custom_39(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 4:
            result = 1
        else:
            result = 0

    return result

def custom_40(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 5:
            result = 1
        else:
            result = 0

    return result

def custom_41(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 6:
            result = 1
        else:
            result = 0

    return result

def custom_42(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 7:
            result = 1
        else:
            result = 0

    return result

def custom_43(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        if getNeighborCount(x, y, ca, ringOneCells) == 8:
            result = 1
        else:
            result = 0

    return result

def custom_44(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  neighborCount >= 1 and neighborCount <= 2:
            result = 1
        else:
            result = 0

    return result

def custom_45(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  neighborCount >= 2 and neighborCount <= 3:
            result = 1
        else:
            result = 0

    return result

def custom_46(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  neighborCount >= 1 and neighborCount <= 3:
            result = 1
        else:
            result = 0

    return result

def custom_47(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  neighborCount >= 1 and neighborCount <= 2:
            result = 1
        elif neighborCount == 0:
            result = 0
        else:
            result = ca.getCell(x, y)

    return result

def custom_48(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount == 8:
            result = 1
        else:
            result = 0

    return result

def custom_49(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7:
            result = 1
        else:
            result = 0

    return result

def custom_50(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 6:
            result = 1
        else:
            result = 0

    return result

def custom_51(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 3) or neighborCount >= 7:
            result = 1
        else:
            result = 0

    return result

def custom_52(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        cardinalCount = getNeighborCount(x, y, ca, cardinalDirections)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7 or cardinalCount == 4:
            result = 1
        else:
            result = 0

    return result

def custom_53(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        ordinalCount = getNeighborCount(x, y, ca, ordinalDirections)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7 or ordinalCount == 4:
            result = 1
        else:
            result = 0

    return result

def custom_54(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        cardinalCount = getNeighborCount(x, y, ca, cardinalDirections)
        ordinalCount = getNeighborCount(x, y, ca, ordinalDirections)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7 or cardinalCount == 4 or ordinalCount == 4:
            result = 1
        else:
            result = 0

    return result

def custom_55(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    elif (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['N2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['S']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['S2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['E2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['W']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['W2']) == 1):
        result = 0
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7:
            result = 1
        else:
            result = 0

    return result

def custom_56(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringOneCells['S']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringOneCells['W']) == 1):
        result = 1
    elif (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['N2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['S']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['S2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['E2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['W']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['W2']) == 1):
           result = 1
    else:
        neighborCount = getNeighborCount(x, y, ca, ringOneCells)
        if  (neighborCount >= 1 and neighborCount <= 2) or neighborCount >= 7:
            result = 1
        else:
            result = 0

    return result

def custom_57(x, y, ca):
    if (getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['N2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['S']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['S2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['E2']) == 1) or (getCellInDirection(x, y, ca, ringOneCells['W']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['W2']) == 1):
           result = 1
    else:
        result = 0

    return result

def custom_58(x, y, ca):
    if ((getCellInDirection(x, y, ca, ringOneCells['N']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['N2']) == 1) and (getCellInDirection(x, y, ca, ringOneCells['S']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['S2']) == 1)) or ((getCellInDirection(x, y, ca, ringOneCells['E']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['E2']) == 1) and (getCellInDirection(x, y, ca, ringOneCells['W']) == 1 and getCellInDirection(x, y, ca, ringTwoCells['W2']) == 1)):
           result = 1
    else:
        result = 0

    return result

def custom_59(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 1:
        return 1
    else:
        return 0

def custom_60(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 2:
        return 1
    else:
        return 0

def custom_61(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 3:
        return 1
    else:
        return 0

def custom_62(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 4:
        return 1
    else:
        return 0

def custom_63(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 0:
        return 1
    else:
        return 0

def custom_64(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 1:
        return 0
    else:
        return 1

def custom_65(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 2:
        return 0
    else:
        return 1

def custom_66(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 3:
        return 0
    else:
        return 1

def custom_67(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 4:
        return 0
    else:
        return 1

def custom_68(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    if cardinalLiveNeighbors == 0:
        return 0
    else:
        return 1

def custom_69(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    if cardinalLiveNeighbors == ordinalLiveNeighbors:
        return 1
    else:
        return 0

def custom_70(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    if cardinalLiveNeighbors == ordinalLiveNeighbors:
        return 1
    else:
        return 0

def custom_71(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    if cardinalLiveNeighbors > ordinalLiveNeighbors:
        return 1
    else:
        return 0

def custom_72(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    if cardinalLiveNeighbors < ordinalLiveNeighbors:
        return 1
    else:
        return 0

def custom_73(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if cardinalLiveNeighbors == liveNeighbors:
        return 1
    else:
        return 0

def custom_74(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if cardinalLiveNeighbors != liveNeighbors:
        return 1
    else:
        return 0

def custom_75(x, y, ca):
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ordinalLiveNeighbors == liveNeighbors:
        return 1
    else:
        return 0

def custom_76(x, y, ca):
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ordinalLiveNeighbors != liveNeighbors:
        return 1
    else:
        return 0

def custom_77(x, y, ca):
    ordinalLiveNeighbors = getNeighborCount(x, y, ca, ordinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ordinalLiveNeighbors < liveNeighbors:
        return 1
    else:
        return 0

def custom_78(x, y, ca):
    cardinalLiveNeighbors = getNeighborCount(x, y, ca, cardinalDirections)
    liveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if cardinalLiveNeighbors < liveNeighbors:
        return 1
    else:
        return 0

def custom_79(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringOneLiveNeighbors == ringTwoLiveNeighbors:
        return 1
    else:
        return 0

def custom_80(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringOneLiveNeighbors != ringTwoLiveNeighbors:
        return 1
    else:
        return 0

def custom_81(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringOneLiveNeighbors > ringTwoLiveNeighbors:
        return 1
    else:
        return 0

def custom_82(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringOneLiveNeighbors < ringTwoLiveNeighbors:
        return 1
    else:
        return 0

def custom_83(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringOneLiveNeighbors == ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_84(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringOneLiveNeighbors != ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_85(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringOneLiveNeighbors > ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_86(x, y, ca):
    ringOneLiveNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringOneLiveNeighbors < ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_87(x, y, ca):
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringTwoLiveNeighbors == ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_88(x, y, ca):
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringTwoLiveNeighbors != ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_89(x, y, ca):
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringTwoLiveNeighbors > ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_90(x, y, ca):
    ringTwoLiveNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringTwoLiveNeighbors < ringThreeLiveNeighbors:
        return 1
    else:
        return 0

def custom_91(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 0:
        return 1
    else:
        return 0

def custom_92(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 1:
        return 1
    else:
        return 0

def custom_93(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 2:
        return 1
    else:
        return 0

def custom_94(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 3:
        return 1
    else:
        return 0

def custom_95(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 4:
        return 1
    else:
        return 0

def custom_96(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 5:
        return 1
    else:
        return 0

def custom_97(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 6:
        return 1
    else:
        return 0

def custom_98(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 7:
        return 1
    else:
        return 0

def custom_99(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 8:
        return 1
    else:
        return 0

def custom_100(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 9:
        return 1
    else:
        return 0

def custom_101(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 10:
        return 1
    else:
        return 0

def custom_102(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 11:
        return 1
    else:
        return 0

def custom_103(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 12:
        return 1
    else:
        return 0

def custom_104(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 13:
        return 1
    else:
        return 0

def custom_105(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 14:
        return 1
    else:
        return 0

def custom_106(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 15:
        return 1
    else:
        return 0

def custom_107(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 16:
        return 1
    else:
        return 0

def custom_108(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 17:
        return 1
    else:
        return 0

def custom_109(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 18:
        return 1
    else:
        return 0

def custom_110(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 19:
        return 1
    else:
        return 0

def custom_111(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 20:
        return 1
    else:
        return 0

def custom_112(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 21:
        return 1
    else:
        return 0

def custom_113(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 22:
        return 1
    else:
        return 0

def custom_114(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 23:
        return 1
    else:
        return 0

def custom_115(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors == 24:
        return 1
    else:
        return 0

def custom_116(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 0:
        return 1
    else:
        return 0

def custom_117(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 1:
        return 1
    else:
        return 0

def custom_118(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 2:
        return 1
    else:
        return 0

def custom_119(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 3:
        return 1
    else:
        return 0

def custom_120(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 4:
        return 1
    else:
        return 0

def custom_121(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 5:
        return 1
    else:
        return 0

def custom_122(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 6:
        return 1
    else:
        return 0

def custom_123(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 7:
        return 1
    else:
        return 0

def custom_124(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 8:
        return 1
    else:
        return 0

def custom_125(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 9:
        return 1
    else:
        return 0

def custom_126(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 10:
        return 1
    else:
        return 0

def custom_127(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 11:
        return 1
    else:
        return 0

def custom_128(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 12:
        return 1
    else:
        return 0

def custom_129(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 13:
        return 1
    else:
        return 0

def custom_130(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 14:
        return 1
    else:
        return 0

def custom_131(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 15:
        return 1
    else:
        return 0

def custom_132(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 16:
        return 1
    else:
        return 0

def custom_133(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 17:
        return 1
    else:
        return 0

def custom_134(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 18:
        return 1
    else:
        return 0

def custom_135(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 19:
        return 1
    else:
        return 0

def custom_136(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 20:
        return 1
    else:
        return 0

def custom_137(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 21:
        return 1
    else:
        return 0

def custom_138(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 22:
        return 1
    else:
        return 0

def custom_139(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors > 23:
        return 1
    else:
        return 0

def custom_140(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 1:
        return 1
    else:
        return 0

def custom_141(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 2:
        return 1
    else:
        return 0

def custom_142(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 3:
        return 1
    else:
        return 0

def custom_143(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 4:
        return 1
    else:
        return 0

def custom_144(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 5:
        return 1
    else:
        return 0

def custom_145(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 6:
        return 1
    else:
        return 0

def custom_146(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 7:
        return 1
    else:
        return 0

def custom_147(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 8:
        return 1
    else:
        return 0

def custom_148(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 9:
        return 1
    else:
        return 0

def custom_149(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 10:
        return 1
    else:
        return 0

def custom_150(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 11:
        return 1
    else:
        return 0

def custom_151(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12:
        return 1
    else:
        return 0

def custom_152(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 13:
        return 1
    else:
        return 0

def custom_153(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 14:
        return 1
    else:
        return 0

def custom_154(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 15:
        return 1
    else:
        return 0

def custom_155(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 16:
        return 1
    else:
        return 0

def custom_156(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 17:
        return 1
    else:
        return 0

def custom_157(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 18:
        return 1
    else:
        return 0

def custom_158(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 19:
        return 1
    else:
        return 0

def custom_159(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 20:
        return 1
    else:
        return 0

def custom_160(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 21:
        return 1
    else:
        return 0

def custom_161(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 22:
        return 1
    else:
        return 0

def custom_162(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 23:
        return 1
    else:
        return 0

def custom_163(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 24:
        return 1
    else:
        return 0

def custom_164(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 0:
        return 1
    else:
        return 0

def custom_165(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 1:
        return 1
    else:
        return 0

def custom_166(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 2:
        return 1
    else:
        return 0

def custom_167(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 3:
        return 1
    else:
        return 0

def custom_168(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 4:
        return 1
    else:
        return 0

def custom_169(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 5:
        return 1
    else:
        return 0

def custom_170(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 6:
        return 1
    else:
        return 0

def custom_171(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 7:
        return 1
    else:
        return 0

def custom_172(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 8:
        return 1
    else:
        return 0

def custom_173(x, y, ca):
    ringThreeLiveNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeLiveNeighbors < 12 and ringThreeLiveNeighbors > 9:
        return 1
    else:
        return 0

def custom_174(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 0:
        return 1
    else:
        return 0

def custom_175(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 1:
        return 1
    else:
        return 0

def custom_176(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 2:
        return 1
    else:
        return 0

def custom_177(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 3:
        return 1
    else:
        return 0

def custom_178(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 4:
        return 1
    else:
        return 0

def custom_179(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 5:
        return 1
    else:
        return 0

def custom_180(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 6:
        return 1
    else:
        return 0

def custom_181(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 7:
        return 1
    else:
        return 0

def custom_182(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching == 8:
        return 1
    else:
        return 0

def custom_183(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 0:
        return 1
    else:
        return 0

def custom_184(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 1:
        return 1
    else:
        return 0

def custom_185(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 2:
        return 1
    else:
        return 0

def custom_186(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 3:
        return 1
    else:
        return 0

def custom_187(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 4:
        return 1
    else:
        return 0

def custom_188(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 5:
        return 1
    else:
        return 0

def custom_189(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 6:
        return 1
    else:
        return 0

def custom_190(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 7:
        return 1
    else:
        return 0

def custom_191(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 1:
        return 1
    else:
        return 0

def custom_192(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 2:
        return 1
    else:
        return 0

def custom_193(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 3:
        return 1
    else:
        return 0

def custom_194(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 4:
        return 1
    else:
        return 0

def custom_195(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 5:
        return 1
    else:
        return 0

def custom_196(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 6:
        return 1
    else:
        return 0

def custom_197(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 7:
        return 1
    else:
        return 0

def custom_198(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 8:
        return 1
    else:
        return 0

def custom_199(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 2 and ringOneTouching < 5:
        return 1
    else:
        return 0

def custom_200(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching > 2 and ringOneTouching < 6:
        return 1
    else:
        return 0

def custom_201(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    if ringOneTouching < 2 and ringOneTouching > 0:
        return 1
    else:
        return 0

def custom_202(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ringOneNeighbors == ringOneTouching:
        return 1
    else:
        return 0

def custom_203(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ringOneNeighbors != ringOneTouching:
        return 1
    else:
        return 0

def custom_204(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ringOneNeighbors > ringOneTouching:
        return 1
    else:
        return 0

def custom_205(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringOneNeighbors = getNeighborCount(x, y, ca, ringOneCells)
    if ringOneNeighbors < ringOneTouching:
        return 1
    else:
        return 0

def custom_206(x, y, ca):
    ringTwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringTwoTouching == ringTwoNeighbors:
        return 1
    else:
        return 0

def custom_207(x, y, ca):
    ringTwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringTwoTouching != ringTwoNeighbors:
        return 1
    else:
        return 0

def custom_208(x, y, ca):
    ringTwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringTwoTouching < ringTwoNeighbors:
        return 1
    else:
        return 0

def custom_209(x, y, ca):
    ringTwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    ringTwoNeighbors = getNeighborCount(x, y, ca, ringTwoCells)
    if ringTwoTouching > ringTwoNeighbors:
        return 1
    else:
        return 0

def custom_210(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringThreeNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeTouching == ringThreeNeighbors:
        return 1
    else:
        return 0

def custom_211(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringThreeNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeTouching != ringThreeNeighbors:
        return 1
    else:
        return 0

def custom_212(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringThreeNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeTouching < ringThreeNeighbors:
        return 1
    else:
        return 0

def custom_213(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringThreeNeighbors = getNeighborCount(x, y, ca, ringThreeCells)
    if ringThreeTouching > ringThreeNeighbors:
        return 1
    else:
        return 0

def custom_214(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringThreeTouching == ringtwoTouching:
        return 1
    else:
        return 0

def custom_215(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringThreeTouching != ringtwoTouching:
        return 1
    else:
        return 0

def custom_216(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringThreeTouching > ringtwoTouching:
        return 1
    else:
        return 0

def custom_217(x, y, ca):
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringThreeTouching < ringtwoTouching:
        return 1
    else:
        return 0

def custom_218(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringOneTouching == ringtwoTouching:
        return 1
    else:
        return 0

def custom_219(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringOneTouching != ringtwoTouching:
        return 1
    else:
        return 0

def custom_220(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringOneTouching < ringtwoTouching:
        return 1
    else:
        return 0

def custom_221(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringtwoTouching = getTouchingNeighborCount(x, y, ca, ringTwoCells)
    if ringOneTouching > ringtwoTouching:
        return 1
    else:
        return 0

def custom_222(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    if ringOneTouching == ringThreeTouching:
        return 1
    else:
        return 0

def custom_223(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    if ringOneTouching != ringThreeTouching:
        return 1
    else:
        return 0

def custom_224(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    if ringOneTouching < ringThreeTouching:
        return 1
    else:
        return 0

def custom_225(x, y, ca):
    ringOneTouching = getTouchingNeighborCount(x, y, ca, ringOneCells)
    ringThreeTouching = getTouchingNeighborCount(x, y, ca, ringThreeCells)
    if ringOneTouching > ringThreeTouching:
        return 1
    else:
        return 0

def custom_226(x, y, ca):
    up = getCellInDirection(x, y, ca, cardinalDirections['N'])
    left = getCellInDirection(x, y, ca, cardinalDirections['W'])
    if up == left:
        return 1
    else:
        return 0

def custom_227(x, y, ca):
    up = getCellInDirection(x, y, ca, cardinalDirections['N'])
    left = getCellInDirection(x, y, ca, cardinalDirections['W'])
    if up != left:
        return 1
    else:
        return 0

def custom_228(x, y, ca):
    up = getCellInDirection(x, y, ca, cardinalDirections['N'])
    left = getCellInDirection(x, y, ca, cardinalDirections['W'])
    if up + left == 2:
        return 1
    else:
        return 0

def custom_229(x, y, ca):
    up = getCellInDirection(x, y, ca, cardinalDirections['N'])
    left = getCellInDirection(x, y, ca, cardinalDirections['W'])
    if up + left == 0:
        return 1
    else:
        return 0

def custom_230(x, y, ca):
    ne = getCellInDirection(x, y, ca, ordinalDirections['NE'])
    nw = getCellInDirection(x, y, ca, ordinalDirections['NW'])
    if ne + nw == 0:
        return 1
    else:
        return 0

def custom_231(x, y, ca):
    ne = getCellInDirection(x, y, ca, ordinalDirections['NE'])
    nw = getCellInDirection(x, y, ca, ordinalDirections['NW'])
    if ne + nw == 2:
        return 1
    else:
        return 0

def custom_232(x, y, ca):
    ne = getCellInDirection(x, y, ca, ordinalDirections['NE'])
    nw = getCellInDirection(x, y, ca, ordinalDirections['NW'])
    if ne == nw:
        return 1
    else:
        return 0

def custom_233(x, y, ca):
    ne = getCellInDirection(x, y, ca, ordinalDirections['NE'])
    nw = getCellInDirection(x, y, ca, ordinalDirections['NW'])
    if ne != nw:
        return 1
    else:
        return 0