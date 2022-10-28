import sys
sys.path.append("/code/./app/test")
import os 
path_dir = '/code/./app/' 
file_list = os.listdir(path_dir)


from fastapi import FastAPI
from datetime import datetime
# from . import test1 as t
import test0 as t2
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
    return {"message": sys.path}    


@app.get("/holy")
async def root():
    print(f'__file__ : {__file__}')
    print(file_list)
    return {"message": t2.sirLancelotsFavouriteColour()}    