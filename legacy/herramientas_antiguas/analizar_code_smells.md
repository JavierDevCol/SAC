# 🛠️ Herramienta: Analizar Code Smells

> **Versión:** 2.1  
> **Fecha de Actualización:** 4 de enero de 2026  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `analizar_code_smells`  
**Comando:** `analizar-smells [archivo.java|paquete]`  
**Rol Propietario:** ArchDev Pro

---

## 🎯 Objetivo

Analizar código Java automáticamente para identificar **code smells**, violaciones de principios **SOLID**, patrones **anti-patrón** y oportunidades de **refactoring**. Genera un reporte priorizado con sugerencias concretas de mejora, acelerando la fase de análisis en el flujo de refactorización de ArchDev Pro.

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 📥 Entradas Requeridas (Contexto)

**Parámetro requerido:**
- `archivo_java`: Código fuente Java a analizar (ruta o contenido)

**Ejemplo de uso:**
```
analizar-smells UserService.java
analizar-smells com.empresa.dominio.servicio
analizar-smells --contenido "public class MiClase { ... }"
```

**Archivos requeridos:**
- `{{session_state_location}}` - Estado de sesión
- `{{contexto_proyecto_location}}` - Contexto del proyecto (opcional, mejora precisión)

**Archivos generados:**
- `{{code_smells_reports_location}}/reporte_[archivo]_[timestamp].json` - Reporte de análisis

**Secundario (Opcional):**
- Umbrales personalizados para detección de code smells
- Configuración de reglas a ignorar

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`tomar_contexto`** | Al inicio si no existe contexto | Obtener información del proyecto (tipo, versión Java, patrones) |

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **`refactorizar`** | En Paso 1 del flujo de refactorización | Análisis inicial antes de planificar cambios |
| **ArchDev Pro** | Directamente por comando del usuario | Análisis de calidad de código |
| **`ejecutar_plan`** | Post-implementación (opcional) | Verificar que no se introdujeron nuevos smells |

### Herramientas que Consume sus Resultados

| Herramienta | Propósito |
|-------------|-----------|
| **`solucionar_smells`** | Ejecuta correcciones basadas en el reporte JSON generado |

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `archivo_java` | string | ruta o contenido | - | Código Java a analizar (requerido) |
| `tipo_proyecto` | string | spring-boot\|maven\|gradle\|standalone | spring-boot | Tipo de proyecto para contexto |
| `version_java` | string | 8\|11\|17\|21 | 17 | Versión de Java del proyecto |
| `patrones_arquitectonicos` | array | clean-architecture\|hexagonal\|mvc\|etc | [] | Patrones arquitectónicos usados |
| `nivel_analisis` | string | basico\|moderado\|exhaustivo | exhaustivo | Profundidad del análisis |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (principal - invoca automáticamente en Flujo 1)
- ✅ **Arquitecto Onad** (consulta para decisiones estratégicas)

---

## 🔄 Proceso Paso a Paso

**Paso 0 [CRÍTICO - OBLIGATORIO]:** 
Cargar y leer `{{session_state_location}}` y `{project-root}/.cochas/CONFIG_INIT.yaml` antes de continuar.

### 1️⃣ Configuración Inicial y Selección de Modo

- **Presentar opciones de ejecución al usuario:**
  - **Modo Automático (Default):** Ejecutar análisis con configuración estándar optimizada
  - **Modo Personalizado:** Configurar parámetros específicos según necesidades del proyecto

- **Si elige Modo Automático, aplicar configuración por defecto:**
  ```
  ⚙️ Configuración Automática del Análisis:
  - tipo_proyecto: spring-boot ✓
  - version_java: 17 ✓
  - nivel_analisis: exhaustivo ✓
  - patrones_arquitectonicos: [] (detectar automáticamente) ✓
  
  ✨ Iniciando análisis de code smells con configuración optimizada...
  ```

- **Si elige Modo Personalizado, mostrar configuración disponible:**
  ```
  🔧 Configuración Personalizada del Análisis:
  
  📦 Tipo de proyecto:
  • spring-boot (análisis optimizado para Spring Boot) ← por defecto
  • maven (proyecto Maven estándar), gradle (proyecto Gradle), standalone (Java puro)
  
  ☕ Versión de Java:
  • 17 (LTS recomendado) ← por defecto
  • 8 (legacy), 11 (LTS), 21 (LTS más reciente)
  
  🔍 Nivel de análisis:
  • exhaustivo (análisis completo - 2-5min) ← por defecto
  • basico (métricas principales - 30s), moderado (análisis estándar - 1min)
  
  🏗️ Patrones arquitectónicos:
  • [] (detectar automáticamente) ← por defecto
  • clean-architecture, hexagonal, mvc, microservicios
  ```

### 2️⃣ Parsing y Análisis Estático (AST)

- **Parsear código Java a Abstract Syntax Tree (AST):**
  - Utilizar librerías como JavaParser o Eclipse JDT para generar representación estructurada del código.
  - Extraer información de clases, métodos, campos, imports y anotaciones.

- **Calcular métricas base:**
  - Líneas de código por clase/método (LOC)
  - Complejidad ciclomática (McCabe Complexity)
  - Profundidad de anidación máxima
  - Número de dependencias (imports)
  - Número de métodos y campos por clase

### 3️⃣ Detección de Code Smells

Aplicar reglas de detección basadas en umbrales configurables:

| Code Smell | Criterio de Detección |
|------------|----------------------|
| **God Object** | Clase > 300 líneas O > 15 métodos O complejidad > 25 |
| **Long Method** | Método > 50 líneas O complejidad > 10 |
| **Long Parameter List** | Método con > 4 parámetros |
| **Feature Envy** | Clase usa > 50% métodos de otra clase |
| **Data Clumps** | Mismo grupo de 3+ parámetros en múltiples métodos |
| **Magic Numbers** | Literales numéricos sin constante declarada |
| **Duplicated Code** | Bloques de código idénticos o muy similares |
| **Coupling Infraestructura** | Imports de `javax.persistence`, `jdbc`, `aws`, etc. en capa de dominio |

- Para cada code smell detectado, registrar:
  - Ubicación exacta (línea inicio/fin)
  - Severidad (CRÍTICA, ALTA, MEDIA, BAJA)
  - Métrica que lo respalda
  - Principios SOLID violados

### 4️⃣ Análisis de Principios SOLID

- **SRP (Single Responsibility):** Detectar múltiples razones de cambio (ej. validación + persistencia + notificación en misma clase).
- **OCP (Open/Closed):** Detectar if/else o switch extensos que deberían ser Strategy Pattern.
- **LSP (Liskov Substitution):** Detectar violaciones en herencia (métodos sobrescritos que lanzan excepciones no esperadas).
- **ISP (Interface Segregation):** Detectar interfaces con > 7 métodos (God Interface).
- **DIP (Dependency Inversion):** Detectar dependencias concretas en lugar de abstracciones.

### 5️⃣ Cálculo de Priorización (ROI Score)

Calcular el ROI Score para cada code smell detectado:

```
ROI Score = (Severidad × Impacto_Mantenibilidad × Impacto_Testabilidad) / Esfuerzo_Estimado

Donde:
- Severidad: CRÍTICA=10, ALTA=7, MEDIA=5, BAJA=2
- Impacto: CRÍTICO=10, ALTO=7, MEDIO=5, BAJO=2
- Esfuerzo: En horas (1-10)
```

- Ordenar todas las recomendaciones por ROI Score descendente.
- Agrupar code smells relacionados que puedan resolverse juntos.

### 6️⃣ Generación del Reporte

- Ensamblar el reporte completo en formato JSON estructurado.
- Incluir métricas generales, lista de code smells priorizados, y recomendaciones concretas.
- Calcular métricas objetivo post-refactoring.
- Generar sugerencias de refactoring con pasos concretos para cada problema.

---

## 🔐 Restricciones

1. **Solo analiza código Java** (no soporta otros lenguajes)
2. **Requiere código sintácticamente correcto** (debe compilar)
3. **No ejecuta código** - solo análisis estático
4. **No modifica archivos** - solo genera reporte
5. **Archivos > 5000 LOC** requieren confirmación del usuario
6. **Respeta configuración de umbrales** del proyecto si existe

---

## 📊 Métricas Sugeridas

Trackear en `{{session_state_location}}`:

| Métrica | Descripción |
|---------|-------------|
| analisis_ejecutados_total | Total de análisis de code smells realizados |
| smells_detectados_total | Acumulado de code smells identificados |
| smells_por_severidad | Distribución por CRÍTICA, ALTA, MEDIA, BAJA |
| tiempo_promedio_analisis | Tiempo promedio por archivo analizado |
| tasa_automatizables | % de smells que pueden corregirse automáticamente |

---

## 🔄 Actualización de Session State

### 7️⃣ Persistencia del Reporte y Registro de Eventos

**Guardar reporte en ubicación estándar:**
```
{{code_smells_reports_location}}/reporte_[NombreArchivo]_[timestamp].json
```

**Actualizar `{{session_state_location}}`:**

```json
{
  "ultimo_analisis_smells": {
    "archivo_analizado": "[NombreArchivo].java",
    "timestamp": "[timestamp]",
    "ruta_reporte": "{{code_smells_reports_location}}/reporte_[NombreArchivo]_[timestamp].json",
    "total_smells": [X],
    "smells_automatizables": [Y],
    "ids_smells": ["CS001", "CS002", "CS003"]
  }
}
```

**Agregar evento a `log_eventos_clave`:**

```json
{
  "timestamp": "[timestamp_actual]",
  "rol": "[rol_actual]",
  "herramienta": "analizar_code_smells",
  "tipo": "analisis_smells_completado",
  "detalle": "Archivo: [NombreArchivo].java - Smells detectados: [X] total, [Y] automatizables"
}
```

**Actualizar metadata:**
- Incrementar `metadata.total_artefactos_generados`
- Actualizar `metadata.ultima_actividad`

### 8️⃣ Ofrecer Integración con `solucionar_smells`

Al finalizar el análisis, presentar opciones:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ANÁLISIS COMPLETADO: [NombreArchivo].java
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Resumen:
- Code smells detectados: [X] total
- Automatizables: [Y] ([Z]%)
- Deuda técnica estimada: [N] horas

📄 Reporte guardado en:
   {{code_smells_reports_location}}/reporte_[NombreArchivo]_[timestamp].json

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿Qué deseas hacer?

A) 🔧 Ejecutar `solucionar-smells CS001` (smell más crítico)
B) 🔧 Ejecutar `solucionar-smells --aplicar-todos` (todos los automatizables)
C) 📋 Ver detalle de un smell específico
D) 📂 Analizar otro archivo
E) ❌ Finalizar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Si el usuario elige A o B:**
- Invocar `solucionar_smells` pasando la referencia al reporte desde `{{session_state_location}}.ultimo_analisis_smells`

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Código con errores de sintaxis | Informar al usuario que el código debe compilar antes de analizar |
| Archivo muy grande (> 5000 LOC) | Advertir que el análisis puede tardar más tiempo o recomendar dividir la clase |
| Sin code smells detectados | Confirmar que el código cumple con los estándares de calidad configurados |
| Contexto de proyecto insuficiente | Usar valores por defecto y advertir al usuario |
| Imports faltantes | Análisis parcial enfocado en estructura interna de la clase |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Un objeto JSON estructurado con el análisis completo.

**Estructura del output:**
```json
{
  "analisis_completado": true,
  "archivo_analizado": "UserService.java",
  "codigo_fuente_original": "/** CÓDIGO COMPLETO AQUÍ PARA REFERENCIA DE SOLUCIONAR_SMELLS */",
  "timestamp": "2025-10-06T14:30:00Z",
  "metricas_generales": {
    "lineas_codigo": 450,
    "complejidad_ciclomatica": 28,
    "nivel_mantenibilidad": "BAJO",
    "deuda_tecnica_estimada_horas": 8,
    "numero_metodos": 28,
    "profundidad_maxima_anidacion": 5
  },
  "code_smells_detectados": [
    {
      "id": "CS001",
      "tipo": "GOD_OBJECT",
      "severidad": "CRITICA",
      "linea_inicio": 1,
      "linea_fin": 450,
      "codigo_afectado": "/** FRAGMENTO ESPECÍFICO DEL CODE SMELL */",
      "descripcion": "La clase UserService tiene múltiples responsabilidades: validación, persistencia, notificación y logging",
      "impacto": {
        "mantenibilidad": "ALTO",
        "testabilidad": "ALTO",
        "escalabilidad": "MEDIO",
        "legibilidad": "ALTO"
      },
      "principios_violados": ["SRP", "OCP"],
      "metrica_soporte": "450 líneas, 28 métodos, complejidad ciclomática = 28",
      "refactoring_sugerido": {
        "patron": "Extract Class + Repository Pattern",
        "esfuerzo_estimado_horas": 5,
        "prioridad": 1,
        "roi_score": 9.5,
        "automatizable": true,
        "nivel_complejidad": "MEDIO",
        "pasos": [
          "Extraer validación a EmailValidator y PasswordValidator",
          "Extraer persistencia a UserRepository (interfaz + implementación)",
          "Extraer notificaciones a UserNotificationService",
          "Aplicar Event-Driven para desacoplar notificaciones"
        ],
        "clases_a_crear": [
          {
            "nombre": "UserValidator",
            "tipo": "@Component",
            "responsabilidad": "Validaciones de usuario"
          },
          {
            "nombre": "UserRepository", 
            "tipo": "@Repository",
            "responsabilidad": "Persistencia de usuarios"
          },
          {
            "nombre": "UserNotificationService",
            "tipo": "@Service", 
            "responsabilidad": "Notificaciones de usuario"
          }
        ],
        "dependencias_requeridas": ["spring-boot-starter-validation", "spring-boot-starter-mail"]
      }
    }
  ],
  "contexto_proyecto": {
    "tipo_proyecto": "spring-boot",
    "version_java": "17",
    "patrones_detectados": ["SERVICE_LAYER", "REPOSITORY"],
    "dependencias_principales": ["spring-boot", "jpa", "lombok"]
  },
  "compatibilidad_solucionar_smells": {
    "version_requerida": "1.0+",
    "smells_automatizables": ["CS001", "CS002", "CS003"],
    "smells_manuales": [],
    "estimacion_total_automatizada": "13 horas"
  }
}
```

**Notificación de confirmación:**
- Resumen de la estimación total y nivel de confianza
- Lista de elementos que requieren validación con Product Owner  
- Próximos pasos sugeridos para la planificación del sprint
- **🆕 Opciones de integración:** "¿Deseas ejecutar `solucionar_smells` automáticamente para aplicar estas correcciones?"

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/analizar_code_smells_ejemplo.md`

---

## 📚 Referencias y Notas

### Tecnologías Sugeridas para Implementación

**Parser AST:**
- JavaParser (https://javaparser.org/) - Recomendado
- Eclipse JDT (Java Development Tools)

**Análisis de Complejidad:**
- Checkstyle (métricas básicas)
- PMD (detección de code smells)
- SonarQube API (análisis avanzado)

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `refactorizar` - Invoca automáticamente esta herramienta en Paso 1 de su flujo
- `define_arquitectura` - Utiliza análisis para evaluación inicial de código legacy
- `tomar_contexto` - Proporciona contexto del proyecto para análisis más preciso

**Flujo de integración:**
```
Usuario solicita refactoring
    ↓
[refactorizar] ejecuta [analizar_code_smells]
    ↓
ArchDev Pro presenta reporte priorizado
    ↓
Usuario aprueba code smell a refactorizar
    ↓
[refactorizar] continúa con Paso 2 (Planificación)
```

### Limitaciones Conocidas

- Solo analiza código Java (no Kotlin, Groovy, etc.)
- Requiere código sintácticamente correcto (no funciona con errores de compilación)
- Análisis de "Feature Envy" puede generar falsos positivos en DTOs
- Análisis estático únicamente (no ejecuta el código)

### Métricas de Evaluación

| Criterio | Objetivo | Medición |
|----------|----------|----------|
| **Precisión** | Detectar 90%+ de code smells comunes | Validación contra benchmark estándar |
| **Velocidad** | < 10 segundos para archivos de 1000 líneas | Medición de tiempo de ejecución |
| **Priorización** | 80%+ de casos ordenados correctamente | Feedback de usuarios expertos |
| **Reducción de tiempo** | De 30 min manual a 2 min automatizado | Comparación antes/después |

### Futuras Mejoras

- **Machine Learning:** Mejorar detección de patrones complejos
- **Multi-lenguaje:** Soporte para Kotlin, TypeScript, C#
- **Análisis histórico:** Integración con Git para evolución de deuda técnica
- **IDE Integration:** Plugin directo para IntelliJ IDEA y VS Code

### Casos de Uso por Contexto

**Proyectos Legacy:**
- Identificación de hot spots para modernización
- Priorización de refactoring por ROI
- Assessment de calidad de código antes de migración

**Proyectos Nuevos:**
- Code review automatizado en CI/CD
- Enforcement de estándares de calidad
- Training y mentoring de desarrolladores junior

**Enterprise/Scale:**
- Análisis masivo de múltiples módulos
- Dashboards de calidad de código
- Métricas de deuda técnica organizacional
