# Trabajo Práctico 1 - Métodos de búsqueda

## Descripción del problema:
El juego consiste en 3 postes y 7 discos apilados de mayor a menor, en el poste de la izquierda. El objetivo es mover todos los discos a la última torre. Hay 2 reglas:

**1 -** Sólo se puede mover un disco por vez

**2 -** No se puede apilar un disco de mayor diámetro sobre uno de menor diámetro

## Configuración:
Para aclarar el método de búsqueda que se desea utilizar, abrir el archivo `hanoi.sh` y aclarar en donde dice `[method]` como primer parámetro, una de las siguientes opciones:
- BPA (Búsqueda primero en ancho)
- BPP (Búsqueda primero en profundidad)
- BPPV (Búsqueda en profundidad variable)
- LOCAL_NO_BACK (Búsqueda heurística local sin retroceso)
- LOCAL_BACK (Búsqueda heurística local con retroceso)
- GLOBAL (Búsqueda heurística global)
- A_STAR (Método A*)

Si escoge un método que utilice heurísticas (estos son `LOCAL_BACK, LOCAL_NO_BACK, GLOBAL y A_STAR`),
tiene la posibilidad de utilizar tres heurísticas. Las mismas se modifican de la misma manera que el método, desde `hanoi.sh`, reemplazando en `[heuristic/depth]` como segundo parámetro.

Existen 3 opciones de heurística, las primeras dos siendo admisibles y la tercera no admisible:
- 1: Función de transición definida por cantidad de discos que faltan ubicar en último poste
- 2: Función de transición definida por discos que aún no están en último poste + discos que están en último poste pero mal ubicados
  (les falta alguno por debajo. Ej: 7 - 5 - 4 tiene dos discos mal ubicados).
- 3:

Si escoge el método `BPPV`, se debe aclarar la profundidad inicial deseada desde `hanoi.sh`, como tercer parámetro, en `[heuristic/depth]`.

## Requerimientos:
Es necesario tener instalado Java en la computadora en la cual se quiere ejecutar el `.jar`

## Ejecución:
Correr el comando `./hanoi.sh` con los argumentos correctos

_Nota: Si se está ejecutando el proyecto desde windows, por favor seguir las siguientes instrucciones:
1) Colocarse sobre el directorio donde está el archivo .jar (A menos que se mueva manualmente, se encuentra en `out/artifacts/TP1__Metodos_de_busqueda_jar`
2) Ejecutar el siguiente comando: `java -jar '.\TP1 - Metodos de busqueda.jar' [método] [heurística/profundidad base]`

#### Ejemplos para ejecución:
###### Métodos desinformados:
``` (path)/filename.jar BPPV 100```
###### Métodos informados:
``` (path)/filename.jar A_STAR 3 ```
