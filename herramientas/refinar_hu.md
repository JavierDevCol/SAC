# 🛠️ Herramienta: Refinar Historia de Usuario

> **Versión:** 2.0  
> **Fecha de Actualización:** 10 de octubre de 2025  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `refinar_hu`

---

## 🎯 Objetivo

Analizar una Historia de Usuario (HU) y producir preguntas de clarificación, criterios de aceptación mejorados, desglose técnico vertical, estrategia y estimación justificadas para optimizar la planificación y ejecución del desarrollo de software.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`tomar_contexto`** | Al inicio del análisis (opcional) | Obtener contexto arquitectónico del proyecto para estimaciones más precisas |

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **Refinador HU** | Durante sesiones de backlog grooming | Refinar historias de usuario antes de planning poker |
| **ArchDev Pro** | Al analizar impacto técnico de features | Evaluar complejidad arquitectónica y desglose técnico |
| **Product Owner** | En preparación de sprint planning | Clarificar y mejorar criterios de aceptación |

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Texto completo de la Historia de Usuario a refinar
- Criterios de aceptación actuales (si existen)

**Secundario (Opcional):**
- Contexto arquitectónico del proyecto (archivo `artefactos/contexto_proyecto.md`)
- Restricciones no funcionales conocidas (performance, seguridad, usabilidad)
- Dependencias técnicas o de negocio identificadas
- Backlog del proyecto para detectar historias relacionadas
- Definición de "Terminado" (Definition of Done) del equipo
- Métricas históricas de estimación del equipo

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `formato_estimacion` | string | story_points\|horas\|ambos | story_points | Tipo de estimación a generar |
| `nivel_detalle` | string | alto\|medio\|bajo | medio | Profundidad del análisis y desglose técnico |
| `incluir_riesgos` | boolean | true\|false | true | Analizar e incluir riesgos y dependencias |
| `generar_tareas` | boolean | true\|false | true | Crear desglose técnico en tareas específicas |
| `enfoque_estimacion` | string | conservador\|optimista\|realista | realista | Sesgo aplicado a las estimaciones |
| `incluir_testing` | boolean | true\|false | true | Incluir consideraciones y tareas de testing |

---

## 👥 Roles Autorizados

- ✅ **Refinador HU** (uso principal - especialista en análisis de historias de usuario)
- ✅ **ArchDev Pro** (refinamiento técnico y estimación de complejidad arquitectónica)
- ✅ **Arquitecto DevOps** *(solo para evaluar impacto en infraestructura)*

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Configuración Inicial y Selección de Modo

- **Presentar opciones de ejecución al usuario:**
  - **Modo Automático (Default):** Ejecutar refinamiento con configuración estándar optimizada
  - **Modo Personalizado:** Configurar parámetros específicos según necesidades del proyecto

- **Si elige Modo Automático, aplicar configuración por defecto:**
  ```
  ⚙️ Configuración Automática del Refinamiento:
  - formato_estimacion: story_points ✓
  - nivel_detalle: medio ✓
  - incluir_riesgos: true ✓
  - generar_tareas: true ✓
  - enfoque_estimacion: realista ✓
  - incluir_testing: true ✓
  
  ✨ Iniciando refinamiento con configuración optimizada...
  ```

- **Si elige Modo Personalizado, mostrar configuración disponible:**
  ```
  🔧 Configuración Personalizada del Refinamiento:
  
  📊 Formato de estimación:
  • story_points (recomendado para equipos ágiles) ← por defecto
  • horas (para equipos con tracking de tiempo)
  • ambos (estimación dual)
  
  📋 Nivel de detalle:
  • medio (análisis estándar - 30min) ← por defecto
  • bajo (overview rápido - 15min), alto (análisis exhaustivo - 60min)
  
  ⚠️ Incluir análisis de riesgos: true ← por defecto
  📝 Generar desglose en tareas: true ← por defecto
  
  🎯 Enfoque de estimación:
  • realista (estimación balanceada) ← por defecto
  • conservador (buffer adicional), optimista (estimación mínima)
  
  🧪 Incluir consideraciones de testing: true ← por defecto
  ```

### 2️⃣ Análisis Inicial de la Historia de Usuario

- **Evaluación de calidad y completitud:**
  - Verificar que sigue formato estándar: "Como [rol] quiero [funcionalidad] para [beneficio]"
  - Detectar ambigüedades en la redacción de la historia
  - Identificar lagunas de información o contexto faltante
  - Evaluar criterios de aceptación existentes (medibles vs no medibles)

- **Clasificación del tipo de Historia de Usuario:**
  - **Feature:** Nueva funcionalidad para el usuario final
  - **Technical Story:** Mejora técnica o refactoring
  - **Bug Fix:** Corrección de defectos existentes
  - **Spike:** Investigación o prototipo para reducir incertidumbre
  - **Debt:** Pago de deuda técnica acumulada

### 3️⃣ Generación de Preguntas de Clarificación

- **Identificar aspectos ambiguos o incompletos:**
  - Casos de uso específicos no cubiertos
  - Flujos alternativos y excepciones
  - Reglas de negocio implícitas que deben hacerse explícitas
  - Validaciones y restricciones no especificadas

- **Priorizar preguntas por impacto:**
  - **Alta prioridad:** Afectan la estimación o implementación técnica
  - **Media prioridad:** Mejoran la experiencia de usuario o claridad
  - **Baja prioridad:** Detalles de implementación específicos

### 4️⃣ Refinamiento de Criterios de Aceptación

- **Aplicar criterios SMART a cada criterio existente:**
  - **Específico:** Definir exactamente qué debe ocurrir
  - **Medible:** Establecer métricas o condiciones verificables
  - **Alcanzable:** Realista dentro del scope del sprint
  - **Relevante:** Directamente relacionado con el objetivo de la HU
  - **Temporal:** Con plazos o condiciones de tiempo específicas

- **Generar criterios adicionales faltantes:**
  - Casos de error y manejo de excepciones
  - Comportamiento de la interfaz de usuario
  - Validaciones de datos y reglas de negocio
  - Criterios de performance cuando aplique

### 5️⃣ Desglose Técnico Vertical (Vertical Slicing)

- **Identificar slices end-to-end mínimos:**
  - **Frontend:** Componentes de UI, validaciones, navegación
  - **API:** Endpoints REST, validación de entrada, respuestas
  - **Servicio:** Lógica de negocio, validaciones, transformaciones
  - **Persistencia:** Modelos de datos, queries, migrations
  - **Testing:** Unit tests, integration tests, acceptance tests

- **Generar tareas específicas por slice (si `generar_tareas=true`):**
  - Asignar identificadores únicos sugeridos (ej: HU-123-UI-01)
  - Definir dependencias entre tareas
  - Estimar esfuerzo individual por tarea
  - Identificar paralelización posible

### 6️⃣ Estrategia de Implementación y Estimación

- **Recomendar enfoque de desarrollo:**
  - **TDD (Test-Driven Development):** Para lógica compleja o crítica
  - **Incremental:** Desarrollo por capas o funcionalidades
  - **Feature Toggle:** Para releases graduales o A/B testing
  - **Spike primero:** Si hay alta incertidumbre técnica

- **Calcular estimación justificada:**
  - **Complejidad técnica:** Basada en el stack y arquitectura
  - **Incertidumbre:** Factor de riesgo por áreas desconocidas
  - **Riesgo:** Dependencias externas, integraciones, nuevas tecnologías
  - **Testing:** Tiempo adicional para pruebas automatizadas y manuales

### 7️⃣ Análisis de Riesgos y Dependencias (si `incluir_riesgos=true`)

- **Identificar bloqueadores potenciales:**
  - Dependencias de otras historias o equipos
  - Integraciones con sistemas externos
  - Requisitos de infraestructura o DevOps
  - Decisiones de arquitectura pendientes

- **Proponer estrategias de mitigación:**
  - Paralelización de tareas independientes
  - Desarrollo de mocks o simuladores
  - Escalación temprana de dependencias
  - Planes B para riesgos técnicos

### 8️⃣ Finalización y Entrega Estructurada

- **Consolidar todo el análisis en formato estructurado**
- **Validar consistencia entre estimación y desglose técnico**
- **Generar recomendaciones para próximos pasos**
- **Destacar elementos que requieren validación con Product Owner**

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Historia de Usuario mal formateada o incompleta | Marcar como severidad alta y priorizar preguntas de clarificación para estructura básica |
| Falta completamente de criterios de aceptación | Generar criterios básicos inferidos y solicitar validación urgente con Product Owner |
| Historia demasiado amplia (epic-sized) | Sugerir partición en historias hijas más manejables con estimación individual |
| Dependencias críticas no resolubles en el sprint | Recomendar diferir la historia hasta resolver dependencias o redefinir scope |
| Alta incertidumbre técnica (>50% de la estimación) | Sugerir spike técnico previo para reducir riesgo antes de implementación |
| Conflicto con restricciones arquitectónicas | Escalar al Arquitecto y proponer alternativas técnicas viables |
| Criterios de aceptación no medibles o ambiguos | Reformular usando métricas específicas y condiciones verificables |
| Estimación excede capacidad típica del sprint | Analizar posibilidad de reducir scope o dividir en múltiples sprints |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Análisis estructurado de la Historia de Usuario con refinamiento completo
- Desglose técnico actionable y estimación justificada

**Estructura del output:**
```
# 📋 Refinamiento de Historia de Usuario: [Título de la HU]

## 1️⃣ Preguntas de Clarificación

### Alta Prioridad (Críticas para la implementación)
- [Pregunta específica sobre aspecto técnico o de negocio]
- [Pregunta sobre casos de uso no cubiertos]

### Media Prioridad (Mejoran la definición)
- [Preguntas sobre experiencia de usuario]
- [Preguntas sobre validaciones específicas]

### Baja Prioridad (Detalles de implementación)
- [Preguntas sobre aspectos menores]

## 2️⃣ Criterios de Aceptación Refinados

### Criterios Existentes Mejorados
- ✅ [Criterio original] → [Versión SMART mejorada]
- ⚠️ [Criterio problemático] → [Sugerencia de mejora]

### Criterios Adicionales Propuestos
- [Nuevo criterio para casos de error]
- [Nuevo criterio para validaciones]
- [Nuevo criterio para performance]

## 3️⃣ Desglose Técnico (Vertical Slicing)

### Slice 1: [Funcionalidad Core]
- **Frontend:** [HU-123-UI-01] Crear componente de [descripción] (3h)
- **API:** [HU-123-API-01] Implementar endpoint POST /[recurso] (5h)
- **Servicio:** [HU-123-SRV-01] Lógica de [proceso de negocio] (8h)
- **Persistencia:** [HU-123-DB-01] Modelo de datos y migration (2h)
- **Testing:** [HU-123-TEST-01] Tests unitarios e integración (5h)

### Slice 2: [Validaciones y Error Handling]
[Similar estructura]

## 4️⃣ Estrategia y Estimación

### Enfoque Recomendado
- **Metodología:** TDD para lógica crítica + desarrollo incremental
- **Orden de implementación:** Persistencia → Servicio → API → Frontend
- **Consideraciones especiales:** [Feature toggle, integración gradual, etc.]

### Estimación Detallada
- **Desarrollo:** 23 Story Points (38 horas)
- **Testing:** 8 Story Points (13 horas)
- **Buffer de riesgo:** 5 Story Points (8 horas)
- **Total:** 36 Story Points (59 horas)

### Justificación de la Estimación
- **Complejidad técnica:** Media (integración con sistema existente)
- **Incertidumbre:** Baja (tecnologías conocidas)
- **Riesgo:** Medio (dependencia de API externa)

## 5️⃣ Riesgos y Mitigaciones

### Riesgos Identificados
- **Alto:** Dependencia de API externa inestable
  - *Mitigación:* Desarrollar mock service + circuit breaker
- **Medio:** Cambios en el modelo de datos
  - *Mitigación:* Validar esquema con DBA antes de sprint

### Dependencias Críticas
- [HU-120] debe completarse antes (servicio de autenticación)
- Configuración de environment de testing pendiente

## 6️⃣ Observaciones y Próximos Pasos

### Recomendaciones
- Validar wireframes con UX antes de comenzar desarrollo
- Coordinar con equipo de DevOps para deployment strategy
- Considerar impacto en performance con volumen esperado

### Elementos Pendientes de Definir
- Reglas específicas de validación de [campo X]
- Comportamiento esperado en caso de timeout de API externa
```

**Notificación de confirmación:**
- Resumen de la estimación total y nivel de confianza
- Lista de elementos que requieren validación con Product Owner
- Próximos pasos sugeridos para la planificación del sprint

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/refinar_hu_ejemplo.md`

---

## 📚 Referencias y Notas

### Metodologías y Frameworks de Referencia

**Gestión de Producto:**
- **User Story Mapping:** Técnica de Jeff Patton para organización de historias
- **INVEST Criteria:** Criterios de calidad para historias de usuario (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- **Three Cs:** Card, Conversation, Confirmation framework

**Técnicas de Estimación:**
- **Planning Poker:** Para estimación colaborativa en Story Points
- **T-Shirt Sizing:** Para estimación rápida de épicas o features grandes
- **Monte Carlo Simulation:** Para proyección de timelines con incertidumbre

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `tomar_contexto` - Proporciona contexto arquitectónico para estimaciones más precisas
- `define_arquitectura` - Para validar impacto arquitectónico de historias grandes
- `crear_pruebas` - Para implementar estrategia de testing definida en el refinamiento
- `generar_adr` - Para documentar decisiones arquitectónicas derivadas del análisis

**Herramientas externas compatibles:**
- **Jira/Azure DevOps:** Para gestión de backlog y tracking de historias
- **Confluence/Notion:** Para documentación de contexto y decisiones
- **Miro/Figma:** Para story mapping y colaboración visual
- **TestRail/Xray:** Para gestión de casos de prueba derivados de criterios

### Patrones de Historias de Usuario

**Tipos de historia por dominio:**
- **CRUD Operations:** Create, Read, Update, Delete de entidades
- **Workflow Stories:** Procesos de negocio multi-paso
- **Integration Stories:** Conexión con sistemas externos
- **Report/Analytics:** Generación de información y métricas
- **Security Stories:** Autenticación, autorización, auditoría

**Anti-patrones comunes:**
- **Technical Tasks disguised as User Stories:** Tareas técnicas sin valor de usuario
- **Epic-sized Stories:** Historias demasiado grandes para un sprint
- **Implementation Details:** Historias que especifican solución técnica en lugar de necesidad
- **Dependent Stories:** Historias que no pueden implementarse independientemente

### Limitaciones Conocidas

- **Contexto de negocio:** No reemplaza la conversación con Product Owner y stakeholders
- **Estimación precisa:** Las estimaciones son aproximaciones basadas en información disponible
- **Dinámicas de equipo:** No considera velocidad específica o skills del equipo asignado
- **Priorización:** No determina prioridad de backlog, solo refina contenido
- **Acceptance Testing:** No genera casos de prueba automatizados, solo criterios

### Casos de Uso por Tipo de Proyecto

**Proyectos Ágiles/Scrum:**
- Refinamiento de backlog en sesiones de grooming
- Preparación de historias para planning poker
- Análisis de dependencias entre sprints

**Proyectos de Producto:**
- Validación de market fit a través de criterios medibles
- Planificación de MVPs con desglose incremental
- Análisis de impacto en métricas de usuario

**Proyectos Enterprise:**
- Análisis de impacto en sistemas legacy
- Consideraciones de compliance y auditoría
- Gestión de dependencias inter-equipos

### Futuras Mejoras

**Análisis automatizado:**
- **NLP Analysis:** Procesamiento de lenguaje natural para detectar ambigüedades
- **Pattern Recognition:** Identificación automática de tipos de historia
- **Estimation ML:** Machine learning basado en histórico de estimaciones del equipo

**Integración avanzada:**
- **Repository Analysis:** Análisis de código para estimar complejidad técnica
- **API Documentation:** Generación automática de criterios basada en contratos
- **Test Case Generation:** Creación automática de casos de prueba desde criterios