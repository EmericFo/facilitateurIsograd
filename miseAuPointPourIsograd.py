import sys, os
from colored import fg, bg, attr

# utiliser le essaiDebug.py pour lancer en débug
# prend en param le nom du repertoir où chercher les fichiers d'exemples input et output
# optionnel prend le numero d'un fichier précis e.g.: 3 => input3 output3



#------------------------- ici exercice ---------
def computeExercice(lines):
    toret = []

    nb = int(lines.pop(0))

    


    return toret

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


