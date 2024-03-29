from fastapi import FastAPI, HTTPException
from model import *

app = FastAPI()

@app.get("/genrate_engagement_score")
async def main():
    try:
        stepsArray = [5000, 6000, 7000, 8000, 9000]
        sleepArray = [6, 7, 8, 7, 6]  
        waterArray = [2, 3, 2, 3, 2]  
        caloriesArray = [2000, 2200, 2100, 2300, 2200]
        
        stepthreshold = 3000
        sleepthreshold = 8
        watershreshold = 5
        caloriesshreshold = 3000
        
        score = calculate_engagement_score(stepsArray, caloriesArray, sleepArray, waterArray, 
                                           stepthreshold, sleepthreshold, watershreshold, caloriesshreshold)
        
        return {"engagement_score": score}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
