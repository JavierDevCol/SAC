# Reglas de Generación: MermaidJS

```yaml
# ============================================
# REGLAS MERMAID - ESTÁNDARES TÉCNICOS Y VISUALES
# ============================================

identificacion:
  nombre: "Reglas de Generación MermaidJS"
  version: "1.1"
  proposito: "Definir estándares técnicos y visuales para diagramas Mermaid"

# ============================================
# PROCESO DE GENERACIÓN
# ============================================
proceso:
  - paso: 1
    accion: "Validar tipo de diagrama"
    usar: "{{diagramas_validos}}"
  - paso: 2
    accion: "Seleccionar tipo según contexto"
    usar: "{{reglas_diagrama.[tipo].cuando_usar}}"
  - paso: 3
    accion: "Validar ausencia de HTML"
    usar: "{{reglas_criticas.html_prohibido}}"
  - paso: 4
    accion: "Aplicar formato de color según tipo"
    usar: "{{reglas_criticas.colores_por_tipo.[tipo]}}"
  - paso: 5
    accion: "Seleccionar colores por propósito"
    usar: "{{paleta_colores.colores}}"
  - paso: 6
    accion: "Aplicar reglas del tipo de diagrama"
    usar: "{{reglas_diagrama.[tipo].reglas}}"
  - paso: 7
    accion: "Si subgraphs anidados, aplicar técnica"
    usar: "{{solucion_subgraphs_anidados}}"
  - paso: 8
    accion: "Ejecutar validaciones pre-renderizado"
    usar: "{{validaciones.pre_renderizado}}"

# ============================================
# PALETA DE COLORES
# ============================================
paleta_colores:
  descripcion: "Colores estandarizados para mantener consistencia visual"
  nota_importante: "Usar transparencia 0.15 para compatibilidad dark/light mode"
  colores:
    azul:
      uso: "App/Build/Procesos"
      hex: "#0096FF26"
      rgba: "rgba(0, 150, 255, 0.15)"
    naranja:
      uso: "Mid/Storage/Almacenamiento"
      hex: "#FFA50026"
      rgba: "rgba(255, 165, 0, 0.15)"
    verde:
      uso: "Red/Deploy/Éxito"
      hex: "#00FF7F26"
      rgba: "rgba(0, 255, 127, 0.15)"
    rosa:
      uso: "Sec/Auth/Seguridad"
      hex: "#FF69B426"
      rgba: "rgba(255, 105, 180, 0.15)"
    rojo:
      uso: "Error/Crítico"
      hex: "#FF000026"
      rgba: "rgba(255, 0, 0, 0.15)"

# ============================================
# REGLAS CRÍTICAS ANTI-ERRORES
# ============================================
reglas_criticas:
  html_prohibido:
    obligatorio: true
    descripcion: "Evitar etiquetas HTML que rompen el renderizado"
    prohibido:
      - "<span>"
      - "<span style=...>"
      - "<b>"
      - "<div>"
      - "<br>"
    alternativa: "Usar sintaxis Markdown estándar (**texto** para negritas)"
    ejemplo_incorrecto: "<b>Texto importante</b>"
    ejemplo_correcto: "**Texto importante**"
  
  colores_por_tipo:
    obligatorio: true
    descripcion: "El formato de color depende del tipo de diagrama"
    flowchart:
      formato_requerido: "HEX con Alpha (#RRGGBBAA)"
      formato_prohibido: "rgba()"
      razon: "rgba() causa error de sintaxis en flowcharts"
      ejemplo_correcto: "style Nodo fill:#0096FF26,stroke:#0096FF,color:#fff"
      ejemplo_incorrecto: "style Nodo fill:rgba(0, 150, 255, 0.15)"
    sequence:
      formato_requerido: "RGBA"
      razon: "Los bloques rect en sequence sí soportan rgba()"
      ejemplo_correcto: "rect rgba(0, 150, 255, 0.15)"

# ============================================
# TIPOS DE DIAGRAMA Y REGLAS ESPECÍFICAS
# ============================================
tipos_diagrama:
  sequence_diagram:
    declaracion: "sequenceDiagram"
    cuando_usar: "Interacciones entre componentes/servicios/actores"
    reglas:
      - accion: "Usar autonumber"
        obligatorio: true
        descripcion: "Numera automáticamente los mensajes"
      - accion: "Agrupar fases con bloques rect"
        obligatorio: false
        descripcion: "Mejora la legibilidad visual"
      - accion: "Usar formato RGBA para colores"
        obligatorio: true
        formato: "rect rgba(R, G, B, 0.15)"
    ejemplo: |
      ```mermaid
      sequenceDiagram
          autonumber
          rect rgba(0, 150, 255, 0.15)
              Note over A,B: Fase de Autenticación
              A->>B: Solicitar token
              B-->>A: Token JWT
          end
          rect rgba(0, 255, 127, 0.15)
              Note over A,C: Fase de Operación
              A->>C: Ejecutar acción
              C-->>A: Resultado
          end
      ```

  flowchart:
    declaracion: "graph TD | graph LR | flowchart TD | flowchart LR"
    cuando_usar: "Flujos de decisión, procesos, pipelines"
    reglas:
      - accion: "Usar subgraph para agrupar"
        obligatorio: false
        descripcion: "Organiza nodos relacionados"
      - accion: "Usar HEX con Alpha para estilos"
        obligatorio: true
        formato: "style Nodo fill:#HEX,stroke:#HEX,color:#fff"
      - accion: "Añadir color:#fff para legibilidad"
        obligatorio: true
        descripcion: "Asegura texto visible en fondos de color"
    ejemplo: |
      ```mermaid
      graph TD
          subgraph Proceso["Flujo Principal"]
              A[Inicio] --> B{Decisión}
              B -->|Sí| C[Procesar]
              B -->|No| D[Rechazar]
              C --> E[Fin]
              D --> E
          end
          style A fill:#0096FF26,stroke:#0096FF,color:#fff
          style C fill:#00FF7F26,stroke:#00FF7F,color:#fff
          style D fill:#FF000026,stroke:#FF0000,color:#fff
      ```

  state_diagram:
    declaracion: "stateDiagram-v2"
    cuando_usar: "Estados y transiciones del sistema"
    reglas:
      - accion: "Usar HEX con Alpha para estilos"
        obligatorio: true
        formato: "Igual que flowchart"
    ejemplo: |
      ```mermaid
      stateDiagram-v2
          [*] --> Pendiente
          Pendiente --> EnProceso: iniciar
          EnProceso --> Completado: finalizar
          EnProceso --> Error: fallo
          Error --> Pendiente: reintentar
          Completado --> [*]
      ```

  c4_component:
    declaracion: "C4Component"
    cuando_usar: "Arquitectura de componentes estilo C4"
    reglas:
      - accion: "Definir contenedores y componentes"
        obligatorio: true
      - accion: "Usar relaciones claras"
        obligatorio: true

# ============================================
# SOLUCIÓN PARA SUBGRAPHS ANIDADOS
# ============================================
solucion_subgraphs_anidados:
  nombre: "Técnica del Nodo Fantasma"
  problema: "Los títulos de subgraphs anidados se superponen visualmente"
  obligatorio_cuando: "Se usan subgraphs dentro de otros subgraphs"
  pasos:
    - paso: 1
      accion: "Definir clase spacer al inicio del diagrama"
      codigo: "classDef spacer fill:none,stroke:none,height:0px;"
    - paso: 2
      accion: "Crear nodo vacío dentro del subgraph padre"
      codigo: "sep[ ]:::spacer"
    - paso: 3
      accion: "Forzar posición con link invisible"
      codigo: "sep ~~~ NodoDelHijo"
  ejemplo_completo: |
    ```mermaid
    graph TD
        classDef spacer fill:none,stroke:none,height:0px;
        subgraph Padre["Contenedor Principal"]
            sep[ ]:::spacer
            sep ~~~ HijoA
            subgraph Hijo["Subcontenedor"]
                HijoA[Nodo A]
                HijoB[Nodo B]
                HijoA --> HijoB
            end
        end
        style HijoA fill:#0096FF26,stroke:#0096FF,color:#fff
        style HijoB fill:#FFA50026,stroke:#FFA500,color:#fff
    ```

# ============================================
# COMPATIBILIDAD Y RENDERIZADO
# ============================================
compatibilidad:
  dark_light_mode:
    estrategia: "Usar transparencia 0.15 en todos los colores de fondo"
    razon: "Asegura visibilidad en ambos modos de tema"
  
  renderizadores_soportados:
    - nombre: "GitHub Markdown"
      notas: "Soporte nativo"
    - nombre: "VS Code Preview"
      notas: "Requiere extensión Mermaid"
    - nombre: "Mermaid Live Editor"
      notas: "https://mermaid.live"
    - nombre: "GitLab"
      notas: "Soporte nativo"
    - nombre: "Notion"
      notas: "Soporte mediante bloques de código"
    - nombre: "Azure DevOps Wiki"
      notas: "Soporte nativo"

# ============================================
# VALIDACIONES
# ============================================
validaciones:
  pre_renderizado:
    - descripcion: "Verificar que no existan etiquetas HTML"
      buscar: ["<span", "<div", "<b>", "<br>"]
    - descripcion: "Confirmar formato de color según tipo de diagrama"
      flowchart: "Solo HEX (#RRGGBBAA)"
      sequence: "RGBA permitido"
    - descripcion: "Validar sintaxis de subgraphs anidados"
      verificar: "Técnica Nodo Fantasma aplicada si hay anidación"
  
  post_renderizado:
    - "Verificar legibilidad de texto sobre fondos de color"
    - "Confirmar que los colores se muestran correctamente"
    - "Validar que no hay superposición de elementos"
    - "Probar en dark mode y light mode"

# ============================================
# RESUMEN RÁPIDO
# ============================================
resumen_rapido:
  reglas_de_oro:
    - "🚫 NUNCA usar HTML (<span>, <b>, <div>, <br>)"
    - "🎨 Flowchart/State → HEX (#RRGGBBAA)"
    - "🎨 Sequence → RGBA (rgba(R,G,B,0.15))"
    - "📦 Subgraphs anidados → Técnica Nodo Fantasma"
    - "🌓 Siempre transparencia 0.15 para dark/light mode"
    - "✏️ Siempre color:#fff en estilos para legibilidad"
```
