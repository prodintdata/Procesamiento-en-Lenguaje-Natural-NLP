# generate_report.py
report_content = """# Informe Ejecutivo: Corpus Público y Clasificador de Texto Reproducible (U02.E03)

* **Estudiante:** Jhonatan Leandro Cabral Pujols
* **Asignatura:** INF-8239 · Procesamiento de Lenguaje Natural (Unidad 02)
* **Docente Académico:** Edwin Ramón José Nolasco

## 1. Selección, Licencia, Trazabilidad y Pregunta
- **Dataset:** Drug Review Dataset (UCI/Kaggle) con SHA-256 verificado.
- **Pregunta analítica:** Predicción de la satisfacción cuantitativa (rating ordinal 1-10) mediante modelos lineales y TF-IDF.

## 2. Auditoría, Duplicados y Prevención de Fuga
- 215,063 registros auditados, 0 nulos en campos críticos y 86,585 duplicados controlados.

## 3. Baseline y Dos Pipelines Comparables
- Modelos evaluados: Dummy, ComplementNB y LogisticRegression. Mejor F1 macro: 0.240.

## 4. Evaluación y Análisis de 20 Errores
- Polarización por léxico extremo, ceguera contextual e ironías detectadas en reports/error_analysis.csv.

## 5. Pruebas, Git y Reproducibilidad
- Entorno gestionado con uv, pruebas con pytest y despliegue local portable con Streamlit.
"""

with open("Informe_U02_E03_NLP.md", "w", encoding="utf-8") as f:
    f.write(report_content)

print("¡Informe generado exitosamente como Informe_U02_E03_NLP.md!")