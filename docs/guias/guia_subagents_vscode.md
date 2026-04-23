# Análisis Experto: Subagents en VS Code Copilot

> **Fuente primaria:** https://code.visualstudio.com/docs/copilot/agents/subagents  
> **Fuentes secundarias:** https://code.visualstudio.com/docs/copilot/concepts/agents | https://code.visualstudio.com/docs/copilot/customization/custom-agents  
> **Fecha de análisis:** 23 de abril de 2026 (documentación oficial actualizada 22/04/2026)  
> **Aplicabilidad:** Sistema SAC (Sistema Agéntico COCHAS)

---

## Tabla de Contenidos

1. [Marco Conceptual: El Loop Agéntico](#1-marco-conceptual-el-loop-agéntico)
2. [¿Qué es un Subagente?](#2-qué-es-un-subagente)
3. [Características Clave](#3-características-clave)
4. [Lo que ve el Usuario](#4-lo-que-ve-el-usuario)
5. [Cómo se Invoca un Subagente](#5-cómo-se-invoca-un-subagente)
6. [Escenarios de Uso con Ejemplos](#6-escenarios-de-uso-con-ejemplos)
7. [Propiedades de Control en Frontmatter](#7-propiedades-de-control-en-frontmatter)
8. [Selección de Modelo](#8-selección-de-modelo)
9. [Restricción de Subagentes Disponibles](#9-restricción-de-subagentes-disponibles)
10. [Subagentes Anidados y Recursivos](#10-subagentes-anidados-y-recursivos)
11. [Patrones de Orquestación Avanzados](#11-patrones-de-orquestación-avanzados)
12. [Agentes Personalizados como Subagentes](#12-agentes-personalizados-como-subagentes)
13. [Handoffs: Flujos Secuenciales Guiados](#13-handoffs-flujos-secuenciales-guiados)
14. [Formato Claude de Agentes](#14-formato-claude-de-agentes)
15. [Sistema de Memoria en Agentes](#15-sistema-de-memoria-en-agentes)
16. [Consideraciones de Seguridad](#16-consideraciones-de-seguridad)
17. [Buenas Prácticas Extraídas](#17-buenas-prácticas-extraídas)
18. [Aplicabilidad para SAC](#18-aplicabilidad-para-sac)
19. [Referencia Rápida de Frontmatter Completo](#19-referencia-rápida-de-frontmatter-completo)

---

## 1. Marco Conceptual: El Loop Agéntico

Antes de entender los subagentes, es fundamental entender el **loop agéntico**: el ciclo que sigue cualquier agente de IA en VS Code al recibir una tarea.

### El ciclo de 3 fases

```
┌─────────────────────────────────────────────────────────────────────┐
│                        LOOP AGÉNTICO                                │
├──────────────┬──────────────────────┬──────────────────────────────┤
│  FASE 1:     │  FASE 2:             │  FASE 3:                     │
│  ENTENDER    │  ACTUAR              │  VALIDAR                     │
│              │                      │                              │
│ • Leer arch. │ • Modificar código   │ • Correr tests               │
│ • Buscar en  │ • Ejecutar comandos  │ • Verificar errores          │
│   codebase   │ • Instalar deps.     │ • Revisar cambios propios    │
│ • Leer docs  │ • Llamar servicios   │ • Iterar si algo falla       │
└──────────────┴──────────────────────┴──────────────────────────────┘
         ↑                                           │
         └─────────────────────────────────────────-┘
                    (ciclo hasta completar la tarea)
```

### Cómo VS Code construye el contexto

En cada iteración del loop, VS Code:
1. Ensambla el contexto actual en un prompt
2. Lo envía al modelo de lenguaje
3. El modelo responde con texto, una edición de código, o una solicitud de tool
4. El output de cada tool se añade al contexto para la siguiente iteración
5. El ciclo se repite hasta completar la tarea

### Problema que resuelven los Subagentes

Sin subagentes, **cada archivo leído, resultado de búsqueda y paso intermedio** acumula en la ventana de contexto del agente principal. Esto puede:
- Saturar el contexto con información de investigación redundante
- Desplazar información importante de implementación
- Aumentar costos de tokens innecesariamente

---

## 2. ¿Qué es un Subagente?

Un subagente es un **agente de IA independiente** que realiza trabajo focalizado (investigar un tema, analizar código, revisar cambios) y reporta **solo el resultado final** al agente principal.

### Flujo de ejecución

```
Usuario describe tarea compleja
          │
          ▼
┌─────────────────────┐
│  AGENTE PRINCIPAL   │
│                     │
│  reconoce subtarea  │
│  que se beneficia   │
│  de contexto aislado│
└─────────┬───────────┘
          │  lanza subagente con solo
          │  la información relevante
          ▼
┌─────────────────────┐
│     SUBAGENTE       │
│                     │
│  trabaja en su      │◄── contexto aislado
│  propia ventana     │    (sin historial del padre)
│  de contexto        │
│                     │
│  devuelve SOLO      │
│  el resultado final │
└─────────┬───────────┘
          │  resultado compacto
          ▼
┌─────────────────────┐
│  AGENTE PRINCIPAL   │
│                     │
│  incorpora resultado│
│  y continúa la      │
│  tarea principal    │
└─────────────────────┘
```

---

## 3. Características Clave

| Característica | Descripción |
|---|---|
| **Aislamiento de contexto** | Cada subagente corre en su propia ventana de contexto. No hereda el historial ni las instrucciones del agente padre. Solo recibe el prompt de la tarea |
| **Ejecución sincrónica** | El agente principal **espera** los resultados del subagente antes de continuar, ya que los hallazgos típicamente informan el siguiente paso |
| **Ejecución en paralelo** | VS Code puede lanzar múltiples subagentes en paralelo para tareas simultáneas (ej. analizar seguridad, rendimiento y accesibilidad al mismo tiempo) |
| **Resultados enfocados** | Solo el resultado final regresa al agente principal — mantiene el contexto principal limpio y reduce el uso de tokens |

---

## 4. Lo que ve el Usuario

Cuando un subagente corre, aparece en el chat como una **tool call colapsable** que por defecto muestra:
- El nombre del agente personalizado (si se especificó)
- La herramienta actualmente en ejecución (ej. "Reading file...", "Searching codebase...")

Al **expandirlo** el usuario puede ver:
- Todas las tool calls que realizó el subagente
- El prompt exacto que se le pasó al subagente
- El resultado devuelto

> Esta visibilidad brinda control sobre cuánto detalle ver sin saturar la conversación principal con pasos intermedios.

---

## 5. Cómo se Invoca un Subagente

### 5.1 Iniciado por el agente (patrón principal)

Los subagentes son típicamente **iniciados por el agente**, no directamente por los usuarios en el chat. El agente principal decide cuándo el aislamiento de contexto ayuda. **No se necesita escribir manualmente "usa un subagente" para cada tarea.**

El patrón funciona así:

```
1. El usuario (o las instrucciones del agente) describe una tarea compleja.
2. El agente principal reconoce la parte que se beneficia de contexto aislado.
3. El agente lanza un subagente, pasando solo la subtarea relevante.
4. El subagente trabaja autónomamente y devuelve un resumen.
5. El agente principal incorpora el resultado y continúa.
```

Se puede insinuar que se quiere delegar a subagente con frases como:
- *"investiga en paralelo..."*
- *"analiza de forma aislada..."*
- *"usa un subagente para investigar..."*

### 5.2 Habilitación requerida

```yaml
# Requisitos para usar subagentes:
# 1. La herramienta runSubagent debe estar habilitada en el agente principal
# 2. Para subagentes recursivos (que lanzan sus propios subagentes):
chat.subagents.allowInvocationsFromSubagents: true  # false por defecto
```

### 5.3 Invocación desde un prompt file (`.prompt.md`)

```markdown
---
name: document-feature
tools: ['agent', 'read', 'search', 'edit']
---
Run a subagent to research the new feature implementation details
and return only information relevant for user documentation.
Then update the docs/ folder with the new documentation.
```

> **Tip:** Para comportamiento consistente, define **cuándo usar subagentes en las instrucciones del agente personalizado**, no promteando manualmente cada vez.

### 5.4 Invocación de un agente personalizado como subagente

```
"Run the Research agent as a subagent to research the best auth methods for this project."
"Use the Plan agent in a subagent to create an implementation plan for myfeature."
"Run a subagent with Claude Sonnet 4.6 to research authentication patterns in this codebase."
```

---

## 6. Escenarios de Uso con Ejemplos

### 6.1 Investigar antes de implementar

**Problema:** La investigación previa satura el contexto antes de comenzar a escribir código.

**Solución con subagente:**
```
"Use a subagent to research how the authentication module works,
then implement the new OAuth provider based on those findings."
```
El subagente devuelve solo los hallazgos clave; el agente principal implementa con contexto limpio.

---

### 6.2 Análisis de código en paralelo

**Problema:** Analizar múltiples módulos secuencialmente es lento y acumula contexto.

**Solución con subagente:**
```
"Analyze the performance of modules A, B, and C in parallel using subagents,
then synthesize the findings."
```
VS Code lanza 3 subagentes simultáneamente, cada uno con acceso solo al módulo que le corresponde.

---

### 6.3 Explorar múltiples soluciones

**Problema:** Evaluar alternativas de arquitectura contamina el contexto con exploración descartada.

**Solución con subagente:**
```
"Use subagents to evaluate three different caching strategies:
Redis, in-memory, and CDN-based. Return pros/cons and recommendation for each."
```
Cada subagente evalúa una estrategia de forma independiente y sin sesgo.

---

### 6.4 Code review con foco especializado

**Problema:** Un solo pass de revisión pierde problemas que son obvios desde otra perspectiva.

**Solución con subagente:**
```
"Review this PR using parallel subagents, each focused on:
security vulnerabilities, performance bottlenecks, and code quality."
```
Cada perspectiva llega al código fresca, sin ser anclada por lo que otras encontraron.

---

### 6.5 Consenso multi-modelo

**Problema:** Un solo modelo puede tener sesgos o puntos ciegos.

**Solución con subagente:**
```
"Run subagents with GPT-4o and Claude Sonnet to evaluate this architecture decision.
Then synthesize both opinions."
```
Se aprovecha la selección de modelo por subagente para obtener perspectivas complementarias.

---

## 7. Propiedades de Control en Frontmatter

### Tabla completa de propiedades

| Propiedad | Tipo | Default | Efecto |
|---|---|---|---|
| `user-invocable` | boolean | `true` | Si `false` → el agente NO aparece en el dropdown del chat. Solo accesible como subagente |
| `disable-model-invocation` | boolean | `false` | Si `true` → el agente NO puede ser invocado como subagente por otros agentes |
| `agents` | lista / `*` / `[]` | `*` | Restringe qué subagentes puede invocar este agente |
| `model` | string / array | modelo actual | Modelo preferido. Array = lista priorizada (intenta cada uno hasta encontrar uno disponible) |
| `tools` | lista | — | Herramientas disponibles. Incluir `'agent'` para poder usar subagentes |
| `argument-hint` | string | — | Texto de ayuda mostrado al usuario en el input del chat |
| `description` | string | — | Descripción breve mostrada como placeholder |
| `name` | string | nombre del archivo | Nombre visible del agente |
| `handoffs` | lista | — | Acciones de transición hacia otros agentes (ver sección 13) |
| `hooks` (Preview) | lista | — | Comandos hook con scope en este agente |
| `target` | string | `vscode` | Entorno destino: `vscode` o `github-copilot` |
| `mcp-servers` | lista | — | Servidores MCP para agentes con `target: github-copilot` |

> ⚠️ **Deprecado:** La propiedad `infer`. Usar `user-invocable` y `disable-model-invocation` en su lugar.
>
> - `infer: true` (antes) = visible en picker + disponible como subagente
> - `infer: false` (antes) = oculto del picker + no disponible como subagente
>
> Los nuevos campos dan control independiente: `user-invocable: false` oculta del picker pero permite subagente. `disable-model-invocation: true` previene subagente pero mantiene en picker.

### Ejemplo: agente solo disponible como subagente (interno)

```markdown
---
name: internal-helper
user-invocable: false
---
Este agente solo puede ser invocado como subagente por otros agentes.
```

### Ejemplo: agente protegido de invocación por subagentes externos

```markdown
---
name: DatabaseAdmin
disable-model-invocation: true
tools: ['edit', 'run']
---
Agente con permisos elevados. Solo puede ser invocado por el usuario directamente.
```

---

## 8. Selección de Modelo

### Orden de prioridad (de mayor a menor)

```
1. Parámetro explícito en la invocación del runSubagent
         ↓ (si no se especifica)
2. Propiedad `model` en el .agent.md del agente personalizado
         ↓ (si no se especifica)
3. Modelo del agente principal (herencia por defecto)
```

### Selección de modelo array (lista priorizada)

```markdown
---
name: Implementer
model: ['Claude Haiku 4.5 (copilot)', 'Gemini 3 Flash (Preview) (copilot)']
---
```
El sistema intenta cada modelo en orden hasta encontrar uno disponible.

### Solicitar modelo en prompt

```
"Run a subagent with Claude Sonnet 4.6 to research authentication patterns in this codebase."
"Use GPT-4o in a subagent to analyze the performance of this module."
```

> ⚠️ **Restricción importante:** El modelo solicitado no puede ser **más costoso** que el modelo principal. Si lo es, el subagente cae automáticamente al modelo principal. Los trabajadores especializados con foco estrecho pueden usar modelos más rápidos/económicos.

---

## 9. Restricción de Subagentes Disponibles

### La propiedad `agents`

```markdown
agents: ['Agente1', 'Agente2']   # solo estos pueden ser subagentes
agents: '*'                       # todos disponibles (default)
agents: []                        # ningún subagente permitido
```

### Cuándo usar la restricción

Por defecto, todos los agentes personalizados que no tengan `disable-model-invocation: true` están disponibles como subagentes. Si dos o más agentes tienen **nombres o descripciones similares**, el LLM puede seleccionar el agente incorrecto.

Especificar `agents` evita este problema:

```markdown
---
name: TDD
tools: ['agent']
agents: ['Red', 'Green', 'Refactor']
---
Implementa usando TDD. Usa subagentes para:
1. Red agent: escribir tests fallidos
2. Green agent: implementar código para pasar los tests
3. Refactor agent: mejorar calidad del código
```

> **Nota crucial:** Listar explícitamente un agente en `agents` **anula** `disable-model-invocation: true`. Esto permite crear agentes protegidos de uso general pero accesibles para coordinadores específicos que los listan explícitamente.

---

## 10. Subagentes Anidados y Recursivos

### Estado por defecto: deshabilitado

Los subagentes por defecto **no pueden lanzar sus propios subagentes**. Esto previene recursión infinita cuando los agentes se llaman a sí mismos accidentalmente.

### Habilitación

```json
// settings.json de VS Code
{
  "chat.subagents.allowInvocationsFromSubagents": true
}
```

**Profundidad máxima de anidamiento: 5 niveles**

### Cuándo habilitar

Flujos que se benefician de recursión:
- Agente divide-y-vencerás que parte una tarea grande en piezas más pequeñas
- Procesamiento recursivo de estructuras de árbol
- Análisis de carpetas/módulos anidados

### Patrón recursivo (divide y vencerás)

```markdown
---
name: RecursiveProcessor
tools: ['agent', 'read', 'search']
agents: [RecursiveProcessor]
argument-hint: A list of items to process
---

Procesas una lista de ítems dividiendo y conquistando:
- Si la lista tiene más de 4 ítems: dividir a la mitad y delegar cada
  mitad a un subagente RecursiveProcessor.
- Si tiene 4 ítems o menos: procesar directamente.
- Combinar los resultados de cada subagente en el resultado final.
```

> Un agente **recursivo** se lista a sí mismo en su propia propiedad `agents`. Requiere `chat.subagents.allowInvocationsFromSubagents` habilitado.

---

## 11. Patrones de Orquestación Avanzados

### 11.1 Coordinador + Trabajadores (Coordinator & Worker)

El agente coordinador gestiona el flujo de alto nivel y delega a agentes especializados. Cada trabajador tiene herramientas ajustadas a su rol específico.

```
┌──────────────────────────────────────────────────────┐
│               COORDINADOR (Feature Builder)          │
│  tools: ['agent', 'edit', 'search', 'read']          │
│  agents: ['Planner', 'Plan Architect',               │
│           'Implementer', 'Reviewer']                  │
└─────┬──────────┬──────────────┬───────────┬──────────┘
      │          │              │           │
      ▼          ▼              ▼           ▼
 ┌─────────┐ ┌───────────┐ ┌──────────┐ ┌──────────┐
 │ Planner │ │Plan Arch. │ │Implement.│ │ Reviewer │
 │         │ │           │ │          │ │          │
 │ read    │ │ read      │ │ edit     │ │ read     │
 │ search  │ │ search    │ │ run      │ │ search   │
 │         │ │           │ │          │ │          │
 │ No edit │ │ No edit   │ │Modelo    │ │ No edit  │
 │ No run  │ │ No run    │ │económico │ │ No run   │
 └─────────┘ └───────────┘ └──────────┘ └──────────┘
```

**Archivo del coordinador:**
```markdown
---
name: Feature Builder
tools: ['agent', 'edit', 'search', 'read']
agents: ['Planner', 'Plan Architect', 'Implementer', 'Reviewer']
---
Eres un coordinador de desarrollo de features. Para cada solicitud:

1. Usa el agente Planner para descomponer el feature en tareas.
2. Usa el agente Plan Architect para validar el plan contra patrones del codebase.
3. Si el Architect identifica patrones reutilizables, envía feedback al Planner.
4. Usa el agente Implementer para escribir código para cada tarea.
5. Usa el agente Reviewer para verificar la implementación.
6. Si el Reviewer identifica problemas, usa Implementer de nuevo para aplicar fixes.

Itera entre planificación y arquitectura, y entre revisión e implementación,
hasta que cada fase converja.
```

**Archivos de trabajadores (con herramientas mínimas necesarias):**
```markdown
---
name: Planner
user-invocable: false
tools: ['read', 'search']
---
Descompón solicitudes de features en tareas de implementación.
Incorpora feedback del Plan Architect.
```

```markdown
---
name: Plan Architect
user-invocable: false
tools: ['read', 'search']
---
Valida planes contra el codebase. Identifica patrones, utilidades y librerías existentes
que deberían reutilizarse. Señala pasos del plan que duplican funcionalidad existente.
```

```markdown
---
name: Implementer
user-invocable: false
model: ['Claude Haiku 4.5 (copilot)', 'Gemini 3 Flash (Preview) (copilot)']
---
Escribe código para completar las tareas asignadas.
```

```markdown
---
name: Reviewer
user-invocable: false
tools: ['read', 'search']
---
Revisa implementaciones en busca de correctitud, calidad y seguridad.
```

---

### 11.2 Revisión Multi-Perspectiva en Paralelo

```
                    ┌──────────────────────┐
                    │  Thorough Reviewer   │
                    │  (Coordinador)       │
                    └──────┬───────────────┘
                           │ lanza en paralelo
              ┌────────────┼────────────┬────────────────┐
              ▼            ▼            ▼                ▼
      ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
      │Correctnes│ │ Calidad  │ │Seguridad │ │ Arquitectura │
      │Reviewer  │ │ Reviewer │ │ Reviewer │ │   Reviewer   │
      │          │ │          │ │          │ │              │
      │lógica    │ │legibil.  │ │validación│ │patrones      │
      │edge cases│ │nombres   │ │inyección │ │consistencia  │
      │tipos     │ │duplic.   │ │exposición│ │alineamiento  │
      └──────────┘ └──────────┘ └──────────┘ └──────────────┘
              │            │            │                │
              └────────────┴────────────┴────────────────┘
                                        │
                           ┌────────────▼───────────────┐
                           │   Síntesis priorizada       │
                           │   - Crítico vs nice-to-have │
                           │   - Lo que el código hace   │
                           │     bien también se reconoce│
                           └────────────────────────────┘
```

```markdown
---
name: Thorough Reviewer
tools: ['agent', 'read', 'search']
---
Revisas código a través de múltiples perspectivas simultáneamente.
Corre cada perspectiva como subagente paralelo para que los hallazgos
sean independientes y sin sesgo mutuo.

Al revisar código, corre estos subagentes EN PARALELO:
- Revisor de Correctitud: errores de lógica, edge cases, problemas de tipos.
- Revisor de Calidad: legibilidad, nombres, duplicación.
- Revisor de Seguridad: validación de entrada, riesgos de inyección, exposición de datos.
- Revisor de Arquitectura: patrones del codebase, consistencia de diseño, alineamiento estructural.

Luego sintetiza los hallazgos en un resumen priorizado. Nota qué issues son
críticos vs nice-to-have. Reconoce también lo que el código hace bien.
```

> **Tip avanzado:** Para más control, cada perspectiva puede ser su propio agente personalizado con herramientas especializadas. Por ejemplo, un revisor de seguridad podría usar un servidor MCP de análisis de seguridad, mientras que el revisor de calidad tendría acceso a herramientas de linting CLI.

---

## 12. Agentes Personalizados como Subagentes

### ¿Qué son los Agentes Personalizados?

Los custom agents son archivos `.agent.md` que definen:
- **Instrucciones** específicas de comportamiento
- **Herramientas** disponibles (controladas por el frontmatter `tools`)
- **Modelo** preferido
- **Handoffs** hacia otros agentes

### Ubicaciones de archivos

| Alcance | Ubicación |
|---|---|
| Workspace | `.github/agents/` |
| Workspace (formato Claude) | `.claude/agents/` |
| Perfil de usuario | `~/.copilot/agents/` o datos de usuario del perfil VS Code |

### Ventajas de usar custom agents como subagentes

- **Herramientas acotadas:** un agente trabajador de solo lectura no puede modificar archivos accidentalmente
- **Modelo económico:** trabajadores con foco estrecho pueden usar modelos más rápidos y baratos
- **Instrucciones especializadas:** instrucciones precisas para cada rol sin contaminar al coordinador
- **Reutilización:** el mismo agente trabajador puede ser invocado por múltiples coordinadores

### Estructura mínima de un `.agent.md`

```markdown
---
name: Nombre del Agente
description: Descripción breve mostrada en el chat
model: Claude Sonnet 4.6 (copilot)
tools: ['read', 'search']
user-invocable: false
---

## Instrucciones

Aquí van las instrucciones detalladas de comportamiento del agente.
Puedes referenciar otros archivos con links de Markdown.
Usa #tool:<nombre> para referenciar herramientas en el cuerpo.
```

---

## 13. Handoffs: Flujos Secuenciales Guiados

Los **handoffs** permiten crear flujos de trabajo secuenciales guiados entre agentes. Después de que una respuesta de chat completa, aparecen **botones de handoff** que llevan al usuario al siguiente agente con contexto relevante y un prompt pre-rellenado.

### Casos de uso

| Flujo | Descripción |
|---|---|
| Planificación → Implementación | Generar plan en agente de planificación, luego handoff al agente de implementación |
| Implementación → Revisión | Completar implementación, luego handoff al revisor de código |
| Tests fallidos → Tests pasando | Generar tests fallidos (fáciles de revisar), luego handoff para implementar el código que los pase |

### Definición en frontmatter

```markdown
---
description: Generate an implementation plan
tools: ['search', 'web']
handoffs:
  - label: Start Implementation    # texto del botón
    agent: implementation          # agente destino
    prompt: Now implement the plan outlined above.  # prompt pre-rellenado
    send: false                    # si true, el prompt se envía automáticamente
    model: GPT-5.2 (copilot)       # modelo opcional para el handoff
---
```

### Comportamiento

- `send: false` (default) → el botón pre-rellena el prompt, el usuario lo revisa antes de enviar
- `send: true` → el prompt se envía automáticamente al seleccionar el botón

> **Diferencia clave con subagentes:** Los handoffs **transfieren el control al usuario** (flujo secuencial con revisión humana), mientras que los subagentes **delegan sin interrumpir** el flujo del agente principal (automatizado).

---

## 14. Formato Claude de Agentes

VS Code también detecta archivos `.md` en la carpeta `.claude/agents/`, siguiendo el formato de Claude sub-agents. Esto permite usar las **mismas definiciones de agentes** tanto en VS Code como en Claude Code.

### Propiedades del formato Claude

| Propiedad | Descripción |
|---|---|
| `name` | Nombre del agente (requerido) |
| `description` | Qué hace el agente |
| `tools` | String separado por comas con herramientas permitidas (ej. `"Read, Grep, Glob, Bash"`) |
| `disallowedTools` | String separado por comas con herramientas bloqueadas |

> VS Code **mapea los nombres de herramientas de Claude** a las herramientas equivalentes de VS Code. Se soporta tanto el formato `.agent.md` (arrays YAML para tools) como el formato Claude (strings separados por comas).

### Ejemplo en formato Claude

```markdown
---
name: CodeAnalyzer
description: Analyzes code quality and patterns
tools: Read, Grep, Glob
disallowedTools: Bash, Write
---

Analyzes the provided code for quality issues, patterns, and improvements.
```

---

## 15. Sistema de Memoria en Agentes

VS Code soporta dos sistemas de memoria complementarios que los agentes pueden utilizar:

### 15.1 Memory Tool (local, en máquina)

Tres scopes organizados en `/memories/`:

| Scope | Path | Persistencia | Contenido |
|---|---|---|---|
| **Usuario** | `/memories/` | Permanente, todos los workspaces | Preferencias, patrones comunes, insights generales. Las primeras 200 líneas se cargan automáticamente en cada sesión |
| **Repositorio** | `/memories/repo/` | Permanente, workspace actual | Convenciones del codebase, comandos de build, estructura del proyecto |
| **Sesión** | `/memories/session/` | Temporal, se borra al terminar la conversación | Contexto específico de la tarea en curso, notas de trabajo en progreso |

### 15.2 Copilot Memory (GitHub-hosted)

- Sistema de memoria alojado en GitHub
- Captura insights específicos del repositorio entre sesiones de Copilot
- Compartido entre superficies de GitHub Copilot (coding agent, code review, CLI)
- Va más allá de VS Code

---

## 16. Consideraciones de Seguridad

### Principio de mínimo privilegio en agentes

Los agentes personalizados pueden **restringir qué herramientas están disponibles**, dando control sobre qué puede hacer la IA.

**Recomendaciones:**

1. **Agentes de solo lectura** para flujos sensibles (planificación, revisión, análisis) — previene modificaciones accidentales
2. **Revisar la lista de tools e instrucciones** antes de compartir agentes en un repositorio
3. **`disable-model-invocation: true`** para agentes con permisos elevados (ej. acceso a BD, operaciones destructivas)
4. **`agents: []`** en agentes que no deben delegar a subagentes — previene escalada de privilegios indirecta
5. **Separar herramientas por rol:** coordinador puede tener `edit`, pero sus trabajadores solo `read` + `search`

### Ejemplo de agente de solo lectura seguro

```markdown
---
name: SecurityAuditor
user-invocable: false
disable-model-invocation: false
tools: ['read', 'search']
---
Auditas el código en busca de vulnerabilidades del OWASP Top 10.
NO tienes herramientas de edición ni ejecución. Solo analizas y reportas.
```

---

## 17. Buenas Prácticas Extraídas

### Para el diseño de subagentes

1. **Definir explícitamente cuándo usar subagentes** en las instrucciones del agente — no promtear manualmente cada vez. Los coordinadores deben tener instrucciones claras de delegation.

2. **Describir con claridad la tarea y el output esperado** para que el subagente no devuelva contexto innecesario al agente principal. La concisión del resultado importa.

3. **Prompt de subagente = solo la subtarea relevante** — no pasar el historial completo ni contexto irrelevante.

### Para la visibilidad y control

4. **`user-invocable: false`** para agentes internos/trabajadores que no deberían aparecer en el dropdown del usuario. Mantiene la UI limpia.

5. **`agents: [lista específica]`** cuando el coordinador solo debe usar subagentes determinados. Evita que el LLM seleccione un agente incorrecto si hay agentes con nombres/descripciones similares.

### Para el rendimiento y costos

6. **Asignar modelo más ligero a trabajadores** con foco estrecho — no necesitan el modelo más potente. Los modelos económicos son suficientes para tareas específicas.

7. **Ejecutar en paralelo** cuando las tareas son independientes. No esperar a que A termine para lanzar B si no hay dependencia entre ellos.

### Para la calidad de resultados

8. **Revisión multi-perspectiva en paralelo**: estructurar cada perspectiva como subagente independiente para evitar **anclaje cognitivo** entre perspectivas.

9. **Iterar entre fases** cuando hay dependencia: el coordinador debe ciclar Planner↔Architect y Implementer↔Reviewer hasta que cada fase converja.

---

## 18. Aplicabilidad para SAC

### Mapeo de capacidades VS Code → SAC

| Capacidad VS Code | Oportunidad en SAC |
|---|---|
| `user-invocable: false` | Agentes internos/auxiliares que no deben aparecer al usuario final (ej. Cronista de Cambios) |
| `agents: [lista]` | Definir en cada agente SAC qué otros agentes puede convocar — evita invocaciones incorrectas |
| Patrón Coordinador+Trabajadores | Agente orquestador que delega a Arquitecto ONAD, Desarrollador, DevOps, Analista de Requisitos |
| Revisión multi-perspectiva en paralelo | Validación de HUs desde múltiples ángulos simultáneamente (negocio, técnico, seguridad) |
| Subagente de investigación | Precargar contexto del proyecto antes de una sesión de refinamiento de HU |
| `disable-model-invocation: true` | Proteger agentes SAC con permisos sensibles de invocación no autorizada |
| Handoffs | Flujo guiado: Planificación → Refinamiento → Implementación → Revisión |
| Memory tool | Persistir contexto del proyecto (stack, patrones, ADRs) entre sesiones |
| Formato Claude | Compatibilidad con Claude Code para los mismos agentes SAC |

### Estado actual de `agents` en SAC

| Agente | Puede invocar a | Notas |
|---|---|---|
| **Arquitecto** | `Analista de Requisitos`, `Desarrollador`, `DevOps`, `Cronista de Cambios` | Consulta al Analista para correcciones al refinamiento antes de decisiones técnicas |
| **Analista de Requisitos** | `Arquitecto`, `Desarrollador`, `Cronista de Cambios`, `DevOps` | Coordinación completa del ciclo de HU |
| **Desarrollador** | `Analista de Requisitos`, `Arquitecto`, `Cronista de Cambios`, `DevOps` | Lanza subagente Analista para validar CA en paralelo mientras avanza a la siguiente tarea |
| **DevOps** | `Cronista de Cambios`, `Analista de Requisitos`, `Arquitecto`, `Desarrollador` | — |
| **Cronista de Cambios** | `Desarrollador`, `DevOps` | `user-invocable: false` — solo accesible como subagente |

### Patrón SAC: Validación de CA en Paralelo (Desarrollador → Analista)

El Desarrollador lanza al Analista de Requisitos como subagente para verificar que una tarea completada cumple los CA, **sin bloquear** el avance a la siguiente tarea.

```
Desarrollador
    │
    ├─► completa Tarea 1
    │       │
    │       └──► lanza subagente Analista
    │                ("Verifica que Tarea 1 cumple CA: [lista de CA]")
    │                   │ (corre en paralelo, contexto aislado)
    │
    ├─► empieza Tarea 2  ◄── contexto limpio, sin acumulación de validación
    │
    │◄──── Analista devuelve: ✅ cumple CA / ❌ fallo en CA [detalle]
    │
    └─► si hay fallo → corrige antes de continuar con Tarea 3
```

**Ventajas:**
- El Desarrollador no bloquea su contexto esperando validación funcional
- El Analista revisa con perspectiva funcional pura, sin el sesgo de quien implementó
- Los CA se verifican frescos, tarea a tarea, no como afterthought al final del sprint

**Consideración importante:** si la Tarea 2 depende directamente de la Tarea 1, priorizar la corrección antes de continuar. Las tareas independientes pueden validarse sin riesgo de encadenamiento roto.

### Acciones pendientes en el sistema SAC

#### ✅ Completadas

1. ~~Añadir propiedad `agents`~~ — ya implementada en todos los agentes
2. ~~`user-invocable: false` al Cronista de Cambios~~ — aplicado
3. ~~Añadir `Analista de Requisitos` al `agents` del Arquitecto~~ — aplicado
4. ~~Añadir `Analista de Requisitos` al `agents` del Desarrollador~~ — aplicado

#### 🟡 Media prioridad

5. **Definir handoffs** entre los agentes del ciclo de vida de una HU (refinamiento → planificación → implementación → revisión).

6. **Diseñar un agente coordinador** de nivel superior que orqueste el flujo completo de una HU usando los agentes SAC existentes como trabajadores.

7. **Añadir `disable-model-invocation: true`** al Arquitecto ONAD u otros agentes con permisos sensibles para protegerlos de invocación no controlada.

#### 🟢 Baja prioridad

8. **Explorar compatibilidad con formato Claude** para los agentes SAC más utilizados, ubicándolos también en `.claude/agents/`.

---

## 19. Referencia Rápida de Frontmatter Completo

```markdown
---
# IDENTIDAD
name: "Nombre del Agente"
description: "Descripción breve (placeholder en el chat)"
argument-hint: "Texto de ayuda para el usuario (ej. 'Describe el feature a implementar')"

# MODELO
model: "Claude Sonnet 4.6 (copilot)"
# o lista priorizada:
# model: ['Claude Haiku 4.5 (copilot)', 'Gemini 3 Flash (Preview) (copilot)']

# HERRAMIENTAS
tools: ['agent', 'read', 'search', 'edit', 'run']
# Incluir 'agent' para poder usar subagentes

# CONTROL DE SUBAGENTES
agents: ['Agente1', 'Agente2']   # lista específica
# agents: '*'                    # todos (default)
# agents: []                     # ninguno

# VISIBILIDAD Y ACCESO
user-invocable: true              # false = solo accessible como subagente
disable-model-invocation: false   # true = no puede ser invocado como subagente

# HANDOFFS (flujos secuenciales guiados)
handoffs:
  - label: "Ir a Implementación"
    agent: implementacion
    prompt: "Implementa el plan descrito arriba."
    send: false           # true = auto-envía el prompt
    model: "GPT-5.2 (copilot)"   # modelo opcional para el handoff

# DESTINO
target: vscode            # o 'github-copilot'
---

## Instrucciones del agente (cuerpo Markdown)

Instrucciones detalladas aquí.
Referenciar herramientas con #tool:<nombre>.
Referenciar archivos con links de Markdown.
```

---

## Recursos Relacionados

- [Agents overview](https://code.visualstudio.com/docs/copilot/agents/overview) — Tipos de agentes en VS Code
- [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents) — Crear agentes personalizados
- [Agents concepts](https://code.visualstudio.com/docs/copilot/concepts/agents#_subagents) — Loop agéntico, memoria, planificación
- [Chat sessions](https://code.visualstudio.com/docs/copilot/chat/chat-sessions) — Gestión de sesiones de chat

---

*Documento generado a partir del análisis exhaustivo de la documentación oficial de VS Code Copilot Subagents y fuentes relacionadas (abril 2026)*
