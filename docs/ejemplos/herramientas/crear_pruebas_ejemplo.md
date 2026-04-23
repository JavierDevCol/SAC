# 💡 Ejemplo de Uso: Herramienta Crear Pruebas

## Entrada

**Código a testear:**
```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private EmailService emailService;
    
    public User registerUser(UserDTO dto) {
        if (dto.getEmail() == null) {
            throw new ValidationException("Email is required");
        }
        User user = new User(dto.getEmail(), dto.getPassword());
        User saved = userRepository.save(user);
        emailService.sendWelcomeEmail(dto.getEmail());
        return saved;
    }
    
    public User findUserByEmail(String email) {
        return userRepository.findByEmail(email)
            .orElseThrow(() -> new UserNotFoundException(email));
    }
}
```

## Parámetros

- **tipo_test:** UNITARIO
- **nivel_cobertura:** COMPLETO
- **generar_automatico:** true

## Salida Esperada

**Archivo generado:** `src/test/java/com/example/service/UserServiceTest.java`

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private EmailService emailService;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void shouldRegisterUserSuccessfullyWhenDataIsValid() {
        // Arrange
        UserDTO dto = new UserDTO("john@example.com", "SecurePass123");
        User savedUser = new User(1L, dto.getEmail());
        when(userRepository.save(any(User.class))).thenReturn(savedUser);
        
        // Act
        User result = userService.registerUser(dto);
        
        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getEmail()).isEqualTo("john@example.com");
        verify(userRepository).save(any(User.class));
        verify(emailService).sendWelcomeEmail(dto.getEmail());
    }
    
    @Test
    void shouldThrowExceptionWhenEmailIsNull() {
        // Arrange
        UserDTO dto = new UserDTO(null, "password");
        
        // Act & Assert
        assertThatThrownBy(() -> userService.registerUser(dto))
            .isInstanceOf(ValidationException.class)
            .hasMessageContaining("Email is required");
        
        verifyNoInteractions(userRepository, emailService);
    }
    
    @Test
    void shouldReturnUserWhenEmailExists() {
        // Arrange
        String email = "existing@example.com";
        User expectedUser = new User(1L, email);
        when(userRepository.findByEmail(email))
            .thenReturn(Optional.of(expectedUser));
        
        // Act
        User result = userService.findUserByEmail(email);
        
        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getEmail()).isEqualTo(email);
    }
    
    @Test
    void shouldThrowExceptionWhenUserNotFound() {
        // Arrange
        String email = "nonexistent@example.com";
        when(userRepository.findByEmail(email))
            .thenReturn(Optional.empty());
        
        // Act & Assert
        assertThatThrownBy(() -> userService.findUserByEmail(email))
            .isInstanceOf(UserNotFoundException.class);
    }
}
```

## Notificación en el Chat

```
✅ Tests generados exitosamente

📁 Archivo creado: src/test/java/com/example/service/UserServiceTest.java
📊 Tests creados: 4 métodos de prueba
🎯 Cobertura estimada: 95% líneas, 87% branches

🧪 Para ejecutar los tests:
mvn test -Dtest="UserServiceTest"
```