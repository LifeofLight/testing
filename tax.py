from fastapi import FastAPI
from fastapi.param_functions import Depends

app =FastAPI()
@app.get('/tax')
def tax(income:int=50000, disabilities:int=0,coupple:int=0,parents:int=1,chile:int=1,agepF:int=60,agepM:int=55,income_pF:int=200,income_pM:int=200,income_c:int=0):
    income_pF=income_pF*12
    income_pM=income_pM*12
    income_p=[income_pF,income_pM]
    agep=[agepF,agepM]
    income_c=income_c*12
    money_Per_Year=income*12
    money_Per_Year=decresstex(money_Per_Year,disabilities,parents,agep,income_p,coupple,income_c,chile)
    tax =caltax(money_Per_Year)


    return{'tax':tax,'money_Per_Year':money_Per_Year}

def decresstex(money_Per_Year,disabilities,parents,agep,income_p,coupple,income_c,chile):
    money_Per_Year=money_Per_Year-60000
    count=0
    j=0
    if(disabilities==1):
        money_Per_Year=money_Per_Year-60000
    if coupple==1&income_c==0:
        money_Per_Year=money_Per_Year-60000
    if chile<2:
        money_Per_Year=money_Per_Year-30000
    elif chile>=2:
        money_Per_Year=money_Per_Year-(60000*chile)
    if parents==1:
        for i in agep:
            if i>=60:
                if income_p[j]<=30000:
                    count=count+1
            j=j+1
    money_Per_Year=money_Per_Year-30000*count

    return money_Per_Year

def caltax(money_Per_Year):
    if money_Per_Year>5000000:
      money_Per_Year=money_Per_Year-4000000
      tex= (money_Per_Year*0.35)+1265000
    elif money_Per_Year>2000000:
      money_Per_Year =money_Per_Year-2000000
      tex= (money_Per_Year*0.3)+365000
    elif(money_Per_Year>1000000):
      money_Per_Year =money_Per_Year-1000000
      tex= (money_Per_Year*0.25)+115000
    elif money_Per_Year>750000:
        money_Per_Year =money_Per_Year-750000
        tex=(money_Per_Year*0.2)+65000
    elif money_Per_Year>500000:
        money_Per_Year =money_Per_Year-500000
        tex= (money_Per_Year*0.15)+27500
    elif money_Per_Year>300000:
        money_Per_Year =money_Per_Year-300000
        tex=(money_Per_Year*0.1)+7500
    elif money_Per_Year>150000:
        money_Per_Year =money_Per_Year-150000
        tex= money_Per_Year*0.05
    return tex
