# Algoritmos Genéticos - Actividades Prácticas

Este repositorio contiene la implementación y el análisis de Algoritmos Genéticos (AG) para la resolución de diversos problemas de optimización. Estas actividades forman parte del Tema 2 de la asignatura **Introducción a la Computación Emergente** (Código: 7006), dictada por el Prof. Esteban Álvarez en la Facultad de Ciencias, Escuela de Física de la Universidad Central de Venezuela.

## Estructura del Repositorio

- `TareaAG.ipynb`: Un Jupyter Notebook interactivo que contiene todas las implementaciones vectorizadas usando `numpy`, así como la documentación teórica y las gráficas analíticas para cada actividad.
- `bohachevsky.py`: Implementación inicial del Algoritmo Genético Simple aplicado a la función de Bohachevsky (Actividad 2).
- `Evaluación AG.pdf` (y otras tareas): Documentos con las especificaciones y lineamientos teóricos de los algoritmos.
- `generate_notebook.py`: Script utilizado para generar de manera automatizada el Jupyter Notebook con todas las resoluciones matemáticas y algorítmicas.

## Fundamentos Teóricos Implementados

Los algoritmos genéticos desarrollados se basan en los principios de la selección natural y constan de los siguientes operadores principales:

1. **Representación Genética:** Dependiendo del problema, se utilizó codificación real, entera y permutaciones.
2. **Función de Adaptación (Fitness):** Formulada específicamente para evaluar la calidad de las soluciones (maximizando $x^2$, minimizando Bohachevsky mediante la inversa con desplazamiento, y minimizando distancia en el TSP).
3. **Selección:** Implementación de **Selección por Torneo** y **Selección por Ruleta**.
4. **Cruce (Recombinación):** Implementación de cruce de un punto, cruce aritmético, cruce BLX-$\alpha$ para dominios continuos y cruce de orden (OX1) para permutaciones en el TSP.
5. **Mutación:** Mutación gaussiana, mutación aleatoria discreta e intercambio (Swap) para mantener la diversidad y explorar el espacio de búsqueda.

## Actividades Resueltas

### Actividad 1: Algoritmo Genético Simple
- **Problema:** Optimización unidimensional de la función $F(x) = x^2$.
- **Enfoque:** Se implementó una clase unificada orientada a objetos, completamente vectorizada, para evaluar la función tanto en dominios enteros como continuos (reales). Se estudió la influencia del cruce y mutación en la velocidad de convergencia.

### Actividad 2: Optimización de Funciones Multimodales
- **Problema:** Minimización de la función de Bohachevsky.
- **Enfoque:** Debido a los mínimos locales de la función de Bohachevsky, el AG Simple tiende a perder presión selectiva. Por ello, se introdujeron **Mecanismos de Renormalización** (Lineal y por Ventana). El notebook muestra una comparativa gráfica demostrando que la renormalización ayuda a mantener la competitividad evolutiva y a explorar mejor el valle óptimo hasta converger en $f(0,0)=0$.

### Actividad 3: Aplicación Práctica - Problema del Viajante de Comercio (TSP)
- **Problema:** Encontrar la ruta más corta que visite un conjunto de ciudades.
- **Enfoque:** Se codificó a cada individuo como una permutación de los índices de las ciudades. Se utilizó el Cruce de Orden (Order Crossover OX1) que evita la duplicación o pérdida de ciudades en las rutas hijas, logrando una convergencia eficiente y visualizando los resultados mediante gráficos del trazado.

## Requisitos y Uso

El proyecto utiliza Python y librerías científicas de optimización.
Se recomienda instalar:

```bash
pip install numpy pandas matplotlib jupyter
```

Para explorar los algoritmos y visualizar los resultados:
1. Clona el repositorio.
2. Ejecuta Jupyter Notebook (`jupyter notebook` o `jupyter lab`).
3. Abre el archivo `TareaAG.ipynb` y ejecuta sus celdas.

### Actividad 4: Seminario de Investigación
- **Problema:** Optimización de la ubicación de pozos de desarrollo en yacimientos de depositación fluvial.
- **Enfoque:** Análisis del artículo "Aplicación de algoritmos genéticos como herramienta de optimización en la ubicación de pozos de desarrollo...". Se creó el notebook `Seminario_Actividad4.ipynb` que resume el artículo, explica el uso del Algoritmo Genético como integrador con la simulación geoestadística (BLIND TEST) y expone un análisis crítico de las ventajas y limitaciones de la metodología empleada.
