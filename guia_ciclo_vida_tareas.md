# 🔄 Guía del Ciclo de Vida de Tareas

> **Sistema:** Cochas - Orquestación de Agentes IA  
> **Versión:** 2.0  
> **Última Actualización:** 16 de octubre de 2025

---

## 📖 Índice

- [Introducción](#introducción)
- [Estados de las Tareas](#estados-de-las-tareas)
- [Flujo de Validación Secuencial](#flujo-de-validación-secuencial)
- [El Backlog de Desarrollo](#el-backlog-de-desarrollo)
- [Roles y Responsabilidades](#roles-y-responsabilidades)
- [Ejemplos Prácticos](#ejemplos-prácticos)

---

## Introducción

El sistema Cochas implementa un **flujo de validación secuencial** para las tareas de desarrollo, garantizando que cada tarea pase por las etapas necesarias de refinamiento, aprobación e implementación antes de ser marcada como completada.

### Principios del Sistema

1. **Validación Secuencial:** Las tareas deben pasar por estados específicos en orden
2. **Responsabilidad de Roles:** Solo ciertos roles pueden cambiar estados específicos
3. **Trazabilidad:** Todo cambio de estado queda registrado en `session_state.json`
4. **No Saltar Pasos:** No se puede pasar directamente de Pendiente a Completada

---

## Estados de las Tareas

### 📋 Estado 1: Pendiente `[ ]`

**Descripción:** Tarea creada pero no refinada. Requiere clarificación de requisitos.

**Características:**
- Descripción básica de qué hacer
- Puede tener requisitos ambiguos
- Necesita criterios de aceptación claros
- Estimación inicial puede ser imprecisa

**Responsable de avanzar:** `Refinador HU` (REFINADOR)

**Siguiente estado:** Refinada `[R]`

**Ejemplo:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [ ] Pendiente
- **Por qué:** Necesario para autenticación de usuarios
- **Origen:** ONAD-001
```

---

### 📝 Estado 2: Refinada `[R]`

**Descripción:** Tarea con criterios de aceptación claros, dependencias identificadas y estimación precisa.

**Características:**
- Criterios de aceptación definidos
- Dependencias técnicas identificadas
- Estimación de esfuerzo validada
- Casos de borde considerados

**Responsable de avanzar:** `Arquitecto Onad` (ONAD)

**Siguiente estado:** Aprobada `[A]`

**Ejemplo:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [R] Refinada
- **Por qué:** Autenticación JWT para usuarios del sistema
- **Origen:** ONAD-001

**Criterios de Aceptación:**
✅ Generación de tokens JWT con RS256
✅ Validación de tokens en cada request
✅ Refresh tokens con expiración de 7 días
✅ Tests unitarios con cobertura > 90%
✅ Manejo de errores (token expirado, inválido)

**Dependencias Técnicas:**
- Librería: spring-security-jwt
- Base de datos: Tabla users con credenciales
- Configuración: Claves pública/privada generadas

**Estimación:** 8 horas
```

---

### ✅ Estado 3: Aprobada `[A]`

**Descripción:** Tarea validada arquitectónicamente y lista para implementación.

**Características:**
- Alineada con decisiones arquitectónicas
- Trade-offs evaluados y aprobados
- Riesgos identificados y mitigados
- Sin conflictos con otras decisiones

**Responsable de avanzar:** `ArchDev Pro` (ARCHDEV)

**Siguiente estado:** Completada `[X]`

**Ejemplo:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [A] Aprobada
- **Por qué:** Autenticación JWT para usuarios del sistema
- **Origen:** ONAD-001
- **Aprobado por:** ONAD el 2025-10-16T10:30:00

**Notas de Aprobación:**
- ✅ Alineado con arquitectura hexagonal
- ✅ JWT preferido sobre sesiones por escalabilidad
- ⚠️ Considerar rate limiting para endpoints de login
- ✅ Usar RS256 (no HS256) por mejor seguridad

**Criterios de Aceptación:**
[... mismos criterios del estado Refinada ...]

**Listo para implementación**
```

---

### 🎉 Estado 4: Completada `[X]`

**Descripción:** Tarea implementada, testeada y lista para deployment.

**Características:**
- Código implementado según diseño
- Tests unitarios y de integración pasando
- Code review aprobado (si aplica)
- Documentación técnica actualizada

**Responsable:** `ArchDev Pro` (ARCHDEV)

**Estado final:** No hay siguiente estado

**Ejemplo:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [X] Completada
- **Por qué:** Autenticación JWT para usuarios del sistema
- **Origen:** ONAD-001
- **Completado por:** ARCHDEV el 2025-10-16T14:45:00

**Implementación:**
✅ JwtTokenProvider con generación RS256
✅ TokenAuthenticationFilter en SecurityConfig
✅ Endpoints: /login, /refresh
✅ Tests: 15 unitarios + 5 integración
✅ Cobertura: 95%
✅ Documentación actualizada en README

**Archivos modificados:**
- src/main/java/auth/JwtTokenProvider.java
- src/main/java/security/SecurityConfig.java
- src/test/java/auth/JwtTokenProviderTest.java
```

---

## Flujo de Validación Secuencial

### Diagrama de Flujo

```
┌─────────────┐
│  Pendiente  │  ← Tarea creada por cualquier rol
│     [ ]     │
└──────┬──────┘
       │
       │ Refinar (REFINADOR)
       ▼
┌─────────────┐
│  Refinada   │  ← Criterios claros, estimación precisa
│     [R]     │
└──────┬──────┘
       │
       │ Aprobar (ONAD)
       ▼
┌─────────────┐
│  Aprobada   │  ← Validación arquitectónica
│     [A]     │
└──────┬──────┘
       │
       │ Implementar (ARCHDEV)
       ▼
┌─────────────┐
│ Completada  │  ← Código implementado y testeado
│     [X]     │
└─────────────┘
```

---

### Reglas Estrictas

#### ❌ Prohibido Saltar Estados

**No se puede:**
- [ ] → [X] (de Pendiente directamente a Completada)
- [ ] → [A] (de Pendiente directamente a Aprobada)
- [R] → [X] (de Refinada directamente a Completada)

**Siempre debe ser secuencial:**
- [ ] → [R] → [A] → [X]

---

#### 🔒 Solo Roles Autorizados Pueden Cambiar Estados

| Transición | Rol Autorizado | Comando |
|------------|----------------|---------|
| [ ] → [R] | Refinador HU | `/cochas +REFINADOR` |
| [R] → [A] | Arquitecto Onad | `/cochas +ONAD` |
| [A] → [X] | ArchDev Pro | `/cochas +ARCHDEV` |

**Ejemplo de validación:**
```
Usuario con rol ARCHDEV activo:
Intenta: [ ] → [R]

Sistema: ❌ Error
"Solo el rol 'Refinador HU' puede cambiar una tarea de Pendiente a Refinada.
Usa: /cochas +REFINADOR"
```

---

## El Backlog de Desarrollo

### Ubicación

`artefactos/backlog_desarrollo.md`

Este archivo se genera automáticamente cuando:
- Un rol completa una tarea que genera tareas de desarrollo
- Se usa el sistema de validación secuencial

---

### Estructura del Backlog

```markdown
# 📋 Backlog de Desarrollo

> **Proyecto:** Sistema E-commerce
> **Última Actualización:** 2025-10-16T14:30:00

---

## Estados de Tareas

- `[ ]` **Pendiente** - Requiere refinamiento por `refinador_hu`
- `[R]` **Refinada** - Refinada y lista para aprobación de `ONAD`
- `[A]` **Aprobada** - Aprobada y lista para desarrollo por `archdev_pro`
- `[X]` **Completada** - Desarrollada e implementada

---

## Tareas

### ARCHDEV-001: Implementar Auth Service
- **Estado:** [X] Completada
- **Por qué:** Necesario para autenticación de usuarios en el sistema
- **Origen:** ONAD-001 (Diseño de arquitectura)
- **Fecha creación:** 2025-10-15
- **Prioridad:** Alta
- **Completado:** 2025-10-16T14:45:00

---

### ARCHDEV-002: Implementar Catalog Service
- **Estado:** [A] Aprobada
- **Por qué:** Gestionar productos del e-commerce con cache
- **Origen:** ONAD-001 (Diseño de arquitectura)
- **Fecha creación:** 2025-10-15
- **Prioridad:** Alta
- **Aprobado:** 2025-10-16T11:00:00

---

### ARCHDEV-003: Implementar Order Service
- **Estado:** [R] Refinada
- **Por qué:** Procesar pedidos de clientes
- **Origen:** ONAD-001 (Diseño de arquitectura)
- **Fecha creación:** 2025-10-15
- **Prioridad:** Media
- **Refinado:** 2025-10-16T09:30:00

---

### ARCHDEV-004: Implementar Payment Gateway Integration
- **Estado:** [ ] Pendiente
- **Por qué:** Integrar pasarela de pagos externa
- **Origen:** ONAD-001 (Diseño de arquitectura)
- **Fecha creación:** 2025-10-15
- **Prioridad:** Alta
```

---

### Actualización Automática

El backlog se actualiza automáticamente cuando:

1. **Un rol completa una tarea con CASO A (desarrollo):**
   - Se agregan nuevas tareas en estado `[ ]` Pendiente

2. **REFINADOR refina una tarea:**
   - Cambia `[ ]` → `[R]`
   - Agrega criterios de aceptación

3. **ONAD aprueba una tarea:**
   - Cambia `[R]` → `[A]`
   - Agrega notas de aprobación

4. **ARCHDEV completa una tarea:**
   - Cambia `[A]` → `[X]`
   - Agrega detalles de implementación

---

## Roles y Responsabilidades

### 👥 Refinador HU (REFINADOR)

**Responsabilidad:** Transformar tareas pendientes en tareas refinadas

**Proceso:**
1. Lee tarea en estado `[ ]` del backlog
2. Ejecuta `> refinar_hu`
3. Define criterios de aceptación claros
4. Identifica dependencias técnicas
5. Estima esfuerzo con precisión
6. Actualiza backlog a estado `[R]`

**Ejemplo de refinamiento:**
```bash
/cochas +REFINADOR

# Leer tarea pendiente del backlog
> refinar_hu

# Sistema pregunta: ¿Qué tarea deseas refinar?
ARCHDEV-004: Implementar Payment Gateway Integration

# El rol refina y actualiza:
[ ] → [R]
```

---

### 🏛️ Arquitecto Onad (ONAD)

**Responsabilidad:** Validar arquitectónicamente tareas refinadas

**Proceso:**
1. Lee tarea en estado `[R]` del backlog
2. Valida alineación con decisiones arquitectónicas
3. Evalúa trade-offs e impactos
4. Identifica riesgos y mitigaciones
5. Aprueba o solicita ajustes
6. Actualiza backlog a estado `[A]`

**Ejemplo de aprobación:**
```bash
/cochas +ONAD

# Revisar tarea refinada
Usuario: Revisa ARCHDEV-004 del backlog

ONAD:
Revisando tarea ARCHDEV-004...

**Validación Arquitectónica:**
✅ Alineado con patrón adapter para integraciones
✅ Trade-offs evaluados: Stripe vs PayPal
⚠️ Riesgo: Dependencia de servicio externo
✅ Mitigación: Circuit breaker pattern

**Decisión:** Aprobada con recomendaciones

[R] → [A]
```

---

### 💻 ArchDev Pro (ARCHDEV)

**Responsabilidad:** Implementar tareas aprobadas

**Proceso:**
1. Lee tarea en estado `[A]` del backlog
2. Implementa código según diseño
3. Crea tests unitarios y de integración
4. Valida criterios de aceptación
5. Actualiza backlog a estado `[X]`

**Ejemplo de implementación:**
```bash
/cochas +ARCHDEV

# Implementar tarea aprobada
Usuario: Implementa ARCHDEV-004 del backlog

ARCHDEV:
Implementando ARCHDEV-004...

> refactorizar
# Implementa código...

> crear_pruebas
# Genera tests...

✅ Implementación completa
✅ Tests pasando (cobertura 92%)
✅ Code review aplicado

[A] → [X]
```

---

## Ejemplos Prácticos

### Ejemplo 1: Flujo Completo de una Tarea

#### Fase 1: Creación (ONAD)

```bash
/cochas +ONAD
> define_arquitectura

# ONAD diseña arquitectura y genera tareas
# Se crea automáticamente:

ARCHDEV-005: Implementar User Profile Service
[ ] Pendiente
```

**Backlog actualizado:**
```markdown
### ARCHDEV-005: Implementar User Profile Service
- **Estado:** [ ] Pendiente
- **Por qué:** Gestionar perfiles de usuarios
- **Origen:** ONAD-002
- **Fecha creación:** 2025-10-16
- **Prioridad:** Media
```

---

#### Fase 2: Refinamiento (REFINADOR)

```bash
/cochas +REFINADOR
> refinar_hu

# Refinar tarea ARCHDEV-005

# El sistema actualiza:
[ ] → [R]
```

**Backlog actualizado:**
```markdown
### ARCHDEV-005: Implementar User Profile Service
- **Estado:** [R] Refinada
- **Por qué:** Gestionar perfiles de usuarios con foto y datos personales
- **Origen:** ONAD-002
- **Fecha creación:** 2025-10-16
- **Prioridad:** Media
- **Refinado:** 2025-10-16T15:00:00

**Criterios de Aceptación:**
✅ CRUD completo de perfil de usuario
✅ Upload de foto de perfil (max 2MB)
✅ Validación de campos obligatorios
✅ API REST con documentación Swagger
✅ Tests con cobertura > 85%

**Dependencias Técnicas:**
- Servicio de storage para fotos (S3/local)
- Tabla users existente en BD

**Estimación:** 12 horas
```

---

#### Fase 3: Aprobación (ONAD)

```bash
/cochas +ONAD

Usuario: Revisar y aprobar ARCHDEV-005

# El sistema actualiza:
[R] → [A]
```

**Backlog actualizado:**
```markdown
### ARCHDEV-005: Implementar User Profile Service
- **Estado:** [A] Aprobada
- **Por qué:** Gestionar perfiles de usuarios con foto y datos personales
- **Origen:** ONAD-002
- **Fecha creación:** 2025-10-16
- **Prioridad:** Media
- **Refinado:** 2025-10-16T15:00:00
- **Aprobado:** 2025-10-16T15:30:00

**Notas de Aprobación (ONAD):**
✅ Alineado con arquitectura hexagonal
✅ Usar S3 para storage de fotos (no filesystem)
⚠️ Considerar compresión de imágenes (reducir costos)
✅ Implementar soft delete de perfiles

[... criterios de aceptación y dependencias ...]
```

---

#### Fase 4: Implementación (ARCHDEV)

```bash
/cochas +ARCHDEV

Usuario: Implementar ARCHDEV-005

> refactorizar
# Implementa ProfileService, ProfileController, etc.

> crear_pruebas
# Genera tests

# El sistema actualiza:
[A] → [X]
```

**Backlog actualizado:**
```markdown
### ARCHDEV-005: Implementar User Profile Service
- **Estado:** [X] Completada
- **Por qué:** Gestionar perfiles de usuarios con foto y datos personales
- **Origen:** ONAD-002
- **Fecha creación:** 2025-10-16
- **Prioridad:** Media
- **Refinado:** 2025-10-16T15:00:00
- **Aprobado:** 2025-10-16T15:30:00
- **Completado:** 2025-10-16T18:15:00

**Implementación (ARCHDEV):**
✅ ProfileService con CRUD completo
✅ S3 integration para upload de fotos
✅ Compresión automática de imágenes
✅ Soft delete implementado
✅ 18 tests unitarios + 6 integración
✅ Cobertura: 89%
✅ Documentación Swagger actualizada

**Archivos:**
- src/main/java/profile/ProfileService.java
- src/main/java/profile/ProfileController.java
- src/main/java/storage/S3StorageService.java
- src/test/java/profile/ProfileServiceTest.java
```

---

### Ejemplo 2: Error al Saltar Estados

```bash
# Usuario tiene rol ARCHDEV activo
/cochas +ARCHDEV

Usuario: Completa la tarea ARCHDEV-006 que está en estado Pendiente

Sistema:
❌ Error de Validación

La tarea ARCHDEV-006 está en estado [ ] Pendiente.
No puedes marcarla como Completada directamente.

**Flujo requerido:**
1. [ ] Pendiente → [R] Refinada (por REFINADOR)
2. [R] Refinada → [A] Aprobada (por ONAD)
3. [A] Aprobada → [X] Completada (por ARCHDEV)

**Siguiente paso:**
Activa el rol REFINADOR para refinar la tarea primero.
Comando: /cochas +REFINADOR
```

---

### Ejemplo 3: Múltiples Tareas en Diferentes Estados

**Estado del backlog:**
```markdown
## Tareas

### ARCHDEV-001: Auth Service
- **Estado:** [X] Completada

### ARCHDEV-002: Catalog Service
- **Estado:** [A] Aprobada (lista para ARCHDEV)

### ARCHDEV-003: Order Service
- **Estado:** [R] Refinada (lista para ONAD)

### ARCHDEV-004: Payment Integration
- **Estado:** [ ] Pendiente (requiere REFINADOR)
```

**Flujo de trabajo sugerido:**

```bash
# Paso 1: Refinar tarea pendiente
/cochas +REFINADOR
> refinar_hu
# Refinar ARCHDEV-004

# Paso 2: Aprobar tarea refinada
/cochas +ONAD
# Revisar y aprobar ARCHDEV-003

# Paso 3: Implementar tarea aprobada
/cochas +ARCHDEV
> refactorizar
# Implementar ARCHDEV-002

# Ver progreso
/cochas status
```

---

## 💡 Mejores Prácticas

### Práctica 1: Refinar Temprano
```bash
# Al inicio del sprint
/cochas +REFINADOR
> refinar_hu

# Refinar todas las tareas [ ] pendientes
# Esto permite aprobación y planificación anticipada
```

### Práctica 2: Aprobar en Lote
```bash
# Una vez al día (si tienes múltiples tareas refinadas)
/cochas +ONAD

# Revisar y aprobar todas las tareas [R] refinadas
# Esto desbloquea a ARCHDEV para implementar
```

### Práctica 3: Implementar por Prioridad
```bash
# Implementar tareas [A] aprobadas según prioridad
/cochas +ARCHDEV

# Prioridad Alta primero
# Luego Prioridad Media
# Finalmente Prioridad Baja
```

### Práctica 4: Revisar el Backlog Regularmente
```bash
# Revisar el backlog completo
cat artefactos/backlog_desarrollo.md

# Ver estado de la sesión
/cochas status
```

---

## 📊 Métricas y Visibilidad

### Ver Estado del Backlog

```bash
/cochas status

# Salida incluye:
📋 **Tablero de Tareas:**
- Pendientes: 2
- Refinadas: 3
- Aprobadas: 1
- Completadas: 5
```

### Ver Historial de Cambios

```bash
/cochas history

# Muestra todos los cambios de estado de tareas
# Con timestamps y roles responsables
```

---

## 📚 Documentación Relacionada

- **[README Principal](README.md)** - Visión general del sistema
- **[Guía de Comandos](guia_comandos.md)** - Comandos detallados
- **[Guía de Roles](guia_roles_activos.md)** - Roles y sus capacidades
- **[Crear Roles](guia_creacion_roles.md)** - Extender el sistema

---

## 🎯 Resumen Rápido

**Flujo secuencial obligatorio:**
```
[ ] Pendiente
  ↓ (REFINADOR)
[R] Refinada
  ↓ (ONAD)
[A] Aprobada
  ↓ (ARCHDEV)
[X] Completada
```

**Archivo central:** `artefactos/backlog_desarrollo.md`

**Comando útil:** `/cochas status` para ver progreso general

**¿Dudas sobre qué hacer?** Usa `/cochas assign "revisar backlog"`
