### 5. Análisis de la Red de Demostración (Club de Karate de Zachary)

#### Descripción Estructural de la Red
Antes de interpretar las métricas, es necesario definir los componentes básicos de esta red de demostración:
- **Nodos:** Representan a cada uno de los 34 miembros individuales (actores) que componían el club de karate en el estudio clásico.
- **Aristas:** Representan las 78 interacciones o vínculos sociales documentados entre dichos miembros fuera de las actividades formales del dojo.
- **Información no incluida:** No contempla la evolución dinámica temporal de las relaciones, la intensidad exacta de conflictos interpersonales profundos ni atributos externos adicionales más allá de su conectividad topológica estructural.

---

### 6. Resultados Cuantitativos y Métricas Estructurales

A partir de la ejecución del script de análisis con la red de demostración (`--network-demo`), se obtuvieron las siguientes métricas globales:
- **Nodos:** 34
- **Aristas:** 78
- **Comunidades detectadas:** 3 subgrupos principales.
- **Modularidad:** 0.411 (un valor superior a 0.3/0.4, lo que denota una estructura comunitaria fuerte y bien definida en clanes o facciones).

#### Interpretación Prudente de Centralidades Clave
Aplicando los criterios de lectura prudente y respetando la prohibición interpretativa de asociar la centralidad a un juicio subjetivo de "liderazgo o influencia social", el análisis de la tabla de centralidades (`reports/centralities.csv`) destaca los siguientes nodos críticos:

1. **Nodo 33 (Máxima conectividad y prestigio estructural):**
   - **Métricas:** Presenta el grado más alto (`degree = 0.515`) y el PageRank más alto (`pagerank = 0.097`) de la red, respaldado por una intermediación de `betweenness = 0.304`.
   - **Interpretación:** Cuenta con una gran cantidad de conexiones locales directas y, al poseer un PageRank superior, recibe enlaces procedentes de otros nodos que también son estructuralmente relevantes en la red.

2. **Nodo 0 (Máximo puente estructural):**
   - **Métricas:** Registra la intermediación más alta de toda la red (`betweenness = 0.437`), un grado muy elevado (`degree = 0.484`) y un PageRank de `0.088`.
   - **Interpretación:** Aunque es ligeramente superado en grado por el nodo 33, su posición topológica destaca por poseer la mayor capacidad de intermediación, actuando como un puente estructural indispensable entre distintas regiones o comunidades del grafo.

3. **Nodo 32 (Soporte de conectividad local):**
   - **Métricas:** Muestra un grado considerable (`degree = 0.363`) y una intermediación notable (`betweenness = 0.145`).
   - **Interpretación:** Funciona como un punto de alta cohesión local dentro de su subgrupo.

