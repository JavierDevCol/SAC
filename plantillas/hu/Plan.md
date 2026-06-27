---
tipo: plan_implementacion
version: "5.0"
generado_por: ">planificar_hu"
actualizado_por: ">ejecutar_plan"
validado_por: ">validar_ca"
---

# Plan de Implementación: [ID-HU] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **HU** | [ID-HU] |
| **Título** | [Título de la HU] |
| **Refinamiento** | [ID-HU]/Refinamiento.md |
| **Arquitectura** | [Hexagonal\|MVC\|Capas\|Script\|Monolito] |
| **Generado por** | ArchDev Pro |
| **Fecha creación** | [FECHA_ISO_8601] |
| **Última actualización** | [FECHA_ISO_8601] |
| **Estimación total** | [X] horas |
| **Estado** | [PENDIENTE \| EN_PROGRESO \| COMPLETADO \| BLOQUEADO] |
| **Modo** | [Plano \| Particionada] |
| **Tasks** | [— \| [ID-HU]-TASK-1, [ID-HU]-TASK-2, ...] |

## Progreso General

<!-- MODO PLANO: Tabla por fases -->
| Fase | Estado | Progreso |
|------|--------|----------|
| Fase 1: [NOMBRE_FASE_1] | [ESTADO] | [X/Y] tareas |
| Fase 2: [NOMBRE_FASE_2] | [ESTADO] | [X/Y] tareas |
| Fase N: Testing | [ESTADO] | [X/Y] tareas |
| Fase Final: Validación CA | [ESTADO] | [X/Y] criterios |

<!-- MODO PARTICIONADO: Tabla por tasks -->
<!--
| Task | Descripción | Estado | Progreso |
|------|-------------|--------|----------|
| [ID-HU]-TASK-1 | [Título task 1] | [ESTADO] | [X/Y] tareas |
| [ID-HU]-TASK-2 | [Título task 2] | [ESTADO] | [X/Y] tareas |
| — | Validación CA Integración | [ESTADO] | [X/Y] criterios |
-->

---

## Dependencias entre Tasks

<!-- Solo si Modo = Particionada -->

| Task | Depende de | Razón | Ejecutable? |
|------|-----------|-------|:-----------:|
| [ID-HU]-TASK-1 | — | Sin dependencias | ✅ |
| [ID-HU]-TASK-2 | [ID-HU]-TASK-1 | [Razón] | ⛔ |

---

## Fase 1: [NOMBRE_FASE_1]

### [Subsección 1.1]

#### EJEC-01: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- [ ] Paso 2: [Descripción]
- **Estimación:** [X]h | **Dependencia:** -

---

## Fase 2: [NOMBRE_FASE_2]

### [Subsección 2.1]

#### EJEC-02: [Título de la tarea] [PENDIENTE]
- [ ] [Descripción del paso]
- **Estimación:** [X]h | **Dependencia:** EJEC-01

---

## Fase N: Testing

### Tests Unitarios

#### EJEC-[N]: Tests de [Componente] [PENDIENTE]
- [ ] Crear tests para [componente]
- [ ] Cubrir casos felices
- [ ] Cubrir casos de borde
- [ ] Cubrir casos de error
- **Estimación:** [X]h | **Dependencia:** [dependencias]

### Tests de Integración

#### EJEC-[N+1]: Tests de Integración [PENDIENTE]
- [ ] Crear tests de integración
- [ ] Validar flujo completo
- **Estimación:** [X]h | **Dependencia:** [dependencias]

---

## Fase Final: Validar Criterios de Aceptación

> 📌 **Los CAs viven en el refinamiento** (fuente de verdad). Esta sección trackea ESTADO de verificación.

### Estado de Verificación de CAs

| CA | Resumen | Verificado |
|----|---------|:----------:|
| CA-01 | [Resumen corto del CA] | [ ] |
| CA-02 | [Resumen corto del CA] | [ ] |

### Validación Final

- [ ] Todos los tests pasan: `[COMANDO_TEST]`
- [ ] Código compila/ejecuta sin errores
- [ ] Sin warnings críticos
- [ ] Revisión de código completada

---

## Notas de Implementación

### Decisiones Técnicas

[Documentar decisiones tomadas durante la planificación]

---

## Historial de Ejecución

| Fecha | Acción | Tarea | Resultado |
|-------|--------|-------|-----------|
| [FECHA] | Inicio | — | Plan creado |

---

> **Archivo:** `{{artifacts.hu_folder}}/[ID-HU]/Plan.md`
> **Creado por:** `>planificar_hu`
> **Actualizado por:** `>ejecutar_plan`
