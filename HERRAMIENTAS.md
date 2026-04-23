# 🛠️ Herramientas del Sistema SAC

> **Versión:** 7.2.0  
> **Última actualización:** 23 de abril de 2026

---

## 📋 Descripción

Índice oficial de herramientas disponibles en el sistema SAC v7.2.0. Cada herramienta tiene un archivo `.tool.md` con su definición completa.

---

## 📦 Herramientas Disponibles

| Herramienta | Comando | Roles Autorizados | Archivo |
|-------------|---------|-------------------|---------|
| Tomar Contexto | `>tomar_contexto` | ONAD, ARCHDEV, DEVOPS, REFINADOR | `herramientas/tomar_contexto.tool.md` |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` | ONAD | `herramientas/init_reglas_arquitectonicas.tool.md` |
| Refinar HU | `>refinar_hu` | REFINADOR | `herramientas/refinar_hu.tool.md` |
| Validar HU | `>validar_hu` | ONAD | `herramientas/validar_hu.tool.md` |
| Planificar HU | `>planificar_hu` | ONAD | `herramientas/planificar_hu.tool.md` |
| Ejecutar Plan | `>ejecutar_plan` | ARCHDEV | `herramientas/ejecutar_plan.tool.md` |
| Crear Pruebas | `>crear_pruebas` | ARCHDEV | `herramientas/crear_pruebas.tool.md` |
| Analizar Code Smells | `>analizar_code_smells` | ARCHDEV | `herramientas/analizar_code_smells.tool.md` |
| Diagnosticar DevOps | `>diagnosticar_devops` | DEVOPS | `herramientas/diagnosticar_devops.tool.md` |
| Generar Commit | `>generar_commit` | ARTESANO, ARCHDEV, DEVOPS, REFINADOR | `herramientas/generar_commit.tool.md` |

**Total:** 10 herramientas activas

---

## 📊 Herramientas por Agente

### @arquitecto (Arquitecto)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Analizar Stack | `>analizar_stack` |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` |
| Generar ADR | `>generar_adr` |
| Validar HU | `>validar_hu` |
| Planificar HU | `>planificar_hu` |

### @desarrollador (Desarrollador)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Analizar Stack | `>analizar_stack` |
| Generar ADR | `>generar_adr` |
| Ejecutar Plan | `>ejecutar_plan` |
| Crear Pruebas | `>crear_pruebas` |
| Analizar Code Smells | `>analizar_code_smells` |
| Generar Commit | `>generar_commit` |

### @devops (DevOps)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Generar ADR | `>generar_adr` |
| Diagnosticar DevOps | `>diagnosticar_devops` |
| Generar Commit | `>generar_commit` |

### @analista_historias (Analista de Requisitos)

| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Refinar HU | `>refinar_hu` |
| Generar Commit | `>generar_commit` |

### @narrador_commit (Cronista de Cambios)

| Herramienta | Comando |
|-------------|---------|
| Generar Commit | `>generar_commit` |

---

## 📂 Categorías

| Categoría | Herramientas |
|-----------|--------------|
| **Contexto** | `>tomar_contexto`, `>analizar_stack` |
| **Arquitectura** | `>init_reglas_arquitectonicas`, `>generar_adr` |
| **Historias de Usuario** | `>refinar_hu`, `>validar_hu`, `>planificar_hu` |
| **Implementación** | `>ejecutar_plan`, `>crear_pruebas` |
| **Calidad de Código** | `>analizar_code_smells` |
| **DevOps** | `>diagnosticar_devops` |
| **Documentación** | `>generar_commit` |

---

## 🆕 Agregar Nueva Herramienta

1. Copiar `plantillas/herramienta_plantilla.tool.md`
2. Guardar en `herramientas/[nombre].tool.md`
3. Actualizar esta tabla
4. Verificar roles autorizados en los agentes correspondientes

---

## 📚 Referencias

| Recurso | Ubicación |
|---------|-----------|
| Plantilla de herramienta | `plantillas/herramienta_plantilla.tool.md` |
| Roles del sistema | `ROLES.md` |
| Guía de comandos | `guias/guia_comandos.md` |

---

## 📅 Historial

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 7.2.0 | 23 abr 2026 | Añadidas `>analizar_stack` y `>generar_adr`; tablas por agente con nombres nuevos |
| 4.0 | 6 ene 2026 | Reescritura completa v4.0, movido a raíz, eliminadas herramientas inexistentes |
| 3.1 | 5 ene 2026 | Versión anterior en `herramientas/herramientas-activas.md` |
