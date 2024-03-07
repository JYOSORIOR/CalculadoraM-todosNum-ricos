import numpy as np

def suma(matriz1, matriz2):
    resultado = np.add(matriz1, matriz2)
    print(f"\nSUMA: \n{resultado} ")
    return resultado


def resta(matriz1, matriz2):
    resultado = np.subtract(matriz1, matriz2)
    print(f"\nRESTA: \n{resultado} ")
    return resultado


def productoPunto(matriz1, matriz2):
    resultado = np.dot(matriz1, matriz2)
    print(f"\nPRODUCTO PUNTO: \n{resultado} ")
    return resultado


def determinante(matriz1):
    resultado = np.linalg.det(matriz1)
    print(f"\nDETERMINANTE: \n{resultado} ")
    return resultado


def inversa(matriz1):
    resultado = np.linalg.inv(matriz1)
    print(f"\nINVERSA: \n{resultado} ")
    return resultado


def transpuesta(matriz1):
    resultado = np.transpose(matriz1)
    print(f"\nTRANSPUESTA: \n{resultado} ")
    return resultado