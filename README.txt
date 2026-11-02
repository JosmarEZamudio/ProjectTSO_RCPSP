El generador de instancias funciona de la siguente manera: 

1-Ingresar cantidad de actividades.
2-Ingresar ingresar cantidad de recursos a utilizar.

3-Ingresar tiempo minimo y maximo para completar las actividades.
4-Ingresar capcidad(cuanto hay de cada recurso) minima y maxima de los recursos.

-Se generaran los tiempos automaticamente (random).
-Se generaran las cantidades maximas de cada recurso automaticamente (random).
-Se generaran las precedencias automaticamente (random).
-Se generaran las asinaciones de recursos a las actividades automaticamente (random).

4 archivos de salida:
*1- actividades.csv (Relacion entre la actividad y el tiempo que lleva para completarla).
*2- recursos.csv (Relacion entre el recurso y la cantidad maxima que hay de ese recurso).
*3- precedencias.csv (Dicta que actividades deben ser completadas para que otra inicie).
*4- actividadRecurso.csv (Matriz que dicta cuanto de un recurso necesita una actividad).


*Nota: relacionar cada actividad con su respectivo indice al igual que el recurso
Ejemplo: Actividades[1,2]  Tiempo[3,10], la actividad 1 dura 3, la actividad 2 dura 10.
Ejemplo: Recursos[1,2] Cantidad[3,6], del recurso 1 hay 3, del recurso 2 hay 6.
