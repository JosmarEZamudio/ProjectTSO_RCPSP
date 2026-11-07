
def localSearch(matrizRespuesta, actividades, recursos, precedencias, matrizDrj):

    # 1. Evaluar todas las combinaciones iniciales
    mejorSolucion = None
    mejorMakespan = float('inf')

    for solucion in matrizRespuesta:

        programadas = []
        inicio = {}
        fin = {}

        horizonte = sum(actividades.values())

        usoRecursos = [
            [0 for t in range(horizonte)]
            for r in recursos
        ]

        while len(programadas) < len(actividades):

            actividad = None

            # Seleccionar según la prioridad de la solución
            for j in solucion:

                if j in programadas:
                    continue

                if all(p in programadas for p in precedencias[j]):
                    actividad = j
                    break

            if actividad is None:
                raise ValueError("No existen actividades elegibles.")

            tiempoMinimo = 0

            if precedencias[actividad]:
                tiempoMinimo = max(fin[p] for p in precedencias[actividad])

            duracion = actividades[actividad]

            for t in range(tiempoMinimo, horizonte - duracion + 1):

                factible = True

                for r in recursos:
                    demanda = matrizDrj[r - 1][actividad - 1]

                    for instante in range(t, t + duracion):
                        if usoRecursos[r - 1][instante] + demanda > recursos[r]:
                            factible = False
                            break

                    if not factible:
                        break

                if factible:
                    break

            else:
                raise ValueError("No se encontró un inicio factible.")

            inicio[actividad] = t
            fin[actividad] = t + duracion

            for r in recursos:
                demanda = matrizDrj[r - 1][actividad - 1]

                for instante in range(t, t + duracion):
                    usoRecursos[r - 1][instante] += demanda

            programadas.append(actividad)

        makespan = max(fin.values())

        if makespan < mejorMakespan:
            mejorMakespan = makespan
            mejorSolucion = solucion.copy()

    # 2. Comenzar Local Search
    while True:

        matriz = []

        # Generar vecinos mediante Insertion Move
        for i in range(len(mejorSolucion)):
            for j in range(len(mejorSolucion)):

                if i != j:

                    respuestaCopia = mejorSolucion.copy()

                    elemento = respuestaCopia.pop(i)
                    respuestaCopia.insert(j, elemento)

                    if respuestaCopia not in matriz:
                        matriz.append(respuestaCopia)

        mejorVecino = None
        mejorMakespanVecino = mejorMakespan

        # 3. Evaluar cada vecino
        for solucion in matriz:

            programadas = []
            inicio = {}
            fin = {}

            horizonte = sum(actividades.values())

            usoRecursos = [
                [0 for t in range(horizonte)]
                for r in recursos
            ]

            while len(programadas) < len(actividades):

                actividad = None

                for j in solucion:

                    if j in programadas:
                        continue

                    if all(p in programadas for p in precedencias[j]):
                        actividad = j
                        break

                if actividad is None:
                    raise ValueError("No existen actividades elegibles.")

                tiempoMinimo = 0

                if precedencias[actividad]:
                    tiempoMinimo = max(fin[p] for p in precedencias[actividad])

                duracion = actividades[actividad]

                for t in range(tiempoMinimo, horizonte - duracion + 1):

                    factible = True

                    for r in recursos:
                        demanda = matrizDrj[r - 1][actividad - 1]

                        for instante in range(t, t + duracion):
                            if usoRecursos[r - 1][instante] + demanda > recursos[r]:
                                factible = False
                                break

                        if not factible:
                            break

                    if factible:
                        break

                else:
                    raise ValueError("No se encontró un inicio factible.")

                inicio[actividad] = t
                fin[actividad] = t + duracion

                for r in recursos:
                    demanda = matrizDrj[r - 1][actividad - 1]

                    for instante in range(t, t + duracion):
                        usoRecursos[r - 1][instante] += demanda

                programadas.append(actividad)

            makespan = max(fin.values())

            if makespan < mejorMakespanVecino:
                mejorMakespanVecino = makespan
                mejorVecino = solucion.copy()

        # 4. Comprobar mejora
        if mejorVecino is None:
            break

        mejorSolucion = mejorVecino.copy()
        mejorMakespan = mejorMakespanVecino

        print("Nueva solución:", mejorSolucion)
        print("Makespan:", mejorMakespan)

    return mejorSolucion, mejorMakespan
