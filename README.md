# INF-8239 · Unidad 02 · Proyecto NLP: Corpus Público y Clasificador de Texto Reproducible

**Asignatura:** INF-8239 Ciencia de Datos II  
**Estudiante:** Jhonatan Leandro Cabral Pujols  
**Autor Académico / Base:** Edwin Ramón José Nolasco  
**Código de Entrega:** U02.E03  

Proyecto reproducible para el procesamiento de lenguaje natural (NLP), auditoría de datos, modelado de texto y despliegue interactivo basado en el *Drug Review Dataset* (UCI / Kaggle).

---

## 1. Descripción del Proyecto

Este repositorio integra de forma reproducible las evidencias producidas en los laboratorios (LAB04, LAB05 y LAB06). Su objetivo principal es construir, entrenar y evaluar modelos de clasificación de texto supervisada para predecir la satisfacción cuantitativa (*rating* ordinal de 1 a 10) de pacientes a partir de reseñas de medicamentos, manteniendo estrictos controles contra la fuga de datos y asegurando la reproducibilidad total mediante el gestor de dependencias moderno `uv`.

---

## 2. Estructura del Repositorio

```text
├── app/
│   └── streamlit_app_2.py     # Aplicación web interactiva para demostraciones
├── data/
│   ├── processed/             # Datos procesados (.gitkeep)
│   ├── raw/                   # Datos crudos del dataset completo
│   └── sample/                # Dataset de demostración inicial (demo_text.csv)
├── docs/
│   ├── DATASET_CARD_2.md      # Tarjeta descriptiva del dataset
│   └── dataset_candidates.csv # Candidatos de datasets evaluados
├── models/                    # Modelos serializados (text_model.joblib, word2vec.model)
├── reports/                   # Métricas, análisis de errores, matrices y redes generadas
├── scripts/
│   ├── audit_data.py          # Script de auditoría e inspección de integridad
│   ├── download_data.py       # Automatización de descarga y validación SHA-256
│   ├── embeddings_network.py  # Generación de embeddings Word2Vec y redes (Zachary's Karate Club)
│   └── train_text.py          # Pipeline de entrenamiento, validación y métricas
├── src/
│   └── inf8239_u02/
│       ├── __init__.py        # Versión del paquete
│       ├── config.py          # Gestión centralizada de configuración (Settings)
│       ├── data.py            # Funciones de carga, validación y hashes criptográficos
│       └── modeling.py        # Definición de pipelines de Scikit-Learn
├── tests/
│   ├── test_data_contract.py  # Pruebas unitarias para contratos de datos
│   ├── test_embeddings_network.py # Pruebas de tokenización y grafos
│   └── test_text_model.py     # Pruebas de pipelines de clasificación
├── .env.example               # Plantilla de variables de entorno
├── pyproject.toml             # Configuración del proyecto y dependencias (uv)
└── README.md                  # Documentación oficial del proyecto
```

---

## 3. Inicio Rápido y Requisitos

Para poner en marcha el entorno y replicar los resultados, asegúrese de tener instalado [uv](https://github.com/astral-sh/uv).

1. **Clonar e instalar dependencias:**
   ```bash
   uv python install 3.12
   uv sync
   ```

2. **Configurar el entorno:**
   Copie el archivo de ejemplo `.env.example` como `.env` en la raíz del proyecto y configure el origen de datos deseado:
   ```bash
   cp .env.example .env
   ```

---

## 4. Guía Paso a Paso para Reproducir Resultados

Siga rigurosamente esta secuencia de comandos para auditar, entrenar y evaluar los modelos:

### Paso 1: Auditoría de Datos e Integridad
Verifique las dimensiones, nulos, duplicados y distribución del corpus mediante el script de auditoría:
```bash
uv run python scripts/audit_data.py
```

### Paso 2: Ejecución de Pruebas Unitarias
Valide que los contratos de datos, las pruebas de tokenización y los pipelines pasen exitosamente:
```bash
uv run pytest -q
```

### Paso 3: Entrenamiento de Modelos y Generación de Reportes
Ejecute el script de entrenamiento para procesar el texto con representaciones TF-IDF, entrenar los clasificadores (Baseline, Naive Bayes y Regresión Logística) y exportar las métricas de rendimiento y matriz de confusión:
```bash
uv run python scripts/train_text.py
```
*(Nota: El script incorpora un muestreo controlado de 45,000 registros para optimizar el uso de memoria RAM en entornos de desarrollo en la nube).*

### Paso 4: Análisis de Embeddings y Redes de Demostración
Genere los embeddings de palabras y el análisis estructural de redes (ej. *Zachary's Karate Club*):
```bash
uv run python scripts/embeddings_network.py --network-demo
```

### Paso 5: Despliegue de la Interfaz Interactiva (Streamlit)
Inicie la aplicación web local para realizar pruebas de clasificación interactivas:
```bash
uv run streamlit run app/streamlit_app_2.py
```

---

## 5. Interpretación y Uso Responsable

* **Evaluación:** Toda conclusión generada en la carpeta `reports/` separa observación empírica, evidencia cuantitativa, interpretación analítica y decisiones metodológicas.
* **Limitaciones y Ética:** Este modelo y corpus están **estrictamente prohibidos** para su uso en diagnósticos clínicos automatizados, recomendaciones de recetas médicas a pacientes reales o toma de decisiones regulatorias farmacéuticas sin supervisión experta.