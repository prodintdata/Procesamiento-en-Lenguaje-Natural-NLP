# Informe Ejecutivo: Corpus Público y Clasificador de Texto Reproducible (U02.E03)

* **Asignatura:** INF-8239 · Ciencia de Datos II (Procesamiento de Lenguaje Natural - Unidad 02)
* **Estudiante:** Jhonatan Leandro Cabral Pujols
* **Docente Académico:** Edwin Ramón José Nolasco
* **Código de Entrega:** U02.E03

---

## 1. Selección, Licencia, Trazabilidad y Pregunta 

* **Dataset Seleccionado:** *Drug Review Dataset (UCI / Kaggle)*, un corpus estándar de reseñas de pacientes sobre medicamentos obtenido de repositorios públicos de referencia.
* **Licencia y Trazabilidad:** Cuenta con licencia de uso público abierto para investigación académica. La trazabilidad y autenticidad del archivo original están garantizadas mediante su huella criptográfica SHA-256 (`8ca8306bd6c9986194fcd5771bc6aea6f0aae786dff7b9dc621c4751cf65da73`) y su almacenamiento estandarizado en la ruta del repositorio (`data/raw/dataset.csv`).
* **Pregunta Analítica:** ¿Es posible predecir con precisión la satisfacción cuantitativa (*rating* ordinal de 1 a 10) de un paciente a partir del análisis léxico de su reseña textual utilizando modelos lineales y representaciones dispersas TF-IDF?

---

## 2. Auditoría, Duplicados y Prevención de Fuga 

* **Volumen y Calidad:** Mediante la ejecución de los scripts de auditoría automatizados (`audit_data.py`), se procesaron e inspeccionaron exitosamente **215,063 registros**, confirmando cero valores nulos en las columnas críticas de texto (`review`) y objetivo (`rating`).
* **Manejo de Duplicados:** Se detectaron **86,585 registros duplicados** basados en texto idéntico, derivados de entradas múltiples o repeticiones en la plataforma original. Estos fueron gestionados rigurosamente durante las fases de partición y vectorización para evitar cualquier fuga de información (*data leakage*) entre los conjuntos de entrenamiento y prueba.
* **Contrato de Datos:** Las validaciones estructurales y de integridad se encuentran respaldadas por pruebas unitarias automatizadas con `pytest` (`tests/test_data_contract.py`), las cuales validan tipos, no nulidad y restricciones de columnas de forma exitosa.

---

## 3. Baseline y Dos Pipelines Comparables 

* **Estrategia de Modelado:** Se implementó una arquitectura modular en `modeling.py` que evalúa tres enfoques comparativos mediante scikit-learn:
  1. **Baseline Estático (`DummyClassifier`):** Estrategia de clase mayoritaria (`most_frequent`).
  2. **Modelo Probabilístico (`ComplementNB`):** Clasificador *Naive Bayes* optimizado para datos desbalanceados y texto disperso.
  3. **Modelo Lineal Robusto (`LogisticRegression`):** Regresión logística con ponderación balanceada de clases (`class_weight="balanced"`) e iteraciones ajustadas (`max_iter=2000`).
* **Nota Técnica de Rendimiento (Entorno de Nube):** Debido a limitaciones operativas de memoria RAM en entornos de desarrollo basados en la nube (código de salida 143), se aplicó un muestreo representativo controlado de **45,000 registros** fijando la semilla aleatoria (`random_state=42`) en `train_text.py`, garantizando la estabilidad y reproducibilidad del entrenamiento sin alterar el rigor metodológico.
* **Desempeño Global (`text_metrics.csv`):**
  * **Regresión Logística (`logistic`):** $F_1$ macro = **0.240** (Modelo seleccionado y persistido en `models/text_model.joblib`).
  * **Naive Bayes (`naive_bayes`):** $F_1$ macro = **0.079**.
  * **Baseline (`dummy`):** $F_1$ macro = **0.048**.

---

## 4. Evaluación y Análisis de 20 Errores 

A partir del análisis detallado en `error_analysis.csv` (respaldado visualmente por la matriz de confusión en `reports/confusion_text.png`), se evaluaron las discrepancias críticas entre los valores reales y las predicciones del modelo:

1. **Polarización por léxico extremo:** El modelo tiende a sesgarse ante palabras aisladas de alta intensidad emocional (ej. *"effective"*, *"awful"*), fallando cuando la reseña presenta argumentos equilibrados o matizados.
2. **Ceguera pragmática y contextual:** Se evidencia incapacidad para interpretar ironías, sarcasmos mordaces (p. ej., reseñas de anticonceptivos que alaban sarcásticamente efectos secundarios graves) y negaciones complejas ("sin efectos secundarios").
3. **Concentración de errores en la matriz de confusión:** El mayor volumen de confusión se concentra en la frontera superior de satisfacción, destacando el caso donde el modelo predice erróneamente la clase máxima (`10`) en reseñas con valoraciones reales de `9` (**632 casos**), lo que refleja un sesgo sistemático de sobreestimación hacia las notas más altas de la escala.

---

## 5. Pruebas, README, Git y Reproducibilidad 

* **Reproducibilidad y Ejecución:** El repositorio está estructurado bajo el gestor de dependencias moderno `uv`, permitiendo reproducir todo el flujo con comandos limpios:
  ```bash
  uv sync
  uv run pytest -q
  uv run python scripts/audit_data.py
  uv run python scripts/train_text.py
  uv run streamlit run app/streamlit_app.py
  ```
* **Portabilidad y Demostración:** Se incluyen archivos de requerimientos limpios con hashes (`requirements-cloud.txt`) y una aplicación web interactiva en Streamlit (`streamlit_app_2.py`) para demostraciones académicas seguras, acompañada de advertencias explícitas sobre las limitaciones del dominio farmacéutico y la prohibición de uso clínico automatizado.
* **Control de Versiones:** Historial de commits estructurado en Git con trazabilidad clara de cada fase del laboratorio.

---

> **Declaración de Uso Responsable de IA:** La inteligencia artificial fue utilizada como apoyo metodológico en la estructuración de notas técnicas, revisión de redacción de hipótesis y síntesis analítica de errores. El código, las auditorías, las ejecuciones locales y las conclusiones del reporte fueron verificados, probados y validados directamente por el estudiante en el entorno de desarrollo.