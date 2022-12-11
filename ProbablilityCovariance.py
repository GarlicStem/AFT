def ProbabilityCovariance (conbinedProb,stag1,stag2):
    '''
    This function is used to calculate probability covariance between only two stages.
    conbinedProb is co-probability of 2 stages
    stag1 and stag2 mean payoffs in ever stage of stage 1 and stage 2 respectively
    '''
    import pandas as pd 
    data=pd.DataFrame({
    'conbinedProb':conbinedProb,
    'stag1':stag1,
    'stag2':stag2
    })
    if sum(conbinedProb)>1:
        print("Combined Probability is larger than 100%, please check")
    else: 
        stag1Mean=round(sum(data['stag1']*data['conbinedProb']),2)
        stag2Mean=round(sum(data['stag2']*data['conbinedProb']),2)
        Cov=sum(data['conbinedProb']*(data['stag1']-stag1Mean)*(data['stag2']-stag2Mean))
        print(Cov)
        return Cov