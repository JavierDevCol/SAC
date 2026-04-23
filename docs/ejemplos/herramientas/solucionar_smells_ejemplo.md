# 📝 Ejemplo de Uso: Herramienta solucionar_smells

> **Herramienta:** `solucionar_smells`  
> **Fecha del ejemplo:** 11 de octubre de 2025  
> **Escenario:** Corrección automática de code smells en UserService después de análisis

---

## 🔍 Contexto del Ejemplo

**Situación:** Después de ejecutar `analizar_code_smells` en el UserService.java del sistema e-commerce, se detectaron 3 code smells críticos. El desarrollador decide usar `solucionar_smells` para aplicar las correcciones automáticamente en lugar del proceso manual de `refactorizar`.

**Estado previo:**
- **Análisis completado:** 3 code smells detectados con ROI alto
- **Decisión:** Aplicar correcciones automáticas para acelerar el proceso
- **Tiempo disponible:** 2 horas (vs 8 horas del proceso manual)

---

## 📥 Entrada Proporcionada

### Reporte JSON de analizar_code_smells:
```json
{
  "analisis_completado": true,
  "archivo_analizado": "UserService.java",
  "codigo_fuente_original": "...código completo de 450 líneas...",
  "timestamp": "2025-10-11T14:30:00Z",
  "code_smells_detectados": [
    {
      "id": "CS001",
      "tipo": "GOD_OBJECT",
      "severidad": "CRITICA",
      "roi_score": 9.2,
      "refactoring_sugerido": {
        "patron": "Extract Class + Repository Pattern",
        "automatizable": true,
        "nivel_complejidad": "MEDIO",
        "esfuerzo_estimado_horas": 8,
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
        ]
      }
    },
    {
      "id": "CS002", 
      "tipo": "LONG_METHOD",
      "severidad": "ALTA",
      "roi_score": 8.5,
      "refactoring_sugerido": {
        "patron": "Extract Method + Builder Pattern",
        "automatizable": true,
        "nivel_complejidad": "BAJO"
      }
    },
    {
      "id": "CS003",
      "tipo": "LONG_PARAMETER_LIST", 
      "severidad": "MEDIA",
      "roi_score": 6.8,
      "refactoring_sugerido": {
        "patron": "Parameter Object + Builder",
        "automatizable": true,
        "nivel_complejidad": "BAJO"
      }
    }
  ],
  "compatibilidad_solucionar_smells": {
    "version_requerida": "1.0+",
    "smells_automatizables": ["CS001", "CS002", "CS003"],
    "smells_manuales": [],
    "estimacion_total_automatizada": "13 horas"
  }
}
```

### Parámetros Seleccionados:
```
🔧 Configuración Personalizada de Correcciones:
- modo_ejecucion: interactivo ✓
- aplicar_todos: true ✓ (aplicar los 3 code smells)
- generar_tests: true ✓
- preservar_comportamiento: true ✓
- estilo_codigo: spring ✓
- nivel_agresividad: balanceado ✓
```

---

## 🔄 Procesamiento Paso a Paso

### Paso 1: Configuración Inicial
✅ **Modo seleccionado:** Personalizado
✅ **Code smells a procesar:** 3 (CS001, CS002, CS003)
✅ **Validación del reporte:** JSON válido, código fuente incluido

### Paso 2: Análisis y Validación
✅ **Plan generado:**
- CS001: Extract Class (8h) → UserValidator, UserRepository, UserNotificationService
- CS002: Extract Method (3h) → searchUsers() refactoring
- CS003: Parameter Object (2h) → CreateUserRequest DTO

✅ **Estimación total:** 13h → 2h automatizado (85% reducción)

### Paso 3: Generación Código Refactorizado
✅ **Aplicación de patrones:** Extract Class + Extract Method + Parameter Object

### Paso 4: Generación Tests
✅ **Tests creados:** 12 nuevos tests para estructura refactorizada

### Paso 5: Validación
✅ **Comportamiento preservado:** Contratos públicos mantenidos
✅ **Métricas mejoradas:** -73% líneas, -71% complejidad

---

## 📤 Salida Generada

### Estructura de Archivos Creados:
```
📦 Refactoring Package: 2025-10-11_14-45-23

├── 📄 REFACTORING_SUMMARY.md
├── 🔧 src/main/java/com/ecommerce/user/
│   ├── UserService.java (refactorizado - 80 líneas)
│   ├── UserValidator.java (nuevo)
│   ├── UserNotificationService.java (nuevo)
│   ├── repository/
│   │   ├── UserRepository.java (interfaz)
│   │   └── JpaUserRepository.java (implementación)
│   └── dto/
│       ├── CreateUserRequest.java (nuevo)
│       └── UserSearchCriteria.java (nuevo)
├── 🧪 src/test/java/com/ecommerce/user/
│   ├── UserServiceTest.java (actualizado)
│   ├── UserValidatorTest.java (nuevo)
│   ├── UserNotificationServiceTest.java (nuevo)
│   └── dto/
│       └── CreateUserRequestTest.java (nuevo)
└── 📊 metrics/
    ├── before_metrics.json
    ├── after_metrics.json
    └── improvement_summary.json
```

### Código Refactorizado Principal:

#### **UserService.java (DESPUÉS del refactoring)**
```java
package com.ecommerce.user;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
@RequiredArgsConstructor
public class UserService {
    
    private final UserValidator userValidator;
    private final UserRepository userRepository;
    private final UserNotificationService notificationService;
    
    public User createUser(CreateUserRequest request) {
        // ✅ SRP: Cada responsabilidad delegada a especialista
        userValidator.validateCreateUserRequest(request);
        
        User user = User.builder()
            .email(request.getEmail())
            .password(request.getPassword())
            .personalInfo(request.getPersonalInfo())
            .address(request.getAddress())
            .active(request.getIsActive() != null ? request.getIsActive() : true)
            .createdAt(LocalDateTime.now())
            .build();
        
        User savedUser = userRepository.save(user);
        notificationService.sendWelcomeEmail(savedUser);
        
        return savedUser;
    }
    
    public List<User> searchUsers(UserSearchCriteria criteria) {
        // ✅ Método simplificado con criterios encapsulados
        userValidator.validateSearchCriteria(criteria);
        return userRepository.findByCriteria(criteria);
    }
    
    // Otros métodos simplificados...
    public void updateUserAddress(Long userId, Address address) {
        userValidator.validateAddress(address);
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException(userId));
        user.updateAddress(address);
        userRepository.save(user);
    }
}
```

#### **UserValidator.java (NUEVA CLASE)**
```java
package com.ecommerce.user;

import org.springframework.stereotype.Component;
import org.springframework.util.StringUtils;

@Component
public class UserValidator {
    
    private static final String EMAIL_REGEX = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$";
    private static final int MIN_PASSWORD_LENGTH = 8;
    
    public void validateCreateUserRequest(CreateUserRequest request) {
        if (request == null) {
            throw new IllegalArgumentException("Create user request cannot be null");
        }
        
        validateEmail(request.getEmail());
        validatePassword(request.getPassword());
        
        if (request.getPersonalInfo() != null) {
            validatePersonalInfo(request.getPersonalInfo());
        }
        
        if (request.getAddress() != null) {
            validateAddress(request.getAddress());
        }
    }
    
    public void validateEmail(String email) {
        if (!StringUtils.hasText(email)) {
            throw new InvalidEmailException("Email cannot be empty");
        }
        
        if (!email.matches(EMAIL_REGEX)) {
            throw new InvalidEmailException("Invalid email format: " + email);
        }
    }
    
    public void validatePassword(String password) {
        if (!StringUtils.hasText(password)) {
            throw new InvalidPasswordException("Password cannot be empty");
        }
        
        if (password.length() < MIN_PASSWORD_LENGTH) {
            throw new InvalidPasswordException(
                "Password must be at least " + MIN_PASSWORD_LENGTH + " characters long");
        }
    }
    
    public void validateSearchCriteria(UserSearchCriteria criteria) {
        if (criteria == null) {
            throw new IllegalArgumentException("Search criteria cannot be null");
        }
        // Validaciones específicas de búsqueda
    }
    
    public void validateAddress(Address address) {
        if (address == null) {
            throw new IllegalArgumentException("Address cannot be null");
        }
        
        if (!StringUtils.hasText(address.getStreet())) {
            throw new InvalidAddressException("Street cannot be empty");
        }
        
        if (!StringUtils.hasText(address.getCity())) {
            throw new InvalidAddressException("City cannot be empty");
        }
        
        if (!StringUtils.hasText(address.getCountry())) {
            throw new InvalidAddressException("Country cannot be empty");
        }
    }
    
    private void validatePersonalInfo(PersonalInfo personalInfo) {
        if (!StringUtils.hasText(personalInfo.getFirstName())) {
            throw new IllegalArgumentException("First name cannot be empty");
        }
        
        if (!StringUtils.hasText(personalInfo.getLastName())) {
            throw new IllegalArgumentException("Last name cannot be empty");
        }
    }
}
```

#### **CreateUserRequest.java (NUEVA CLASE DTO)**
```java
package com.ecommerce.user.dto;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class CreateUserRequest {
    
    private String email;
    private String password;
    private PersonalInfo personalInfo;
    private Address address;
    private Boolean isActive;
    
    @Data
    @Builder
    public static class PersonalInfo {
        private String firstName;
        private String lastName;
        private String phone;
    }
    
    @Data
    @Builder
    public static class Address {
        private String street;
        private String city;
        private String country;
        private String postalCode;
    }
}
```

#### **UserRepository.java (NUEVA INTERFAZ)**
```java
package com.ecommerce.user.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    Optional<User> findByEmail(String email);
    
    List<User> findByCriteria(UserSearchCriteria criteria);
    
    boolean existsByEmail(String email);
    
    List<User> findByActiveTrue();
    
    List<User> findByPersonalInfo_FirstNameContainingIgnoreCase(String firstName);
}
```

#### **Tests Principales Generados:**
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock private UserValidator userValidator;
    @Mock private UserRepository userRepository;
    @Mock private UserNotificationService notificationService;
    @InjectMocks private UserService userService;
    
    @Test
    @DisplayName("Should create user successfully with valid request")
    void createUser_withValidRequest_shouldCreateSuccessfully() {
        // Given
        CreateUserRequest request = CreateUserRequest.builder()
            .email("john@example.com")
            .password("securePassword123")
            .personalInfo(CreateUserRequest.PersonalInfo.builder()
                .firstName("John")
                .lastName("Doe")
                .build())
            .build();
            
        User expectedUser = User.builder()
            .id(1L)
            .email("john@example.com")
            .build();
            
        when(userRepository.save(any(User.class))).thenReturn(expectedUser);
        
        // When
        User result = userService.createUser(request);
        
        // Then
        verify(userValidator).validateCreateUserRequest(request);
        verify(userRepository).save(any(User.class));
        verify(notificationService).sendWelcomeEmail(expectedUser);
        
        assertThat(result).isNotNull();
        assertThat(result.getEmail()).isEqualTo("john@example.com");
    }
    
    @Test
    @DisplayName("Should throw exception when request validation fails")
    void createUser_withInvalidRequest_shouldThrowException() {
        // Given
        CreateUserRequest invalidRequest = CreateUserRequest.builder().build();
        
        doThrow(new IllegalArgumentException("Invalid email"))
            .when(userValidator).validateCreateUserRequest(invalidRequest);
        
        // When & Then
        assertThatThrownBy(() -> userService.createUser(invalidRequest))
            .isInstanceOf(IllegalArgumentException.class)
            .hasMessage("Invalid email");
            
        verify(userValidator).validateCreateUserRequest(invalidRequest);
        verifyNoInteractions(userRepository);
        verifyNoInteractions(notificationService);
    }
}

@ExtendWith(MockitoExtension.class) 
class UserValidatorTest {
    
    private UserValidator validator = new UserValidator();
    
    @Test
    @DisplayName("Should validate email successfully with correct format")
    void validateEmail_withValidEmail_shouldPass() {
        assertThatNoException()
            .isThrownBy(() -> validator.validateEmail("user@example.com"));
    }
    
    @Test
    @DisplayName("Should throw exception with invalid email format")
    void validateEmail_withInvalidFormat_shouldThrowException() {
        assertThatThrownBy(() -> validator.validateEmail("invalid-email"))
            .isInstanceOf(InvalidEmailException.class)
            .hasMessage("Invalid email format: invalid-email");
    }
    
    @ParameterizedTest
    @ValueSource(strings = {"", "   ", "short"})
    @DisplayName("Should throw exception with invalid password")
    void validatePassword_withInvalidPassword_shouldThrowException(String password) {
        assertThatThrownBy(() -> validator.validatePassword(password))
            .isInstanceOf(InvalidPasswordException.class);
    }
}
```

### Resumen de Mejoras Aplicadas:

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
│ Cobertura de tests          │ 30%      │ 89%       │ +197% 🔥🔥🔥🔥🔥│
│ Deuda técnica (horas)       │ 8        │ 1.5       │ -81% 🔥🔥🔥🔥  │
└─────────────────────────────┴──────────┴───────────┴──────────────┘

📁 Archivos Modificados: 1
📁 Archivos Creados: 8
🧪 Tests Creados/Actualizados: 15

🎯 Principios SOLID Aplicados:
✅ SRP: Cada clase tiene una única responsabilidad
  - UserService: Orchestration
  - UserValidator: Validaciones
  - UserRepository: Persistencia
  - UserNotificationService: Notificaciones
  
✅ OCP: Interfaces permiten extensión sin modificación
  - UserRepository interface permite múltiples implementaciones
  
✅ DIP: Dependencias por abstracción
  - UserService depende de interfaces, no implementaciones concretas

⚠️ Acciones Requeridas Post-Refactoring:
• Actualizar imports en clases que usan UserService (automático en IDE)
• Configurar beans de Spring para nuevas clases (ya incluido @Component/@Service/@Repository)
• Ejecutar tests de integración completos
• Verificar que otras clases que heredaban de UserService funcionen correctamente
```

### Interacción Final con el Usuario:
```
🚀 Refactoring Completado Successfully en 2 horas

📋 Próximos Pasos Recomendados:

1. ✅ Inmediatos (0-15 min):
   • Revisar código generado en tu IDE ✓
   • Ejecutar tests: `mvn test` ✓ (89% cobertura)
   • Verificar compilación: `mvn compile` ✓

2. 🔍 Validación (15-30 min):
   • Ejecutar tests de integración completos
   • Verificar funcionalidad en ambiente de desarrollo
   • Code review con el equipo

3. 📝 Documentación (30-45 min):
   • Actualizar README.md del proyecto
   • Documentar nuevas clases en JavaDoc  
   • Actualizar diagramas arquitectónicos si aplica

🎉 Code Smells Resueltos: 3/3
📈 Tiempo Ahorrado: 11 horas (13h estimado manual → 2h automatizado)
💡 ROI del Refactoring: 550% (beneficio vs tiempo invertido)

❓ Opciones Disponibles:
1. 🔍 Analizar otros archivos del proyecto con analizar_code_smells
2. 📊 Generar reporte de calidad del proyecto completo  
3. ✅ Continuar con desarrollo normal

¿Qué te gustaría hacer a continuación?
```

---

## 🔄 Variaciones del Ejemplo

### Si hubiera elegido **Modo Automático:**
```
⚙️ Configuración Automática aplicada
🤖 Procesando 3 code smells automáticamente...
✅ Refactoring completado en 1.5 horas sin intervención
```

### Si **algunos code smells no fueran automatizables:**
```
⚠️ Code Smells Detectados: 5 total
✅ Automatizables: 3 (CS001, CS002, CS003)
🔧 Requieren atención manual: 2 (CS004: Complex Business Logic, CS005: Performance Critical)

Aplicando correcciones automáticas para CS001-CS003...
Para CS004-CS005 se recomienda usar herramienta 'refactorizar' para análisis detallado.
```

### Para **proyectos con tests existentes que fallan:**
```
⚠️ Tests Existentes Afectados: 8 tests fallan después del refactoring

🔧 Análisis de Tests:
- UserServiceTest: 5 tests requieren actualización (métodos movidos)
- IntegrationTest: 3 tests necesitan ajuste de mocks

✅ Tests de Migración Generados:
- Migration_UserServiceTest.java (adaptadores para tests existentes)
- Guía de actualización paso a paso incluida
```

---

## 📚 Notas Adicionales

- **Duración total del refactoring:** 2 horas (vs 8 horas manual)
- **Nivel de automatización alcanzado:** 85% del trabajo automatizado
- **Patrón de refactoring principal:** Extract Class + Single Responsibility Principle
- **Compatibilidad:** Mantiene 100% compatibilidad con API pública existente
- **Próximo análisis recomendado:** Ejecutar `analizar_code_smells` en clases relacionadas para detectar posibles mejoras adicionales