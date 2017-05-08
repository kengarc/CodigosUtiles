'''
Created on 27 abr. 2017

@author: Jaime Garcia
'''

import re

def compruebaErrores(email):
    #Array de elementos no permitidos en un email y que ira recorriendo y comparando
    elementosNoPermitidos = [" ", "!", "%", "&", "(", ")", "=", "*", "+"]
    
    #Recorre el listado de elementos no permitidos, en caso de que alguno se encuentre en el email, devolverá un mensaje
    #indicándolo
    for item in elementosNoPermitidos:
        if (item in email):
            return "Un email no puede contener el caracter "+item
    

   
def compruebaEmail (email):
    
    """
    Esta funcion devuelve True en caso de que el email que se le pase tenga la estructura correcta
    (algo de texto o numeros, una arroba, al menos una letra, un punto y al menos otra letra) y un 
    mensaje con el error de validacion en caso de que ocurra algo
    """
    
    patron = re.compile("[A-Za-z0-9.-_]+@[A-Za-z0-9]+.[A-Za-z-.0-9]+")
    if (patron.match(email)):
        return True
    else:
        return compruebaErrores(email)
    