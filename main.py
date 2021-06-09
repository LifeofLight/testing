<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.param_functions import Depends

app =FastAPI()
@app.get('/bmi')
def bmi(h:int=170 , w:int=50):

    h=(h/100)**2
    bmi =w/h


=======
from fastapi import FastAPI
from fastapi.param_functions import Depends

app =FastAPI()
@app.get('/bmi')
def bmi(h:int=170 , w:int=50):

    h=(h/100)**2
    bmi =w/h


>>>>>>> 56478962320c8bdbf4a185e8df027ec973f9f6d1
    return{'bmi':bmi}