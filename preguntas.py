"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    with open('/Datos.txt', 'r') as archivo:
         datos = archivo.read()
    filas = datos.split('\n') 
    fila0 = filas[0]
    columna0 = fila0.split() 
    D1 = int(columna0[1]) 
    fila1 = filas[1]
    columna1 = fila1.split() 
    D2 = int(columna1[1]) 
    fila2 = filas[2]
    columna2 = fila2.split() 
    D3 = int(columna2[1]) 
    fila3 = filas[3]
    columna3 = fila3.split() 
    D4 = int(columna3[1])
    fila4 = filas[4]
    columna4 = fila4.split() 
    D5 = int(columna4[1])
    fila5 = filas[5]
    columna5 = fila5.split() 
    D6 = int(columna5[1])
    fila6 = filas[6]
    columna6 = fila6.split() 
    D7 = int(columna6[1])
    fila7 = filas[7]
    columna7 = fila7.split() 
    D8 = int(columna7[1])
    fila8 = filas[8]
    columna8 = fila8.split() 
    D9 = int(columna8[1])
    fila9 = filas[9]
    columna9 = fila9.split() 
    D10 = int(columna9[1])
    fila10 = filas[10]
    columna10 = fila10.split() 
    D11 = int(columna10[1])
    fila11 = filas[11]
    columna11 = fila11.split() 
    D12 = int(columna11[1])
    fila12 = filas[12]
    columna12 = fila12.split() 
    D13 = int(columna12[1])
    fila13 = filas[13]
    columna13 = fila13.split() 
    D14 = int(columna13[1])
    fila14 = filas[14]
    columna14 = fila14.split() 
    D15 = int(columna14[1])
    fila15 = filas[15]
    columna15 = fila15.split() 
    D16 = int(columna15[1])
    fila16 = filas[16]
    columna16 = fila16.split() 
    D17 = int(columna16[1])
    fila17 = filas[17]
    columna17 = fila17.split() 
    D18 = int(columna17[1])
    fila18 = filas[18]
    columna18 = fila18.split() 
    D19 = int(columna18[1])
    fila19 = filas[19]
    columna19 = fila19.split() 
    D20 = int(columna19[1])
    fila20 = filas[20]
    columna20 = fila20.split() 
    D21 = int(columna20[1])
    fila21 = filas[21]
    columna21 = fila21.split() 
    D22 = int(columna21[1])
    fila22 = filas[22]
    columna22 = fila22.split() 
    D23 = int(columna22[1])
    fila23 = filas[23]
    columna23 = fila23.split() 
    D24 = int(columna23[1])
    fila24 = filas[24]
    columna24 = fila24.split() 
    D25 = int(columna24[1])
    fila25 = filas[25]
    columna25 = fila25.split() 
    D26 = int(columna25[1])
    fila26 = filas[26]
    columna26 = fila26.split() 
    D27 = int(columna26[1])
    fila27 = filas[27]
    columna27 = fila27.split() 
    D28 = int(columna27[1])
    fila28 = filas[28]
    columna28 = fila28.split() 
    D29 = int(columna28[1])
    fila29 = filas[29]
    columna29 = fila29.split() 
    D30 = int(columna29[1])
    fila30 = filas[30]
    columna30 = fila30.split() 
    D31 = int(columna30[1])
    fila31 = filas[31]
    columna31 = fila31.split() 
    D32 = int(columna31[1])
    fila32 = filas[32]
    columna32 = fila32.split() 
    D33 = int(columna32[1])
    fila33 = filas[33]
    columna33 = fila33.split() 
    D34 = int(columna33[1])
    fila34 = filas[34]
    columna34 = fila34.split() 
    D35 = int(columna34[1])
    fila35 = filas[35]
    columna35 = fila35.split() 
    D36 = int(columna35[1])
    fila36 = filas[36]
    columna36 = fila36.split() 
    D37 = int(columna36[1])
    fila37 = filas[37]
    columna37 = fila37.split() 
    D38 = int(columna37[1])
    fila38 = filas[38]
    columna38 = fila38.split() 
    D39 = int(columna38[1])
    fila39 = filas[39]
    columna39 = fila39.split() 
    D40 = int(columna39[1])

    print(D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16+D17+D18+D19+D20+D21+D22+D23+D24+D25+D26+D27+D28+D29+D30+D31+D32+D33+D34+D35+D36+D37+D38+D39+D40)        
     return


def pregunta_02():
    with open('/Datos.txt', 'r') as archivo:
         datos = archivo.read()
    filas = datos.split('\n') 
    fila0 = filas[0]
    columna0 = fila0.split() 
    D1 = (columna0[0]) 
    fila1 = filas[1]
    columna1 = fila1.split() 
    D2 = (columna1[0]) 
    fila2 = filas[2]
    columna2 = fila2.split() 
    D3 = (columna2[0]) 
    fila3 = filas[3]
    columna3 = fila3.split() 
    D4 = (columna3[0])
    fila4 = filas[4]
    columna4 = fila4.split() 
    D5 = (columna4[0])
    fila5 = filas[5]
    columna5 = fila5.split() 
    D6 = (columna5[0])
    fila6 = filas[6]
    columna6 = fila6.split() 
    D7 = (columna6[0])
    fila7 = filas[7]
    columna7 = fila7.split() 
    D8 = (columna7[0])
    fila8 = filas[8]
    columna8 = fila8.split() 
    D9 = (columna8[0])
    fila9 = filas[9]
    columna9 = fila9.split() 
    D10 = (columna9[0])
    fila10 = filas[10]
    columna10 = fila10.split() 
    D11 = (columna10[0])
    fila11 = filas[11]
    columna11 = fila11.split() 
    D12 = (columna11[0])
    fila12 = filas[12]
    columna12 = fila12.split() 
    D13 = (columna12[0])
    fila13 = filas[13]
    columna13 = fila13.split() 
    D14 = (columna13[0])
    fila14 = filas[14]
    columna14 = fila14.split() 
    D15 = (columna14[0])
    fila15 = filas[15]
    columna15 = fila15.split() 
    D16 = (columna15[0])
    fila16 = filas[16]
    columna16 = fila16.split() 
    D17 = (columna16[0])
    fila17 = filas[17]
    columna17 = fila17.split() 
    D18 = (columna17[0])
    fila18 = filas[18]
    columna18 = fila18.split() 
    D19 = (columna18[0])
    fila19 = filas[19]
    columna19 = fila19.split() 
    D20 = (columna19[0])
    fila20 = filas[20]
    columna20 = fila20.split() 
    D21 = (columna20[0])
    fila21 = filas[21]
    columna21 = fila21.split() 
    D22 = (columna21[0])
    fila22 = filas[22]
    columna22 = fila22.split() 
    D23 = (columna22[0])
    fila23 = filas[23]
    columna23 = fila23.split() 
    D24 = (columna23[0])
    fila24 = filas[24]
    columna24 = fila24.split() 
    D25 = (columna24[0])
    fila25 = filas[25]
    columna25 = fila25.split() 
    D26 = (columna25[0])
    fila26 = filas[26]
    columna26 = fila26.split() 
    D27 = (columna26[0])
    fila27 = filas[27]
    columna27 = fila27.split() 
    D28 = (columna27[0])
    fila28 = filas[28]
    columna28 = fila28.split() 
    D29 = (columna28[0])
    fila29 = filas[29]
    columna29 = fila29.split() 
    D30 = (columna29[0])
    fila30 = filas[30]
    columna30 = fila30.split() 
    D31 = (columna30[0])
    fila31 = filas[31]
    columna31 = fila31.split() 
    D32 = (columna31[0])
    fila32 = filas[32]
    columna32 = fila32.split() 
    D33 = (columna32[0])
    fila33 = filas[33]
    columna33 = fila33.split() 
    D34 = (columna33[0])
    fila34 = filas[34]
    columna34 = fila34.split() 
    D35 = (columna34[0])
    fila35 = filas[35]
    columna35 = fila35.split() 
    D36 = (columna35[0])
    fila36 = filas[36]
    columna36 = fila36.split() 
    D37 = (columna36[0])
    fila37 = filas[37]
    columna37 = fila37.split() 
    D38 = (columna37[0])
    fila38 = filas[38]
    columna38 = fila38.split() 
    D39 = (columna38[0])
    fila39 = filas[39]
    columna39 = fila39.split() 
    D40 = (columna39[0])

    X = [D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40]
    contadorA = 0
    contadorB = 0
    contadorC = 0
    contadorD = 0
    contadorE = 0
    for i in X:
      if i == "A":
        contadorA = contadorA + 1
      elif i == "B":
        contadorB = contadorB + 1
      elif i == "C":
        contadorC = contadorC + 1
      elif i == "D":
        contadorD = contadorD + 1  
      else:
        contadorE = contadorE + 1

    print(("A", contadorA) )
    print(("B", contadorB) )
    print(("C", contadorC) )
    print(("D", contadorD) )
    print(("E", contadorE) )
    return


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
