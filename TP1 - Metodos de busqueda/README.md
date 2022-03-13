Trabajo Práctico 1 - Métodos de búsqueda

Descripción del problema: 
El juego consiste en 3 postes y 7 discos apilados de mayor a menor, en el poste de la izquierda. El objetivo es mover todos los discos a alguna de las otras dos torres. Hay 2 únicas reglas:
1- Sólo se puede mover un disco por vez
2- No se puede apilar un disco de mayor diámetro sobre uno de menor diámetro

Configuración:
Para aclarar el método de búsqueda que se desea utilizar, abrir el archivo "config.json" y aclarar al lado de "method", una de las siguientes opciones:
- BPA (Búsqueda primero en ancho)
- BPP (Búsqueda primero en profundidad)
- BPPV (Búsqueda en profundidad variable)
- LOCAL_NO_BACK (Búsqueda heurística local sin retroceso)
- LOCAL_BACK (Búsqueda heurística local con retroceso)
- GLOBAL (Búsqueda heurística global)
- A_STAR (Método A*)

Ejecución:
