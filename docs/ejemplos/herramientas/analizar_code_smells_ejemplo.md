# 📝 Ejemplo de Uso: Herramienta analizar_code_smells

> **Herramienta:** `analizar_code_smells`  
> **Fecha del ejemplo:** 11 de octubre de 2025  
> **Escenario:** Análisis de code smells en una clase Service de sistema e-commerce

---

## 🔍 Contexto del Ejemplo

**Situación:** Un desarrollador está refactorizando código legacy de un sistema e-commerce. La clase `UserService` ha crecido demasiado y necesita identificar qué code smells tiene antes de proceder con el refactoring.

**Estado del código:**
- **Antigüedad:** 18 meses de desarrollo
- **Líneas de código:** ~450 líneas
- **Mantenibilidad:** Dificultades para agregar nuevas funcionalidades
- **Testing:** Cobertura actual del 30%

---

## 📥 Entrada Proporcionada

### Código a Analizar:
```java
// UserService.java - Fragmento representativo
@Service
@Transactional
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private EmailService emailService;
    
    @Autowired
    private AuditLogService auditLogService;
    
    // 28 métodos en total, mostramos algunos representativos
    
    public User createUser(String email, String password, String firstName, 
                          String lastName, String phone, String address, 
                          String city, String country, Boolean isActive) {
        
        // Validación inline (debería ser extracted)
        if (email == null || email.trim().isEmpty()) {
            throw new InvalidUserException("Email cannot be empty");
        }
        if (!email.contains("@") || !email.contains(".")) {
            throw new InvalidUserException("Invalid email format");
        }
        if (password.length() < 8) {
            throw new InvalidUserException("Password too short");
        }
        
        // Lógica de negocio mezclada con persistencia
        User existingUser = userRepository.findByEmail(email);
        if (existingUser != null) {
            throw new UserAlreadyExistsException("User already exists");
        }
        
        // God Object - demasiadas responsabilidades
        User user = new User();
        user.setEmail(email);
        user.setPassword(hashPassword(password)); // Magic number aquí
        user.setFirstName(firstName);
        user.setLastName(lastName);
        user.setPhone(phone);
        user.setAddress(address);
        user.setCity(city);
        user.setCountry(country);
        user.setActive(isActive != null ? isActive : true);
        user.setCreatedAt(new Date());
        
        User savedUser = userRepository.save(user);
        
        // Notificación inline (Feature Envy)
        emailService.sendWelcomeEmail(savedUser.getEmail(), 
                                     savedUser.getFirstName());
        
        // Logging inline
        auditLogService.logUserCreation(savedUser.getId(), 
                                       savedUser.getEmail());
        
        return savedUser;
    }
    
    private String hashPassword(String password) {
        // Magic numbers sin constantes
        return BCrypt.hashpw(password, BCrypt.gensalt(12));
    }
    
    // Long Method con alta complejidad ciclomática
    public List<User> searchUsers(String query, String status, String role, 
                                 Date createdAfter, Date createdBefore, 
                                 String city, String country, int page, int size) {
        
        // Duplicated code en múltiples métodos de búsqueda
        if (query != null && query.trim().isEmpty()) {
            query = null;
        }
        if (status != null && status.trim().isEmpty()) {
            status = null;
        }
        
        // Complejidad ciclomática alta (muchos if/else anidados)
        List<User> users = new ArrayList<>();
        if (query != null) {
            if (status != null) {
                if (role != null) {
                    if (createdAfter != null) {
                        if (createdBefore != null) {
                            // ... más anidación
                            users = userRepository.findByComplexCriteria(
                                query, status, role, createdAfter, 
                                createdBefore, city, country, page, size);
                        } else {
                            users = userRepository.findByOtherCriteria(
                                query, status, role, createdAfter, 
                                city, country, page, size);
                        }
                    }
                }
            }
        } else {
            // Más código duplicado...
        }
        
        return users;
    }
    
    // Data Clumps - mismo conjunto de parámetros en múltiples métodos
    public void updateUserAddress(Long userId, String address, 
                                 String city, String country) {
        // ...implementación
    }
    
    public void validateUserAddress(String address, String city, String country) {
        // ...implementación
    }
    
    // 20+ métodos más con patrones similares...
}
```

### Parámetros Seleccionados:
```
🔧 Configuración Personalizada del Análisis:
- tipo_proyecto: spring-boot ✓
- version_java: 17 ✓
- nivel_analisis: exhaustivo ✓
- patrones_arquitectonicos: [] (detectar automáticamente) ✓
```

---

## 🔄 Procesamiento Paso a Paso

### Paso 1: Configuración Inicial
✅ **Modo seleccionado:** Personalizado
✅ **Configuración aplicada:** Spring Boot, Java 17, análisis exhaustivo

### Paso 2: Parsing y Análisis AST
✅ **Métricas extraídas:**
- Clases analizadas: 1 (UserService)
- Métodos totales: 28
- Líneas de código: 453
- Imports detectados: 12
- Complejidad ciclomática total: 34

### Paso 3: Detección de Code Smells
✅ **Code smells identificados:** 8 tipos diferentes
- God Object: 1 instancia (clase principal)
- Long Method: 3 métodos
- Long Parameter List: 4 métodos  
- Magic Numbers: 2 instancias
- Duplicated Code: 3 bloques
- Data Clumps: 1 conjunto de parámetros
- Feature Envy: 2 casos

### Paso 4: Análisis SOLID
✅ **Principios violados:**
- SRP: Múltiples responsabilidades (validación + persistencia + notificación)
- OCP: Lógica de búsqueda con múltiples if/else
- DIP: Dependencia directa de servicios concretos

### Paso 5: Cálculo ROI
✅ **Priorización calculada:** Ordenados por impacto vs esfuerzo

---

## 📤 Salida Generada

### Análisis Completo JSON:
```json
{
  "analisis_completado": true,
  "archivo_analizado": "UserService.java",
  "timestamp": "2025-10-11T14:30:00Z",
  "metricas_generales": {
    "lineas_codigo": 453,
    "complejidad_ciclomatica": 34,
    "nivel_mantenibilidad": "BAJO",
    "deuda_tecnica_estimada_horas": 12,
    "numero_metodos": 28,
    "profundidad_maxima_anidacion": 6
  },
  "code_smells_detectados": [
    {
      "id": "CS001",
      "tipo": "GOD_OBJECT",
      "severidad": "CRITICA",
      "linea_inicio": 1,
      "linea_fin": 453,
      "descripcion": "La clase UserService tiene múltiples responsabilidades: validación, persistencia, notificación, logging y búsqueda",
      "impacto": {
        "mantenibilidad": "CRITICO",
        "testabilidad": "ALTO",
        "escalabilidad": "ALTO",
        "legibilidad": "ALTO"
      },
      "principios_violados": ["SRP", "OCP"],
      "metrica_soporte": "453 líneas, 28 métodos, complejidad = 34",
      "refactoring_sugerido": {
        "patron": "Extract Class + Strategy Pattern",
        "esfuerzo_estimado_horas": 8,
        "prioridad": 1,
        "roi_score": 9.2,
        "pasos": [
          "Extraer validación a UserValidator",
          "Extraer persistencia a UserRepository (ya existe pero mejorar)",
          "Extraer notificaciones a UserNotificationService",
          "Crear UserSearchService para lógica de búsqueda",
          "Aplicar Command Pattern para operaciones de usuario"
        ]
      }
    },
    {
      "id": "CS002",
      "tipo": "LONG_METHOD",
      "severidad": "ALTA",
      "linea_inicio": 85,
      "linea_fin": 142,
      "descripcion": "Método searchUsers con 58 líneas y complejidad ciclomática de 14",
      "impacto": {
        "mantenibilidad": "ALTO",
        "testabilidad": "CRITICO",
        "escalabilidad": "MEDIO",
        "legibilidad": "ALTO"
      },
      "principios_violados": ["SRP", "OCP"],
      "metrica_soporte": "58 líneas, complejidad = 14, anidación = 6",
      "refactoring_sugerido": {
        "patron": "Extract Method + Builder Pattern",
        "esfuerzo_estimado_horas": 3,
        "prioridad": 2,
        "roi_score": 8.5,
        "pasos": [
          "Crear UserSearchCriteria como Builder",
          "Extraer validación de parámetros a método separado",
          "Usar Specification Pattern para criterios dinámicos",
          "Simplificar lógica condicional"
        ]
      }
    },
    {
      "id": "CS003",
      "tipo": "LONG_PARAMETER_LIST",
      "severidad": "MEDIA",
      "linea_inicio": 25,
      "linea_fin": 27,
      "descripcion": "Método createUser con 9 parámetros",
      "impacto": {
        "mantenibilidad": "MEDIO",
        "testabilidad": "MEDIO",
        "escalabilidad": "BAJO",
        "legibilidad": "ALTO"
      },
      "principios_violados": ["SRP"],
      "metrica_soporte": "9 parámetros (límite recomendado: 4)",
      "refactoring_sugerido": {
        "patron": "Parameter Object + Builder",
        "esfuerzo_estimado_horas": 2,
        "prioridad": 4,
        "roi_score": 6.8,
        "pasos": [
          "Crear CreateUserRequest DTO",
          "Implementar Builder pattern para el DTO",
          "Refactorizar método para usar objeto único",
          "Agregar validación en el DTO"
        ]
      }
    },
    {
      "id": "CS004",
      "tipo": "MAGIC_NUMBERS",
      "severidad": "BAJA",
      "linea_inicio": 78,
      "linea_fin": 78,
      "descripcion": "Magic number '12' en BCrypt.gensalt(12)",
      "impacto": {
        "mantenibilidad": "BAJO",
        "testabilidad": "BAJO",
        "escalabilidad": "BAJO",
        "legibilidad": "MEDIO"
      },
      "principios_violados": [],
      "metrica_soporte": "Literal numérico sin constante declarada",
      "refactoring_sugerido": {
        "patron": "Extract Constant",
        "esfuerzo_estimado_horas": 0.5,
        "prioridad": 6,
        "roi_score": 4.2,
        "pasos": [
          "Crear constante BCRYPT_SALT_ROUNDS = 12",
          "Reemplazar magic number con constante",
          "Documentar el propósito del valor"
        ]
      }
    },
    {
      "id": "CS005",
      "tipo": "DATA_CLUMPS",
      "severidad": "MEDIA",
      "linea_inicio": 165,
      "linea_fin": 175,
      "descripcion": "Parámetros address, city, country aparecen juntos en 3+ métodos",
      "impacto": {
        "mantenibilidad": "MEDIO",
        "testabilidad": "MEDIO",
        "escalabilidad": "MEDIO",
        "legibilidad": "MEDIO"
      },
      "principios_violados": ["SRP"],
      "metrica_soporte": "Grupo de 3 parámetros en 4 métodos diferentes",
      "refactoring_sugerido": {
        "patron": "Extract Class (Value Object)",
        "esfuerzo_estimado_horas": 1.5,
        "prioridad": 5,
        "roi_score": 5.8,
        "pasos": [
          "Crear clase Address como Value Object",
          "Refactorizar métodos para usar Address",
          "Agregar validación en Address",
          "Implementar equals/hashCode en Address"
        ]
      }
    }
  ],
  "patrones_detectados": [
    {
      "patron": "SERVICE_LAYER",
      "calidad": "PARCIAL",
      "observaciones": "Service layer implementado pero violando SRP. Considerar dividir en UserCommandService y UserQueryService (CQRS)."
    },
    {
      "patron": "REPOSITORY",
      "calidad": "BUENO",
      "observaciones": "Repository pattern correctamente implementado, pero podría beneficiarse de Specification pattern para búsquedas complejas."
    }
  ],
  "recomendaciones_priorizadas": [
    {
      "prioridad": 1,
      "titulo": "Refactorizar God Object aplicando SRP",
      "justificacion": "Alta deuda técnica (8h), dificulta testing (cobertura 30%) y mantenimiento",
      "impacto_estimado": "Reducción 65% complejidad, +50% cobertura tests, mantenibilidad BAJO → ALTO",
      "code_smell_ids": ["CS001"],
      "tiempo_estimado": "8 horas"
    },
    {
      "prioridad": 2,
      "titulo": "Simplificar método de búsqueda complejo",
      "justificacion": "Método crítico para performance, difícil de testear y mantener",
      "impacto_estimado": "Mejora significativa en testabilidad y legibilidad",
      "code_smell_ids": ["CS002"],
      "tiempo_estimado": "3 horas"
    },
    {
      "prioridad": 3,
      "titulo": "Refactoring de parámetros y data clumps",
      "justificacion": "Mejora general de API y mantenibilidad",
      "impacto_estimado": "API más limpia, menos propenso a errores",
      "code_smell_ids": ["CS003", "CS005"],
      "tiempo_estimado": "3.5 horas"
    }
  ],
  "metricas_objetivo_post_refactoring": {
    "lineas_codigo_max_clase": 150,
    "complejidad_ciclomatica_max": 12,
    "nivel_mantenibilidad_objetivo": "ALTO",
    "cobertura_tests_objetivo": 85,
    "tiempo_refactoring_total": "12 horas"
  }
}
```

### Interacción con el Usuario:
```
🔍 Análisis de Code Smells Completado - UserService.java

📊 **Resumen del Análisis:**
- ⚠️ Nivel de mantenibilidad: BAJO
- 🔴 Code smells críticos: 1 (God Object)
- 🟡 Code smells de prioridad alta: 1 (Long Method)
- 📈 Deuda técnica estimada: 12 horas de refactoring
- 🎯 ROI más alto: Refactorizar God Object (ROI: 9.2)

🚨 **Problemas Críticos Identificados:**
1. **God Object:** Clase con 453 líneas y múltiples responsabilidades
2. **Long Method:** searchUsers() con complejidad ciclomática de 14
3. **Violaciones SOLID:** SRP y OCP principalmente afectados

💡 **Recomendación Principal:**
Comenzar por dividir UserService en clases especializadas:
- UserValidator (validaciones)
- UserCommandService (operaciones CRUD)
- UserQueryService (búsquedas)
- UserNotificationService (notificaciones)

📈 **Impacto Esperado del Refactoring:**
- Reducción de complejidad: 65%
- Mejora en cobertura de tests: 30% → 85%
- Tiempo de desarrollo de nuevas features: -40%

¿Deseas proceder con el refactoring del God Object (8h estimadas)?
```

---

## 🔄 Variaciones del Ejemplo

### Si hubiera elegido **Nivel de Análisis Básico:**
```json
{
  "analisis_completado": true,
  "nivel_analisis": "basico",
  "metricas_generales": {
    "lineas_codigo": 453,
    "complejidad_ciclomatica": 34,
    "nivel_mantenibilidad": "BAJO"
  },
  "code_smells_principales": [
    "GOD_OBJECT (crítico)",
    "LONG_METHOD (alto)",
    "LONG_PARAMETER_LIST (medio)"
  ],
  "recomendacion_principal": "Refactorizar God Object - ROI Score: 9.2"
}
```

### Si el código **no tuviera Code Smells:**
```
✅ Análisis Completado - Código Limpio Detectado

📊 **Resultados:**
- Mantenibilidad: ALTO
- Complejidad: Dentro de límites aceptables
- Principios SOLID: Respetados
- Line Coverage objetivo: Alcanzable

💚 **El código cumple con estándares de calidad**
No se detectaron code smells significativos que requieran refactoring inmediato.
```

### Para **Proyectos Legacy Grandes:**
```
⚠️ **Archivo Grande Detectado** (2,400 líneas)

🔍 **Análisis Optimizado Aplicado:**
- Enfoque en hot spots críticos
- Priorización automática por ROI
- Recomendación: Dividir archivo antes de refactoring detallado

📊 **Code Smells de Alta Prioridad Detectados:** 15
Tiempo estimado análisis completo: 45 minutos
```

---

## 📚 Notas Adicionales

- **Duración del análisis:** 2 minutos (código de tamaño medio, análisis exhaustivo)
- **Code smells detectados:** 8 tipos diferentes con 15 instancias totales
- **Priorización:** Basada en algoritmo ROI (impacto vs esfuerzo)
- **Integración:** El resultado JSON se pasa automáticamente a la herramienta `refactorizar` si el usuario aprueba continuar
- **Precisión:** ~90% en detección de code smells comunes según benchmarks internos