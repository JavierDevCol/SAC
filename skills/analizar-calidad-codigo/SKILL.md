---
name: analizar-calidad-codigo
description: Analiza calidad de código: detecta code smells clásicos y verifica cumplimiento de reglas arquitectónicas del proyecto. Soporta scopes commits, project y archivo. Ejecuta esta skill después de implementar para validar calidad o antes de un release para auditoría completa.
---

## Parámetros

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `--scope` | string | `commits` | Qué archivos analizar |
| `--archivo` | string | — | Ruta específica (requerido si scope=archivo) |
| `--modo` | string | `todos` | Qué análisis ejecutar |

### Scope — Qué archivos analizar

| Scope | Qué analiza | Cuándo usar |
|-------|-------------|-------------|
| `commits` | Solo archivos cambiados en la rama actual (desde su creación) | Después de implementar una task/HU |
| `project` | Todos los archivos del proyecto | Auditoría completa pre-release |
| `archivo` | Un archivo específico | Revisar un archivo concreto |

### Modo — Qué análisis ejecutar

| Modo | Qué verifica | Sub-agente |
|------|--------------|------------|
| `smells` | Code smells clásicos: Long Method, God Object, Feature Envy, Duplicate Code, etc. | `assets/prompt-analisis-smells.md` + `assets/catalogo-smells.md` |
| `arquitectura` | Cumplimiento de reglas: nomenclatura, patrones, SOLID, estructura de carpetas | `assets/prompt-analisis-arquitectura.md` + reglas del proyecto |
| `todos` | Ambos análisis en paralelo | Ambos prompts |

### Combinaciones

| Comando | Scope | Modo | Resultado |
|---------|-------|------|-----------|
| `>analizar-calidad-codigo` | commits | todos | Ambos análisis en cambios de rama |
| `>analizar-calidad-codigo --scope project` | project | todos | Ambos análisis en proyecto completo |
| `>analizar-calidad-codigo --scope commits --modo smells` | commits | smells | Solo code smells en cambios |
| `>analizar-calidad-codigo --scope archivo X --modo arquitectura` | archivo | arquitectura | Solo reglas en un archivo |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.reglas_arquitectonicas`
- Leer `.SAC/config/CONFIG_USER.yaml` (si existe)

**Mostrar configuración al usuario:**
```
⚙️ Configuración del análisis:
- Scope: [commits/project/archivo]
- Modo: [smells/arquitectura/todos]
- Archivos a analizar: [lista o "todos"]
- Reglas arquitectónicas: [configuradas / no configuradas]
```

### 2. Determinar Archivos a Analizar

**Si scope=commits:**
- Ejecutar `git log --oneline main..HEAD` para obtener commits
- Ejecutar `git diff main..HEAD --name-only` para obtener archivos cambiados
- Analizar SOLO esos archivos

**Si scope=project:**
- Escanear todos los archivos del proyecto
- Excluir: node_modules, .git, .SAC, build, dist, vendor

**Si scope=archivo:**
- Verificar que el archivo existe
- Analizar solo ese archivo

### 3. Ejecutar Análisis (Sub-agentes en paralelo)

**Si modo INCLUYE smells:**
- Cargar prompt desde `assets/prompt-analisis-smells.md`
- Cargar catálogo desde `assets/catalogo-smells.md`
- Pasar ambos al sub-agente junto con los archivos a analizar
- Sub-agente analiza código contra catálogo
- Retorna: JSON con lista de smells

**Si modo INCLUYE arquitectura:**
- Cargar prompt desde `assets/prompt-analisis-arquitectura.md`
- Cargar reglas desde `{archivos.reglas_arquitectonicas}`
- Pasar ambos al sub-agente junto con los archivos a analizar
- Sub-agente verifica código contra reglas
- Retorna: JSON con lista de violaciones

### 4. Consolidar Resultados

- Unificar hallazgos de ambos análisis
- Eliminar duplicados
- Ordenar por severidad: Crítica → Alta → Media → Baja

### 5. Presentar Reporte

**Reporte compacto:**
```
📊 ANÁLISIS DE CALIDAD: [scope]
📁 Archivos analizados: [N]
🔍 Hallazgos: [X] Críticos | [Y] Altos | [Z] Medios | [W] Bajos

🐛 Code Smells:
| # | Tipo | Archivo | Línea | Severidad | Solución |
|---|------|---------|-------|-----------|----------|
| 1 | Long Method | AuthService.java | 45 | Alta | Extract Method |

📐 Arquitectura:
| # | Regla | Archivo | Línea | Violación |
|---|-------|---------|-------|-----------|
| 1 | nom_01 PascalCase | usuario_service.py | 12 | Nombre en snake_case |

💡 Top 3 recomendaciones:
1. [recomendación más impactante]
2. [segunda más impactante]
3. [tercera más impactante]
```

### 6. Ofrecer Corrección

> ¿Deseas que corrija estos hallazgos?
> - [S] Sí, corregir todos
> - [P] Seleccionar cuáles corregir
> - [N] No, solo era análisis

Si SÍ o P → Ejecutar correcciones (sub-agente con herramientas de edición)

## Code Smells (Catálogo)

| Categoría | Smell | Indicador | Solución |
|-----------|-------|-----------|----------|
| Bloaters | Long Method | >20 líneas | Extract Method |
| Bloaters | Large Class | >300 líneas o >10 métodos | Extract Class |
| Bloaters | Long Parameter List | >3 parámetros | Parameter Object |
| Bloaters | Data Clumps | Datos que aparecen juntos | Extract Class |
| OO Abusers | Feature Envy | Usa más datos de otra clase | Move Method |
| OO Abusers | Inappropriate Intimacy | Accede a internals de otras | Move Method/Field |
| Change Preventers | Divergent Change | Clase cambia por múltiples razones | Extract Class (SRP) |
| Change Preventers | Shotgun Surgery | Un cambio afecta múltiples clases | Move Method/Field |
| Dispensables | Dead Code | Código no ejecutado | Remove |
| Dispensables | Speculative Generality | Abstracciones no usadas | Collapse Hierarchy |
| Dispensables | Duplicate Code | Código repetido | Extract Method |
| Couplers | Message Chains | a.getB().getC().getD() | Hide Delegate |
| Couplers | Middle Man | Clase solo delega | Remove Middle Man |

## Reglas Arquitectónicas

Se cargan desde `{archivos.reglas_arquitectonicas}` si existen:

| Sección | Qué verifica |
|---------|--------------|
| nomenclatura.* | Convenciones de nombres (clases, métodos, variables) |
| arquitectura.estructura | Estructura de carpetas |
| patrones.obligatorios | Patrones que deben usarse |
| patrones.prohibidos | Patrones que NO deben usarse |
| principios.* | SOLID, inmutabilidad, nulls |
| calidad.* | Límites de código (líneas, parámetros) |

## Restricciones

- **NO** analizar archivos de configuración (.json, .yaml, .xml)
- **NO** analizar archivos generados (build, dist, node_modules)
- **Priorizar** hallazgos por severidad
- **Ofrecer** corrección siempre al final
- **Delegar** análisis a sub-agentes

## Formato de salida

**Análisis sin hallazgos:**
```
✅ ANÁLISIS DE CALIDAD COMPLETADO
📁 Archivos analizados: [N]
🎉 Sin hallazgos — código cumple estándares
```

**Análisis con hallazgos:**
```
⚠️ ANÁLISIS DE CALIDAD COMPLETADO
📁 Archivos analizados: [N]
🔍 Hallazgos: [X] Críticos | [Y] Altos | [Z] Medios | [W] Bajos

[reporte detallado]
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| No hay commits en la rama | Rama sin cambios | Usar scope project o archivo |
| Archivo no encontrado | Ruta incorrecta | Verificar ruta del archivo |
| Sin reglas arquitectónicas | No configuradas | Ejecutar >init_reglas_arquitectonicas |

## Después de ejecutar

- `>ejecutar-plan [ID-HU]` — Corregir hallazgos durante implementación
- `>init-reglas-arquitectonicas` — Configurar reglas si no existen
