def average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)

def calculate_engagement_score(medicationDuration, stepsWalked, caloriesBurned, sleepDuration, waterIntake, 
                               step, calories, sleep, water):
    stepsArray = []
    sleepArray = []
    waterArray = []
    caloriesArray = []
    mdedicationArray = []
    
    n = len(stepsWalked)
    cnt=0
    score=0
    for i in range(n):
        if(cnt<7):
            cnt=1
            temp=(score/7)
            mdedicationArray.append(temp)
            score=0
            if(medicationDuration[i]):
                score=score+1
            else:
                score=score
                
        else:
            if(medicationDuration[i]):
                score=score+1
            else:
                score=score
            cnt=cnt+1
                
            
            
    for i in range(n):
        stepsRate = 100
        sleepRate = 100
        waterRate = 100
        caloriesRate = 100
        
        if stepsWalked[i] == step:
            stepsRate = 1
        else:
            stepsRate = abs(stepsWalked[i] - step) / step
            
        if caloriesBurned[i] == calories:
            caloriesRate = 1
        else:
            caloriesRate = abs(caloriesBurned[i] - calories) / calories
            
        if sleepDuration[i] == sleep:
            sleepRate = 1
        else:
            sleepRate = abs(sleepDuration[i] - sleep) / sleep
            
        if waterIntake[i] == water:
            waterRate = 1
        else:
            waterRate = abs(waterIntake[i] - water) / water
            
        stepsArray.append(stepsRate)
        sleepArray.append(sleepRate)
        waterArray.append(waterRate)
        caloriesArray.append(caloriesRate)
        
    stepsavg = average(stepsArray)    
    sleepavg = average(sleepArray)    
    wateravg = average(waterArray)    
    caloriesavg = average(caloriesArray)    
    medicationsavg = average(mdedicationArray)    

    engagementScore = ((stepsavg + sleepavg + wateravg + caloriesavg+medicationsavg) / 5) * 10
    return engagementScore
