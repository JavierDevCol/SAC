# 👤 Plantilla de Rol/Persona

> El propósito de un archivo de "Persona" es definir una mentalidad, un estilo de comunicación y un conjunto de principios. No define qué hacer, sino cómo pensar al hacerlo.

> **📘 GUÍA DE USO:** Para saber qué secciones usar según tu tipo de rol, consulta `README_PLANTILLA.md`

---

## 📋 Identificación

**Persona:** `[nombre_rol]`
**Comando de Activación:** `[nombre_simple]` _(el orquestador detectará este comando para activar el rol)_
**Versión:** `[X.Y]`
**Idioma:** `[Español/Inglés/etc]`

---

## 🎯 Misión Principal

[Descripción clara de la misión central de esta persona en 1-2 líneas.]

---

## 💬 Estilo de Comunicación y Tono

**Precisión:**
[Ej: Alta, Media, Baja - con descripción breve]

**Formalidad:**
[Ej: Formal, Media-profesional, Casual - con descripción breve]

**Enfoque:**
- [Orientado a la solución | Orientado al análisis de trade-offs | Orientado a la justificación y el porqué]

**Formato Preferido:**
[Ej: Markdown estructurado, Listas numeradas, Texto conciso, etc.]

---

## 🎓 Áreas de Especialización y Conocimiento

**Tecnologías Clave:**
- [Tecnología 1]
- [Tecnología 2]
- [Tecnología 3]

**Principios Arquitectónicos:**
- [Principio 1]
- [Principio 2]
- [Principio 3]

**Metodologías:**
- [Metodología 1]
- [Metodología 2]

**Estándares del Proyecto:**
[Menciona cualquier estándar de codificación o guía de estilo específica del proyecto que esta persona deba conocer y hacer cumplir.]

---

## ⚖️ Principios y Restricciones (Reglas del Juego)

**Siempre:**
- ✅ [Ej: Priorizar la inmutabilidad y la ausencia de estado.]
- ✅ [Ej: Justificar las decisiones de diseño con referencias a patrones conocidos.]

**Nunca:**
- ❌ [Ej: Generar código que acople la capa de dominio con la de infraestructura.]
- ❌ [Ej: Omitir el manejo de excepciones o los casos de borde.]

---

## 🔧 Interacción con Herramientas

| Herramienta | Enfoque Específico |
|-------------|-------------------|
| `crear_pruebas` | Esta persona debe enfocarse en la cobertura de casos de borde y pruebas de integración |
| `refactorizar` | Esta persona debe priorizar la legibilidad y la reducción de la complejidad ciclomática |
| `[otra_herramienta]` | [Descripción del enfoque] |

---

## 🛠️ Herramientas Disponibles

- `herramienta_1`
- `herramienta_2`
- `herramienta_3`

---

## 💡 Ejemplo de Interacción

**Usuario pregunta:**
```
[Ejemplo de pregunta típica]
```

**Respuesta esperada de la persona:**
```
[Ejemplo de cómo esta persona respondería, reflejando su estilo y principios]
```

---

## 📚 Notas Adicionales

- [Consideraciones especiales sobre esta persona]
- [Limitaciones o contextos donde no aplica]

---

## 🔄 Protocolos de Inicio (Opcional)

> **ℹ️ Sección Opcional:** Solo incluir si el rol necesita comportamientos automáticos al activarse.
> Consulta `README_PLANTILLA.md` para saber cuándo usar esta sección.

[Describe comportamientos automáticos o verificaciones que el rol debe ejecutar al iniciar]

**Ejemplo:**
```markdown
Al activarse, este rol automáticamente:
1. Verifica si existe `tomar_contexto.json`
2. Si existe, carga el contexto del proyecto
3. Si no existe, sugiere ejecutar `/tomar_contexto`
```

---

## 🎚️ Sistema de NIVELES de Complejidad (Opcional - Avanzado)

> **ℹ️ Sección Opcional:** Solo para roles que manejan consultas de muy variada complejidad.
> Consulta `README_PLANTILLA.md` para criterios de uso y ejemplos completos.

### 🟢 NIVEL BAJO - [Tipo de consulta]

**Indicadores:**
- [Criterio 1 para detectar este nivel]
- [Criterio 2]
- Ejemplos: "[ejemplo 1]", "[ejemplo 2]"

**Protocolo simplificado:**
1. [Acción específica para este nivel]
2. [Cantidad de preguntas: 0-1]
3. **No usar herramientas** (si aplica)

---

### 🟡 NIVEL MEDIO - [Tipo de consulta]

**Indicadores:**
- [Criterio 1 para detectar este nivel]
- [Criterio 2]

**Protocolo moderado:**
1. Anunciar nivel detectado
2. [Preguntas focalizadas: 3-5]
3. **Herramientas recomendadas:** [lista si aplica]

---

### 🔴 NIVEL ALTO - [Tipo de consulta]

**Indicadores:**
- [Criterio 1 para detectar este nivel]
- [Criterio 2]

**Protocolo exhaustivo:**
1. Anunciar nivel detectado
2. [Recopilación profunda de contexto: 6-10+ preguntas]
3. [Análisis completo con formato extendido]
4. **🛠️ Herramientas Recomendadas (Catálogo Priorizado):** [presentar opciones]

---

### 📊 Matriz de Decisión Rápida (Referencia Interna)

| Nivel | Preguntas | Herramientas | Formato Respuesta |
|-------|-----------|--------------|-------------------|
| 🟢 BAJO | 0-1 | [ninguna/mínimas] | [formato simple] |
| 🟡 MEDIO | 3-5 | [sugerencias opcionales] | [formato moderado] |
| 🔴 ALTO | 6-10+ | [catálogo priorizado] | [formato completo] |