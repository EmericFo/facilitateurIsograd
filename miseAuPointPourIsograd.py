import sys, os
from colored import fg, bg, attr

# utiliser le essaiDebug.py pour lancer en débug
# prend en param le nom du repertoir où chercher les fichiers d'exemples input et output
# optionnel prend le numero d'un fichier précis e.g.: 3 => input3 output3



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


#---------------------------


def openFileToLines(filePath):
    with open(filePath, "r") as fichier:
        linesToRet = fichier.read().split("\n")
    return linesToRet

def print_green(content):
   print ('%s%s%s %s' % (fg('white'),  bg('green'), content, attr('reset'))) 

def print_red(content):
   print ('%s%s%s %s' % (fg('white'),  bg('red'), content, attr('reset'))) 


def testMoiCa(exo, i):
    #input
    inpulines = openFileToLines(exo+"/input"+i+".txt")

    # exo 
    toCompare = computeExercice(inpulines)

    # check 
    outputLines = openFileToLines(exo+"/output"+i+".txt")


    print(toCompare)
    print(outputLines)
    if toCompare == outputLines:
        print_green("cool")
    else:
        print_red("not cool")



if __name__ == '__main__':
    try: 
        exo = sys.argv[1] # nom de l'exo = repertoire avec le code python et les fichier sample inputN et outputN
        # si param pour cibler un fichier exemple précis
        numExemple = 0
        if len(sys.argv) > 2:
            numExemple = sys.argv[2]
        if int(numExemple) > 0:
            testMoiCa(exo, numExemple)
        # Parcour de tous les fichiers d'exemple
        else:
            nbFiles = len(os.listdir(exo))
            for i in range(1,int(nbFiles/2)+1):
                i = str(i)
                testMoiCa(exo, i)


    except Exception as e:
        print(e)
        print("fin des fichier a comparer")


