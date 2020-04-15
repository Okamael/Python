import pyautogui as pg
from tkinter import *
import clipboard
import time
import pandas as pd
import pyodbc
import os.path

def checkFuncionario():
    ''' Função para  validar se   vai calcular o funcionario'''
    ''' procurando e validando filial e  se  a pessoa esta com a bolinha verde'''
    while(True):
        bola_verde = pg.locateCenterOnScreen('./RH/bola_verde.png')
        filial = pg.locateOnScreen('./RH/filial_mg.png')
        print(bola_verde, filial)
        if((bola_verde is not None) and (filial is not None)):
            print('entrou')
            flag=False
            break  
        else:
            print('True')
            flag=True
            break
    if(flag):
        return True
    else:
        return False

def fechaFerias():
    '''Fecha ferias por que deu algum erro com as datas digitadas'''
    pg.press('enter')
    time.sleep(0.9)
    pg.press('enter')
    time.sleep(0.9)
    pg.click(pg.locateOnScreen('./RH/fechar.png'))
    while(True):
        botao = pg.locateOnScreen('./RH/sair_pagina.png')
        if(botao is not None):
            break  
    pg.press('enter')

def preencherFerias():
    pg.press('enter',presses=4, interval=0.2)
    pg.write('02042020')

def preencherFerias2():
    pg.press('enter',presses=2, interval=0.2)
    pg.write('01042020')
    pg.press('enter',presses=3, interval=0.2)
    pg.write('N')
    pg.press('enter')
    pg.press('f6')
    


matriculas = [173,175,153,138,100,130,180,188,169,157,154,129,183,177,161,144,136
,143,115,109,54 ,189,137,184,165,176,146,145,185,150,164,48 ,147,156
,174,178,30 ,149]



for x in matriculas:
    time.sleep(1)
    prog1 = pg.locateOnScreen('./RH/lupa.png')
    prog2 = pg.locateOnScreen('./RH/lupa2.png')
    if(prog1 is None):
        click = prog2
    else:
        click = prog1
    pg.click((click.left)-15,(click.top) +5)
    pg.write(str(x))
    time.sleep(1)
    pg.click(click)
    pg.click(interval=0.2)
    flag = False
    cont = 0
    while(True):
        bola_verde = pg.locateCenterOnScreen('./RH/bola_verde.png')
        filial = pg.locateOnScreen('./RH/filial_lj.png')
        print(bola_verde, filial)
        if((bola_verde is not None) and (filial is not None)):
            print('entrou')
            flag=False
            break  
        if(cont==0):
            print('count0')
            time.sleep(0.3)
        else:
            print('True')
            flag=True
            break
        cont+=1
    if(flag):
        continue
    
    '''Encontra a bolinah verde  e inicia o calculo'''
    pg.click(bola_verde)
    time.sleep(0.5)
    pg.press('c')
    time.sleep(7.0)
    if(pg.locateOnScreen('./RH/confirmar_ferias.png')):
        pg.press('enter')
            
                
            
    '''verifica se esta na tela de ferias'''
    while(True):
        botao= pg.locateOnScreen('./RH/calculo.png')
        if(botao is not None):
            break
    '''Inicia digitação das ferias'''
    pg.press('enter')
    time.sleep(0.5)
    pg.write('20,0')
    time.sleep(0.5)
    if(pg.locateOnScreen('./RH/redigita.png')):
        fechaFerias()
        continue
    time.sleep(0.2)
    '''valida se a pessoa vai ter desconto com dia negativo no adiamanto'''
    if(pg.locateOnScreen('./RH/aviso_afastado.png')):
        pg.press('enter')
        preencherFerias()
        time.sleep(0.5)
        if(pg.locateOnScreen('./RH/aviso_afastado.png')):
            pg.press('enter')
            fechaFerias()
        else:
            preencherFerias2()
            while(True):
                botao = pg.locateOnScreen('./RH/antes_confirma.png')
                if(botao is not None):
                    break
            pg.click(pg.locateOnScreen('./RH/confirmar.png'))
            time.sleep(3)
            pg.press('enter')
            time.sleep(4)
            pg.press('enter')

        
    else:
        preencherFerias()
        time.sleep(0.5)
        if(pg.locateOnScreen('./RH/aviso_afastado.png')):
            pg.press('enter')
            fechaFerias()
        else:
            preencherFerias2()
            while(True):
                botao = pg.locateOnScreen('./RH/antes_confirma.png')
                if(botao is not None):
                    break    
            pg.click(pg.locateOnScreen('./RH/confirmar.png'))
            time.sleep(3.0)
            pg.press('enter')
            time.sleep(4.0)
            pg.press('enter')