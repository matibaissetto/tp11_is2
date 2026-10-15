
# TP11 - Gestión de Calidad
## Ingeniería de Software II

---

## Consigna 1 - Requerimientos

### Requerimientos funcionales (R)

- **R1:** El programa debe solicitar un número por teclado.
- **R2:** El programa debe validar que el número ingresado sea un entero positivo entre 1 y 1999.
- **R3:** Si el número es par, debe dividirlo entre 2.
- **R4:** Si el número es impar, debe multiplicarlo por 3 y sumarle 1.
- **R5:** Debe repetir las operaciones hasta alcanzar el valor 1.
- **R6:** Debe contabilizar las iteraciones realizadas.
- **R7:** Debe mostrar el número inicial y la cantidad de iteraciones necesarias para alcanzar 1.

### Requerimientos no funcionales (F)

Los siguientes requerimientos son criterios adicionales propuestos para el ejercicio, no exigencias explícitas del enunciado de Collatz.

- **F1:** El programa debe implementarse en lenguaje Python.
- **F2:** El código debe ser legible y facilitar su mantenimiento.
- **F3:** El programa debe ejecutarse mediante una interfaz de consola.

---

## Consigna 2 - Casos de prueba

Se definieron inicialmente 13 casos de prueba, identificados como T1 a T13.

Posteriormente, durante la inspección de los casos de prueba, se agregaron T14 y T15.

### Casos de prueba definidos

| Test | Entrada | Resultado esperado | Tipo |
|---|---|---|---|
| T1 | 1 | 0 iteraciones | Unitario |
| T2 | 2 | 1 iteración | Unitario |
| T3 | 3 | 7 iteraciones | Unitario |
| T4 | 4 | 2 iteraciones | Unitario |
| T5 | 6 | 8 iteraciones | Unitario |
| T6 | 20 | 7 iteraciones | Unitario |
| T7 | 0 | Rechazar entrada | Funcional |
| T8 | -5 | Rechazar entrada | Funcional |
| T9 | 2000 | Rechazar entrada | Funcional |
| T10 | 1999 | Aceptar y mostrar 50 iteraciones | Funcional |
| T11 | 3.5 | Rechazar entrada | Funcional |
| T12 | abc | Rechazar entrada | Funcional |
| T13 | 10 | Mostrar número inicial y 6 iteraciones | Funcional |
| T14 | 1 | Aceptar y mostrar 0 iteraciones | Funcional |
| T15 | 1998 | Aceptar y mostrar 50 iteraciones | Funcional |

### Clasificación de los casos

**Pruebas unitarias (caja blanca):**

T1, T2, T3, T4, T5 y T6.

Verifican directamente el comportamiento de la función `collatz()` y los resultados de las operaciones matemáticas.

**Pruebas funcionales (caja negra):**

T7, T8, T9, T10, T11, T12, T13, T14 y T15.

Verifican el comportamiento del programa desde la entrada por teclado hasta la presentación de los resultados.

---

## Consigna 3 - Matriz de trazabilidad (RTMX)

La matriz de trazabilidad permite relacionar los requerimientos con los casos de prueba y verificar su cobertura.

### Matriz RTMX actualizada

| Requerimiento | Casos de prueba asociados |
|---|---|
| R1 - Solicitar número | T7, T8, T9, T10, T11, T12, T13, T14, T15 |
| R2 - Validar entrada | T7, T8, T9, T10, T11, T12, T14, T15 |
| R3 - Operación par | T2, T4, T5, T6 |
| R4 - Operación impar | T3, T5, T6 |
| R5 - Alcanzar el valor 1 | T1, T2, T3, T4, T5, T6, T13, T14, T15 |
| R6 - Contar iteraciones | T1, T2, T3, T4, T5, T6, T10, T13, T14, T15 |
| R7 - Mostrar resultados | T10, T13, T14, T15 |
| F1 - Lenguaje Python | Verificación V1 |
| F2 - Legibilidad | Inspección V2 |
| F3 - Interfaz de consola | T7, T8, T9, T10, T11, T12, T13, T14, T15 |

### Validación de integridad

Se verificaron las siguientes condiciones:

- Todos los requerimientos funcionales están asociados a uno o más casos de prueba.
- Todos los casos T1 a T15 están asociados al menos a un requerimiento.
- Los requerimientos no funcionales cuentan con verificaciones específicas.
- Todos los casos de prueba definidos fueron ejecutados exitosamente al menos una vez.

**Resultado:** La matriz presenta cobertura completa de los requerimientos identificados, considerando las verificaciones complementarias V1 y V2.

---

## Consigna 4 - Inspección estática del código

### Sesión de inspección 1

**Método:** Revisión estática del código original sin ejecutar el programa.

El objetivo fue identificar defectos sintácticos, semánticos y funcionales presentes en la implementación inicial.

### Defectos detectados

| ID | Defecto detectado | Clasificación |
|---|---|---|
| D1 | La función devuelve `iter` en lugar de `iteraciones`. | Semántico |
| D2 | Se utiliza la variable `j` sin haber sido definida. | Semántico |
| D3 | El valor inicial está fijado en 20 y no se solicita por teclado. | Funcional |
| D4 | No existe validación ni manejo de entradas fuera del rango permitido o de tipos inválidos. | Funcional |

### Evaluación de la tasa de comentarios

El enunciado establece que una tasa de comentarios mayor a 12 debe considerarse un defecto.

El programa original presenta 2 líneas de comentarios y el enunciado establece un tamaño de 18 LOC.

Tasa de comentarios:

(2 / 18) × 100 = 11,11%

Como 11,11% es inferior a 12%, no corresponde registrar un defecto por exceso de comentarios.

Esta comprobación utiliza las 18 LOC indicadas por la consigna.

### Resultados de la inspección 1

- Técnica: Inspección estática.
- Código ejecutado: No.
- Defectos únicos identificados: 4.
- Defectos corregidos durante la sesión: 0.
- Estado: Inspección finalizada.

Las correcciones se realizaron posteriormente, respetando las sesiones de prueba solicitadas.

---

## Consigna 5 - Inspección de casos de prueba

### Sesión de inspección 2

**Método:** Revisión estática de los casos de prueba, sin ejecutar el programa.

Se revisaron los 13 casos de prueba definidos inicialmente con el objetivo de identificar omisiones y mejorar su cobertura.

### Defectos de diseño de pruebas detectados

| ID | Defecto | Corrección propuesta |
|---|---|---|
| D6 | No se verificaba explícitamente la aceptación del límite inferior desde la interfaz. | Agregar T14 |
| D7 | No se verificaba el valor inmediatamente inferior al máximo. | Agregar T15 |
| D8 | T10 no especificaba el número exacto de iteraciones esperadas. | Completar resultado esperado |

### Nuevos casos incorporados

| Caso | Entrada | Resultado esperado | Tipo |
|---|---|---|---|
| T14 | 1 | Aceptar y mostrar 0 iteraciones | Funcional |
| T15 | 1998 | Aceptar y mostrar 50 iteraciones | Funcional |

### Actualización de la matriz RTMX

Se incorporaron T14 y T15 a los requerimientos correspondientes.

La matriz presentada en la consigna 3 refleja esta actualización.

### Resultados de la inspección 2

- Casos iniciales: 13.
- Casos nuevos: 2.
- Total de casos definidos: 15.
- Defectos de diseño de pruebas identificados: 3.
- Estado: Inspección finalizada.

Estos defectos corresponden al diseño de las pruebas y no se contabilizan como defectos únicos de implementación del programa.

---

## Consigna 6 - Ejecución de pruebas unitarias

Las pruebas unitarias se desarrollaron utilizando:

- Lenguaje: Python 3.14.3.
- Herramienta: Pytest 9.1.1.
- Archivo: `test_collatz.py`.

Se realizaron cuatro sesiones de ejecución.

### Sesión S1

**Resultado:** Error durante la recolección de pruebas.

- Casos previstos: T1 a T6.
- Casos ejecutados: 0.
- Fallas observadas: 1.
- Defectos únicos nuevos: 1.

**Defecto D9:**

Se detectó un error sintáctico en `collatz.py`, línea 14.

La instrucción `print()` no tenía cerrado correctamente uno de sus paréntesis.

Error obtenido:

`SyntaxError: '(' was never closed`

**Corrección realizada:**

Se agregó el paréntesis faltante.

**Estado:** Sesión finalizada con error.

### Sesión S2

**Resultado:** Error durante la recolección de pruebas.

- Casos previstos: T1 a T6.
- Casos ejecutados: 0.
- Fallas observadas: 1.
- Defectos únicos nuevos: 0.

**Defecto observado:** D2.

El programa intentaba utilizar la variable `j`, que no había sido definida.

Error obtenido:

`NameError: name 'j' is not defined`

**Corrección realizada:**

Se reemplazó `collatz(j)` por `collatz(i)`.

Este defecto ya había sido identificado durante la inspección estática.

**Estado:** Sesión finalizada con error.

### Sesión S3

**Resultado:** Error durante la recolección de pruebas.

- Casos previstos: T1 a T6.
- Casos ejecutados: 0.
- Fallas observadas: 1.
- Defectos únicos nuevos: 0.

**Defecto observado:** D1.

La función devolvía `iter`, correspondiente a una función incorporada de Python, en lugar de devolver la variable `iteraciones`.

Error obtenido:

`TypeError: %d format: a real number is required`

**Corrección realizada:**

Se reemplazó `return iter` por `return iteraciones`.

**Estado:** Sesión finalizada con error.

### Sesión S4

**Resultado:** Pruebas exitosas.

- Casos ejecutados: T1 a T6.
- Casos exitosos: 6.
- Casos fallidos: 0.
- Fallas observadas: 0.

Resultado de Pytest:

`6 passed in 0.23s`

Se alcanzó el 100% de éxito en los casos unitarios definidos.

### Resumen de sesiones unitarias

| Sesión | Casos ejecutados | Exitosos | Fallas observadas |
|---|---|---|---|
| S1 | 0 | 0 | 1 |
| S2 | 0 | 0 | 1 |
| S3 | 0 | 0 | 1 |
| S4 | 6 | 6 | 0 |

**Total de sesiones unitarias:** 4.

Todos los casos unitarios fueron ejecutados exitosamente al menos una vez.

### Verificación posterior

Después de modificar el programa para las pruebas funcionales, se ejecutaron nuevamente los casos unitarios.

Resultado:

`6 passed in 0.04s`

Esto permitió comprobar que los cambios realizados no alteraron los resultados de los seis casos unitarios existentes.

---

## Consigna 7 - Ejecución de pruebas funcionales

Las pruebas funcionales verificaron el comportamiento del programa desde el ingreso de datos hasta la presentación de resultados.

Se utilizaron:

- Archivo: `test_funcional.py`.
- Herramienta: Pytest.
- Ejecución del programa mediante `subprocess`.

### Sesión S5

**Resultado:** 8 pruebas fallidas.

- Escenarios ejecutados: 8.
- Exitosos: 0.
- Fallidos: 8.
- Fallas observadas: 8.
- Defectos únicos nuevos de implementación: 0.

### Defectos manifestados

**D3:** El programa utilizaba un valor fijo de 20 en lugar de solicitar el número por teclado.

**D4:** No existía validación de las entradas.

Los defectos ya habían sido identificados durante la inspección inicial.

Las ocho pruebas fallidas no equivalen a ocho defectos únicos.

### Correcciones realizadas después de S5

Se modificó el programa para incorporar:

- Lectura del número mediante `input()`.
- Conversión del número ingresado mediante `int()`.
- Validación del rango de 1 a 1999.
- Manejo de entradas inválidas con `try-except`.
- Presentación del número original y las iteraciones.
- Separación de la función `collatz()` y la función `main()`.
- Control de ejecución mediante `if __name__ == "__main__"`.

### Sesión S6

**Resultado:** Pruebas exitosas.

- Escenarios ejecutados: 8.
- Exitosos: 8.
- Fallidos: 0.
- Fallas observadas: 0.

Resultado de Pytest:

`8 passed in 1.29s`

Se alcanzó el 100% de éxito en los ocho escenarios funcionales implementados hasta ese momento.

### Sesión S7

Se agregaron verificaciones explícitas para los valores 1998 y 1999.

**Resultado:**

- Escenarios ejecutados: 10.
- Exitosos: 9.
- Fallidos: 1.
- Fallas observadas: 1.

### Defecto detectado en S7

El caso de prueba T10 contenía un resultado esperado incorrecto.

Inicialmente se esperaba que el número 1999 necesitara 51 iteraciones.

El programa devolvió 50 iteraciones, que es el resultado correcto.

**Clasificación:** Defecto del caso de prueba, no de la implementación.

Este error se manifestó después de que T10 había sido completado durante la preparación de las pruebas.

**Corrección realizada:**

Se actualizó el resultado esperado de T10 de 51 a 50 iteraciones.

No fue necesario modificar `collatz.py`.

### Sesión S8

**Resultado:** Pruebas exitosas.

- Escenarios ejecutados: 10.
- Exitosos: 10.
- Fallidos: 0.
- Fallas observadas: 0.

Resultado de Pytest:

`10 passed in 1.99s`

Se alcanzó el 100% de éxito en los escenarios funcionales implementados.

### Resumen de sesiones funcionales

| Sesión | Ejecutados | Exitosos | Fallidos |
|---|---|---|---|
| S5 | 8 | 0 | 8 |
| S6 | 8 | 8 | 0 |
| S7 | 10 | 9 | 1 |
| S8 | 10 | 10 | 0 |

**Total de sesiones funcionales:** 4.

---

## Consigna 8 - Consolidación de resultados

### Correspondencia de casos automatizados

| Caso | Prueba automatizada |
|---|---|
| T1 | test_t1 |
| T2 | test_t2 |
| T3 | test_t3 |
| T4 | test_t4 |
| T5 | test_t5 |
| T6 | test_t6 |
| T7 | test_entradas_invalidas[0] |
| T8 | test_entradas_invalidas[-5] |
| T9 | test_entradas_invalidas[2000] |
| T10 | test_t10_limite_superior |
| T11 | test_entradas_invalidas[3.5] |
| T12 | test_entradas_invalidas[abc] |
| T13 | test_resultados[10-6] |
| T14 | test_resultados[1-0] |
| T15 | test_t15_valor_1998 |

### Prueba funcional adicional

`test_entrada_por_teclado`

Verifica que el programa acepta el valor 1999 y lo incluye en la salida.

### Verificación de integridad

Se comprobó que:

- Los 15 casos de prueba definidos fueron ejecutados.
- Todos los casos fueron exitosos al menos una vez.
- Los seis casos unitarios finalizaron exitosamente.
- Los diez escenarios funcionales automatizados finalizaron exitosamente.
- Todos los requerimientos funcionales están relacionados con pruebas.
- Los requerimientos no funcionales propuestos cuentan con verificaciones específicas.

### Verificación de requerimientos no funcionales

| ID | Verificación realizada | Resultado |
|---|---|---|
| F1 - V1 | Se comprobó que `collatz.py` está implementado en Python. | Cumple |
| F2 - V2 | Se inspeccionó la legibilidad del código, verificando nombres descriptivos y separación de funciones. | Cumple |
| F3 | Se comprobó la ejecución mediante consola utilizando las pruebas funcionales. | Cumple |

F1 y F2 corresponden a criterios de calidad propuestos para el ejercicio.

La legibilidad fue evaluada cualitativamente, dado que no se definió una métrica cuantitativa.

### Registro general de sesiones

| Fase | Sesión | Defectos detectados o fallas observadas |
|---|---|---|
| Inspección de código | Inspección 1 | 4 defectos únicos |
| Inspección de pruebas | Inspección 2 | 3 defectos de diseño de pruebas |
| Pruebas unitarias | S1 | 1 error de recolección |
| Pruebas unitarias | S2 | 1 error de recolección |
| Pruebas unitarias | S3 | 1 error de recolección |
| Pruebas unitarias | S4 | 0 fallas |
| Pruebas funcionales | S5 | 8 pruebas fallidas |
| Pruebas funcionales | S6 | 0 fallas |
| Pruebas funcionales | S7 | 1 prueba fallida |
| Pruebas funcionales | S8 | 0 fallas |

### Resumen general

- Sesiones de inspección: 2.
- Sesiones unitarias: 4.
- Sesiones funcionales: 4.
- Total de sesiones registradas: 10.
- Defectos únicos de implementación identificados: 5.
- Defectos de diseño de pruebas detectados en inspección: 3.
- Defecto adicional de prueba observado en S7: 1.
- Pruebas unitarias exitosas en última ejecución: 6.
- Pruebas funcionales exitosas en última ejecución: 10.
- Total de escenarios automatizados exitosos: 16.

### Consideraciones sobre el conteo de defectos

Es importante distinguir tres conceptos:

**Defecto:** Problema existente en el código o en otro artefacto del proceso.

**Falla:** Comportamiento incorrecto observado durante la ejecución de una prueba.

**Defecto único:** Problema individual que se contabiliza una sola vez, aunque provoque varias fallas o se observe en distintas sesiones.

Por lo tanto:

- Las fallas repetidas no se suman como defectos únicos nuevos.
- Los defectos encontrados durante inspecciones no se vuelven a contabilizar cuando se manifiestan durante la ejecución.
- Los defectos del diseño de pruebas se mantienen diferenciados de los defectos del programa.

Para las métricas del programa Collatz se consideran los cinco defectos únicos de implementación identificados.

---

## Consigna 9 - Cálculo del PCE por fase

### Definición

El PCE (Phase Containment Effectiveness) permite evaluar la efectividad de una fase para identificar defectos.

Para este ejercicio, el profesor establece que el 100% corresponde al total de defectos observados.

Se adopta como criterio contabilizar los defectos únicos de implementación según la fase en la que fueron identificados por primera vez.

### Fórmula

PCE = (Defectos únicos detectados en la fase / Total de defectos únicos) × 100

### Inventario de defectos únicos de implementación

| Defecto | Descripción | Fase de primera detección |
|---|---|---|
| D1 | Retorno incorrecto de la función | Inspección |
| D2 | Variable `j` no definida | Inspección |
| D3 | Entrada fija en lugar de teclado | Inspección |
| D4 | Falta de validación de entradas | Inspección |
| D9 | Paréntesis faltante | Pruebas unitarias |

**Total de defectos únicos:** 5.

### Cálculo por fase

**Fase 1 - Inspección**

Defectos únicos detectados: 4.

PCE = (4 / 5) × 100

PCE = 80%

**Fase 2 - Pruebas unitarias**

Defectos únicos nuevos detectados: 1.

PCE = (1 / 5) × 100

PCE = 20%

**Fase 3 - Pruebas funcionales**

Defectos únicos nuevos detectados: 0.

PCE = (0 / 5) × 100

PCE = 0%

### Resultados por fase

| Fase | Defectos únicos detectados | Porcentaje del total |
|---|---|---|
| Inspección del código | 4 | 80% |
| Pruebas unitarias | 1 | 20% |
| Pruebas funcionales | 0 | 0% |
| Total | 5 | 100% |

### PCE acumulado

| Fase finalizada | Defectos acumulados | Porcentaje acumulado |
|---|---|---|
| Inspección del código | 4 | 80% |
| Pruebas unitarias | 5 | 100% |
| Pruebas funcionales | 5 | 100% |

### Interpretación de los resultados

La inspección estática permitió identificar el 80% de los defectos únicos de implementación observados.

Durante las pruebas unitarias se identificó el 20% restante.

Las pruebas funcionales manifestaron defectos previamente identificados, por lo que no aportaron nuevos defectos únicos.

Esto no significa que las pruebas funcionales fueran innecesarias, ya que permitieron comprobar el correcto funcionamiento del programa completo después de las correcciones.

### Consideración metodológica

Los porcentajes anteriores representan la distribución de defectos únicos descubiertos por primera vez en cada fase.

Se utiliza este criterio para evitar duplicaciones y cumplir con el total observado del ejercicio.

No se incluyen defectos de diseño de los casos de prueba, que fueron registrados por separado.

El 100% obtenido representa el total de defectos observados, no una garantía de ausencia absoluta de defectos latentes.

---

## Consigna 10 - Densidad de defectos

### Definición

La densidad de defectos es una métrica de calidad que relaciona la cantidad de defectos únicos identificados con el tamaño del software.

Permite comparar la calidad relativa de programas o módulos de diferentes tamaños.

### Fórmula

δ0 = μ0 / S

Donde:

- δ0 = Densidad de defectos inicial.
- μ0 = Cantidad de defectos únicos considerados.
- S = Tamaño del software en líneas de código.

### Datos del ejercicio

El enunciado establece:

S = 18 LOC.

De las inspecciones y pruebas realizadas se obtuvo:

μ0 = 5 defectos únicos de implementación identificados.

### Cálculo

δ0 = 5 / 18

δ0 = 0,2778 defectos/LOC.

Para expresar el resultado por cada 1000 líneas:

0,2778 × 1000 = 277,78 defectos/KLOC.

### Resultado

**Densidad observada del programa original:**

0,2778 defectos por línea de código.

Equivalente a:

277,78 defectos por cada 1000 líneas de código.

### Interpretación

La densidad calculada representa la cantidad de defectos únicos identificados durante el proceso de inspección y pruebas respecto del tamaño original del programa.

Se considera una densidad elevada debido a la cantidad de defectos encontrados en una implementación de solamente 18 LOC.

No obstante, debe tenerse en cuenta que se trata de un programa pequeño, preparado para realizar un ejercicio académico de detección y corrección de defectos.

### Consideración sobre los defectos latentes

La densidad calculada utiliza únicamente defectos identificados.

El número total real de defectos del programa podría ser diferente, ya que pueden existir defectos latentes no detectados.

En una consigna posterior se utilizará un modelo estadístico de regresión para estimar el total de defectos esperados y los posibles defectos remanentes.

---

## Consigna 11 - Kanban y parámetro TEP

### Definición

Según el tutorial "Kanban para uso genérico" de
Álvaro Ruiz de Mendarozqueta, el parámetro TEP
significa Trabajo en Progreso (Work in Progress,
WIP).

Representa la cantidad de tareas que se encuentran
en ejecución simultáneamente dentro del proceso.

### Significado crítico

La importancia del TEP radica en establecer un
límite a la cantidad de tareas que pueden estar
en desarrollo al mismo tiempo.

Limitar el trabajo en progreso permite:

- Evitar la acumulación excesiva de tareas.
- Reducir la multitarea.
- Identificar posibles cuellos de botella.
- Mejorar el flujo de trabajo.
- Mantener un ritmo de producción sostenible.
- Reducir los tiempos de entrega.

Por ejemplo, si se establece TEP = 2, solamente
pueden mantenerse dos tareas en progreso a la vez.
Para comenzar una nueva, debe liberarse capacidad
terminando alguna de las anteriores.

### Relación con la ley de Little

Plazo de ejecución = Trabajo en progreso / Rendimiento

Esta relación permite comprender que, si aumenta
el trabajo en progreso mientras el rendimiento
permanece constante, también aumenta el plazo
de ejecución de las tareas.

### Conclusión

El TEP es un parámetro fundamental en Kanban porque
permite controlar la cantidad de trabajo simultáneo
y favorecer un flujo continuo de tareas terminadas.

Su correcta utilización ayuda a mejorar la eficiencia
del equipo, evitando iniciar más actividades de las
que se pueden completar adecuadamente.

Fuente: Álvaro Ruiz de Mendarozqueta,
"Kanban para uso genérico", versión 1.1, marzo de 2015.

---

## Consigna 12 - Proyección de defectos con regresión

### Datos proporcionados por la cátedra

Se utilizó un modelo aproximado de crecimiento de detección de defectos, tomando como referencia el taller `Taller_Defectos.ipynb` y la implementación `regresion_defectos.py`.

| Día | Defectos detectados | Acumulado |
|---|---:|---:|
| 0 | 9 | 9 |
| 1 | 18 | 27 |
| 2 | 5 | 32 |
| 3 | 7 | 39 |
| 4 | 23 | 62 |
| 5 | 2 | 64 |
| 6 | 8 | 72 |

### Modelo y resultados

Se trabajó con una curva exponencial de detección, del tipo:

\[
\mu(t) = \mu_0(1-e^{-\lambda_0t})
\]

donde `μ(t)` representa los defectos acumulados detectados hasta el tiempo `t`, `μ0` representa el total asintótico estimado y `λ0` representa un parámetro de velocidad del modelo. La implementación utilizó una aproximación mediante regresión sobre los datos.

La ejecución local de `regresion_defectos.py` produjo:

| Indicador | Resultado |
|---|---:|
| Defectos observados | 72 |
| Tasa inicial reportada (`λ0`) | 11,29 |
| Defectos totales estimados (`μ0`) | 98,12 |
| Defectos remanentes estimados | 26,12 |
| Coeficiente `R²` | 0,0939 |

**Interpretación:** el modelo proyecta aproximadamente **98,12 defectos totales** y **26,12 remanentes** respecto de los 72 observados. Sin embargo, un `R²` de 0,0939 indica un **ajuste muy débil**. La proyección debe considerarse ilustrativa y no una estimación suficientemente fiable para decidir una liberación de software.

Los defectos diarios no presentan una disminución ordenada: el día 4 tiene 23 defectos, por encima de los días anteriores. Esa irregularidad contribuye a la baja capacidad explicativa del ajuste.

---

## Consigna 13 - Regresión sobre las sesiones de Collatz y defectos remanentes

### Datos obtenidos en la práctica

Se consideran únicamente los **cinco defectos únicos de implementación**, contabilizados en su fase de primera detección:

| Etapa o sesión | Nuevos defectos únicos |
|---|---:|
| Inspección estática inicial | 4 |
| Primera sesión de pruebas unitarias (S1) | 1 |
| Sesiones posteriores de pruebas unitarias | 0 |
| Sesiones de pruebas funcionales | 0 |
| **Total observado** | **5** |

Esta distribución no debe confundirse con la cantidad de **fallas** por ejecución: por ejemplo, S5 registró ocho pruebas fallidas, pero no ocho defectos únicos nuevos.

### Posibilidad de estimación estadística

El conjunto de datos tiene **muy pocas observaciones positivas**, está dominado por ceros y corresponde a una aplicación educativa extremadamente pequeña. En estas condiciones no resulta defendible extrapolar una curva exponencial confiable para obtener `μ0` en Collatz.

Por lo tanto:

- Defectos únicos observados: **5**.
- Defectos únicos observados que quedaron sin corregir al finalizar las pruebas: **0**, según los casos ejecutados.
- **`μ0` estadístico:** no se dispone de una estimación fiable con esta muestra.
- **`μr = μ0 - Σμi`:** no puede calcularse un valor estadístico fiable sin un `μ0` defendible.

Si se utiliza **solo como supuesto ilustrativo** que `μ0 = 5`, entonces `μr = 5 - 5 = 0`. Esto **no prueba** que no existan defectos latentes.

### Tamaño final del código

El tamaño final registrado de `collatz.py` fue **37 LOC**, frente a las 18 LOC originales proporcionadas en la consigna.

Comando equivalente en PowerShell:

```powershell
(Get-Content collatz.py | Measure-Object -Line).Lines
```

El crecimiento refleja principalmente la incorporación de entrada por teclado, validaciones, manejo de errores y separación de responsabilidades.

---

## Consigna 14 - Relación entre PCE y duración óptima de las pruebas para otorgar garantía

El modelo de garantía relaciona el costo de ejecutar actividades de verificación y validación (V&V) con el costo futuro de atender defectos que llegan al producto liberado.

Si aumenta el **PCE** del proceso, se contienen más defectos antes de la liberación y disminuye la cantidad esperada de defectos que deberá cubrir la garantía.

En igualdad de condiciones de costo, productividad y riesgo, un PCE mayor tiende a **reducir el tiempo óptimo de prueba** necesario para alcanzar un nivel de riesgo y costo aceptable. Esto ocurre porque una detección más eficaz permite lograr el mismo objetivo de calidad con menos esfuerzo adicional de búsqueda de defectos.

Esta conclusión es **cualitativa**. El tiempo óptimo no depende únicamente del PCE: también intervienen el costo de las pruebas, la gravedad de los defectos, los costos de reparación y las obligaciones de garantía. No significa que mejorar el PCE justifique eliminar las pruebas finales.

---

## Consigna 15 - Cálculo de defectos a partir de la línea de base organizacional

### Datos del enunciado

- Efectividad de contención del proceso: `PCE = 89% = 0,89`.
- Densidad residual al liberar: `δr = 0,12 defectos/FP`.
- Tamaño del producto: `S = 100 FP`.

### a) Defectos totales esperados (`μ0`)

Primero se calculan los defectos esperados al liberar:

\[
\mu_r = \delta_r S = 0,12 \times 100 = 12
\]

Como la fracción no contenida es `1 - PCE = 0,11`:

\[
\mu_0 = \frac{\mu_r}{1-PCE}
       = \frac{12}{0,11}
       \approx 109,09
\]

**Resultado:** alrededor de **109 defectos totales esperados** según la línea de base organizacional.

### b) Densidad al finalizar la construcción (`δ0`)

\[
\delta_0 = \frac{\mu_0}{S}
         = \frac{109,09}{100}
         \approx 1,0909\ \text{defectos/FP}
\]

**Resultado:** **1,0909 defectos/FP**.

### c) Defectos a detectar durante V&V

\[
\mu_{\mathrm{V\&V}} = \mu_0-\mu_r
                   = 109,09 - 12
                   = 97,09
\]

**Resultado:** se deberían planificar aproximadamente **97 defectos detectados durante V&V** para mantener la performance histórica.

### d) Interpretación de 60 defectos encontrados en los tres primeros días

Se detectaron `20 × 3 = 60` defectos durante los primeros tres días de V&V.

En términos del objetivo de detección histórico:

\[
\frac{60}{97,09}\times 100 \approx 61,8\%
\]

Es decir, en tres días ya se detectó cerca del **61,8%** de los defectos que históricamente se esperaba encontrar durante todo V&V.

Esto puede interpretarse de al menos dos maneras:

1. El proceso de prueba está detectando defectos con gran rapidez y concentra una proporción importante de los hallazgos al principio.
2. El producto tiene una cantidad inicial de defectos mayor que la esperada, de modo que el número total podría superar la línea de base.

**No alcanza la información para afirmar cuál explicación es la correcta.** Debe observarse la tendencia en los días siguientes, el esfuerzo de prueba empleado y la severidad de los hallazgos. Si la tasa de 20 defectos diarios continuara durante demasiado tiempo, aumentaría la sospecha de que el total supera lo históricamente esperable.

---

## Consigna 16 - Conversor JSON a CSV mediante filtro

### Objetivo y diseño

Se implementó `json2csv`, una herramienta Python de línea de comandos que transforma una **lista JSON de objetos** en contenido CSV.

Opciones admitidas:

| Opción | Función |
|---|---|
| `-i`, `--input` | Archivo JSON de entrada |
| `-o`, `--output` | Archivo CSV de salida |
| `-d`, `--delimiter` | Delimitador CSV; por defecto `,` |

Al omitir `-i` se utiliza `stdin`; al omitir `-o` se utiliza `stdout`. Esto permite utilizarlo como **filtro** de una tubería de comandos.

El proyecto se estructuró con **Cookiecutter** y se ejecuta como módulo instalado:

```powershell
cd json2csv
python -m pip install -e .
python -m json2csv -i ejemplo.json -o resultado.csv
python -m json2csv -i ejemplo.json -o resultado_pyc.csv -d ";"
Get-Content ejemplo.json -Raw | python -m json2csv
```

**Precisión respecto de la consigna:** el enunciado propone `python json2csv.py ...`; la implementación comprobada utiliza `python -m json2csv ...`, con las mismas opciones y comportamiento de entrada/salida. Si se exige literalmente el nombre del archivo invocado, queda pendiente agregar y comprobar un lanzador `json2csv.py`.

### Tratamiento de entradas

Se comprobaron las siguientes condiciones:

- JSON válido con varios registros.
- Columnas diferentes entre los objetos.
- Delimitador personalizado.
- Entrada y salida por archivos.
- Entrada y salida estándar.
- Archivo inexistente.
- JSON sintácticamente inválido.
- Delimitador inválido de longitud mayor a un carácter.

El conversor utiliza mensajes de error controlados y un código de salida distinto de cero para los errores contemplados. El terminador de filas se configuró explícitamente como `\n` para evitar líneas vacías adicionales en Windows.

---

## Consigna 17 - Garantía de calidad del conversor e integración continua

### Entorno y estructura

El desarrollo se realizó dentro de un entorno virtual de Python en Windows, con el paquete alojado en `json2csv/` y su implementación principal en `src/json2csv/`.

Se incorporaron los siguientes artefactos:

| Archivo o elemento | Función |
|---|---|
| `pyproject.toml` | Metadatos, versión `0.1.0`, dependencias y configuración |
| `requirements.txt` | Instalación del paquete y herramientas de desarrollo |
| `README.md` | Instalación, uso y comandos de comprobación |
| `CHANGELOG.md` | Registro de cambios de la versión `0.1.0` |
| `CONTEXT.md` | Registro general de asistencia mediante IA |
| `LICENSE` | Archivo de licencia MIT generado por la plantilla |
| `VERSION` | Identificador `0.1.0` |
| `BUILD` | Identificador `1` |
| `tests/test_json2csv.py` | Pruebas automatizadas |
| `.github/workflows/calidad.yml` | Configuración del control automático en GitHub |

### Pruebas y cobertura

Comando utilizado:

```powershell
python -m pytest tests/test_json2csv.py --cov=json2csv --cov-report=term-missing
```

Resultado observado en el entorno local:

- **13 pruebas aprobadas de 13 ejecutadas.**
- **88,33% de cobertura total**, incluyendo cobertura de ramas según configuración.
- Límite mínimo establecido en `pyproject.toml`: **85%**.
- La herramienta informó expresamente: `Required test coverage of 85.0% reached`.

### Controles de calidad y seguridad

| Herramienta | Resultado de la revisión local |
|---|---|
| Ruff | `All checks passed!` |
| Black | `5 files would be left unchanged` |
| MyPy | Sin errores en 4 archivos fuente |
| Pyright | 0 errores, 0 advertencias |
| Bandit | `No issues identified` |

Comandos principales:

```powershell
python -m ruff check src tests
python -m black --check src tests
python -m mypy src/json2csv
python -m pyright src/json2csv
python -m bandit -r src/json2csv
```

**PEP 8:** comprobado parcialmente mediante Ruff y Black. **PEP 257:** aunque existen docstrings, no se aportó una ejecución específica de un conjunto completo de reglas PEP 257; este control debe verificarse por separado antes de declararlo cumplido de forma exhaustiva.

### GitHub y CI/CD

Se creó y publicó el repositorio:

`https://github.com/matibaissetto/tp11_is2`

- Rama publicada: `master`.
- Primer commit: `97a111a`.
- Mensaje del commit: `Entrega TP11 IS2`.
- Se subieron los archivos de Collatz, pruebas, documentación, regresión y conversor.
- Se ubicó el workflow principal en `.github/workflows/calidad.yml` de la raíz.
- Sus comandos se ejecutan con directorio de trabajo `json2csv`.
- Se informó visualmente un indicador de éxito en GitHub Actions; para documentar el resultado concreto del workflow debe consultarse el detalle de la ejecución.

### Generación de documentación automatizada

Cookiecutter proporcionó una estructura `docs/` y configuraciones de documentación. No obstante, la consigna exige **pdoc o Sphinx** y su generación/actualización con cada PR exitoso.

**Pendiente de validación:** no hay constancia de una ejecución de pdoc o Sphinx ni de su integración efectiva con cada PR. No debe considerarse satisfecho este requisito solo por disponer de Markdown y la estructura de `docs/`.

### Alcance de la verificación

Las comprobaciones descritas prueban el funcionamiento de los escenarios implementados y de los controles ejecutados, pero no demuestran ausencia absoluta de defectos ni cobertura completa de entradas JSON posibles.

---

## Consigna 18 - Deuda técnica y proceso de calidad

La deuda técnica representa trabajo técnico pendiente que, si se acumula, reduce la capacidad futura de un equipo para producir valor. Puede ser **deliberada**, cuando se difiere una mejora por una decisión de negocio, o **involuntaria**, cuando el retrabajo aparece por defectos, insuficiente validación y malas decisiones técnicas.

Desde el proceso de calidad, los factores que más ayudan a controlarla son:

1. **Prevención de defectos:** revisar requisitos, diseño y código reduce el número de problemas que posteriormente requieren retrabajo.
2. **Inspecciones y pruebas tempranas:** descubrir errores antes de la entrega disminuye el costo y la complejidad de corregirlos.
3. **PCE alto:** contener defectos dentro de las fases donde se originan impide que se propaguen a etapas posteriores o a producción.
4. **Automatización de controles y regresión:** pruebas, análisis estático e integración continua permiten identificar rápidamente defectos incorporados por cambios.
5. **Visibilidad y priorización de deuda:** registrar, estimar y atender las tareas de corrección evita que compitan indefinidamente con nuevas funciones.
6. **Sostenibilidad de la velocidad:** limitar el trabajo pendiente y reservar capacidad para reparaciones impide que todo el esfuerzo de un sprint se consuma en corregir problemas antiguos.

### Relación con la velocidad del proyecto

El material teórico de la cátedra explica que el retrabajo obligatorio reduce la **velocidad efectiva**, porque parte de la capacidad del equipo se utiliza en corregir funcionalidades previamente desarrolladas, en lugar de entregar nuevas funcionalidades.

Si la deuda pendiente llega a consumir toda la velocidad disponible, el proyecto puede avanzar muy poco o dejar de reducir su backlog. Por eso, mantener un PCE alto contribuye a reducir la generación de deuda técnica involuntaria y preservar la capacidad productiva.

**Aclaración de fuentes:** estas conclusiones se fundamentan en las clases de calidad y deuda técnica de la cátedra. No se verificó directamente el texto íntegro del artículo externo «Agile and software engineering, an invisible bond», por lo que no se atribuyen a ese artículo afirmaciones textuales específicas.

---

## Consigna 19 - Efecto de una multa en el equilibrio económico de garantía

En un modelo simplificado de garantía, la organización busca equilibrar:

- El **costo preventivo** de continuar probando y corrigiendo antes de la entrega.
- El **costo esperado posterior a la liberación** de atender defectos durante el período de garantía.

Sin multas, el tiempo óptimo de test se encuentra donde el beneficio esperado de seguir eliminando defectos compensa el costo adicional de las pruebas.

### Efecto de introducir una multa

Una multa contractual por defectos, incumplimiento de calidad o fallas durante la garantía **aumenta el costo esperado de liberar el producto con defectos**.

Por lo tanto, si las demás variables permanecen constantes y las pruebas adicionales reducen efectivamente los defectos remanentes:

- Se incrementa el incentivo económico para ejecutar más actividades de V&V antes de liberar.
- El punto de equilibrio se desplaza hacia un **mayor esfuerzo o tiempo óptimo de pruebas**.
- Se vuelve más valioso mejorar el PCE y evitar que defectos alcancen la fase de garantía.

La magnitud del desplazamiento depende de la probabilidad de la multa, su importe, el costo marginal de las pruebas y la eficacia real de detección.

**Matiz:** si existe un plazo contractual rígido y también se penalizan las demoras, la decisión final puede implicar un equilibrio entre multa por calidad y multa por entrega tardía. No corresponde afirmar un aumento ilimitado del tiempo de prueba.

---

## Estado final y pendientes de verificación

### Actividades desarrolladas

Se documentaron los requerimientos de Collatz, la matriz de trazabilidad, las inspecciones, las sesiones de pruebas unitarias y funcionales, el inventario de defectos, el PCE, la densidad, el análisis Kanban, las regresiones, los cálculos de garantía, el conversor y los controles locales de calidad.

### Puntos aún no comprobados completamente contra la consigna

1. **Invocación literal `python json2csv.py`:** la variante ejecutada y probada fue `python -m json2csv`.
2. **Generación automática con pdoc o Sphinx en cada PR:** no se verificó una integración que cumpla ese requisito.
3. **Reglas PEP 257:** falta una comprobación específica de docstrings con las reglas solicitadas.
4. **Proyección estadística de Collatz:** el dataset de cinco defectos no permite una estimación robusta del total latente.
5. **Artículos externos de Kanban, garantía y deuda técnica:** algunas interpretaciones se apoyaron en materiales y discusiones de clase; para referencias documentales exactas corresponde contrastar los artículos originales.

Se deja constancia de estas limitaciones para distinguir los requisitos **implementados y observados** de aquellos que todavía requieren comprobación adicional.
