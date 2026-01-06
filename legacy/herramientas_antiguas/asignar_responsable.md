#  Herramienta: Asignar Responsable

## Descripción
Analiza una lista de tareas generadas y asigna automáticamente el **rol más adecuado** y la **herramienta óptima** para ejecutar cada tarea, basándose en las capacidades y especialidades de cada agente del sistema Cochas.

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## Cuándo Usar Esta Herramienta

- Después de completar una tarea que generó múltiples subtareas
- Al recibir una lista de requerimientos que deben distribuirse entre roles
- Cuando se necesita planificar la ejecución de un proyecto completo
- Para optimizar la asignación de trabajo entre los agentes disponibles

---

## Entrada Esperada

### Contexto Requerido:
1. **Lista de tareas a asignar** (descripción, prioridad, dependencias)
2. **Roles disponibles en el sistema** (leer de `/personas/roles-activos.md` la seccion `# Roles Activos del Sistema`)
3. **Herramientas disponibles por rol** (leer de cada archivo de rol)
4. **Contexto del proyecto actual** (de `session_state.json`)

### Formato de Tareas a Analizar:
```json
{
  "tareas_sin_asignar": [
    {
      "id": "TEMP-001",
      "descripcion": "Implementar autenticación con JWT",
      "tipo": "implementacion",
      "complejidad": "media",
      "keywords": ["jwt", "autenticación", "spring security"],
      "estimacion_horas": 8,
      "dependencias": []
    },
    {
      "id": "TEMP-002",
      "descripcion": "Configurar pipeline de CI/CD con GitHub Actions",
      "tipo": "infraestructura",
      "complejidad": "alta",
      "keywords": ["ci/cd", "github actions", "deploy"],
      "estimacion_horas": 6,
      "dependencias": ["TEMP-001"]
    }
  ]
}
```

---

## Proceso de Ejecución

### Paso 1: Cargar Matriz de Capacidades

Leer todos los archivos en `/personas/roles-activos.md` y extraer:

```json
{
  "roles_disponibles": {
    "onad": {
      "nombre": "Arquitecto Onad",
      "comando": "onad",
      "especialidad": ["arquitectura", "diseño", "decisiones estratégicas"],
      "keywords": ["microservicios", "patrones", "trade-offs", "adr"],
      "herramientas": ["tomar_contexto", "define_arquitectura", "generar_adr"],
      "tipo_tareas": ["diseño", "análisis", "decisiones"]
    },
    "archdev": {
      "nombre": "ArchDev Pro",
      "comando": "archdev",
      "especialidad": ["implementación", "código", "refactorización"],
      "keywords": ["spring", "java", "tests", "tdd", "clean code"],
      "herramientas": ["refactorizar", "crear_pruebas", "analizar_code_smells", "solucionar_smells"],
      "tipo_tareas": ["implementacion", "refactoring", "testing"]
    },
    "devops": {
      "nombre": "Arquitecto DevOps",
      "comando": "devops",
      "especialidad": ["infraestructura", "ci/cd", "deployment"],
      "keywords": ["pipeline", "docker", "kubernetes", "terraform"],
      "herramientas": ["diagnosticar_devops"],
      "tipo_tareas": ["infraestructura", "deploy", "monitoreo"]
    },
    "artesano": {
      "nombre": "Artesano de Commits",
      "comando": "artesano",
      "especialidad": ["documentación", "commits", "conventional commits"],
      "keywords": ["git", "commit", "changelog", "semver"],
      "herramientas": ["generar_commit"],
      "tipo_tareas": ["documentacion", "versionado"]
    },
    "refinador": {
      "nombre": "Refinador HU",
      "comando": "refinador",
      "especialidad": ["historias de usuario", "criterios aceptación"],
      "keywords": ["user story", "gherkin", "bdd", "criterios"],
      "herramientas": ["refinar_hu"],
      "tipo_tareas": ["refinamiento", "especificacion"]
    }
  }
}
```

### Paso 2: Analizar Cada Tarea

Para cada tarea sin asignar:

1. **Extraer keywords** de la descripción
2. **Calcular score de compatibilidad** con cada rol:
   ```
   Score = (keywords_match * 0.5) + (tipo_tarea_match * 0.3) + (herramientas_disponibles * 0.2)
   ```
3. **Identificar herramientas aplicables** del rol con mayor score
4. **Asignar rol + herramienta óptima**

### Paso 3: Generar Asignaciones

```json
{
  "asignaciones": [
    {
      "tarea_id": "TEMP-001",
      "id_asignado": "ARCHDEV-001",
      "rol_asignado": "archdev",
      "rol_nombre": "ArchDev Pro",
      "herramienta_sugerida": "crear_pruebas",
      "score_compatibilidad": 0.85,
      "justificacion": "Implementación de autenticación requiere código robusto con tests. ArchDev Pro tiene experiencia en Spring Security y TDD.",
      "alternativas": [
        {
          "rol": "onad",
          "score": 0.45,
          "razon": "Podría diseñar la arquitectura, pero no implementa código"
        }
      ]
    },
    {
      "tarea_id": "TEMP-002",
      "id_asignado": "DEVOPS-001",
      "rol_asignado": "devops",
      "rol_nombre": "Arquitecto DevOps",
      "herramienta_sugerida": "diagnosticar_devops",
      "score_compatibilidad": 0.95,
      "justificacion": "Pipeline de CI/CD es responsabilidad directa de DevOps. Tiene experiencia en GitHub Actions.",
      "alternativas": []
    }
  ],
  "resumen": {
    "total_tareas_analizadas": 2,
    "asignaciones_realizadas": 2,
    "distribucion_por_rol": {
      "archdev": 1,
      "devops": 1
    }
  }
}
```

### Paso 4: Actualizar `session_state.json`

Transformar las tareas temporales en tareas asignadas:

```json
{
  "tablero_tareas": {
    "tareas": [
      {
        "id": "ARCHDEV-001",
        "descripcion": "Implementar autenticación con JWT",
        "estado": "pendiente",
        "prioridad": "alta",
        "rol_asignado": "archdev",
        "rol_origen": "onad",
        "herramienta_sugerida": "crear_pruebas",
        "estimacion_horas": 8,
        "dependencias": [],
        "criterios_aceptacion": [
          "Endpoints: POST /register, POST /login, GET /validate-token",
          "JWT con refresh token",
          "Tests de integración completos"
        ],
        "asignacion_automatica": true,
        "score_compatibilidad": 0.85
      }
    ]
  }
}
```

---

## Salida Esperada

### Formato Visual para el Usuario:

```markdown
##  Asignación de Responsables

Analicé **2 tareas** y realicé las siguientes asignaciones:

---

### 1. Implementar autenticación con JWT
**ID Asignado:** ARCHDEV-001  
**Rol:** ArchDev Pro (`archdev`)  
**Herramienta Sugerida:** `crear_pruebas`  
**Compatibilidad:** 85%  
**Estimación:** 8h  

**Justificación:**
Implementación de autenticación requiere código robusto con tests. ArchDev Pro tiene experiencia en Spring Security y TDD.

**Alternativas Consideradas:**
- Arquitecto Onad (45%) - Podría diseñar la arquitectura, pero no implementa código

---

### 2. Configurar pipeline de CI/CD
**ID Asignado:** DEVOPS-001  
**Rol:** Arquitecto DevOps (`devops`)  
**Herramienta Sugerida:** `diagnosticar_devops`  
**Compatibilidad:** 95%  
**Estimación:** 6h  

**Justificación:**
Pipeline de CI/CD es responsabilidad directa de DevOps. Tiene experiencia en GitHub Actions.

---

##  Resumen de Distribución

| Rol | Tareas Asignadas | Horas Estimadas |
|-----|------------------|-----------------|
| ArchDev Pro | 1 | 8h |
| Arquitecto DevOps | 1 | 6h |

**Total:** 2 tareas, 14h estimadas

---

##  Próximos Pasos

1. Ejecutar `@switch archdev` para iniciar ARCHDEV-001
2. Al completar, ejecutar `@switch devops` para DEVOPS-001

Las asignaciones se han guardado en `session_state.json` y `sesion_{fecha}_resumen.md`.
```

---

## Validaciones

### Validación 1: Roles Disponibles

- Verificar que todos los archivos en `/personas/` son accesibles
- Si algún rol referenciado no existe  advertir y excluir de matriz

### Validación 2: Herramientas Disponibles

- Verificar que las herramientas sugeridas existen en `/herramientas/`
- Si no existe  sugerir alternativa o marcar como "sin herramienta específica"

### Validación 3: Dependencias Circulares

- Detectar si hay dependencias circulares en las tareas asignadas
- Si se detectan  advertir y sugerir reorganización

### Validación 4: Carga de Trabajo

- Calcular carga total por rol (horas estimadas)
- Si un rol tiene > 40h asignadas  advertir sobre posible sobrecarga
- Sugerir redistribución si es posible

---

## Casos Especiales

### Caso 1: Tarea Sin Rol Compatible

Si ningún rol tiene score > 0.3:

```markdown
 **Tarea sin rol compatible detectada:**

**TEMP-003:** Crear modelo de ML para recomendaciones

**Problema:** Ningún rol actual tiene especialidad en Machine Learning.

**Sugerencia:** 
- Crear nuevo rol especializado
- Delegar a servicio externo
- Rediseñar la tarea para usar capacidades actuales
```

### Caso 2: Múltiples Roles con Score Similar

Si 2+ roles tienen score  0.7:

```markdown
? **Asignación Ambigua Detectada:**

**TEMP-004:** Refinar criterios de aceptación

**Candidatos:**
1. Refinador HU (75%) - Especialista en historias de usuario
2. Arquitecto Onad (72%) - Puede definir criterios técnicos

**Decisión:** Asignado a Refinador HU por especialización directa.

**Recomendación:** Considerar colaboración entre ambos roles.
```

### Caso 3: Tarea Multidisciplinaria

Si la tarea requiere múltiples especialidades:

```markdown
 **Tarea Multidisciplinaria Detectada:**

**TEMP-005:** Implementar sistema de pagos completo

**Requiere:**
- Arquitecto Onad: Diseño de arquitectura segura
- ArchDev Pro: Implementación con tests
- Arquitecto DevOps: Configuración de entorno PCI-DSS

**Estrategia:** Dividir en 3 subtareas:
- ONAD-003: Diseñar arquitectura de pagos (4h)
- ARCHDEV-002: Implementar integración con Stripe (10h)
- DEVOPS-002: Configurar entorno seguro (6h)
```

---

## Ejemplo de Uso Completo

### Usuario:
```
He terminado el diseño de arquitectura. Generé estas tareas para el proyecto:
1. Implementar API REST de productos
2. Crear tests de integración
3. Configurar base de datos PostgreSQL
4. Configurar Redis para cache
5. Crear pipeline de CI/CD
6. Generar commits siguiendo conventional commits
```

### Rol Activo (Onad):
```
 Analizando tareas y asignando responsables...

[Ejecuta herramienta: asignar_responsable]
```

### Salida:
```markdown
##  Asignación de Responsables

Analicé **6 tareas** y realicé las siguientes asignaciones:

[Tabla con todas las asignaciones]

##  Resumen de Distribución

| Rol | Tareas | Horas |
|-----|--------|-------|
| ArchDev Pro | 3 | 24h |
| Arquitecto DevOps | 2 | 12h |
| Artesano de Commits | 1 | 2h |

Las asignaciones se han guardado en `session_state.json`.

¿Deseas iniciar con la primera tarea (ARCHDEV-001)?
```

---

## Integración con Otros Componentes

### Con `session_state.json`:
- Lee tareas temporales de `tareas_sin_asignar`
- Escribe asignaciones en `tablero_tareas`
- Actualiza `metadata` con distribución de carga

### Con `sesion_{fecha}_resumen.md`:
- Genera sección "Asignaciones Automáticas"
- Documenta justificaciones de asignación
- Incluye métricas de distribución

### Con Comando `@switch`:
- Al cambiar de rol, muestra tareas asignadas a ese rol
- Sugiere qué tarea ejecutar primero según prioridad y dependencias

---

## Notas de Implementación

**Algoritmo de Scoring:**

```javascript
function calcularScore(tarea, rol) {
  let score = 0;
  
  // Keywords match (50%)
  const keywordsMatch = tarea.keywords.filter(k => 
    rol.keywords.includes(k)
  ).length / tarea.keywords.length;
  score += keywordsMatch * 0.5;
  
  // Tipo de tarea match (30%)
  const tipoMatch = rol.tipo_tareas.includes(tarea.tipo) ? 1 : 0;
  score += tipoMatch * 0.3;
  
  // Herramientas disponibles (20%)
  const herramientasMatch = rol.herramientas.length > 0 ? 1 : 0;
  score += herramientasMatch * 0.2;
  
  return score;
}
```

**Priorización de Asignaciones:**

1. Tareas sin dependencias primero
2. Tareas con alta compatibilidad (score > 0.8)
3. Tareas de prioridad alta
4. Distribución equitativa de carga

---

## Métricas de Éxito

-  Score de compatibilidad > 0.7 en todas las asignaciones
-  Carga balanceada entre roles (desviación estándar < 20%)
-  Sin dependencias circulares
-  100% de tareas asignadas (o justificadas si no se asignan)
