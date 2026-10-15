# Inspección de la Matriz de Confusión - Laboratorio 05

## 1. Identificación de la celda crítica fuera de la diagonal
* **Coordenadas:** Valor real = **9**, Valor predicho = **10**.
* **Frecuencia:** **632** instancias. Es la celda con mayor volumen de error fuera de la diagonal principal del modelo.

## 2. Análisis del costo real de esa confusión
* **Perspectiva local (impacto leve):** Desde un punto de vista puramente numérico y de escala ordinal, confundir un 9 con un 10 tiene un costo operativo bajo, ya que ambas representan valoraciones sumamente positivas y la diferencia conceptual entre ambas es mínima para el paciente.
* **Perspectiva sistémica (sesgo de inflación artificial):** El costo real y crítico radica en que esta celda evidencia un patrón de sesgo generalizado del modelo: **una tendencia sistemática a sobrestimar y concentrar sus predicciones en las categorías superiores (entre 8 y 10)**. 
* **Implicación en producción:** Este sesgo infla de manera irreal la calificación predicha de los medicamentos, haciendo que fármacos con valoraciones reales moderadas o altas pero no perfectas aparezcan artificialmente sobrevalorados. Esto desvirtuaría los indicadores de calidad y podría generar falsas expectativas sobre la eficacia o satisfacción del producto farmacéutico ante una toma de decisiones automatizada.