# 📦 Especificación: `session_state.json`

> **Versión:** 4.0  
> **Última actualización:** 6 de enero de 2026

---

## 🎯 Propósito

Archivo central de estado del Sistema COCHAS que persiste información entre cambios de rol, trackea HUs y mantiene contexto de ejecución. Soporta workspaces single y multi-proyecto.

---

## 📖 Especificación

> ⚠️ **INSTRUCCIÓN OBLIGATORIA**  
> Para generar o actualizar `session_state.json`, seguir AL PIE DE LA LETRA las siguientes instrucciones. NO omitir ningún paso ni campo.

```yaml
# ============================================
# SESSION_STATE.JSON - Especificación v4.0
# ============================================

# ============================================
# MANDATORY - Reglas Inviolables
# ============================================
mandatory:
  - instruccion: "Actualizar campo 'timestamp' en CADA modificación del archivo"
    nunca_saltar: true
  - instruccion: "Actualizar 'metadata.ultima_actividad' en CADA modificación"
    nunca_saltar: true
  - instruccion: "Agregar entrada a 'log_eventos_clave' para eventos significativos"
    nunca_saltar: true
  - instruccion: "Mantener 'tablero_tareas' sincronizado con backlog_desarrollo.md"
    nunca_saltar: true
  - instruccion: "Campo 'proyecto' en HU es OBLIGATORIO: null=compartida, 'nombre'=específica"
    nunca_saltar: true
  - instruccion: "En multi-proyecto: solo UN proyecto puede tener activo=true"
    nunca_saltar: true
  - instruccion: "Limpiar 'ejecucion_activa' (poner null) cuando finaliza una ejecución"
    nunca_saltar: true

# ============================================
# CAMPOS RAÍZ
# ============================================
campos_raiz:
  version:
    tipo: string
    requerido: true
    valor: "4.0"
    descripcion: "Versión del esquema"
  
  timestamp:
    tipo: string
    formato: ISO_8601
    requerido: true
    descripcion: "Última actualización del archivo"
    ejemplo: "2026-01-06T10:00:00Z"

# ============================================
# WORKSPACE
# ============================================
workspace:
  descripcion: "Información del workspace (reemplaza 'proyecto' de v3.0)"
  requerido: true
  campos:
    tipo:
      tipo: enum
      valores: [single, multi]
      requerido: true
      descripcion: "single=proyecto único, multi=múltiples proyectos"
    
    nombre:
      tipo: string
      requerido: true
      descripcion: "Nombre del workspace"
    
    workspace_archivo:
      tipo: string_o_null
      requerido: true
      descripcion: "Ruta a workspace.md (null si tipo=single)"
    
    proyectos:
      tipo: array
      requerido: true
      descripcion: "Lista de proyectos en el workspace"
      items:
        nombre:
          tipo: string
          descripcion: "Nombre del proyecto"
        contexto_archivo:
          tipo: string
          descripcion: "Ruta al contexto_proyecto_[nombre].md"
        activo:
          tipo: boolean
          descripcion: "true si es el proyecto actualmente seleccionado"

# ============================================
# ROL ACTIVO
# ============================================
rol_activo:
  descripcion: "Rol actualmente activo en la sesión"
  requerido: true
  puede_ser_null: true
  campos:
    nombre:
      tipo: string
      descripcion: "Nombre completo del rol"
      ejemplo: "ArchDev Pro"
    
    comando:
      tipo: string
      formato: "+NOMBRE"
      descripcion: "Comando de activación"
      ejemplo: "+ARCHDEV"
    
    archivo:
      tipo: string
      descripcion: "Ruta al archivo .agent.md"
      ejemplo: "personas/archdev_pro.agent.md"
    
    activado_en:
      tipo: string
      formato: ISO_8601
      descripcion: "Timestamp de activación"

# ============================================
# HISTORIAL ROLES
# ============================================
historial_roles:
  descripcion: "Historial de roles usados en la sesión"
  tipo: array
  items:
    rol:
      tipo: string
      descripcion: "Nombre del rol"
    comando:
      tipo: string
      formato: "+NOMBRE"
    timestamp_inicio:
      tipo: string
      formato: ISO_8601
    timestamp_fin:
      tipo: string_o_null
      formato: ISO_8601
      descripcion: "null si es el rol activo actual"

# ============================================
# HU ACTIVA
# ============================================
hu_activa:
  descripcion: "Historia de Usuario actualmente en foco"
  requerido: true
  puede_ser_null: true
  campos:
    id:
      tipo: string
      descripcion: "Identificador de la HU"
      ejemplo: "HU-001"
    
    titulo:
      tipo: string
      descripcion: "Título descriptivo"
    
    proyecto:
      tipo: string_o_null
      requerido: true
      descripcion: "OBLIGATORIO: null=compartida, 'nombre'=específica"
    
    tipo:
      tipo: enum
      valores: [especifica, compartida]
      descripcion: "Derivado del campo proyecto"
    
    estado:
      tipo: enum
      valores: ["[ ]", "[R]", "[A]", "[P]", "[E]", "[X]", "[B]"]
      descripcion: "Estado actual según ciclo de vida"
    
    refinamiento:
      tipo: string_o_null
      descripcion: "Ruta al archivo de refinamiento"
    
    plan:
      tipo: string_o_null
      descripcion: "Ruta al plan de implementación"
    
    ejecucion:
      tipo: string_o_null
      descripcion: "Ruta al tracking de ejecución"

# ============================================
# EJECUCIÓN ACTIVA
# ============================================
ejecucion_activa:
  descripcion: "Solo se llena cuando ejecutar_plan está en progreso"
  requerido: true
  puede_ser_null: true
  regla: "Poner null cuando finaliza la ejecución"
  campos:
    hu_id:
      tipo: string
    proyecto:
      tipo: string_o_null
      descripcion: "null=HU compartida"
    plan_archivo:
      tipo: string
    seccion_actual:
      tipo: number
      descripcion: "1-indexed"
    total_secciones:
      tipo: number
    paso_actual:
      tipo: number
    total_pasos:
      tipo: number
    progreso_porcentaje:
      tipo: number
      rango: [0, 100]
    tracking_archivo:
      tipo: string

# ============================================
# TABLERO TAREAS
# ============================================
tablero_tareas:
  descripcion: "Resumen y lista de todas las HUs"
  requerido: true
  campos:
    total:
      tipo: number
    pendientes:
      tipo: number
      descripcion: "Estado [ ]"
    en_progreso:
      tipo: number
      descripcion: "Estados [R], [A], [P], [E]"
    completadas:
      tipo: number
      descripcion: "Estado [X]"
    bloqueadas:
      tipo: number
      descripcion: "Estado [B]"
    tareas:
      tipo: array
      items:
        id:
          tipo: string
        titulo:
          tipo: string
        proyecto:
          tipo: string_o_null
          descripcion: "OBLIGATORIO: null=compartida"
        tipo:
          tipo: enum
          valores: [especifica, compartida]
        estado:
          tipo: enum
          valores: ["[ ]", "[R]", "[A]", "[P]", "[E]", "[X]", "[B]"]
        prioridad:
          tipo: enum
          valores: [alta, media, baja]
        rol_asignado:
          tipo: string_o_null
          formato: "+NOMBRE"
        rol_origen:
          tipo: string_o_null
        dependencias:
          tipo: array
          descripcion: "IDs de HUs de las que depende"
        bloqueada_por:
          tipo: array
          descripcion: "IDs de HUs que la bloquean"
        estimacion_sp:
          tipo: number_o_null
        estimacion_horas:
          tipo: number_o_null
        refinamiento_archivo:
          tipo: string_o_null
        plan_archivo:
          tipo: string_o_null
        fecha_completada:
          tipo: string_o_null
          formato: ISO_8601

# ============================================
# HERRAMIENTAS USADAS
# ============================================
herramientas_usadas:
  tipo: array
  descripcion: "Lista de nombres de herramientas ejecutadas en la sesión"
  ejemplo: ["tomar_contexto", "refinar_hu", "planificar_hu"]

# ============================================
# LOG EVENTOS CLAVE
# ============================================
log_eventos_clave:
  tipo: array
  descripcion: "Registro de eventos significativos"
  items:
    timestamp:
      tipo: string
      formato: ISO_8601
    rol:
      tipo: string
    herramienta:
      tipo: string_o_null
    tipo:
      tipo: enum
      valores:
        - sesion_iniciada
        - cambio_rol
        - herramienta_ejecutada
        - hu_refinada
        - hu_aprobada
        - hu_planificada
        - hu_en_ejecucion
        - hu_completada
        - hu_bloqueada
        - artefacto_generado
        - proyecto_agregado
        - error
    id_hu:
      tipo: string_o_null
    proyecto:
      tipo: string_o_null
    detalle:
      tipo: string

# ============================================
# METADATA
# ============================================
metadata:
  descripcion: "Estadísticas de la sesión"
  campos:
    total_cambios_rol:
      tipo: number
    sesion_iniciada:
      tipo: string
      formato: ISO_8601
    ultima_actividad:
      tipo: string
      formato: ISO_8601
      regla: "Actualizar en CADA modificación"
    roles_unicos_usados:
      tipo: array
      descripcion: "Lista de comandos +ROL usados"
    total_tareas_completadas:
      tipo: number
    total_artefactos_generados:
      tipo: number

# ============================================
# ESTADOS HU - Ciclo de Vida
# ============================================
ciclo_vida_hu:
  flujo: |
    [ ] Pendiente
      ↓ refinar_hu (+REFINADOR)
    [R] Refinada
      ↓ validar_hu (+ONAD)
    [A] Aprobada
      ↓ planificar_hu (+ONAD)
    [P] Planificada
      ↓ ejecutar_plan (+ARCHDEV)
    [E] En Ejecución
      ↓ (finaliza)
    [X] Completada
    
    [B] Bloqueada (puede ocurrir en cualquier estado)
```

---

## 📋 Esqueleto JSON

```json
{
  "version": "4.0",
  "timestamp": "",
  
  "workspace": {
    "tipo": "",
    "nombre": "",
    "workspace_archivo": null,
    "proyectos": [
      {
        "nombre": "",
        "contexto_archivo": "",
        "activo": true
      }
    ]
  },
  
  "rol_activo": {
    "nombre": "",
    "comando": "",
    "archivo": "",
    "activado_en": ""
  },
  
  "historial_roles": [],
  
  "hu_activa": null,
  
  "ejecucion_activa": null,
  
  "tablero_tareas": {
    "total": 0,
    "pendientes": 0,
    "en_progreso": 0,
    "completadas": 0,
    "bloqueadas": 0,
    "tareas": []
  },
  
  "herramientas_usadas": [],
  
  "log_eventos_clave": [],
  
  "metadata": {
    "total_cambios_rol": 0,
    "sesion_iniciada": "",
    "ultima_actividad": "",
    "roles_unicos_usados": [],
    "total_tareas_completadas": 0,
    "total_artefactos_generados": 0
  }
}
```
