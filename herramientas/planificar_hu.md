# 🛠️ Herramienta: Planificar Implementación de HU

**Comando:** `planificar-hu`  
**Versión:** 1.0  
**Rol Propietario:** Arquitecto Onad

---

## 📋 Descripción

Esta herramienta actúa como un **Líder Técnico** que traduce Historias de Usuario (HUs) aprobadas arquitectónicamente en **planes de implementación paso a paso ultra-detallados**. El objetivo es generar una guía tan precisa que el **rol ArchDev Pro** (agente desarrollador) pueda ejecutarla sin ambigüedades ni improvisación.

**⚠️ IMPORTANTE - FLUJO DE TRABAJO AGÉNTICO:**
- **ONAD (Arquitecto)** ejecuta `planificar-hu` → Genera el plan de implementación
- **ArchDev Pro (Desarrollador Agéntico)** recibe el plan → Ejecuta los comandos y modificaciones
- Esta herramienta **NO ejecuta comandos directamente**, solo genera el plan
- El usuario debe **activar el rol ArchDev Pro** para que ejecute el plan
- **⚠️ ArchDev Pro DEBE preguntar ANTES de ejecutar comandos Git:**
  - `git checkout`, `git add`, `git commit`, `git push`
  - El usuario puede indicar si ya lo hizo, si quiere que se ejecute, o si lo hará manualmente
  - **Razón:** La rama puede existir, el usuario puede querer revisar código, o preferir control manual de Git

---

## 🎯 Objetivo

Generar un **Plan de Implementación Técnica** completo y ejecutable para una HU en estado **`[A] Aprobada`**, proporcionando instrucciones detalladas, ejemplos de código, comandos exactos y checklist de validación por cada fase.

---

## 📥 Entrada

**Parámetro requerido:**
- `ID-HU`: Identificador de la tarea aprobada (ej. `ARCHDEV-001`)

**Ejemplo de uso:**
```
planificar-hu ARCHDEV-001
```

---

## 🔄 Flujo de Ejecución

### **Fase 1: Solicitud y Validación de Prerequisites**

#### **1.1. Solicitud de Entrada**
- Pedir al usuario el ID de la Tarea/HU
- Si el usuario ya proporcionó el ID, omitir este paso

#### **1.2. Validar Prerequisites**

**A. Validar Estado de la HU:**
- Leer `cochas/artifacts/backlog_desarrollo.md`
- Buscar la HU con el ID especificado
- **Validación obligatoria:**
  - **SI la HU NO existe:** Mostrar error y listar IDs disponibles
  - **SI la HU NO está en estado `[A]`:** Mostrar error indicando su estado actual
  - **Solo continuar si está en estado `[A] Aprobada`**

**Mensaje de error si no está aprobada:**
```
❌ La HU [ID-HU] no está aprobada arquitectónicamente (estado actual: [X]).

💡 Debe estar en estado [A] Aprobada antes de generar el plan de implementación.
   Usa la herramienta `validar-hu` para aprobarla primero.
```

**B. Cargar Contexto del Proyecto:**
- Verificar existencia de `cochas/artifacts/contexto_proyecto.md`
- **SI NO EXISTE:**
  - Mostrar: "⚠️ El contexto del proyecto no está inicializado. Ejecutando `tomar_contexto`..."
  - Ejecutar herramienta `tomar_contexto` completa
- **SI EXISTE:**
  - Leer archivo completo y cargar en memoria:
    - Estructura de directorios del proyecto
    - Convenciones de nombres (paquetes, clases)
    - Comandos de build (Gradle/Maven)
    - Stack tecnológico (frameworks, librerías)
    - Arquitectura (capas, patrones)

**C. Leer Reglas Arquitectónicas:**
- Leer `cochas/artifacts/reglas_arquitectonicas.md`
- Cargar restricciones y patrones obligatorios para referencia durante la planificación

**D. Validar Información Completa de la HU:**
- La HU debe contener:
  - ✅ Descripción clara del objetivo
  - ✅ Criterios de Aceptación (CAs)
  - ✅ Tareas técnicas (si fueron refinadas)
  - ✅ Estimación (story points o horas)

**SI falta información crítica:**
```
⚠️ La HU [ID-HU] carece de información suficiente para generar un plan detallado.

Información faltante:
- [ ] Criterios de Aceptación
- [ ] Tareas técnicas detalladas

💡 Recomendación: Ejecuta `refinar_hu` primero para completar la información.
```

---

### **Fase 2: Generación del Plan de Implementación**

El plan se estructura en **7 secciones secuenciales** que el desarrollador debe seguir en orden.

---

#### **Sección 0: Metadata del Plan**

Genera un encabezado con información de trazabilidad:

```markdown
# 📋 Plan de Implementación: [ID-HU]

> **Historia de Usuario:** [Título de la HU]  
> **Estado:** Aprobada  
> **Estimación:** [X] Story Points / [Y] Horas  
> **Plan generado por:** Arquitecto Onad  
> **Fecha de generación:** [timestamp]  
> **Versión de contexto:** [fecha del último análisis de contexto_proyecto.md]

---

## 🎯 Objetivo de la Implementación

[Descripción breve del objetivo de la HU]

---

## 📌 Criterios de Aceptación (CAs)

[Listar los CAs de la HU para referencia rápida]

1. ✅ CA1: [descripción]
2. ✅ CA2: [descripción]
3. ✅ CA3: [descripción]

---
```

---

#### **Sección 1: Configuración de Tarea**

**Objetivo:** Preparar el entorno de trabajo antes de escribir código.

```markdown
## 1️⃣ Configuración de Tarea

### 🎯 Objetivo
Preparar el entorno de desarrollo antes de empezar a codificar.

```
# Asegurarse de tener la última versión de develop

**Si el usuario elige B, ejecutar:**
```bash
git checkout develop

```
# Crear rama siguiendo convención del proyecto

**Si el usuario elige B, ejecutar:**
```bash
git checkout -b feature/[ID-HU]-[descripcion-corta]

# Ejemplo:
git checkout -b feature/ARCHDEV-001-migrar-plantillas-flyway
```

**⚠️ Nota:** Si el proyecto usa otro patrón de nombres de ramas, ajusta según las convenciones del equipo.

#### 1.3. Verificar build inicial
```bash
# Ejecutar build limpio para verificar punto de partida
gradlew clean build

# O si es Maven:
mvn clean install
```

**✅ Validación:** El build debe pasar sin errores antes de empezar cambios.

---

### ✅ Checklist de Validación

- [ ] Rama `develop` actualizada con últimos cambios
- [ ] Rama `feature/[ID-HU]` creada correctamente
- [ ] Build inicial pasa sin errores
- [ ] IDE configurado correctamente (si aplica)

---
```

---

#### **Sección 2: Modificaciones de Dominio**

**Objetivo:** Implementar cambios en la capa de dominio (modelos, entidades, value objects).

**Generar solo si la HU requiere cambios en dominio.**

```markdown
## 2️⃣ Modificaciones de Dominio

### 🎯 Objetivo
[Describir qué se modifica en el dominio y por qué]

### 📝 Pasos

#### 2.1. Modificar Entidad [NombreEntidad]

**Archivo:** `[ruta-completa-desde-contexto]/dominio/modelo/[NombreEntidad].java`

**Cambios requeridos:**

```java
// ANTES:
@Builder
@Getter
public class [NombreEntidad] {
    private final String campoExistente;
}

// DESPUÉS:
@Builder
@Getter
public class [NombreEntidad] {
    private final String campoExistente;
    private final [Tipo] campoNuevo; // ← Nuevo campo agregado

    // Si requiere validación:
    public void validarCampoNuevo() {
        if (campoNuevo == null || campoNuevo.isEmpty()) {
            throw new [ExcepcionDominio]("Campo nuevo es obligatorio");
        }
    }
}
```

**🔍 Detalles de implementación:**
- Usar `final` para inmutabilidad (según reglas arquitectónicas)
- Agregar validaciones de negocio si aplica
- Actualizar constructor del builder si es necesario

---

#### 2.2. Actualizar Tests de la Entidad

**Archivo:** `[ruta]/dominio/modelo/[NombreEntidad]Test.java`

```java
@Test
void deberiaCrearEntidad_CuandoCampoNuevoEsValido_EntoncesNoLanzaExcepcion() {
    // Given
    [NombreEntidad] entidad = [NombreEntidad].builder()
        .campoExistente("valor")
        .campoNuevo([valorNuevo]) // ← Nuevo campo en test
        .build();

    // When & Then
    assertNotNull(entidad.getCampoNuevo());
    assertDoesNotThrow(() -> entidad.validarCampoNuevo());
}

@Test
void deberiaLanzarExcepcion_CuandoCampoNuevoEsNull_EntoncesExcepcionDominio() {
    // Given
    [NombreEntidad] entidad = [NombreEntidad].builder()
        .campoExistente("valor")
        .campoNuevo(null) // ← Caso de error
        .build();

    // When & Then
    assertThrows([ExcepcionDominio].class, () -> entidad.validarCampoNuevo());
}
```

---

### ✅ Checklist de Validación

- [ ] Campo nuevo agregado a la entidad con `final`
- [ ] Validaciones de negocio implementadas (si aplica)
- [ ] Tests unitarios de la entidad actualizados
- [ ] Tests de casos de borde (nulls, vacíos) agregados
- [ ] Todos los tests de dominio pasan (`gradlew :dominio:test`)

---
```

---

#### **Sección 3: Modificaciones de Persistencia**

**Objetivo:** Implementar cambios en base de datos (migraciones Flyway, scripts SQL).

**Generar solo si la HU requiere cambios en BD.**

```markdown
## 3️⃣ Modificaciones de Persistencia

### 🎯 Objetivo
[Describir qué se modifica en la BD y por qué]

### 📝 Pasos

#### 3.1. Crear Migración Flyway

**Ubicación:** `[ruta]/infraestructura/src/main/resources/db/migration/`

**Nombre del archivo:** `V[SIGUIENTE_VERSION]__[descripcion_snake_case].sql`

**Ejemplo:** `V005__agregar_columna_email_clientes.sql`

**Contenido del archivo:**

```sql
-- ==============================================================================
-- Descripción: [Descripción de la migración]
-- Autor: [Tu nombre]
-- Fecha: [fecha actual]
-- Ticket: [ID-HU]
-- ==============================================================================

-- 1. Agregar nueva columna
ALTER TABLE [nombre_tabla]
ADD COLUMN [nombre_columna] [tipo_dato] [NOT NULL DEFAULT 'valor'];

-- 2. Crear índice (si aplica)
CREATE INDEX idx_[nombre_tabla]_[nombre_columna]
ON [nombre_tabla]([nombre_columna]);

-- 3. Agregar comentario para documentación
COMMENT ON COLUMN [nombre_tabla].[nombre_columna] IS '[Descripción del campo]';
```

**⚠️ Restricciones importantes:**
- No modificar migraciones existentes (ya ejecutadas en producción)
- Usar versiones incrementales (verificar última versión antes de crear)
- Para cambios destructivos (DROP COLUMN), consultar con el equipo

---

#### 3.2. Actualizar Repositorio (Adaptador)

**Archivo:** `[ruta]/infraestructura/adaptador/repositorio/[NombreRepositorio]Postgres.java`

**Cambios requeridos:**

```java
@Repository
public class [NombreRepositorio]Postgres implements [NombreRepositorio] {
    
    private final JdbcTemplate jdbcTemplate;

    @Override
    public void guardar([NombreEntidad] entidad) {
        String sql = """
            INSERT INTO [nombre_tabla] (campo_existente, campo_nuevo)
            VALUES (?, ?)
            """;
        
        jdbcTemplate.update(sql,
            entidad.getCampoExistente(),
            entidad.getCampoNuevo() // ← Nuevo campo mapeado
        );
    }

    @Override
    public Optional<[NombreEntidad]> buscarPorId(Long id) {
        String sql = """
            SELECT id, campo_existente, campo_nuevo
            FROM [nombre_tabla]
            WHERE id = ?
            """;
        
        return jdbcTemplate.query(sql, this::mapear, id)
            .stream()
            .findFirst();
    }

    private [NombreEntidad] mapear(ResultSet rs, int rowNum) throws SQLException {
        return [NombreEntidad].builder()
            .id(rs.getLong("id"))
            .campoExistente(rs.getString("campo_existente"))
            .campoNuevo(rs.getString("campo_nuevo")) // ← Mapeo nuevo campo
            .build();
    }
}
```

---

#### 3.3. Crear Test de Integración con Testcontainers

**Archivo:** `[ruta]/infraestructura/adaptador/repositorio/[NombreRepositorio]PostgresIntegrationTest.java`

```java
@Testcontainers
class [NombreRepositorio]PostgresIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
        .withDatabaseName("test_db");

    private JdbcTemplate jdbcTemplate;
    private [NombreRepositorio]Postgres repositorio;

    @BeforeEach
    void setUp() {
        DataSource dataSource = DataSourceBuilder.create()
            .url(postgres.getJdbcUrl())
            .username(postgres.getUsername())
            .password(postgres.getPassword())
            .build();
        
        jdbcTemplate = new JdbcTemplate(dataSource);
        
        // Ejecutar migraciones Flyway
        Flyway flyway = Flyway.configure()
            .dataSource(dataSource)
            .locations("classpath:db/migration")
            .load();
        flyway.migrate();
        
        repositorio = new [NombreRepositorio]Postgres(jdbcTemplate);
    }

    @Test
    void deberiaGuardarYRecuperar_CuandoEntidadTieneCampoNuevo_EntoncesSePersisteCorrectamente() {
        // Given
        [NombreEntidad] entidad = [NombreEntidad].builder()
            .campoExistente("valor")
            .campoNuevo("valor_nuevo")
            .build();

        // When
        repositorio.guardar(entidad);
        Optional<[NombreEntidad]> resultado = repositorio.buscarPorId(entidad.getId());

        // Then
        assertTrue(resultado.isPresent());
        assertEquals("valor_nuevo", resultado.get().getCampoNuevo());
    }
}
```

---

### ✅ Checklist de Validación

- [ ] Migración Flyway creada con versión correcta
- [ ] SQL ejecutado manualmente en BD local sin errores
- [ ] Repositorio actualizado con mapeo del nuevo campo
- [ ] Test de integración con Testcontainers creado
- [ ] Test de integración pasa localmente
- [ ] Migración documentada (comentarios SQL)

---
```

---

#### **Sección 4: Lógica de Aplicación (Casos de Uso)**

**Objetivo:** Implementar la lógica de negocio en los casos de uso.

```markdown
## 4️⃣ Lógica de Aplicación (Casos de Uso)

### 🎯 Objetivo
[Describir qué lógica de negocio se implementa]

### 📝 Pasos

#### 4.1. Modificar/Crear Caso de Uso

**Archivo:** `[ruta]/dominio/casodeuso/[NombreCasoUso].java`

**Cambios requeridos:**

```java
public class [NombreCasoUso] {
    
    private final [NombreRepositorio] repositorio;
    private final [OtroDependencia] dependencia; // Si aplica

    public [NombreCasoUso]([NombreRepositorio] repositorio) {
        this.repositorio = repositorio;
    }

    public [TipoRetorno] ejecutar([TipoEntrada] entrada) {
        // 1. Validar entrada
        validarEntrada(entrada);

        // 2. Ejecutar lógica de negocio
        [NombreEntidad] entidad = construirEntidad(entrada);
        entidad.validarCampoNuevo(); // ← Validación de dominio

        // 3. Persistir
        repositorio.guardar(entidad);

        // 4. Retornar resultado
        return construirRespuesta(entidad);
    }

    private void validarEntrada([TipoEntrada] entrada) {
        if (entrada == null) {
            throw new IllegalArgumentException("Entrada no puede ser null");
        }
        // Más validaciones...
    }

    private [NombreEntidad] construirEntidad([TipoEntrada] entrada) {
        return [NombreEntidad].builder()
            .campoExistente(entrada.getCampoExistente())
            .campoNuevo(entrada.getCampoNuevo()) // ← Mapeo nuevo campo
            .build();
    }

    private [TipoRetorno] construirRespuesta([NombreEntidad] entidad) {
        // Lógica de construcción de respuesta
        return new [TipoRetorno](entidad.getId(), "Éxito");
    }
}
```

---

#### 4.2. Actualizar Configuración de Spring (si aplica)

**Archivo:** `[ruta]/aplicacion/configuracion/[ConfiguracionCasosDeUso].java`

```java
@Configuration
public class [ConfiguracionCasosDeUso] {

    @Bean
    public [NombreCasoUso] [nombreCasoUso]([NombreRepositorio] repositorio) {
        return new [NombreCasoUso](repositorio);
    }
}
```

---

#### 4.3. Crear Tests Unitarios del Caso de Uso

**Archivo:** `[ruta]/dominio/casodeuso/[NombreCasoUso]Test.java`

```java
class [NombreCasoUso]Test {

    private [NombreRepositorio] repositorioMock;
    private [NombreCasoUso] casoUso;

    @BeforeEach
    void setUp() {
        repositorioMock = mock([NombreRepositorio].class);
        casoUso = new [NombreCasoUso](repositorioMock);
    }

    @Test
    void deberiaEjecutarCasoUso_CuandoEntradaEsValida_EntoncesGuardaEntidad() {
        // Given
        [TipoEntrada] entrada = new [TipoEntrada]("valor", "valor_nuevo");

        // When
        [TipoRetorno] resultado = casoUso.ejecutar(entrada);

        // Then
        verify(repositorioMock, times(1)).guardar(any([NombreEntidad].class));
        assertNotNull(resultado);
    }

    @Test
    void deberiaLanzarExcepcion_CuandoEntradaEsNull_EntoncesIllegalArgumentException() {
        // When & Then
        assertThrows(IllegalArgumentException.class, () -> casoUso.ejecutar(null));
        verify(repositorioMock, never()).guardar(any());
    }

    @Test
    void deberiaLanzarExcepcion_CuandoCampoNuevoEsInvalido_EntoncesExcepcionDominio() {
        // Given
        [TipoEntrada] entrada = new [TipoEntrada]("valor", null); // Campo inválido

        // When & Then
        assertThrows([ExcepcionDominio].class, () -> casoUso.ejecutar(entrada));
    }
}
```

---

### ✅ Checklist de Validación

- [ ] Caso de uso implementado con lógica de negocio completa
- [ ] Validaciones de entrada agregadas
- [ ] Configuración de Spring actualizada (si aplica)
- [ ] Tests unitarios cubren happy path
- [ ] Tests unitarios cubren casos de error
- [ ] Tests unitarios cubren edge cases (nulls, vacíos)
- [ ] Todos los tests del caso de uso pasan

---
```

---

#### **Sección 5: Controladores/Adaptadores de Entrada**

**Objetivo:** Exponer la funcionalidad a través de APIs REST u otros mecanismos de entrada.

**Generar solo si la HU requiere exposición externa.**

```markdown
## 5️⃣ Controladores/Adaptadores de Entrada

### 🎯 Objetivo
[Describir qué endpoint o entrada se crea/modifica]

### 📝 Pasos

#### 5.1. Crear/Modificar Controlador REST

**Archivo:** `[ruta]/infraestructura/adaptador/controlador/[NombreControlador].java`

**Cambios requeridos:**

```java
@RestController
@RequestMapping("/api/v1/[recurso]")
public class [NombreControlador] {

    private final [NombreCasoUso] casoUso;

    public [NombreControlador]([NombreCasoUso] casoUso) {
        this.casoUso = casoUso;
    }

    @PostMapping
    public ResponseEntity<[TipoRespuesta]> crear(@RequestBody @Valid [TipoRequest] request) {
        // 1. Mapear request a entrada de caso de uso
        [TipoEntrada] entrada = mapearAEntrada(request);

        // 2. Ejecutar caso de uso
        [TipoRetorno] resultado = casoUso.ejecutar(entrada);

        // 3. Mapear resultado a respuesta
        [TipoRespuesta] respuesta = mapearARespuesta(resultado);

        return ResponseEntity.status(HttpStatus.CREATED).body(respuesta);
    }

    private [TipoEntrada] mapearAEntrada([TipoRequest] request) {
        return new [TipoEntrada](
            request.getCampoExistente(),
            request.getCampoNuevo()
        );
    }

    private [TipoRespuesta] mapearARespuesta([TipoRetorno] resultado) {
        return new [TipoRespuesta](resultado.getId(), resultado.getMensaje());
    }
}
```

---

#### 5.2. Crear DTOs de Request/Response

**Archivo Request:** `[ruta]/infraestructura/adaptador/controlador/dto/[NombreRequest].java`

```java
@Builder
@Getter
public class [NombreRequest] {
    @NotNull(message = "Campo existente es obligatorio")
    private String campoExistente;

    @NotNull(message = "Campo nuevo es obligatorio")
    @Email(message = "Campo nuevo debe ser un email válido")
    private String campoNuevo;
}
```

**Archivo Response:** `[ruta]/infraestructura/adaptador/controlador/dto/[NombreResponse].java`

```java
@Builder
@Getter
public class [NombreResponse] {
    private Long id;
    private String mensaje;
    private LocalDateTime timestamp;
}
```

---

#### 5.3. Crear Tests de Integración del Controlador

**Archivo:** `[ruta]/infraestructura/adaptador/controlador/[NombreControlador]IntegrationTest.java`

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class [NombreControlador]IntegrationTest {

    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    void deberiaCrearRecurso_CuandoRequestEsValido_EntoncesRetorna201() {
        // Given
        [NombreRequest] request = [NombreRequest].builder()
            .campoExistente("valor")
            .campoNuevo("valor_nuevo")
            .build();

        String url = "http://localhost:" + port + "/api/v1/[recurso]";

        // When
        ResponseEntity<[NombreResponse]> response = restTemplate.postForEntity(
            url,
            request,
            [NombreResponse].class
        );

        // Then
        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        assertNotNull(response.getBody().getId());
    }

    @Test
    void deberiaRetornar400_CuandoRequestEsInvalido_EntoncesRetornaError() {
        // Given
        [NombreRequest] request = [NombreRequest].builder()
            .campoExistente("valor")
            .campoNuevo(null) // Campo inválido
            .build();

        String url = "http://localhost:" + port + "/api/v1/[recurso]";

        // When
        ResponseEntity<String> response = restTemplate.postForEntity(
            url,
            request,
            String.class
        );

        // Then
        assertEquals(HttpStatus.BAD_REQUEST, response.getStatusCode());
    }
}
```

---

### ✅ Checklist de Validación

- [ ] Controlador creado/modificado con endpoint correcto
- [ ] DTOs de request/response implementados con validaciones
- [ ] Mapeo entre DTOs y objetos de dominio implementado
- [ ] Tests de integración del endpoint creados
- [ ] Tests de integración pasan localmente
- [ ] Validaciones de entrada funcionan correctamente (400 para requests inválidos)

---
```

---

#### **Sección 6: Pruebas (TDD/BDD)**

**Objetivo:** Consolidar todas las pruebas y asegurar cobertura completa.

```markdown
## 6️⃣ Pruebas (TDD/BDD)

### 🎯 Objetivo
Garantizar que todos los criterios de aceptación están cubiertos por tests automatizados.

### 📝 Pasos

#### 6.1. Verificar Cobertura de Tests

**Ejecutar reporte de cobertura:**

```bash
# Generar reporte de cobertura con JaCoCo
gradlew jacocoTestReport

# El reporte se genera en:
# build/reports/jacoco/test/html/index.html
```

**Verificar métricas mínimas:**
- Dominio: ≥ 80% de cobertura
- Casos de Uso: ≥ 75% de cobertura
- Adaptadores: ≥ 60% de cobertura

---

#### 6.2. Matriz de Trazabilidad CA → Tests

Crear tabla de trazabilidad entre Criterios de Aceptación y Tests:

| Criterio de Aceptación | Clase de Test | Método de Test | Estado |
|-------------------------|---------------|----------------|--------|
| CA1: [descripción] | [NombreEntidad]Test | deberiaValidar[X] | ✅ |
| CA2: [descripción] | [NombreCasoUso]Test | deberiaEjecutar[Y] | ✅ |
| CA3: [descripción] | [NombreRepositorio]IntegrationTest | deberiaGuardar[Z] | ✅ |
| CA4: [descripción] | [NombreControlador]IntegrationTest | deberiaRetornar[W] | ✅ |

**⚠️ Importante:** Todos los CAs deben estar marcados como ✅ antes de considerar la tarea completa.

---

#### 6.3. Tests End-to-End (E2E) Manuales

**Escenario de prueba manual:**

1. **Setup:** Levantar aplicación en local
   ```bash
   gradlew bootRun
   ```

2. **Test CA1:** [descripción del escenario]
   ```bash
   curl -X POST http://localhost:8080/api/v1/[recurso] \
     -H "Content-Type: application/json" \
     -d '{"campoExistente": "valor", "campoNuevo": "valor_nuevo"}'
   ```
   
   **Resultado esperado:** HTTP 201, respuesta con ID generado

3. **Test CA2:** [descripción del escenario]
   ```bash
   curl -X GET http://localhost:8080/api/v1/[recurso]/[id]
   ```
   
   **Resultado esperado:** HTTP 200, campo nuevo presente en respuesta

4. **Test CA3 (caso de error):** [descripción del escenario]
   ```bash
   curl -X POST http://localhost:8080/api/v1/[recurso] \
     -H "Content-Type: application/json" \
     -d '{"campoExistente": "valor", "campoNuevo": null}'
   ```
   
   **Resultado esperado:** HTTP 400, mensaje de error claro

---

### ✅ Checklist de Validación

- [ ] Todos los tests unitarios pasan (`gradlew test`)
- [ ] Todos los tests de integración pasan
- [ ] Cobertura de código cumple métricas mínimas
- [ ] Matriz de trazabilidad CA → Tests completada
- [ ] Tests E2E manuales ejecutados y documentados
- [ ] No hay tests ignorados (@Disabled) sin justificación

---
```

---

#### **Sección 7: Verificación Final y Entrega**

**Objetivo:** Validar que la implementación está lista para revisión y merge.

```markdown
## 7️⃣ Verificación Final y Entrega

### 🎯 Objetivo
Garantizar que la implementación cumple con todos los estándares de calidad antes de abrir el Pull Request.

### 📝 Pasos

#### 7.1. Ejecutar Build Completo

```bash
# Build limpio con todos los tests
gradlew clean build

# Verificar que el build pase sin errores ni warnings críticos
```

**✅ Validación:** El build debe pasar al 100% sin fallos.

---

#### 7.2. Ejecutar Análisis Estático (si aplica)

```bash
# SonarQube local (si está configurado)
gradlew sonarqube

# Checkstyle
gradlew checkstyleMain checkstyleTest

# PMD
**⚠️ CONFIRMACIÓN REQUERIDA ANTES DE EJECUTAR:**

**Paso 1: Revisar cambios**

Preguntar al usuario:
```
¿Quieres que muestre los cambios realizados?
A) Sí, ejecuta: git status && git diff
B) No, ya revisé los cambios
C) Prefiero revisar manualmente (pausar aquí)
```

**Si el usuario elige A, ejecutar:**
gradlew pmdMain pmdTest

**✅ Validación:** No debe haber violaciones críticas (CRITICAL o BLOCKER).
```

---

**Paso 2: Stage de archivos**

Preguntar al usuario:
```
¿Qué archivos deseas agregar al commit?
A) Todos los archivos modificados (git add .)
B) Solo archivos específicos (especificar cuáles)
C) Ya hice git add manualmente
D) Prefiero hacerlo manualmente (pausar aquí)
```

**Si el usuario elige A, ejecutar:**
```bash
git add .
```
#### 7.3. Revisar Checklist de Definition of Done (DoD)
**Si el usuario elige B, pedir lista de archivos y ejecutar:**
```bash
git add [archivos especificados por el usuario]
```

**⚠️ CONFIRMACIÓN REQUERIDA ANTES DE EJECUTAR:**

Preguntar al usuario:
```
¿Deseas hacer push de la rama al remoto?
A) Sí, ejecuta: git push origin feature/[ID-HU]
B) Ya hice git push manualmente
C) No, prefiero hacer push más tarde (pausar aquí)
D) Necesito hacer push con --force (situación especial)
```

**Si el usuario elige A, ejecutar:**
---
**Paso 3: Crear commit**

Preguntar al usuario:
**Si el usuario elige D, preguntar confirmación adicional:**
```
⚠️ ADVERTENCIA: git push --force puede sobrescribir cambios remotos.
¿Estás seguro de que deseas forzar el push?
A) Sí, ejecuta: git push origin feature/[ID-HU] --force
B) No, cancelar
```

---

```
¿Deseas que genere el mensaje de commit automáticamente?
A) Sí, genera y ejecuta git commit con mensaje convencional
B) No, yo escribiré el mensaje manualmente
C) Ya hice git commit
D) Prefiero hacerlo manualmente (pausar aquí)
```

**Si el usuario elige A, ejecutar:**
```bash
git commit -m "[tipo]: [descripción breve generada]

[Descripción detallada generada basada en la HU]
- [ ] Todos los Criterios de Aceptación cumplidos
- [ ] Tests unitarios creados y pasando
- [ ] Tests de integración creados y pasando
- [ ] Cobertura de código ≥ [porcentaje del proyecto]%
# Ejemplo generado:
- [ ] Código revisado por al menos 1 peer (pre-PR)
- [ ] Sin deuda técnica innecesaria introducida
- [ ] Documentación actualizada (JavaDoc, README si aplica)
- [ ] No hay código comentado sin justificación
- [ ] No hay TODOs sin ticket asociado
- [ ] Logs apropiados agregados (nivel INFO para eventos, ERROR para fallos)
- [ ] Validaciones de seguridad implementadas (si aplica)

---

#### 7.4. Preparar Commits

```bash
# Revisar cambios antes de commit
git status
git diff

# Stage de archivos modificados
git add [archivos]

# Commit siguiendo convención del proyecto
git commit -m "[tipo]: [descripción breve]

[Descripción detallada opcional]

Refs: [ID-HU]
"

# Ejemplo:
git commit -m "feat: agregar validación de estados OTP en estrategia generación

Implementa switch-case para manejar 7 estados posibles de generación OTP
con mensajes contextuales y finalización de flujo para casos de error.

- Nuevas plantillas: LIMITE_REENVIOS_EXCEDIDO_OTP, NUMERO_NO_ALCANZABLE_OTP
- 16 tests unitarios con cobertura completa
- Fallback a campo 'exitoso' cuando 'estado' es null

Refs: REFINADOR-001
"
```

**⚠️ Convenciones de commits:**
- `feat:` para nuevas funcionalidades
- `fix:` para corrección de bugs
- `refactor:` para refactorización sin cambio de comportamiento
- `test:` para agregar/modificar tests
- `docs:` para documentación

---

#### 7.5. Push y Pull Request

```bash
# Push de la rama al remoto
git push origin feature/[ID-HU]
```

**Crear Pull Request con:**

**Título:**
```
[ID-HU]: [Descripción breve de la HU]
```

**Descripción:**
```markdown
## 🎯 Objetivo
[Descripción del objetivo de la HU]

## 📋 Criterios de Aceptación
- [x] CA1: [descripción]
- [x] CA2: [descripción]
- [x] CA3: [descripción]

## 🔧 Cambios Realizados
- [Resumen de cambios técnicos]
- [Archivos principales modificados]

## 🧪 Pruebas
- Tests unitarios: ✅ [X] tests pasando
- Tests de integración: ✅ [Y] tests pasando
- Cobertura: [Z]%

## 📚 Documentación
- [ ] README actualizado (si aplica)
- [ ] ADR creado (si aplica)
- [ ] JavaDoc actualizado

## ✅ Checklist
- [x] Build completo pasa sin errores
- [x] Todos los tests pasan
- [x] Cobertura de código cumple métricas
- [x] Sin deuda técnica innecesaria
- [x] Code review pre-PR realizado

2. **Preguntará antes de ejecutar cada comando Git** (checkout, add, commit, push)
- Ticket: [ID-HU]
- Plan de implementación: [link si está en wiki]
```
6. Preparará el Pull Request (tras confirmar push)
---
⚠️ **IMPORTANTE:** ArchDev Pro preguntará antes de cada comando Git. Puedes:
- Indicar que ya lo hiciste manualmente
- Pedirle que lo ejecute automáticamente
- Pausar para hacerlo tú mismo y luego continuar
### ✅ Checklist Final de Validación

- [ ] Build completo pasa sin errores
- [ ] Todos los tests pasan (unitarios + integración)
- [ ] Análisis estático sin violaciones críticas
- [ ] Definition of Done cumplida al 100%
- [ ] Commits con mensajes descriptivos y referencia a HU
- [ ] Rama pusheada al remoto
- [ ] Pull Request creado con descripción completa
- [ ] Code review solicitado al equipo

---

## 🎉 ¡Implementación Completada!

Tu implementación está lista para revisión. Recuerda:
- Responder feedback del code review oportunamente
- Resolver conflictos de merge si aparecen
- Actualizar el estado de la HU en el backlog tras el merge

---
```

---

### **Fase 3: Entrega y Cierre**

#### **3.1. Generar Documento Completo**

Consolidar todas las secciones generadas en un solo documento Markdown.

**Guardar en:**
```
cochas/artifacts/planes_implementacion/plan_[ID-HU]_[timestamp].md
```

**Ejemplo:**
```
cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_143000.md
```

**⚠️ IMPORTANTE - ENLACE CON LA HU:**
El plan generado queda **automáticamente enlazado** con la HU mediante:
1. **En el backlog (`backlog_desarrollo.md`)**: Se agrega el campo `Plan de Implementación` con la ruta del archivo
2. **En el estado de sesión (`session_state.json`)**: Se actualiza el campo `plan_implementacion` en la tarea

**Esto permite que ArchDev Pro:**
- Sepa exactamente qué plan ejecutar cuando se le asigna una HU
- Cargue automáticamente el plan correcto basándose en el ID de la HU
- Valide que la HU tenga un plan antes de iniciar implementación

---

#### **3.2. Presentar Plan al Usuario**

```markdown
---
✅ **Plan de Implementación Generado: [ID-HU]**

📄 **Documento Guardado:**
`cochas/artifacts/planes_implementacion/plan_[ID-HU]_[timestamp].md`

📊 **Resumen del Plan:**
- **Secciones:** 7 (Configuración → Verificación Final)
🤖 **Siguiente Paso: Activar ArchDev Pro para Ejecutar el Plan**

El plan está listo para ser ejecutado por el agente desarrollador. Para iniciar la implementación:

```
/cochas +archdev
```

Una vez activado ArchDev Pro, el agente:
1. Cargará automáticamente el plan de implementación
2. Ejecutará todos los comandos Git (crear rama, commits)
3. Modificará los archivos de código según las especificaciones
4. Creará y ejecutará los tests
5. Realizará el build y validación final
6. Preparará el Pull Request

⚠️ **IMPORTANTE:** No ejecutes comandos manualmente. El rol ArchDev Pro se encargará de todo.
Copia el plan completo y entrégalo al desarrollador asignado. El plan contiene:
- Comandos exactos listos para copiar/pegar
A) Activar ArchDev Pro ahora para ejecutar el plan
B) Ver el plan completo antes de ejecutar
C) Planificar otra HU

¿Deseas:
A) Ver el plan completo ahora
B) Planificar otra HU
C) Ejecutar otra herramienta
D) Otra cosa
---
```

---

#### **3.3. Actualizar Backlog con Referencia al Plan**

1. **Leer `cochas/artifacts/backlog_desarrollo.md`**
2. **Buscar la HU con el ID correspondiente**
3. **Agregar campo `plan_implementacion` con la ruta del plan generado:**
   ```markdown
   - **Plan de Implementación:** `cochas/artifacts/planes_implementacion/plan_[ID-HU]_[timestamp].md`
   ```

**Ejemplo de HU actualizada en el backlog:**
```markdown
### ARCHDEV-001: Migrar plantillas faltantes
- **Estado:** [A] Aprobada
- **Plan de Implementación:** `cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md`
- **Estimación:** 3 SP / 4.5 horas
```

---

#### **3.4. Actualizar Estado de Sesión (session_state.json)**

1. **Actualizar el campo `plan_implementacion` en `tablero_tareas`:**
   ```json
   {
     "id": "ARCHDEV-001",
     "plan_implementacion": "cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md"
   }
   ```

2. Agregar evento a `log_eventos_clave`:
   ```json
   {
     "timestamp": "[timestamp_actual]",
     "rol": "Arquitecto Onad",
     "tipo": "plan_implementacion_generado",
     "detalle": "Plan de implementación para [ID-HU] generado y enlazado"
   }
   ```

3. Incrementar `metadata.total_artefactos_generados`

4. Actualizar `metadata.ultima_actividad`

---

## 📤 Salida

### Archivos Generados

1. **Plan de Implementación:**
   - `cochas/artifacts/planes_implementacion/plan_[ID-HU]_[timestamp].md`
   - Documento Markdown completo con 7 secciones detalladas

### Archivos Actualizados

1. **`cochas/session/session_state.json`**
   - Evento agregado a `log_eventos_clave`
   - Metadata actualizada

---

## 🔧 Dependencias

- **Archivos requeridos:**
  - `cochas/artifacts/contexto_proyecto.md` (se crea si no existe)
  - `cochas/artifacts/reglas_arquitectonicas.md`
  - `cochas/artifacts/backlog_desarrollo.md` (debe tener HU aprobada)
  - `cochas/session/session_state.json`

- **Herramientas relacionadas:**
  - `tomar_contexto` (si el contexto no está inicializado)
  - `validar-hu` (prerequisito: HU debe estar aprobada)

---

## 📚 Notas de Implementación

### Adaptación al Contexto del Proyecto

El plan generado debe adaptarse automáticamente a:

1. **Sistema de Build:**
   - Detectar si es Gradle o Maven desde `contexto_proyecto.md`
   - Ajustar comandos (`gradlew` vs `mvn`)

2. **Estructura de Paquetes:**
   - Leer estructura de `contexto_proyecto.md`
   - Usar rutas exactas del proyecto (ej. `co.com.bmm.dominio.modelo`)

3. **Convenciones de Nombres:**
   - Detectar patrones de nombres de clases (ej. sufijos Repository, Service)
   - Aplicar consistentemente en ejemplos

4. **Stack Tecnológico:**
   - Adaptar ejemplos según frameworks detectados (Spring Boot, JPA, etc.)
   - Incluir librerías específicas del proyecto

---

### Generación Inteligente de Ejemplos

Para cada sección:

1. **Leer la descripción de la HU** desde `backlog_desarrollo.md`
2. **Identificar entidades/conceptos** mencionados (ej. "Cliente", "OTP", "Plantilla")
3. **Generar nombres de clases** siguiendo convenciones del proyecto
4. **Crear código de ejemplo** reemplazando placeholders con nombres reales

**Ejemplo:**
- HU menciona: "Agregar campo email a Cliente"
- Genera: `Cliente.java`, `ClienteTest.java`, `RepositorioClientePostgres.java`
- Usa nombres reales, no genéricos como `[NombreEntidad]`

---

### Validación de Completitud del Plan

Antes de entregar, verificar que el plan incluye:

- ✅ Al menos 1 ejemplo de código por sección relevante
- ✅ Comandos exactos para Git, Gradle/Maven
- ✅ Checklist de validación por sección
- ✅ Matriz de trazabilidad CAs → Tests
- ✅ Tests end-to-end manuales documentados
- ✅ Definition of Done completa

---

## 🎯 Casos de Uso

### Caso 1: HU Simple (Solo Dominio)

```
Usuario: planificar-hu ARCHDEV-007

Onad:
✅ Plan generado para ARCHDEV-007

Secciones incluidas:
- 1️⃣ Configuración de Tarea
- 2️⃣ Modificaciones de Dominio
- 4️⃣ Lógica de Aplicación
- 6️⃣ Pruebas
- 7️⃣ Verificación Final

(Omitidas: Persistencia, Controladores - No requeridas por esta HU)

Documento guardado en:
cochas/artifacts/planes_implementacion/plan_ARCHDEV-007_20251021_143500.md
```

---

### Caso 2: HU Completa (Full Stack)

```
Usuario: planificar-hu REFINADOR-001

Onad:
✅ Plan generado para REFINADOR-001

🤖 Para ejecutar este plan, activa ArchDev Pro:
/cochas +archdev

¿Deseas activar ArchDev Pro ahora? (S/N)

Secciones incluidas:
- 1️⃣ Configuración de Tarea (5 pasos)
- 2️⃣ Modificaciones de Dominio (2 clases modificadas)
- 3️⃣ Modificaciones de Persistencia (1 migración Flyway)
- 4️⃣ Lógica de Aplicación (1 caso de uso modificado)
- 5️⃣ Controladores (1 endpoint modificado)
- 6️⃣ Pruebas (16 tests unitarios + 4 tests integración)
- 7️⃣ Verificación Final (DoD completo)

Archivos a modificar: 8
Tests a crear: 20
Estimación: 4.0 horas

Documento guardado en:
cochas/artifacts/planes_implementacion/plan_REFINADOR-001_20251021_144000.md
```

---

### Caso 3: HU No Aprobada (Error)

```
Usuario: planificar-hu ARCHDEV-001

Onad:
❌ La HU ARCHDEV-001 no está aprobada arquitectónicamente (estado actual: [R]).

💡 Debe estar en estado [A] Aprobada antes de generar el plan de implementación.
   Usa la herramienta `validar-hu` para aprobarla primero.

¿Deseas que ejecute `validar-hu ARCHDEV-001` ahora? (S/N)
```

---

## 🔐 Restricciones
5. **⚠️ RESTRICCIÓN CRÍTICA - SEPARACIÓN DE RESPONSABILIDADES AGÉNTICAS:**
   - **ONAD** (este rol) solo **planifica** (genera el documento del plan)
   - **ONAD NO ejecuta** comandos Git, Gradle, ni modifica archivos de código
   - **ArchDev Pro** es el único rol autorizado para **ejecutar** el plan generado
   - El usuario debe **cambiar de rol a ArchDev Pro** (`/cochas +archdev`) para iniciar la implementación
   - ArchDev Pro recibirá el plan y ejecutará automáticamente todos los pasos
5. **⚠️ RESTRICCIÓN CRÍTICA: Esta herramienta NUNCA ejecuta comandos automáticamente**
   - Solo genera documentación con instrucciones
   - Los comandos Git, Gradle, etc. son sugerencias para que el desarrollador los ejecute manualmente
   - El desarrollador humano es responsable de revisar y ejecutar cada comando
   - ONAD NO ejecutará `git checkout`, `git commit`, `gradlew build`, ni ningún otro comando del sistema

---

## 📊 Métricas Sugeridas

Trackear en `session_state.json`:
- Total de planes generados
- Tiempo promedio de generación por plan
- Cantidad de secciones promedio por plan
- HUs planificadas vs HUs implementadas (tasa de éxito)

---

**Fin de la documentación de la herramienta `planificar-hu`.**

