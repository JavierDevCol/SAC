# 🔄 Diagrama de Ciclo de Vida del Sistema SAC

> **Sistema:** SAC - Sistema Agéntico COCHAS
> **Versión:** 7.25.0
> **Última Actualización:** 3 de julio de 2026

---

## 📖 Descripción

Este diagrama de estado muestra el **ciclo de vida completo** del sistema SAC, incluyendo:
- Historias de Usuario (HU)
- Bugs
- Pendientes y Hallazgos

---

## 🎨 Leyenda de Colores

| Color | Significado |
|-------|-------------|
| 🟠 Naranja | Estados iniciales / Pendientes |
| 🔵 Azul | Procesos de análisis y refinamiento |
| 🟢 Verde | Estados de éxito / Completados |
| 🩷 Rosa | Planificación y ejecución |
| 🔴 Rojo | Bloqueos / Estados críticos |

---

## 🔄 Diagrama de Estado Principal

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Pendiente: Crear HU
    
    state "Ciclo de Vida HU" as hu_cycle {
        Pendiente --> Refinada: >refinar_hu<br/>(REFINADOR)
        Refinada --> Aprobada: >validar_hu<br/>(ARQUITECTO)
        Aprobada --> Planificada: >planificar_hu<br/>(ARCHDEV)
        Planificada --> EnEjecucion: >ejecutar_plan<br/>(ARCHDEV)
        EnEjecucion --> Completada: Tests OK<br/>Commit
    }
    
    state "Bloqueos" as blocks {
        state "Bloqueada [B]" as Bloqueada
        Bloqueada --> Pendiente: Resolver
        Bloqueada --> Refinada: Resolver
        Bloqueada --> Aprobada: Resolver
        Bloqueada --> Planificada: Resolver
        Bloqueada --> EnEjecucion: Resolver
    }
    
    state "Bugs" as bugs {
        [*] --> Nuevo: Detectar bug
        Nuevo --> EnTriage: Analizar
        EnTriage --> VinculadoHU: Asignar a HU
        EnTriage --> AjusteHU: Fix menor
        VinculadoHU --> Corregido: >registrar_bug
        AjusteHU --> Corregido: Fix aplicado
        Corregido --> [*]
    }
    
    state "Pendientes" as pnds {
        [*] --> Registrado: Detectar
        Registrado --> PromovidoHU: >crear_hu
        Registrado --> ReclasificadoBUG: >registrar_bug
        Registrado --> Descartado: Evaluar
        PromovidoHU --> [*]
        ReclasificadoBUG --> [*]
        Descartado --> [*]
    }
    
    Pendiente --> Bloqueada: Dependencia
    Refinada --> Bloqueada: Dependencia
    Aprobada --> Bloqueada: Dependencia
    Planificada --> Bloqueada: Dependencia
    EnEjecucion --> Bloqueada: Dependencia
    Completada --> [*]

    classDef pending fill:#FFA50026,stroke:#FFA500,color:#fff
    classDef refined fill:#0096FF26,stroke:#0096FF,color:#fff
    classDef approved fill:#00FF7F26,stroke:#00FF7F,color:#fff
    classDef planned fill:#FF69B426,stroke:#FF69B4,color:#fff
    classDef executing fill:#FF000026,stroke:#FF0000,color:#fff
    classDef completed fill:#00FF7F26,stroke:#00FF7F,color:#fff
    classDef blocked fill:#FF000026,stroke:#FF0000,color:#fff
    classDef bugNew fill:#FFA50026,stroke:#FFA500,color:#fff
    classDef bugTriage fill:#0096FF26,stroke:#0096FF,color:#fff
    classDef bugLinked fill:#FF69B426,stroke:#FF69B4,color:#fff
    classDef bugFixed fill:#00FF7F26,stroke:#00FF7F,color:#fff
    classDef pndRegistered fill:#FFA50026,stroke:#FFA500,color:#fff
    classDef pndPromoted fill:#00FF7F26,stroke:#00FF7F,color:#fff
    classDef pndReclassified fill:#0096FF26,stroke:#0096FF,color:#fff
    classDef pndDiscarded fill:#FF000026,stroke:#FF0000,color:#fff
    
    class Pendiente pending
    class Refinada refined
    class Aprobada approved
    class Planificada planned
    class EnEjecucion executing
    class Completada completed
    class Bloqueada blocked
    class Nuevo bugNew
    class EnTriage bugTriage
    class VinculadoHU bugLinked
    class AjusteHU bugLinked
    class Corregido bugFixed
    class Registrado pndRegistered
    class PromovidoHU pndPromoted
    class ReclasificadoBUG pndReclassified
    class Descartado pndDiscarded
```

---

## 📋 Estados de las HU

| Estado | Símbolo | Descripción | Responsable |
|--------|---------|-------------|-------------|
| Pendiente | `[ ]` | HU creada, sin analizar | - |
| Refinada | `[R]` | Analizada con criterios y estimación | Refinador HU |
| Aprobada | `[A]` | Validada arquitectónicamente | Arquitecto Onad |
| Planificada | `[P]` | Tiene plan de implementación | ArchDev Pro |
| En Ejecución | `[E]` | Agente está ejecutando el plan | ArchDev Pro |
| Completada | `[X]` | Implementación terminada | ArchDev Pro |
| Bloqueada | `[B]` | Dependencias no resueltas | Cualquier rol |

---

## 🐛 Estados de los Bugs

| Estado | Descripción |
|--------|-------------|
| Nuevo | Bug detectado, sin analizar |
| En Triage | Analizando causa raíz |
| Vinculado a HU | Asignado a una HU para corrección |
| Ajuste en HU | Fix menor aplicado directamente |
| Corregido | Bug solucionado |

---

## 📝 Estados de los Pendientes

| Estado | Descripción |
|--------|-------------|
| Registrado | Pendiente documentado |
| Promovido a HU | Convertido en Historia de Usuario |
| Reclasificado a BUG | Convertido en Bug |
| Descartado | Evaluado y descartado |

---

## 🔗 Referencias

- [Guía del Ciclo de Vida de Tareas](guia_ciclo_vida_tareas.md)
- [Plantilla de HU](../../plantillas/hu/HU.md)
- [Plantilla de Bug](../../plantillas/bug_plantilla.md)
- [Plantilla de Pendientes](../../plantillas/pendientes_plantilla.md)
