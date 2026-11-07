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