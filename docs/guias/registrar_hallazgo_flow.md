# Diagrama: registrar_hallazgo.tool.yaml

## Flujo del Dispatcher de Clasificación

```mermaid
flowchart TD
    classDef startEnd fill:#00FF7F26,stroke:#00FF7F,color:#fff
    classDef process fill:#0096FF26,stroke:#0096FF,color:#fff
    classDef decision fill:#FFA50026,stroke:#FFA500,color:#fff
    classDef redirect fill:#FF69B426,stroke:#FF69B4,color:#fff

    INICIO([🚀 INICIO]) --> P1

    subgraph PROCESO["📋 REGISTRAR HALLAZGO — Dispatcher"]
        P1["📥 PASO 1: Recepción Universal
        ─────────────────────────────
        • Recopilar descripción del hallazgo
        • Detectar proyecto del contexto
        • Preguntar por evidencia/logs
        • Preguntar si ya fue corregido"]

        P1 --> P2

        P2["🔍 PASO 2: Clasificación Automática
        ─────────────────────────────
        • Analizar keywords (error vs warning)
        • Evaluar comportamiento descrito
        • Mostrar evaluación al usuario:
        📊 Evaluación: [SUGERENCIA]"]

        P2 --> P3

        P3["❓ PASO 3: Confirmación del Usuario
        ─────────────────────────────
        Este hallazgo parece un [SUGERENCIA]
        
        ¿Confirmas?"]

        P3 -->|"🐛 [B] Es un bug"| R1
        P3 -->|"📋 [P] Es un pendiente"| R2
        P3 -->|"🔍 [I] Investigar"| R3
    end

    subgraph REDIRECCION["↪️ REDIRECCIÓN CON CONTEXTO"]
        R1["📦 Preparar contexto_transferido
        ─────────────────────────────
        • origen: dispatcher
        • descripcion, proyecto, logs
        • ya_corregido
        • clasificacion_confirmada: true"]

        R2["📦 Preparar contexto_transferido
        ─────────────────────────────
        • origen: dispatcher
        • descripcion, proyecto, logs
        • ya_corregido
        • clasificacion_confirmada: true"]

        R3["📦 Preparar contexto_transferido
        ─────────────────────────────
        • origen: dispatcher
        • descripcion, proyecto, logs
        • ya_corregido
        • categoria: investigacion
        • clasificacion_confirmada: true"]
    end

    R1 --> BUG
    R2 --> PND
    R3 --> PND

    subgraph DESTINOS["🎯 HERRAMIENTAS DESTINO"]
        BUG["🐛 registrar_bug
        ─────────────────────────────
        MODO ABREVIADO
        • Reutiliza datos del contexto
        • Asigna ID autoincremental
        • Crea carpeta BUG-NNN/"]

        PND["📋 registrar_pendiente
        ─────────────────────────────
        MODO ABREVIADO
        • Reutiliza datos del contexto
        • Asigna ID autoincremental
        • SALTA evaluación de severidad"]
    end

    BUG --> FIN
    PND --> FIN

    FIN([✅ FIN])

    class INICIO,FIN startEnd
    class P1,P2 process
    class P3 decision
    class R1,R2,R3 redirect
    class BUG,PND process
```

## Notas

- **Dispatcher**: Esta herramienta NO genera archivos propios
- **Contexto Transferido**: Todos los datos se pasan a la herramienta destino
- **Modo Abreviado**: Las herramientas destino reutilizan datos sin duplicar trabajo
- **Restricción de Rol**: Si el Desarrollador elige [P], se informa que es exclusivo del Arquitecto
