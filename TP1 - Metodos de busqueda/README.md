# Trabajo Práctico 1 - Métodos de búsqueda

## Descripción del problema:
El juego consiste en 3 postes y 7 discos apilados de mayor a menor, en el poste de la izquierda. El objetivo es mover todos los discos a alguna de las otras dos torres. Hay 2 únicas reglas:

**1 -** Sólo se puede mover un disco por vez

**2 -** No se puede apilar un disco de mayor diámetro sobre uno de menor diámetro

## Configuración:
Para aclarar el método de búsqueda que se desea utilizar, abrir el archivo `config.properties` y aclarar al lado de la variable `method`, una de las siguientes opciones:
- BPA (Búsqueda primero en ancho)
- BPP (Búsqueda primero en profundidad)
- BPPV (Búsqueda en profundidad variable)
- LOCAL_NO_BACK (Búsqueda heurística local sin retroceso)
- LOCAL_BACK (Búsqueda heurística local con retroceso)
- GLOBAL (Búsqueda heurística global)
- A_STAR (Método A*)

Si escoge un método que utilice heurísticas (estos son `LOCAL_BACK, LOCAL_NO_BACK, GLOBAL y A_STAR`),
tiene la posibilidad de utilizar tres heurísticas. Las mismas se modifican de la misma manera que el método, desde `config.properties`.

Existen 3 opciones de heurística, las primeras dos siendo admisibles y la tercera no admisible:
- 1: Función de transición definida por cantidad de discos que faltan ubicar en último poste
- 2: Función de transición definida por discos que aún no están en último poste + discos que están en último poste pero mal ubicados
  (les falta alguno por debajo. Ej: 7 - 5 - 4 tiene dos discos mal ubicados).
- 3:

## Ejecución:
Ejecutar el archivo .jar