def serialSGS(precedencias, actividades, recursos, matrizDrj):

    # Validar requerimientos de recursos
    for r in recursos:
        for actividad in actividades:

            demanda = matrizDrj[r - 1][actividad - 1]

            if demanda > recursos[r]:
                raise ValueError(
                    f"La actividad {actividad} requiere {demanda} "
                    f"unidades del recurso {r}, pero solo existen "
                    f"{recursos[r]} disponibles."
                )
            
    #Variables para guardar la actividades que ya fueron incorporadas al calendario
    programadas = []
    #Diccionario para guardar los tiempos asignados
    inicio = {}
    fin = {}
    #Sumar todas las duraciones de las actividades
    horizonte = sum(actividades.values())
#Matriz para saber cuantos recursos estamos utilizando en cada instante
    usoRecursos = [
        [0 for t in range(horizonte)]
        for r in recursos
    ]
#Este ciclo compara cuantas actividades hemos programado contra cuantas existe en total
    while len(programadas) < len(actividades):

        #1-Identificar actividades disponibles
        disponibles = []
        #Recorrer todas las actividades
        for actividad in actividades:
        #Si ya existe en la programacion, continuar
            if actividad in programadas:
                continue
        #Comprobar que todas las predecesoras de la actividad ya esten programadas
            if all(p in programadas for p in precedencias[actividad]):
                disponibles.append(actividad) #Agregar a disponibles si sus precedencias ya estan
                #completas

        #2-Seleccionar actividad con menor duración (SPT)
        actividad = min(disponibles, key=lambda j: actividades[j])
        #****************NOTA, esta parte puede ser cambiada por cualquier otra consideracion
        #para la seleccion de actividad

#NOTA********* Este proceso es para cuando ya se elegio una actividad a ejecutar

        #3-Determinar el tiempo mínimo de inicio
        tiempoMinimo = 0
        #Encuentra el maximo tiempo registrado, ya que ese tiempo sera el comienzo para la
        #nueva actividad
        if precedencias[actividad]:
            tiempoMinimo = max(fin[p] for p in precedencias[actividad])
    #Simplemente se obtiene la duracion de la actividad que se selecciono
        duracion = actividades[actividad]

        #4-Buscar disponibilidad de recursos
        #Probar varios instantes para iniciar la activdad
        for t in range(tiempoMinimo, horizonte - duracion + 1):
            #Si es factible devuelve tru
            factible = True
            #Recorrer recursos (la cantidad total recursos.csv)
            for r in recursos:
                #La actividad seleccionada, se le comprueba cuantos recursos utiliza
                demanda = matrizDrj[r - 1][actividad - 1]
            #Comprueba cada instante de la actividad
                for instante in range(t, t + duracion):
                #Condicion para evitar exceder los recursos disponivles
                    if usoRecursos[r - 1][instante] + demanda > recursos[r]:
                        factible = False
                        break #Si no es factible, se interreumpe el ciclo
            #Interrumpir
                if not factible:
                    break
            #Si todos los instantes y recursos cumplieron condiciones, conservar t
            if factible:
                break

        #5-Registrar tiempos
        inicio[actividad] = t
        fin[actividad] = t + duracion

        #6-Actualizar consumo de recursos
        for r in recursos:
        #Encontrar recursos demandados
            demanda = matrizDrj[r - 1][actividad - 1]
        #Guardarlos en la lista
            for instante in range(t, t + duracion):
                usoRecursos[r - 1][instante] += demanda

    #Cuando se encuentre un inicio, final y recursos, agregar la actividad a las programadas
        programadas.append(actividad)

    return inicio, fin