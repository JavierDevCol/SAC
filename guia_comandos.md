# 📋 Guía Completa de Comandos del Sistema

> **Sistema:** Cochas - Orquestación de Agentes IA  
> **Versión:** 2.0  
> **Última Actualización:** 16 de octubre de 2025

---

## 📖 Índice

- [Comandos del Orquestador](#comandos-del-orquestador)
- [Comandos de Herramientas](#comandos-de-herramientas)
- [Casos de Uso Comunes](#casos-de-uso-comunes)
- [Gestión de Errores](#gestión-de-errores)

---

## Comandos del Orquestador

Todos los comandos del orquestador comienzan con `/cochas`.

---

### `/cochas list`

**Descripción:** Lista todos los roles disponibles en el sistema.

**Formato:**
```
/cochas list
```

**Salida Esperada:**
```markdown
📋 **Roles Disponibles en el Sistema**

| Comando | Nombre del Rol | Área de Expertise |
|---------|----------------|-------------------|
| ONAD | Arquitecto Onad | Arquitectura estratégica y decisiones de alto nivel |
| ARCHDEV | ArchDev Pro | Implementación de código y refactoring |
| DEVOPS | Arquitecto DevOps | Infraestructura, pipelines y deployment |
| REFINADOR | Refinador HU | Refinamiento de historias de usuario |
| ARTESANO | Artesano de Commits | Creación de mensajes de commit profesionales |

💡 **Uso:** `/cochas +<COMANDO>` o `/cochas switch <COMANDO>`

**Ejemplo:** `/cochas +ONAD`
```

**Cuándo Usarlo:**
- Al iniciar una nueva sesión
- Cuando no recuerdas qué roles están disponibles
- Para verificar el comando exacto de activación de un rol

---

### `/cochas +<ROL>` o `/cochas switch <ROL>`

**Descripción:** Activa un rol específico en la sesión.

**Formato:**
```
/cochas +ONAD
/cochas switch ARCHDEV
```

**Ambos formatos son equivalentes:**
- `/cochas +ONAD` = `/cochas switch ONAD`
- `/cochas +ARCHDEV` = `/cochas switch ARCHDEV`

**Proceso Interno:**
1. Lee `personas/roles-activos.md`
2. Busca el comando en la columna **COMANDO**
3. Obtiene la ruta del archivo del rol
4. Carga el rol desde esa ruta
5. Actualiza `artefactos/session_state.json`
6. Presenta el saludo del rol activado

**Salida Esperada:**
```markdown
🔄 **Cambio de Rol Exitoso**

Rol anterior: Ninguno
Rol nuevo: Arquitecto Onad (ONAD)

---

👋 ¡Hola! Soy el **Arquitecto Onad**, especialista en arquitectura de software...

🛠️ **Herramientas Disponibles:**
- tomar_contexto
- define_arquitectura
- generar_adr

💡 **Tip:** Usa `> tomar_contexto` para analizar el proyecto.

---
**[ESTADO_SESION]**
🎯 **Rol Activo:** `Arquitecto Onad` (ONAD)
📊 **Contexto Proyecto:** `NO_INICIALIZADO`
🕒 **Timestamp:** `2025-10-16T10:30:00`
```

**Cuándo Usarlo:**
- Al comenzar una tarea que requiere expertise específica
- Para cambiar de contexto de trabajo
- Cuando el orquestador te recomienda un rol

**Errores Comunes:**

❌ **Comando no encontrado:**
```
Usuario: /cochas +DEVELOPER
Sistema: ❌ El rol 'DEVELOPER' no existe en el sistema.
         💡 Usa `/cochas list` para ver roles disponibles.
```

---

### `/cochas status`

**Descripción:** Muestra el estado completo de la sesión actual.

**Formato:**
```
/cochas status
```

**Salida Esperada:**
```markdown
📊 **Estado de la Sesión**

🎯 **Rol Activo:**
- Nombre: Arquitecto Onad
- Comando: ONAD
- Ruta: personas/arquitecto_onad.md

📁 **Contexto del Proyecto:**
- Estado: INICIALIZADO
- Archivo: artefactos/contexto_proyecto.md
- Última actualización: 2025-10-16T09:15:00

📚 **Herramientas Usadas en esta Sesión:**
1. tomar_contexto (usado 1 vez)
2. define_arquitectura (usado 1 vez)

🔄 **Historial de Roles:**
1. Arquitecto Onad (ONAD) - Activo desde 2025-10-16T10:30:00
   - Tareas completadas: 2
   - Herramientas usadas: tomar_contexto, define_arquitectura

📈 **Estadísticas:**
- Total cambios de rol: 1
- Total tareas completadas: 2
- Sesión iniciada: 2025-10-16T10:00:00
- Última actividad: 2025-10-16T10:45:00

📋 **Tablero de Tareas:**
- Pendientes: 2
- Refinadas: 0
- Aprobadas: 0
- Completadas: 0
```

**Cuándo Usarlo:**
- Para verificar qué rol está activo
- Para revisar el progreso de la sesión
- Para diagnosticar problemas
- Al retomar una sesión anterior

---

### `/cochas assign <tarea>`

**Descripción:** Sugiere el rol más adecuado para una tarea específica.

**Formato:**
```
/cochas assign "descripción de la tarea"
```

**Ejemplos:**

**Ejemplo 1: Optimización de base de datos**
```
Usuario: /cochas assign "Necesito optimizar las consultas de la base de datos"

Sistema:
🎯 **Análisis de Tarea**

**Tarea:** Optimizar consultas de base de datos

**Rol Recomendado:** 🥇 Arquitecto Onad (ONAD)

**Justificación:**
- Requiere decisiones arquitectónicas sobre índices y queries
- Puede impactar el diseño general del sistema
- Necesita evaluar trade-offs de performance vs complejidad

**Herramienta Sugerida:** `define_arquitectura`
- Para documentar decisiones de optimización
- Generar ADR si se cambia estrategia de persistencia

**Roles Alternativos:**
- 🥈 ArchDev Pro (ARCHDEV) - Si solo se necesita refactorizar queries existentes
- 🥉 Arquitecto DevOps (DEVOPS) - Si el problema es de infraestructura (cache, réplicas)

💡 **¿Deseas activar ONAD ahora?** Usa: `/cochas +ONAD`
```

**Ejemplo 2: Crear tests unitarios**
```
Usuario: /cochas assign "Crear tests unitarios para el módulo de autenticación"

Sistema:
🎯 **Análisis de Tarea**

**Tarea:** Crear tests unitarios para módulo de autenticación

**Rol Recomendado:** 🥇 ArchDev Pro (ARCHDEV)

**Justificación:**
- Es una tarea de implementación de código
- Requiere conocimiento de testing frameworks
- ARCHDEV tiene herramienta especializada para esto

**Herramienta Sugerida:** `crear_pruebas`
- Genera tests con cobertura completa
- Aplica mejores prácticas de testing

**Roles Alternativos:**
- No hay alternativas viables para esta tarea

💡 **¿Deseas activar ARCHDEV ahora?** Usa: `/cochas +ARCHDEV`
```

**Cuándo Usarlo:**
- Cuando no sabes qué rol activar
- Para validar si elegiste el rol correcto
- Al enfrentar una tarea compleja que podría involucrar múltiples roles

**Proceso Interno:**
1. Ejecuta la herramienta `asignar_responsable`
2. Analiza las capacidades de cada rol
3. Evalúa la compatibilidad con la tarea
4. Sugiere el más adecuado con justificación

---

### `/cochas history`

**Descripción:** Muestra el historial completo de la sesión.

**Formato:**
```
/cochas history
```

**Salida Esperada:**
```markdown
📜 **Historial de la Sesión**

---

## 🔄 Cambios de Rol

### 1. Arquitecto Onad (ONAD)
- **Activado:** 2025-10-16T10:00:00
- **Duración:** 45 minutos
- **Tareas Completadas:**
  - ✅ ONAD-001: Análisis de contexto del proyecto
  - ✅ ONAD-002: Diseño de arquitectura microservicios

### 2. ArchDev Pro (ARCHDEV)
- **Activado:** 2025-10-16T10:45:00
- **Duración:** 30 minutos (activo)
- **Tareas Completadas:**
  - ✅ ARCHDEV-001: Refactorización del módulo de autenticación

---

## 📝 Log de Eventos Clave

| Timestamp | Evento | Descripción |
|-----------|--------|-------------|
| 2025-10-16T10:00:00 | Sesión iniciada | Nueva sesión creada |
| 2025-10-16T10:05:00 | Rol activado | Arquitecto Onad (ONAD) |
| 2025-10-16T10:10:00 | Herramienta ejecutada | tomar_contexto |
| 2025-10-16T10:15:00 | Contexto inicializado | contexto_proyecto.md creado |
| 2025-10-16T10:20:00 | Herramienta ejecutada | define_arquitectura |
| 2025-10-16T10:25:00 | Tarea completada | ONAD-001 |
| 2025-10-16T10:30:00 | ADR generado | adr_001_microservicios.md |
| 2025-10-16T10:35:00 | Tarea completada | ONAD-002 |
| 2025-10-16T10:40:00 | Backlog actualizado | 3 nuevas tareas agregadas |
| 2025-10-16T10:45:00 | Rol cambiado | ONAD → ARCHDEV |
| 2025-10-16T10:50:00 | Herramienta ejecutada | refactorizar |
| 2025-10-16T11:00:00 | Tarea completada | ARCHDEV-001 |

---

## 📈 Estadísticas

- **Total tareas completadas:** 3
- **Total cambios de rol:** 2
- **Herramientas más usadas:**
  1. tomar_contexto (1 vez)
  2. define_arquitectura (1 vez)
  3. refactorizar (1 vez)
- **Rol más usado:** Arquitecto Onad (45 min)
- **Duración de sesión:** 1 hora 15 minutos
```

**Cuándo Usarlo:**
- Para revisar todo lo que has hecho en la sesión
- Para generar reportes de trabajo
- Para auditar decisiones tomadas
- Para recordar el flujo de trabajo seguido

---

### `/cochas reload`

**Descripción:** Recarga el rol activo actual desde su archivo fuente.

**Formato:**
```
/cochas reload
```

**Proceso Interno:**
1. Lee `session_state.json` para obtener el comando del rol activo
2. Lee `personas/roles-activos.md` para obtener la ruta del archivo
3. Recarga el archivo del rol desde disco
4. Limpia la caché de herramientas

**Salida Esperada:**
```markdown
🔄 **Recarga de Rol**

Rol recargado: Arquitecto Onad (ONAD)
Ruta: personas/arquitecto_onad.md

✅ Archivo recargado exitosamente
🧹 Caché de herramientas limpiada

💡 Las herramientas se recargarán al usarlas nuevamente.

---
**[ESTADO_SESION]**
🎯 **Rol Activo:** `Arquitecto Onad` (ONAD)
📊 **Contexto Proyecto:** `INICIALIZADO`
🕒 **Timestamp:** `2025-10-16T11:00:00`
```

**Cuándo Usarlo:**
- Después de modificar el archivo de un rol
- Si actualizaste herramientas del rol
- Para forzar recarga de definiciones
- Si el rol se comporta de forma inconsistente

**Casos de Uso:**
```
# Ejemplo: Actualizaste el archivo arquitecto_onad.md
# agregando una nueva herramienta

1. Editas: personas/arquitecto_onad.md
2. Ejecutas: /cochas reload
3. El rol se recarga con los cambios
```

---

### `/cochas reset`

**Descripción:** Reinicia completamente la sesión (requiere confirmación).

**Formato:**
```
/cochas reset
```

**Proceso Interno:**
1. Solicita confirmación al usuario
2. Si confirma, elimina `artefactos/session_state.json`
3. Crea nuevo estado inicial vacío

**Salida Esperada:**
```markdown
⚠️ **Confirmación Requerida**

Estás a punto de reiniciar la sesión completamente.

**Esto eliminará:**
- ❌ El rol activo actual
- ❌ Todo el historial de roles
- ❌ El log de eventos
- ❌ El registro de herramientas usadas

**Esto NO eliminará:**
- ✅ artefactos/contexto_proyecto.md
- ✅ artefactos/backlog_desarrollo.md
- ✅ Archivos de roles y herramientas

¿Estás seguro? (S/N)
```

**Si el usuario confirma:**
```markdown
✅ **Sesión Reiniciada**

- Estado anterior eliminado
- Nuevo estado creado
- Sistema listo para usar

💡 Usa `/cochas list` para ver roles disponibles.
```

**Cuándo Usarlo:**
- Al comenzar un proyecto completamente nuevo
- Si el estado está corrupto
- Para limpiar sesiones de prueba
- Cuando necesitas empezar de cero

**⚠️ Advertencia:**
- Esta acción no se puede deshacer
- Asegúrate de exportar el estado antes si lo necesitas

---

### `/cochas export`

**Descripción:** Exporta el estado de la sesión a un archivo con timestamp.

**Formato:**
```
/cochas export
```

**Proceso Interno:**
1. Lee `session_state.json`
2. Agrega metadata de exportación
3. Formatea con indentación legible
4. Guarda copia con timestamp

**Salida Esperada:**
```markdown
📦 **Exportación de Sesión**

✅ Estado exportado exitosamente

**Archivo creado:**
`artefactos/session_state_export_2025-10-16_11-30-00.json`

**Contenido incluido:**
- Rol activo
- Historial de roles
- Log de eventos
- Herramientas usadas
- Metadata de la sesión
- Tablero de tareas

**Tamaño:** 3.2 KB

💡 **Uso:**
- Respaldo antes de `/cochas reset`
- Compartir estado con el equipo
- Auditoría de trabajo realizado
```

**Cuándo Usarlo:**
- Antes de ejecutar `/cochas reset`
- Para crear respaldos periódicos
- Para compartir el progreso con otros
- Para auditoría o documentación

**Ejemplo de Archivo Exportado:**
```json
{
  "version": "1.0",
  "export_metadata": {
    "timestamp": "2025-10-16T11:30:00",
    "exported_by": "Orquestador Cochas v2.0"
  },
  "rol_activo": {
    "nombre": "Arquitecto Onad",
    "comando": "ONAD",
    "ruta": "personas/arquitecto_onad.md"
  },
  "historial_roles": [...],
  "log_eventos_clave": [...],
  "metadata": {...}
}
```

---

### `/cochas help`

**Descripción:** Muestra ayuda rápida con todos los comandos disponibles.

**Formato:**
```
/cochas help
```

**Salida Esperada:**
```markdown
🤖 **Comandos del Orquestador Cochas**

---

## 📋 Gestión de Roles

| Comando | Descripción |
|---------|-------------|
| `/cochas list` | Lista todos los roles disponibles |
| `/cochas +<ROL>` | Activa un rol |
| `/cochas switch <ROL>` | Activa un rol (alternativa) |

---

## 📊 Estado y Diagnóstico

| Comando | Descripción |
|---------|-------------|
| `/cochas status` | Muestra estado de la sesión |
| `/cochas history` | Muestra historial completo |

---

## 🎯 Asignación Inteligente

| Comando | Descripción |
|---------|-------------|
| `/cochas assign <tarea>` | Sugiere el mejor rol para una tarea |

---

## 🔧 Mantenimiento

| Comando | Descripción |
|---------|-------------|
| `/cochas reload` | Recarga el rol activo |
| `/cochas reset` | Reinicia la sesión |
| `/cochas export` | Exporta el estado |

---

## 🚀 Inicio Rápido

1. Ver roles: `/cochas list`
2. Activar rol: `/cochas +ONAD`
3. Ver estado: `/cochas status`
4. Pedir ayuda: `/cochas assign "tu tarea"`

---

📚 **Documentación Completa:** `guia_comandos.md`
```

**Cuándo Usarlo:**
- Primera vez usando el sistema
- Para recordar la sintaxis de comandos
- Como referencia rápida

---

## Comandos de Herramientas

Los comandos de herramientas permiten ejecutar funcionalidades específicas del rol activo.

### `> <herramienta>` o `-> <herramienta>`

**Descripción:** Ejecuta una herramienta del rol activo.

**Formato:**
```
> tomar_contexto
-> refactorizar
> crear_pruebas
```

**Ambos formatos son equivalentes:**
- `> tomar_contexto` = `-> tomar_contexto`

**Requisitos:**
- ✅ Debe haber un rol activo
- ✅ El rol debe tener acceso a la herramienta
- ✅ La herramienta debe existir en el sistema

**Ejemplos por Rol:**

**Arquitecto Onad (ONAD):**
```
> tomar_contexto
> define_arquitectura
> generar_adr
```

**ArchDev Pro (ARCHDEV):**
```
> refactorizar
> analizar_code_smells
> solucionar_smells
> crear_pruebas
> verifica_pruebas
```

**Arquitecto DevOps (DEVOPS):**
```
> diagnosticar_devops
> tomar_contexto
```

**Refinador HU (REFINADOR):**
```
> refinar_hu
> tomar_contexto
```

**Artesano de Commits (ARTESANO):**
```
> generar_commit
```

---

## Casos de Uso Comunes

### Caso 1: Primera Vez en el Sistema

```bash
# Paso 1: Ver ayuda
/cochas help

# Paso 2: Ver roles disponibles
/cochas list

# Paso 3: Activar primer rol
/cochas +ONAD

# Paso 4: Analizar proyecto
> tomar_contexto

# Paso 5: Ver estado
/cochas status
```

---

### Caso 2: No Sé Qué Rol Usar

```bash
# Describir la tarea
/cochas assign "Necesito crear un pipeline de CI/CD con GitHub Actions"

# El sistema te recomendará:
# 🥇 Arquitecto DevOps (DEVOPS)
# Herramienta: diagnosticar_devops

# Activar el rol recomendado
/cochas +DEVOPS
```

---

### Caso 3: Cambiar Entre Roles

```bash
# Verificar rol actual
/cochas status

# Cambiar a otro rol
/cochas +ARCHDEV

# Ver historial de cambios
/cochas history
```

---

### Caso 4: Retomar Sesión Anterior

```bash
# Ver estado de la sesión guardada
/cochas status

# El último rol se mantiene activo
# Continuar trabajando o cambiar de rol
/cochas +REFINADOR
```

---

### Caso 5: Exportar y Reiniciar

```bash
# Exportar estado antes de limpiar
/cochas export

# Reiniciar sesión
/cochas reset

# Confirmar: S

# Comenzar nueva sesión
/cochas list
```

---

## Gestión de Errores

### Error: Rol No Existe

**Entrada:**
```
/cochas +DEVELOPER
```

**Salida:**
```
❌ El rol 'DEVELOPER' no existe en el sistema.

💡 Usa `/cochas list` para ver la lista completa de roles disponibles.
```

**Solución:** Verifica el nombre correcto con `/cochas list`.

---

### Error: Herramienta Sin Rol Activo

**Entrada:**
```
> refactorizar
```
(Sin tener un rol activo)

**Salida:**
```
❌ No hay ningún rol activo. Las herramientas solo pueden ejecutarse cuando un rol está cargado.

💡 La herramienta 'refactorizar' puede ser activada por los siguientes roles:

• ArchDev Pro - Usar: /cochas +ARCHDEV

¿Deseas activar un rol ahora?
```

**Solución:** Activa un rol compatible antes de usar herramientas.

---

### Error: Herramienta No Compatible

**Entrada:**
```
/cochas +ONAD
> diagnosticar_devops
```

**Salida:**
```
❌ El rol activo 'Arquitecto Onad' no puede ejecutar la herramienta 'diagnosticar_devops'.

💡 La herramienta 'diagnosticar_devops' puede ser activada por:

• Arquitecto DevOps - Usar: /cochas +DEVOPS

¿Deseas cambiar de rol?
```

**Solución:** Cambia al rol apropiado con `/cochas +DEVOPS`.

---

### Error: Herramienta No Existe

**Entrada:**
```
/cochas +ARCHDEV
> compilar_proyecto
```

**Salida:**
```
❌ La herramienta 'compilar_proyecto' no existe en el sistema.

💡 Herramientas disponibles para 'ArchDev Pro':

• refactorizar
• analizar_code_smells
• solucionar_smells
• crear_pruebas
• verifica_pruebas
• generar_adr
• tomar_contexto
```

**Solución:** Usa una herramienta disponible para tu rol activo.

---

## 💡 Tips y Mejores Prácticas

### Tip 1: Usa `assign` Cuando Tengas Dudas
```bash
/cochas assign "descripción de lo que necesitas hacer"
```
El sistema te guiará al rol correcto.

### Tip 2: Exporta Antes de Reset
```bash
/cochas export  # Guarda respaldo
/cochas reset   # Limpia sesión
```

### Tip 3: Revisa el Status Regularmente
```bash
/cochas status  # Ver progreso y estado
```

### Tip 4: Analiza el Proyecto Una Vez
```bash
/cochas +ONAD
> tomar_contexto  # Se guarda y reutiliza
```

### Tip 5: Usa History para Reportes
```bash
/cochas history  # Genera log completo de trabajo
```

---

## 📚 Documentación Relacionada

- **[README Principal](README.md)** - Visión general del sistema
- **[Guía de Roles](guia_roles_activos.md)** - Roles disponibles y sus capacidades
- **[Guía de Ciclo de Vida](guia_ciclo_vida_tareas.md)** - Flujo de tareas
- **[Arquitectura del Sistema](core-cochas.md)** - Documentación técnica completa

---

**¿Necesitas más ayuda?** Usa `/cochas help` en cualquier momento.
