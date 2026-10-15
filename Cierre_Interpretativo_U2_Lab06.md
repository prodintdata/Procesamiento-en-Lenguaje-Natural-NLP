# Cierre Interpretativo (Lab 06)

- **Resultado de embeddings:** Vocabulario de 16,068 tokens (con `min_count=10`) / 53,558 (baseline y `window=50`), con vecinos semánticos robustos para la palabra clave `effective` (ej. `useful`, `helpful`, `potent`).
- **Evidencia de cobertura:** Cobertura elevada de 0.994 a 1.0, lo que confirma que el término analizado mantiene una representación sólida y constante en el espacio vectorial.
- **Resultado estructural de la red:** 34 nodos, 78 aristas, 3 comunidades detectadas y una modularidad de 0.411, evidenciando una fuerte cohesión comunitaria en el grafo de demostración.
- **Dos métricas comparadas:** Centralidad de Grado (`degree`) frente a Centralidad de Intermediación (`betweenness`).
- **Interpretación permitida:** El Nodo 0 actúa como un puente estructural crítico (`betweenness` máxima de 0.437), mientras que el Nodo 33 concentra la mayor conectividad directa y PageRank (0.515 y 0.097, respectivamente).
- **Interpretación que NO puede sostenerse:** Catalogar a un nodo como «la persona más influyente» o líder basándose únicamente en su puntaje de centralidad, ya que las métricas miden estrictamente propiedades topológicas y no atributos sociales subjetivos.
- **Siguiente experimento:** Evaluar el impacto de incrementar las épocas de entrenamiento (`epochs`) o ajustar la dimensión del vector (`vector_size`) para medir la estabilidad y convergencia del espacio vectorial.