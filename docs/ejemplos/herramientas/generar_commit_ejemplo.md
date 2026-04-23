# 📝 Ejemplo de Uso: Herramienta generar_commit

> **Herramienta:** `generar_commit`  
> **Fecha del ejemplo:** 10 de octubre de 2025  
> **Escenario:** Implementación de autenticación JWT en una API Spring Boot

---

## 🔍 Contexto del Ejemplo

**Situación:** Un desarrollador ha implementado un sistema de autenticación JWT y necesita documentar los cambios realizados con un commit claro y estandarizado.

**Estado del repositorio:**
- Branch actual: `feature/user-authentication`
- Issue relacionado: `#AUTH-123 - Implementar autenticación con JWT`
- Archivos modificados: 3 archivos principales

---

## 📥 Entrada Proporcionada

### Git Diff Output:
```bash
diff --git a/src/main/java/com/ecommerce/service/UserService.java b/src/main/java/com/ecommerce/service/UserService.java
index 1234567..abcdefg 100644
--- a/src/main/java/com/ecommerce/service/UserService.java
+++ b/src/main/java/com/ecommerce/service/UserService.java
@@ -15,6 +15,18 @@ public class UserService {
     }
 
+    public User authenticateUser(String email, String password) {
+        validateCredentials(email, password);
+        User user = userRepository.findByEmail(email);
+        if (user != null && passwordEncoder.matches(password, user.getHashedPassword())) {
+            user.setLastLoginDate(LocalDateTime.now());
+            return userRepository.save(user);
+        }
+        throw new AuthenticationException("Invalid credentials");
+    }
+
     private void validateEmail(String email) {

diff --git a/src/main/java/com/ecommerce/config/SecurityConfig.java b/src/main/java/com/ecommerce/config/SecurityConfig.java
new file mode 100644
index 0000000..xyz9876
--- /dev/null
+++ b/src/main/java/com/ecommerce/config/SecurityConfig.java
@@ -0,0 +1,25 @@
+@Configuration
+@EnableWebSecurity
+public class SecurityConfig {
+    
+    @Bean
+    public JwtAuthenticationFilter jwtAuthenticationFilter() {
+        return new JwtAuthenticationFilter();
+    }
+    
+    @Bean
+    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
+        return http
+            .csrf().disable()
+            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
+            .and()
+            .authorizeHttpRequests(auth -> auth
+                .requestMatchers("/api/auth/**").permitAll()
+                .anyRequest().authenticated()
+            )
+            .addFilterBefore(jwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class)
+            .build();
+    }
+}

diff --git a/pom.xml b/pom.xml
index abc123..def456 100644
--- a/pom.xml
+++ b/pom.xml
@@ -45,6 +45,12 @@
         <artifactId>spring-boot-starter-validation</artifactId>
     </dependency>
+    <dependency>
+        <groupId>io.jsonwebtoken</groupId>
+        <artifactId>jjwt-api</artifactId>
+        <version>0.11.5</version>
+    </dependency>
 </dependencies>
```

### Contexto Adicional:
- **Branch name:** `feature/user-authentication`
- **Issue/Ticket:** `#AUTH-123`
- **Archivos afectados:** UserService.java, SecurityConfig.java (nuevo), pom.xml

---

## ⚙️ Configuración Seleccionada

**Paso 1: Selección de Modo**
- **Modo elegido:** Configuración Manual

**Parámetros configurados:**
```
📝 Tipo de Commit: auto (detectar automáticamente)
📄 Incluir cuerpo detallado: true
🎯 Formato del alcance: auto (inferir del contexto)
⚠️ Breaking change: false
📏 Límite de caracteres del título: 50
```

---

## 🔄 Procesamiento Paso a Paso

### Paso 2: Análisis del Contexto
- **Archivos detectados:** 3 archivos (service, config, dependency)
- **Branch pattern:** `feature/` → sugiere nueva funcionalidad
- **Cambios críticos:** Nuevo archivo de configuración + dependencia JWT
- **Alcance inferido:** Autenticación/Security

### Paso 3: Clasificación del Tipo
- **Detección automática:** `feat` (nueva funcionalidad)
- **Justificación:** Nuevos métodos públicos + nueva configuración + nueva dependencia

### Paso 4: Determinación del Alcance
- **Estrategia:** auto
- **Análisis:** Archivos relacionados con autenticación y seguridad
- **Alcance generado:** `auth` (conciso y descriptivo)

### Paso 5: Construcción del Título
```
feat(auth): Implement JWT-based user authentication
```
- **Longitud:** 48 caracteres (dentro del límite de 50)
- **Formato:** Conventional Commits compliant
- **Verbo imperativo:** "Implement"

### Paso 6: Generación del Cuerpo
- **Párrafo justificativo:** Explica el porqué del cambio
- **Lista de cambios:** Detalla modificaciones específicas
- **Referencias:** Incluye issue tracking

### Paso 7: Validación
- ✅ Formato Conventional Commits válido
- ✅ Límite de caracteres respetado
- ✅ Referencias incluidas

---

## 📤 Salida Generada

### Mensaje de Commit Completo:
```bash
feat(auth): Implement JWT-based user authentication

Add comprehensive JWT authentication system to improve API security
and enable stateless session management across the platform.

- Add authenticateUser method with credential validation
- Create SecurityConfig with JWT filter configuration  
- Integrate password encoding verification in UserService
- Configure stateless session policy for REST API
- Add JWT dependency to project dependencies
- Update last login timestamp on successful authentication
- Add authentication exception handling for invalid credentials

Refs: #AUTH-123
```

### Comando Sugerido:
```bash
git commit -m "feat(auth): Implement JWT-based user authentication

Add comprehensive JWT authentication system to improve API security
and enable stateless session management across the platform.

- Add authenticateUser method with credential validation
- Create SecurityConfig with JWT filter configuration  
- Integrate password encoding verification in UserService
- Configure stateless session policy for REST API
- Add JWT dependency to project dependencies
- Update last login timestamp on successful authentication
- Add authentication exception handling for invalid credentials

Refs: #AUTH-123"
```

---

## ✅ Resultado Final

**Configuración aplicada:**
- ✅ Tipo detectado: `feat` (nueva funcionalidad)
- ✅ Alcance inferido: `auth` (autenticación)
- ✅ Cuerpo detallado incluido
- ✅ Referencias agregadas: `#AUTH-123`
- ✅ Longitud del título: 48 caracteres

**Beneficios del commit generado:**
- 📋 **Trazabilidad:** Vinculado al issue original
- 🎯 **Claridad:** Explica tanto el qué como el porqué
- 📊 **Detalle técnico:** Lista cambios específicos realizados
- 🔍 **Búsqueda:** Fácil de encontrar en el historial con `git log --grep="auth"`
- 📈 **Métricas:** Compatible con herramientas de análisis de commits

---

## 🔄 Variaciones del Ejemplo

### Si se hubiera elegido **Modo Automático:**
```bash
feat(auth): Add JWT authentication system

Refs: #AUTH-123
```
*(Título únicamente, sin cuerpo detallado)*

### Si se hubiera detectado **Breaking Change:**
```bash
feat(auth): Implement JWT-based user authentication

BREAKING CHANGE: Authentication endpoint now requires JWT tokens
```

### Si hubiera **múltiples módulos afectados:**
```bash
feat(multi): Implement JWT authentication across services
```

---

## 📚 Notas Adicionales

- **Tiempo estimado de generación:** < 5 segundos
- **Precisión de detección automática:** Alta (basada en patrones claros)
- **Casos de uso similares:** Features de autenticación, autorización, seguridad
- **Herramientas complementarias:** Se integra bien con `refactorizar` y `crear_pruebas`