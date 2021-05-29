""" Modulo Ciclos
    Funciones para practicas con ciclos
    Daniel Valencia Cordero
    Mayo 10-2021 """
# Definición de Funciones
import numpy as np

def simulador_caida_libre(altura):
  #Se ha de suponer que un segundo de tiempo es equivalente a un aumento de 0.1 en t
  t = 0.0
  g = 9.8
  while(altura > 0):
    print(str(t)+"segundos  "+str(altura)+" metros de altura.")
    t = round(t + 0.1, 1)
    d = 0.5*g*(t**2)
    altura = round(altura - d, 3)
  print(str(t)+"segundos  "+str(altura)+" metros de altura.")

def generador_generaciones(generacion):
  tem = 0
  personas = []
  if(generacion >=0 ):
    personas.append(1)
    print("Generacion = "+str(tem)+"   familiares = "+str(personas[0]))

  while(tem < generacion ):
    personas.append(personas[tem]*2)
    tem = tem + 1
    print("Generacion = "+str(tem)+"   familiares = "+str(personas[len(personas)-1]) )

  return sum(personas)

def constructor_triangulos(pisos):
  num = 1  
  for i in range(1,pisos+1):
    nivel = i
    while(nivel > 0):
      print(str(num)+" ", end="")
      num = num + 1
      nivel = nivel - 1
    print("")  
    
def constructor_tableros(longitud):
  fil = int(longitud)*3
  col = int(longitud)*3
  tablero = np.full((fil,col)," ")
  for i in range(0,fil,3):
    if( i%2 == 0 ):
      for j in range(3,col,6):
        tablero[i][j]   = "*"
        tablero[i][j+1] = "*"
        tablero[i][j+2] = "*"

        tablero[i+1][j]   = "*"
        tablero[i+1][j+1] = "*"
        tablero[i+1][j+2] = "*"

        tablero[i+2][j]   = "*"
        tablero[i+2][j+1] = "*"
        tablero[i+2][j+2] = "*"
    elif( i%2 == 1 ):
      for j in range(0,col,6):
        tablero[i][j]   = "*"
        tablero[i][j+1] = "*"
        tablero[i][j+2] = "*"

        tablero[i+1][j]   = "*"
        tablero[i+1][j+1] = "*"
        tablero[i+1][j+2] = "*"

        tablero[i+2][j]   = "*"
        tablero[i+2][j+1] = "*"
        tablero[i+2][j+2] = "*"
  mostrarMatriz(tablero, fil, col)

def mostrarMatriz(tablero, fil, col):
  for i in range(fil):
    for j in range(col):
      valor = tablero[i][j]
      print(valor+" ",end="")
    print()