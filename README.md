# EDA-Lab1

Practica de Estructuras de Datos y Algoritmos centrada en listas enlazadas simples. El proyecto extiende una implementacion base de lista para resolver operaciones adicionales y comprobar su comportamiento con pruebas unitarias.

## Objetivo

Practicar el manejo de nodos, referencias y recorridos sobre listas enlazadas, implementando operaciones que modifican la estructura interna de la lista.

## Contenido

| Archivo | Descripcion |
| --- | --- |
| `slistH.py` | Implementacion base de lista simplemente enlazada. |
| `phase1.py` | Extension `SList2` con operaciones avanzadas. |
| `phase1_unittest.py` | Pruebas unitarias de la practica. |

## Funcionalidades Implementadas

- Eliminacion de la secuencia consecutiva mas larga.
- Deteccion y reparacion de bucles en una lista enlazada.
- Creacion de bucles para pruebas.
- Desplazamientos izquierda/derecha de elementos de la lista.
- Operaciones basicas de lista: insertar, eliminar, buscar y acceder por indice.

## Como Ejecutar Pruebas

```bash
python -m unittest phase1_unittest.py
```

## Aprendizajes

- Manipular punteros/referencias entre nodos.
- Detectar casos limite en estructuras enlazadas.
- Proteger operaciones ante listas vacias o indices invalidos.
- Escribir pruebas para estructuras con estados internos complejos.

## Estado

Proyecto academico finalizado. Se conserva como practica de listas enlazadas y razonamiento sobre estructuras dinamicas.