#  Estructura del Archivo `session_state.json`

Este documento describe la estructura completa del archivo `session_state.json` utilizado por el Sistema Cochas para mantener el estado de la sesión, tracking de tareas y contexto entre roles.

---

##  Estructura Base (Esqueleto)

```json
{
  "version": "string (ej: '2.0')",
  "timestamp": "string ISO 8601 (ej: '2025-10-13T10:30:00Z')",
  
  "proyecto": {
    "nombre": "string",
    "descripcion": "string",
    "fase_actual": "string (Diseño|Implementación|Testing|Deploy)"
  },
  
  "rol_activo": {
    "nombre": "string",
    "comando": "string",
    "archivo": "string (ruta relativa)",
    "activado_en": "string ISO 8601",
    "contexto_heredado_de": "string | null"
  },
  
  "estado_contexto_proyecto": "string (NO_INICIALIZADO|INICIALIZADO)",
  "contexto_proyecto_archivo": "string (ruta relativa)",
  
  "historial_roles": [
    {
      "rol": "string",
      "comando": "string",
      "timestamp_inicio": "string ISO 8601",
      "timestamp_fin": "string ISO 8601 | null",
      "duracion_minutos": "number | null",
      
      "tareas_completadas": [
        {
          "id": "string (formato: ROL-NNN)",
          "descripcion": "string",
          "estado": "string (completada)",
          "timestamp_inicio": "string ISO 8601",
          "timestamp_fin": "string ISO 8601",
          "duracion_minutos": "number",
          
          "contexto_tarea": {
            "objetivo": "string",
            "decisiones_clave": ["array de strings"],
            "trade_offs_evaluados": [
              {
                "alternativa_1": "string",
                "alternativa_2": "string",
                "decision": "string",
                "justificacion": "string"
              }
            ],
            "riesgos_identificados": [
              {
                "riesgo": "string",
                "severidad": "string (alta|media|baja)",
                "mitigacion": "string"
              }
            ],
            "artefactos_generados": [
              {
                "archivo": "string (ruta relativa)",
                "tipo": "string (documentacion|codigo|diagrama|adr|config|resumen_usuario)",
                "descripcion": "string"
              }
            ],
            "herramientas_utilizadas": [
              {
                "nombre": "string",
                "timestamp": "string ISO 8601",
                "resultado": "string"
              }
            ]
          },
          
          "tareas_generadas_para_siguiente_rol": [
            {
              "id": "string (formato: ROL-NNN)",
              "descripcion": "string",
              "prioridad": "string (alta|media|baja)",
              "estado": "string (pendiente)",
              "dependencias": ["array de strings (IDs de tareas)"],
              "estimacion_horas": "number",
              "criterios_aceptacion": ["array de strings"]
            }
          ]
        }
      ],
      
      "tareas_heredadas": [
        {
          "id": "string",
          "origen": "string (nombre del rol origen)",
          "estado": "string (pendiente|en_progreso|completada)",
          "timestamp_inicio": "string ISO 8601 | null"
        }
      ],
      
      "resumen_rol": {
        "total_tareas_completadas": "number",
        "total_decisiones_clave": "number",
        "total_artefactos_generados": "number",
        "total_tareas_generadas": "number",
        "tareas_pendientes": "number",
        "tareas_en_progreso": "number",
        "progreso_porcentaje": "number"
      }
    }
  ],
  
  "tablero_tareas": {
    "total_tareas": "number",
    "pendientes": "number",
    "en_progreso": "number",
    "completadas": "number",
    "bloqueadas": "number",
    
    "tareas": [
      {
        "id": "string",
        "descripcion": "string",
        "estado": "string (pendiente|en_progreso|completada|bloqueada)",
        "prioridad": "string (alta|media|baja)",
        "rol_asignado": "string",
        "rol_origen": "string",
        "herramienta_sugerida": "string | null",
        "dependencias": ["array de strings"],
        "bloqueada_por": ["array de strings"],
        "estimacion_horas": "number",
        "criterios_aceptacion": ["array de strings"],
        "asignacion_automatica": "boolean",
        "score_compatibilidad": "number (0-1) | null",
        "completada_por": "string | null",
        "timestamp_completada": "string ISO 8601 | null",
        "progreso_notas": [
          {
            "timestamp": "string ISO 8601",
            "nota": "string"
          }
        ]
      }
    ]
  },
  
  "memoria_conversacion": {
    "decisiones_arquitectonicas": [
      {
        "timestamp": "string ISO 8601",
        "rol": "string",
        "decision": "string",
        "justificacion": "string",
        "impacto": "string",
        "documentado_en": "string (ruta relativa) | null"
      }
    ],
    "problemas_identificados": [
      {
        "timestamp": "string ISO 8601",
        "rol": "string",
        "problema": "string",
        "severidad": "string (alta|media|baja)",
        "solucion_propuesta": "string",
        "estado": "string (identificado|en_progreso|resuelto)"
      }
    ],
    "contexto_global": {
      "proyecto": "string",
      "fase_actual": "string",
      "restricciones": ["array de strings"],
      "objetivos_sesion": ["array de strings"]
    }
  },
  
  "herramientas_usadas": ["array de strings (nombres de herramientas)"],
  
  "log_eventos_clave": [
    {
      "timestamp": "string ISO 8601",
      "rol": "string",
      "tipo": "string (sesion_iniciada|herramienta|decision|tarea_completada|tarea_iniciada|cambio_rol|contexto_heredado|resumen_generado|archivo_creado)",
      "detalle": "string"
    }
  ],
  
  "metadata": {
    "total_cambios_rol": "number",
    "sesion_iniciada": "string ISO 8601",
    "ultima_actividad": "string ISO 8601",
    "roles_unicos_usados": ["array de strings"],
    "total_tareas_completadas": "number",
    "total_tareas_pendientes": "number",
    "total_tareas_en_progreso": "number",
    "total_artefactos_generados": "number",
    "total_decisiones_documentadas": "number"
  }
}
```

---

##  Ejemplo Sencillo (Sesión con 2 Roles)

```json
{
  "version": "2.0",
  "timestamp": "2025-10-13T11:00:00Z",
  
  "proyecto": {
    "nombre": "Sistema de Tareas",
    "descripcion": "Aplicación web para gestión de tareas",
    "fase_actual": "Implementación"
  },
  
  "rol_activo": {
    "nombre": "ArchDev Pro",
    "comando": "archdev",
    "archivo": "personas/archdev_pro.md",
    "activado_en": "2025-10-13T10:30:00Z",
    "contexto_heredado_de": "onad"
  },
  
  "estado_contexto_proyecto": "INICIALIZADO",
  "contexto_proyecto_archivo": "artefactos/contexto_proyecto.md",
  
  "historial_roles": [
    {
      "rol": "onad",
      "comando": "onad",
      "timestamp_inicio": "2025-10-13T10:00:00Z",
      "timestamp_fin": "2025-10-13T10:30:00Z",
      "duracion_minutos": 30,
      
      "tareas_completadas": [
        {
          "id": "ONAD-001",
          "descripcion": "Diseñar arquitectura REST para gestión de tareas",
          "estado": "completada",
          "timestamp_inicio": "2025-10-13T10:05:00Z",
          "timestamp_fin": "2025-10-13T10:28:00Z",
          "duracion_minutos": 23,
          
          "contexto_tarea": {
            "objetivo": "Diseñar API REST escalable para CRUD de tareas",
            "decisiones_clave": [
              "API REST con Spring Boot",
              "Base de datos PostgreSQL",
              "Autenticación con JWT"
            ],
            "trade_offs_evaluados": [
              {
                "alternativa_1": "Monolito",
                "alternativa_2": "Microservicios",
                "decision": "Monolito",
                "justificacion": "MVP con equipo pequeño, no justifica complejidad de microservicios"
              }
            ],
            "riesgos_identificados": [
              {
                "riesgo": "Escalabilidad limitada a largo plazo",
                "severidad": "media",
                "mitigacion": "Arquitectura hexagonal permite migración futura"
              }
            ],
            "artefactos_generados": [
              {
                "archivo": "artefactos/arquitectura_api_tareas.md",
                "tipo": "documentacion",
                "descripcion": "Diseño de API REST con endpoints y modelos"
              }
            ],
            "herramientas_utilizadas": [
              {
                "nombre": "tomar_contexto",
                "timestamp": "2025-10-13T10:05:00Z",
                "resultado": "Contexto del proyecto inicializado"
              },
              {
                "nombre": "define_arquitectura",
                "timestamp": "2025-10-13T10:15:00Z",
                "resultado": "Arquitectura REST definida"
              }
            ]
          },
          
          "tareas_generadas_para_siguiente_rol": [
            {
              "id": "ARCHDEV-001",
              "descripcion": "Implementar modelo Task con validaciones",
              "prioridad": "alta",
              "estado": "pendiente",
              "dependencias": [],
              "estimacion_horas": 4,
              "criterios_aceptacion": [
                "Modelo Task con JPA",
                "Validaciones con Bean Validation",
                "Tests unitarios"
              ]
            },
            {
              "id": "ARCHDEV-002",
              "descripcion": "Implementar TaskController con CRUD completo",
              "prioridad": "alta",
              "estado": "pendiente",
              "dependencias": ["ARCHDEV-001"],
              "estimacion_horas": 6,
              "criterios_aceptacion": [
                "Endpoints: GET, POST, PUT, DELETE",
                "Manejo de errores con @ControllerAdvice",
                "Tests de integración"
              ]
            }
          ]
        }
      ],
      
      "tareas_heredadas": [],
      
      "resumen_rol": {
        "total_tareas_completadas": 1,
        "total_decisiones_clave": 3,
        "total_artefactos_generados": 1,
        "total_tareas_generadas": 2
      }
    },
    {
      "rol": "archdev",
      "comando": "archdev",
      "timestamp_inicio": "2025-10-13T10:30:00Z",
      "timestamp_fin": null,
      "duracion_minutos": null,
      
      "tareas_completadas": [],
      
      "tareas_heredadas": [
        {
          "id": "ARCHDEV-001",
          "origen": "onad",
          "estado": "en_progreso",
          "timestamp_inicio": "2025-10-13T10:35:00Z"
        },
        {
          "id": "ARCHDEV-002",
          "origen": "onad",
          "estado": "pendiente",
          "timestamp_inicio": null
        }
      ],
      
      "resumen_rol": {
        "tareas_pendientes": 1,
        "tareas_en_progreso": 1,
        "tareas_completadas": 0,
        "progreso_porcentaje": 0
      }
    }
  ],
  
  "tablero_tareas": {
    "total_tareas": 2,
    "pendientes": 1,
    "en_progreso": 1,
    "completadas": 0,
    "bloqueadas": 0,
    
    "tareas": [
      {
        "id": "ARCHDEV-001",
        "descripcion": "Implementar modelo Task con validaciones",
        "estado": "en_progreso",
        "prioridad": "alta",
        "rol_asignado": "archdev",
        "rol_origen": "onad",
        "herramienta_sugerida": null,
        "dependencias": [],
        "bloqueada_por": [],
        "estimacion_horas": 4,
        "criterios_aceptacion": [
          "Modelo Task con JPA",
          "Validaciones con Bean Validation",
          "Tests unitarios"
        ],
        "asignacion_automatica": false,
        "score_compatibilidad": null,
        "completada_por": null,
        "timestamp_completada": null,
        "progreso_notas": [
          {
            "timestamp": "2025-10-13T10:35:00Z",
            "nota": "Iniciada implementación del modelo Task"
          }
        ]
      },
      {
        "id": "ARCHDEV-002",
        "descripcion": "Implementar TaskController con CRUD completo",
        "estado": "pendiente",
        "prioridad": "alta",
        "rol_asignado": "archdev",
        "rol_origen": "onad",
        "herramienta_sugerida": null,
        "dependencias": ["ARCHDEV-001"],
        "bloqueada_por": ["ARCHDEV-001"],
        "estimacion_horas": 6,
        "criterios_aceptacion": [
          "Endpoints: GET, POST, PUT, DELETE",
          "Manejo de errores con @ControllerAdvice",
          "Tests de integración"
        ],
        "asignacion_automatica": false,
        "score_compatibilidad": null,
        "completada_por": null,
        "timestamp_completada": null,
        "progreso_notas": []
      }
    ]
  },
  
  "memoria_conversacion": {
    "decisiones_arquitectonicas": [
      {
        "timestamp": "2025-10-13T10:15:00Z",
        "rol": "onad",
        "decision": "API REST monolítica con Spring Boot",
        "justificacion": "MVP con equipo pequeño, simplicidad sobre escalabilidad prematura",
        "impacto": "Toda la arquitectura del sistema",
        "documentado_en": "artefactos/arquitectura_api_tareas.md"
      }
    ],
    "problemas_identificados": [],
    "contexto_global": {
      "proyecto": "Sistema de Tareas",
      "fase_actual": "Implementación",
      "restricciones": [
        "Equipo de 2 desarrolladores",
        "Lanzamiento en 1 mes"
      ],
      "objetivos_sesion": [
        "Diseñar arquitectura base",
        "Implementar modelos y controladores"
      ]
    }
  },
  
  "herramientas_usadas": ["tomar_contexto", "define_arquitectura"],
  
  "log_eventos_clave": [
    {
      "timestamp": "2025-10-13T10:00:00Z",
      "rol": "orquestador",
      "tipo": "sesion_iniciada",
      "detalle": "Nueva sesión iniciada"
    },
    {
      "timestamp": "2025-10-13T10:05:00Z",
      "rol": "onad",
      "tipo": "herramienta",
      "detalle": "tomar_contexto ejecutado"
    },
    {
      "timestamp": "2025-10-13T10:15:00Z",
      "rol": "onad",
      "tipo": "herramienta",
      "detalle": "define_arquitectura ejecutado"
    },
    {
      "timestamp": "2025-10-13T10:15:00Z",
      "rol": "onad",
      "tipo": "decision",
      "detalle": "Arquitectura REST monolítica aprobada"
    },
    {
      "timestamp": "2025-10-13T10:28:00Z",
      "rol": "onad",
      "tipo": "tarea_completada",
      "detalle": "ONAD-001 completada"
    },
    {
      "timestamp": "2025-10-13T10:30:00Z",
      "rol": "orquestador",
      "tipo": "cambio_rol",
      "detalle": "onad  archdev"
    },
    {
      "timestamp": "2025-10-13T10:30:00Z",
      "rol": "archdev",
      "tipo": "contexto_heredado",
      "detalle": "2 tareas heredadas de onad"
    },
    {
      "timestamp": "2025-10-13T10:35:00Z",
      "rol": "archdev",
      "tipo": "tarea_iniciada",
      "detalle": "ARCHDEV-001 iniciada"
    }
  ],
  
  "metadata": {
    "total_cambios_rol": 1,
    "sesion_iniciada": "2025-10-13T10:00:00Z",
    "ultima_actividad": "2025-10-13T10:35:00Z",
    "roles_unicos_usados": ["onad", "archdev"],
    "total_tareas_completadas": 1,
    "total_tareas_pendientes": 1,
    "total_tareas_en_progreso": 1,
    "total_artefactos_generados": 1,
    "total_decisiones_documentadas": 1
  }
}
```

---


- **Plantilla de Resumen:** `/plantillas/resumen_sesion_plantilla.md`
- **Core del Orquestador:** `/core-cochas.md`
- **Herramienta de Asignación:** `/herramientas/asignar_responsable.md`
