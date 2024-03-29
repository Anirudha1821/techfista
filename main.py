from fastapi import FastAPI, HTTPException
from model import *
from typing import List

app = FastAPI()

@app.post("/generate_engagement_score")
async def main(
    medicineArray: List[bool], 
    stepsArray: List[int], 
    sleepArray: List[int], 
    waterArray: List[int], 
    caloriesArray: List[int],
    stepthreshold: int, 
    sleepthreshold: int, 
    watersthreshold: int, 
    caloriessthreshold: int
):
    try:
        score = calculate_engagement_score(
            medicineArray, 
            stepsArray, 
            caloriesArray, 
            sleepArray, 
            waterArray, 
            stepthreshold, 
            sleepthreshold, 
            watersthreshold, 
            caloriessthreshold
        )
        
        return {"engagement_score": score}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000, debug=True)
