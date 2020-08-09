def companyBotStrategy(trainingData):
    l=0
    s=0.0
    for i in range(len(trainingData)):
        if trainingData[i][1]==1:
            s=s+trainingData[i][0]
            l=l+1
        else:
            continue
    if l>0:
        return s/l
    else:
        return 0.0

