---
tipo: plan_implementacion
version: "2.0"
generado_por: ">planificar_hu"
actualizado_por: ">ejecutar_plan"
---

#  Plan de Implementación: [ID-HU] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **HU** | [ID-HU] |
| **Título** | [Título de la HU] |
| **Arquitectura** | [Hexagonal\|MVC\|Capas\|Script\|Monolito] |
| **Generado por** | ONAD |
| **Fecha creación** | [FECHA_ISO_8601] |
| **Última actualización** | [FECHA_ISO_8601] |
| **Estimación total** | [X] horas |
| **Estado** | [PENDIENTE \| EN_PROGRESO \| COMPLETADO \| BLOQUEADO] |

## Progreso General

<!--
INSTRUCCIÓN PARA >planificar_hu:
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
-->

| Fase | Estado | Progreso |
|------|--------|----------|
| Fase 1: [NOMBRE_FASE_1] | [ESTADO] | [X/Y] tareas |
| Fase 2: [NOMBRE_FASE_2] | [ESTADO] | [X/Y] tareas |
| Fase 3: [NOMBRE_FASE_3] | [ESTADO] | [X/Y] tareas |
| Fase N: Testing | [ESTADO] | [X/Y] tareas |
| Fase Final: Validación CA | [ESTADO] | [X/Y] criterios |

---

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

---

## Fase Final: Validar Criterios de Aceptación

>  **IMPORTANTE:** Copiar criterios de aceptación de la HU.
> Al validar cada criterio, marcarlo aquí Y en la HU.

### Criterios de Aceptación

- [ ] **CA-01:** [Descripción del criterio de aceptación 1]
- [ ] **CA-02:** [Descripción del criterio de aceptación 2]
- [ ] **CA-03:** [Descripción del criterio de aceptación 3]

### Validación Final

- [ ] Todos los tests pasan: `[COMANDO_TEST]`
- [ ] Código compila/ejecuta sin errores
- [ ] Sin warnings críticos
- [ ] Revisión de código completada

---

## Notas de Implementación

### Consideraciones Especiales
[Agregar notas relevantes para la implementación]

### Decisiones Técnicas
[Documentar decisiones tomadas durante la planificación]

### Riesgos Identificados
| Riesgo | Mitigación |
|--------|------------|
| [Riesgo 1] | [Estrategia de mitigación] |

---

## Historial de Ejecución

| Fecha | Acción | Tarea | Resultado |
|-------|--------|-------|-----------|
| [FECHA] | Inicio | - | Plan creado |
