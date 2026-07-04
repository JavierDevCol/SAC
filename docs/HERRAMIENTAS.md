# 🛠️ Herramientas del Sistema SAC

> **Versión:** 7.25.0
> **Última actualización:** 27 de junio de 2026

---

## 📋 Descripción

Índice oficial de herramientas disponibles en el sistema SAC v7.25.0. Cada herramienta tiene un archivo `.tool.yaml` con su definición completa.

---

## 📦 Herramientas Disponibles

| Herramienta | Comando | Roles Autorizados | Archivo |
|-------------|---------|-------------------|---------|
| Tomar Contexto | `>tomar_contexto` | ONAD, ARCHDEV, DEVOPS, REFINADOR | `herramientas/tomar_contexto.tool.yaml` |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` | ONAD | `herramientas/init_reglas_arquitectonicas.tool.yaml` |
| Generar ADR | `>generar_adr` | ONAD, ARCHDEV, DEVOPS | `herramientas/generar_adr.tool.yaml` |
| Refinar HU | `>refinar_hu` | REFINADOR | `herramientas/refinar_hu.tool.yaml` |
| Validar HU | `>validar_hu` | ONAD | `herramientas/validar_hu.tool.yaml` |
| Planificar HU | `>planificar_hu` | ARCHDEV | `herramientas/planificar_hu.tool.yaml` |
| Ejecutar Plan | `>ejecutar_plan` | ARCHDEV | `herramientas/ejecutar_plan.tool.yaml` |
| Validar CA | `>validar_ca` | ARCHDEV | `herramientas/validar_ca.tool.yaml` |
| Crear Pruebas | `>crear_pruebas` | ARCHDEV | `herramientas/crear_pruebas.tool.yaml` |
| Analizar Code Smells | `>analizar_code_smells` | ARCHDEV | `herramientas/analizar_code_smells.tool.yaml` |
| Diagnosticar DevOps | `>diagnosticar_devops` | DEVOPS | `herramientas/diagnosticar_devops.tool.yaml` |
| Registrar Bug | `>registrar_bug` | ONAD, ARCHDEV | `herramientas/registrar_bug.tool.yaml` |
| Registrar Pendiente | `>registrar_pendiente` | ONAD | `herramientas/registrar_pendiente.tool.yaml` |
| Registrar Hallazgo | `>registrar_hallazgo` | ONAD, ARCHDEV | `herramientas/registrar_hallazgo.tool.yaml` |
| Sincronizar Backlog | `>sincronizar_backlog` | ONAD, ARCHDEV, REFINADOR | `herramientas/sincronizar_backlog.tool.yaml` |

**Total:** 15 herramientas activas

---

## 📊 Herramientas por Agente

### @arquitecto (Arquitecto)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` |
| Generar ADR | `>generar_adr` |
| Validar HU | `>validar_hu` |
| Registrar Bug | `>registrar_bug` |
| Registrar Pendiente | `>registrar_pendiente` |
| Registrar Hallazgo | `>registrar_hallazgo` |
| Sincronizar Backlog | `>sincronizar_backlog` |

### @desarrollador (Desarrollador)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Generar ADR | `>generar_adr` |
| Planificar HU | `>planificar_hu` |
| Ejecutar Plan | `>ejecutar_plan` |
| Validar CA | `>validar_ca` |
| Crear Pruebas | `>crear_pruebas` |
| Analizar Code Smells | `>analizar_code_smells` |
| Registrar Bug | `>registrar_bug` |
| Registrar Hallazgo | `>registrar_hallazgo` |
| Sincronizar Backlog | `>sincronizar_backlog` |

### @devops (DevOps)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Generar ADR | `>generar_adr` |
| Diagnosticar DevOps | `>diagnosticar_devops` |

### @analista_historias (Analista de Requisitos)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Refinar HU | `>refinar_hu` |
| Sincronizar Backlog | `>sincronizar_backlog` |

### @cronista_de_cambios (Cronista de Cambios)

| Herramienta | Comando |
|-------------|---------|
| Registrar Hallazgo | `>registrar_hallazgo` |

---

## 🤖 Sub-Agentes

Los sub-agentes se configuran a nivel de plataforma (opencode, claude, etc.) y son invocados por las herramientas para tareas de validación.

| Sub-agente | Propósito | Permisos | Herramientas que lo invocan |
|------------|-----------|----------|----------------------------|
| `validador-calidad` | Validar CAs, alineación arquitectónica, ambigüedades, existencia de archivos | Solo lectura | `>validar_ca`, `>validar_hu`, `>refinar_hu`, `>sincronizar_backlog`, `>registrar_hallazgo` |
| `validador-compilacion` | Verificar compilación y ejecutar tests | Lectura + bash | `>ejecutar_plan` |

---

## 📂 Categorías

| Categoría | Herramientas |
|-----------|--------------|
| **Contexto** | `>tomar_contexto` |
| **Arquitectura** | `>init_reglas_arquitectonicas`, `>generar_adr` |
| **Historias de Usuario** | `>refinar_hu`, `>validar_hu`, `>planificar_hu`, `>validar_ca` |
| **Implementación** | `>ejecutar_plan`, `>crear_pruebas` |
| **Calidad de Código** | `>analizar_code_smells` |
| **DevOps** | `>diagnosticar_devops` |
| **Bugs y Hallazgos** | `>registrar_bug`, `>registrar_pendiente`, `>registrar_hallazgo` |
| **Backlog** | `>sincronizar_backlog` |

---

## 🆕 Agregar Nueva Herramienta

1. Copiar `plantillas/herramienta_plantilla.tool.yaml`
2. Guardar en `herramientas/[nombre].tool.yaml`
3. Actualizar esta tabla
4. Verificar roles autorizados en los agentes correspondientes

---

## 📚 Referencias

| Recurso | Ubicación |
|---------|-----------|
| Plantilla de herramienta | `plantillas/herramienta_plantilla.tool.yaml` |
| Roles del sistema | `ROLES.md` |
| Guía de comandos | `guias/guia_comandos.md` |

---

## 📅 Historial

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 7.25.0 | 27 jun 2026 | Agregadas 7 herramientas, sub-agentes, corregidos roles |
| 7.2.0 | 23 abr 2026 | Añadida `>generar_adr`; tablas por agente con nombres nuevos |
| 4.0 | 6 ene 2026 | Reescritura completa v4.0, movido a raíz, eliminadas herramientas inexistentes |
| 3.1 | 5 ene 2026 | Versión anterior en `herramientas/herramientas-activas.md` |
