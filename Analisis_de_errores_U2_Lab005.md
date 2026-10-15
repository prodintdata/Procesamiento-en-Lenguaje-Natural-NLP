# Análisis del Caso 1 (Error de Predicción)

* **Caso analizado:** Fila 2 del archivo de errores (`reports/error_analysis.csv`). Valor real: **9**, Valor predicho del modelo: **10**.
* **Texto de la reseña:** La paciente explica que el tratamiento le ayudó parcialmente (*"sentí un 60% de mejoría"*), menciona que apenas va comenzando (*"tomé la segunda dosis"*), expresa una expectativa a futuro (*"espero que se cure por completo"*) y reporta un efecto secundario menor (*"un dolor de cabeza leve"*).
* **Motivo del error del modelo:** El modelo de Regresión Logística se basa en la frecuencia de palabras sueltas. Al detectar términos positivos repetidos como *"better"* (mejor) y *"clear up"* (resolverse), el clasificador asume de forma automática que se trata de una reseña perfecta (10). 
* **Limitación detectada:** El modelo es ciego ante los porcentajes de progreso parcial (*"60%"*), las expectativas condicionales (*"esperemos que..."*) y los efectos adversos menores, interpretando erróneamente una mejoría en proceso como un resultado absoluto.

# Análisis del Caso 2 (Error Crítico de Predicción)

* **Caso analizado:** Fila 3 del archivo de errores (`reports/error_analysis.csv`). Valor real: **2**, Valor predicho del modelo: **9**.
* **Texto de la reseña:** La paciente detalla un efecto secundario estético severo por una pastilla anticonceptiva (*"mi cara parece un juego de unir puntos y duele"*), lo cual la obligó a cambiar de medicamento. Aunque al inicio menciona que un tratamiento pasado fue exitoso, su evaluación global del producto actual es pésima (calificación real: 2).
* **Motivo del error del modelo:** El modelo predijo erróneamente un 9 debido a un falso positivo léxico. El clasificador detectó términos de polaridad muy positiva al inicio del texto (*"successful"*) y una mención de alivio parcial (*"pain has been much better"*).
* **Limitación detectada:** El modelo es incapaz de separar el contexto histórico del texto actual. Además, falla completamente al procesar metáforas hiperbólicas (*"connect the dot"*) y al ponderar adecuadamente que un efecto secundario grave (acné quístico doloroso) anula por completo cualquier mejoría menor en el dolor, dando una calificación muy baja que el enfoque lineal pasa por alto.


# Análisis del Caso 3 (Error Menor de Predicción)

* **Caso analizado:** Fila 4 del archivo de errores (`reports/error_analysis.csv`). Valor real: **1**, Valor predicho del modelo: **2**.
* **Texto de la reseña:** La usuaria relata una experiencia traumática absoluta con un anticonceptivo que le destruyó el cabello (pérdida en mechones, parches de calvicie, uso de Rogaine y cortes de emergencia para ocultarlo) tras haber sufrido acné quístico y cambios de humor severos.
* **Motivo de la desviación del modelo:** Aunque el error numérico es mínimo (predijo 2 y era 1), la duda surge porque todo el texto es drásticamente negativo. El modelo predijo un 2 debido a que el texto incluye una frase de transición sobre la adaptación biológica (*«Then I got use to the hormones and those symptoms went away»*).
* **Limitación detectada:** El clasificador lineal asigna pesos parciales a frases de transición temporal sin entender el impacto real de la severidad acumulativa. No logra diferenciar la distancia emocional entre un desastre total (1) y un problema grave pero atenuado por el tiempo (2).


# Análisis del Caso 4 (Error por Sentimientos Mixtos)

* **Caso analizado:** Fila 5 del archivo de errores (`reports/error_analysis.csv`). Valor real: **6**, Valor predicho del modelo: **1**.
* **Texto de la reseña:** El paciente describe una dicotomía clínica: por un lado, el fármaco mejoró drásticamente su estado de ánimo y claridad mental (*«haciéndome sentir mucho más feliz y sin pensamientos distorsionados»*); por el otro, el efecto secundario físico es intolerable (*«el mareo es terrible»*).
* **Motivo del error del modelo:** El modelo predijo un 1 (la peor calificación posible) porque detectó de forma aislada términos negativos de alto impacto como *"dizzy"* y *"awful"*. 
* **Limitación detectada:** El clasificador lineal carece de la capacidad para ponderar un balance de costos y beneficios. Al encontrar una queja física severa, el modelo ignora por completo que el balance psicológico general es positivo, lo que justifica una calificación real intermedia (6) que el enfoque de bolsa de palabras no pudo calcular.


# Análisis del Caso 5 (Error por Sesgo de Cierre Léxico)

* **Caso analizado:** Fila 6 del archivo de errores (`reports/error_analysis.csv`). Valor real: **5**, Valor predicho del modelo: **10**.
* **Texto de la reseña:** Un historial médico sumamente complejo y traumático de varios años (insuficiencia cardíaca, taquicardias, fatiga incapacitante por toxicidad de medicamentos) que culmina con un procedimiento exitoso y recuperación de energía al final (*«Found ablation effective»*).
* **Motivo del error del modelo:** El modelo predijo un 10 perfecto porque el vectorizador le otorga un peso positivo desproporcionado a la palabra clave *"effective"* ubicada al final del texto. 
* **Limitación detectada:** El clasificador carece de comprensión temporal y semántica. Las múltiples patologías y crisis graves descritas en el cuerpo del texto actúan como términos técnicos neutrales para el algoritmo, mientras que el modelo se deja cegar por un único término de éxito final, sobreestimando por completo una reseña que en la realidad representa un balance neutral/intermedio (5).

# Análisis del Caso 6 (Error por Desbalance de Polaridad Léxica Positiva)

* **Caso analizado:** Fila 7 del archivo de errores (`reports/error_analysis.csv`). Valor real: **7**, Valor predicho del modelo: **9**.
* **Texto de la reseña:** La paciente describe efectos secundarios gastrointestinales severos y constantes (náuseas, vómitos matutinos, diarrea), los cuales logra mitigar mediante una dieta estricta, obteniendo además una excelente pérdida de peso (34 libras) y control de azúcar. Cierra con una postura muy satisfecha.
* **Motivo del error del modelo:** El modelo predijo un 9 porque el texto contiene frases de polaridad sumamente alta concentradas en el éxito del tratamiento (*«helped me tremendously»*, *«I am very happy with the medication»*). 
* **Limitación detectada:** El clasificador lineal sobrepondera el vocabulario de felicidad y ayuda extrema, restando peso o interpretando de manera insuficiente el costo físico real (vómitos y diarrea frecuente). Esto provoca que la calificación real (7, que refleja un balance con efectos secundarios molestos) sea sobreestimada por el algoritmo hacia una categoría casi perfecta (9).

# Análisis del Caso 7 (Error por Sesgo de Éxito Funcional)

* **Caso analizado:** Fila 8 del archivo de errores (`reports/error_analysis.csv`). Valor real: **8**, Valor predicho del modelo: **10**.
* **Texto de la reseña:** La usuaria relata una experiencia sumamente aterradora y dolorosa a nivel físico (retraso menstrual de 40 días, síntomas de embarazo, dolor constante), pero concluye enfáticamente que el anticonceptivo cumplió su propósito (*«The pill WORKED»*).
* **Motivo del error del modelo:** El modelo predijo la calificación máxima (10) porque el clasificador lineal prioriza las expresiones contundentes de éxito funcional del fármaco (incluso resaltadas en mayúsculas: *«WORKED»*).
* **Limitación detectada:** El modelo vuelve a mostrar su incapacidad para ponderar el sufrimiento físico intermedio. Al encontrar que el medicamento funcionó, el algoritmo asume un desempeño perfecto, ignorando que los efectos secundarios traumáticos reducen la satisfacción real de la paciente a una nota de 8.

# Análisis del Caso 8 (Error por Sobrecarga de Léxico Punitivo)

* **Caso analizado:** Fila 9 del archivo de errores (`reports/error_analysis.csv`). Valor real: **3**, Valor predicho del modelo: **1**.
* **Texto de la reseña:** La paciente relata una experiencia sumamente dolorosa (cólicos insoportables, hemorragias con coágulos gigantes y anemia que requirió sala de emergencias). No obstante, muestra una gran madurez al inicio y al final al reconocer que cada cuerpo reacciona distinto y que el anticonceptivo sí cumplió su objetivo principal, justificando su calificación real de 3.
* **Motivo del error del modelo:** El modelo predijo un 1 debido a una severa penalización algorítmica impulsada por la enorme acumulación de términos de crisis física e intensa penalización léxica (*«stabbed»*, *«anemic»*, *«ER»*).
* **Limitación detectada:** El clasificador lineal carece de la capacidad para procesar la matización humana ("sé que cada cuerpo es diferente"). Al encontrar tantas palabras de dolor agrupadas, el modelo asume de forma automática una catástrofe total (1), siendo totalmente ciego ante la ponderación racional y justa que hace la paciente.

# Análisis del Caso 9 (Error por Sobreestimación de Expectativa Positiva)

- **Caso analizado:** Fila 10 del archivo de errores (`reports/error_analysis.csv`). Valor real: **8**, Valor predicho del modelo: **9**.
- **Texto de la reseña:** La paciente describe una experiencia inicial con *Estring* que incluye molestias físicas menores (irritación leve y ardor al orinar), expresando el deseo de que sea temporal y la duda de si retirarlo en el futuro, otorgando finalmente una valoración positiva pero moderada (8).
- **Motivo del error del modelo:** El modelo predijo un 9 y el valor real fue 8, representando una desviación muy pequeña. El clasificador detectó términos de apoyo y expectativa favorable como *"well"* y *"Hopefully"*.
- **Limitación detectada:** La discrepancia es mínima porque el texto carece de extremos léxicos violentos. No obstante, el modelo tiende a sobreestimar ligeramente al encontrar frases condicionales de esperanza (*"Hopefully"*), interpretándolas como un éxito superior al que la paciente experimentó en la realidad.

# Análisis del Caso 10 (Error por Contaminación Léxica de Estados Pasados)

- **Caso analizado:** Fila 11 del archivo de errores (`reports/error_analysis.csv`). Valor real: **1**, Valor predicho del modelo: **3**.
- **Texto de la reseña:** La paciente relata una experiencia psiquiátrica y emocional devastadora debido al anticonceptivo (depresión severa, aislamiento, hinchazón, acné y niebla mental). Utiliza palabras de bienestar únicamente en pasado para contrastar con su estado actual de infelicidad absoluta, otorgando la calificación mínima (1).
- **Motivo del error del modelo:** El modelo predijo un 3 en lugar de un 1 debido a la presencia de términos con alta polaridad positiva como *"happy"* y *"kind"* dentro del texto.
- **Limitación detectada:** El clasificador carece de comprensión temporal y contextual. Al ser un modelo de bolsa de palabras, no distingue que la usuaria describe virtudes y felicidad en tiempo pasado ("solía ser feliz") como contraste a su situación actual, lo que provoca que el algoritmo sobrestime levemente la puntuación y falle al asignar un 3.

# Análisis del Caso 11 (Error por Incongruencia entre Sentimientos Mixtos y Ponderación Léxica)

- **Caso analizado:** Fila 12 del archivo de errores (`reports/error_analysis.csv`). Valor real: **8**, Valor predicho del modelo: **5**.
- **Texto de la reseña:** La paciente describe sentimientos encontrados con el anticonceptivo Sprintec (ya no tiene cólicos severos y su acné mejoró, pero le causa depresión, tristeza y periodos extremadamente largos de 17 días), concluyendo con una recomendación positiva global.
- **Motivo del error del modelo:** El modelo predijo un 5 (neutral) porque el texto contiene una alta densidad de problemas emocionales y físicos molestos descritos explícitamente[cite: 2].
- **Limitación detectada:** El clasificador lineal promedia o colapsa el texto hacia una zona neutral al detectar la coocurrencia de quejas de salud mental y duración anormal del periodo, perdiendo de vista la recomendación final positiva y el alivio de los cólicos que elevan la calificación real a un 8.

# Análisis del Caso 12 (Error por Subestimación de Enfoque Comercial Descontinuado)

- **Caso analizado:** Fila 13 del archivo de errores (`reports/error_analysis.csv`). Valor real: **10**, Valor predicho del modelo: **7**.
- **Texto de la reseña:** La usuaria elogia de forma absoluta el producto Alli para la pérdida de peso (*«works great for me»*, perdió 30 libras y otras 12 después), expresando tristeza y expectativa por su retirada temporal del mercado.
- **Motivo del error del modelo:** El modelo predijo un 7 en lugar de la máxima puntuación (10) porque el texto incluye menciones sobre haber dejado de tomarlo temporalmente debido a retiros del mercado y fluctuaciones de peso previas.
- **Limitación detectada:** El modelo penaliza analíticamente la mención de retiradas del mercado (*«latest recall»*) y parones en el consumo, interpretando estas incidencias externas como una reducción en la satisfacción del producto, a pesar de que el tono general y el resultado final son de absoluta admiración (10).

# Análisis del Caso 13 (Error por Subestimación de Efectos Secundarios Íntimos y Físicos)

- **Caso analizado:** Fila 14 del archivo de errores (`reports/error_analysis.csv`). Valor real: **3**, Valor predicho del modelo: **5**.
- **Texto de la reseña:** La paciente relata una experiencia sumamente negativa de cinco meses con un anticonceptivo que le causó dolor constante en los senos, aumento de peso imposible de bajar, hinchazón permanente y una pérdida total del interés sexual que dañó severamente su relación de pareja.
- **Motivo del error del modelo:** El modelo predijo un 5 (neutral) porque el vocabulario de la reseña mezcla descripciones de cambios físicos y malestares que el clasificador no logra estructurar como una catástrofe total.
- **Limitación detectada:** El clasificador lineal falla al no comprender la gravedad social y psicológica de los efectos adversos íntimos (pérdida total de la libido y daño de pareja). Al no encontrar insultos o groserías explícitas, el modelo suaviza erróneamente la predicción llevándola a un punto medio tibio (5) en lugar de reflejar la insatisfacción real de la usuaria (3).

# Análisis del Caso 14 (Error por Sobreestimación de Estabilidad Psiquiátrica)

- **Caso analizado:** Fila 15 del archivo de errores (`reports/error_analysis.csv`). Valor real: **8**, Valor predicho del modelo: **9**.
- **Texto de la reseña:** Una paciente con historial de ansiedad, TEPT y acoso detalla el uso exitoso de un medicamento (citalopram) que le ayuda a manejar el estrés y las reacciones de enojo, mencionando únicamente efectos secundarios físicos menores y temporales (náusea leve con el estómago vacío).
- **Motivo del error del modelo:** El modelo predijo un 9 y el valor real fue 8 debido a la alta concentración de vocabulario orientado al control terapéutico exitoso, la estabilidad emocional y la reducción de la ira.
- **Limitación detectada:** El modelo sobreestima ligeramente la puntuación al verse inundado por términos de gestión psicológica positiva y alivio sintomático, tratando los pequeños efectos adversos físicos como anécdotas menores y arrastrando la predicción un punto por encima de la evaluación prudente de la paciente (8).

# Análisis del Caso 15 (Error por Subestimación de Inestabilidad Emocional Progresiva)

- **Caso analizado:** Fila 16 del archivo de errores (`reports/error_analysis.csv`). Valor real: **4**, Valor predicho del modelo: **3**.
- **Texto de la reseña:** La paciente describe cómo un anticonceptivo (implanon) alteró su estabilidad mental a partir del mes 16, provocándole cambios de humor extremos, discusiones de pareja inusuales, ansiedad severa, celos y opresión en el pecho, concluyendo que planea retirárselo pronto.
- **Motivo del error del modelo:** El modelo predijo un 3 y el valor real fue 4, mostrando una cercanía aceptable gracias a que el clasificador detectó múltiples términos de malestar emocional.
- **Limitación detectada:** Aunque la predicción es cercana, el modelo penaliza de forma ligeramente más severa (3) debido a la acumulación de palabras de ansiedad y cambios de humor, capturando adecuadamente que la experiencia es mala, aunque sin lograr calibrar con precisión exacta el matiz moderadamente bajo de un 4.

# Análisis del Caso 16 (Error por Sarcasmo e Ironía Léxica)

- **Caso analizado:** Fila 17 del archivo de errores (`reports/error_analysis.csv`). Valor real: **1**, Valor predicho del modelo: **2**.
- **Texto de la reseña:** La usuaria utiliza una ironía mordaz y un humor negro evidente para calificar un anticonceptivo: afirma que *"funciona como anticonceptivo porque nunca tendrás sexo ya que sangrarás todo el mes y no tendrás deseo sexual"*.
- **Motivo del error del modelo:** El modelo predijo un 2, acercándose a la realidad (1) pero fallando por completo en comprender la lógica detrás de la frase.
- **Limitación detectada:** Los clasificadores lineales basados en TF-IDF son totalmente ciegos al sarcasmo y a la ironía contextual. El modelo asocia la palabra *"birth control"* (anticonceptivo) y la negación de tener relaciones con un contexto descriptivo ordinario, sin entender que la frase es una crítica furibunda disfrazada de chiste cínico.

# Análisis del Caso 17 (Error por Descompensación de Costo-Beneficio Farmacológico)

- **Caso analizado:** Fila 18 del archivo de errores (`reports/error_analysis.csv`). Valor real: **1**, Valor predicho del modelo: **3**.
- **Texto de la reseña:** La paciente relata una experiencia insoportable de apenas tres días con el medicamento *Contrave*, describiendo náuseas inmanejables, pérdida total de energía, incapacidad para entrenar y un abandono drástico del tratamiento.
- **Motivo del error del modelo:** El modelo predijo un 3 en lugar de la calificación mínima absoluta (1) debido a la presencia de una cláusula concesiva al inicio del texto que reconoce la efectividad general del fármaco para otros (*«I'm sure it works for some»*).
- **Limitación detectada:** El clasificador se desvía y sobreestima levemente la nota al procesar un reconocimiento neutral o positivo condicional hacia terceros (*«funciona para algunos»*), ignorando que la experiencia personal de la usuaria fue un fracaso absoluto e incapacitante que ameritaba un 1 neto.

# Análisis del Caso 18 (Error por Contraste entre Beneficio Clínico y Sufrimiento Físico)

- **Caso analizado:** Fila 19 del archivo de errores (`reports/error_analysis.csv`). Valor real: **5**, Valor predicho del modelo: **2**.
- **Texto de la reseña:** La paciente detalla efectos secundarios terroríficos y extremos con un parche de clonidina (mareos severos, estreñimiento, diarrea e inflamación abdominal) que la obligaron a suspenderlo a los 6 días, con secuelas de meses, aunque reconoce al final que su presión arterial sí bajó.
- **Motivo del error del modelo:** El modelo predijo un 2 (muy negativo) porque el texto está dominado masivamente por una lista espantosa de efectos adversos incapacitantes.
- **Limitación detectada:** El clasificador lineal colapsa la predicción hacia el fondo de la escala por la alta densidad de términos de toxicidad física severa, volviéndose completamente ciego ante la cláusula final de éxito médico (*«My blood pressure did go down»*), lo que genera una disparidad con el balance neutral de 5 otorgado por la paciente.

# Análisis del Caso 19 (Error por Sobredensidad de Negación Absoluta)

- **Caso analizado:** Fila 20 del archivo de errores (`reports/error_analysis.csv`). Valor real: **5**, Valor predicho del modelo: **2**.
- **Texto de la reseña:** Un usuario sigue una recomendación de una tienda naturista para consumir raíz de remolacha contra la hipertensión, reportando un resultado clínico neutro/exitoso donde su presión arterial se normaliza y añade de forma categórica que *"no tiene efectos secundarios"*.
- **Motivo del error del modelo:** El modelo predijo erróneamente un 2 a pesar de ser una reseña favorable sin efectos secundarios.
- **Limitación detectada:** Este es un fallo crítico del modelo debido a la presencia de la frase de negación *"having no side effects"*. Para un clasificador lineal ingenuo, la combinación de la partícula de negación (*"no"*) junto con palabras de problemas médicos (*"side effects"*) confunde al vectorizador, haciendo que el algoritmo interprete la frase como la presencia de efectos adversos graves en lugar de su ausencia total.

# Análisis del Caso 20 (Error por Éxito Terapéutico Sobresaliente)

- **Caso analizado:** Fila 21 del archivo de errores (`reports/error_analysis.csv`). Valor real: **10**, Valor predicho del modelo: **9**.
- **Texto de la reseña:** Reseña sumamente entusiasta de un paciente joven que sufría de acné severo durante 7 años y que, tras el uso de doxiciclina y un cambio de rutina, logró una piel completamente lisa, limpia y perfecta en pocas semanas, cerrando con una expresión de optimismo (*«Fingers crossed it stays away :)»*).
- **Motivo del error del modelo:** El modelo predijo un 9 y el valor real fue 10, representando una aproximación excelente y de muy baja desviación.
- **Limitación detectada:** Al tratarse de un texto con un vocabulario de polaridad abrumadoramente positiva (*«super smooth and clear»*, *"looks great"*), el modelo procesa la señal de éxito de manera limpia y directa, acercándose casi a la perfección, con una mínima variación atribuida solo a la cautela expresada en la frase de cierre con los dedos cruzados.



# Conclusión General del Análisis de Errores (Lab 05)

Tras la revisión exhaustiva de los 20 casos de error del modelo de Regresión Logística con representaciones TF-IDF, se puede formular y sostener la siguiente hipótesis de conclusión sobre el comportamiento del clasificador:

- **Polarización por léxico extremo:** El modelo presenta una marcada tendencia a permitir que su calificación se vea arrastrada y polarizada por términos de vocabulario altamente positivos o negativos. Ante reseñas que expresan balances mixtos, el clasificador tiende a sesgarse drásticamente hacia los extremos de la escala en lugar de reflejar un punto de equilibrio intermedio.
- **Literalidad algorítmica y ceguera pragmática:** El enfoque lineal carece de la capacidad para procesar matices complejos del lenguaje humano, interpretando de forma estrictamente literal el contenido. Esto se evidencia en su incapacidad para detectar ironías, sarcasmos mordaces, metáforas o dobles sentidos (como evaluar de forma positiva textos donde se critica el producto de forma cínica).
- **Incapacidad de procesamiento contextual avanzado:** El modelo muestra limitaciones severas ante construcciones condicionales, referencias temporales (contrastes entre estados pasados y actuales), negaciones complejas ("sin efectos secundarios") y la ponderación real entre efectos secundarios físicos severos y el éxito terapéutico final.