import pyautogui as pg
from tkinter import *
import clipboard
import time
import pandas as pd
import pyodbc
import os.path

#matricula = [42234,95850,150473]
bola_verde = pg.locateOnScreen('./bola_verde.png')


#relação dos  funcionarios.
matricula =[103543,97500]


for x in matricula:
    time.sleep(1)
    prog1 = pg.locateOnScreen('./lupa.png')
    prog2 = pg.locateOnScreen('./lupa2.png')
    if( prog1 is None):
        click = prog2
    else:
        click = prog1
    pg.click( (click.left)-15, (click.top)+5 )
    pg.write( str(x) )
    pg.click(click)
    pg.click(interval = 0.2)
    flag = False
    cont = 0
    
    while (True):
        filial=pg.locateOnScreen('./filial.png')
        print(filial)
        if (filial is not None):
            print('entrou')
            flag = False
            break
        else:
            print('Não Encontrado')
            flag=True
            break
    if(flag):
        continue
    
    pg.click(bola_verde)
    pg.press('f')
    while(True):
        ausencia= pg.locateOnScreen('./ausencia.png')
        if (ausencia is not None):
            break
    pg.click(ausencia)

    while(True):
        manutencao= pg.locateOnScreen('./manutencao.png')
        if (manutencao is not None):
            break
    pg.click(manutencao)
    
    
