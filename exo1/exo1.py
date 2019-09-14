def computeExercice(lines):
    toret = []

    placeStart = int(lines.pop(0))

    for km in lines:
        ayanDep, aiDep = km.split(" ")
        placeStart += int(ayanDep)
        placeStart -= int(aiDep)


    if placeStart <= 100:
        toret.append("1000")
    elif placeStart <= 10000:
        toret.append("100")
    else:
        toret.append("KO")
    
    return toret


#for result in computeExercice(lines):
#   print(result)


------------

