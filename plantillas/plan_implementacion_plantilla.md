---
tipo: plan_implementacion
version: "1.0"
generado_por: ">planificar_hu"
actualizado_por: ">ejecutar_plan"
---

# 📋 Plan de Implementación: [ID-HU] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **HU** | [ID-HU] |
| **Título** | [Título de la HU] |
| **Generado por** | ONAD |
| **Fecha creación** | [FECHA_ISO_8601] |
| **Última actualización** | [FECHA_ISO_8601] |
| **Estimación total** | [X] horas |
| **Estado** | [PENDIENTE \| EN_PROGRESO \| COMPLETADO \| BLOQUEADO] |

## Progreso General

| Fase | Estado | Progreso |
|------|--------|----------|
| Fase 1: Infraestructura | [ESTADO] | [X/Y] tareas |
| Fase 2: Dominio | [ESTADO] | [X/Y] tareas |
| Fase 3: Aplicación | [ESTADO] | [X/Y] tareas |
| Fase 4: Adaptadores | [ESTADO] | [X/Y] tareas |
| Fase 5: Testing | [ESTADO] | [X/Y] tareas |
| Fase Final: Validación CA | [ESTADO] | [X/Y] criterios |

---

## Fase 1: Infraestructura

### Migraciones

#### T01: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- [ ] Paso 2: [Descripción]
- **Estimación:** [X]h | **Dependencia:** -

#### T02: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- **Estimación:** [X]h | **Dependencia:** T01

### Configuración

#### T03: [Título de la tarea] [PENDIENTE]
- [ ] Paso 1: [Descripción]
- **Estimación:** [X]h | **Dependencia:** -

---

## Fase 2: Dominio

### Entidades

#### T04: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[Entidad].java` en `domain/model/`
  ```java
  // Código esqueleto (opcional)
  ```
- **Estimación:** [X]h | **Dependencia:** T01

### Value Objects

#### T05: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[ValueObject].java` en `domain/model/`
- **Estimación:** [X]h | **Dependencia:** -

### Puertos (Interfaces)

#### T06: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[Puerto]Port.java` en `domain/ports/`
- **Estimación:** [X]h | **Dependencia:** T04

---

## Fase 3: Aplicación

### Casos de Uso

#### T07: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[CasoDeUso]UseCase.java` en `application/usecases/`
- [ ] Implementar lógica de negocio
- [ ] Inyectar dependencias via constructor
- **Estimación:** [X]h | **Dependencia:** T06

### DTOs

#### T08: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[Nombre]Request.java` en `application/dto/`
- [ ] Crear `[Nombre]Response.java` en `application/dto/`
- **Estimación:** [X]h | **Dependencia:** -

---

## Fase 4: Adaptadores

### Controllers (Adaptadores de Entrada)

#### T09: [Título de la tarea] [PENDIENTE]
- [ ] Crear/Modificar `[Controller].java` en `infrastructure/adapters/in/`
- [ ] Implementar endpoint REST
- [ ] Mapear DTOs
- **Estimación:** [X]h | **Dependencia:** T07, T08

### Repositorios (Adaptadores de Salida)

#### T10: [Título de la tarea] [PENDIENTE]
- [ ] Crear `[Repositorio]Adapter.java` en `infrastructure/adapters/out/`
- [ ] Implementar puerto de persistencia
- **Estimación:** [X]h | **Dependencia:** T06

---

## Fase 5: Testing

### Tests Unitarios

#### T11: Tests de Dominio [PENDIENTE]
- [ ] Crear `[Entidad]Test.java`
- [ ] Cubrir casos felices
- [ ] Cubrir casos de borde
- [ ] Cubrir casos de error
- **Estimación:** [X]h | **Dependencia:** T04, T05

#### T12: Tests de Casos de Uso [PENDIENTE]
- [ ] Crear `[CasoDeUso]UseCaseTest.java`
- [ ] Mockear dependencias
- [ ] Verificar interacciones
- **Estimación:** [X]h | **Dependencia:** T07

### Tests de Integración

#### T13: Tests de Adaptadores [PENDIENTE]
- [ ] Crear `[Controller]IntegrationTest.java`
- [ ] Usar Testcontainers si aplica
- [ ] Validar flujo completo
- **Estimación:** [X]h | **Dependencia:** T09, T10

---

## Fase Final: Validar Criterios de Aceptación

> ⚠️ **IMPORTANTE:** Esta sección contiene los criterios de aceptación copiados de la HU.
> Al validar cada criterio, marcarlo como [X] aquí Y en la HU correspondiente.

### Criterios de Aceptación

- [ ] **CA-01:** [Descripción del criterio de aceptación 1]
- [ ] **CA-02:** [Descripción del criterio de aceptación 2]
- [ ] **CA-03:** [Descripción del criterio de aceptación 3]

### Validación Final

- [ ] Todos los tests pasan: `[COMANDO_TEST]`
- [ ] Código compila sin errores
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
| [FECHA] | Ejecución | T01 | ✅ Completada |
| [FECHA] | Ejecución | T02 | ❌ Error: [descripción] |
