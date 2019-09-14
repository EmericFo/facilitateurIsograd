def computeExercice(lines):
    toret = []

    nbCarton = int(lines.pop(0))

    nbMonte = 1
    poidTo = 0

    for spoid in lines:
        poid = int(spoid)
        
        if poidTo+poid > 100:
            nbMonte +=1
            poidTo = 0
        poidTo += poid


   
    toret.append(str(nbMonte))
    
    return toret


#for result in computeExercice(lines):
#   print(result)
