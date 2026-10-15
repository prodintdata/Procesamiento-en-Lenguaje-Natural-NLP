### Hipótesis de Experimentación (`window = 50`)

- **Planteamiento:** Dado que una ventana de contexto estándar (ej. `window=5`) se limita a capturar sinónimos gramaticales y vecindades inmediatas, al ampliar masivamente el parámetro `window` a un valor de 50, el modelo Word2Vec incorporará un contexto asociativo y temático de mayor alcance dentro de las reseñas del corpus.
- **Criterio de validación (Falsabilidad):**
  - Si al reentrenar y evaluar con una palabra clave como `effective`, los vecinos se mantienen estrictamente idénticos y acotados a sinónimos directos, **descartamos** que el tamaño de la ventana altere la dimensión temática del espacio vectorial.
  - Si, por el contrario, la lista de vecinos incorpora términos asociados a la experiencia general del paciente, consecuencias, juicios de valor o contrastes más amplios (como `ineffective`, `frustrating` o `difficult`), **aceptamos** que una ventana amplia favorece el descubrimiento de relaciones tópicas globales por encima de la estricta sustitución sintáctica.

---

### Evidencia y Resultado Obtenido (`window = 50`)

- **Vocabulario:** 53,558 tokens (estable, ya que el corpus no cambió).
- **Cobertura:** 1.0 (100%).
- **Vecinos semánticos obtenidos:** 
  `[('useful', 0.817), ('helpful', 0.767), ('potent', 0.684), ('beneficial', 0.683), ('ineffective', 0.646), ('important', 0.645), ('difficult', 0.640), ('strong', 0.633), ('frustrating', 0.627), ('reliable', 0.618)]`

### Interpretación del Hallazgo:
Al ampliar la ventana a 50, **aceptamos la hipótesis**. Aunque el núcleo de sinónimos directos (`useful`, `helpful`) se conserva, el espacio vectorial ahora es capaz de capturar relaciones de escala global y polaridad opuesta o experiencial que están presentes en el documento pero más separadas en la estructura de la oración (como `ineffective` y `frustrating`). Esto demuestra que el modelo deja de mirar solo el entorno inmediato de la palabra para capturar el contexto temático general de las opiniones farmacéuticas.

---

### Hipótesis de Experimentación (`min_count = 10`)

- **Planteamiento:** Dado que el corpus contiene múltiples términos infrecuentes, errores tipográficos o jerga aislada, al incrementar el parámetro `min_count` de 1 a 10, exigiremos que cada palabra aparezca al menos 10 veces para ser integrada en el diccionario, eliminando el ruido ortográfico y reduciendo drásticamente la dimensionalidad del vocabulario.
- **Criterio de validación (Falsabilidad):**
  - Si al comparar los resultados con el modelo base el tamaño del vocabulario se mantiene inalterado y los vecinos semánticos de palabras clave como `effective` no sufren cambios sustanciales, **descartamos** que el ruido de baja frecuencia distorsionara la representación vectorial.
  - Si, por el contrario, el vocabulario se reduce significativamente y los vecinos se limpian o estabilizan en un núcleo semántico más coherente, **aceptamos** que la restricción de frecuencia elimina eficazmente el ruido y mejora la calidad del espacio latente.

---

### Evidencia y Resultado Obtenido (`min_count = 10`)

- **Vocabulario:** 16,068 tokens (una reducción masiva frente a los 53,558 tokens del modelo base, eliminando más de 37,000 palabras infrecuentes o erróneas).[cite: 8]
- **Cobertura:** 0.994 (99.4%, lo que indica que la gran mayoría de las apariciones de la palabra analizada se conservaron dentro del espacio de entrenamiento a pesar del filtro).[cite: 8]
- **Vecinos semánticos obtenidos:** 
  `[('useful', 0.847), ('helpful', 0.840), ('efficient', 0.829), ('potent', 0.793), ('beneficial', 0.774), ('powerful', 0.768), ('inexpensive', 0.762), ('sedating', 0.751), ('expensive', 0.746), ('costly', 0.719)]`[cite: 8]

### Interpretación del Hallazgo:
Al establecer `min_count = 10`, **aceptamos la hipótesis**. La reducción del vocabulario de más de 53 mil a 16,068 términos demuestra que el corpus albergaba una enorme cantidad de ruido (errores tipográficos, tokens únicos o palabras de una sola aparición). A pesar de esta intensa poda, la palabra clave `effective` retiene una cobertura casi perfecta (0.994) y sus vecinos cercanos se vuelven sumamente limpios y cohesivos (`useful`, `helpful`, `efficient`, `potent`), consolidando un espacio vectorial robusto libre de distorsiones superficiales.