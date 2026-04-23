# 📐 Reglas Arquitectónicas del Proyecto

> **Proyecto:** {{proyecto.nombre}}  
> **Stack:** {{proyecto.stack}}  
> **Generado:** {{fecha}}  
> **Versión:** 1.0  
> **Aprobado por:** {{usuario.nombre}}

---

## 📋 Índice

1. [Nomenclatura](#1-nomenclatura)
2. [Arquitectura](#2-arquitectura)
3. [Patrones de Diseño](#3-patrones-de-diseño)
4. [Principios y Paradigmas](#4-principios-y-paradigmas)
5. [Dependencias](#5-dependencias)
6. [Testing](#6-testing)
7. [Documentación](#7-documentación)
8. [Seguridad y Calidad](#8-seguridad-y-calidad)
9. [Checklist de Validación](#9-checklist-de-validación)

---

## 1. Nomenclatura

### 1.1 Convenciones Generales

| Elemento | Convención | Ejemplo | Anti-patrón |
|----------|------------|---------|-------------|
| Clases/Tipos | {{nomenclatura.clases}} | {{nomenclatura.ejemplo_clase}} | {{nomenclatura.antipatron_clase}} |
| Métodos/Funciones | {{nomenclatura.metodos}} | {{nomenclatura.ejemplo_metodo}} | {{nomenclatura.antipatron_metodo}} |
| Variables | {{nomenclatura.variables}} | {{nomenclatura.ejemplo_variable}} | {{nomenclatura.antipatron_variable}} |
| Constantes | {{nomenclatura.constantes}} | {{nomenclatura.ejemplo_constante}} | {{nomenclatura.antipatron_constante}} |
| Interfaces | {{nomenclatura.interfaces}} | {{nomenclatura.ejemplo_interface}} | {{nomenclatura.antipatron_interface}} |
| Implementaciones | {{nomenclatura.implementaciones}} | {{nomenclatura.ejemplo_impl}} | {{nomenclatura.antipatron_impl}} |

### 1.2 Patrones de Nombres por Tipo

| Tipo de Clase | Patrón | Ejemplo |
|---------------|--------|---------|
| Entidad | `{Sustantivo}` | `Usuario`, `Pedido`, `Producto` |
| Value Object | `{Concepto}` | `Dinero`, `Email`, `Direccion` |
| Servicio de Dominio | `{Dominio}Service` | `TransferenciaService` |
| Caso de Uso | `{Accion}{Entidad}UseCase` | `CrearPedidoUseCase` |
| Repositorio | `{Entidad}Repository` | `UsuarioRepository` |
| Controlador/Handler | `{Recurso}Controller` | `PedidoController` |
| DTO Request | `{Accion}{Entidad}Request` | `CrearUsuarioRequest` |
| DTO Response | `{Entidad}Response` | `UsuarioResponse` |
| Excepción | `{Dominio}Exception` | `PagoRechazadoException` |
| Evento | `{Entidad}{Accion}Event` | `PedidoCreadoEvent` |
| Factory | `{Entidad}Factory` | `PedidoFactory` |
| Builder | `{Entidad}Builder` | `PedidoBuilder` |

### 1.3 Prefijos y Sufijos

| Uso | Prefijo/Sufijo | Ejemplo | Cuándo Usar |
|-----|----------------|---------|-------------|
| Interfaces | {{nomenclatura.prefijo_interface}} | {{nomenclatura.ejemplo_interface}} | {{nomenclatura.cuando_interface}} |
| Implementaciones | {{nomenclatura.sufijo_impl}} | {{nomenclatura.ejemplo_impl}} | {{nomenclatura.cuando_impl}} |
| Test classes | `Test` sufijo | `UsuarioServiceTest` | Siempre para tests |
| Mocks | `Mock` prefijo | `MockUsuarioRepository` | En tests |

---

## 2. Arquitectura

### 2.1 Estilo Arquitectónico

**Patrón Principal:** {{arquitectura.estilo}}

{{arquitectura.descripcion}}

### 2.2 Estructura de Carpetas/Paquetes

```
{{arquitectura.estructura}}
```

### 2.3 Reglas de Dependencia

```
{{arquitectura.diagrama_dependencias}}
```

**Regla:** {{arquitectura.regla_dependencias}}

| Capa | Puede Importar | NO Puede Importar |
|------|----------------|-------------------|
| Domain | Nada externo | Application, Infrastructure |
| Application | Domain | Infrastructure |
| Infrastructure | Domain, Application | - |

### 2.4 Domain-Driven Design

**Nivel de DDD:** {{arquitectura.nivel_ddd}}

| Táctica DDD | Uso | Descripción |
|-------------|-----|-------------|
| Aggregates | {{ddd.aggregates}} | {{ddd.desc_aggregates}} |
| Value Objects | {{ddd.value_objects}} | {{ddd.desc_value_objects}} |
| Domain Events | {{ddd.domain_events}} | {{ddd.desc_domain_events}} |
| Repositories | {{ddd.repositories}} | {{ddd.desc_repositories}} |
| Domain Services | {{ddd.domain_services}} | {{ddd.desc_domain_services}} |

---

## 3. Patrones de Diseño

### 3.1 Patrones Obligatorios

| Patrón | Cuándo Usar | Ejemplo de Aplicación |
|--------|-------------|----------------------|
{{#each patrones.obligatorios}}
| {{nombre}} | {{cuando}} | {{ejemplo}} |
{{/each}}

### 3.2 Patrones Prohibidos

| Patrón | Razón | Alternativa |
|--------|-------|-------------|
{{#each patrones.prohibidos}}
| {{nombre}} | {{razon}} | {{alternativa}} |
{{/each}}

### 3.3 Guía de Selección de Patrones

| Situación | Patrón Recomendado | Justificación |
|-----------|-------------------|---------------|
| Creación de objetos complejos (>3 params) | {{patrones.creacion_compleja}} | {{patrones.just_creacion}} |
| Múltiples algoritmos intercambiables | Strategy | Open/Closed principle |
| Acceso a datos externos | Repository | Abstracción de persistencia |
| Llamadas a servicios externos | Adapter | Aislamiento de dependencias |
| Operaciones que pueden fallar | Circuit Breaker | Resiliencia |
| Notificación de cambios | Observer/Events | Desacoplamiento |

---

## 4. Principios y Paradigmas

### 4.1 Principios SOLID

**Nivel de aplicación:** {{principios.nivel_solid}}

| Principio | Obligatorio | Guía de Aplicación |
|-----------|-------------|-------------------|
| **S**ingle Responsibility | {{solid.srp}} | Una clase = una razón para cambiar |
| **O**pen/Closed | {{solid.ocp}} | Abierto a extensión, cerrado a modificación |
| **L**iskov Substitution | {{solid.lsp}} | Subtipos intercambiables con tipos base |
| **I**nterface Segregation | {{solid.isp}} | Interfaces pequeñas y específicas |
| **D**ependency Inversion | {{solid.dip}} | Depender de abstracciones, no concreciones |

### 4.2 Principios Adicionales

| Principio | Aplicación |
|-----------|------------|
| DRY | {{principios.dry}} |
| KISS | {{principios.kiss}} |
| YAGNI | {{principios.yagni}} |

### 4.3 Inmutabilidad

**Política:** {{principios.inmutabilidad}}

- [ ] Usar `final`/`readonly`/`const` por defecto
- [ ] Preferir Records/Data Classes inmutables para DTOs
- [ ] Value Objects siempre inmutables
- [ ] Colecciones inmutables donde sea posible

### 4.4 Manejo de Null

**Política:** {{principios.null_policy}}

| Situación | Manejo Requerido |
|-----------|------------------|
| Retorno de métodos | {{null.retorno}} |
| Parámetros opcionales | {{null.parametros}} |
| Campos opcionales | {{null.campos}} |

### 4.5 Paradigma

**Paradigma predominante:** {{principios.paradigma}}

| Aspecto | Enfoque |
|---------|---------|
| Estructura | {{paradigma.estructura}} |
| Lógica de negocio | {{paradigma.logica}} |
| Transformaciones de datos | {{paradigma.transformaciones}} |

### 4.6 Composición vs Herencia

**Política:** {{principios.composicion_herencia}}

- ✅ **Usar herencia cuando:** Framework lo requiere, es-un verdadero
- ❌ **Evitar herencia cuando:** Solo para reutilizar código, más de 2 niveles

---

## 5. Dependencias

### 5.1 Dependencias Aprobadas

#### Testing
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
{{#each dependencias.testing}}
| {{nombre}} | {{version}} | {{uso}} |
{{/each}}

#### Logging
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
{{#each dependencias.logging}}
| {{nombre}} | {{version}} | {{uso}} |
{{/each}}

#### Utilidades
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
{{#each dependencias.utilidades}}
| {{nombre}} | {{version}} | {{uso}} |
{{/each}}

### 5.2 Dependencias Prohibidas

| Librería | Razón | Alternativa |
|----------|-------|-------------|
{{#each dependencias.prohibidas}}
| {{nombre}} | {{razon}} | {{alternativa}} |
{{/each}}

### 5.3 Política de Actualizaciones

**Estrategia:** {{dependencias.politica_actualizacion}}

- {{dependencias.detalle_politica}}

---

## 6. Testing

### 6.1 Metodología

**Enfoque principal:** {{testing.metodologia}}

### 6.2 Cobertura

| Capa | Cobertura Mínima | Tipo de Tests |
|------|------------------|---------------|
| Domain | {{testing.cobertura_domain}}% | Unitarios |
| Application | {{testing.cobertura_application}}% | Unitarios + Integración |
| Infrastructure | {{testing.cobertura_infrastructure}}% | Integración |
| **Global** | **{{testing.cobertura_global}}%** | Todos |

### 6.3 Convención de Nombres

**Patrón:** `{{testing.patron_nombres}}`

**Ejemplos:**
```
{{testing.ejemplos_nombres}}
```

### 6.4 Estructura de Tests

**Patrón:** {{testing.patron_estructura}}

```{{proyecto.lenguaje}}
{{testing.ejemplo_estructura}}
```

### 6.5 Tests de Integración

**Herramienta:** {{testing.herramienta_integracion}}

**Configuración:**
- {{testing.config_integracion}}

---

## 7. Documentación

### 7.1 Documentación de Código

**Obligatoria en:**
{{#each documentacion.obligatoria}}
- [ ] {{this}}
{{/each}}

**Formato de comentarios:**
```{{proyecto.lenguaje}}
{{documentacion.formato_comentarios}}
```

### 7.2 Architecture Decision Records (ADRs)

**Formato:** {{documentacion.formato_adr}}

**Ubicación:** {{artifacts.adr_folder}}

**Plantilla:**
```markdown
{{documentacion.plantilla_adr}}
```

### 7.3 README por Módulo

- [ ] Cada módulo/paquete principal debe tener README
- [ ] Incluir: propósito, dependencias, ejemplos de uso

---

## 8. Seguridad y Calidad

### 8.1 Datos Sensibles

**Regla de logging:** {{seguridad.regla_logging}}

| Tipo de Dato | Loguear | Acción |
|--------------|---------|--------|
| Passwords | ❌ NUNCA | No incluir en ningún log |
| Tokens/API Keys | ❌ NUNCA | Enmascarar si necesario |
| PII (emails, nombres) | ⚠️ Enmascarar | `***@domain.com` |
| IDs de transacción | ✅ Permitido | Para trazabilidad |

### 8.2 Validación de Entradas

**Política:** {{seguridad.validacion_entradas}}

- [ ] Validar en punto de entrada (Controllers/Handlers)
- [ ] Validar en constructores de dominio (fail-fast)
- [ ] Usar framework de validación: {{seguridad.framework_validacion}}

### 8.3 Límites de Código

| Métrica | Límite | Acción si Excede |
|---------|--------|------------------|
| Líneas por método | {{calidad.max_lineas_metodo}} | Extraer métodos |
| Líneas por clase | {{calidad.max_lineas_clase}} | Dividir responsabilidades |
| Parámetros por método | {{calidad.max_parametros}} | Usar objeto de parámetros |
| Complejidad ciclomática | {{calidad.max_complejidad}} | Simplificar lógica |
| Profundidad de herencia | {{calidad.max_herencia}} | Preferir composición |

### 8.4 Análisis Estático

**Herramientas obligatorias:**
{{#each calidad.herramientas_estaticas}}
- {{this}}
{{/each}}

**Configuración:** {{calidad.config_estatico}}

---

## 9. Checklist de Validación

### Para Code Reviews

- [ ] ¿Sigue las convenciones de nomenclatura?
- [ ] ¿Respeta las capas arquitectónicas?
- [ ] ¿Usa los patrones obligatorios correctamente?
- [ ] ¿Tiene tests con cobertura mínima?
- [ ] ¿Documenta según las reglas?
- [ ] ¿No usa dependencias prohibidas?
- [ ] ¿No loguea datos sensibles?
- [ ] ¿Métodos/clases dentro de límites de tamaño?

### Para Pull Requests

- [ ] Tests pasan ✅
- [ ] Cobertura >= {{testing.cobertura_global}}%
- [ ] Sin warnings de análisis estático
- [ ] Documentación actualizada si aplica
- [ ] ADR creado si hay decisión arquitectónica

---

## 📜 Historial de Cambios

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | {{fecha}} | {{usuario.nombre}} | Versión inicial |

---

{{#if usuario.incluir_firma_en_documentos}}
---
✅ Aprobado por **{{usuario.nombre}}** | 📅 {{fecha}}
---
{{/if}}
