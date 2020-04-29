import pyautogui as pg
from tkinter import *
import clipboard
import time
import pandas as pd
import pyodbc
import os.path

#matricula = []
bola_verde = pg.locateOnScreen('./bola_verde.png')


#relação dos  funcionarios.
matricula =[103543,42234,95850,105473]
contador= len(matricula)
repeticao= 0
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
        if (filial is not None):
            flag = False
            break
        else:
            print('Não Encontrado')
            flag=True
            break
    if(flag):
        continue
    
    ##pg.click(bola_verde)
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
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('enter')

    #checa  se esta dentro do cadastro de ausencia
    while(True):
        telaAfastamento = pg.locateOnScreen('./cadastrodeausencia.png')
        if(telaAfastamento is not None):
            break
    #checa se incluiu uma linha para a  digitação do afastamento.
    while(True):
        dataBranco=pg.locateOnScreen('./dataAvisoBranco.png')
        dataCinza= pg.locateOnScreen('./dataAvisoCinza.png')
        if( (dataBranco is not None) or (dataCinza is not None)):
            break
        else:
            pg.press('down')
    #inicia uma linha para a digitação do lançamento.
    pg.press('right')
    pg.write('019')
    pg.press('right')
    pg.press('right')
    pg.write('27042020')
    pg.write('30')
    pg.press('enter')
    while(True):
        validaterminoBranco = pg.locateOnScreen('./validaterminoBranco.png')
        validaterminoCinza = pg.locateOnScreen('./validaterminoCinza.png')
        if( (validaterminoBranco is not None) or (validaterminoCinza is not None)):
            break
    #confirmação do afastamento.
    pg.click(pg.locateOnScreen('./bt_Confirma.png'))
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.press('enter')
    repeticao += 1
    print('execução matricula:{} concluida'.format(x) )
    print('resta apenas:{} matriculas'.format(contador-repeticao) )
print('Execução Concluida')




    
