# 🛠️ Herramientas Potenciales para Refinador HU

> Documento de análisis y especificación de herramientas potenciales identificadas durante la refactorización del rol **Refinador HU**. Este documento sirve como referencia para futuras implementaciones o refactorizaciones de herramientas existentes.

---

## 📋 Índice

1. [Herramienta 1: `validar_criterios_aceptacion` (NUEVA)](#1-validar_criterios_aceptacion)
2. [Herramienta 2: `estimar_complejidad_hu` (NUEVA)](#2-estimar_complejidad_hu)
3. [Mejora a herramienta existente: `refinar_hu`](#3-mejora-refinar_hu)

---

## 1. `validar_criterios_aceptacion`

### 🎯 Propósito

Validar automáticamente que los Criterios de Aceptación sean SMART (Específicos, Medibles, Alcanzables, Relevantes, Temporales), detectar ambigüedades y sugerir reformulaciones para hacerlos testeables.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es crítico para mantener el principio cardinal "Claridad Sobre Velocidad" del Refinador HU.

### 🔍 Problema que Resuelve

- **Antes:** El Refinador debe analizar manualmente cada CA buscando ambigüedades
- **Después:** La herramienta detecta automáticamente CA problemáticos y propone mejoras

### 📥 Input Esperado

**Parámetros:**
- `criterios_aceptacion` (array, requerido): Lista de CA en texto plano
  ```json
  [
    "El usuario puede agregar productos",
    "El carrito debe guardar los productos",
    "El usuario debe ver la cantidad de productos"
  ]
  ```
- `contexto_hu` (object, opcional): Contexto de la HU para validaciones contextuales
  ```json
  {
    "titulo": "Agregar productos al carrito",
    "rol_usuario": "usuario registrado",
    "dominio": "e-commerce"
  }
  ```

### 📤 Output Esperado

**Formato: JSON con análisis detallado por CA**

```json
{
  "validacion_completada": true,
  "score_global": 45,
  "nivel_calidad": "BAJO",
  "criterios_analizados": 3,
  "criterios_validos": 0,
  "criterios_ambiguos": 3,
  "analisis_por_criterio": [
    {
      "indice": 1,
      "ca_original": "El usuario puede agregar productos",
      "es_valido": false,
      "score_smart": 20,
      "problemas_detectados": [
        {
          "tipo": "NO_MEDIBLE",
          "severidad": "CRITICA",
          "descripcion": "No especifica cómo se mide el éxito de la acción",
          "pregunta_sugerida": "¿Qué debe ocurrir exactamente cuando el usuario agrega un producto? ¿Debe ver una confirmación? ¿Se incrementa un contador?"
        },
        {
          "tipo": "AMBIGUO",
          "severidad": "ALTA",
          "descripcion": "No especifica el flujo completo (acción → resultado esperado)",
          "pregunta_sugerida": "¿El usuario puede agregar el mismo producto múltiples veces? ¿Hay límite de cantidad?"
        },
        {
          "tipo": "NO_TESTEABLE",
          "severidad": "CRITICA",
          "descripcion": "No hay condición observable que permita automatizar una prueba",
          "sugerencia": "Reformular usando formato Given-When-Then"
        }
      ],
      "ca_mejorado_sugerido": "Dado que el usuario está autenticado y visualiza un producto con stock disponible, cuando hace clic en 'Agregar al carrito', entonces el producto se añade al carrito con cantidad 1, el contador del header se incrementa y se muestra la notificación 'Producto agregado al carrito'",
      "justificacion_mejora": "Esta versión es SMART porque: (1) Es Específico: define claramente la acción y el contexto, (2) Es Medible: se puede verificar el contador y la notificación, (3) Es Testeable: cada condición es observable en una prueba automatizada"
    },
    {
      "indice": 2,
      "ca_original": "El carrito debe guardar los productos",
      "es_valido": false,
      "score_smart": 30,
      "problemas_detectados": [
        {
          "tipo": "NO_ESPECIFICO",
          "severidad": "ALTA",
          "descripcion": "No especifica CUÁNDO o POR CUÁNTO TIEMPO debe guardar",
          "pregunta_sugerida": "¿El carrito persiste entre sesiones? ¿Por cuánto tiempo se mantienen los productos?"
        },
        {
          "tipo": "VERBO_PASIVO",
          "severidad": "MEDIA",
          "descripcion": "Usa 'debe' en lugar de un flujo testeable",
          "sugerencia": "Reformular con flujo activo: Dado X, Cuando Y, Entonces Z"
        }
      ],
      "ca_mejorado_sugerido": "Dado que el usuario tiene productos en su carrito, cuando cierra sesión y vuelve a iniciar sesión en menos de 7 días, entonces el carrito mantiene todos los productos agregados con sus cantidades",
      "justificacion_mejora": "Define claramente el tiempo de persistencia (7 días) y el comportamiento esperado en un escenario testeable"
    },
    {
      "indice": 3,
      "ca_original": "El usuario debe ver la cantidad de productos",
      "es_valido": false,
      "score_smart": 35,
      "problemas_detectados": [
        {
          "tipo": "NO_ESPECIFICO",
          "severidad": "ALTA",
          "descripcion": "No especifica DÓNDE debe ver la cantidad",
          "pregunta_sugerida": "¿Dónde se muestra la cantidad: en el header, en la página del carrito, en ambos lugares?"
        },
        {
          "tipo": "AMBIGUO",
          "severidad": "MEDIA",
          "descripcion": "No especifica si es cantidad total o por producto individual",
          "pregunta_sugerida": "¿Es la cantidad total de productos o la cantidad de cada producto individual?"
        }
      ],
      "ca_mejorado_sugerido": "Dado que el usuario tiene N productos en su carrito, cuando visualiza el header de la aplicación, entonces ve un badge con el número N junto al ícono del carrito",
      "justificacion_mejora": "Especifica la ubicación exacta (header), el elemento UI (badge), y la información mostrada (número total)"
    }
  ],
  "recomendaciones_generales": [
    "Todos los CA deberían reformularse en formato Given-When-Then para máxima claridad",
    "Ningún CA actual es testeable automáticamente. Se recomienda añadir condiciones observables",
    "Los CA están enfocados en capacidades técnicas, no en valor de negocio. Considerar añadir el 'Para qué' (beneficio)"
  ],
  "preguntas_criticas_pendientes": [
    "¿El carrito debe persistir entre sesiones?",
    "¿Hay límite de cantidad por producto?",
    "¿Qué ocurre si el producto se queda sin stock después de agregarlo al carrito?",
    "¿El usuario puede tener múltiples carritos o solo uno activo?"
  ]
}
```

### 🔧 Lógica Interna Sugerida

**Fase 1: Análisis Semántico**
1. **Detectar palabras clave problemáticas:**
   - "debe", "puede", "debería" → Verbos pasivos, no testeables
   - "rápido", "fácil", "intuitivo" → Subjetivos, no medibles
   - "correctamente", "adecuadamente" → Ambiguos sin definición

2. **Verificar estructura SMART:**
   - **Específico:** ¿Define claramente quién, qué, dónde, cuándo?
   - **Medible:** ¿Tiene condiciones observables o umbrales numéricos?
   - **Alcanzable:** ¿Es técnicamente factible? (requiere contexto)
   - **Relevante:** ¿Relacionado con el valor de negocio de la HU?
   - **Temporal:** ¿Define timeouts, duraciones, límites temporales si aplica?

3. **Validar formato Given-When-Then:**
   - ¿Tiene precondiciones claras (Given)?
   - ¿Define la acción explícitamente (When)?
   - ¿Especifica resultado observable (Then)?

**Fase 2: Generación de Mejoras**
1. **Aplicar plantillas de reformulación:**
   - Template básico: "Dado que [contexto], cuando [acción], entonces [resultado observable]"
   - Template con validación: "... y [validación adicional]"
   - Template con excepciones: "... pero si [condición] entonces [resultado alternativo]"

2. **Sugerir preguntas de clarificación** según problemas detectados

3. **Calcular score SMART** (0-100) basado en:
   - Presencia de cada criterio SMART: 20 puntos cada uno
   - Bonificación por formato Given-When-Then: +10 puntos
   - Penalización por palabras problemáticas: -5 puntos cada una

**Fase 3: Priorización**
- Ordenar CA por severidad de problemas (CRITICA > ALTA > MEDIA)
- Identificar preguntas críticas que bloquean el refinamiento

### 🎭 Comportamiento Esperado del Rol Refinador HU

**Con esta herramienta:**
```markdown
Usuario: [Proporciona HU con CA ambiguos]

Refinador: "Voy a validar la calidad de tus Criterios de Aceptación..."

[Ejecuta: > validar_criterios_aceptacion]

Refinador: "⚠️ He detectado que los 3 CA tienen problemas de claridad (score: 45/100).
           
           Ninguno es actualmente testeable de forma automática. Te propongo estos
           refinamientos basados en formato Given-When-Then:
           
           **CA1 Original:** 'El usuario puede agregar productos'
           **CA1 Mejorado:** 'Dado que el usuario está autenticado y visualiza un 
           producto con stock, cuando hace clic en Agregar al carrito, entonces...'
           
           ¿Estos refinamientos capturan la intención correcta?"
```

### 🔗 Integración con Otros Roles

| Rol | Uso |
|-----|-----|
| **Refinador HU** | Validar CA automáticamente antes del desglose técnico |
| **ArchDev Pro** | Validar que CA técnicos sean medibles antes de diseñar arquitectura |
| **Artesano de Commits** | Validar que commits de CA cumplan estándares |

### 📈 Criterios de Éxito

- ✅ Detecta CA no medibles en 90%+ de casos
- ✅ Genera reformulaciones SMART válidas en 80%+ de casos
- ✅ Completa análisis en < 5 segundos para 10 CA
- ✅ Reduce iteraciones de refinamiento de 3+ a 1-2

### 🚧 Limitaciones Conocidas

- No entiende contexto de negocio específico del dominio
- Puede generar falsos positivos con CA técnicos válidos pero no convencionales
- Requiere que los CA estén en español (o idioma configurado)

---

## 2. `estimar_complejidad_hu`

### 🎯 Propósito

Calcular automáticamente Story Points basado en complejidad técnica, incertidumbre y esfuerzo estimado, generando justificación detallada de la estimación.

### 📊 Nivel de Prioridad

**🟡 MEDIA** - Mejora significativa pero el Refinador puede estimar manualmente.

### 🔍 Problema que Resuelve

- **Antes:** Estimaciones inconsistentes entre diferentes refinadores o sesiones
- **Después:** Estimaciones objetivas y justificadas basadas en factores medibles

### 📥 Input Esperado

**Parámetros:**
- `tareas_tecnicas` (array, requerido): Lista de tareas desglosadas
  ```json
  [
    {
      "id": "API-101",
      "descripcion": "Definir endpoint POST /api/cart/items",
      "tipo": "api",
      "complejidad_estimada": "baja"
    },
    {
      "id": "SVC-102",
      "descripcion": "Implementar CartService con validación de stock",
      "tipo": "service",
      "complejidad_estimada": "media"
    }
  ]
  ```
- `contexto_hu` (object, requerido):
  ```json
  {
    "tiene_integraciones_externas": false,
    "cantidad_modulos_impactados": 3,
    "requiere_migracion_datos": false,
    "es_greenfield": true,
    "equipo_experiencia_nivel": "medio"
  }
  ```
- `factores_riesgo` (array, opcional): Factores de incertidumbre conocidos

### 📤 Output Esperado

**Formato: JSON con estimación justificada**

```json
{
  "estimacion_completada": true,
  "story_points_total": 8,
  "confianza_estimacion": "alta",
  "nivel_complejidad": "MEDIO",
  "desglose_detallado": {
    "complejidad_tecnica": {
      "puntos": 3,
      "justificacion": "Lógica de negocio con validaciones moderadas (stock, límites). Usa patrones conocidos (Repository, DTO).",
      "factores": [
        "Implementación de CartService: 2 puntos (validaciones complejas)",
        "Persistencia con JPA: 1 punto (uso estándar de Repository Pattern)"
      ]
    },
    "integraciones": {
      "puntos": 0,
      "justificacion": "Sin integraciones externas. Solo comunicación interna entre capas.",
      "factores": []
    },
    "testing": {
      "puntos": 2,
      "justificacion": "Tests en 3 niveles: unitarios (CartService), integración (endpoints), e2e (flujo completo). Primera vez con Testcontainers en módulo de carrito.",
      "factores": [
        "Tests unitarios: 0.5 puntos (estándar con Mockito)",
        "Tests integración: 1 punto (setup inicial de Testcontainers)",
        "Tests e2e: 0.5 puntos (uso de suite Cypress existente)"
      ]
    },
    "frontend": {
      "puntos": 2,
      "justificacion": "Componente de contador en header + página de carrito. Complejidad media si estado global ya existe.",
      "factores": [
        "Contador en header: 0.5 puntos (componente simple)",
        "Página de carrito: 1 punto (lista con renderizado condicional)",
        "Estado global: 0.5 puntos (integración con Context/Redux existente)"
      ]
    },
    "infraestructura": {
      "puntos": 0,
      "justificacion": "Sin cambios de infraestructura. Usa stack existente.",
      "factores": []
    },
    "deuda_tecnica": {
      "puntos": 1,
      "justificacion": "Requiere refactor menor en ProductService para extraer validación de stock a módulo compartido.",
      "factores": [
        "Extracción de lógica duplicada: 0.5 puntos",
        "Actualización de tests de ProductService: 0.5 puntos"
      ]
    }
  },
  "analisis_incertidumbre": {
    "nivel": "baja",
    "factores": [
      {
        "factor": "Patrón conocido",
        "impacto": "positivo",
        "descripcion": "El equipo ya implementó funcionalidad similar en módulo de wishlist"
      },
      {
        "factor": "Dependencia de stock",
        "impacto": "neutral",
        "descripcion": "Lógica de stock ya existe, solo se reutiliza"
      }
    ],
    "ajuste_por_incertidumbre": 0,
    "justificacion": "Sin incertidumbre significativa. Sigue patrones existentes y no hay dependencias externas."
  },
  "comparativa_historica": {
    "hu_similares_pasadas": [
      {
        "titulo": "Agregar productos a wishlist",
        "story_points_estimados": 5,
        "story_points_reales": 6,
        "similitud": 85
      }
    ],
    "leccion_aprendida": "HU similar (wishlist) tomó 1 SP más por complejidad no anticipada en sincronización de estado. Esta HU ya contempla ese escenario."
  },
  "recomendaciones": [
    "Considerar buffer de 1 SP si el equipo es nuevo con Testcontainers",
    "Validar con el equipo que la lógica de validación de stock es reutilizable",
    "Confirmar que estado global (Context/Redux) está configurado para carrito"
  ],
  "distribucion_esfuerzo": {
    "backend": "37%",
    "frontend": "25%",
    "testing": "25%",
    "refactoring": "13%"
  }
}
```

### 🔧 Lógica Interna Sugerida

**Fase 1: Análisis de Tareas**
1. **Categorizar tareas por tipo:**
   - API/Endpoints
   - Servicios/Lógica de negocio
   - Persistencia/Base de datos
   - Frontend/UI
   - Testing
   - Infraestructura
   - Seguridad

2. **Asignar peso base por tipo de tarea:**
   - API simple (CRUD): 0.5 SP
   - Servicio con lógica compleja: 1-2 SP
   - Integración externa: 2-3 SP
   - Tests unitarios: 0.3 SP
   - Tests integración: 0.5-1 SP
   - UI componente simple: 0.5 SP
   - UI componente complejo: 1-2 SP

**Fase 2: Factores Multiplicadores**
- **Experiencia del equipo:**
  - Experto: 0.8x
  - Medio: 1.0x
  - Junior: 1.3x

- **Módulos impactados:**
  - 1-2 módulos: 1.0x
  - 3-5 módulos: 1.2x
  - 6+ módulos: 1.5x

- **Integraciones externas:**
  - Sin integraciones: 1.0x
  - 1-2 integraciones: 1.3x
  - 3+ integraciones: 1.6x

**Fase 3: Análisis de Incertidumbre**
- Greenfield vs Brownfield
- Dependencias externas
- Tecnologías nuevas para el equipo
- Requisitos no funcionales exigentes

**Fase 4: Comparativa Histórica**
- Buscar HU similares en histórico (si existe BD)
- Calcular desviación entre estimado vs real
- Aplicar lecciones aprendidas

**Fase 5: Generar Justificación**
- Narrativa humanizada del cálculo
- Desglose punto por punto
- Recomendaciones contextuales

### 🎭 Comportamiento Esperado del Rol Refinador HU

**Con esta herramienta:**
```markdown
Refinador: "Voy a estimar la complejidad de la HU basándome en las tareas desglosadas..."

[Ejecuta: > estimar_complejidad_hu tareas_tecnicas=[...] contexto_hu={...}]

Refinador: "Estimo esta HU en **8 Story Points**. Aquí está el desglose:
           
           **Complejidad Técnica:** 3 SP
           - CartService con validaciones: 2 SP
           - Persistencia JPA estándar: 1 SP
           
           **Testing:** 2 SP
           - Setup inicial Testcontainers: 1 SP
           - Tests unit + e2e: 1 SP
           
           **Frontend:** 2 SP
           - Contador + página carrito: 2 SP
           
           **Refactoring:** 1 SP
           - Extracción de validación de stock duplicada
           
           **Incertidumbre:** Baja (equipo ya implementó wishlist similar)
           
           ¿Esta estimación te parece razonable?"
```

### 📈 Criterios de Éxito

- ✅ Estimaciones dentro del ±20% de esfuerzo real en 70%+ de casos
- ✅ Justificaciones claras y comprensibles
- ✅ Completa cálculo en < 3 segundos
- ✅ Aprende de histórico para mejorar precisión con el tiempo

---

## 3. Mejora: `refinar_hu`

### 🎯 Propósito de la Mejora

Refactorizar la herramienta existente `refinar_hu.md` para:
1. **Incluir el proceso completo de 3 pasos** del .txt (Análisis → Desglose → Estrategia)
2. **Integrar con nuevas herramientas** (`validar_criterios_aceptacion`, `estimar_complejidad_hu`)
3. **Documentar vertical slicing** con ejemplos
4. **Incluir sistema de NIVELES** (Simple/Estándar/Complejo)

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es la herramienta principal del Refinador HU.

### 🔍 Estado Deseado

**Nueva estructura completa:**

```markdown
# 🛠️ Herramienta: `refinar_hu`

## 🎯 Propósito

Transformar Historias de Usuario ambiguas en planes de ejecución técnicos claros, aplicando
un proceso estructurado de 3 pasos con validación automática de CA y estimación justificada.

## 📥 Input Esperado

**Parámetros:**
- `historia_usuario` (string, requerido): Narrativa "Como [rol], quiero [funcionalidad], para [beneficio]"
- `criterios_aceptacion` (array, requerido): Lista de CA iniciales
- `contexto_adicional` (object, opcional): Restricciones técnicas, integraciones, requisitos NFR
- `usar_validacion_automatica` (boolean, opcional): Ejecutar `validar_criterios_aceptacion` automáticamente. Default: `true`
- `calcular_estimacion` (boolean, opcional): Ejecutar `estimar_complejidad_hu` al final. Default: `true`

## 📤 Output Esperado

**Formato estructurado en 6 secciones:**

### **1. 🔍 Preguntas de Clarificación**
[Lista de preguntas priorizadas por riesgo]

### **2. ✅ Criterios de Aceptación Refinados**
[CA en formato Given-When-Then SMART]

### **3. 🔨 Desglose Técnico (Vertical Slicing)**
[Tareas agrupadas en slices funcionales end-to-end]

### **4. 🎯 Estrategia de Desarrollo**
[Enfoque TDD, patrones sugeridos, orden de implementación]

### **5. 📊 Estimación Justificada**
[Story Points con desglose detallado]

### **6. ⚠️ Riesgos y Observaciones**
[Tabla de riesgos + deuda técnica identificada]

## 🔄 Proceso Interno de 3 Pasos

### Paso 1: Análisis y Refinamiento
1. Ejecutar `validar_criterios_aceptacion` (si `usar_validacion_automatica=true`)
2. Analizar gaps y ambigüedades
3. Generar preguntas de clarificación priorizadas por severidad
4. Proponer CA mejorados en formato SMART

### Paso 2: Desglose en Tareas Técnicas
1. Detectar nivel de complejidad (🟢 BAJO / 🟡 MEDIO / 🔴 ALTO)
2. Aplicar vertical slicing:
   - Slice 1: MVP funcional end-to-end
   - Slice 2: Funcionalidades secundarias
   - Slice 3: Validaciones avanzadas
3. Cada tarea debe ser < 1 día de esfuerzo
4. Incluir tareas de testing (unit + integration + e2e)
5. Incluir tareas de seguridad si aplica

### Paso 3: Estrategia y Estimación
1. Proponer enfoque de desarrollo (TDD, patrones, orden)
2. Ejecutar `estimar_complejidad_hu` (si `calcular_estimacion=true`)
3. Analizar riesgos y proponer mitigaciones
4. Identificar deuda técnica o refactorings necesarios
5. Sugerir escalamiento a otros roles si es necesario

## 💡 Ejemplos Completos

### Ejemplo 1: HU Simple (CRUD básico)
[Input + Output esperado para nivel 🟢 BAJO]

### Ejemplo 2: HU Estándar (Lógica + integraciones)
[Input + Output esperado para nivel 🟡 MEDIO]

### Ejemplo 3: HU Compleja (Múltiples integraciones + impacto arquitectónico)
[Input + Output esperado para nivel 🔴 ALTO]

## 🔗 Integración con Otras Herramientas

**Flujo automático:**
1. Usuario invoca `refinar_hu` con HU + CA
2. Herramienta ejecuta `validar_criterios_aceptacion` → detecta ambigüedades
3. Presenta preguntas de clarificación al usuario
4. Usuario responde → herramienta genera CA mejorados
5. Genera desglose técnico vertical
6. Ejecuta `estimar_complejidad_hu` → calcula Story Points
7. Presenta output completo en 6 secciones

## 🎚️ Sistema de NIVELES

La herramienta adapta su comportamiento según complejidad detectada:

| Nivel | Preguntas | Tareas | Slices | Análisis de Riesgo |
|-------|-----------|--------|--------|-------------------|
| 🟢 BAJO | 1-2 | 3-5 | 1 MVP | Básico |
| 🟡 MEDIO | 3-5 | 5-10 | 2-3 | Moderado |
| 🔴 ALTO | 6-10+ | 10-20 | 3-4 | Exhaustivo + escalamiento |
```

### 📈 Criterios de Éxito de la Mejora

- ✅ Proceso de 3 pasos documentado exhaustivamente
- ✅ Integración automática con herramientas de validación y estimación
- ✅ Sistema de NIVELES implementado con ejemplos
- ✅ Vertical slicing documentado con patrones claros
- ✅ 3 ejemplos completos (uno por nivel de complejidad)

---

## 📝 Notas Finales

### Priorización Recomendada para Implementación

1. **🥇 Primera iteración (Crítica):**
   - Implementar `validar_criterios_aceptacion`
   - Refactorizar `refinar_hu` con proceso de 3 pasos

2. **🥈 Segunda iteración (Alta prioridad):**
   - Implementar `estimar_complejidad_hu`
   - Integrar flujo completo automático

3. **🥉 Tercera iteración (Optimización):**
   - Añadir BD histórica para comparativas
   - Implementar aprendizaje de estimaciones pasadas

### Impacto Estimado

| Herramienta/Mejora | Ahorro de Tiempo | Mejora de Calidad | Complejidad Implementación |
|-------------------|------------------|-------------------|---------------------------|
| `validar_criterios_aceptacion` | 🔥🔥🔥 (70%) | 🔥🔥🔥🔥 (90%) | 🟡 Media |
| `estimar_complejidad_hu` | 🔥🔥 (50%) | 🔥🔥🔥 (60%) | 🔴 Alta |
| Mejora `refinar_hu` | 🔥🔥🔥 (80%) | 🔥🔥🔥 (70%) | 🟡 Media |

---

## 📅 Última Actualización

**Fecha:** 5 de octubre de 2025  
**Autor:** Análisis durante refactorización de Refinador HU v2.0  
**Estado:** Propuesta de herramientas pendientes de implementación
