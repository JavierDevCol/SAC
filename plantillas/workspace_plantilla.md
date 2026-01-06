# Workspace: [Nombre del Workspace]

> **Generado:** [timestamp]  
> **Tipo:** Multi-Proyecto  
> **Total Proyectos:** [N]

---

## 📊 Resumen del Workspace

| Proyecto | Tipo | Stack | Estado | Contexto |
|----------|------|-------|--------|----------|
| [nombre_proyecto] | [tipo] | [stack] | [estado] | [enlace] |

---

## 🔗 Relaciones entre Proyectos

| Proyecto Origen | Proyecto Destino | Tipo Relación |
|-----------------|------------------|---------------|
| [proyecto] | [proyecto] | [Consume API/Comparte BD/Independiente] |

---

## 📁 Estructura del Workspace

```
[nombre_workspace]/
├── .cochas/
│   ├── artifacts/
│   │   ├── workspace.md
│   │   ├── contextos/
│   │   │   └── contexto_proyecto_[nombre].md
│   │   ├── backlog_desarrollo.md
│   │   └── HU/
│   │       ├── compartidas/
│   │       └── [nombre_proyecto]/
│   └── session/
│       └── session_state.json
├── [proyecto_1]/
└── [proyecto_2]/
```

---

## 📋 Backlogs

### Backlog Compartido
| ID | Título | Proyectos Afectados | Estado |
|----|--------|---------------------|--------|
| [ID] | [título] | [lista proyectos] | [estado] |

### Backlog por Proyecto

#### [nombre_proyecto]
| ID | Título | Estado |
|----|--------|--------|
| [ID] | [título] | [estado] |

---

## ⚙️ Comandos del Workspace

```bash
# Analizar proyecto específico
>tomar_contexto [nombre_proyecto]

# Analizar todos los proyectos
>tomar_contexto --all

# Ver HUs compartidas
*HU --compartidas

# Ver HUs de un proyecto
*HU --proyecto=[nombre_proyecto]
```

---

## 📝 Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| [timestamp] | Workspace detectado | [N] proyectos identificados |

---

> **Archivo generado automáticamente por >tomar_contexto**
