import csv
from math import inf
from re import sub
from json import loads

def pregunta_01():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    suma = 0
    for fila in lista:
        suma += int(fila[1])
    return suma

def pregunta_02():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    valores_iniciales = ['A', 'B', 'C', 'D', 'E']
    maximos = []
    for valor in valores_iniciales:
        contador = 0
        for fila in lista:
            if fila[0] == valor:
                contador += 1
        maximos.append((valor, contador))
    return maximos

def pregunta_03():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    valores_iniciales = ['A', 'B', 'C', 'D', 'E']
    maximos = []
    for valor in valores_iniciales:
        filas = []
        for fila in lista:
            if fila[0] == valor:
                filas.append(fila)
        suma = 0
        for fila in filas:
            suma += int(fila[1])
        maximos.append((valor, suma))
    return maximos

def pregunta_04():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    conteo_meses = [0] * 12
    for fila in lista:
        mes = int(fila[2][5:7])
        conteo_meses[mes - 1] += 1
    return [(meses[i], conteo_meses[i]) for i in range(12)]

def pregunta_05():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"A": [0, inf], "B": [0, inf], "C": [0, inf], "D": [0, inf], "E": [0, inf]}
    for fila in lista:
        if maximos.get(fila[0])[0] < int(fila[1]):
            maximos[fila[0]][0] = int(fila[1])
        if maximos.get(fila[0])[1] > int(fila[1]):
            maximos[fila[0]][1] = int(fila[1])
    return [(clave, maximos[clave][0], maximos[clave][1]) for clave in maximos.keys()]

def pregunta_06():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"aaa": [0, float('inf')], "bbb": [0, float('inf')], "ccc": [0, float('inf')], "ddd": [0, float('inf')], "eee": [0, float('inf')], "fff": [0, float('inf')], "ggg": [0, float('inf')], "hhh": [0, float('inf')], "iii": [0, float('inf')], "jjj": [0, float('inf')]}
    datos = []
    for fila in lista:
        datos.append(loads(formateo('{' + fila[4] + '}')))
    for d in datos:
        for clave in d.keys():
            valor = int(d[clave])
            if maximos.get(clave)[0] < valor:
                maximos[clave][0] = valor
            if maximos.get(clave)[1] > valor:
                maximos[clave][1] = valor
    return [(clave, maximos[clave][1], maximos[clave][0]) for clave in maximos.keys()]

def pregunta_07():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    li = [[] for i in range(10)]
    for fila in lista:
        li[int(fila[1][0])].append(fila[0])
    return [(i, li[i]) for i in range(10)]

def pregunta_08():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    li = [[] for i in range(10)]
    for fila in lista:
        li[int(fila[1])].append(fila[0])
    return [(i, sorted(list(set(li[i])))) for i in range(10)]

def pregunta_09():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"aaa": 0, "bbb": 0, "ccc": 0, "ddd": 0, "eee": 0, "fff": 0, "ggg": 0, "hhh": 0, "iii": 0, "jjj": 0}
    datos = []
    for fila in lista:
        datos.append(loads(formateo('{' + fila[4] + '}')))
    for d in datos:
        for clave in d.keys():
            maximos[clave] += 1
    return maximos
import csv
from math import inf
from re import sub
from json import loads

def formateo(cadena):
    resultado = ""
    entrecomillado = False
    for caracter in cadena:
        if caracter.isalnum():
            if not entrecomillado:
                resultado += '"'
                entrecomillado = True
        elif entrecomillado:
            resultado += '"'
            entrecomillado = False
        resultado += caracter
    return resultado

def pregunta_01():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    suma = 0
    for fila in lista:
        suma += int(fila[1])
    return suma

def pregunta_02():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    valores_iniciales = ['A', 'B', 'C', 'D', 'E']
    maximos = []
    for valor in valores_iniciales:
        contador = 0
        for fila in lista:
            if fila[0] == valor:
                contador += 1
        maximos.append((valor, contador))
    return maximos

def pregunta_03():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    valores_iniciales = ['A', 'B', 'C', 'D', 'E']
    maximos = []
    for valor in valores_iniciales:
        filas = []
        for fila in lista:
            if fila[0] == valor:
                filas.append(fila)
        suma = 0
        for fila in filas:
            suma += int(fila[1])
        maximos.append((valor, suma))
    return maximos

def pregunta_04():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    conteo_meses = [0] * 12
    for fila in lista:
        mes = int(fila[2][5:7])
        conteo_meses[mes - 1] += 1
    return [(meses[i], conteo_meses[i]) for i in range(12)]

def pregunta_05():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"A": [0, inf], "B": [0, inf], "C": [0, inf], "D": [0, inf], "E": [0, inf]}
    for fila in lista:
        if maximos.get(fila[0])[0] < int(fila[1]):
            maximos[fila[0]][0] = int(fila[1])
        if maximos.get(fila[0])[1] > int(fila[1]):
            maximos[fila[0]][1] = int(fila[1])
    return [(clave, maximos[clave][0], maximos[clave][1]) for clave in maximos.keys()]

def pregunta_06():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"aaa": [0, float('inf')], "bbb": [0, float('inf')], "ccc": [0, float('inf')], "ddd": [0, float('inf')], "eee": [0, float('inf')], "fff": [0, float('inf')], "ggg": [0, float('inf')], "hhh": [0, float('inf')], "iii": [0, float('inf')], "jjj": [0, float('inf')]}
    datos = []
    for fila in lista:
        datos.append(loads(formateo('{' + fila[4] + '}')))
    for d in datos:
        for clave in d.keys():
            valor = int(d[clave])
            if maximos.get(clave)[0] < valor:
                maximos[clave][0] = valor
            if maximos.get(clave)[1] > valor:
                maximos[clave][1] = valor
    return [(clave, maximos[clave][1], maximos[clave][0]) for clave in maximos.keys()]

def pregunta_07():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    li = [[] for i in range(10)]
    for fila in lista:
        li[int(fila[1][0])].append(fila[0])
    return [(i, li[i]) for i in range(10)]

def pregunta_08():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    li = [[] for i in range(10)]
    for fila in lista:
        li[int(fila[1])].append(fila[0])
    return [(i, sorted(list(set(li[i])))) for i in range(10)]

def pregunta_09():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    maximos = {"aaa": 0, "bbb": 0, "ccc": 0, "ddd": 0, "eee": 0, "fff": 0, "ggg": 0, "hhh": 0, "iii": 0, "jjj": 0}
    datos = []
    for fila in lista:
        datos.append(loads(formateo('{' + fila[4] + '}')))
    for d in datos:
        for clave in d.keys():
            maximos[clave] += 1
    return maximos

def pregunta_10():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    return [(fila[0], len(sub(',', '', fila[3])), len(loads(formateo('{' + fila[4] + '}')))) for fila in lista]

def pregunta_11():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    conteo = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for fila in lista:
        for letra in list(sub(',', '', fila[3])):
            conteo[letra] += int(fila[1])
    return conteo

def formateo(cadena):
    resultado = ""
    entrecomillado = False
    for caracter in cadena:
        if caracter.isalnum():
            if not entrecomillado:
                resultado += '"'
                entrecomillado = True
        elif entrecomillado:
            resultado += '"'
            entrecomillado = False
        resultado += caracter
    return resultado

def pregunta_12():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    resultado = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for fila in lista:
        resultado[fila[0]] += sum(map(int, loads(formateo('{' + fila[4] + '}')).values()))
    return resultado

def pregunta_10():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    return [(fila[0], len(sub(',', '', fila[3])), len(loads(formateo('{' + fila[4] + '}')))) for fila in lista]

def pregunta_11():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    conteo = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for fila in lista:
        for letra in list(sub(',', '', fila[3])):
            conteo[letra] += int(fila[1])
    return conteo

def pregunta_12():
    with open('data.csv', 'r') as tabla:
        archivo = csv.reader(tabla, delimiter='\t')
        lista = list(archivo)
    resultado = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for fila in lista:
        resultado[fila[0]] += sum(map(int, loads(formateo('{' + fila[4] + '}')).values()))
    return resultado

