---
nombre: "Creación de Pruebas"
comando: ">crear_pruebas"
alias: [">crear-pruebas", ">tests"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Pasos obligatorios NO se pueden omitir"
  - instruccion: "Generar tests ejecutables con patrón AAA (Arrange-Act-Assert)"
  - instruccion: "Incluir casos felices, de borde y de error"
  - instruccion: "Nomenclatura: should[Comportamiento]When[Condicion]()"
  - instruccion: "Comentarios en idioma: {{preferencias.idioma_documentacion}}"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Código fuente Java a testear"
      formato: "[Clase].java"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"

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
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: tipo_test='UNITARIO', framework_test='junit5', nivel_cobertura='COMPLETO', cobertura_objetivo=80"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

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
