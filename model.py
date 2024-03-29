def average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)

def calculate_engagement_score(stepsWalked, caloriesBurned, sleepDuration, waterIntake, 
                               step, sleep, water,calories):
    stepsArray = []
    sleepArray = []
    waterArray = []
    caloriesArray = []
    
    n = len(stepsWalked)
    
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
        
    for step in stepsArray:
        print(step)
        
    for step in sleepArray:
        print(step)
        
    for step in waterArray:
        print(step)
        
    for step in caloriesArray:
        print(step)
    stepsavg = average(stepsArray)    
    sleepavg = average(sleepArray)    
    wateravg = average(waterArray)    
    caloriesavg = average(caloriesArray)    

    engagementScore = ((stepsavg + sleepavg + wateravg + caloriesavg) / 4) * 10
    return engagementScore
