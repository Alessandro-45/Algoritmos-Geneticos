import json

notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

def add_markdown(text):
    lines = text.split("\n")
    source = [line + "\n" for line in lines[:-1]] + [lines[-1]] if lines else []
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": source
    })

add_markdown("""# Actividad 4: Seminario de Investigación
## Computación Evolutiva - Tema 2: Algoritmos Genéticos

Este documento sirve como material de apoyo para la presentación oral (seminario) sobre la aplicación de un Algoritmo Genético en la resolución de un problema ingenieril y científico, basado en el artículo seleccionado.""")

add_markdown("""---
## 1. Referencia Bibliográfica Completa

Idrobo, E.-A., Santos Santos, N., & Pérez Vega, H.-H. (2005). **Aplicación de algoritmos genéticos como herramienta de optimización en la ubicación de pozos de desarrollo y en el trazado de los canales en yacimientos de depositación fluvial**. *CT&F - Ciencia, Tecnología y Futuro*, 3(1), 139-149.""")

add_markdown("""---
## 2. Resumen Escrito del Artículo

La optimización de la explotación petrolera requiere identificar con precisión la ubicación de nuevos pozos de desarrollo (infill wells). Debido a la incertidumbre geológica en yacimientos fluviales (donde existen diversas unidades como arenas de canal, arenas de desborde y arcillas), trazar la conectividad del fluido es sumamente complejo. 

El artículo presenta una metodología novedosa que integra el **modelamiento geoestadístico basado en objetos** con la **computación evolutiva (Algoritmos Genéticos)**. Se codifican en un sistema binario las variables geométricas que definen las características de los canales (espesor, sinuosidad, anchura). El Algoritmo Genético optimiza estos parámetros evolucionando una población de modelos geológicos hasta encontrar aquel que mejor se ajuste a los datos reales de los pozos (proceso evaluado a través de una función objetivo llamada *BLIND TEST*). El resultado es un trazado óptimo de los canales, permitiendo maximizar el factor de recobro de hidrocarburos.""")

add_markdown("""---
## 3. Comprensión del Problema Abordado

**¿Cuál es el problema?**
En los yacimientos de depositación fluvial (antiguos ríos subterráneos que almacenan petróleo), las "arenas de canal" poseen la mejor calidad para extraer hidrocarburos. Sin embargo, no se sabe exactamente por dónde pasaban estos canales entre un pozo y otro. Si se perfora un nuevo pozo "a ciegas", puede caer en zonas de arcilla estéril (Floodplain Shale).

**El desafío:**
Generar un modelo geológico 3D que reconstruya fielmente la trayectoria de estos canales utilizando información muy dispersa (solo se tiene información exacta en los puntos donde ya existen pozos perforados). Tradicionalmente, hacer coincidir modelos matemáticos complejos con la realidad en múltiples puntos simultáneamente es un problema de optimización no lineal muy difícil de resolver de manera analítica.""")

add_markdown("""---
## 4. Explicación del Algoritmo Genético Utilizado

El método propuesto reemplaza la búsqueda a prueba y error por un Algoritmo Genético (AG):

*   **Representación (Genotipo):** Cada "individuo" es un modelo del yacimiento. Su cromosoma está formado por genes codificados en bits que representan variables geométricas: desviación de sinuosidad, espesor, ondulación, relación ancho/espesor, etc., para tres tipos de facies (Channel Sand, Natural Levee, Crevasse Splay).
*   **Población Inicial:** Generada aleatoriamente a través del software *FLUVSIM*, respetando límites geológicos.
*   **Función de Adaptación (Fitness):** Denominada *BLIND TEST*. Se interceptan los modelos generados con los pozos de prueba. Si el modelo dice que a 1000 pies hay arena de canal, y en la vida real el pozo también tiene arena de canal allí, se suma un acierto. Se aplica una función objetivo (FO) ponderada para maximizar la coincidencia.
*   **Selección:** Basada en jerarquía (Ranking). Los modelos que más se parecen a la realidad tienen mayor probabilidad de ser seleccionados como padres.
*   **Cruce:** Intercambio de información geométrica entre los mejores modelos de yacimiento, pudiendo ser cruce por bits, por genes o multipunto.
*   **Mutación:** Cambio de un bit aleatorio para explorar nuevas configuraciones de canales.
*   **Renormalización / Criterios de Parada:** El algoritmo se detiene si la aptitud alcanza 1 (100% de aciertos), si hay estancamiento durante el 14% del tiempo total, o si se cumple el límite máximo de generaciones.""")

add_markdown("""---
## 5. Análisis Crítico: Ventajas y Limitaciones

### Ventajas (Aportes del método)
1.  **Exploración Global:** A diferencia de los métodos clásicos numéricos que se estancan en mínimos locales, el AG evalúa múltiples soluciones en paralelo, siendo ideal para problemas altamente no lineales como la geología estocástica.
2.  **No requiere derivabilidad:** Al no utilizar derivadas, se puede trabajar con variables discontinuas (facies categóricas: arena vs arcilla).
3.  **Reducción de Incertidumbre:** Automatiza y mejora significativamente la correlación entre pozos, reduciendo el riesgo económico millonario de perforar pozos secos.

### Limitaciones
1.  **Costo Computacional:** Cada "evaluación de fitness" requiere correr un software de simulación geoestadística pesada (*FLUVSIM*) para generar el yacimiento 3D y luego hacer la intersección de pozos. Esto consume grandes recursos de máquina.
2.  **Sensibilidad a la Codificación:** La precisión depende de la cantidad de bits asignados. Una discretización muy pobre puede hacer que el óptimo real no se encuentre en el espacio de búsqueda binario.
3.  **Dependencia de la Ponderación:** Los factores de peso en el *BLIND TEST* son asignados por el "usuario de acuerdo a su experticia", lo cual introduce cierto sesgo humano empírico en la función de adaptación.""")

add_markdown("""---
## 6. Conclusiones Personales

El artículo demuestra de forma brillante cómo los Algoritmos Genéticos no son simples ejercicios matemáticos abstractos (como minimizar una función de prueba), sino herramientas industriales poderosas. El enfoque de tratar un **modelo de yacimiento petrolero** entero como un "individuo" o "cromosoma" cambia la perspectiva de cómo abordar la incertidumbre geológica. 

La metodología refleja un entendimiento profundo del concepto de *Fitness*: la supervivencia del más apto es, en este contexto, la supervivencia del modelo geológico que mejor logre predecir la geología real. El uso de software acoplado (AG controlando a FLUVSIM) es un excelente ejemplo de arquitectura de software para ingeniería. Finalmente, este trabajo subraya que en problemas multidimensionales con alto ruido e incertidumbre, las técnicas de computación emergente son a menudo la única vía factible para alcanzar soluciones económicamente viables en la industria petrolera.""")

with open('Seminario_Actividad4.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)
    
print("Notebook Seminario_Actividad4.ipynb generado exitosamente.")
