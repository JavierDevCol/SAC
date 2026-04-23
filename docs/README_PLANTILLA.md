# 📘 Plantillas del Sistema COCHAS

> **Versión:** 7.0  
> **Última actualización:** 13 de febrero de 2026

---

## 🎯 Propósito

Este documento es el **índice central** de plantillas para crear nuevos roles (`.agent.md`) y herramientas (`.tool.md`) en el sistema COCHAS v4.0.

---

## 📁 Estructura de Plantillas

```
plantillas/
├── agente_plantilla.agent.md          # Plantilla para roles/agentes
├── herramienta_plantilla.tool.md      # Plantilla para herramientas
├── backlog_desarrollo_plantilla.md    # Plantilla para backlog de HU
├── contexto_proyecto_plantilla.md     # Plantilla para contexto de proyecto
├── refinamiento_hu_plantilla.md       # Plantilla para refinamientos de HU
├── plan_implementacion_plantilla.md   # Plantilla para planes de implementación
├── adr_nygard.plantilla.md            # Plantilla ADR formato Nygard
├── adr_madr.plantilla.md              # Plantilla ADR formato MADR
├── adr_y_statement.plantilla.md       # Plantilla ADR formato Y-Statement
└── workspace_plantilla.md             # Plantilla para workspace multi-proyecto
```

---

## 🤖 Plantilla: Rol/Agente (`.agent.md`)

> **Ubicación destino:** `agentes/[nombre].agent.md`  
> **Audiencia:** IA  
> **📄 Plantilla completa:** `plantillas/agente_plantilla.agent.md`

La plantilla de agentes incluye:

- ✅ Sección `mandatory` con 5 instrucciones base estándar
- ✅ Estructura completa de `identidad`, `especializacion`, `inicializacion`
- ✅ Definición de `herramientas` y `comandos` universales
- ✅ Sección `niveles` (opcional) para adaptar comportamiento por complejidad
- ✅ Secciones de `comportamiento`, `restricciones` y `actualizacion_estado`
- ✅ Sección `escalamiento` (opcional) para delegación a otros roles
- ✅ Guía de uso y tabla de secciones obligatorias/opcionales

---

## 🔧 Plantilla: Herramienta (`.tool.md`)

> **Ubicación destino:** `herramientas/[nombre].tool.md`  
> **Audiencia:** IA  
> **📄 Plantilla completa:** `plantillas/herramienta_plantilla.tool.md`

La plantilla de herramientas incluye:

- ✅ Sección `condiciones_entrada` con validaciones requeridas
- ✅ Estructura completa de `identificacion`, `parametros`
- ✅ Proceso con pasos definidos
- ✅ Secciones de `salida`, `errores` y `siguiente`
- ✅ Guía de uso detallada

⚠️ **Importante:** Las instrucciones base ahora están centralizadas en `_base.agent.md`.

---

## 📋 Guía Rápida de Creación

### Crear un Nuevo Rol

1. **Copiar plantilla** desde `plantillas/agente_plantilla.agent.md`
2. **Guardar** en `agentes/[nombre].agent.md`
3. **Rellenar** todas las secciones marcadas con `[placeholder]`
4. **Agregar** instrucciones MANDATORY específicas del rol
5. **Definir** herramientas disponibles (verificar que existan)
6. **Registrar** en `ROLES.md`

### Crear una Nueva Herramienta

1. **Copiar plantilla** desde `plantillas/herramienta_plantilla.tool.md`
2. **Guardar** en `herramientas/[nombre].tool.md`
3. **Rellenar** todas las secciones marcadas con `[placeholder]`
4. **Definir** proceso paso a paso con `obligatorio: true|false`
5. **⚠️ MANTENER** el `paso_final` de actualización de sesión
6. **Especificar** roles autorizados
7. **Registrar** en `HERRAMIENTAS.md`

---

## ✅ Checklist de Validación

### Para Roles (.agent.md)

| Sección | Obligatoria | Notas |
|---------|-------------|-------|
| `mandatory` | ✅ | Incluir las 5 instrucciones base + específicas |
| `identidad` | ✅ | Nombre, comando, estilo, descripción |
| `especializacion` | ✅ | Tecnologías, principios, metodologías |
| `inicializacion` | ✅ | Pasos de arranque del rol |
| `herramientas` | ✅ | Lista de herramientas disponibles |
| `comandos` | ✅ | Comandos universales del sistema |
| `niveles` | ⚠️ Opcional | Para roles con tareas de diferente escala |
| `comportamiento` | ✅ | Acciones ante eventos principales |
| `restricciones` | ✅ | Anti-patrones y buenas prácticas |
| `escalamiento` | ⚠️ Opcional | Delegación a otros roles |
| `actualizacion_estado` | ✅ | Registro de eventos en sesión |

### Para Herramientas (.tool.md)

| Sección | Obligatoria | Notas |
|---------|-------------|-------|
| `identificacion` | ✅ | Nombre, comando, alias |
| `roles_autorizados` | ✅ | Al menos un rol |
| `condiciones_entrada` | ✅ | Validaciones requeridas (puede estar vacío) |
| `parametros` | ⚠️ Opcional | Si la herramienta los requiere |
| `proceso` | ✅ | Mínimo paso_1 |
| `salida` | ✅ | Archivos generados/actualizados |
| `errores` | ✅ | Al menos un error común |
| `siguiente` | ⚠️ Recomendado | Guía el flujo de trabajo |

---

## 📚 Referencias

| Recurso | Ubicación |
|---------|-----------|
| **Plantilla de agente** | `plantillas/agente_plantilla.agent.md` |
| **Plantilla de herramienta** | `plantillas/herramienta_plantilla.tool.md` |
| Roles existentes | `agentes/*.agent.md` |
| Herramientas existentes | `herramientas/*.tool.md` |
| Índice de roles | `ROLES.md` |
| Índice de herramientas | `HERRAMIENTAS.md` |
| Guía de creación de roles | `guias/guia_creacion_roles.md` |
| Estructura del directorio | `estructura_directorio.md` |

---

## 🔄 Historial

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 4.3 | 6 ene 2026 | Esqueleto de agente movido a `plantillas/agente_plantilla.agent.md`, README convertido en índice |
| 4.2 | 6 ene 2026 | Añadida sección `niveles` (opcional), documentado `escalamiento` como opcional |
| 4.1 | 6 ene 2026 | Esqueleto de herramienta movido a `plantillas/herramienta_plantilla.tool.md` |
| 4.0 | 6 ene 2026 | Rediseño completo para formato YAML v4.0 |
| 2.0 | 13 oct 2025 | Versión anterior con plantillas MD |
