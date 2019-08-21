from datetime import date
from datetime import datetime
data_atual = datetime.now()
horaAtual = data_atual.strftime('%H:%M')

ArrayExchangeList= ["Londres","Nova York","Sydney","Tóquio"]
ArrayExchangeOpenTime = ["04:00","09:00","18:00","21:00"]
ArrayExchangeCloseTime = ["13:00","18:00","03:00","06:00"]
ArrayExchangeOpenNow=[]
ArrayExchegeNameOpen=[]
ArrayExchengeNameClose=[]

for i in range (4):
    if horaAtual >= ArrayExchangeOpenTime[i]:
        ArrayExchangeOpenNow.append(ArrayExchangeOpenTime[i])
    else:ArrayExchengeNameClose.append(ArrayExchangeOpenTime[i])

for i in range(len(ArrayExchangeOpenNow) ):
    print("A Bolsa %s esta aberta ate :"%ArrayExchangeList[i],ArrayExchangeCloseTime[i])
print("-----------------------------------------------")
for i in range(len(ArrayExchengeNameClose)):
    print("A Bolsa %s esta fechada, abre as "%ArrayExchangeList[i],ArrayExchengeNameClose)
    






