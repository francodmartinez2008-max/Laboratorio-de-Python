# Simulador de Liga de Fútbol (Torneo Amateur)

Trabajo Integrador para la materia **Algoritmos y Estructuras de Datos**.

## Integrantes del Grupo
* Franco Daniel Martínez
* Tiago Daniel Wlozovitz Barrios
* Gael Cuevas Corsi

## Comisión: **K1.2**

## Descripción General del Sistema
Este sistema es un software de consola desarrollado en Python para administrar un torneo deportivo amateur de fútbol formato liga (todos contra todos). El cual permite la carga validada de una cantidad par de equipos (entre 2 y 20 participantes), planifica y empareja de forma automática los cruces de todas las fechas del torneo, calcula en tiempo real los puntos acumulados (3 por victoria, 1 por empate), goles a favor y goles en contra, y por ultimo genera y muestra una tabla de posiciones ordenada bajo criterios deportivos oficiales:
  1. Mayor cantidad de Puntos.
  2. Mejor Diferencia de Goles (DG).
  3. Mayor cantidad de Goles a Favor (GF).
Por ultimo, escanea linealmente las estadísticas al finalizar el fixture para determinar el campeon.

## Instrucciones de Ejecución
### Prerrequisitos e Instalación
1. Tener instalado **Python 3.x** en la computadora.
2. Descargar el archivo `labpython.py` en una carpeta local.
3. Abrir una terminal (consola de comandos) en la ubicación de dicha carpeta y ejecutar:
   ```bash
   python labpython.py

## Guía para realizar la prueba de escritorio (Simulación del Torneo)
. Paso 1: Seleccionar la opcion 1 del menu para registrar los equipos
Ingresar una cantidad par de equipos entre 2 y 20 (por ejemplo: 4)
Escribir los nombres de los equipos 
. Paso 2: Seleccionar la opcion 2 del menu para visualizar y realizar el fixture
Ingresar la cantidad de goles de cada equipo que usted desee hasta terminar todos los cruzes
. Paso 3: Seleccionar la opcion 3 del menu para mostrar la tabla de posiciones y el campeon del torneo
. Paso 4: Seleccionar la opcion 4 del menu para salir del programa

## Uso de Inteligencia Artificial (IA)
* **IA Utilizada:** Gemini (Google).
* **¿Para qué y cómo se utilizó?:** Para garantizar que el desarrollo no excediera los contenidos brindados por la catedra, se le proporcionaron a la IA los módulos
teóricos oficiales brindados por la cátedra. Toda la asistencia se limitó estrictamente a las estructuras analizadas en dichos documentos. En base a esa teoría, se
interactuó con la IA mediante un proceso de consultas por pasos. Se utilizó principalmente para resolver el desafío de la **función de ordenamiento de la tabla de posiciones**
y la implementación de la **diferencia de goles** como criterio de desempate. Se empleó tambien para recibir explicaciones conceptuales detalladas sobre el funcionamiento y
propósito exacto de funciones nativas de manipulación de arreglos como `.pop()`, `.index()` e `.insert()`, utilizadas para resolver la rotación de equipos en el fixture.