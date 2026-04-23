# Guía de Análisis: Subagents en VS Code Copilot

> **Fuente:** https://code.visualstudio.com/docs/copilot/agents/subagents  
> **Fecha de análisis:** 23 de abril de 2026  
> **Aplicabilidad:** Sistema SAC (Sistema Agéntico COCHAS)

---

## 1. ¿Qué es un Subagente?

Un subagente es un **agente de IA independiente** que realiza trabajo focalizado (investigar, analizar código, revisar cambios) y reporta los resultados al agente principal. Su característica clave es el **aislamiento de contexto**: trabaja con solo la información relevante para su subtarea, sin cargar el historial completo de la conversación principal.

### Flujo de ejecución

```
Usuario → Agente Principal → reconoce subtarea → lanza Subagente
                                                       ↓
                                              trabaja autónomamente
                                                       ↓
                                              devuelve solo resultado
                              ↑
              Agente Principal incorpora resultado y continúa
```

---

## 2. Lo que ve el Usuario

Cuando un subagente corre, aparece en el chat como una **tool call colapsable** que muestra:
- Nombre del agente personalizado (si se especificó)
- Herramienta en ejecución ("Reading file...", "Searching codebase...")

Al expandirlo se ve: todas las tool calls realizadas, el prompt enviado y el resultado devuelto.

---

## 3. Cómo se Invoca un Subagente

### Iniciado por el agente (patrón principal)
El agente principal decide cuándo delegar. **No requiere que el usuario escriba "usa un subagente"**. El usuario puede insinuarlo con frases como:
- *"investiga en paralelo..."*
- *"analiza de forma aislada..."*

### Habilitación requerida
- La herramienta `runSubagent` debe estar habilitada en el agente principal
- Por defecto, subagentes **no pueden invocar** otros subagentes
- Para habilitar recursividad: `chat.subagents.allowInvocationsFromSubagents = true`

### Invocación desde un prompt file (`.prompt.md`)
```markdown
---
name: document-feature
tools: ['agent', 'read', 'search', 'edit']
---
Run a subagent to research the new feature implementation details...
```

---

## 4. Propiedades de Control en Frontmatter

| Propiedad | Valores | Efecto |
|---|---|---|
| `user-invocable` | `true` (default) / `false` | Si `false`, el agente NO aparece en el dropdown del chat — solo accesible como subagente |
| `disable-model-invocation` | `false` (default) / `true` | Si `true`, el agente NO puede ser invocado como subagente por otros agentes |
| `agents` | lista / `*` / `[]` | Restringe qué subagentes puede invocar este agente |
| `model` | nombre del modelo | Modelo preferido cuando corre como subagente |

> ⚠️ **Deprecado:** La propiedad `infer` — usar `user-invocable` y `disable-model-invocation` en su lugar.

### Ejemplo: agente solo disponible como subagente
```markdown
---
name: internal-helper
user-invocable: false
---
Este agente solo puede ser invocado como subagente.
```

---

## 5. Selección de Modelo

Orden de prioridad para el modelo del subagente:

1. **Parámetro explícito** en la invocación del agente principal
2. **Propiedad `model`** en el `.agent.md` del agente personalizado
3. **Modelo del agente principal** (herencia por defecto)

> ⚠️ **Restricción:** El modelo solicitado no puede ser más costoso que el modelo principal. Si lo es, cae al modelo principal.

---

## 6. Restringir qué Subagentes Puede Usar un Agente

```markdown
---
name: TDD
tools: ['agent']
agents: ['Red', 'Green', 'Refactor']
---
```

- Lista de nombres → solo esos agentes disponibles como subagentes
- `*` → todos los agentes disponibles (comportamiento por defecto)
- `[]` → ningún subagente permitido

> **Nota importante:** Listar explícitamente un agente en `agents` anula `disable-model-invocation: true`. Permite crear agentes protegidos de uso general pero accesibles para coordinadores específicos.

---

## 7. Subagentes Anidados (Nested Subagents)

Por defecto **deshabilitado** para evitar recursión infinita.

- Activación: `chat.subagents.allowInvocationsFromSubagents = true`
- Profundidad máxima: **5 niveles**

### Patrón recursivo (divide y vencerás)
```markdown
---
name: RecursiveProcessor
tools: ['agent', 'read', 'search']
agents: [RecursiveProcessor]
---
Si la lista tiene más de 4 ítems → dividir en mitades y delegar cada mitad a RecursiveProcessor.
Si ≤ 4 ítems → procesar directamente.
Combinar resultados.
```

---

## 8. Patrones de Orquestación

### 8.1 Coordinador + Trabajadores

El agente coordinador gestiona el flujo y delega a agentes especializados. Cada trabajador tiene herramientas ajustadas a su rol.

```markdown
---
name: Feature Builder
tools: ['agent', 'edit', 'search', 'read']
agents: ['Planner', 'Plan Architect', 'Implementer', 'Reviewer']
---
1. Planner: descomponer en tareas
2. Plan Architect: validar contra patrones del código
3. (ciclo) Si el Architect da feedback → Planner actualiza el plan
4. Implementer: escribir código por tarea
5. Reviewer: revisar implementación
6. (ciclo) Si Reviewer detecta issues → Implementer aplica fixes
```

Los trabajadores (`user-invocable: false`) tienen herramientas mínimas para su función. Los de solo lectura (Planner, Reviewer) no necesitan `edit`.

### 8.2 Revisión Multi-Perspectiva en Paralelo

```markdown
---
name: Thorough Reviewer
tools: ['agent', 'read', 'search']
---
Correr en paralelo:
- Subagente de Corrección: lógica, edge cases, tipos
- Subagente de Calidad: legibilidad, nombres, duplicados
- Subagente de Seguridad: validación de entradas, inyección, exposición de datos
- Subagente de Arquitectura: consistencia con patrones del código

Sintetizar hallazgos en un resumen priorizado.
```

> Clave: cada subagente llega al código **sin ser influenciado** por los otros. Resultados más independientes y objetivos.

---

## 9. Escenarios de Uso Recomendados

| Escenario | Por qué usar subagente |
|---|---|
| Investigar antes de implementar | Contexto de investigación separado del contexto de implementación |
| Análisis de código en paralelo | Múltiples archivos/módulos analizados simultáneamente |
| Explorar múltiples soluciones | Cada alternativa evaluada en su propio contexto aislado |
| Code review con foco especializado | Perspectivas independientes y sin sesgo mutuo |
| Consenso multi-modelo | Mismo problema evaluado con diferentes modelos |

---

## 10. Buenas Prácticas Extraídas

1. **Definir cuándo usar subagentes en las instrucciones del agente**, no promtear manualmente cada vez
2. **Describir claramente la tarea y el output esperado** para que el subagente no devuelva contexto innecesario
3. **Usar `user-invocable: false`** para agentes internos/trabajadores que no deberían aparecer en el dropdown
4. **Restringir `agents`** cuando el coordinador solo debe usar subagentes específicos (evita selección incorrecta si hay agentes con nombres/descripciones similares)
5. **Asignar modelo más ligero a trabajadores** con foco estrecho — no necesitan el modelo más potente
6. **Para revisión paralela**: estructurar cada perspectiva como un subagente independiente para evitar anclas cognitivas entre ellas

---

## 11. Aplicabilidad para SAC

| Capacidad VS Code | Oportunidad en SAC |
|---|---|
| `user-invocable: false` | Agentes internos/auxiliares que no deben aparecer al usuario final |
| `agents: [lista]` | Definir en cada agente SAC qué otros agentes puede convocar |
| Patrón Coordinador+Trabajadores | Agente orquestador que delega a Arquitecto, Desarrollador, DevOps, Analista |
| Revisión multi-perspectiva | Validación de HUs desde múltiples ángulos en paralelo |
| Subagente de investigación | Precargar contexto del proyecto antes de una sesión de refinamiento |
| `disable-model-invocation: true` | Proteger agentes SAC de invocación no autorizada por agentes externos |

### Propiedad `agents` pendiente de añadir a agentes SAC

Ningún agente `.agent.md` de SAC tiene actualmente la propiedad `agents` en su frontmatter. Añadirla permitiría:
- Controlar exactamente qué agentes puede delegar cada uno
- Evitar que el LLM seleccione un agente incorrecto cuando hay descripciones similares
- Habilitar flujos de orquestación formales (ej. Arquitecto → Desarrollador → Cronista)

---

## 12. Referencia Rápida de Frontmatter

```markdown
---
name: "Nombre del Agente"
description: "Descripción breve"
model: "Claude Sonnet 4.6 (copilot)"   # opcional
tools: ['agent', 'read', 'search', 'edit']
agents: ['Agente1', 'Agente2']          # opcional: restringe subagentes
user-invocable: true                    # false = solo subagente
disable-model-invocation: false         # true = no puede ser subagente
---
```

---

*Documento generado a partir del análisis de la documentación oficial de VS Code Copilot Subagents (abril 2026)*
