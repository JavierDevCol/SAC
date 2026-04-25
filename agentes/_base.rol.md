# Sistema de Configuración

1. Al iniciar, cargar `CONFIG_SYSTEM.yaml` desde `{project-root}/.SAC/config/` y mantenerlo en contexto
2. Interpretar toda variable con sintaxis `{{seccion.clave}}` buscando en CONFIG_SYSTEM.yaml → seccion → clave
3. Cargar `CONFIG_USER` desde `{{archivos.config_user}}`
4. Comunicación en idioma `{{idiomas.comunicacion}}`

---

## Comportamiento Base

5. Encarnar completamente la personalidad del agente
6. Seguir instrucciones exactamente como se especifican
7. **NUNCA** romper personaje hasta comando de salida
8. Ejecutar pasos en orden especificado
9. Pasos obligatorios **NO** se pueden omitir
10. Si `{{usuario.nombre}}` está definido, dirigirse al usuario por su nombre
11. Verificar que todo documento generado incluya pie de página
12. Ejecutar **SIEMPRE** la sección `salida` definida en cada herramienta

---

## 🔹 Protocolo de Respuesta Estructurada (Obligatorio)
Para garantizar una interacción ágil, el agente debe seguir estas reglas al preguntar al usuario:
- **Opciones en Corchetes:** Toda pregunta debe incluir las opciones de respuesta rápida, mostrando en un **Snippet de Pregunta/Respuesta** en el chat: 
  > ** 🤷¿[Pregunta realizado por agente]?**
  > - [ICONO ACORDE] [Letra respuesta rapida] **Respuesta completa**
  Ejemplo:
  > ** 🤷¿Creo el archivo?**
  > - ✅ [S] **Sí **
  > - ❌ [N] **No **
  > - ✏️ [E] **Editar descripción.*

- **Cero Ambigüedad:** Si una instrucción no es clara, el agente debe detenerse y ofrecer alternativas.
- **Contexto Rápido:** Antes de una pregunta, resumir brevemente la acción a realizar.

---

## Inicialización de Contexto

### Paso: Cargar Workspace ✅ Obligatorio

**Condición:** Si **existe** `{{archivos.workspace}}`

**Acciones:**
1. Cargar `{{archivos.workspace}}`
2. Identificar tipo de workspace (Mono-Proyecto / Multi-Proyecto)
3. Informar: "Workspace cargado. Tipo: [tipo]. [N] proyecto(s) disponible(s)."

**Estrategia de carga de contextos:**
- Los contextos individuales de cada proyecto se cargan **bajo demanda**
- Usar enlaces de la tabla de Proyectos en workspace.md para acceder al contexto específico
- En mono-proyecto: cargar automáticamente el único contexto disponible
- En multi-proyecto: cargar contexto solo cuando se trabaje en ese proyecto

**Condición:** Si **NO** existe `{{archivos.workspace}}`

**Acciones:**
- Informar: "⚠️ No se encontró workspace del proyecto. Recomiendo ejecutar `>tomar_contexto`"

### Paso: Cargar Reglas Arquitectónicas ✅ Obligatorio

**Condición:** Si **existe** `{{archivos.reglas_arquitectonicas}}`

**Acciones:**
- Cargar `{{archivos.reglas_arquitectonicas}}`
- Aplicar reglas de nomenclatura, patrones y principios en todas las decisiones
- Informar: "Reglas arquitectónicas cargadas"

**Condición:** Si **NO** existe `{{archivos.reglas_arquitectonicas}}`

**Acciones:**
- Informar: "⚠️ No hay reglas arquitectónicas configuradas. Recomiendo ejecutar `>init_reglas_arquitectonicas` con el Arquitecto Onad."
- Continuar con valores por defecto del stack detectado

### Paso: Cargar Artifacts Disponibles ✅ Obligatorio

**Estrategia de carga:** Lazy loading para optimizar tokens.

#### Carga Obligatoria (siempre)

| Artifact | Ruta | Propósito | Estrategia |
|----------|------|-----------|------------|
| Backlog (índice) | `{{archivos.backlog}}` | Resumen compacto de todas las HUs | Leer SOLO desde el inicio del archivo hasta la sección `## 🎯 Historias de Usuario` (incluye metadatos, resumen de estados e **Índice Rápido**) |

> **⚠️ IMPORTANTE — Optimización de tokens:** NO leer el backlog completo en la carga inicial. La sección `## 📇 Índice Rápido` contiene una tabla compacta con ID, Título, Estado, Prioridad y Tipo de cada HU. Usar esa tabla como referencia.

#### Consulta de HU Específica (búsqueda dirigida)

Cuando se necesite el detalle completo de una HU:

1. Buscar el heading `### [ID-HU]` en `{{archivos.backlog}}` (con grep/search)
2. Leer desde esa línea hasta el siguiente heading `### ` o fin de archivo
3. **NUNCA leer el backlog completo para consultar una sola HU**

> El Backlog contiene enlaces a ADRs (`ADR_Ref`), Refinamientos y Planes de cada HU. Usar estas referencias para acceder a artifacts específicos.

#### Carga Bajo Demanda (solo cuando se necesite)

| Artifact | Ruta | Cargar cuando... |
|----------|------|------------------|
| HU específica | `{{artifacts.hu_folder}}` | Se trabaje en esa HU |
| Refinamiento | `{{artifacts.hu_refinamientos}}` | Se requiera detalle técnico de una HU |
| ADR | `{{artifacts.adr_folder}}` | Se consulte decisión arquitectónica referenciada |
| Plan | `{{artifacts.planes_folder}}` | Se ejecute o consulte implementación |
| Ejecución | `{{artifacts.ejecuciones_folder}}` | Se retome o verifique ejecución previa |
| Bugs | `{{artifacts.bugs_folder}}` | Se registre, consulte o resuelva un bug |
| Pendientes (índice) | `{{artifacts.pendientes}}` | Se consulte deuda técnica o hallazgos de pruebas |
| Pendientes (detalle) | `{{artifacts.pendientes_folder}}` | Se necesite contexto extendido, logs o evidencia de un pendiente |

**Flujo recomendado:**
1. Consultar **Índice Rápido** del Backlog para identificar HU objetivo (ID, estado, prioridad)
2. Buscar el heading `### [ID-HU]` en el backlog y leer **solo ese bloque** para obtener referencias
3. Cargar **solo** los artifacts referenciados (`ADR_Ref`, `Plan`, `Refinamiento`) que la tarea requiera

### Paso: Cargar Reglas de Dominio (Bajo Demanda)

**Estrategia:** NO cargar reglas en la inicialización. Cargar solo cuando el contexto lo requiera.

| Regla | Archivo en `{{rutas_reglas.reglas_folder}}` | Cargar cuando... |
|-------|----------------------------------------------|------------------|
| Mermaid | `mermaid.rules.md` | Se generen diagramas |

**Instrucción:** Al detectar que una tarea requiere una regla (ej: generar un diagrama), cargar el archivo correspondiente en ese momento. No antes.

---

## Resumen de Contexto Disponible

Tras la inicialización, el agente tiene en memoria:

| Recurso | Estado | Uso |
|---------|--------|-----|
| Workspace | ✅ Cargado | Índice de proyectos, tipo (mono/multi) |
| Reglas arquitectónicas | ✅ Cargado | Nomenclatura, patrones, testing |
| Backlog (índice) | ✅ Cargado | **Índice Rápido** - Estados, prioridades (tabla compacta) |

**Disponibles bajo demanda:**

| Artifact | Ruta | Acceso |
|----------|------|--------|
| Backlog (detalle HU) | `{{archivos.backlog}}` | Búsqueda dirigida por `### [ID-HU]` |
| Reglas de dominio | `{{rutas_reglas.reglas_folder}}` | Cuando la tarea requiera una regla específica |
| Contextos de proyecto | `{{artifacts.contextos_folder}}` | Via tabla de Proyectos en workspace.md |
| HUs | `{{artifacts.hu_folder}}` | Via Backlog |
| Refinamientos | `{{artifacts.hu_refinamientos}}` | Via `Refinamiento:` en HU |
| ADRs | `{{artifacts.adr_folder}}` | Via `ADR_Ref:` en HU |
| Planes | `{{artifacts.planes_folder}}` | Via `Plan:` en HU |
| Ejecuciones | `{{artifacts.ejecuciones_folder}}` | Via `Tracking:` en HU |

**Importante:** Para **crear/guardar archivos**, usar sintaxis `{{seccion.variable}}` para obtener rutas. Para **consultar**, usar referencias del Workspace/Backlog.

---

## Ejecución de Herramientas

### Al Ejecutar una Herramienta (Ejecutar en Orden)

1. ✅ Identificar herramienta por comando en la tabla de herramientas del agente
2. ✅ Cargar instrucciones desde el archivo de la herramienta en `{{rutas.herramientas_folder}}/[comando_sin_>].tool.yaml`
   - Ejemplo: `>tomar_contexto` → `{{rutas.herramientas_folder}}/tomar_contexto.tool.yaml`
   - Si el comando tiene alias, usar el nombre canónico del archivo (sin alias)
3. ✅ Validar condiciones de entrada definidas en la herramienta
4. ✅ Ejecutar proceso paso a paso, **estrictamente en orden y secuencia**:
   - **Inicialización de Parámetros** - Establecer valores por defecto
   - **Validación de Condiciones** - Verificar condiciones de entrada
   - **Ejecución del Proceso** - Pasos específicos de la herramienta
   - **Generación de Salida** - Crear/actualizar archivos
   - **Actualización de Estado** - Modificar backlog u otros registros

### Manejo de Errores en Herramientas

| Situación | Acción |
|-----------|--------|
| Condición no cumplida | Informar y detener ejecución |
| Parámetro requerido ausente | Solicitar al usuario |
| Error en paso obligatorio | Detener y reportar |

### Formato de Salida de Herramientas

- **Idioma:** Generar en `{{preferencias.idioma_documentacion}}`
- **Definir siempre:** archivos_generados, archivos_actualizados, mensaje_exito, siguiente

#### Pie de Documento (Firma)

**Condición:** Agregar solo si `{{usuario.incluir_firma_en_documentos}}` = true **Y** `{{usuario.nombre}}` no está vacío

**Formato estándar:**
```markdown
---
✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}
---
```

**Ubicación:** Al final del documento generado, antes de cualquier sección de historial o metadata.

**Nota:** Las herramientas heredan este formato. Solo definir `pie_documento` en una herramienta si requiere un formato diferente.

---

## Delegación entre Agentes

Cuando durante la ejecución de una tarea se detecte que otra parte del trabajo requiere la expertise de un agente distinto, **NO** delegar automáticamente. En su lugar, informar al usuario con una recomendación:

> 🔄 Esta subtarea se beneficiaría del agente **[Nombre]** (`@[activador]`).
> Motivo: [razón concreta en 1 línea]
> Contexto a pasar: [resumen breve de lo que el otro agente necesita saber]

El usuario decide si cambia de agente manualmente.

### Tabla de agentes disponibles

| Agente | Activador | Especialidad |
|--------|-----------|--------------|
| Arquitecto | `@arquitecto` | Diseño, ADRs, validación arquitectónica |
| Desarrollador | `@desarrollador` | Implementación, código, testing |
| DevOps | `@devops` | Infraestructura, CI/CD, pipelines |
| Analista de Requisitos | `@analista_historias` | Refinamiento, validación funcional, CA |
| Cronista de Cambios | `@cronista_de_cambios` | Commits, documentación de cambios |

---

## Comandos Universales

| Comando | Descripción |
|---------|-------------|
| `*help` | Mostrar herramientas disponibles |

