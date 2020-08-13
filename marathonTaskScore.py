def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    k=0
    l=0
    k=((submissions-1)*10)+((maxScore/2)*(1/marathonLength)*successfulSubmissionTime)
    l=maxScore-k
    if successfulSubmissionTime<0:
        return 0
    if l<(maxScore/2):
        return maxScore/2
    else:
        return l

