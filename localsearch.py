import csv
import serialSGS

#Esta heuristica sera del tipo insertion move, es decir, cada actividad moverla a otro punto

#1-Cargar resultado obtenido por la heuristica 
with open ("resultados.csv","r",newline="") as archivo:
    lector = csv.reader(archivo)

    respuesta = []

    for i in lector:
        respuesta.append(i)

    respuesta = [int(valor) for valor in respuesta[0]]

#***********************************************
#2-Cargar tiempos de actividad
with open ("actividades.csv","r",newline="") as archivo:
    lectorInicial = csv.reader(archivo)
    numeroActividades = int(next(lectorInicial)[0].split(":")[1].strip())

    lector = csv.DictReader(archivo)

    actividades = {}

    for fila in lector:
        numero = int(fila["Numero_actividad"])
        duracion = int(fila["duracion_actividad"])

        actividades[numero] = duracion

    matriz = [[0 for j in range(numeroActividades)]
        for i in range(1)]
#***********************************************
#2-Cargar cantidad de recursos
with open ("recursos.csv","r",newline="") as archivo:
    lectorInicial = csv.reader(archivo)
    numeroRecursos = int(next(lectorInicial)[0].split(":")[1].strip())

    lector = csv.DictReader(archivo)
   
    recursos = {}
    
    for fila in lector:
        numero = int(fila["Numero_recurso"])
        cantidad = int(fila["cantidad_recurso"])

        recursos[numero] = cantidad
#***********************************************
matrizDrj = [[0 for j in range(numeroActividades)]
        for i in range(numeroRecursos)]

#***********************************************
#3-Cargar matriz drj (actividad recursos)
with open ("actividadRecurso.csv","r",newline="") as archivo:
    lector = csv.reader(archivo)

    for i, fila in enumerate(lector):
        for j, valor in enumerate(fila):
            matrizDrj[i][j] = int(valor)

#***********************************************
#4-Cargar precedencias
with open ("precedencias.csv","r",newline="") as archivo:
    lector = csv.DictReader(archivo)

    precedencias = {}

    for fila in lector:
        actividad = int(fila["Actividad"])
        predecesora = int(fila["Precedencia"])

        if actividad not in precedencias:
            precedencias[actividad] = []

        if predecesora != 0:
            precedencias[actividad].append(predecesora)
#***********************************************
matrizRespuesta = []

print(respuesta)
print("esta es la respuesta")

for i in range(numeroActividades):
    for j in range(numeroActividades):
    
        if i != j:

            respuestaCopia = respuesta.copy()

            elemento = respuestaCopia.pop(i)
            respuestaCopia.insert(j, elemento)

            matrizRespuesta.append(respuestaCopia)

#Ejecutar local search y obtener resultados

mejorSolucion, makespan = serialSGS.localSearch(
    matrizRespuesta,
    actividades,
    recursos,
    precedencias,
    matrizDrj
)

print("\n===== RESULTADO FINAL =====")
print("Mejor solución:", mejorSolucion)
print("Makespan:", makespan)
#print("Inicio:", inicio)
#print("Fin:", fin)




