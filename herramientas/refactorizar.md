# 🔧 Herramienta: Refactorizar Código

> **Versión:** 2.0  
> **Fecha de Actualización:** 6 de octubre de 2025  
> **Autor:** Sistema de Herramientas ArchDev Pro  
> **Estado:** Activa  
> **Cambio Principal v2.0:** Integración automática con `analizar_code_smells` para priorización por ROI

---

## 📋 Identificación

**Herramienta:** `refactorizar`

---

## 🎯 Objetivo

Guiar al usuario en un proceso estructurado de **refactorización de código Java/Spring Boot**, desde el análisis automático de code smells hasta la implementación validada con tests, mejorando la calidad, testabilidad y mantenibilidad del código mediante la aplicación de principios SOLID y patrones de diseño.

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`analizar_code_smells`** | Paso 1 - Al iniciar el refactoring (si `ejecutar_analisis_automatico: true`) | Identificar automáticamente code smells y priorizarlos por ROI |
| **`solucionar_smells`** | Cuando el usuario elige "Modo Automático" | Ejecutar correcciones automatizables de code smells detectados |
| **`crear_pruebas`** | Paso 4 - Después del refactoring (si `generar_tests_post_refactoring: true`) | Generar suite de tests unitarios para el código refactorizado |

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **ArchDev Pro** | Cuando se detecta código con code smells o deuda técnica | Mejorar la calidad del código existente |
| **`define_arquitectura`** | Durante reestructuración arquitectónica | Refactorizar código para ajustarse a nueva arquitectura definida |

---

## 🤖 Integración Automática Avanzada

**🆕 Novedad v2.0:** Esta herramienta ahora ejecuta automáticamente `analizar_code_smells` en el **Paso 1** para acelerar el análisis inicial y priorizar refactorings por impacto/ROI.

### Flujo Automatizado

```
Usuario proporciona código
    ↓
AUTO: analizar_code_smells
    ↓
Reporte priorizado por ROI
    ↓
Usuario selecciona code smell
    ↓
Continuar con Paso 2-5
```

### Beneficios de la Integración

| Aspecto | Antes (v1.0) | Después (v2.0) | Mejora |
|---------|-------------|----------------|--------|
| Tiempo de análisis | 20-30 min | 2-3 min | 🔥🔥🔥🔥 (-90%) |
| Precisión | ~70% (manual) | ~90% (automático) | 🔥🔥🔥 (+28%) |
| Priorización | Subjetiva | Objetiva (ROI Score) | 🔥🔥🔥🔥 |

### Control de Ejecución

El análisis automático puede desactivarse si el usuario ya tiene un análisis previo:

```json
{
  "ejecutar_analisis_automatico": false
}
```

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- El fragmento de código Java a refactorizar (clase completa preferiblemente).
- Puede ser proporcionado como ruta de archivo o contenido directo del código.

**Secundario (Opcional):**
- Contexto del proyecto (arquitectura, patrones usados, restricciones específicas).
- Análisis de code smells previo (si ya se ejecutó).
- Tests existentes relacionados con el código.

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `codigo_fuente` | string | ruta o contenido | - | Código Java a refactorizar (requerido) |
| `ejecutar_analisis_automatico` | boolean | true\|false | true | Si ejecutar `analizar_code_smells` en Paso 1 |
| `nivel_refactoring` | string | SIMPLE\|MEDIO\|ARQUITECTONICO | MEDIO | Complejidad del refactoring esperado |
| `generar_tests_post_refactoring` | boolean | true\|false | true | Si ejecutar `crear_pruebas` después del refactoring |
| `nivel_analisis` | string | basico\|moderado\|exhaustivo | exhaustivo | Nivel de profundidad del análisis automático |
| `contexto_adicional` | string | texto libre | - | Dependencias, arquitectura, restricciones |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (principal)
- ✅ **Onad** (revisión estratégica)

---

## 🔄 Proceso Paso a Paso

### **Paso 1: Análisis Profundo del Código** 🤖

**🆕 EJECUCIÓN AUTOMÁTICA:** Al iniciar este flujo, la herramienta ejecuta automáticamente `analizar_code_smells` para identificar problemas y priorizarlos por impacto/ROI.

#### 1.1 Análisis Automático

**Acción interna (si `ejecutar_analisis_automatico: true`):**
```bash
> analizar_code_smells 
    archivo_java=<codigo_proporcionado>
    nivel_analisis=exhaustivo
    contexto_proyecto=<from_context_md>
```

#### 1.2 Presentación del Reporte

Mostrar al usuario:
- ✅ **Métricas generales:** LOC, complejidad ciclomática, deuda técnica estimada
- ✅ **Code smells detectados:** Ordenados por ROI Score (impacto/esfuerzo)
- ✅ **Recomendación prioritaria:** Con justificación técnica

**Ejemplo de presentación:**
```markdown
### 🔍 Análisis Completado: UserService.java

**Métricas Generales:**
- 📏 Líneas de código: **450** (⚠️ Supera límite recomendado: 150)
- 🔢 Complejidad ciclomática: **28** (🔴 Crítico - límite: 10)
- ⏱️ Deuda técnica estimada: **8 horas**

### 🚨 3 Code Smells Detectados (ordenados por impacto)

#### 🔴 #1. God Object (Severidad: CRÍTICA) | ROI Score: 9.5
**Problema:** Múltiples responsabilidades (validación + persistencia + notificación)
**Refactoring sugerido:** Extract Class + Repository Pattern
**Esfuerzo:** 5 horas
```

#### 1.3 Selección del Problema

**Pregunta obligatoria:**
> "He detectado **X code smells críticos**. Te recomiendo empezar por **[Problema #1]** por su alto impacto/ROI (Score: 9.5). 
> 
> **🔧 Opciones de Refactoring:**
> 
> 1. **🤖 Automático** - Ejecutar `solucionar_smells` para correcciones automatizables
>    - ⚡ Tiempo: 1-3 horas (85% automatizado)
>    - 🎯 Ideal para: Code smells estándar, proyectos con tiempo limitado
>    - ✅ Incluye: Código refactorizado + tests + validación automática
> 
> 2. **🧠 Guiado** - Continuar con planificación manual paso a paso  
>    - 📚 Tiempo: 4-8 horas (proceso educativo completo)
>    - 🎯 Ideal para: Aprendizaje, casos complejos, decisiones arquitectónicas
>    - ✅ Incluye: Análisis detallado + planificación estratégica + implementación supervisada
> 
> **¿Cuál método prefieres para este refactoring?**"

**Si usuario elige "Automático":**
- Ejecutar `solucionar_smells` con el reporte JSON generado
- Al completar, ofrecer continuar con más code smells o finalizar
- Si hay code smells no automatizables, continuar con flujo manual para esos casos

**Si usuario elige "Guiado":**
- Continuar con Paso 2 (Planificación manual) del flujo tradicional

---

### **Paso 2: Planificación del Refactoring** 📋

Una vez seleccionado el code smell a refactorizar:

#### 2.1 Diseño de la Estrategia

**Presentar al usuario:**
```markdown
## 📋 Plan de Refactoring para: [Nombre del Code Smell]

### 🎯 Objetivo
[Descripción clara del objetivo, ej. "Separar responsabilidades aplicando SRP"]

### 🛠️ Patrón/Técnica a Aplicar
[Ej. "Extract Class + Repository Pattern + Dependency Injection"]

### 📦 Clases/Archivos Involucrados
- ✅ **A modificar:** `UserService.java`
- 🆕 **A crear:** 
  - `EmailValidator.java`
  - `UserRepository.java` (interfaz)
  - `JpaUserRepository.java` (implementación)
  - `UserNotificationService.java`

### ⚙️ Pasos de Implementación
1. Extraer validación de email → `EmailValidator`
2. Extraer persistencia → `UserRepository` + implementación
3. Extraer notificaciones → `UserNotificationService`
4. Inyectar dependencias en `UserService` refactorizado
5. Actualizar tests existentes

### ⚠️ Riesgos Identificados
- Posibles dependencias ocultas en otros servicios que usan `UserService`
- Necesidad de actualizar tests existentes

### ✅ Criterios de Éxito
- Reducción complejidad ciclomática: 28 → ~12
- Cobertura de tests: 30% → 80%+
- LOC por clase: < 150 líneas
```

#### 2.2 Confirmación

**Pregunta obligatoria:**
> "¿Apruebas este plan de refactoring? ¿Algún ajuste antes de proceder con la implementación?"

---

### **Paso 3: Implementación del Refactoring** 💻

#### 3.1 Código Refactorizado

**Formato de presentación:**

```markdown
## 🔄 Código Refactorizado

### 📄 Archivo: UserService.java

#### ❌ ANTES (450 líneas, complejidad: 28)

```java
@Service
public class UserService {
    private JdbcTemplate jdbcTemplate; // ⚠️ Acoplamiento con infraestructura
    
    public User registerUser(String email, String password) {
        // ❌ Validación mezclada con lógica de negocio
        if (!email.contains("@")) {
            throw new IllegalArgumentException("Email inválido");
        }
        
        // ❌ Lógica de persistencia directa
        jdbcTemplate.update("INSERT INTO users...", email, password);
        
        // ❌ Notificaciones mezcladas
        sendEmail(email, "Bienvenido!");
        
        // ... 400 líneas más ...
    }
}
```

#### ✅ DESPUÉS (80 líneas, complejidad: 5)

**UserService.java (refactorizado):**
```java
@Service
public class UserService {
    private final EmailValidator emailValidator;
    private final UserRepository userRepository;
    private final UserNotificationService notificationService;
    
    // ✅ Inyección de dependencias por constructor
    public UserService(
        EmailValidator emailValidator,
        UserRepository userRepository,
        UserNotificationService notificationService
    ) {
        this.emailValidator = emailValidator;
        this.userRepository = userRepository;
        this.notificationService = notificationService;
    }
    
    public User registerUser(String email, String password) {
        // ✅ Responsabilidades claramente separadas
        emailValidator.validate(email);
        User user = userRepository.save(new User(email, password));
        notificationService.sendWelcomeEmail(user);
        return user;
    }
}
```

[... más clases nuevas ...]
```

#### 3.2 Principios SOLID Aplicados

**Explicar qué principios se aplicaron:**
```markdown
### 🎯 Principios SOLID Aplicados

1. **✅ SRP (Single Responsibility Principle)**
   - **Antes:** `UserService` tenía 4 responsabilidades
   - **Después:** Cada clase tiene una única razón de cambio

2. **✅ OCP (Open/Closed Principle)**
   - Las interfaces `UserRepository` y `EmailValidator` permiten extensión sin modificación

3. **✅ DIP (Dependency Inversion Principle)**
   - `UserService` depende de abstracciones (`UserRepository`), no de implementaciones concretas
```

---

### **Paso 4: Creación/Actualización de Tests** 🧪

#### 4.1 Evaluación de Tests Existentes

Revisar si existen tests para el código original:
- ✅ Tests existentes: Actualizar para el nuevo diseño
- ❌ Sin tests: Crear suite completa

#### 4.2 Generación Automática (Opcional)

**Si `generar_tests_post_refactoring: true`:**

```bash
> crear_pruebas
    archivo_java=UserService.java
    tipo_tests=unitarios
    cobertura_objetivo=85
```

#### 4.3 Presentación de Tests

**Ejemplo:**
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private EmailValidator emailValidator;
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private UserNotificationService notificationService;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void registerUser_withValidEmail_shouldSaveAndNotify() {
        // Given
        String email = "test@example.com";
        String password = "password123";
        User expectedUser = new User(email, password);
        
        when(userRepository.save(any(User.class))).thenReturn(expectedUser);
        
        // When
        User result = userService.registerUser(email, password);
        
        // Then
        verify(emailValidator).validate(email);
        verify(userRepository).save(any(User.class));
        verify(notificationService).sendWelcomeEmail(expectedUser);
        assertThat(result).isEqualTo(expectedUser);
    }
}
```

---

### **Paso 5: Validación y Entrega** ✅

#### 5.1 Métricas de Mejora

**Presentar comparativa:**

```markdown
## 📊 Métricas de Mejora

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| Líneas de código (LOC) | 450 | 180 (-60%) | 🔥🔥🔥🔥 |
| Complejidad ciclomática | 28 | 12 (-57%) | 🔥🔥🔥🔥 |
| Número de clases | 1 | 5 | ➖ (por diseño) |
| Responsabilidades por clase | 4 | 1 | 🔥🔥🔥🔥🔥 |
| Acoplamiento con infraestructura | Alto | Nulo | 🔥🔥🔥🔥🔥 |
| Cobertura de tests | 30% | 85% | 🔥🔥🔥🔥 |
| Nivel de mantenibilidad | BAJO | ALTO | 🔥🔥🔥🔥🔥 |
| Deuda técnica estimada | 8 horas | 1 hora | 🔥🔥🔥🔥 |
```

#### 5.2 Justificación de Beneficios

```markdown
### 🎁 Beneficios del Refactoring

**Corto Plazo (inmediato):**
- ✅ Código más legible y comprensible
- ✅ Clases más pequeñas y enfocadas
- ✅ Tests más simples y mantenibles

**Medio Plazo (1-3 meses):**
- ✅ Reducción de bugs (mejor testabilidad)
- ✅ Velocidad de desarrollo aumentada (menor complejidad)
- ✅ Onboarding de nuevos desarrolladores más rápido

**Largo Plazo (6+ meses):**
- ✅ Escalabilidad mejorada
- ✅ Costo de mantenimiento reducido (-87% deuda técnica)
- ✅ Flexibilidad arquitectónica
```

#### 5.3 Pregunta Final

**Confirmación:**
> "✅ **Refactoring completado**. El código ahora cumple con principios SOLID, tiene 85% de cobertura de tests y reduce la complejidad en 57%. ¿Deseas que analice otro code smell de la lista o necesitas ajustes en este refactoring?"

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| **Contexto insuficiente** | Solicitar clase completa + dependencias |
| **Código con errores de sintaxis** | Pedir corrección antes de refactorizar |
| **Análisis automático falla** | Fallback a análisis manual |
| **Sin code smells detectados** | Confirmar con usuario si aún desea refactoring |
| **Tests existentes incompatibles** | Proponer actualización de tests antes de refactorizar |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Un documento Markdown estructurado con el refactoring completo.

**Contendrá:**
1. ✅ Reporte de análisis automático (si aplica)
2. ✅ Plan de refactoring paso a paso
3. ✅ Código refactorizado con formato "Antes/Después"
4. ✅ Justificación de cambios (principios SOLID aplicados)
5. ✅ Tests generados (si se configuró)
6. ✅ Métricas de mejora

---

## 💡 Ejemplo de Uso

**Entrada:**
```java
// UserService.java (450 líneas)
@Service
public class UserService {
    private JdbcTemplate jdbcTemplate;
    
    public User registerUser(String email, String password) {
        // Validación mezclada
        if (!email.contains("@")) {
            throw new IllegalArgumentException("Email inválido");
        }
        
        // Persistencia directa
        jdbcTemplate.update("INSERT INTO users...", email, password);
        
        // Notificaciones mezcladas
        sendEmail(email, "Bienvenido!");
        
        // ... 400 líneas más con múltiples responsabilidades ...
    }
}
```

**Parámetros:**
- codigo_fuente: UserService.java
- ejecutar_analisis_automatico: true
- nivel_refactoring: MEDIO
- generar_tests_post_refactoring: true

**Salida esperada:**
- Análisis automático con 3 code smells detectados
- Plan de refactoring aprobado por usuario
- 5 clases nuevas creadas siguiendo SRP
- Suite de tests con 85% de cobertura
- Métricas mostrando 60% reducción en complejidad

---

## 📚 Referencias y Notas

### Relación con Otras Herramientas

**Herramientas que Invoca Automáticamente:**
1. **`analizar_code_smells`** (Paso 1 - si `ejecutar_analisis_automatico: true`)
2. **`crear_pruebas`** (Paso 4 - si `generar_tests_post_refactoring: true`)

**Herramientas que la Invocan:**
- **`define_arquitectura`** (puede invocar `refactorizar` para ajustar código existente)

### Patrones de Refactoring Más Comunes

| Code Smell | Patrón de Refactoring Sugerido |
|------------|-------------------------------|
| God Object | Extract Class + Single Responsibility |
| Long Method | Extract Method + Compose Method |
| Feature Envy | Move Method + Encapsulate Field |
| Data Clumps | Introduce Parameter Object |
| Switch Statements | Replace Conditional with Polymorphism / Strategy Pattern |
| Duplicate Code | Extract Method / Pull Up Method |

### Limitaciones Conocidas

- Solo analiza código Java/Spring Boot (no otros lenguajes)
- Requiere contexto del proyecto para refactorings arquitectónicos complejos
- El análisis automático puede no detectar code smells muy específicos del dominio

### Futuras Mejoras

- **v2.1:** Soporte para Kotlin
- **v2.2:** Integración con Git para análisis de evolución de deuda técnica
- **v2.3:** Refactorings parciales automatizados con AI
- **v2.4:** Análisis de impacto en otros módulos antes de refactorizar

### Métricas de Éxito de la Herramienta

| Criterio | Objetivo | Medición |
|----------|----------|----------|
| **Reducción tiempo análisis** | -85% vs manual | Tiempo promedio por refactoring |
| **Satisfacción usuario** | 4.5+/5 | Feedback post-refactoring |
| **Reducción deuda técnica** | -70% promedio | Métricas antes/después |
| **Cobertura tests mejorada** | +50% promedio | Cobertura antes/después |

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | - | Versión inicial básica (solo análisis manual) |
| 2.0 | 2025-10-06 | ✅ Integración automática con `analizar_code_smells`<br>✅ Proceso estructurado de 5 pasos<br>✅ Priorización por ROI Score<br>✅ Formato estandarizado siguiendo `herramienta_plantilla.md`<br>✅ Métricas de mejora cuantificables<br>✅ Generación automática de tests post-refactoring |