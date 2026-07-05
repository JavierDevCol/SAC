```mermaid
stateDiagram-v2
    [*] --> EstadoInicial
    EstadoInicial --> EnProceso: evento_inicio
    EnProceso --> Completado: evento_fin
    EnProceso --> Error: evento_fallo
    Error --> EstadoInicial: reintento
    Completado --> [*]
```
