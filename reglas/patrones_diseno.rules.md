# Reglas de Referencias: Patrones de Diseño

```yaml
descripcion: "Catálogo de patrones de diseño con referencias a documentación externa"
fuente_principal: "refactoring.guru"
ultima_actualizacion: "2026-01-12"
version: "1.0"

# =============================================================================
# PATRONES CREACIONALES
# =============================================================================
creacionales:
  descripcion: "Mecanismos de creación de objetos que incrementan flexibilidad y reutilización"
  patrones:
    factory_method:
      nombre: "Factory Method"
      url: "https://refactoring.guru/es/design-patterns/factory-method"
      problema: "Crear objetos sin especificar su clase exacta"
      solucion: "Definir interfaz para crear objetos, dejando a subclases decidir qué clase instanciar"
      cuando_usar:
        - "No conoces de antemano las dependencias exactas"
        - "Quieres permitir extensión por usuarios de tu framework"
        - "Reutilizar objetos existentes en lugar de crear nuevos"
      relacionado_con: ["Abstract Factory", "Prototype"]
    
    abstract_factory:
      nombre: "Abstract Factory"
      url: "https://refactoring.guru/es/design-patterns/abstract-factory"
      problema: "Crear familias de objetos relacionados sin especificar clases concretas"
      solucion: "Interfaz para crear familias de productos relacionados"
      cuando_usar:
        - "Código debe trabajar con varias familias de productos"
        - "Garantizar consistencia entre productos relacionados"
        - "No quieres exponer clases concretas"
      relacionado_con: ["Factory Method", "Builder"]
    
    builder:
      nombre: "Builder"
      url: "https://refactoring.guru/es/design-patterns/builder"
      problema: "Construir objetos complejos paso a paso"
      solucion: "Separar construcción de representación para crear distintas representaciones"
      cuando_usar:
        - "Objeto con muchos parámetros opcionales"
        - "Crear distintas representaciones del mismo producto"
        - "Construir árboles Composite u objetos complejos"
      relacionado_con: ["Abstract Factory", "Composite"]
    
    prototype:
      nombre: "Prototype"
      url: "https://refactoring.guru/es/design-patterns/prototype"
      problema: "Clonar objetos existentes sin acoplar código a sus clases"
      solucion: "Delegar proceso de clonación a los propios objetos"
      cuando_usar:
        - "Código no debe depender de clases concretas a clonar"
        - "Reducir subclases que solo difieren en inicialización"
        - "Objetos con estado complejo que es costoso recrear"
      relacionado_con: ["Factory Method", "Memento"]
    
    singleton:
      nombre: "Singleton"
      url: "https://refactoring.guru/es/design-patterns/singleton"
      problema: "Garantizar una única instancia de una clase con punto de acceso global"
      solucion: "Constructor privado y método estático que retorna instancia única"
      cuando_usar:
        - "Una clase debe tener exactamente una instancia"
        - "Instancia debe ser accesible desde cualquier punto"
      advertencia: "⚠️ Viola SRP, dificulta testing, oculta dependencias. Considerar Dependency Injection"
      relacionado_con: ["Factory Method", "Facade"]

# =============================================================================
# PATRONES ESTRUCTURALES
# =============================================================================
estructurales:
  descripcion: "Ensamblar objetos y clases en estructuras más grandes manteniendo flexibilidad"
  patrones:
    adapter:
      nombre: "Adapter"
      url: "https://refactoring.guru/es/design-patterns/adapter"
      problema: "Permitir colaboración entre objetos con interfaces incompatibles"
      solucion: "Objeto envoltorio que traduce llamadas entre interfaces"
      cuando_usar:
        - "Usar clase existente con interfaz incompatible"
        - "Reutilizar subclases que carecen de funcionalidad común"
        - "Integrar código legacy o APIs de terceros"
      relacionado_con: ["Bridge", "Decorator", "Proxy"]
    
    bridge:
      nombre: "Bridge"
      url: "https://refactoring.guru/es/design-patterns/bridge"
      problema: "Separar abstracción de implementación para variar independientemente"
      solucion: "Dividir clase grande en dos jerarquías separadas"
      cuando_usar:
        - "Evitar enlace permanente entre abstracción e implementación"
        - "Abstracción e implementación deben ser extensibles por subclases"
        - "Cambios en implementación no deben afectar código cliente"
      relacionado_con: ["Adapter", "Abstract Factory", "Strategy"]
    
    composite:
      nombre: "Composite"
      url: "https://refactoring.guru/es/design-patterns/composite"
      problema: "Componer objetos en estructuras de árbol y trabajar uniformemente"
      solucion: "Interfaz común para objetos simples y compuestos"
      cuando_usar:
        - "Implementar estructura de árbol"
        - "Clientes deben tratar objetos simples y compuestos uniformemente"
        - "Menús, sistemas de archivos, estructuras organizacionales"
      relacionado_con: ["Builder", "Iterator", "Visitor"]
    
    decorator:
      nombre: "Decorator"
      url: "https://refactoring.guru/es/design-patterns/decorator"
      problema: "Añadir comportamientos a objetos sin modificar su clase"
      solucion: "Envolver objeto en otro que añade comportamiento"
      cuando_usar:
        - "Asignar comportamientos adicionales en runtime"
        - "Herencia es problemática o imposible"
        - "Combinar múltiples comportamientos"
      relacionado_con: ["Adapter", "Composite", "Proxy", "Strategy"]
    
    facade:
      nombre: "Facade"
      url: "https://refactoring.guru/es/design-patterns/facade"
      problema: "Proporcionar interfaz simplificada a sistema complejo"
      solucion: "Clase que provee interfaz simple a subsistema complejo"
      cuando_usar:
        - "Necesitas interfaz limitada pero directa a subsistema complejo"
        - "Estructurar subsistema en capas"
        - "Desacoplar clientes de componentes del subsistema"
      relacionado_con: ["Abstract Factory", "Mediator", "Singleton"]
    
    flyweight:
      nombre: "Flyweight"
      url: "https://refactoring.guru/es/design-patterns/flyweight"
      problema: "Ahorrar RAM compartiendo estado común entre múltiples objetos"
      solucion: "Separar estado intrínseco (compartido) de extrínseco (único)"
      cuando_usar:
        - "Aplicación necesita gran cantidad de objetos similares"
        - "Objetos contienen estado duplicado que puede extraerse"
        - "Grupos de objetos pueden reemplazarse por pocos compartidos"
      relacionado_con: ["Composite", "Singleton"]
    
    proxy:
      nombre: "Proxy"
      url: "https://refactoring.guru/es/design-patterns/proxy"
      problema: "Proporcionar sustituto que controla acceso al objeto original"
      solucion: "Clase proxy con misma interfaz que delega a objeto real"
      cuando_usar:
        - "Lazy initialization (proxy virtual)"
        - "Control de acceso (proxy de protección)"
        - "Caché de resultados (proxy de caché)"
        - "Logging de solicitudes (proxy de logging)"
      relacionado_con: ["Adapter", "Decorator", "Facade"]

# =============================================================================
# PATRONES DE COMPORTAMIENTO
# =============================================================================
comportamiento:
  descripcion: "Algoritmos y asignación de responsabilidades entre objetos"
  patrones:
    chain_of_responsibility:
      nombre: "Chain of Responsibility"
      url: "https://refactoring.guru/es/design-patterns/chain-of-responsibility"
      problema: "Pasar solicitud a lo largo de cadena de manejadores"
      solucion: "Cada manejador decide procesar o pasar al siguiente"
      cuando_usar:
        - "Varios objetos pueden manejar solicitud, manejador no conocido a priori"
        - "Emitir solicitud a varios objetos sin especificar receptor"
        - "Conjunto de manejadores debe especificarse dinámicamente"
      relacionado_con: ["Composite", "Command", "Mediator"]
    
    command:
      nombre: "Command"
      url: "https://refactoring.guru/es/design-patterns/command"
      problema: "Convertir solicitud en objeto independiente con toda su información"
      solucion: "Encapsular solicitud como objeto con método execute()"
      cuando_usar:
        - "Parametrizar objetos con operaciones"
        - "Encolar, programar o ejecutar operaciones remotamente"
        - "Implementar operaciones reversibles (undo/redo)"
      relacionado_con: ["Chain of Responsibility", "Memento", "Strategy"]
    
    iterator:
      nombre: "Iterator"
      url: "https://refactoring.guru/es/design-patterns/iterator"
      problema: "Recorrer elementos de colección sin exponer representación interna"
      solucion: "Extraer comportamiento de recorrido a objeto iterador"
      cuando_usar:
        - "Colección tiene estructura compleja pero ocultar complejidad"
        - "Reducir duplicación de código de recorrido"
        - "Recorrer diferentes estructuras de datos uniformemente"
      relacionado_con: ["Composite", "Factory Method", "Memento", "Visitor"]
    
    mediator:
      nombre: "Mediator"
      url: "https://refactoring.guru/es/design-patterns/mediator"
      problema: "Reducir dependencias caóticas entre objetos"
      solucion: "Objeto mediador que coordina comunicación entre componentes"
      cuando_usar:
        - "Difícil cambiar clases por estar acopladas a muchas otras"
        - "No poder reutilizar componente por depender de muchos otros"
        - "Crear muchas subclases para reutilizar comportamiento"
      relacionado_con: ["Chain of Responsibility", "Facade", "Observer"]
    
    memento:
      nombre: "Memento"
      url: "https://refactoring.guru/es/design-patterns/memento"
      problema: "Guardar y restaurar estado previo de objeto sin violar encapsulación"
      solucion: "Objeto memento que almacena snapshot del estado"
      cuando_usar:
        - "Producir snapshots del estado para restaurar"
        - "Acceso directo a campos viola encapsulación"
        - "Implementar undo/redo o checkpoints"
      relacionado_con: ["Command", "Iterator", "Prototype"]
    
    observer:
      nombre: "Observer"
      url: "https://refactoring.guru/es/design-patterns/observer"
      problema: "Notificar a múltiples objetos sobre eventos en objeto observado"
      solucion: "Mecanismo de suscripción para notificar cambios"
      cuando_usar:
        - "Cambios en un objeto requieren cambiar otros"
        - "Conjunto de objetos a notificar cambia dinámicamente"
        - "Objetos deben observar otros por tiempo limitado"
      relacionado_con: ["Mediator", "Command", "Chain of Responsibility"]
    
    state:
      nombre: "State"
      url: "https://refactoring.guru/es/design-patterns/state"
      problema: "Alterar comportamiento de objeto cuando cambia su estado interno"
      solucion: "Extraer comportamientos a clases de estado separadas"
      cuando_usar:
        - "Objeto se comporta diferente según estado actual"
        - "Muchos condicionales que alteran comportamiento según estado"
        - "Código duplicado entre estados similares"
      relacionado_con: ["Bridge", "Strategy", "Singleton"]
    
    strategy:
      nombre: "Strategy"
      url: "https://refactoring.guru/es/design-patterns/strategy"
      problema: "Definir familia de algoritmos intercambiables"
      solucion: "Extraer algoritmos a clases separadas con interfaz común"
      cuando_usar:
        - "Usar diferentes variantes de algoritmo"
        - "Muchas clases similares que solo difieren en comportamiento"
        - "Aislar lógica de negocio de detalles de implementación"
        - "Condicional masivo que selecciona variante de algoritmo"
      relacionado_con: ["Bridge", "State", "Template Method", "Command"]
    
    template_method:
      nombre: "Template Method"
      url: "https://refactoring.guru/es/design-patterns/template-method"
      problema: "Definir esqueleto de algoritmo permitiendo redefinir ciertos pasos"
      solucion: "Método en superclase que define estructura, subclases implementan pasos"
      cuando_usar:
        - "Clientes extiendan solo pasos particulares de algoritmo"
        - "Varias clases con algoritmos casi idénticos"
        - "Controlar puntos de extensión de subclases"
      relacionado_con: ["Factory Method", "Strategy"]
    
    visitor:
      nombre: "Visitor"
      url: "https://refactoring.guru/es/design-patterns/visitor"
      problema: "Separar algoritmos de objetos sobre los que operan"
      solucion: "Mover operación a clase visitor que recibe objeto como parámetro"
      cuando_usar:
        - "Realizar operación sobre elementos de estructura compleja"
        - "Limpiar lógica de negocio de comportamientos auxiliares"
        - "Comportamiento solo tiene sentido en algunas clases de jerarquía"
      relacionado_con: ["Composite", "Iterator", "Command"]

# =============================================================================
# MAPEO CODE SMELLS → PATRONES SUGERIDOS
# =============================================================================
mapeo_smells:
  descripcion: "Patrones recomendados según code smell detectado"
  
  god_class:
    smells: ["Clase > 300 líneas", "Múltiples responsabilidades", "Demasiados métodos"]
    patrones_sugeridos: ["Facade", "Strategy", "Command"]
    razon: "Extraer responsabilidades a clases especializadas"
  
  switch_statements:
    smells: ["Switch extenso", "Múltiples if-else por tipo", "instanceof repetido"]
    patrones_sugeridos: ["Strategy", "State", "Factory Method"]
    razon: "Reemplazar condicionales con polimorfismo"
  
  feature_envy:
    smells: ["Método usa más datos de otra clase", "Acceso excesivo a getters externos"]
    patrones_sugeridos: ["Move Method", "Visitor"]
    razon: "Mover comportamiento donde están los datos"
  
  parallel_inheritance:
    smells: ["Crear subclase requiere crear otra en jerarquía paralela"]
    patrones_sugeridos: ["Bridge", "Strategy"]
    razon: "Separar dimensiones de variación"
  
  shotgun_surgery:
    smells: ["Cambio pequeño requiere modificar muchas clases"]
    patrones_sugeridos: ["Mediator", "Observer", "Facade"]
    razon: "Centralizar comunicación entre componentes"
  
  primitive_obsession:
    smells: ["Uso excesivo de primitivos para conceptos de dominio"]
    patrones_sugeridos: ["Value Object (DDD)", "Builder"]
    razon: "Encapsular conceptos en objetos ricos"
  
  duplicate_code:
    smells: ["Código repetido en múltiples lugares"]
    patrones_sugeridos: ["Template Method", "Strategy", "Factory Method"]
    razon: "Extraer variación a puntos de extensión"

# =============================================================================
# INDICADORES DE DETECCIÓN (para agentes)
# =============================================================================
indicadores_deteccion:
  descripcion: "Patrones regex y estructurales para detectar patrones en código"
  herramientas: ["grep_search", "semantic_search", "file_search"]
  
  patrones_por_nombre_clase:
    # Buscar con: grep_search("Factory|Builder|Singleton|Adapter|...", isRegexp=true)
    alta_confianza:
      - {patron: "factory_method", regex: "Factory|FactoryMethod|Creator", archivos: "**/*[Ff]actory*"}
      - {patron: "abstract_factory", regex: "AbstractFactory|FactoryProvider", archivos: "**/*[Ff]actory*"}
      - {patron: "builder", regex: "Builder|Director", archivos: "**/*[Bb]uilder*"}
      - {patron: "singleton", regex: "getInstance|_instance|INSTANCE", archivos: "*"}
      - {patron: "adapter", regex: "Adapter|Wrapper", archivos: "**/*[Aa]dapter*|**/*[Ww]rapper*"}
      - {patron: "decorator", regex: "Decorator|Wrapper", archivos: "**/*[Dd]ecorator*"}
      - {patron: "facade", regex: "Facade|Gateway", archivos: "**/*[Ff]acade*|**/*[Gg]ateway*"}
      - {patron: "proxy", regex: "Proxy|Surrogate", archivos: "**/*[Pp]roxy*"}
      - {patron: "observer", regex: "Observer|Listener|Subscriber|EventEmitter", archivos: "**/*[Oo]bserver*|**/*[Ll]istener*"}
      - {patron: "strategy", regex: "Strategy|Policy", archivos: "**/*[Ss]trategy*|**/*[Pp]olicy*"}
      - {patron: "command", regex: "Command|Handler|Executor", archivos: "**/*[Cc]ommand*|**/*[Hh]andler*"}
      - {patron: "repository", regex: "Repository|Repo|DAO", archivos: "**/*[Rr]epository*|**/*[Rr]epo*|**/*DAO*"}
    
    media_confianza:
      - {patron: "state", regex: "State|Context", requiere_validacion: "Verificar máquina de estados"}
      - {patron: "template_method", regex: "Template|Abstract.*Step", requiere_validacion: "Verificar herencia con métodos abstractos"}
      - {patron: "composite", regex: "Composite|Component|Leaf|Node", requiere_validacion: "Verificar estructura de árbol"}
  
  patrones_por_estructura_carpetas:
    # Buscar con: file_search("**/domain/**") o list_dir
    arquitectura:
      - {patron: "clean_architecture", indicadores: ["domain/", "application/", "infrastructure/", "usecases/"]}
      - {patron: "hexagonal", indicadores: ["ports/", "adapters/", "driven/", "driving/"]}
      - {patron: "mvc", indicadores: ["controllers/", "models/", "views/"]}
      - {patron: "mvvm", indicadores: ["viewmodels/", "views/", "models/"]}
      - {patron: "cqrs", indicadores: ["commands/", "queries/", "handlers/"]}
      - {patron: "ddd", indicadores: ["entities/", "valueobjects/", "aggregates/", "repositories/"]}
    
    organizacion:
      - {patron: "feature_based", indicadores: ["features/*/components", "features/*/hooks", "features/*/services"]}
      - {patron: "layer_based", indicadores: ["src/services/", "src/controllers/", "src/models/", "src/utils/"]}
  
  patrones_por_codigo:
    # Buscar con: grep_search dentro de archivos específicos
    singleton:
      java: "private static .* instance|getInstance\\(\\)"
      python: "_instance|__new__|@singleton"
      typescript: "private static instance|getInstance\\(\\)"
      csharp: "private static readonly .* _instance|Lazy<"
    
    observer:
      all: "subscribe|unsubscribe|notify|emit|addEventListener|removeEventListener|on\\(|off\\("
    
    dependency_injection:
      java: "@Inject|@Autowired|@Resource"
      typescript: "@Injectable|@Inject|constructor\\(.*private.*service"
      python: "@inject|Depends\\("
      csharp: "\\[Inject\\]|IServiceProvider|AddScoped|AddTransient|AddSingleton"

  algoritmo_deteccion:
    paso_1:
      nombre: "Buscar por nombre de clase/archivo"
      herramienta: "file_search"
      accion: "Buscar archivos que coincidan con patrones de alta_confianza"
    paso_2:
      nombre: "Buscar por estructura de carpetas"
      herramienta: "list_dir + file_search"
      accion: "Detectar patrones arquitectónicos por organización"
    paso_3:
      nombre: "Validar por código"
      herramienta: "grep_search + read_file"
      accion: "Confirmar implementación real del patrón"
    paso_4:
      nombre: "Asignar confianza"
      accion: |
        SI nombre_clase + estructura + código coinciden → confianza: alta
        SI solo nombre_clase coincide → confianza: media
        SI solo estructura coincide → confianza: baja (requiere validación manual)

  output_deteccion:
    formato: |
      patrones_detectados:
        - patron: "[nombre]"
          categoria: "[creacional|estructural|comportamiento|arquitectura]"
          confianza: "[alta|media|baja]"
          ubicaciones:
            - archivo: "[path]"
              linea: [numero]
              evidencia: "[fragmento de código]"
          referencia: "[URL de patrones_diseno.rules.md]"


  formato_sugerencia: |
    📚 **Patrón sugerido:** {nombre}
    **Problema que resuelve:** {problema}
    **Cuándo usar:** {cuando_usar[0]}
    **Referencia:** {url}
  
  ejemplo_output: |
    📚 **Patrón sugerido:** Strategy
    **Problema que resuelve:** Definir familia de algoritmos intercambiables
    **Cuándo usar:** Condicional masivo que selecciona variante de algoritmo
    **Referencia:** https://refactoring.guru/es/design-patterns/strategy

# =============================================================================
# EJEMPLOS DE CÓDIGO POR LENGUAJE
# =============================================================================
ejemplos_codigo:
  descripcion: "URLs directas a ejemplos de implementación por lenguaje"
  base_url: "https://refactoring.guru/es/design-patterns"
  patron_url: "{base_url}/{patron}/{lenguaje}/example"
  
  lenguajes_disponibles:
    java: "java"
    csharp: "csharp"
    cpp: "cpp"
    python: "python"
    go: "go"
    typescript: "typescript"
    php: "php"
    ruby: "ruby"
    rust: "rust"
    swift: "swift"
  
  # Mapeo stack del proyecto → lenguaje en refactoring.guru
  mapeo_stack:
    java: "java"
    kotlin: "java"           # Usa ejemplos Java (compatible)
    javascript: "typescript" # TypeScript es superset
    typescript: "typescript"
    python: "python"
    dotnet: "csharp"
    csharp: "csharp"
    go: "go"
    php: "php"
    ruby: "ruby"
    rust: "rust"
    swift: "swift"
    cpp: "cpp"
  
  urls_por_patron:
    # Creacionales
    factory_method:
      java: "https://refactoring.guru/es/design-patterns/factory-method/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/factory-method/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/factory-method/python/example"
      go: "https://refactoring.guru/es/design-patterns/factory-method/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/factory-method/typescript/example"
    
    abstract_factory:
      java: "https://refactoring.guru/es/design-patterns/abstract-factory/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/abstract-factory/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/abstract-factory/python/example"
      go: "https://refactoring.guru/es/design-patterns/abstract-factory/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/abstract-factory/typescript/example"
    
    builder:
      java: "https://refactoring.guru/es/design-patterns/builder/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/builder/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/builder/python/example"
      go: "https://refactoring.guru/es/design-patterns/builder/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/builder/typescript/example"
    
    prototype:
      java: "https://refactoring.guru/es/design-patterns/prototype/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/prototype/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/prototype/python/example"
      go: "https://refactoring.guru/es/design-patterns/prototype/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/prototype/typescript/example"
    
    singleton:
      java: "https://refactoring.guru/es/design-patterns/singleton/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/singleton/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/singleton/python/example"
      go: "https://refactoring.guru/es/design-patterns/singleton/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/singleton/typescript/example"
    
    # Estructurales
    adapter:
      java: "https://refactoring.guru/es/design-patterns/adapter/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/adapter/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/adapter/python/example"
      go: "https://refactoring.guru/es/design-patterns/adapter/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/adapter/typescript/example"
    
    bridge:
      java: "https://refactoring.guru/es/design-patterns/bridge/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/bridge/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/bridge/python/example"
      go: "https://refactoring.guru/es/design-patterns/bridge/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/bridge/typescript/example"
    
    composite:
      java: "https://refactoring.guru/es/design-patterns/composite/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/composite/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/composite/python/example"
      go: "https://refactoring.guru/es/design-patterns/composite/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/composite/typescript/example"
    
    decorator:
      java: "https://refactoring.guru/es/design-patterns/decorator/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/decorator/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/decorator/python/example"
      go: "https://refactoring.guru/es/design-patterns/decorator/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/decorator/typescript/example"
    
    facade:
      java: "https://refactoring.guru/es/design-patterns/facade/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/facade/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/facade/python/example"
      go: "https://refactoring.guru/es/design-patterns/facade/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/facade/typescript/example"
    
    flyweight:
      java: "https://refactoring.guru/es/design-patterns/flyweight/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/flyweight/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/flyweight/python/example"
      go: "https://refactoring.guru/es/design-patterns/flyweight/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/flyweight/typescript/example"
    
    proxy:
      java: "https://refactoring.guru/es/design-patterns/proxy/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/proxy/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/proxy/python/example"
      go: "https://refactoring.guru/es/design-patterns/proxy/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/proxy/typescript/example"
    
    # Comportamiento
    chain_of_responsibility:
      java: "https://refactoring.guru/es/design-patterns/chain-of-responsibility/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/chain-of-responsibility/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/chain-of-responsibility/python/example"
      go: "https://refactoring.guru/es/design-patterns/chain-of-responsibility/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/chain-of-responsibility/typescript/example"
    
    command:
      java: "https://refactoring.guru/es/design-patterns/command/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/command/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/command/python/example"
      go: "https://refactoring.guru/es/design-patterns/command/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/command/typescript/example"
    
    iterator:
      java: "https://refactoring.guru/es/design-patterns/iterator/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/iterator/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/iterator/python/example"
      go: "https://refactoring.guru/es/design-patterns/iterator/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/iterator/typescript/example"
    
    mediator:
      java: "https://refactoring.guru/es/design-patterns/mediator/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/mediator/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/mediator/python/example"
      go: "https://refactoring.guru/es/design-patterns/mediator/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/mediator/typescript/example"
    
    memento:
      java: "https://refactoring.guru/es/design-patterns/memento/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/memento/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/memento/python/example"
      go: "https://refactoring.guru/es/design-patterns/memento/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/memento/typescript/example"
    
    observer:
      java: "https://refactoring.guru/es/design-patterns/observer/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/observer/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/observer/python/example"
      go: "https://refactoring.guru/es/design-patterns/observer/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/observer/typescript/example"
    
    state:
      java: "https://refactoring.guru/es/design-patterns/state/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/state/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/state/python/example"
      go: "https://refactoring.guru/es/design-patterns/state/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/state/typescript/example"
    
    strategy:
      java: "https://refactoring.guru/es/design-patterns/strategy/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/strategy/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/strategy/python/example"
      go: "https://refactoring.guru/es/design-patterns/strategy/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/strategy/typescript/example"
    
    template_method:
      java: "https://refactoring.guru/es/design-patterns/template-method/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/template-method/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/template-method/python/example"
      go: "https://refactoring.guru/es/design-patterns/template-method/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/template-method/typescript/example"
    
    visitor:
      java: "https://refactoring.guru/es/design-patterns/visitor/java/example"
      csharp: "https://refactoring.guru/es/design-patterns/visitor/csharp/example"
      python: "https://refactoring.guru/es/design-patterns/visitor/python/example"
      go: "https://refactoring.guru/es/design-patterns/visitor/go/example"
      typescript: "https://refactoring.guru/es/design-patterns/visitor/typescript/example"

  uso_dinamico: |
    # Para obtener URL de ejemplo según stack del proyecto:
    # 1. Leer stack de {{archivos.stack_proyecto}}
    # 2. Mapear a lenguaje usando mapeo_stack
    # 3. Construir URL: urls_por_patron[patron][lenguaje]
    # 4. Hacer fetch para obtener código de ejemplo

# =============================================================================
# REFERENCIAS ADICIONALES
# =============================================================================
referencias:
  principal:
    nombre: "Refactoring.Guru"
    url: "https://refactoring.guru/es/design-patterns"
    idiomas: ["es", "en", "ru", "zh", "pt", "fr", "de", "it", "pl", "ko", "uk"]
    ejemplos_codigo: ["Java", "C#", "C++", "PHP", "Python", "Go", "Ruby", "TypeScript", "Swift"]
  
  alternativas:
    - nombre: "SourceMaking"
      url: "https://sourcemaking.com/design_patterns"
    - nombre: "Design Patterns (GoF Book)"
      referencia: "ISBN 0-201-63361-2"
    - nombre: "Head First Design Patterns"
      referencia: "ISBN 978-0596007126"
```
