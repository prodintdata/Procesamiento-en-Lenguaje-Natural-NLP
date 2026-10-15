# Nota Técnica: Ajuste de Rendimiento en el Entrenamiento de Modelos (LAB05)

Durante la ejecución del script de entrenamiento (`scripts/train_text.py`) con el dataset completo de más de 200,000 registros, el entorno de desarrollo en la nube (GitHub Codespaces) experimentó una interrupción por limitación de memoria RAM (código de salida 143), debido al alto consumo de recursos al generar la matriz dispersa de TF-IDF combinada con la Regresión Logística.

**Justificación del cambio:**
Para garantizar la ejecución exitosa de los tres pipelines requeridos (`DummyClassifier`, `ComplementNB` y `LogisticRegression`) sin comprometer la estabilidad del Codespace, se implementó una optimización mediante un muestreo aleatorio representativo de 45,000 registros preservando la semilla de aleatoriedad (`random_state=42`). 

Esta medida permitió completar el entrenamiento comparativo, generar correctamente las métricas en `reports/text_metrics.csv`, la matriz de confusión y el artefacto final, manteniendo intacto el rigor metodológico y la estructura del flujo de trabajo.