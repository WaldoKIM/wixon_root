from fastapi import FastAPI
from datetime import datetime
from test import *

app = FastAPI()

@app.get("/day", tags=["Dates"])
def get_day_of_week():
    """
    Get the current day of week
    """
    return {
        "day": datetime.now().strftime("%A")
    }

@app.get("/waldo")
async def root():
    return {"message": "Hello there!!!!"}    