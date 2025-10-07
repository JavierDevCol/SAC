# 🛠️ Herramientas Potenciales para Artesano de Commits

> Documento de análisis y especificación de herramientas potenciales identificadas durante la refactorización del rol **Artesano de Commits**. Este documento sirve como referencia para futuras implementaciones o refactorizaciones de herramientas existentes.

---

## 📋 Índice

1. [Herramienta 1: `obtener_diff_git` (NUEVA)](#1-obtener_diff_git)
2. [Herramienta 2: `analizar_diff_contextual` (NUEVA)](#2-analizar_diff_contextual)
3. [Mejora a herramienta existente: `generar_commit`](#3-mejora-generar_commit)
4. [Catálogo de referencia: `conventional_commits_catalog.md`](#4-catalogo-conventional_commits_catalog)

---

## 1. `obtener_diff_git`

### 🎯 Propósito

Obtener automáticamente el `git diff` del repositorio actual, detectando el estado de los cambios (unstaged, staged, o commit reciente) y ejecutando el comando apropiado.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es esencial para el flujo del Artesano de Commits y potencialmente útil para otros roles que necesiten analizar cambios de código.

### 🔍 Problema que Resuelve

- **Antes:** El usuario debe salir del chat, ejecutar `git diff` manualmente, copiar el resultado y pegarlo
- **Después:** La herramienta lo obtiene automáticamente según el estado del repositorio

### 📥 Input Esperado

**Parámetros:**
- `tipo_cambios` (enum, requerido): 
  - `unstaged` - Cambios modificados pero no agregados con `git add`
  - `staged` - Cambios ya agregados al staging area con `git add`
  - `ultimo_commit` - Mostrar el último commit realizado
  - `auto` - Detectar automáticamente qué tipo de cambios existen (prioridad: staged > unstaged)

- `ruta_repositorio` (string, opcional): Path al repositorio Git. Default: directorio actual

- `incluir_contexto` (boolean, opcional): Si es true, incluye información adicional como:
  - Rama actual
  - Archivos modificados (listado)
  - Estado del repositorio (limpio, sucio, conflictos)
  
  Default: `true`

**Ejemplo de invocación:**
```
> obtener_diff_git tipo_cambios=staged incluir_contexto=true
```

### 📤 Output Esperado

**Formato: JSON + Diff en texto plano**

```json
{
  "exito": true,
  "tipo_cambios_detectado": "staged",
  "contexto_repositorio": {
    "rama_actual": "feature/auth-refactor",
    "archivos_modificados": [
      "src/services/AuthService.java",
      "src/services/JwtValidatorService.java",
      "test/AuthServiceTest.java"
    ],
    "estado": "limpio",
    "total_archivos_modificados": 3,
    "lineas_agregadas": 45,
    "lineas_eliminadas": 12
  },
  "comando_ejecutado": "git diff --cached",
  "diff_completo": "diff --git a/src/services/AuthService.java b/src/services/AuthService.java\nindex 1a2b3c4..5d6e7f8 100644\n--- a/src/services/AuthService.java\n+++ b/src/services/AuthService.java\n@@ -10,8 +10,15 @@ public class AuthService {\n+    private final JwtValidatorService validator;\n..."
}
```

**Si no hay cambios:**
```json
{
  "exito": false,
  "mensaje": "No se encontraron cambios en el estado 'staged'. ¿Los cambios están en 'unstaged' o ya fueron commiteados?",
  "sugerencia": "Intenta con tipo_cambios=unstaged o tipo_cambios=ultimo_commit"
}
```

### 🔧 Lógica Interna Sugerida

1. **Validar que estamos en un repositorio Git:**
   ```bash
   git rev-parse --is-inside-work-tree
   ```
   - Si falla → retornar error: "No se detectó un repositorio Git en el directorio actual"

2. **Según el tipo_cambios, ejecutar:**

   **Si `tipo_cambios=unstaged`:**
   ```bash
   git diff
   ```

   **Si `tipo_cambios=staged`:**
   ```bash
   git diff --cached
   ```

   **Si `tipo_cambios=ultimo_commit`:**
   ```bash
   git show HEAD
   ```

   **Si `tipo_cambios=auto`:**
   - Primero verificar si hay cambios staged:
     ```bash
     git diff --cached --quiet
     ```
     Si el exit code es 1, hay cambios staged → usar `git diff --cached`
   
   - Si no hay staged, verificar unstaged:
     ```bash
     git diff --quiet
     ```
     Si el exit code es 1, hay cambios unstaged → usar `git diff`
   
   - Si no hay ninguno → retornar mensaje: "No hay cambios para analizar. El repositorio está limpio."

3. **Si `incluir_contexto=true`, ejecutar:**
   ```bash
   git branch --show-current          # rama actual
   git status --porcelain             # archivos modificados
   git diff --stat [--cached]         # estadísticas de cambios
   ```

4. **Parsear y estructurar el output:**
   - Extraer nombres de archivos del diff
   - Contar líneas agregadas/eliminadas
   - Detectar estado del repositorio

5. **Retornar JSON + diff completo**

### 🎭 Comportamiento Esperado del Rol Artesano

**Antes (sin herramienta):**
```markdown
Usuario: "Ayúdame con un commit"
Artesano: "¿Puedes compartirme el resultado de `git diff`?"
[Usuario copia y pega manualmente]
```

**Después (con herramienta):**
```markdown
Usuario: "Ayúdame con un commit, obtenlo tú"
Artesano: "¿Tus cambios están en staging, unstaged o no estás seguro?"
Usuario: "No estoy seguro"
Artesano: [Ejecuta: > obtener_diff_git tipo_cambios=auto]
Artesano: "✅ He detectado 3 archivos modificados en staging en la rama feature/auth-refactor. Analizando el diff..."
```

### 🔗 Integración con Otros Roles

**Roles que pueden usar esta herramienta:**

| Rol | Uso |
|-----|-----|
| **Artesano de Commits** | Obtener diff para generar mensaje de commit |
| **Onad** | Analizar cambios antes de proponer refactoring arquitectónico |
| **ArchDev Pro** | Revisar cambios en código para validar patrones de diseño |
| **Refinador de HU** | Verificar si los cambios implementados cubren criterios de aceptación de la historia |

### 📈 Criterios de Éxito

- ✅ Detecta correctamente el tipo de cambios en 95%+ de casos
- ✅ Completa ejecución en < 5 segundos para repositorios de tamaño medio
- ✅ Maneja errores comunes (no es repo Git, no hay cambios, etc.) con mensajes claros
- ✅ Output estructurado y parseable por otros sistemas
- ✅ Compatible con Windows, Linux y macOS

### 🚧 Limitaciones Conocidas

- Requiere que el repositorio Git esté accesible desde el contexto de ejecución
- No funciona con repositorios remotos (solo local)
- No maneja conflictos de merge activos (retorna error descriptivo)
- No soporta análisis de múltiples commits simultáneamente

---

## 2. `analizar_diff_contextual`

### 🎯 Propósito

Analizar un `git diff` y extraer automáticamente la intención, agrupar cambios lógicos, identificar el problema que resuelve y detectar el tipo de cambio según Conventional Commits. Esta es la automatización del "Paso 1: Análisis Contextual" del proceso del Artesano.

### 📊 Nivel de Prioridad

**🟡 MEDIA** - Mejora significativa de la experiencia, pero el Artesano puede hacer el análisis manualmente.

### 🔍 Problema que Resuelve

- **Antes:** El rol debe analizar manualmente cada línea del diff para inferir la intención
- **Después:** La herramienta proporciona un análisis estructurado automático que el rol puede refinar

### 📥 Input Esperado

**Parámetros:**
- `diff_completo` (string, requerido): El output completo de `git diff`
- `contexto_adicional` (object, opcional): Información adicional que ayude al análisis
  ```json
  {
    "rama_actual": "feature/auth-refactor",
    "ticket_id": "JIRA-123",
    "descripcion_usuario": "Refactorizar servicio de autenticación para mejorar testabilidad"
  }
  ```

### 📤 Output Esperado

**Formato: JSON estructurado con análisis completo**

```json
{
  "analisis_completado": true,
  "intencion_principal": "Refactorizar el servicio de autenticación extrayendo la lógica de validación de tokens a un servicio dedicado",
  "problema_resuelto": "Mejorar la testabilidad y seguir el principio de responsabilidad única",
  "tipo_cambio_sugerido": "refactor",
  "alcance_sugerido": "auth",
  "nivel_complejidad": "ALTO",
  "grupos_logicos": [
    {
      "tema": "Extracción de servicio de validación",
      "archivos": ["src/services/JwtValidatorService.java"],
      "tipo": "nuevo_componente",
      "descripcion": "Creación de nuevo servicio JwtValidatorService"
    },
    {
      "tema": "Refactorización de AuthService",
      "archivos": ["src/services/AuthService.java"],
      "tipo": "refactor",
      "descripcion": "Modificación para usar el nuevo servicio de validación"
    },
    {
      "tema": "Corrección de bug en manejo de excepciones",
      "archivos": ["src/services/AuthService.java"],
      "tipo": "fix",
      "descripcion": "Se añade captura de TokenExpiredException"
    },
    {
      "tema": "Tests para el nuevo servicio",
      "archivos": ["test/AuthServiceTest.java"],
      "tipo": "test",
      "descripcion": "Pruebas unitarias para JwtValidatorService"
    }
  ],
  "cambios_secundarios": [
    {
      "tipo": "fix",
      "descripcion": "Corrección de bug en manejo de tokens expirados"
    },
    {
      "tipo": "test",
      "descripcion": "Añadir pruebas unitarias para validador"
    }
  ],
  "metricas": {
    "archivos_modificados": 3,
    "archivos_nuevos": 1,
    "archivos_eliminados": 0,
    "lineas_agregadas": 45,
    "lineas_eliminadas": 12,
    "complejidad_estimada": "media-alta"
  },
  "sugerencias": [
    "El cambio principal es un refactor, pero incluye un fix importante",
    "Considerar etiquetar el fix dentro del body del commit",
    "El cambio afecta la arquitectura del servicio de autenticación"
  ]
}
```

### 🔧 Lógica Interna Sugerida

1. **Parsear el diff:**
   - Extraer lista de archivos modificados
   - Identificar líneas agregadas (+) vs eliminadas (-)
   - Detectar archivos nuevos vs modificados vs eliminados

2. **Análisis semántico:**
   - Buscar patrones comunes:
     - Nuevas clases/funciones → probable `feat` o `refactor`
     - Cambios en `if` con validaciones → probable `fix`
     - Archivos en `/test/` → cambios de `test`
     - Cambios solo de formato → probable `style`
   
3. **Agrupación lógica:**
   - Relacionar archivos por dominio (misma carpeta, mismo contexto)
   - Identificar tema principal vs cambios secundarios
   - Detectar si hay múltiples tipos de cambios (refactor + fix)

4. **Inferir intención:**
   - Analizar nombres de funciones/clases nuevas
   - Buscar palabras clave en comentarios del diff
   - Considerar contexto_adicional si está disponible

5. **Clasificar complejidad:**
   - 🟢 BAJO: < 5 archivos, < 50 líneas, un solo tipo
   - 🟡 MEDIO: 5-15 archivos, 50-200 líneas, 1-2 tipos
   - 🔴 ALTO: > 15 archivos, > 200 líneas, múltiples tipos

6. **Generar sugerencias:**
   - Recomendar tipo de commit principal
   - Identificar cambios secundarios para etiquetar en body
   - Alertar sobre breaking changes potenciales

### 🎭 Comportamiento Esperado del Rol Artesano

**Con esta herramienta:**
```markdown
Artesano: [Recibe diff]
Artesano: [Ejecuta: > analizar_diff_contextual diff_completo="..."]
Artesano: "He analizado tu diff. Veo que el cambio principal es un refactor del 
           servicio de autenticación (complejidad ALTA 🔴). La herramienta detectó 
           también un fix importante en el manejo de excepciones.
           
           Voy a construir un mensaje que capture el refactor como tema principal 
           y etiquete el fix dentro del body..."
```

### 🔗 Integración con Otros Roles

| Rol | Uso |
|-----|-----|
| **Artesano de Commits** | Automatizar el Paso 1 de su proceso (Análisis Contextual) |
| **Onad** | Identificar el tipo de cambio antes de analizar arquitectura |
| **ArchDev Pro** | Detectar si un cambio afecta patrones arquitectónicos |

### 📈 Criterios de Éxito

- ✅ Identifica correctamente el tipo principal en 85%+ de casos
- ✅ Detecta cambios secundarios en 80%+ de casos
- ✅ Agrupa cambios lógicamente en 90%+ de casos
- ✅ Completa análisis en < 10 segundos para diffs de tamaño medio
- ✅ Clasifica complejidad correctamente en 90%+ de casos

### 🚧 Limitaciones Conocidas

- No entiende lenguajes específicos (análisis sintáctico limitado)
- Puede confundirse con diffs muy grandes (> 1000 líneas)
- La inferencia de intención depende de la calidad del código y comentarios
- No tiene acceso al historial de commits previos para contexto

---

## 3. Mejora: `generar_commit`

### 🎯 Propósito de la Mejora

Refactorizar completamente la herramienta existente `generar_commit.md` para:
1. **Limpiar errores de formato** (marcas `[cite_start]` actuales)
2. **Incluir el proceso completo de 5 pasos** del Artesano
3. **Documentar el catálogo Conventional Commits**
4. **Integrar con las nuevas herramientas** (`obtener_diff_git`, `analizar_diff_contextual`)

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es la herramienta principal del Artesano y está actualmente incompleta.

### 🔍 Estado Actual vs Estado Deseado

#### **Estado Actual (Problemas detectados):**
```markdown
# Herramienta: generar_commit

[cite_start]
... (marcas de parseo incorrectas)
[cite_end]
```
- Tiene errores de formato
- No documenta el proceso de 5 pasos
- No menciona Conventional Commits explícitamente
- No tiene ejemplos de output
- No documenta reglas de formato (50 chars, imperativo, etc.)

#### **Estado Deseado:**

**Nueva estructura completa:**

```markdown
# 🛠️ Herramienta: `generar_commit`

## 🎯 Propósito

Transformar un `git diff` en un mensaje de commit estandarizado según Conventional Commits, 
siguiendo un proceso estructurado de 5 pasos que garantiza claridad, contexto y utilidad futura.

## 📥 Input Esperado

**Parámetros:**
- `diff` (string, requerido): El git diff a analizar (puede venir de `obtener_diff_git`)
- `contexto_adicional` (object, opcional):
  ```json
  {
    "ticket_id": "JIRA-123",
    "rama": "feature/auth-refactor",
    "descripcion_usuario": "Mejora de testabilidad en auth"
  }
  ```
- `usar_analisis_automatico` (boolean, opcional): Si es true, ejecuta `analizar_diff_contextual` primero. Default: `true`

## 📤 Output Esperado

**Formato: Mensaje de commit en Markdown**

```
refactor(auth): Extraer validación de JWT a servicio dedicado

Se desacopla la lógica de validación de tokens del `AuthService` 
extrayéndola a un nuevo `JwtValidatorService`, siguiendo el 
principio de responsabilidad única y mejorando la testabilidad.

- Se crea `JwtValidatorService` con método `validate()`
- Se inyecta el nuevo servicio via constructor en `AuthService`
- Se delega la validación al servicio extraído
- **fix:** Se añade manejo de `TokenExpiredException` que 
  antes no se capturaba, lanzando ahora `UnauthorizedError`
- **test:** Se añaden pruebas unitarias para el validador

El cambio facilita mockear la validación en tests y centraliza 
la lógica de tokens para futuras mejoras de seguridad.
```

## 🔄 Proceso de 5 Pasos Documentado

### Paso 1: Análisis Contextual (El "Porqué")
[Documentación completa del paso]

### Paso 2: Clasificación de Patrones (Conventional Commits)
[Catálogo completo de tipos]

### Paso 3: Construcción del Título
[Reglas estrictas de formato]

### Paso 4: Redacción de la Narrativa (Body)
[Estructura del body con ejemplos]

### Paso 5: Formato y Entrega Final
[Reglas de formato final]

## 📋 Conventional Commits - Catálogo Completo

[Tabla con los 10 tipos, descripción, cuándo usar, ejemplos]

## 🎯 Reglas de Formato Estrictas

**Título:**
- ✅ Modo imperativo ("Añadir", no "Añadido")
- ✅ Máximo 50 caracteres (72 absoluto)
- ✅ Primera letra mayúscula
- ❌ No terminar con punto
- ❌ No usar "y" o "e" (señal de commit múltiple)

**Body:**
- ✅ Separado del título por línea en blanco
- ✅ Envolver a 72 caracteres
- ✅ Explicar "qué" y "porqué", no "cómo"
- ✅ Listas con viñetas (-) para cambios múltiples
- ✅ Etiquetar cambios secundarios (fix:, test:, docs:)

## 🔗 Integración con Otras Herramientas

**Flujo completo:**
1. Usuario invoca herramienta sin diff → llamar `obtener_diff_git`
2. Con diff obtenido → llamar `analizar_diff_contextual` (si `usar_analisis_automatico=true`)
3. Con análisis → ejecutar proceso de 5 pasos
4. Generar mensaje de commit formateado

## 💡 Ejemplos

[Ejemplo 1: Commit simple (MEDIO)]
[Ejemplo 2: Commit complejo con cambios secundarios (ALTO)]
[Ejemplo 3: Commit trivial (BAJO)]
```

### 📈 Criterios de Éxito de la Mejora

- ✅ Herramienta completamente funcional sin errores de formato
- ✅ Proceso de 5 pasos documentado exhaustivamente
- ✅ Integración con `obtener_diff_git` y `analizar_diff_contextual`
- ✅ Catálogo Conventional Commits completo con ejemplos
- ✅ Reglas de formato documentadas como checklist

---

## 4. Catálogo: `conventional_commits_catalog.md`

### 🎯 Propósito

Documento de referencia rápida que centraliza el catálogo completo de tipos de Conventional Commits 
con definiciones, ejemplos y árbol de decisión visual. No es una herramienta ejecutable, sino un 
documento de referencia que puede ser usado por múltiples herramientas y roles.

### 📊 Nivel de Prioridad

**🟢 BAJA** - Es útil pero no crítico. Puede incluirse dentro de `generar_commit.md` inicialmente.

### 📄 Contenido Sugerido

```markdown
# 📚 Catálogo de Conventional Commits

> Referencia completa de tipos de commit según el estándar Conventional Commits

---

## 🌳 Árbol de Decisión Visual

┌─ ¿El cambio afecta al usuario final?
│
├─ SÍ (cambios funcionales)
│  ├─ ¿Añade nueva funcionalidad? → `feat`
│  ├─ ¿Corrige un bug? → `fix`
│  └─ ¿Mejora rendimiento? → `perf`
│
└─ NO (cambios internos)
   ├─ ¿Cambia estructura sin afectar comportamiento? → `refactor`
   ├─ ¿Añade/modifica tests? → `test`
   ├─ ¿Cambia documentación? → `docs`
   ├─ ¿Cambia formato (espacios, comillas, etc.)? → `style`
   ├─ ¿Cambia CI/CD (pipelines, workflows)? → `ci`
   ├─ ¿Cambia build (dependencias, config)? → `build`
   └─ ¿Otra tarea de mantenimiento? → `chore`

---

## 📋 Catálogo Completo

### 1. `feat` - Nueva Funcionalidad

**Definición:** Añade una nueva capacidad o característica que el usuario final puede usar.

**Cuándo usar:**
- ✅ Nuevo endpoint en API
- ✅ Nueva pantalla en UI
- ✅ Nueva opción de configuración
- ✅ Nueva integración con servicio externo

**Cuándo NO usar:**
- ❌ Refactorizar código existente sin cambiar comportamiento
- ❌ Mejorar rendimiento de funcionalidad existente (usar `perf`)

**Ejemplos:**
```
feat(auth): Añadir autenticación con Google OAuth

feat(api): Implementar endpoint de búsqueda avanzada

feat(ui): Añadir modo oscuro en configuración
```

---

### 2. `fix` - Corrección de Bug

**Definición:** Corrige un comportamiento erróneo o inesperado del sistema.

**Cuándo usar:**
- ✅ Corregir validación que fallaba
- ✅ Solucionar crash o excepción no manejada
- ✅ Arreglar cálculo incorrecto
- ✅ Resolver problema de concurrencia

**Cuándo NO usar:**
- ❌ Optimizar código lento (usar `perf`)
- ❌ Cambiar formato de código (usar `style`)

**Ejemplos:**
```
fix(auth): Corregir validación de email en registro

fix(payment): Resolver race condition en procesamiento de pagos

fix(api): Manejar correctamente error 500 en endpoint de usuarios
```

---

### 3. `refactor` - Mejora de Estructura

**Definición:** Mejora la estructura interna del código sin cambiar su comportamiento observable.

**Cuándo usar:**
- ✅ Extraer método/clase
- ✅ Renombrar variables/funciones para claridad
- ✅ Reorganizar código en módulos
- ✅ Aplicar patrón de diseño
- ✅ Eliminar código duplicado

**Cuándo NO usar:**
- ❌ Si cambia el comportamiento (usar `feat` o `fix`)
- ❌ Si solo cambia formato (usar `style`)

**Ejemplos:**
```
refactor(auth): Extraer validación de JWT a servicio dedicado

refactor(user): Aplicar patrón Repository en acceso a datos

refactor(payment): Eliminar duplicación en cálculo de descuentos
```

---

### 4. `perf` - Mejora de Rendimiento

**Definición:** Optimiza el rendimiento del sistema sin cambiar funcionalidad.

**Cuándo usar:**
- ✅ Optimizar query de base de datos
- ✅ Implementar caché
- ✅ Reducir complejidad algorítmica
- ✅ Lazy loading de recursos

**Ejemplos:**
```
perf(db): Añadir índice en columna user_id para mejorar búsquedas

perf(api): Implementar caché Redis en endpoint de productos

perf(ui): Lazy load de imágenes en galería
```

---

### 5. `test` - Cambios en Tests

**Definición:** Añadir, modificar o eliminar pruebas (sin cambiar código de producción).

**Cuándo usar:**
- ✅ Añadir test unitario nuevo
- ✅ Corregir test que falla incorrectamente
- ✅ Mejorar cobertura de tests
- ✅ Refactorizar tests

**Ejemplos:**
```
test(auth): Añadir test para caso de token expirado

test(payment): Aumentar cobertura de edge cases en cálculo

test(api): Corregir mock en test de integración
```

---

### 6. `docs` - Cambios en Documentación

**Definición:** Cambios exclusivos en documentación (README, comentarios, wiki, etc.).

**Cuándo usar:**
- ✅ Actualizar README
- ✅ Añadir/mejorar comentarios de código
- ✅ Actualizar documentación de API
- ✅ Corregir typos en docs

**Ejemplos:**
```
docs: Actualizar guía de instalación en README

docs(api): Documentar nuevo endpoint de búsqueda

docs: Corregir typo en comentario de AuthService
```

---

### 7. `style` - Cambios de Formato

**Definición:** Cambios que no afectan el significado del código (formato, espacios, indentación).

**Cuándo usar:**
- ✅ Aplicar formato automático (prettier, black)
- ✅ Corregir indentación
- ✅ Añadir/quitar espacios en blanco
- ✅ Cambiar comillas simples a dobles

**Cuándo NO usar:**
- ❌ Si cambia lógica del código

**Ejemplos:**
```
style: Aplicar formato con Prettier en todo el proyecto

style(auth): Corregir indentación en AuthService

style: Cambiar comillas simples a dobles en tests
```

---

### 8. `ci` - Cambios en Integración Continua

**Definición:** Cambios en configuración de CI/CD (pipelines, workflows).

**Cuándo usar:**
- ✅ Modificar GitHub Actions
- ✅ Actualizar Jenkins pipeline
- ✅ Cambiar configuración de GitLab CI
- ✅ Añadir paso de deploy

**Ejemplos:**
```
ci: Añadir step de análisis de seguridad con Snyk

ci(github): Actualizar versión de Node en workflow

ci: Configurar deploy automático a staging
```

---

### 9. `build` - Cambios en Sistema de Build

**Definición:** Cambios en sistema de compilación o dependencias externas.

**Cuándo usar:**
- ✅ Actualizar dependencias (package.json, pom.xml)
- ✅ Cambiar configuración de webpack/gradle
- ✅ Modificar scripts de build

**Ejemplos:**
```
build: Actualizar Spring Boot a versión 3.2.0

build(deps): Bump lodash de 4.17.20 a 4.17.21

build: Optimizar configuración de webpack para producción
```

---

### 10. `chore` - Otras Tareas de Mantenimiento

**Definición:** Tareas de mantenimiento que no modifican código fuente ni tests.

**Cuándo usar:**
- ✅ Actualizar .gitignore
- ✅ Modificar configuración del editor
- ✅ Limpiar archivos temporales
- ✅ Tareas administrativas del repo

**Ejemplos:**
```
chore: Actualizar .gitignore para ignorar archivos de IDE

chore: Limpiar logs antiguos del directorio temp

chore: Configurar EditorConfig para el proyecto
```

---

## 📊 Tabla Resumen

| Tipo | Afecta Usuario | Cambia Funcionalidad | Ejemplo |
|------|----------------|----------------------|---------|
| `feat` | ✅ Sí | ✅ Añade | Nuevo login con Google |
| `fix` | ✅ Sí | ✅ Corrige | Arreglar validación de email |
| `perf` | ✅ Indirectamente | ❌ No | Optimizar query SQL |
| `refactor` | ❌ No | ❌ No | Extraer clase duplicada |
| `test` | ❌ No | ❌ No | Añadir test unitario |
| `docs` | ❌ No | ❌ No | Actualizar README |
| `style` | ❌ No | ❌ No | Aplicar formato |
| `ci` | ❌ No | ❌ No | Modificar GitHub Actions |
| `build` | ❌ No | ❌ No | Actualizar dependencias |
| `chore` | ❌ No | ❌ No | Actualizar .gitignore |

---

## 🤔 Casos Difíciles

### ¿Refactor o Fix?
- Si el código funcionaba correctamente → `refactor`
- Si el código tenía un bug → `fix`

### ¿Feat o Refactor?
- Si añade capacidad nueva para el usuario → `feat`
- Si mejora implementación interna → `refactor`

### ¿Perf o Refactor?
- Si hay medición cuantificable de mejora → `perf`
- Si solo mejora legibilidad → `refactor`

### Commit con múltiples tipos
- Usar el tipo del cambio principal
- Etiquetar cambios secundarios en el body:
  ```
  refactor(auth): Simplificar servicio de autenticación
  
  - Se extrae validación a nuevo servicio
  - **fix:** Se corrige bug de tokens expirados
  - **test:** Se añaden pruebas unitarias
  ```
```

---

## 📝 Notas Finales sobre Abstracciones

### Priorización Recomendada para Implementación

1. **🥇 Primera iteración (Crítica):**
   - Refactorizar `generar_commit.md` completamente
   - Implementar `obtener_diff_git`

2. **🥈 Segunda iteración (Alta prioridad):**
   - Implementar `analizar_diff_contextual`
   - Integrar las 3 herramientas en flujo completo

3. **🥉 Tercera iteración (Nice-to-have):**
   - Crear `conventional_commits_catalog.md` como documento separado
   - (O mantenerlo dentro de `generar_commit.md`)

### Impacto Estimado

| Herramienta/Mejora | Ahorro de Tiempo | Mejora de Calidad | Complejidad Implementación |
|-------------------|------------------|-------------------|---------------------------|
| `obtener_diff_git` | 🔥🔥🔥 (80%) | 🔥 (20%) | 🟡 Media |
| `analizar_diff_contextual` | 🔥🔥 (60%) | 🔥🔥🔥 (70%) | 🔴 Alta |
| Mejora `generar_commit` | 🔥🔥 (50%) | 🔥🔥🔥 (80%) | 🟡 Media |
| Catálogo Conventional Commits | 🔥 (20%) | 🔥🔥 (40%) | 🟢 Baja |

---

## 📅 Última Actualización

**Fecha:** 5 de octubre de 2025  
**Autor:** Análisis durante refactorización de Artesano de Commits v2.0  
**Estado:** Propuesta de herramientas pendientes de implementación
