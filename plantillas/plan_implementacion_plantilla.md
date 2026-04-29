---
tipo: plan_implementacion
version: "4.0"
generado_por: ">planificar_hu"
actualizado_por: ">ejecutar_plan"
validado_por: ">validar_ca"
---

#  Plan de Implementación: [ID-HU] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **HU** | [ID-HU] |
| **Título** | [Título de la HU] |
| **Refinamiento** | {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md |
| **Arquitectura** | [Hexagonal\|MVC\|Capas\|Script\|Monolito] |
| **Generado por** | ONAD |
| **Fecha creación** | [FECHA_ISO_8601] |
| **Última actualización** | [FECHA_ISO_8601] |
| **Estimación total** | [X] horas |
| **Estado** | [PENDIENTE \| EN_PROGRESO \| COMPLETADO \| BLOQUEADO] |
| **Modo** | [Plano \| Particionada] |
| **Tasks** | [— \| [ID-HU]-T1, [ID-HU]-T2, ...] |

## Progreso General

<!--
INSTRUCCIÓN PARA >planificar_hu:

SI Modo = 'Plano':
  Generar filas de fases según arquitectura detectada en contexto_proyecto.md:

  SI arquitectura = Hexagonal:
    Fases: Infraestructura  Dominio  Aplicación  Adaptadores  Testing  Validación

  SI arquitectura = MVC:
    Fases: Infraestructura  Modelos  Controladores  Vistas  Testing  Validación

  SI arquitectura = Capas:
    Fases: Infraestructura  Datos  Negocio  Presentación  Testing  Validación

  SI arquitectura = Script/CLI:
    Fases: Setup  Lógica Principal  Testing  Validación

  SI arquitectura = Frontend (React/Vue/Angular):
    Fases: Setup  Componentes  Hooks/Services  Integración  Testing  Validación

  DEFAULT:
    Fases: Preparación  Implementación  Testing  Validación

  Usar tabla de fases (formato actual).

SI Modo = 'Particionada':
  Generar tabla agrupada por task funcional (NO por fase arquitectónica).
  Agregar fila final para Validación CA Integración.
-->

| Fase | Estado | Progreso |
|------|--------|----------|
| Fase 1: [NOMBRE_FASE_1] | [ESTADO] | [X/Y] tareas |
| Fase 2: [NOMBRE_FASE_2] | [ESTADO] | [X/Y] tareas |
| Fase 3: [NOMBRE_FASE_3] | [ESTADO] | [X/Y] tareas |
| Fase N: Testing | [ESTADO] | [X/Y] tareas |
| Fase Final: Validación CA | [ESTADO] | [X/Y] criterios |

<!-- OPCIÓN PARTICIONADA: Reemplazar tabla anterior por esta si Modo = Particionada -->
<!--
| Task | Descripción | Estado | Progreso |
|------|-------------|--------|----------|
| [ID-HU]-T1 | [Título task 1] | [ESTADO] | [X/Y] tareas |
| [ID-HU]-T2 | [Título task 2] | [ESTADO] | [X/Y] tareas |
| [ID-HU]-T3 | [Título task 3] | [ESTADO] | [X/Y] tareas |
| — | Validación CA Integración | [ESTADO] | [X/Y] criterios |
-->

---

<!-- ======================================================================== -->
<!-- SECCIÓN SOLO PARTICIONADA: Dependencias entre Tasks                     -->
<!-- Incluir SOLO si Modo = Particionada. Eliminar si Modo = Plano.          -->
<!-- ======================================================================== -->
<!--
## Dependencias entre Tasks

| Task | Depende de | Razón | Ejecutable? |
|------|-----------|-------|:-----------:|
| [ID-HU]-T1 | — | Sin dependencias | ✅ |
| [ID-HU]-T2 | [ID-HU]-T1 | [Razón: requiere entidades/ports/endpoints de T1] | ⛔ |
| [ID-HU]-T3 | [ID-HU]-T1, [ID-HU]-T2 | [Razón: requiere backend completo] | ⛔ |

> 💡 La columna "Ejecutable?" se evalúa en tiempo de ejecución por >ejecutar_plan según el estado actual de cada task.
-->

---

<!-- ======================================================================== -->
<!-- ESTRUCTURA MODO PLANO (sin tasks): Usar secciones de fase directas      -->
<!-- ESTRUCTURA MODO PARTICIONADA: Usar secciones de Task > Fases internas   -->
<!-- Elegir UNA estructura según el Modo del refinamiento. Eliminar la otra. -->
<!-- ======================================================================== -->

<!-- ═══ OPCIÓN A: MODO PLANO (eliminar si Modo = Particionada) ═══ -->

## Fase 1: [NOMBRE_FASE_1]

<!--
Contenido generado dinámicamente por >planificar_hu según arquitectura.
Ejemplos de subsecciones por arquitectura:

Hexagonal: Migraciones, Configuración
MVC: Migraciones, Configuración  
Script: Dependencias, Configuración
Frontend: Dependencias, Estructura de carpetas
-->

### [Subsección 1.1]

#### T01: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- [ ] Paso 2: [Descripción]
- **Estimación:** [X]h | **Dependencia:** -

---

## Fase 2: [NOMBRE_FASE_2]

<!--
Ejemplos por arquitectura:

Hexagonal: Entidades, Value Objects, Puertos
MVC: Modelos, Validaciones
Capas: Entidades, Repositorios
Script: Funciones principales
Frontend: Componentes, Props/State
-->

### [Subsección 2.1]

#### T02: [Título de la tarea] [PENDIENTE]
- [ ] [Descripción del paso]
- **Estimación:** [X]h | **Dependencia:** T01

---

## Fase 3: [NOMBRE_FASE_3]

<!--
Ejemplos por arquitectura:

Hexagonal: Casos de Uso, DTOs
MVC: Controladores, Rutas
Capas: Servicios, Lógica de negocio
Script: Orquestación, CLI args
Frontend: Hooks, Services, API calls
-->

### [Subsección 3.1]

#### T03: [Título de la tarea] [PENDIENTE]
- [ ] [Descripción del paso]
- **Estimación:** [X]h | **Dependencia:** T02

---

## Fase N: Testing

### Tests Unitarios

#### T[N]: Tests de [Componente] [PENDIENTE]
- [ ] Crear tests para [componente]
- [ ] Cubrir casos felices
- [ ] Cubrir casos de borde
- [ ] Cubrir casos de error
- **Estimación:** [X]h | **Dependencia:** [dependencias]

### Tests de Integración

#### T[N+1]: Tests de Integración [PENDIENTE]
- [ ] Crear tests de integración
- [ ] Validar flujo completo
- **Estimación:** [X]h | **Dependencia:** [dependencias]

<!-- ═══ OPCIÓN B: MODO PARTICIONADA (eliminar Opción A si se usa esta) ═══ -->

<!--
## Task [ID-HU]-T1: [Título de la task funcional]
**Traza CA padre:** CA-01
**Estimación:** [X] SP (~[Y]h)
**Depende de:** —

### Fase 1: [Nombre fase según arquitectura de la task]

#### T01: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- [ ] Paso 2: [Descripción]
- **Estimación:** [X]h | **Dependencia:** —

### Fase 2: [Nombre fase]

#### T02: [Título de la tarea] [PENDIENTE]
- [ ] [Descripción del paso]
- **Estimación:** [X]h | **Dependencia:** T01

### Fase N: Testing

#### T03: Tests [Componente] [PENDIENTE]
- [ ] Tests unitarios
- [ ] Tests integración
- **Estimación:** [X]h | **Dependencia:** T01, T02

### ✅ Validar CAs de T1 → ver refinamiento sección Task [ID-HU]-T1

> Los CAs granulares viven en el refinamiento (fuente de verdad).
> >validar_ca [ID-HU] --task_id [ID-HU]-T1 --scope granulares

| CA | Verificado |
|----|:----------:|
| CA-T1-01 | [ ] |
| CA-T1-02 | [ ] |

---

## Task [ID-HU]-T2: [Título de la task funcional]
**Traza CA padre:** CA-02
**Estimación:** [X] SP (~[Y]h)
**Depende de:** [ID-HU]-T1

### Fase 1: [Nombre fase]

#### T04: [Título de la tarea] [PENDIENTE]
- [ ] [Descripción del paso]
- **Estimación:** [X]h | **Dependencia:** T01 ⟵T1

> NOTA sobre dependencias cross-task:
> - Dependencia intra-task: "Dependencia: T05" (sin marca, misma task)
> - Dependencia cross-task: "Dependencia: T01 ⟵T1" (tarea T01 pertenece a task T1)
> El ejecutor usa la marca ⟵T[N] para validar que la task dependiente esté [EJECUTADA].

### ✅ Validar CAs de T2 → ver refinamiento sección Task [ID-HU]-T2

| CA | Verificado |
|----|:----------:|
| CA-T2-01 | [ ] |
-->

---

## Fase Final: Validar Criterios de Aceptación

> 📌 **Los CAs viven en el refinamiento** (fuente de verdad). Esta sección trackea ESTADO de verificación.
> Ejecutar: `>validar_ca [ID-HU] --scope integracion` (particionada) o `>validar_ca [ID-HU]` (plana)

### Estado de Verificación de CAs

<!--
MODO PLANO: Listar todos los CAs del refinamiento con checkbox de estado.
MODO PARTICIONADA: Listar solo los CAs de integración (padre).
NO copiar el texto completo del CA — solo el ID y un resumen corto.
-->

| CA | Resumen | Verificado |
|----|---------|:----------:|
| CA-01 | [Resumen corto del CA] | [ ] |
| CA-02 | [Resumen corto del CA] | [ ] |
| CA-03 | [Resumen corto del CA] | [ ] |

### Validación Final

- [ ] Todos los tests pasan: `[COMANDO_TEST]`
- [ ] Código compila/ejecuta sin errores
- [ ] Sin warnings críticos
- [ ] Revisión de código completada

---

## Notas de Implementación

### Decisiones Técnicas
[Documentar decisiones tomadas durante la planificación que NO están en el refinamiento]

> 📌 Riesgos y dependencias ya documentados en el refinamiento. No duplicar aquí.

---

## Historial de Ejecución

<!-- Modo Plano: usar tabla sin columna Task -->
| Fecha | Acción | Tarea | Resultado |
|-------|--------|-------|-----------|
| [FECHA] | Inicio | - | Plan creado |

<!-- Modo Particionada: usar tabla CON columna Task -->
<!--
| Fecha | Acción | Task | Tarea | Resultado |
|-------|--------|------|-------|-----------|
| [FECHA] | Inicio | — | — | Plan creado |
-->
