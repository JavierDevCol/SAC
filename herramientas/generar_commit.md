# 🛠️ Herramienta: Generar Commit

> **Versión:** 2.0  
> **Fecha de Actualización:** 10 de octubre de 2025  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `generar_commit`

---

## 🎯 Objetivo

Analizar automáticamente un `git diff` y generar mensajes de commit claros, estandarizados y semánticamente correctos siguiendo la especificación **Conventional Commits**. Acelera el proceso de documentación de cambios y mejora la trazabilidad del historial de desarrollo.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

*Esta herramienta funciona de manera independiente y no invoca otras herramientas del sistema.*

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **Artesano de Commits** | Después de realizar cambios en el código | Generar mensaje de commit estandarizado y semánticamente correcto |
| **ArchDev Pro** | Al finalizar implementación de features o refactoring | Documentar cambios arquitectónicos con commits claros |
| **`refactorizar`** | Al completar proceso de refactorización | Generar commit que documenta las mejoras realizadas |
| **`crear_pruebas`** | Después de generar tests | Crear commit específico para los tests añadidos |
| **Arquitecto DevOps** | Al modificar infraestructura o pipelines | Documentar cambios de CI/CD y configuración |

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Resultado de `git diff` (staged o unstaged) con los cambios a documentar
- Lista de archivos modificados para inferir el alcance del cambio

**Secundario (Opcional):**
- Branch name actual (para inferir tipo de trabajo: feature/, bugfix/, hotfix/)
- Número de issue/ticket relacionado (para trazabilidad y contexto)
- Contexto de la tarea o historia de usuario que motiva los cambios
- Indicación de breaking changes o migraciones incluidas
- Mensajes de commit previos en la misma branch (para consistencia de estilo)

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `tipo_commit` | string | auto\|feat\|fix\|docs\|style\|refactor\|perf\|test\|build\|ci\|chore | auto | Forzar tipo específico o detectar automáticamente |
| `incluir_body` | boolean | true\|false | true | Generar cuerpo detallado del commit o solo título |
| `formato_alcance` | string | auto\|archivo\|modulo\|componente | auto | Estrategia para determinar el alcance (scope) |
| `breaking_change` | boolean | true\|false | false | Marcar explícitamente como breaking change |
| `max_lineas_titulo` | number | 50-72 | 50 | Límite de caracteres para el título del commit |

---

## 👥 Roles Autorizados

- ✅ **Artesano de Commits** (uso principal - especialista en documentación de cambios)
- ✅ **ArchDev Pro** (integración con flujos de desarrollo arquitectónico)
- ✅ **Arquitecto DevOps** (commits relacionados con infraestructura y pipelines)
- ✅ **Refinador HU** *(para commits relacionados con refinamiento de historias)*

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Selección de Modo de Operación (Opcional)

- **Presentar opciones al usuario:**
  - **Modo Automático**: Generar commit inmediatamente con configuración por defecto
  - **Modo Configuración**: Mostrar parámetros disponibles para personalizar la generación
  
- **Si elige Modo Configuración, mostrar formulario interactivo:**
  ```
  🔧 Configuración de Generación de Commit:
  
  📝 Tipo de Commit:
  • auto (detectar automáticamente) ← por defecto
  • feat, fix, docs, style, refactor, perf, test, build, ci, chore
  
  📄 Incluir cuerpo detallado:
  • true (generar descripción completa) ← por defecto  
  • false (solo título)
  
  🎯 Formato del alcance:
  • auto (inferir del contexto) ← por defecto
  • archivo (usar nombre de archivo principal)
  • modulo (detectar módulo/paquete)
  • componente (identificar componente arquitectónico)
  
  ⚠️ Breaking change:
  • false (cambio compatible) ← por defecto
  • true (rompe compatibilidad hacia atrás)
  
  📏 Límite de caracteres del título:
  • 50 (estándar Git) ← por defecto
  • 72 (máximo recomendado)
  ```
  
- **Capturar preferencias del usuario o usar valores por defecto si elige Modo Automático**

### 2️⃣ Análisis del Contexto de Cambios

- Parsear el `git diff` para identificar archivos modificados, líneas añadidas/eliminadas y patrones de cambio
- Extraer información del branch name para inferir el tipo de trabajo (feature/, bugfix/, hotfix/, etc.)
- Analizar la estructura de archivos afectados para determinar el alcance del cambio (frontend, backend, config, tests)
- Identificar si hay cambios en archivos críticos (package.json, pom.xml, Dockerfile) que sugieran cambios de dependencias o configuración

### 3️⃣ Clasificación Automática del Tipo de Commit

- Aplicar reglas de detección basadas en patrones del diff:
  - `feat`: Nuevos archivos de funcionalidad, nuevos métodos públicos, nuevas rutas API
  - `fix`: Cambios en bloques try-catch, correcciones de bugs reportados, hotfixes
  - `refactor`: Renombrado de métodos/clases, extracción de código, cambios de estructura sin nueva funcionalidad
  - `test`: Archivos en carpetas de test, nuevos casos de prueba
  - `docs`: Archivos .md, comentarios de documentación, README
  - `style`: Cambios de formato, espacios, lint fixes
  - `ci/build`: Archivos de CI/CD, Docker, scripts de build
- Si el parámetro `tipo_commit` está forzado, usar ese valor en lugar de la detección automática

### 4️⃣ Determinación del Alcance (Scope)

- Analizar la estrategia definida en `formato_alcance`:
  - **auto**: Inferir automáticamente basado en la estructura del proyecto
  - **archivo**: Usar el nombre del archivo principal modificado
  - **modulo**: Detectar el módulo/paquete afectado (ej: auth, payment, user)
  - **componente**: Identificar el componente arquitectónico (api, service, repository, etc.)
- Generar alcance conciso y descriptivo (máximo 15 caracteres)

### 5️⃣ Construcción del Título del Commit

- Ensamblar el título siguiendo el formato: `tipo(alcance): descripción`
- Generar descripción en modo imperativo y tiempo presente
- Respetar el límite de caracteres definido en `max_lineas_titulo`
- Aplicar convenciones: primera letra mayúscula, sin punto final, verbo de acción claro

### 6️⃣ Generación del Cuerpo (si incluir_body=true)

- Crear párrafo inicial explicando el "porqué" del cambio basado en el contexto disponible
- Generar lista detallada de cambios específicos usando viñetas (-)
- Incluir referencias a issues/tickets si están disponibles en el contexto
- Agregar footer con breaking changes si `breaking_change=true` usando formato `BREAKING CHANGE:`
- Aplicar formato Markdown para mejorar legibilidad

### 7️⃣ Validación y Entrega

- Verificar que el mensaje cumple con la especificación Conventional Commits
- Validar longitud de líneas y formato general
- Entregar el mensaje completo listo para usar con `git commit -m`

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Git diff vacío o sin cambios detectados | Informar al usuario que no hay cambios para documentar y sugerir verificar el estado del repositorio |
| Diff contiene solo cambios binarios (imágenes, archivos compilados) | Generar commit básico tipo `chore` con descripción genérica de actualización de recursos |
| Branch name no sigue convenciones estándar | Usar detección automática basado solo en el contenido del diff, ignorar información del branch |
| Archivos modificados pertenecen a múltiples módulos/componentes | Sugerir dividir en múltiples commits o usar alcance más genérico como `global` o `multi` |
| Detecta cambios que rompen compatibilidad pero `breaking_change=false` | Advertir al usuario sobre posibles breaking changes detectados y sugerir revisión |
| Título generado excede el límite de caracteres configurado | Acortar automáticamente manteniendo las palabras clave más importantes y agregar `...` si es necesario |
| No se puede determinar el tipo de commit automáticamente | Usar `chore` como fallback y solicitar al usuario que revise y ajuste manualmente |
| Contexto insuficiente para generar cuerpo descriptivo | Generar solo el título del commit e informar que se requiere más contexto para el cuerpo detallado |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Un mensaje de commit completo formateado según Conventional Commits, listo para usar con `git commit -m`

**Estructura del output:**
```
tipo(alcance): descripción concisa del cambio

Párrafo explicativo del porqué del cambio, proporcionando contexto
y justificación de las decisiones tomadas.

- Lista detallada de cambios específicos realizados
- Modificaciones en funcionalidad o comportamiento
- Ajustes en configuración o dependencias
- Mejoras en documentación o tests

Refs: #123, #456
BREAKING CHANGE: Descripción del cambio que rompe compatibilidad (solo si aplica)
```

**Notificación de confirmación:**
- Resumen de la configuración utilizada (tipo detectado, alcance, parámetros aplicados)
- Mensaje de éxito con el commit generado listo para copiar

**Ejemplo de salida completa:**
```bash
# Comando sugerido:
git commit -m "feat(auth): Implementar autenticación con JWT

Agrega sistema de autenticación basado en tokens JWT para mejorar
la seguridad y permitir sesiones stateless en la API.

- Crear middleware de autenticación JWT
- Implementar endpoints de login y logout
- Agregar validación de tokens en rutas protegidas
- Configurar expiración de tokens en 24 horas
- Añadir tests unitarios para AuthService

Refs: #AUTH-001, #SEC-045"
```

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/generar_commit_ejemplo.md`

---

## 📚 Referencias y Notas

### Especificaciones y Estándares

- **Conventional Commits Specification:** https://www.conventionalcommits.org/
- **Semantic Versioning (SemVer):** https://semver.org/ - Para entender el impacto de breaking changes
- **Git Commit Best Practices:** https://chris.beams.io/posts/git-commit/ - Referencia clásica sobre mensajes de commit

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `refactorizar` - Puede invocar `generar_commit` al finalizar refactorizaciones
- `crear_pruebas` - Útil para commits relacionados con testing
- `analizar_code_smells` - Para commits de mejoras de calidad

**Herramientas externas compatibles:**
- Commitizen CLI - Para flujo interactivo de commits
- Husky + Commitlint - Para validación automática de mensajes
- Conventional Changelog - Para generación automática de changelogs

### Limitaciones Conocidas

- **Idioma:** Genera commits únicamente en inglés siguiendo estándares internacionales
- **Detección de contexto:** La precisión depende de la calidad del git diff y información contextual
- **Proyectos monorepo:** Puede requerir configuración manual del alcance en repositorios muy complejos
- **Dependencias externas:** No analiza el impacto en sistemas externos o APIs consumidoras

### Consideraciones de Rendimiento

- **Archivos grandes:** Diffs superiores a 1000 líneas pueden requerir más tiempo de análisis
- **Múltiples módulos:** Cambios que afectan +5 módulos pueden necesitar revisión manual del alcance
- **Tiempo de ejecución:** < 5 segundos para casos típicos, hasta 15 segundos para análisis complejos

### Futuras Mejoras

- **Análisis semántico:** Machine Learning para mejor detección de tipos de cambio
- **Multiidioma:** Soporte para generar commits en español y otros idiomas
- **Integración Git:** Plugin directo para Git hooks y flujos automatizados
- **Contexto de historial:** Análisis de commits previos para mantener consistencia de estilo