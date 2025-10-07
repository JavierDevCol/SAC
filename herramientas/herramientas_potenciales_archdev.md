# 🛠️ Herramientas Potenciales para ArchDev Pro

> Documento de análisis y especificación de herramientas potenciales identificadas durante la refactorización del rol **ArchDev Pro**. Este documento sirve como referencia para futuras implementaciones o refactorizaciones de herramientas existentes.

---

## 📋 Índice

1. [Herramienta 1: `analizar_code_smells` (NUEVA)](#1-analizar_code_smells)
2. [Herramienta 2: `generar_tests_automaticos` (NUEVA)](#2-generar_tests_automaticos)
3. [Mejora a herramienta existente: `refactorizar`](#3-mejora-refactorizar)
4. [Mejora a herramienta existente: `crear_pruebas`](#4-mejora-crear_pruebas)

---

## 1. `analizar_code_smells`

### 🎯 Propósito

Analizar código Java automáticamente para identificar code smells, violaciones de principios SOLID, patrones anti-patrón y oportunidades de refactoring. Genera un reporte priorizado con sugerencias concretas de mejora.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es el primer paso crítico en el flujo de refactorización de ArchDev Pro.

### 🔍 Problema que Resuelve

- **Antes:** ArchDev debe leer y analizar código manualmente para identificar problemas
- **Después:** La herramienta detecta automáticamente code smells y prioriza por impacto

### 📥 Input Esperado

**Parámetros:**
- `archivo_java` (string, requerido): Path del archivo o contenido del código Java
- `contexto_proyecto` (object, opcional): Información del proyecto para análisis contextual
  ```json
  {
    "tipo_proyecto": "spring-boot",
    "version_java": "17",
    "patrones_arquitectonicos": ["clean-architecture", "hexagonal"],
    "nivel_analisis": "exhaustivo"  // "basico", "moderado", "exhaustivo"
  }
  ```

### 📤 Output Esperado

**Formato: JSON con análisis detallado**

```json
{
  "analisis_completado": true,
  "archivo_analizado": "UserService.java",
  "metricas_generales": {
    "lineas_codigo": 450,
    "complejidad_ciclomatica": 28,
    "nivel_mantenibilidad": "BAJO",
    "deuda_tecnica_estimada_horas": 8
  },
  "code_smells_detectados": [
    {
      "tipo": "GOD_OBJECT",
      "severidad": "CRITICA",
      "linea_inicio": 1,
      "linea_fin": 450,
      "descripcion": "La clase UserService tiene múltiples responsabilidades: validación, persistencia, notificación y logging",
      "impacto": {
        "mantenibilidad": "ALTO",
        "testabilidad": "ALTO",
        "escalabilidad": "MEDIO"
      },
      "principios_violados": ["SRP", "OCP"],
      "metrica_soporte": "450 líneas, 28 métodos, complejidad ciclomática = 28",
      "refactoring_sugerido": {
        "patron": "Extract Class + Repository Pattern",
        "esfuerzo_estimado": "4-6 horas",
        "prioridad": 1,
        "pasos": [
          "Extraer validación a EmailValidator y PasswordValidator",
          "Extraer persistencia a UserRepository",
          "Extraer notificaciones a UserNotificationService",
          "Aplicar Event-Driven para desacoplar notificaciones"
        ]
      }
    },
    {
      "tipo": "LONG_METHOD",
      "severidad": "ALTA",
      "linea_inicio": 45,
      "linea_fin": 120,
      "descripcion": "El método registerUser() tiene 75 líneas con múltiples niveles de anidación",
      "impacto": {
        "legibilidad": "ALTO",
        "testabilidad": "MEDIO",
        "mantenibilidad": "ALTO"
      },
      "principios_violados": ["SRP"],
      "metrica_soporte": "75 líneas, 4 niveles de anidación, complejidad = 12",
      "refactoring_sugerido": {
        "patron": "Extract Method",
        "esfuerzo_estimado": "1-2 horas",
        "prioridad": 2,
        "pasos": [
          "Extraer validateUserInput() privado",
          "Extraer hashPassword() privado",
          "Extraer saveToDatabase() delegando a repository",
          "Extraer sendWelcomeEmail() delegando a notification service"
        ]
      }
    },
    {
      "tipo": "MAGIC_NUMBERS",
      "severidad": "MEDIA",
      "lineas": [67, 89, 102],
      "descripcion": "Uso de números mágicos sin constantes declaradas (18, 100, 3600)",
      "impacto": {
        "mantenibilidad": "MEDIO",
        "legibilidad": "MEDIO"
      },
      "refactoring_sugerido": {
        "patron": "Replace Magic Number with Symbolic Constant",
        "esfuerzo_estimado": "30 minutos",
        "prioridad": 4,
        "codigo_sugerido": "private static final int MINIMUM_AGE = 18;"
      }
    },
    {
      "tipo": "COUPLING_INFRAESTRUCTURA",
      "severidad": "CRITICA",
      "linea_inicio": 25,
      "linea_fin": 30,
      "descripcion": "La capa de dominio depende directamente de JdbcTemplate (infraestructura)",
      "impacto": {
        "testabilidad": "CRITICO",
        "escalabilidad": "ALTO",
        "mantenibilidad": "ALTO"
      },
      "principios_violados": ["DIP", "Clean Architecture"],
      "refactoring_sugerido": {
        "patron": "Dependency Inversion + Repository Pattern",
        "esfuerzo_estimado": "3-4 horas",
        "prioridad": 1,
        "pasos": [
          "Definir interfaz UserRepository en capa de dominio",
          "Implementar JpaUserRepository en infraestructura",
          "Inyectar dependencia por constructor usando la interfaz"
        ]
      }
    }
  ],
  "patrones_detectados": [
    {
      "patron": "SERVICE_LAYER",
      "calidad": "PARCIAL",
      "observaciones": "El service existe pero tiene demasiadas responsabilidades. Considerar dividir."
    }
  ],
  "recomendaciones_priorizadas": [
    {
      "prioridad": 1,
      "titulo": "Refactorizar God Object aplicando SRP",
      "justificacion": "Alta deuda técnica, dificulta testing y mantenimiento",
      "impacto_estimado": "Reducción 60% complejidad, +40% cobertura de tests"
    },
    {
      "prioridad": 2,
      "titulo": "Desacoplar capa de dominio de infraestructura",
      "justificacion": "Violación crítica de Clean Architecture, dificulta tests unitarios",
      "impacto_estimado": "Testabilidad de 30% a 90%"
    },
    {
      "prioridad": 3,
      "titulo": "Extraer métodos largos",
      "justificacion": "Mejora legibilidad y facilita comprensión del código",
      "impacto_estimado": "Reducción 40% complejidad ciclomática"
    },
    {
      "prioridad": 4,
      "titulo": "Reemplazar magic numbers con constantes",
      "justificacion": "Quick win, bajo esfuerzo, mejora mantenibilidad",
      "impacto_estimado": "Mejora legibilidad sin cambiar comportamiento"
    }
  ],
  "metricas_objetivo_post_refactoring": {
    "lineas_codigo": "< 150 por clase",
    "complejidad_ciclomatica": "< 10",
    "nivel_mantenibilidad": "ALTO",
    "cobertura_tests": "> 80%"
  }
}
```

### 🔧 Lógica Interna Sugerida

**Fase 1: Análisis Estático (AST)**
1. Parsear código Java a Abstract Syntax Tree
2. Calcular métricas:
   - Líneas de código por clase/método
   - Complejidad ciclomática (McCabe)
   - Profundidad de anidación
   - Número de dependencias

**Fase 2: Detección de Code Smells**
- **God Object:** Clase > 300 líneas o > 15 métodos
- **Long Method:** Método > 50 líneas o complejidad > 10
- **Feature Envy:** Clase usa más métodos de otra clase que propios
- **Data Clumps:** Mismo grupo de parámetros en múltiples métodos
- **Magic Numbers:** Literales numéricos sin constante
- **Acoplamiento infraestructura:** Imports de javax.persistence, jdbc, etc. en dominio

**Fase 3: Análisis de Principios SOLID**
- **SRP:** Detectar múltiples razones de cambio (validación + persistencia + notificación)
- **OCP:** Detectar if/else o switch que deberían ser Strategy
- **LSP:** Detectar violaciones en herencia
- **DIP:** Detectar dependencias concretas en lugar de abstracciones

**Fase 4: Priorización por Impacto**
- Calcular score de impacto: (severidad × mantenibilidad × testabilidad) / esfuerzo
- Ordenar recomendaciones por ROI

### 🎭 Comportamiento Esperado del Rol ArchDev Pro

**Con esta herramienta:**
```markdown
Usuario: "Revisa este código y dime cómo mejorarlo"
[Comparte UserService.java con 450 líneas]

ArchDev Pro: "Voy a analizar el código para identificar oportunidades de mejora..."

[Ejecuta: > analizar_code_smells archivo_java=UserService.java]

ArchDev Pro: "He detectado **4 code smells críticos** en UserService.java:

🔴 **1. God Object (Severidad CRÍTICA)**
La clase tiene 450 líneas y maneja 4 responsabilidades diferentes: validación, 
persistencia, notificación y logging. Esto viola el principio SRP.

**Impacto:** Dificulta testing (cobertura actual ~30%), mantenimiento y escalabilidad.

**Refactoring sugerido:** Aplicar Extract Class + Repository Pattern
- Esfuerzo estimado: 4-6 horas
- Impacto esperado: Reducción 60% complejidad, +40% cobertura tests

---

🔴 **2. Acoplamiento de Infraestructura (Severidad CRÍTICA)**
La capa de dominio depende directamente de JdbcTemplate (línea 25-30).

**Impacto:** Imposible testear sin base de datos real, viola Clean Architecture.

**Refactoring sugerido:** Dependency Inversion + Repository Pattern
[Código específico del refactoring]

---

¿Quieres que proceda con el refactoring del problema #1 (God Object)?"
```

### 📈 Criterios de Éxito

- ✅ Detecta 90%+ de code smells comunes
- ✅ Priorización por impacto precisa en 80%+ de casos
- ✅ Completa análisis en < 10 segundos para archivos de 1000 líneas
- ✅ Reduce tiempo de análisis manual de 30 min a 2 min

---

## 2. `generar_tests_automaticos`

### 🎯 Propósito

Generar código de pruebas (unitarias, integración) automáticamente basándose en el código fuente analizado, cubriendo casos felices, casos de borde y escenarios de error.

### 📊 Nivel de Prioridad

**🟡 MEDIA-ALTA** - Acelera significativamente el proceso de creación de tests.

### 🔍 Problema que Resuelve

- **Antes:** ArchDev escribe tests manualmente, proceso lento y propenso a omitir casos
- **Después:** Generación automática de scaffolding de tests con casos identificados

### 📥 Input Esperado

**Parámetros:**
- `codigo_fuente` (string, requerido): Código Java a testear
- `tipo_test` (enum, requerido): "UNITARIO", "INTEGRACION", "AMBOS"
- `framework_test` (string, opcional): "junit5", "testcontainers" (default: "junit5")
- `nivel_cobertura` (enum, opcional): "BASICO", "COMPLETO", "EXHAUSTIVO" (default: "COMPLETO")

### 📤 Output Esperado

```json
{
  "tests_generados": true,
  "tipo_test": "UNITARIO",
  "casos_identificados": {
    "casos_felices": 3,
    "casos_borde": 4,
    "casos_error": 3
  },
  "cobertura_estimada": {
    "lineas": "95%",
    "branches": "90%"
  },
  "codigo_tests": "...",
  "dependencias_necesarias": [
    "org.junit.jupiter:junit-jupiter:5.10.0",
    "org.mockito:mockito-core:5.5.0",
    "org.assertj:assertj-core:3.24.2"
  ],
  "instrucciones_ejecucion": "mvn test -Dtest=UserServiceTest"
}
```

### 🔧 Lógica Interna Sugerida

**Fase 1: Análisis de Código**
1. Identificar métodos públicos (casos de prueba)
2. Analizar parámetros y tipos de retorno
3. Detectar dependencias (para mocking)
4. Identificar excepciones declaradas

**Fase 2: Generación de Casos**
- **Happy path:** Valores válidos típicos
- **Edge cases:** null, vacío, límites (0, -1, MAX_VALUE)
- **Error cases:** Valores inválidos, excepciones esperadas

**Fase 3: Generación de Código**
- Usar templates de JUnit 5 + Mockito
- Nomenclatura descriptiva: `shouldReturnUserWhenEmailIsValid()`
- AssertJ para assertions legibles
- @BeforeEach para setup común

---

## 3. Mejora: `refactorizar`

### 🎯 Propósito de la Mejora

Refactorizar la herramienta existente para integrarla con el proceso de 5 pasos de ArchDev Pro y conectarla con `analizar_code_smells`.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es la herramienta principal de ArchDev Pro.

### 🔍 Estado Deseado

**Flujo mejorado:**

1. **Input:** Usuario proporciona código
2. **Auto-ejecutar:** `analizar_code_smells` automáticamente
3. **Mostrar análisis:** Presentar code smells detectados
4. **Proponer plan:** Basado en análisis automático
5. **Ejecutar refactoring:** Código antes/después
6. **Generar tests:** Auto-ejecutar `generar_tests_automaticos`
7. **Validar:** Presentar checklist

**Parámetros nuevos:**
- `ejecutar_analisis_automatico` (boolean, default: true)
- `generar_tests_post_refactoring` (boolean, default: true)
- `nivel_refactoring` (enum): "SIMPLE", "MEDIO", "ARQUITECTONICO"

---

## 4. Mejora: `crear_pruebas`

### 🎯 Propósito de la Mejora

Integrar con `generar_tests_automaticos` para acelerar el proceso y conectar con el flujo de 5 pasos de ArchDev Pro.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Herramienta crítica para TDD.

### 🔍 Estado Deseado

**Flujo mejorado:**

1. **Input:** Usuario proporciona código o solicitud de tests
2. **Auto-generar scaffolding:** Ejecutar `generar_tests_automaticos`
3. **Revisar casos:** ArchDev Pro revisa y ajusta casos generados
4. **Presentar código:** Tests completos y ejecutables
5. **Instrucciones:** Comandos para ejecutar tests

**Parámetros nuevos:**
- `usar_generacion_automatica` (boolean, default: true)
- `incluir_testcontainers` (boolean, default: false)
- `nivel_cobertura_objetivo` (int, default: 80)

---

## 📝 Notas Finales

### Priorización Recomendada para Implementación

1. **🥇 Primera iteración (Crítica):**
   - Implementar `analizar_code_smells`
   - Mejorar `refactorizar` con integración automática

2. **🥈 Segunda iteración (Alta):**
   - Implementar `generar_tests_automaticos`
   - Mejorar `crear_pruebas` con integración

3. **🥉 Tercera iteración (Optimización):**
   - Machine Learning para mejorar detección de code smells
   - Aprendizaje de patrones de refactoring del usuario

### Impacto Estimado

| Herramienta/Mejora | Ahorro de Tiempo | Mejora de Calidad | Complejidad Implementación |
|-------------------|------------------|-------------------|---------------------------|
| `analizar_code_smells` | 🔥🔥🔥🔥 (90%) | 🔥🔥🔥🔥 (95%) | 🔴 Alta |
| `generar_tests_automaticos` | 🔥🔥🔥 (70%) | 🔥🔥🔥 (80%) | 🔴 Alta |
| Mejora `refactorizar` | 🔥🔥 (60%) | 🔥🔥🔥 (75%) | 🟡 Media |
| Mejora `crear_pruebas` | 🔥🔥🔥 (75%) | 🔥🔥🔥 (85%) | 🟡 Media |

---

## 📅 Última Actualización

**Fecha:** 6 de octubre de 2025  
**Autor:** Análisis durante refactorización de ArchDev Pro v2.0  
**Estado:** Propuesta de herramientas pendientes de implementación
