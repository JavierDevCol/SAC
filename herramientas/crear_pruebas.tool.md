---
nombre: "Creación de Pruebas"
comando: ">crear_pruebas"
alias: [">crear-pruebas", ">tests"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Generar tests ejecutables con patrón AAA (Arrange-Act-Assert)"
  - instruccion: "Incluir casos felices, de borde y de error"
  - instruccion: "Nomenclatura: should[Comportamiento]When[Condicion]()"

reglas_arquitectonicas_requeridas:
  descripcion: "Si hay reglas arquitectónicas cargadas, aplicar:"
  secciones:
    - seccion: "testing.metodologia"
      aplicar: "Usar TDD estricto/flexible según configuración"
    - seccion: "testing.cobertura_*"
      aplicar: "Respetar cobertura mínima por capa (domain, application, infrastructure)"
    - seccion: "testing.patron_nombres"
      aplicar: "Usar convención de nombres definida (should_when, given_when_then, etc.)"
    - seccion: "testing.herramienta_integracion"
      aplicar: "Usar Testcontainers/Mocks según configuración"
    - seccion: "dependencias.testing"
      aplicar: "Usar SOLO librerías aprobadas (JUnit5, Mockito, AssertJ, etc.)"
  si_no_existe: "Usar valores por defecto de la herramienta"

condiciones_entrada:
  - condicion: "Código fuente a testear"
    formato: "Clase o módulo existente"

parametros:
  opcionales:
    - {nombre: tipo_test, tipo: string, valores: [UNITARIO, INTEGRACION, CARGA, AMBOS], defecto: UNITARIO}
    - {nombre: framework_test, tipo: string, valores: [junit5, testcontainers], defecto: junit5}
    - {nombre: nivel_cobertura, tipo: string, valores: [BASICO, COMPLETO, EXHAUSTIVO], defecto: COMPLETO}
    - {nombre: cobertura_objetivo, tipo: number, rango: [0, 100], defecto: 80}

tipos_prueba:
  unitario: {framework: "JUnit5 + Mockito + AssertJ", estructura: "@ExtendWith(MockitoExtension.class)", aislamiento: "Mocks completos"}
  integracion: {framework: "Spring Boot Test + Testcontainers", estructura: "@SpringBootTest + @Testcontainers", bd: "Contenedor real"}
  carga: {herramientas: "JMeter o Gatling", output: "Plan de pruebas (no código)"}

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones:
      - "Establecer valores por defecto para parámetros opcionales no especificados: tipo_test='UNITARIO', framework_test='junit5', nivel_cobertura='COMPLETO', cobertura_objetivo=80"
      - "Mostrar resumen compacto de configuración activa:"
      - "  ⚙️ Configuración: tipo=[valor] | framework=[valor] | cobertura=[valor] | objetivo=[valor]%"
      - "  Personaliza con: >crear_pruebas --tipo_test INTEGRACION --framework_test pytest --cobertura_objetivo 90"
    nota: "Garantiza evaluación correcta de condiciones y visibilidad de la configuración activa"

  - paso: "Análisis Automático del Código"
    obligatorio: true
    acciones: ["Identificar métodos públicos testeables", "Analizar parámetros, retornos y excepciones", "Detectar dependencias para mocking", "Calcular complejidad"]
    output: "Métodos: [N] | Casos felices: [N] | Borde: [N] | Error: [N] | Mocks: [lista]"

  - paso: "Generación de Scaffolding"
    obligatorio: true
    acciones: ["Generar clase test con estructura según tipos_prueba", "Configurar @ExtendWith según framework", "Declarar @Mock y @InjectMocks (sut)", "Crear @BeforeEach con setup común"]

  - paso: "Generación de Tests por Tipo"
    obligatorio: true
    acciones: ["Aplicar configuración según tipos_prueba[tipo_test]", "Generar métodos test con patrón AAA", "Incluir verify() para interacciones con mocks"]

  - paso: "Revisión y Ajuste"
    obligatorio: false
    acciones: ["Presentar código generado", "Preguntar por escenarios adicionales", "Ajustar según feedback"]

  - paso: "Entrega y Validación"
    obligatorio: true
    acciones: ["Crear archivo en src/test/java/[paquete]/", "Proporcionar checklist de verificación", "Sugerir: mvn test -Dtest=[Clase]Test"]

plantilla_test:
  estructura: |
    @ExtendWith(MockitoExtension.class)
    class [Clase]Test {
        @Mock private [Dependencia] dep;
        @InjectMocks private [Clase] sut;
        
        @Test void should[Comportamiento]When[Condicion]() {
            // Arrange  Act  Assert + verify()
        }
    }

salida:
  archivos_generados:
    unitario: "src/test/java/[paquete]/[Clase]Test.java"
    integracion: "src/test/java/[paquete]/[Clase]IntegrationTest.java"
  mensaje_exito: |
     Tests Generados: [Clase]Test.java
     Métodos: [N] | Cobertura estimada: [X]%
     Ejecutar: mvn test -Dtest=[Clase]Test

errores:
  codigo_invalido: {msg: " Código Java no válido", accion: "Solicitar código corregido"}
  sin_metodos: {msg: " Sin métodos públicos testeables", accion: "Revisar visibilidad de métodos"}
  no_mockeable: {msg: " Clase final no mockeable", accion: "Sugerir wrapper o spy"}

siguiente:
  - {comando: ">verifica_pruebas", desc: "Validar que los tests pasen correctamente", chat_agente: "ArchDev Pro"}
```
