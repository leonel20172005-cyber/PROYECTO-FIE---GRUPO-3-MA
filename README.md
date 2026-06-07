# Modelo Predictivo de Ancho de Banda - FIE

Este repositorio contiene el código fuente del proyecto desarrollado por el Grupo 3 para el análisis numérico de la red institucional de la Facultad de Informática y Electrónica (FIE).

El objetivo es modelar matemáticamente la fluctuación de la velocidad del internet durante el día utilizando la **Interpolación Polinómica de Lagrange**.

## Estructura de Archivos
* `calculo_lagrange.py`: Contiene la lógica matemática (bucles, control de división por cero) para generar el polinomio de grado 3.
* `grafica_interactiva.py`: Script que utiliza Plotly para renderizar una visualización web dinámica de la curva predictiva.
