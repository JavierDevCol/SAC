# Sistema de Configuración

1. Al iniciar, cargar `CONFIG_SYSTEM.yaml` desde `{project-root}/.SAC/config/` y mantenerlo en contexto
2. Interpretar toda variable con sintaxis `{{seccion.clave}}` buscando en CONFIG_SYSTEM.yaml → seccion → clave
3. Cargar `CONFIG_USER` desde `{{archivos.config_user}}`
4. Comunicación en idioma `{{idiomas.comunicacion}}`

---

## Comportamiento Base

5. Seguir instrucciones exactamente como se especifican
6. Ejecutar pasos en orden especificado
7. Pasos obligatorios **NO** se pueden omitir
8. Si `{{usuario.nombre}}` está definido, dirigirse al usuario por su nombre

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
- En multi-proyecto: cargar contexto solo cuando se trabaje en ese proyecto o cuando se requiera. 

**Condición:** Si **NO** existe `{{archivos.workspace}}`

**Acciones:**
- Informar: "⚠️ No se encontró workspace del proyecto. Recomiendo ejecutar `>tomar_contexto`"

### Paso: Cargar Reglas Arquitectónicas ✅ Obligatorio

**Condición:** Si **existe** `{{archivos.reglas_arquitectonicas}}`

**Acciones:**
- Cargar `{{archivos.reglas_arquitectonicas}}`
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
| Backlog (índice) | `{{archivos.backlog}}` | Resumen compacto de todas las HUs | Leer SOLO el Índice Rápido y Resumen de Estados |

#### Consulta de HU Específica (búsqueda dirigida)

Cuando se necesite el detalle completo de una HU:

1. Leer `{{artifacts.hu_folder}}/[ID-HU]/HU.md` para metadata básica
2. Leer `{{artifacts.hu_folder}}/[ID-HU]/Refinamiento.md` si se necesita detalle técnico
3. Leer `{{artifacts.hu_folder}}/[ID-HU]/Plan.md` si se necesita plan de implementación
4. **NUNCA leer el backlog completo para consultar una sola HU**

#### Carga Bajo Demanda (solo cuando se necesite)

| Artifact | Ruta | Cargar cuando... |
|----------|------|------------------|
| HU específica | `{{artifacts.hu_folder}}/[ID-HU]/HU.md` | Se trabaje en esa HU |
| Refinamiento | `{{artifacts.hu_folder}}/[ID-HU]/Refinamiento.md` | Se requiera detalle técnico |
| Plan | `{{artifacts.hu_folder}}/[ID-HU]/Plan.md` | Se ejecute o consulte implementación |
| Tracking | `{{artifacts.hu_folder}}/[ID-HU]/Tracking.md` | Se retome o verifique ejecución |
| ADR | `{{artifacts.adr_folder}}` | Se consulte decisión arquitectónica |
| Bugs | `{{artifacts.hu_folder}}/BUG-NNN/` | Se registre, consulte o resuelva un bug |
| Pendientes (índice) | `{{artifacts.pendientes}}` | Se consulte deuda técnica o hallazgos |
| Pendientes (detalle) | `{{artifacts.pendientes_folder}}` | Se necesite contexto extendido |
| Deuda Técnica | `{{artifacts.deuda_tecnica_folder}}` | Se registre o consulte deuda técnica |

---

## Resumen de Contexto Disponible

Tras la inicialización, el agente tiene en memoria:

| Recurso | Estado | Uso |
|---------|--------|-----|
| Workspace | ✅ Cargado | Índice de proyectos, tipo (mono/multi) |
| Reglas arquitectónicas | ✅ Cargado | Nomenclatura, patrones, testing |
| Backlog (índice) | ✅ Cargado | **Índice Rápido** - Estados, prioridades (tabla compacta) |

**Importante:** Para **crear/guardar archivos**, usar sintaxis `{{seccion.variable}}` para obtener rutas. Para **consultar**, usar referencias del Workspace/Backlog.

---

## Ejecución de Herramientas

### Al Ejecutar una Herramienta (Ejecutar en Orden)

1. ✅ Identificar herramienta por comando en la tabla de herramientas del agente
2. ✅ Cargar instrucciones desde el archivo de la herramienta en `{{rutas.herramientas_folder}}/[comando].tool.yaml`
   - Ejemplo: `tomar contexto` → `{{rutas.herramientas_folder}}/tomar_contexto.tool.yaml`
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

---

## Comandos Universales

| Comando | Descripción |
|---------|-------------|
| `menu` | Mostrar herramientas disponibles |

