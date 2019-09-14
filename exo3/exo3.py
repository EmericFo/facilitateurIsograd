#------------------------- ici exercice ---------
def computeExercice(lines):
    toret = []

    tailleGrille = int(lines.pop(0))

    actualPos = [0,0] #row, colon

    bonusToKeep = []

    for numLine in range(0, tailleGrille):
        row = lines[numLine]
        for numCol in range(0, tailleGrille):
            cel = row[numCol]
            if cel == "o":
                go(actualPos, [numLine,numCol], toret)
                toret.append("x")
            elif cel == "*":
                bonusToKeep.append([numLine,numCol])


    for bToKeep in bonusToKeep:
        go(actualPos, bToKeep, toret)
        toret.append("x")

    toret = ["".join(toret)]

    return toret

def go(fromPos, toPos, posToRet):

    goOnRow(fromPos, toPos, posToRet)
    goOnCol(fromPos, toPos, posToRet)


def goOnRow(fromPos, toPos, rToRet):
    toR = toPos[1]
    if fromPos[1] < toR:
        fromPos[1] += 1
        rToRet.append(">")
        return goOnRow(fromPos, toPos, rToRet)
    elif fromPos[1] > toR:
        fromPos[1] -= 1
        rToRet.append("<")
        return goOnRow(fromPos, toPos, rToRet)
    return rToRet
    
def goOnCol(fromPos, toPos, cToRet):
    toC = toPos[0]
    if fromPos[0] < toC:
        fromPos[0] += 1
        cToRet.append("v")
        return goOnCol(fromPos, toPos, cToRet)
    elif fromPos[0] > toC:
        fromPos[0] -= 1
        cToRet.append("^")
        return goOnCol(fromPos, toPos, cToRet)
    return cToRet

#for result in computeExercice(lines):
#   print(result)

