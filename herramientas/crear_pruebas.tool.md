```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Actualizar session_state.json al finalizar"
    nunca_saltar: true
  - instruccion: "Generar tests ejecutables con patrón AAA (Arrange-Act-Assert)"
    nunca_saltar: true
  - instruccion: "Incluir casos felices, de borde y de error"
    nunca_saltar: true
  - instruccion: "Usar nomenclatura: should[Comportamiento]When[Condicion]()"
    nunca_saltar: true
  - instruccion: "Generar comentarios de tests en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Creación de Pruebas"
  comando: ">crear_pruebas"
  alias: [">crear-pruebas", ">tests"]
  version: "4.0"

roles_autorizados:
  - ARCHDEV

prerequisitos:
  archivos_requeridos:
    - descripcion: "Código fuente Java a testear"
      formato: "[Clase].java"
  archivos_opcionales:
    - "{{archivos.session_state}}"
    - "{{archivos.contexto_proyecto}}"

parametros:
  opcionales:
    - nombre: tipo_test
      tipo: string
      valores: [UNITARIO, INTEGRACION, CARGA, AMBOS]
      defecto: UNITARIO
    - nombre: framework_test
      tipo: string
      valores: [junit5, testcontainers]
      defecto: junit5
    - nombre: nivel_cobertura
      tipo: string
      valores: [BASICO, COMPLETO, EXHAUSTIVO]
      defecto: COMPLETO
    - nombre: cobertura_objetivo
      tipo: number
      rango: [0, 100]
      defecto: 80

proceso:
  paso_1:
    nombre: "Análisis Automático del Código"
    obligatorio: true
    acciones:
      - "Identificar métodos públicos que requieren pruebas"
      - "Analizar parámetros, tipos de retorno y excepciones"
      - "Detectar dependencias para mocking"
      - "Calcular complejidad del código"
    output: |
      📊 Análisis Completado:
      - Métodos a testear: [N]
      - Casos felices: [N]
      - Casos de borde: [N]
      - Casos de error: [N]
      - Dependencias a mockear: [lista]

  paso_2:
    nombre: "Generación de Scaffolding"
    obligatorio: true
    acciones:
      - "Generar clase de test con estructura completa"
      - "Configurar @ExtendWith según framework"
      - "Declarar mocks y subject under test"
      - "Crear @BeforeEach con setup común"

  paso_3:
    nombre: "Generación por Tipo de Prueba"
    obligatorio: true
    acciones_unitario:
      framework: "JUnit 5 + Mockito + AssertJ"
      estructura: "@ExtendWith(MockitoExtension.class)"
      aislamiento: "Mocks completos de dependencias"
    acciones_integracion:
      framework: "Spring Boot Test + Testcontainers"
      estructura: "@SpringBootTest + @Testcontainers"
      dependencias: "Contenedor de BD real"
    acciones_carga:
      output: "Plan de pruebas (no código)"
      herramientas: "JMeter o Gatling"

  paso_4:
    nombre: "Revisión y Ajuste"
    obligatorio: false
    acciones:
      - "Presentar código generado"
      - "Preguntar por escenarios adicionales"
      - "Ajustar según feedback"

  paso_5:
    nombre: "Entrega y Validación"
    obligatorio: true
    acciones:
      - "Crear archivo en src/test/java/..."
      - "Proporcionar checklist de verificación"
      - "Sugerir comando de ejecución"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Verificar si existe {{archivos.session_state}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas {{rutas.session_folder}} si no existe"
      - "  2. Copiar plantilla desde {{plantillas.session_state}}"
      - "  3. Inicializar con valores por defecto"
      - "Si existe:"
      - "  1. Leer estado actual"
      - "  2. Actualizar campos correspondientes"
      - "Registrar herramienta ejecutada: crear_pruebas"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Si hay HU activa, actualizar su estado"
      - "Guardar cambios en {{archivos.session_state}}"
    plantilla_referencia: "{{plantillas.session_state}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "crear_pruebas"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"
    validacion_post:
      - "Confirmar que {{archivos.session_state}} existe y es válido"
      - "Confirmar que el JSON es parseable"

salida:
  archivos_generados:
    - tipo: "test_unitario"
      ruta: "src/test/java/[paquete]/[Clase]Test.java"
    - tipo: "test_integracion"
      ruta: "src/test/java/[paquete]/[Clase]IntegrationTest.java"
      condicion: "si tipo_test=INTEGRACION o AMBOS"
  
  archivos_actualizados:
    - "{{archivos.session_state}}"
  
  mensaje_exito: |
    ✅ Tests Generados: [Clase]Test.java
    
    📊 Resumen:
    - Métodos de test: [N]
    - Cobertura estimada: [X]%
    
    🚀 Ejecutar: mvn test -Dtest=[Clase]Test

plantilla_unitario: |
  @ExtendWith(MockitoExtension.class)
  class [Clase]Test {
      
      @Mock
      private [Dependencia] [dependencia];
      
      @InjectMocks
      private [Clase] sut; // Subject Under Test
      
      @Test
      void should[Comportamiento]When[Condicion]() {
          // Arrange
          [preparación]
          
          // Act
          [ejecución]
          
          // Assert
          assertThat([resultado]).[verificación];
          verify([mock]).[interacción];
      }
  }

errores:
  codigo_invalido:
    mensaje: "❌ Código Java no válido o no compilable"
    accion: "Solicitar código corregido"
  sin_metodos_publicos:
    mensaje: "⚠️ No se detectaron métodos públicos testeables"
    accion: "Informar y sugerir revisar visibilidad"
  dependencia_no_mockeable:
    mensaje: "⚠️ Clase final no se puede mockear"
    accion: "Sugerir wrapper o spy"

siguiente:
  herramienta: "verifica_pruebas"
  comando: ">verifica_pruebas"
  descripcion: "Validar que los tests pasen correctamente"
```
