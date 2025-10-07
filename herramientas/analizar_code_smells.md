# 🔍 Herramienta: Analizar Code Smells

> **Versión:** 1.0  
> **Fecha de Creación:** 6 de octubre de 2025  
> **Autor:** Sistema de Herramientas ArchDev Pro  
> **Estado:** Activa

---

## 📋 Identificación

**Herramienta:** `analizar_code_smells`

---

## 🎯 Objetivo

Analizar código Java automáticamente para identificar **code smells**, violaciones de principios **SOLID**, patrones **anti-patrón** y oportunidades de **refactoring**. Genera un reporte priorizado con sugerencias concretas de mejora, acelerando la fase de análisis en el flujo de refactorización de ArchDev Pro.

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- El código fuente Java a analizar (clase completa preferiblemente, o archivo `.java`).
- Puede ser proporcionado como ruta de archivo o contenido directo del código.

**Secundario (Opcional):**
- Contexto del proyecto desde `contexto_proyecto.md` (tipo de proyecto, versión Java, patrones arquitectónicos).
- Nivel de análisis deseado (básico, moderado o exhaustivo).
- Umbrales personalizados para detección de code smells (opcional).

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
- ✅ **Onad** (consulta para decisiones estratégicas)

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Parsing y Análisis Estático (AST)

- **Parsear código Java a Abstract Syntax Tree (AST):**
  - Utilizar librerías como JavaParser o Eclipse JDT para generar representación estructurada del código.
  - Extraer información de clases, métodos, campos, imports y anotaciones.

- **Calcular métricas base:**
  - Líneas de código por clase/método (LOC)
  - Complejidad ciclomática (McCabe Complexity)
  - Profundidad de anidación máxima
  - Número de dependencias (imports)
  - Número de métodos y campos por clase

### 2️⃣ Detección de Code Smells

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

### 3️⃣ Análisis de Principios SOLID

- **SRP (Single Responsibility):** Detectar múltiples razones de cambio (ej. validación + persistencia + notificación en misma clase).
- **OCP (Open/Closed):** Detectar if/else o switch extensos que deberían ser Strategy Pattern.
- **LSP (Liskov Substitution):** Detectar violaciones en herencia (métodos sobrescritos que lanzan excepciones no esperadas).
- **ISP (Interface Segregation):** Detectar interfaces con > 7 métodos (God Interface).
- **DIP (Dependency Inversion):** Detectar dependencias concretas en lugar de abstracciones.

### 4️⃣ Cálculo de Priorización (ROI Score)

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

### 5️⃣ Generación del Reporte

- Ensamblar el reporte completo en formato JSON estructurado.
- Incluir métricas generales, lista de code smells priorizados, y recomendaciones concretas.
- Calcular métricas objetivo post-refactoring.
- Generar sugerencias de refactoring con pasos concretos para cada problema.

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
        "pasos": [
          "Extraer validación a EmailValidator y PasswordValidator",
          "Extraer persistencia a UserRepository (interfaz + implementación)",
          "Extraer notificaciones a UserNotificationService",
          "Aplicar Event-Driven para desacoplar notificaciones"
        ]
      }
    }
  ],
  "patrones_detectados": [
    {
      "patron": "SERVICE_LAYER",
      "calidad": "PARCIAL",
      "observaciones": "El service existe pero tiene demasiadas responsabilidades. Considerar dividir en UserCommandService y UserQueryService (CQRS)."
    }
  ],
  "recomendaciones_priorizadas": [
    {
      "prioridad": 1,
      "titulo": "Refactorizar God Object aplicando SRP",
      "justificacion": "Alta deuda técnica (8h estimadas), dificulta testing (cobertura actual ~30%) y mantenimiento",
      "impacto_estimado": "Reducción 60% complejidad, +40% cobertura de tests, mejora mantenibilidad de BAJO a MEDIO",
      "code_smell_ids": ["CS001"]
    }
  ],
  "metricas_objetivo_post_refactoring": {
    "lineas_codigo_max_clase": 150,
    "complejidad_ciclomatica_max": 10,
    "nivel_mantenibilidad_objetivo": "ALTO",
    "cobertura_tests_objetivo": 85
  }
}
```

---

## 💡 Ejemplo de Uso

**Entrada:**
```java
// UserService.java (450 líneas)
@Service
public class UserService {
    private JdbcTemplate jdbcTemplate; // Acoplamiento con infraestructura
    
    public User registerUser(String email, String password) {
        // Validación mezclada
        if (!email.contains("@")) {
            throw new IllegalArgumentException("Email inválido");
        }
        
        // Persistencia directa
        jdbcTemplate.update("INSERT INTO users...", email, password);
        
        // Notificaciones mezcladas
        sendEmail(email, "Bienvenido!");
        
        // ... 400 líneas más ...
    }
}
```

**Parámetros:**
- archivo_java: UserService.java
- nivel_analisis: exhaustivo
- tipo_proyecto: spring-boot
- version_java: 17

**Salida esperada (resumida):**
```markdown
### 🔍 Análisis Completado: UserService.java

**Métricas Generales:**
- 📏 Líneas de código: **450** (⚠️ Supera límite recomendado: 150)
- 🔢 Complejidad ciclomática: **28** (🔴 Crítico - límite: 10)
- 📊 Nivel de mantenibilidad: **BAJO**
- ⏱️ Deuda técnica estimada: **8 horas**

---

### 🚨 3 Code Smells Detectados (ordenados por impacto)

#### 🔴 #1. God Object (Severidad: CRÍTICA) | ROI Score: 9.5
**Ubicación:** Líneas 1-450  
**Problema:** Múltiples responsabilidades (validación + persistencia + notificación)

**Impacto:**
- 🔴 Testabilidad: ALTO (cobertura actual ~30%)
- 🔴 Mantenibilidad: ALTO (dificulta cambios)
- 🟡 Escalabilidad: MEDIO

**Principios violados:** SRP, OCP

**Refactoring sugerido:** Extract Class + Repository Pattern  
**Esfuerzo estimado:** 5 horas

**Pasos concretos:**
1. Extraer validación → `EmailValidator` y `PasswordValidator`
2. Extraer persistencia → `UserRepository` (interfaz + implementación)
3. Extraer notificaciones → `UserNotificationService`
4. Aplicar Event-Driven para desacoplar notificaciones

---

### 🎯 Recomendación Prioritaria

Te sugiero empezar por el **Code Smell #1 (God Object)** ya que:
- Tiene el ROI más alto (9.5)
- Mejorará cobertura de tests de 30% a ~70%
- Reducirá complejidad en 60%
```

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

### Limitaciones Conocidas

- Solo analiza código Java (no Kotlin, Groovy, etc.)
- Requiere código sintácticamente correcto (no funciona con errores de compilación)
- Análisis de "Feature Envy" puede generar falsos positivos en DTOs

### Futuras Mejoras

- Machine Learning para mejorar detección de patrones
- Soporte multi-lenguaje (Kotlin, TypeScript)
- Integración con Git para análisis de evolución histórica de deuda técnica

### Relación con Otras Herramientas

**Herramientas que la invocan:**
- `refactorizar` (automáticamente en Paso 1 de su flujo)
- `define_arquitectura` (para análisis inicial de código legacy)

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

### Métricas de Éxito de la Herramienta

| Criterio | Objetivo | Medición |
|----------|----------|----------|
| **Precisión** | Detectar 90%+ de code smells comunes | Validación contra benchmark estándar |
| **Velocidad** | < 10 segundos para archivos de 1000 líneas | Medición de tiempo de ejecución |
| **Priorización** | 80%+ de casos ordenados correctamente | Feedback de usuarios expertos |
| **Reducción de tiempo** | De 30 min manual a 2 min automatizado | Comparación antes/después |

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2025-10-06 | Creación inicial de la herramienta |
