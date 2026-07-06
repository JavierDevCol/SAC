---
name: registrar-hallazgo
description: Registra hallazgos encontrados durante el desarrollo. Analiza el hallazgo con sub-agentes, clasifica como BUG o PENDIENTE, y crea el artifact correspondiente. Ejecuta esta skill cuando se encuentre un error, mejora, deuda técnica o cualquier incidencia que deba registrarse.
---

## Parámetros

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `descripcion` | string | — | Descripción libre del hallazgo |
| `--proyecto` | string | null | Proyecto afectado |
| `--logs` | string | null | Logs, stack traces o evidencia |

## Flujo General

```
1. Preguntar al usuario (contexto inicial)
2. Sub-agentes analizan (código + HUs)
3. Comparar respuestas del usuario vs análisis
4. Clasificar: BUG o PENDIENTE
5. Presentar sugerencia al usuario
6. Crear artifact si acepta
```

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `artifacts.hu_folder`, `artifacts.contextos_folder`

### 2. Recepción del Hallazgo

- Recopilar descripción del hallazgo tal como el usuario la proporciona
- Detectar proyecto del contexto activo
- Preguntar por evidencia:
  > 🤷 ¿Tienes logs, mensajes de error o evidencia para adjuntar?
  > - 📎 [S] Sí, los pego a continuación
  > - ➡️ [N] No, continuar con lo que tengo

### 3. Preguntas al Usuario (Contexto Inicial)

**Hacer UNA pregunta a la vez, esperar respuesta antes de continuar:**

> **Pregunta 1:** ¿Este hallazgo afecta funcionalidad ACTUAL del sistema?
> - [S] Sí, algo no funciona / está roto
> - [N] No, funciona pero podría mejorar
> - [?] No estoy seguro

> **Pregunta 2:** ¿Qué error o comportamiento observas exactamente?
> - [texto libre del usuario]

> **Pregunta 3:** ¿Cuándo ocurre este hallazgo?
> - [A] Siempre
> - [B] Solo a veces
> - [C] Después de un cambio específico
> - [D] No estoy seguro

> **Pregunta 4:** ¿El hallazgo ocurrió luego de probar alguna funcionalidad (HU)?
> - [C] Sí, puedo indicar el ID (ej: HU-003)
> - [X] No, no estoy seguro / fue en otro contexto

**Almacenar respuestas del usuario para pasar a sub-agentes.**

### 4. Análisis con Sub-Agentes (Paralelo)

**Ejecutar 2 sub-agentes en paralelo, pasando respuestas del usuario como contexto:**

**Sub-agente 1 — Análisis de Código:**
- Cargar prompt desde `assets/prompt-analisis-codigo.md`
- Pasar: hallazgo + respuestas del usuario
- Sub-agente retorna: JSON con evidencias (lista), causa raíz, severidad

**Sub-agente 2 — Análisis de HUs:**
- Cargar prompt desde `assets/prompt-analisis-hus.md`
- Pasar: hallazgo + respuestas del usuario
- Sub-agente retorna: JSON con HUs relacionadas, CA afectado, gap

### 5. Comparar y Clasificar

**Cargar tabla de clasificación desde `assets/tabla-clasificacion.md`**

**Comparar respuestas del usuario vs análisis de sub-agentes:**

| Usuario dice | Sub-agente encuentra | Clasificación |
|--------------|----------------------|---------------|
| "No funciona" | Código roto confirmado | 🐛 BUG (alta confianza) |
| "No funciona" | Código OK, mejora necesaria | 📋 PENDIENTE (usuario confundido) |
| "Podría mejorar" | Código roto | 🐛 BUG (sub-agente corrige) |
| "Podría mejorar" | Mejora confirmada | 📋 PENDIENTE (alta confianza) |
| No está seguro | Código roto | 🐛 BUG (sub-agente determina) |
| No está seguro | Mejora | 📋 PENDIENTE (sub-agente determina) |

**Clasificación final:**
- Si hay conflicto → Priorizar evidencia del código sobre opinión del usuario
- Si coinciden → Alta confianza
- Si sub-agente no encuentra evidencia → Preguntar más detalles

### 6. Presentar Sugerencia al Usuario

```
🔍 **Análisis del hallazgo:**

**Evidencia encontrada:**
- Archivo: src/auth/AuthService.java:45
- Causa: validateEmail() retorna true siempre
- HU relacionada: HU-003 (CA-02: validar formato email)

**Clasificación sugerida:** 🐛 **BUG**
**Confianza:** Alta (usuario + código coinciden)
**Severidad:** Alta (funcionalidad core bloqueada)
**Motivo:** Error que impide validación de email en login

❓ **¿Aceptas la sugerencia?**
- [B] Sí, registrar como BUG
- [P] No, es un PENDIENTE
- [E] Editar antes de registrar (severidad, descripción, etc.)
- [N] Cancelar
```

### 7. Crear Artifact

**Si BUG aceptado:**
- Crear `{hu_folder}/BUG-NNN/` (autoincremental)
- Copiar plantillas: HU.md, RefinamientoBug.md
- Rellenar HU.md: ID=BUG-NNN, Tipo=Bug, Prioridad=según severidad
- Rellenar RefinamientoBug.md: Síntoma, Causa Raíz, Archivos Afectados, Corrección Sugerida
- Agregar fila en backlog con estado [P] Planificable

**Si PENDIENTE aceptado:**
- Crear entrada en `{artifacts.pendientes}`
- Categorizar: deuda_tecnica, mejora_ux, optimizacion, verificacion, investigacion
- Asignar prioridad: Baja o Media (si es Alta → reclasificar como BUG)

## Restricciones

- **SIEMPRE** preguntar al usuario antes de analizar con sub-agentes
- Pasar respuestas del usuario como contexto a los sub-agentes
- Comparar respuestas del usuario vs análisis de sub-agentes
- Priorizar evidencia del código sobre opinión del usuario
- **NUNCA** crear artifact sin confirmación del usuario
- Si el usuario dice que ya está corregido → registrar como post-mortem

## Formato de salida

**BUG registrado:**
```
🐛 BUG REGISTRADO: BUG-NNN
📁 Carpeta: {hu_folder}/BUG-NNN/
📄 Archivos: HU.md, RefinamientoBug.md
🔴 Severidad: [severidad]
📌 Estado: [P] Planificable
```

**PENDIENTE registrado:**
```
📋 PENDIENTE REGISTRADO: PND-NNN
📁 Archivo: {artifacts.pendientes}
📂 Categoría: [categoría]
🟡 Prioridad: [prioridad]
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| No se encontró código relacionado | Hallazgo muy vago | Pedir más detalles al usuario |
| Clasificación incierta | Evidencia conflictiva | Preguntar al usuario para clarificar |
| Usuario cancela | No quiere registrar | Aceptar y terminar |

## Después de ejecutar

- `>planificar_hu BUG-NNN` — Planificar resolución del bug
- `>sincronizar_backlog` — Verificar estado del backlog
