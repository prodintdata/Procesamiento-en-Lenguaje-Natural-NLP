# Dataset Card

## Identificación
- Nombre: Drug Review Dataset (UCI / Kaggle)
- Fuente original: [Kaggle Drug Review Dataset](https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018/data)
- Responsable: Repositorio UCI Machine Learning / Adaptadores de Kaggle
- Versión o fecha: Versión estándar para benchmarking de PLN (Actualizada)
- Licencia: Licencia de uso público abierto para investigación académica
- Idioma: Inglés

## Propósito y variable objetivo
- **Propósito:** Desarrollar, entrenar y evaluar modelos de procesamiento de lenguaje natural (PLN) y aprendizaje automático para la clasificación de texto y análisis de opiniones de pacientes en el dominio farmacéutico.
- **Variable objetivo (Target):** `rating` (puntuación numérica de satisfacción del paciente en escala ordinal de 1 a 10).

## Diccionario de datos

| Columna | Tipo | Descripción | Valores o unidad |
|---|---|---|---|
| uniqueID | int64 | Identificador único de la reseña | Numérico entero |
| drugName | object | Nombre comercial o genérico del medicamento | Texto descriptivo |
| condition | object | Patología o condición médica diagnosticada | Texto descriptivo |
| review | object | Reseña textual libre escrita por el paciente sobre su experiencia | Texto libre (promedio ~458 caracteres) |
| rating | float64 / int64 | Puntuación cuantitativa otorgada por el paciente | Escala ordinal del 1 al 10 |
| date | object | Fecha de publicación de la reseña | Formato DD-Mes-AA |
| usefulCount | int64 | Cantidad de usuarios que marcaron la reseña como útil | Conteo entero no negativo |

## Procedimiento de obtención
Los datos fueron descargados directamente desde el repositorio público de Kaggle, validados localmente mediante scripts de integridad y colocados en la ruta estandarizada del proyecto (`data/raw/dataset.csv`). Se verificó la ausencia de valores nulos en las columnas clave mediante el script de auditoría.

## Calidad observada
- **Volumen:** 215,063 registros y 7 columnas auditadas exitosamente.
- **Valores Nulos:** 0 nulos en las columnas de texto (`review`) y objetivo (`rating`).
- **Duplicados y Anomalías:** Se detectaron 86,585 duplicados basados en texto idéntico, los cuales reflejan opiniones repetidas o múltiples entradas en la plataforma original, manejados adecuadamente durante las fases de vectorización.
- **Distribución:** Se observa una concentración significativa en las valoraciones más altas (rating 10), lo que indica un sesgo natural de autoselección en las reseñas de los usuarios.

## Población cubierta y excluida
- **Población cubierta:** Pacientes angloparlantes que comparten de forma voluntaria sus experiencias con medicamentos en plataformas web públicas.
- **Población excluida:** Pacientes de habla hispana, poblaciones sin acceso a internet o alfabetización digital, y pacientes bajo tratamientos hospitalarios clínicos cerrados sin exposición digital pública.

## Riesgos, sesgos y usos prohibidos
- **Sesgos previsibles:** Sesgo de autoselección (los usuarios con experiencias extremas, muy positivas o muy negativas, tienden a escribir más) y sesgo idiomático/cultural.
- **Uso prohibido:** Este modelo y corpus **están estrictamente prohibidos** para su uso en diagnósticos clínicos automatizados, recomendaciones de recetas médicas a pacientes reales o toma de decisiones regulatorias de aprobación farmacéutica sin supervisión experta.



