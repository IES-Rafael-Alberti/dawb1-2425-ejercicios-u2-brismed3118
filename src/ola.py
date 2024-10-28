import time
import os
import shutil
import random

def hacer_ola(ola:str ):
    primer = ola[0]
    ultimo = ola[-1]

    while primer != "C":
        ola = ola[-1] + ola[:-1]
        print (ola)
        time.sleep(0.08)
        primer = ola[-1]            
    
    while ultimo != "C":
        ola = ola[1:] + ola[0]
        print (ola)
        time.sleep(0.08)
        ultimo = ola[0]
    
    return ola

def hacer_nueva(nueva_ola:str ):
    primer = nueva_ola[0]
    ultimo = nueva_ola[-1]

    while primer != "C":
        nueva_ola = nueva_ola[-1] + nueva_ola[:-1]
        print (nueva_ola)
        time.sleep(0.08)
        primer = nueva_ola[0]            
    
    while ultimo != "C":
        nueva_ola = nueva_ola[1:] + nueva_ola[0]
        print (nueva_ola)
        time.sleep(0.08)
        ultimo = nueva_ola[0]
    
    return nueva_ola

def main():
    i = None
    ola = "OOOOOOOOO000000000ooooooooocccccccccooooooooo000000000OOOOOCOOOOO0000000000ooooooooocccccccccooooooooo000000000OOOOOOOOO"
    nueva_ola = ""
    while i == None:    
        nueva_ola = hacer_ola(ola)
        ola = hacer_nueva(nueva_ola)
        
  
if __name__ == "__main__":
    main()