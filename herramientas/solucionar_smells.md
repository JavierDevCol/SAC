# 🛠️ Herramienta: Solucionar Code Smells

> **Versión:** 2.1  
> **Fecha de Actualización:** 4 de enero de 2026  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `solucionar_smells`  
**Comando:** `solucionar-smells [CS-ID]`  
**Rol Propietario:** ArchDev Pro

---

## 🎯 Objetivo

Ejecutar automáticamente las correcciones de code smells identificados por `analizar_code_smells`, aplicando refactorings específicos, generando código mejorado y validando los resultados mediante tests. Automatiza la implementación de patrones de diseño y principios SOLID para reducir la deuda técnica de manera eficiente y segura.

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`tomar_contexto`** | Al inicio del proceso (opcional) | Obtener contexto del proyecto para decisiones de refactoring apropiadas |
| **`crear_pruebas`** | Después de generar código refactorizado (si `generar_tests=true`) | Generar/actualizar tests para el código refactorizado |

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **`refactorizar`** | Cuando el usuario elige "Modo Automático" | Ejecutar correcciones automatizables de code smells detectados |
| **ArchDev Pro** | Para automatizar refactoring de code smells identificados | Reducir deuda técnica de manera eficiente |
| **`analizar_code_smells`** | Al finalizar análisis (sugerencia opcional) | Ofrecer solución automática de smells detectados |

---

## 📥 Entradas Requeridas (Contexto)

**Parámetro requerido:**
- `CS-ID`: Identificador del code smell a solucionar (ej. `CS001`)

**Ejemplo de uso:**
```
solucionar-smells CS001
solucionar-smells CS001 CS002 CS003
solucionar-smells --aplicar-todos
```

**Archivos requeridos:**
- `{{session_state_location}}` - Estado de sesión (contiene `ultimo_analisis_smells`)
- `{{contexto_proyecto_location}}` - Contexto del proyecto (se crea si no existe)
- `{{code_smells_reports_location}}/reporte_[archivo]_[timestamp].json` - Reporte de `analizar_code_smells`

**Fuente del reporte (en orden de prioridad):**
1. **Desde `session_state`:** Lee `ultimo_analisis_smells.ruta_reporte` si existe análisis reciente
2. **Parámetro explícito:** `solucionar-smells CS001 --reporte=ruta/al/reporte.json`
3. **Búsqueda automática:** Último reporte en `{{code_smells_reports_location}}/`

**Secundario (Opcional):**
- Tests existentes relacionados con el código a refactorizar
- Configuración de estilo de código del proyecto (checkstyle, formatter)
- Dependencias del proyecto (pom.xml o build.gradle)

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `code_smell_id` | string | CS001, CS002, etc | - | ID específico del code smell a solucionar (requerido) |
| `modo_ejecucion` | string | automatico\|interactivo\|validar_solo | interactivo | Nivel de automatización del refactoring |
| `aplicar_todos` | boolean | true\|false | false | Solucionar todos los code smells del reporte automáticamente |
| `generar_tests` | boolean | true\|false | true | Crear/actualizar tests para código refactorizado |
| `preservar_comportamiento` | boolean | true\|false | true | Garantizar que no cambie el comportamiento externo |
| `estilo_codigo` | string | google\|spring\|custom | spring | Estilo de formateo del código generado |
| `nivel_agresividad` | string | conservador\|balanceado\|agresivo | balanceado | Qué tan profundos son los refactorings aplicados |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (uso principal - automatización de refactoring)
- ✅ **Arquitecto Onad** (supervisión de cambios arquitectónicos significativos)

---

## 🔄 Proceso Paso a Paso

**Paso 0 [CRÍTICO - OBLIGATORIO]:** 
Cargar y leer `{{session_state_location}}` y `{project-root}/.cochas/CONFIG_INIT.yaml` antes de continuar.

### 1️⃣ Configuración Inicial y Selección de Modo

- **Presentar opciones de ejecución al usuario:**
  - **Modo Automático (Default):** Ejecutar correcciones con configuración estándar optimizada
  - **Modo Personalizado:** Configurar parámetros específicos según necesidades del proyecto

- **Si elige Modo Automático, aplicar configuración por defecto:**
  ```
  ⚙️ Configuración Automática de Correcciones:
  - modo_ejecucion: interactivo ✓
  - generar_tests: true ✓
  - preservar_comportamiento: true ✓
  - estilo_codigo: spring ✓
  - nivel_agresividad: balanceado ✓
  
  ✨ Iniciando corrección de code smells con configuración optimizada...
  ```

- **Si elige Modo Personalizado, mostrar configuración disponible:**
  ```
  🔧 Configuración Personalizada de Correcciones:
  
  🎯 Modo de ejecución:
  • interactivo (mostrar cambios antes de aplicar) ← por defecto
  • automatico (aplicar sin confirmación), validar_solo (solo mostrar plan)
  
  🧪 Generar tests: true ← por defecto
  🛡️ Preservar comportamiento: true ← por defecto
  
  📝 Estilo de código:
  • spring (Google Style con Spring conventions) ← por defecto
  • google (Google Java Style), custom (usar configuración del proyecto)
  
  ⚡ Nivel de agresividad:
  • balanceado (refactorings seguros y de impacto medio) ← por defecto
  • conservador (solo cambios mínimos), agresivo (cambios arquitectónicos profundos)
  ```

### 2️⃣ Análisis del Reporte y Validación

- **Procesar reporte de `analizar_code_smells`:**
  - Validar formato JSON del reporte de entrada
  - Verificar que el código fuente coincida con el analizado
  - Extraer code smell específico o lista completa según parámetros

- **Presentar plan de ejecución:**
  ```
  📋 Plan de Corrección de Code Smells
  
  📂 Archivo: UserService.java
  🔍 Code Smells a corregir: 3 seleccionados
  
  1. 🔴 GOD_OBJECT (CS001) - ROI: 9.2 - Esfuerzo: 8h
     └── Refactoring: Extract Class + Repository Pattern
  
  2. 🟡 LONG_METHOD (CS002) - ROI: 8.5 - Esfuerzo: 3h
     └── Refactoring: Extract Method + Builder Pattern
  
  3. 🟠 LONG_PARAMETER_LIST (CS003) - ROI: 6.8 - Esfuerzo: 2h
     └── Refactoring: Parameter Object + Builder
  
  ⏱️ Tiempo total estimado: 13 horas
  📈 Reducción deuda técnica esperada: 75%
  ```

### 3️⃣ Generación de Código Refactorizado

- **Para cada code smell seleccionado, ejecutar refactoring específico:**

  **GOD_OBJECT → Extract Class Pattern:**
  ```java
  // ANTES: UserService (450 líneas)
  @Service
  public class UserService {
      // 28 métodos mezclando responsabilidades
  }
  
  // DESPUÉS: Clases especializadas
  @Component
  public class UserValidator {
      public void validateEmail(String email) { /* ... */ }
      public void validatePassword(String password) { /* ... */ }
  }
  
  @Repository 
  public interface UserRepository {
      User save(User user);
      Optional<User> findByEmail(String email);
  }
  
  @Service
  public class UserNotificationService {
      public void sendWelcomeEmail(User user) { /* ... */ }
  }
  
  @Service // Refactorizado (80 líneas)
  public class UserService {
      private final UserValidator validator;
      private final UserRepository repository;
      private final UserNotificationService notificationService;
      
      // Constructor injection + métodos especializados
  }
  ```

  **LONG_METHOD → Extract Method:**
  ```java
  // ANTES: método de 58 líneas con complejidad 14
  public List<User> searchUsers(String query, String status, /*8 más*/) {
      // Lógica compleja anidada
  }
  
  // DESPUÉS: métodos especializados
  public List<User> searchUsers(UserSearchCriteria criteria) {
      validateSearchCriteria(criteria);
      return executeSearch(criteria);
  }
  
  private void validateSearchCriteria(UserSearchCriteria criteria) { /* ... */ }
  private List<User> executeSearch(UserSearchCriteria criteria) { /* ... */ }
  ```

  **LONG_PARAMETER_LIST → Parameter Object:**
  ```java
  // ANTES: 9 parámetros
  public User createUser(String email, String password, String firstName, 
                         String lastName, String phone, String address, 
                         String city, String country, Boolean isActive) { }
  
  // DESPUÉS: Parameter Object
  @Builder
  public class CreateUserRequest {
      private String email;
      private String password;
      private PersonalInfo personalInfo;
      private Address address;
      private Boolean isActive;
  }
  
  public User createUser(CreateUserRequest request) { }
  ```

### 4️⃣ Generación y Actualización de Tests

- **Analizar tests existentes:**
  - Identificar tests que se romperán por los cambios
  - Determinar qué nuevos tests se necesitan para las clases creadas

- **Generar tests actualizados (si `generar_tests=true`):**
  ```java
  // Tests para la nueva estructura
  @ExtendWith(MockitoExtension.class)
  class UserServiceTest {
      @Mock private UserValidator validator;
      @Mock private UserRepository repository;
      @Mock private UserNotificationService notificationService;
      @InjectMocks private UserService userService;
      
      @Test
      void createUser_withValidRequest_shouldCreateSuccessfully() {
          // Given
          CreateUserRequest request = CreateUserRequest.builder()
              .email("test@example.com")
              .password("password123")
              .build();
          User expectedUser = new User(request);
          
          when(repository.save(any(User.class))).thenReturn(expectedUser);
          
          // When
          User result = userService.createUser(request);
          
          // Then
          verify(validator).validateEmail("test@example.com");
          verify(repository).save(any(User.class));
          verify(notificationService).sendWelcomeEmail(expectedUser);
          assertThat(result).isEqualTo(expectedUser);
      }
  }
  
  @ExtendWith(MockitoExtension.class)
  class UserValidatorTest {
      private UserValidator validator = new UserValidator();
      
      @Test
      void validateEmail_withInvalidEmail_shouldThrowException() {
          assertThatThrownBy(() -> validator.validateEmail("invalid"))
              .isInstanceOf(InvalidEmailException.class)
              .hasMessage("Email format is invalid");
      }
  }
  ```

### 5️⃣ Validación y Verificación de Cambios

- **Ejecutar validaciones de seguridad:**
  - Verificar que no se rompan contratos públicos (API compatibility)
  - Comprobar que se mantiene el comportamiento esperado
  - Validar que se aplican correctamente los principios SOLID

- **Presentar resumen de cambios:**
  ```
  ✅ Refactoring Completado - Resumen de Cambios
  
  📊 Métricas de Mejora:
  ┌─────────────────────────────┬──────────┬───────────┬──────────────┐
  │ Métrica                     │ Antes    │ Después   │ Mejora       │
  ├─────────────────────────────┼──────────┼───────────┼──────────────┤
  │ Líneas por clase (max)      │ 450      │ 120       │ -73% 🔥🔥🔥🔥  │
  │ Complejidad ciclomática     │ 28       │ 8         │ -71% 🔥🔥🔥🔥  │
  │ Número de responsabilidades │ 4        │ 1         │ -75% 🔥🔥🔥🔥🔥 │
  │ Parámetros por método (max) │ 9        │ 2         │ -78% 🔥🔥🔥🔥  │
  │ Cobertura de tests          │ 30%      │ 87%       │ +190% 🔥🔥🔥🔥🔥│
  │ Deuda técnica (horas)       │ 8        │ 2         │ -75% 🔥🔥🔥🔥  │
  └─────────────────────────────┴──────────┴───────────┴──────────────┘
  
  📁 Archivos Modificados: 1
  📁 Archivos Creados: 6
  🧪 Tests Creados/Actualizados: 12
  
  🎯 Principios SOLID Aplicados:
  ✅ SRP: Cada clase tiene una única responsabilidad
  ✅ OCP: Interfaces permiten extensión sin modificación  
  ✅ DIP: Dependencias por abstracción, no implementaciones concretas
  
  ⚠️ Acciones Requeridas Post-Refactoring:
  • Actualizar imports en clases que usan UserService
  • Configurar beans de Spring para nuevas clases
  • Ejecutar tests de integración completos
  ```

### 6️⃣ Entrega y Documentación

- **Generar documentación de cambios:**
  - Crear archivo `REFACTORING_SUMMARY.md` con todos los cambios
  - Documentar decisiones de diseño tomadas
  - Listar acciones manuales que el usuario debe completar

- **Presentar próximos pasos:**
  ```
  🚀 Refactoring Completado Successfully
  
  📋 Próximos Pasos Recomendados:
  
  1. ✅ Inmediatos (0-15 min):
     • Revisar código generado en tu IDE
     • Ejecutar tests: `mvn test`
     • Verificar compilación: `mvn compile`
  
  2. 🔍 Validación (15-30 min):
     • Ejecutar tests de integración completos
     • Verificar funcionalidad en ambiente de desarrollo
     • Code review con el equipo
  
  3. 📝 Documentación (30-45 min):
     • Actualizar README.md del proyecto
     • Documentar nuevas clases en JavaDoc
     • Actualizar diagramas arquitectónicos si aplica
  
  ❓ ¿Deseas continuar con el siguiente code smell de la lista o necesitas ajustes en este refactoring?
  ```

---

## 🔐 Restricciones

1. **Solo modifica código identificado en el reporte** de `analizar_code_smells`
2. **Preserva comportamiento externo** - No cambia contratos públicos sin confirmación
3. **No elimina código** sin generar equivalente funcional
4. **Requiere reporte válido** de `analizar_code_smells` como entrada
5. **En modo automático**, solo aplica refactorings con >80% de automatización
6. **No modifica tests existentes** sin generar reemplazo equivalente
7. **Backup implícito** - El usuario debe tener control de versiones (Git) activo

---

## 📊 Métricas Sugeridas

Trackear en `{{session_state_location}}`:

| Métrica | Descripción |
|---------|-------------|
| smells_solucionados_total | Total de code smells corregidos |
| smells_solucionados_auto | Correcciones 100% automáticas |
| smells_solucionados_interactivo | Correcciones con intervención del usuario |
| tiempo_promedio_refactoring | Tiempo promedio por code smell |
| tests_generados | Tests creados/actualizados por refactoring |
| reduccion_deuda_tecnica | Horas de deuda técnica eliminadas |

---

## 🔄 Actualización de Session State

### 7️⃣ Registro de Eventos

**Agregar evento a `{{session_state_location}}` en `log_eventos_clave`:**

```json
{
  "timestamp": "[timestamp_actual]",
  "rol": "[rol_actual]",
  "herramienta": "solucionar_smells",
  "tipo": "smells_solucionados",
  "detalle": "Code smells corregidos: [X] total, patrones aplicados: [lista], archivos modificados: [Y]"
}
```

**Actualizar metadata:**
- Incrementar `metadata.total_artefactos_generados` (por cada archivo creado)
- Actualizar `metadata.ultima_actividad`

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/solucionar_smells_ejemplo.md`

---

## 📚 Referencias y Notas

### Integración con Otras Herramientas del Sistema

**Herramientas que consume:**
- `analizar_code_smells` - Requiere su reporte JSON como entrada principal
- `tomar_contexto` - Usa contexto del proyecto para decisiones de refactoring
- `crear_pruebas` - Puede invocarla para generar tests adicionales si es necesario

**Herramientas que la invocan:**
- `refactorizar` - Podría usar esta herramienta para automatizar implementaciones
- `define_arquitectura` - Para aplicar cambios arquitectónicos detectados

### Patrones de Refactoring Automatizables

| Code Smell | Patrón Aplicado | Nivel Automatización | Tiempo Promedio |
|------------|-----------------|---------------------|-----------------|
| **GOD_OBJECT** | Extract Class + SRP | 85% | 15-30 min |
| **LONG_METHOD** | Extract Method + Compose Method | 90% | 5-10 min |
| **LONG_PARAMETER_LIST** | Parameter Object + Builder | 95% | 3-5 min |
| **DATA_CLUMPS** | Value Object Pattern | 90% | 5-8 min |
| **MAGIC_NUMBERS** | Extract Constants | 100% | 1-2 min |
| **DUPLICATED_CODE** | Extract Method + Template Method | 75% | 10-15 min |
| **FEATURE_ENVY** | Move Method + Encapsulate Field | 70% | 10-20 min |
| **SWITCH_STATEMENTS** | Strategy Pattern + Polymorphism | 60% | 20-40 min |

### Limitaciones Conocidas

- **Refactorings complejos:** Patrones arquitectónicos avanzados requieren intervención manual
- **Contexto de negocio:** No comprende reglas de negocio específicas del dominio
- **Dependencias externas:** Puede requerir ajustes manuales en integraciones con APIs externas
- **Performance crítica:** Cambios que afecten performance requieren validación manual
- **Legacy dependencies:** Código muy acoplado puede requerir refactoring gradual

### Futuras Mejoras

**Automatización avanzada:**
- **Machine Learning:** Aprender de feedback de usuario para mejorar patrones aplicados
- **Análisis de impacto:** Detectar automáticamente efectos en otros módulos
- **Rollback inteligente:** Capacidad de deshacer refactorings si fallan las validaciones

**Integración extendida:**
- **IDE Plugins:** Integración directa con IntelliJ IDEA, VS Code, Eclipse
- **CI/CD Integration:** Ejecutión automática en pipelines con aprobación manual
- **Git Integration:** Commits automáticos con mensajes descriptivos del refactoring

### Casos de Uso Recomendados

**Desarrollo diario:**
- Refactoring rápido durante desarrollo de features
- Cleanup automático al final de sprints
- Preparación de código para code reviews

**Mantenimiento de código:**
- Reducción sistemática de deuda técnica
- Modernización gradual de código legacy
- Preparación para cambios arquitectónicos

**Onboarding y training:**
- Demostración práctica de principios SOLID
- Ejemplos automáticos de buenas prácticas
- Comparación antes/después para aprendizaje