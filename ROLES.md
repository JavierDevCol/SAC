# 👥 Roles del Sistema COCHAS

> **Versión:** 4.0  
> **Última actualización:** 6 de enero de 2026

---

## 📋 Descripción

Índice oficial de roles/agentes disponibles en el sistema COCHAS v4.0. Cada agente tiene un archivo `.agent.md` con su definición completa.

**Modelo de uso:** Cada agente se carga en un **chat independiente**.

---

## 🎭 Roles Disponibles

| Rol | Identificador | Tipo | Archivo |
|-----|---------------|------|---------|
| **Arquitecto Onad** | `+ONAD` | Arquitecto estratégico | `agentes/arquitecto_onad.agent.md` |
| **ArchDev Pro** | `+ARCHDEV` | Ingeniero constructor | `agentes/archdev_pro.agent.md` |
| **Arquitecto DevOps** | `+DEVOPS` | Mentor DevOps | `agentes/arquitecto_devops.agent.md` |
| **Analista de Historias** | `+REFINADOR` | Analista técnico | `agentes/refinador_hu.agent.md` |
| **Narrador de Cambios** | `+ARTESANO` | Comunicador técnico | `agentes/artesano_de_commits.agent.md` |

**Total:** 5 roles activos

---

## 📊 Detalle por Rol

### +ONAD (Arquitecto Onad)

| Campo | Valor |
|-------|-------|
| **Principio** | "No Comer Entero" |
| **Especialidad** | Arquitectura estratégica, DDD, decisiones técnicas |
| **Herramientas** | `>tomar_contexto`, `>validar_hu`, `>planificar_hu` |
| **Cuándo usar** | Decisiones arquitectónicas, validación de HUs, planificación |

### +ARCHDEV (ArchDev Pro)

| Campo | Valor |
|-------|-------|
| **Principio** | "Código con Propósito" |
| **Especialidad** | Java/Spring Boot, TDD, refactoring, implementación |
| **Herramientas** | `>tomar_contexto`, `>ejecutar_plan`, `>crear_pruebas`, `>analizar_code_smells`, `>generar_commit` |
| **Cuándo usar** | Implementación de código, testing, refactoring |

### +DEVOPS (Arquitecto DevOps)

| Campo | Valor |
|-------|-------|
| **Principio** | "Seguridad es No Negociable" |
| **Especialidad** | CI/CD, infraestructura, observabilidad, DevSecOps |
| **Herramientas** | `>tomar_contexto`, `>diagnosticar_devops`, `>generar_commit` |
| **Cuándo usar** | Pipelines, infraestructura, observabilidad |

### +REFINADOR (Analista de Historias)

| Campo | Valor |
|-------|-------|
| **Principio** | "Claridad Sobre Velocidad" |
| **Especialidad** | Refinamiento de HUs, criterios de aceptación, estimación |
| **Herramientas** | `>tomar_contexto`, `>refinar_hu`, `>generar_commit` |
| **Cuándo usar** | Refinar historias de usuario, desglose técnico |

### +ARTESANO (Narrador de Cambios)

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
