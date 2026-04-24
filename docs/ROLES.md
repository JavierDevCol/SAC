# 👥 Roles del Sistema SAC

> **Versión:** 7.3.0  
> **Última actualización:** 23 de abril de 2026

---

## 📋 Descripción

Índice oficial de roles/agentes disponibles en el sistema SAC v7.3.0. Cada rol tiene un archivo `.rol.md` con su definición completa.

**Modelo de uso:** Cada agente se invoca con `@nombre` en GitHub Copilot Chat.

---

## 🎭 Roles Disponibles

| Rol | Invocación Copilot | Tipo | Archivo de rol |
|-----|--------------------|------|----------------|
| **Arquitecto** | `@arquitecto` | Arquitecto estratégico | `agentes/arquitecto_onad.rol.md` |
| **Desarrollador** | `@desarrollador` | Ingeniero constructor | `agentes/archdev_pro.rol.md` |
| **DevOps** | `@devops` | Mentor DevOps | `agentes/arquitecto_devops.rol.md` |
| **Analista de Requisitos** | `@analista_historias` | Analista técnico | `agentes/refinador_hu.rol.md` |
| **Cronista de Cambios** | `@cronista_de_cambios` | Comunicador técnico | `agentes/cronista_de_cambios.rol.md` |

**Total:** 5 roles activos

---

## 📊 Detalle por Rol

### @arquitecto (Arquitecto)

| Campo | Valor |
|-------|-------|
| **Principio** | "No Comer Entero" |
| **Especialidad** | Arquitectura estratégica, DDD, decisiones técnicas |
| **Herramientas** | `>tomar_contexto`, `>analizar_stack`, `>validar_hu`, `>planificar_hu`, `>generar_adr`, `>init_reglas_arquitectonicas` |
| **Cuándo usar** | Decisiones arquitectónicas, validación de HUs, planificación, ADRs |

### @desarrollador (Desarrollador)

| Campo | Valor |
|-------|-------|
| **Principio** | "Código con Propósito" |
| **Especialidad** | Java/Spring Boot, TDD, refactoring, implementación |
| **Herramientas** | `>tomar_contexto`, `>analizar_stack`, `>generar_adr`, `>ejecutar_plan`, `>crear_pruebas`, `>analizar_code_smells`, `>generar_commit` |
| **Cuándo usar** | Implementación de código, testing, refactoring |

### @devops (DevOps)

| Campo | Valor |
|-------|-------|
| **Principio** | "Seguridad es No Negociable" |
| **Especialidad** | CI/CD, infraestructura, observabilidad, DevSecOps |
| **Herramientas** | `>tomar_contexto`, `>generar_adr`, `>diagnosticar_devops`, `>generar_commit` |
| **Cuándo usar** | Pipelines, infraestructura, observabilidad |

### @analista_historias (Analista de Requisitos)

| Campo | Valor |
|-------|-------|
| **Principio** | "Claridad Sobre Velocidad" |
| **Especialidad** | Refinamiento de HUs, criterios de aceptación, estimación |
| **Herramientas** | `>tomar_contexto`, `>refinar_hu`, `>generar_commit` |
| **Cuándo usar** | Refinar historias de usuario, desglose técnico |

### @cronista_de_cambios (Cronista de Cambios)

| Campo | Valor |
|-------|-------|
| **Principio** | "La Historia Importa" |
| **Especialidad** | Conventional Commits, documentación de cambios |
| **Herramientas** | `>generar_commit` |
| **Cuándo usar** | Crear mensajes de commit profesionales |

---

## 🚀 Cómo Usar un Rol

1. Abre un **nuevo chat** en tu cliente de IA
2. Carga el archivo `.agent.md` correspondiente como contexto
3. El agente se presentará con su personalidad
4. Usa sus herramientas con el prefijo `>`

```bash
# Ejemplo: usar el Analista de Historias
# 1. Cargar agentes/refinador_hu.agent.md en el chat
# 2. El agente saluda y se presenta
# 3. Ejecutar herramientas:
>tomar_contexto
>refinar_hu
```

---

## 🆕 Agregar Nuevo Rol

1. Copiar `plantillas/agente_plantilla.agent.md`
2. Guardar en `agentes/[nombre].agent.md`
3. Actualizar esta tabla
4. Verificar herramientas disponibles en `HERRAMIENTAS.md`

---

## 📚 Referencias

| Recurso | Ubicación |
|---------|-----------|
| Plantilla de agente | `plantillas/agente_plantilla.agent.md` |
| Herramientas del sistema | `HERRAMIENTAS.md` |
| Guía de creación de roles | `guias/guia_creacion_roles.md` |

---

## 📅 Historial

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 4.0 | 6 ene 2026 | Reescritura completa v4.0, movido a raíz, nombres actualizados |
| 3.0 | 5 ene 2026 | Versión anterior en `agentes/roles-activos.md` |
