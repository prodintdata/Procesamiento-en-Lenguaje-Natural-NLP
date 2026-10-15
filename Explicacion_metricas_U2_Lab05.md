# Análisis e Interpretación de Métricas - Laboratorio 05

## 1. Evaluación Crítica del Modelo (Lectura de Métricas)

* **¿Supera el baseline?:** Sí. El modelo de Regresión Logística obtuvo un F1 macro de **0.240**, superando ampliamente al modelo base estratificado (`dummy`, con **0.048**) y al clasificador de Naive Bayes (`naive_bayes`, con **0.079**), lo que confirma que el pipeline logró capturar patrones útiles en el texto.
* **¿Qué clase se pierde?:** La clase **4** presenta el menor rendimiento del modelo, con un *recall* crítico de **0.09** (9%), evidenciando una alta tasa de falsos negativos en esa categoría.
* **¿Qué predicción es poco confiable?:** Las calificaciones intermedias y moderadas-bajas (como las clases 4, 5 y 6) muestran precisiones muy bajas (entre 0.09 y 0.12), lo que indica que las predicciones del modelo en estos rangos generan una alta cantidad de falsos positivos.
* **¿Existe desbalance?:** Sí. La columna `support` demuestra un fuerte desbalance de clases; las categorías extremas (como la clase 10 con 3,538 casos y la clase 1 con 1,501 casos) concentran la mayor cantidad de muestras, mientras que las calificaciones intermedias tienen un soporte mucho menor.
* **¿Puede generalizar?:** Las conclusiones están estrictamente limitadas al idioma inglés, al periodo temporal del corpus original y a reseñas de pacientes recopiladas en plataformas web públicas de participación voluntaria.

---

## 2. Modelo de Explicación y Conclusión

> «La regresión logística obtuvo el mejor F1 macro (0.240). Sin embargo, **la clase 4** presentó el menor recall (0.09), con **múltiples** falsos negativos. En este contexto ese error implica **confundir las reseñas con una valoración moderada-baja con otras categorías de insatisfacción o neutralidad**. Por ello proponemos **implementar balanceo adicional de clases o ajustar los umbrales de decisión** antes de publicar».