---
nombre: "Inicializar Reglas Arquitectónicas"
comando: ">init_reglas_arquitectonicas"
alias: [">reglas", ">init_reglas", ">ra"]
version: "1.0"
---

```yaml
mandatory:
  - instruccion: "Ejecutar cuestionario PREGUNTA POR PREGUNTA, esperar respuesta antes de continuar"
  - instruccion: "Adaptar preguntas dinámicamente según stack detectado en contexto_proyecto"
  - instruccion: "NUNCA generar archivo final sin confirmación explícita del usuario (OK)"
  - instruccion: "Mostrar configuración COMPLETA antes de solicitar confirmación, NO resúmenes"
  - instruccion: "Ofrecer siempre opciones EDITAR para modificar secciones específicas"

condiciones_entrada:
  - condicion: "contexto_proyecto cargado con stack tecnológico detectado"
    si_no_cumple: "Informar: 'Necesito conocer el proyecto primero. Ejecuta >tomar_contexto'"

parametros:
  opcionales:
    - {nombre: modo, tipo: string, valores: [nuevo, editar, mostrar], defecto: nuevo}
    - {nombre: seccion, tipo: string, descripcion: "Sección específica a editar (solo en modo=editar)"}
    - {nombre: force, tipo: flag, descripcion: "Regenerar aunque exista archivo previo"}

# ============================================
# CUESTIONARIO INTERACTIVO
# ============================================
cuestionario:
  instrucciones_generales:
    - "Hacer UNA pregunta a la vez"
    - "Esperar respuesta del usuario antes de siguiente pregunta"
    - "Ofrecer opciones predefinidas cuando sea posible [A/B/C]"
    - "Permitir respuestas personalizadas con 'Otro: ...'"
    - "Mostrar valor sugerido basado en stack detectado"
    - "Si usuario responde 'default' o 'siguiente', usar valor sugerido"
  
  secciones:
    # ========== SECCIÓN 1: NOMENCLATURA ==========
    - seccion: "nomenclatura"
      titulo: "📝 Nomenclatura y Convenciones de Nombres"
      preguntas:
        - id: "nom_01"
          pregunta: "¿Convención para nombres de **CLASES/TIPOS**?"
          tipo: "seleccion"
          opciones:
            A: "PascalCase (ej: UsuarioService, PedidoController)"
            B: "snake_case (ej: usuario_service)"
            C: "Otro (especificar)"
          sugerido: "Según stack detectado"
          aplica_a: ["java", "typescript", "python", "csharp", "go", "rust", "javascript"]
        
        - id: "nom_02"
          pregunta: "¿Convención para nombres de **MÉTODOS/FUNCIONES**?"
          tipo: "seleccion"
          opciones:
            A: "camelCase (ej: obtenerUsuario, calcularTotal)"
            B: "snake_case (ej: obtener_usuario, calcular_total)"
            C: "PascalCase (ej: ObtenerUsuario)"
          sugerido: "Según stack detectado"
        
        - id: "nom_03"
          pregunta: "¿Convención para nombres de **VARIABLES**?"
          tipo: "seleccion"
          opciones:
            A: "camelCase (ej: totalPedido, nombreUsuario)"
            B: "snake_case (ej: total_pedido, nombre_usuario)"
          sugerido: "Según stack detectado"
        
        - id: "nom_04"
          pregunta: "¿Convención para **CONSTANTES**?"
          tipo: "seleccion"
          opciones:
            A: "UPPER_SNAKE_CASE (ej: MAX_REINTENTOS, API_URL)"
            B: "PascalCase (ej: MaxReintentos)"
            C: "Mantener igual que variables"
          sugerido: "A"
        
        - id: "nom_05"
          pregunta: "¿Patrón para nombres de **INTERFACES**?"
          tipo: "seleccion"
          opciones:
            A: "Sin prefijo (ej: UserRepository)"
            B: "Prefijo I (ej: IUserRepository)"
            C: "Sufijo (ej: UserRepositoryPort)"
          sugerido: "Según stack: Java=A, C#=B, Hexagonal=C"
          aplica_a: ["java", "typescript", "csharp"]
        
        - id: "nom_06"
          pregunta: "¿Patrón para nombres de **IMPLEMENTACIONES**?"
          tipo: "seleccion"
          opciones:
            A: "Sufijo Impl (ej: UserRepositoryImpl)"
            B: "Prefijo descriptivo (ej: JpaUserRepository, MongoUserRepository)"
            C: "Sin sufijo, mismo nombre en paquete diferente"
          sugerido: "B"
          aplica_a: ["java", "typescript", "csharp"]

    # ========== SECCIÓN 2: ARQUITECTURA ==========
    - seccion: "arquitectura"
      titulo: "🏗️ Arquitectura y Estructura"
      preguntas:
        - id: "arq_01"
          pregunta: "¿Estilo arquitectónico principal del proyecto?"
          tipo: "seleccion"
          opciones:
            A: "Hexagonal / Ports & Adapters"
            B: "Clean Architecture"
            C: "Layered (Capas tradicionales)"
            D: "Modular Monolith"
            E: "Microservicios"
            F: "Serverless"
            G: "MVC tradicional"
            H: "Otro (especificar)"
          sugerido: "Detectar del contexto_proyecto.md"
        
        - id: "arq_02"
          pregunta: "¿Estructura de carpetas/paquetes preferida?"
          tipo: "seleccion"
          opciones:
            A: "Por capas (domain/, application/, infrastructure/)"
            B: "Por features/módulos (users/, orders/, payments/)"
            C: "Híbrido (features con capas internas)"
          sugerido: "A para Hexagonal/Clean, B para Microservicios"
        
        - id: "arq_03"
          pregunta: "¿Regla de dependencias entre capas?"
          tipo: "seleccion"
          opciones:
            A: "Estricta: infra → app → domain (nunca al revés)"
            B: "Flexible: permitir dependencias bidireccionales controladas"
          sugerido: "A"
        
        - id: "arq_04"
          pregunta: "¿Uso de Domain-Driven Design (DDD)?"
          tipo: "seleccion"
          opciones:
            A: "DDD Completo (Aggregates, Value Objects, Domain Events)"
            B: "DDD Táctico parcial (Entities, Repositories)"
            C: "Solo patrones Repository/Service"
            D: "No usar DDD"
          sugerido: "Según complejidad del dominio"

    # ========== SECCIÓN 3: PATRONES ==========
    - seccion: "patrones"
      titulo: "🎨 Patrones de Diseño"
      preguntas:
        - id: "pat_01"
          pregunta: "¿Patrones **OBLIGATORIOS** en el proyecto? (selecciona múltiples)"
          tipo: "multiseleccion"
          opciones:
            A: "Repository (acceso a datos)"
            B: "Factory/Builder (creación de objetos)"
            C: "Strategy (algoritmos intercambiables)"
            D: "Observer/Event (notificaciones)"
            E: "Adapter (integración externa)"
            F: "Decorator (extensión de comportamiento)"
            G: "CQRS (separación lectura/escritura)"
            H: "Circuit Breaker (resiliencia)"
          sugerido: "A, B según stack"
        
        - id: "pat_02"
          pregunta: "¿Patrones **PROHIBIDOS** o a evitar?"
          tipo: "multiseleccion"
          opciones:
            A: "Singleton (estado global)"
            B: "Service Locator (anti-pattern)"
            C: "God Object (clases gigantes)"
            D: "Anemic Domain Model"
            E: "Ninguno específicamente prohibido"
          sugerido: "B, C siempre; A y D según contexto"
        
        - id: "pat_03"
          pregunta: "¿Para creación de objetos complejos?"
          tipo: "seleccion"
          opciones:
            A: "Builder pattern obligatorio"
            B: "Factory methods"
            C: "Constructores con validación"
            D: "Libre elección según caso"
          sugerido: "A para objetos con >3 parámetros"

    # ========== SECCIÓN 4: PRINCIPIOS ==========
    - seccion: "principios"
      titulo: "📐 Principios y Paradigmas"
      preguntas:
        - id: "pri_01"
          pregunta: "¿Nivel de aplicación de **SOLID**?"
          tipo: "seleccion"
          opciones:
            A: "Estricto (todos los principios obligatorios)"
            B: "Flexible (guía, no dogma)"
            C: "Solo SRP y DIP obligatorios"
          sugerido: "A"
        
        - id: "pri_02"
          pregunta: "¿Preferencia de **inmutabilidad**?"
          tipo: "seleccion"
          opciones:
            A: "Inmutabilidad por defecto (final, readonly, const)"
            B: "Inmutabilidad en dominio, mutable en infraestructura"
            C: "Sin preferencia específica"
          sugerido: "A"
        
        - id: "pri_03"
          pregunta: "¿Manejo de **valores nulos**?"
          tipo: "seleccion"
          opciones:
            A: "Prohibir null - usar Optional/Maybe/Option"
            B: "Null permitido con documentación @Nullable"
            C: "Null Object pattern"
            D: "Sin restricción específica"
          sugerido: "A"
          aplica_a: ["java", "csharp", "typescript", "rust"]
        
        - id: "pri_04"
          pregunta: "¿Paradigma predominante?"
          tipo: "seleccion"
          opciones:
            A: "OOP (Orientado a Objetos)"
            B: "Funcional"
            C: "Híbrido (OOP estructura, Funcional lógica)"
          sugerido: "C para la mayoría de stacks modernos"
        
        - id: "pri_05"
          pregunta: "¿Composición vs Herencia?"
          tipo: "seleccion"
          opciones:
            A: "Composición siempre (herencia prohibida excepto frameworks)"
            B: "Composición preferida (herencia permitida justificada)"
            C: "Sin preferencia"
          sugerido: "B"

    # ========== SECCIÓN 5: DEPENDENCIAS ==========
    - seccion: "dependencias"
      titulo: "📦 Dependencias y Librerías"
      preguntas:
        - id: "dep_01"
          pregunta: "¿Librerías **APROBADAS** para testing?"
          tipo: "texto_libre"
          placeholder: "Ej: JUnit 5, Mockito, AssertJ, Testcontainers"
          sugerido: "Según stack detectado"
        
        - id: "dep_02"
          pregunta: "¿Librerías **APROBADAS** para logging?"
          tipo: "seleccion_o_texto"
          opciones:
            A: "SLF4J + Logback (Java)"
            B: "Winston/Pino (Node.js)"
            C: "logging + structlog (Python)"
            D: "Serilog (C#)"
            E: "Otro (especificar)"
          sugerido: "Según stack"
        
        - id: "dep_03"
          pregunta: "¿Librerías **PROHIBIDAS** o a evitar?"
          tipo: "texto_libre"
          placeholder: "Ej: Lombok @Data, Apache Commons Lang (usar APIs nativas)"
          sugerido: "Dependencias obsoletas o con vulnerabilidades conocidas"
        
        - id: "dep_04"
          pregunta: "¿Política de actualización de dependencias?"
          tipo: "seleccion"
          opciones:
            A: "Siempre última versión estable"
            B: "Versiones LTS preferidas"
            C: "Actualizar solo por seguridad"
            D: "Fijar versiones específicas"
          sugerido: "B"

    # ========== SECCIÓN 6: TESTING ==========
    - seccion: "testing"
      titulo: "🧪 Testing y Calidad"
      preguntas:
        - id: "test_01"
          pregunta: "¿Metodología de testing principal?"
          tipo: "seleccion"
          opciones:
            A: "TDD estricto (test primero)"
            B: "TDD flexible (test junto al código)"
            C: "Test después de implementar"
            D: "BDD (Given-When-Then)"
          sugerido: "A o B"
        
        - id: "test_02"
          pregunta: "¿Cobertura mínima requerida?"
          tipo: "seleccion"
          opciones:
            A: "90%+ (alta)"
            B: "80%+ (estándar)"
            C: "70%+ (mínima)"
            D: "Sin mínimo obligatorio"
          sugerido: "B"
        
        - id: "test_03"
          pregunta: "¿Convención de nombres para tests?"
          tipo: "seleccion"
          opciones:
            A: "should_{resultado}_when_{condicion}"
            B: "test_{metodo}_{escenario}_{resultado}"
            C: "given_{contexto}_when_{accion}_then_{resultado}"
            D: "Descriptivo libre con @DisplayName"
          sugerido: "A o C según metodología"
        
        - id: "test_04"
          pregunta: "¿Tests de integración con?"
          tipo: "seleccion"
          opciones:
            A: "Testcontainers (contenedores reales)"
            B: "Mocks/Stubs de infraestructura"
            C: "Base de datos en memoria (H2, SQLite)"
            D: "Ambiente de testing dedicado"
          sugerido: "A para mayor fidelidad"
          aplica_a: ["java", "typescript", "python", "csharp"]

    # ========== SECCIÓN 7: DOCUMENTACIÓN ==========
    - seccion: "documentacion"
      titulo: "📚 Documentación"
      preguntas:
        - id: "doc_01"
          pregunta: "¿Documentación de código obligatoria en?"
          tipo: "multiseleccion"
          opciones:
            A: "Clases/Interfaces públicas"
            B: "Métodos públicos"
            C: "Métodos complejos (>10 líneas)"
            D: "Solo excepciones y casos especiales"
            E: "Código auto-documentado (sin comentarios)"
          sugerido: "A, B, C"
        
        - id: "doc_02"
          pregunta: "¿Decisiones arquitectónicas documentadas en?"
          tipo: "seleccion"
          opciones:
            A: "ADRs (Architecture Decision Records)"
            B: "Wiki/Confluence"
            C: "README por módulo"
            D: "Comentarios en código"
          sugerido: "A"
        
        - id: "doc_03"
          pregunta: "¿Formato de ADRs?"
          tipo: "seleccion"
          opciones:
            A: "MADR (Markdown ADR)"
            B: "Nygard (clásico)"
            C: "Y-Statement (conciso)"
            D: "Personalizado"
          sugerido: "A"
          condicion: "doc_02 = A"

    # ========== SECCIÓN 8: SEGURIDAD Y CALIDAD ==========
    - seccion: "seguridad"
      titulo: "🔒 Seguridad y Calidad de Código"
      preguntas:
        - id: "seg_01"
          pregunta: "¿Reglas de logging para datos sensibles?"
          tipo: "seleccion"
          opciones:
            A: "NUNCA loguear PII, passwords, tokens, secrets"
            B: "Permitido con enmascaramiento"
            C: "Sin restricción específica"
          sugerido: "A"
        
        - id: "seg_02"
          pregunta: "¿Validación de entradas?"
          tipo: "seleccion"
          opciones:
            A: "Obligatoria en todos los puntos de entrada"
            B: "Solo en API pública"
            C: "En capa de dominio únicamente"
          sugerido: "A"
        
        - id: "seg_03"
          pregunta: "¿Límites de tamaño de código?"
          tipo: "texto_estructurado"
          campos:
            - {campo: "max_lineas_metodo", pregunta: "Máximo líneas por método:", sugerido: "20-30"}
            - {campo: "max_lineas_clase", pregunta: "Máximo líneas por clase:", sugerido: "200-300"}
            - {campo: "max_parametros", pregunta: "Máximo parámetros por método:", sugerido: "4-5"}
        
        - id: "seg_04"
          pregunta: "¿Herramientas de análisis estático obligatorias?"
          tipo: "texto_libre"
          placeholder: "Ej: SonarQube, ESLint, Checkstyle, Pylint"
          sugerido: "Según stack detectado"

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Verificar Contexto"
    obligatorio: true
    acciones:
      - "Verificar que contexto_proyecto esté cargado (desde _base.agent.md)"
      - "Si NO hay stack detectado: informar 'Ejecuta >tomar_contexto primero'"
      - "Extraer stack tecnológico del contexto"

  - paso: "Detectar Modo de Operación"
    obligatorio: true
    acciones:
      - "Verificar si ya existen reglas_arquitectonicas"
      - "Si existe Y modo != 'force': ofrecer opciones [VER | EDITAR | REGENERAR]"
      - "Si NO existe: continuar con MODO_NUEVO"

  - paso: "Introducción al Cuestionario"
    obligatorio: true
    acciones:
      - "Mostrar mensaje introductorio:"
      - |
        📐 **CONFIGURACIÓN DE REGLAS ARQUITECTÓNICAS**
        
        Voy a hacerte una serie de preguntas para definir los estándares del proyecto.
        
        **Stack detectado:** [stack del contexto]
        **Arquitectura detectada:** [arquitectura del contexto]
        
        💡 Tips:
        - Responde con la letra de la opción (A, B, C...)
        - Escribe 'default' o 'd' para aceptar la sugerencia
        - Escribe 'saltar' o 's' para omitir una pregunta
        - Puedes escribir respuestas personalizadas
        
        ¿Comenzamos? [Sí/No]

  - paso: "Ejecutar Cuestionario por Secciones"
    obligatorio: true
    acciones:
      - "Para cada sección en cuestionario.secciones:"
      - "  1. Mostrar título de la sección"
      - "  2. Para cada pregunta en sección.preguntas:"
      - "     a. Verificar si aplica_a incluye el stack actual (si no, saltar)"
      - "     b. Mostrar pregunta con opciones"
      - "     c. Mostrar valor sugerido"
      - "     d. ESPERAR respuesta del usuario"
      - "     e. Validar y almacenar respuesta"
      - "  3. Mostrar resumen de la sección antes de continuar"
      - "  4. Ofrecer [CONTINUAR | EDITAR SECCIÓN]"

  - paso: "Compilar Configuración"
    obligatorio: true
    acciones:
      - "Consolidar todas las respuestas del cuestionario"
      - "Aplicar valores por defecto donde usuario respondió 'default' o saltó"
      - "Generar estructura completa del documento"

  - paso: "Mostrar Configuración Completa"
    obligatorio: true
    acciones:
      - "Mostrar EN EL CHAT el documento completo generado"
      - "NO mostrar resumen, mostrar TODO el contenido"
      - "Incluir todas las secciones con sus valores configurados"
      - "Solicitar confirmación:"
      - |
        ---
        📋 **REVISIÓN DE CONFIGURACIÓN**
        
        Arriba puedes ver la configuración completa que se guardará.
        
        **Opciones:**
        - **OK** → Guardar archivo y finalizar
        - **EDITAR [sección]** → Modificar una sección específica
          (ej: EDITAR nomenclatura, EDITAR patrones)
        - **EDITAR [pregunta_id]** → Modificar una respuesta específica
          (ej: EDITAR nom_01, EDITAR arq_02)
        - **REGENERAR** → Volver a empezar el cuestionario
        
        ¿Qué deseas hacer?

  - paso: "Procesar Ediciones (si aplica)"
    obligatorio: false
    condicion: "Usuario seleccionó EDITAR"
    acciones:
      - "Identificar sección o pregunta a editar"
      - "Mostrar pregunta(s) correspondiente(s)"
      - "Recopilar nueva(s) respuesta(s)"
      - "Actualizar configuración"
      - "Volver a mostrar configuración completa"
      - "Repetir hasta que usuario responda OK"

  - paso: "Generar Archivo de Reglas"
    obligatorio: true
    condicion: "Usuario confirmó con OK"
    acciones:
      - "Crear directorio {{rutas.artifacts_folder}} si no existe"
      - "Generar {{archivos.reglas_arquitectonicas}} desde {{plantillas.reglas_arquitectonicas}}"
      - "Incluir metadata: fecha, versión, aprobado_por"
      - "Aplicar pie de documento si configurado"

  - paso: "Actualizar Contexto del Proyecto"
    obligatorio: true
    condicion: "Archivo de reglas generado exitosamente"
    acciones:
      - "Abrir contexto_proyecto"
      - "Buscar sección '## Referencias' o '## Artefactos Relacionados'"
      - "Si NO existe la sección, crearla al final del documento"
      - "Agregar referencia a reglas arquitectónicas:"
      - |
        ### Reglas Arquitectónicas
        - **Archivo:** {{archivos.reglas_arquitectonicas}}
        - **Generado:** {{fecha}}
        - **Versión:** 1.0
        - **Estado:** ✅ Configurado
      - "Si ya existe referencia previa, actualizarla con nueva fecha/versión"
    nota: "Vincula el contexto con las reglas para que otros agentes sepan que están configuradas"

salida:
  archivos_generados:
    ruta: "{{archivos.reglas_arquitectonicas}}"
    plantilla: "{{plantillas.reglas_arquitectonicas}}"
  
  archivos_actualizados:
    - ruta: "Contexto del proyecto activo (desde {{archivos.workspace}})"
      cambio: "Agregada/actualizada sección de referencia a reglas arquitectónicas"
  
  mensaje_exito: |
    ✅ REGLAS ARQUITECTÓNICAS CONFIGURADAS
    
    📁 Archivo generado: {{archivos.reglas_arquitectonicas}}
    📝 Contexto actualizado: (ver workspace)
    
    📊 Configuración aplicada:
    - Nomenclatura: [resumen]
    - Arquitectura: [estilo seleccionado]
    - Patrones obligatorios: [lista]
    - Testing: [metodología] con [cobertura]%
    
    💡 Los agentes ARCHDEV, DEVOPS y REFINADOR consultarán estas reglas
       para tomar decisiones consistentes con los estándares del proyecto.
    
    Siguiente sugerido: >refinar_hu o >validar_hu

errores:
  sin_contexto: {msg: "❌ No existe contexto del proyecto", accion: "Ejecutar >tomar_contexto primero"}
  stack_no_detectado: {msg: "⚠️ Stack tecnológico no identificado", accion: "Usar configuración genérica con preguntas ampliadas"}
  respuesta_invalida: {msg: "⚠️ Respuesta no reconocida", accion: "Mostrar opciones válidas nuevamente"}

siguiente:
  - {comando: ">refinar_hu", desc: "Refinar HUs aplicando las nuevas reglas", chat_agente: "Refinador HU"}
  - {comando: ">validar_hu", desc: "Validar HUs contra reglas arquitectónicas", chat_agente: "Arquitecto Onad"}
```
