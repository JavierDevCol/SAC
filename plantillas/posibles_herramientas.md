# 🛠️ Herramientas Potenciales para [Nombre del Rol]

> Documento de análisis y especificación de herramientas potenciales identificadas durante la refactorización del rol **[Nombre del Rol]**. Este documento sirve como referencia para futuras implementaciones o refactorizaciones de herramientas existentes.

---

## 📋 Índice

- [🛠️ Herramientas Potenciales para \[Nombre del Rol\]](#️-herramientas-potenciales-para-nombre-del-rol)
  - [📋 Índice](#-índice)
  - [Herramienta 1: `nombre_herramienta_1` (NUEVA)](#herramienta-1-nombre_herramienta_1-nueva)
  - [Mejora a herramienta existente: `nombre_herramienta_existente`](#mejora-a-herramienta-existente-nombre_herramienta_existente)
  - [📝 Notas Finales](#-notas-finales)
    - [Priorización Recomendada para Implementación](#priorización-recomendada-para-implementación)
    - [Impacto Estimado](#impacto-estimado)
    - [📅 Última Actualización](#-última-actualización)

---

## Herramienta 1: `nombre_herramienta_1` (NUEVA)

**🎯 Propósito**
[Describe el objetivo principal de la herramienta en una sola frase concisa.]

**📊 Nivel de Prioridad**
[Selecciona: 🔴 ALTA, 🟡 MEDIA, 🟢 BAJA] - [Justifica brevemente la prioridad]

**🔍 Problema que Resuelve**
*   **Antes**: [Describe el flujo de trabajo manual, lento o propenso a errores que existe actualmente.]
*   **Después**: [Describe cómo la nueva herramienta soluciona ese problema, haciendo el proceso más rápido, más preciso o automático.]

**📥 Input Esperado**
*   **Parámetros**:
    *   `parametro_1` ([tipo], [requerido/opcional]): [Descripción del parámetro.]
    *   `parametro_2` ([tipo], [requerido/opcional]): [Descripción del parámetro.]
*   **Ejemplo de Invocación**:
    ```json
    {
      "parametro_1": "valor de ejemplo",
      "parametro_2": {
        "sub_parametro": true
      }
    }
    ```

**📤 Output Esperado**
*   **Formato**: [Describe el formato de salida, ej: JSON estructurado, Markdown, etc.]
*   **Ejemplo de Salida**:
    ```json
    {
      "resultado_exitoso": true,
      "datos_generados": {
        "clave": "valor",
        "descripcion": "Resultado del procesamiento."
      },
      "recomendaciones": [
        "Acción sugerida 1.",
        "Acción sugerida 2."
      ]
    }
    ```

**🔧 Lógica Interna Sugerida**
*   **Fase 1: [Nombre de la Fase, ej: Validación de Entradas]**
    *   [Paso 1.1: Describir la primera acción lógica.]
    *   [Paso 1.2: Describir la segunda acción lógica.]
*   **Fase 2: [Nombre de la Fase, ej: Procesamiento Principal]**
    *   [Paso 2.1: Describir la lógica central de la herramienta.]
*   **Fase 3: [Nombre de la Fase, ej: Formateo de Salida]**
    *   [Paso 3.1: Describir cómo se estructura el resultado final.]

**🎭 Comportamiento Esperado del Rol**
*   **Usuario**: "[Ejemplo de lo que el usuario pide.]"
*   **[Nombre del Rol]**: "[Ejemplo de cómo el rol invoca la herramienta y presenta los resultados.]"
    ```
    [Ejecuta: > nombre_herramienta_1 parametro_1="..."]
    ```
*   **[Nombre del Rol]**: "[Ejemplo de la respuesta del rol después de que la herramienta se ejecuta, mostrando el valor aportado.]"

**🔗 Integración con Otros Roles/Herramientas**

| Rol / Herramienta | Uso / Sinergia                                                              |
| :---------------- | :-------------------------------------------------------------------------- |
| **[Otro Rol]**    | [Describe cómo este otro rol podría beneficiarse o usar esta herramienta.]    |
| **[Otra Herramienta]** | [Describe si esta herramienta es usada por otra, o si usa el output de otra.] |

**📈 Criterios de Éxito**
*   ✅ [Métrica 1 cuantificable. Ej: Reduce el tiempo de la tarea X en un 80%.]
*   ✅ [Métrica 2 cuantificable. Ej: Aumenta la precisión de Y en un 95%.]
*   ✅ [Métrica 3 de rendimiento. Ej: Completa el análisis en < 5 segundos para entradas estándar.]

**🚧 Limitaciones Conocidas**
*   [Describe cualquier limitación, dependencia o caso en el que la herramienta podría no funcionar de manera óptima.]
*   [Menciona cualquier pre-requisito (ej: necesita acceso a un sistema de archivos, etc.).]

---

## Mejora a herramienta existente: `nombre_herramienta_existente`

**🎯 Propósito de la Mejora**
[Describe el objetivo principal de la actualización y qué se busca lograr con el cambio.]

**📊 Nivel de Prioridad**
[Selecciona: 🔴 ALTA, 🟡 MEDIA, 🟢 BAJA] - [Justifica brevemente la prioridad de la mejora.]

**🔍 Estado Deseado**
[Describe de forma clara cómo debería funcionar o verse la herramienta después de la mejora. Puedes usar un formato "Antes/Después", describir nuevos parámetros, o mostrar la nueva estructura de salida deseada.]

**📈 Criterios de Éxito de la Mejora**
*   ✅ [Métrica 1 específica para la mejora. Ej: La integración con la herramienta X funciona sin errores.]
*   ✅ [Métrica 2 específica para la mejora. Ej: El nuevo parámetro Y es utilizado correctamente y mejora la flexibilidad.]

---

## 📝 Notas Finales

### Priorización Recomendada para Implementación

*   **🥇 Primera iteración (Crítica):**
    *   [Nombre de la herramienta/mejora más importante.]
    *   *Justificación*: [Justificación breve.]
*   **🥈 Segunda iteración (Alta prioridad):**
    *   [Nombre de la siguiente herramienta/mejora.]
*   **🥉 Tercera iteración (Optimización):**
    *   [Nombre de la herramienta/mejora de menor prioridad o "nice-to-have".]

### Impacto Estimado

| Herramienta/Mejora           | Ahorro de Tiempo     | Mejora de Calidad    | Complejidad Implementación |
| :--------------------------- | :------------------- | :------------------- | :------------------------- |
| `nombre_herramienta_1`       | [Califica: 🔥 a 🔥🔥🔥🔥] | [Califica: 🔥 a 🔥🔥🔥🔥] | [🟢 Baja, 🟡 Media, 🔴 Alta] |
| `nombre_herramienta_existente` | [Califica: 🔥 a 🔥🔥🔥🔥] | [Califica: 🔥 a 🔥🔥🔥🔥] | [🟢 Baja, 🟡 Media, 🔴 Alta] |

### 📅 Última Actualización

*   **Fecha**: [YYYY-MM-DD]
*   **Autor**: [Tu Nombre/Alias]
*   **Estado**: [Propuesta / En Análisis / Aprobado]
