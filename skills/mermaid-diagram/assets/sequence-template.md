```mermaid
sequenceDiagram
    autonumber
    rect rgba(0, 150, 255, 0.15)
        Note over Actor,Servicio: Fase 1 — Descripción
        Actor->>Servicio: Mensaje de solicitud
        Servicio-->>Actor: Respuesta
    end
    rect rgba(0, 255, 127, 0.15)
        Note over Actor,Servicio: Fase 2 — Descripción
        Actor->>Servicio: Siguiente acción
        Servicio-->>Actor: Resultado
    end
```
