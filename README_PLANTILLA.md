# 📘 Guía de Uso: Plantillas de Roles/Personas

> **Fecha de actualización:** 13 de octubre de 2025  
> **Versión:** 2.0

---

## 🎯 Propósito de este Documento

Este archivo contiene la **documentación completa** del sistema de plantillas para crear roles/personas. Aquí encontrarás:
- **Cómo usar las dos plantillas** (`para_ia/` y `para_humanos/`)
- **Cuándo usar cada sección** de la plantilla
- **Análisis de importancia** de cada componente
- **Recomendaciones según el tipo de rol** que estés creando
- **Ejemplos de casos de uso reales**

---

## 📁 Estructura del Sistema de Plantillas

```
plantillas/
├── README_PLANTILLA.md              ← Este archivo (guía completa)
├── para_ia/
│   └── rol_persona_clean.md        ← Template LIMPIO para copiar a /personas/
└── para_humanos/
    └── rol_persona_con_guias.md    ← Template CON GUÍAS para consulta
```

### 🤖 **`para_ia/rol_persona_clean.md`**
**Propósito:** Plantilla lista para ser usada por la IA
- ✅ Sin hints ni meta-instrucciones
- ✅ Sin referencias a documentación externa
- ✅ Placeholders descriptivos
- ✅ Listo para copiar a `/personas/nuevo_rol.md`

**📌 USO:** Este es el archivo que debes **COPIAR** cuando crees un nuevo rol.

---

### 👨‍💻 **`para_humanos/rol_persona_con_guias.md`**
**Propósito:** Referencia con ayudas extensivas para desarrolladores
- ✅ Hints visuales (`> ℹ️`, `> 💡`, `> ⚠️`)
- ✅ Ejemplos reales inline de Onad y Artesano
- ✅ Comparaciones "MAL vs BIEN"
- ✅ Checklist de validación
- ✅ Referencias a roles existentes

**📌 USO:** Este archivo es solo para **CONSULTA** cuando tengas dudas al rellenar un rol.

---

## 🚀 Flujo de Trabajo Recomendado

### **Opción A: Usuario Experimentado** (Recomendada)
```
1. Copia para_ia/rol_persona_clean.md → /personas/tu_nuevo_rol.md
2. Rellena las secciones según tu tipo de rol
3. Valida y prueba con el orquestador
```

### **Opción B: Usuario Nuevo**
```
1. Lee este README_PLANTILLA.md (decisión estratégica de secciones)
2. Consulta para_humanos/rol_persona_con_guias.md si tienes dudas
3. Copia para_ia/rol_persona_clean.md → /personas/tu_nuevo_rol.md
4. Rellena siguiendo las guías
5. Elimina secciones opcionales que no uses
6. Valida con el orquestador
```

---

## 📊 Clasificación de Secciones

### ✅ **OBLIGATORIAS** (Todos los roles deben tenerlas)

#### 1. 📋 Identificación
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- El **Comando de Activación** permite al orquestador detectar y cargar el rol
- La **Versión** facilita el mantenimiento y trazabilidad de cambios
- Sin identificación correcta, el sistema de activación falla

**Ejemplo:**
```markdown
**Persona:** `Arquitecto Senior Java`
**Comando de Activación:** `onad`
**Versión:** `2.5`
**Idioma:** `Español`
```

---

#### 2. 🎯 Misión Principal
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- Define el **propósito único** del rol en el ecosistema
- Ayuda al orquestador a decidir cuándo sugerir este rol vs. otros
- Es la brújula que guía todas las decisiones del agente

**Patrón recomendado:** 
> "Actuar como [rol] que [acción principal], [cómo lo hace] mediante [enfoque único]."

**Ejemplo real (Onad):**
```markdown
Actuar como consultor técnico de élite y arquitecto estratégico especializado 
en arquitectura de software con ecosistema Java/Spring Boot, guiando decisiones 
técnicas a través de análisis crítico de trade-offs, validación de supuestos 
y visión a largo plazo.
```

---

#### 3. 💬 Estilo de Comunicación y Tono
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- Diferencia la **personalidad** entre roles (el "cómo pensar" del proyecto)
- Implementa la **Directiva de Claridad y Estructura** del orquestador
- Sin esto, todos los roles sonarían igual y genéricos

**Componentes clave:**
- **Precisión:** Nivel de detalle técnico (Alta/Media/Baja)
- **Formalidad:** Tono de las respuestas (Formal/Profesional/Casual)
- **Enfoque:** Orientación principal (Solución/Análisis/Justificación)
- **Formato Preferido:** Estructura de respuestas (Markdown/Listas/Tablas)
- **Frase típica:** Una frase característica del rol

**💡 Crítico:** Esto es lo que diferencia roles similares. Dos arquitectos pueden tener
el mismo conocimiento técnico pero diferentes personalidades.

---

#### 4. 🎓 Áreas de Especialización y Conocimiento
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- Define el **contexto técnico** y límites del rol
- Implementa la **Directiva de Límites de Conocimiento** del orquestador
- Permite respuestas especializadas y precisas
- Indica cuándo devolver control al orquestador

**Subsecciones:**
- **Tecnologías Clave:** Stack técnico específico
- **Principios Arquitectónicos:** Filosofías de diseño
- **Metodologías:** Frameworks de trabajo (Scrum, TDD, DDD, etc.)
- **Estándares del Proyecto:** Guías de estilo específicas

**⚠️ Sé específico:** No pongas "Desarrollo de software" (demasiado genérico).
Pon "Spring Boot, Microservicios REST, PostgreSQL" (específico y útil).

---

#### 5. ⚖️ Principios y Restricciones
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- Implementa las **Directivas del Núcleo** personalizadas por rol
- Los "Siempre/Nunca" evitan soluciones genéricas
- Es el corazón de la filosofía **"No Comer Entero"** del sistema
- Garantiza calidad y coherencia en las respuestas

**Estructura:**
```markdown
### 🔴 Principio Cardinal: "[Nombre del Principio]"
[Descripción del principio fundamental]

**Siempre:**
- ✅ [Buena práctica obligatoria ESPECÍFICA]
- ✅ [Comportamiento esperado ESPECÍFICO]

**Nunca:**
- ❌ [Anti-patrón ESPECÍFICO a evitar]
- ❌ [Comportamiento prohibido ESPECÍFICO]
```

**⚠️ CRÍTICO - Sé ESPECÍFICO:**
- ❌ MAL: "Escribir buen código" (genérico, no aporta valor)
- ✅ BIEN: "Usar inmutabilidad en entidades de dominio DDD" (específico, accionable)

---

#### 6. 🔧 Interacción con Herramientas
**Importancia:** ⭐⭐⭐⭐ MUY ALTA

**Por qué es muy recomendada:**
- Personaliza **cómo cada rol usa las mismas herramientas**
- Evita respuestas genéricas entre roles
- Es el **diferenciador clave** entre roles similares

**Ejemplo del diferenciador:**
- **Arquitecto ONAD** usa `crear_pruebas` → Enfoque en arquitectura hexagonal
- **Artesano de Commits** usa `crear_pruebas` → Enfoque en TDD estricto
- **ArchDev Pro** usa `crear_pruebas` → Implementación pragmática
- **Mismo comando, diferente filosofía** ✨

**Formato:**
```markdown
| Herramienta | Enfoque Específico de Este Rol |
|-------------|--------------------------------|
| `crear_pruebas` | [Cómo ESTE rol usa esta herramienta] |
| `refactorizar` | [La FILOSOFÍA única con la que la aplica] |
```

---

#### 7. 🛠️ Herramientas Disponibles
**Importancia:** ⭐⭐⭐⭐⭐ CRÍTICA

**Por qué es obligatoria:**
- Lista los **comandos ejecutables** del rol
- Permite al orquestador hacer **lazy loading** eficiente
- Sin herramientas, el rol sería solo teoría sin capacidad de acción

**Formato:**
```markdown
- `tomar_contexto`
- `refactorizar`
- `crear_pruebas`
```

**⚠️ Importante:** Verifica que estas herramientas EXISTEN en `/herramientas/`

---

#### 8. 💡 Ejemplo de Interacción
**Importancia:** ⭐⭐⭐⭐ ALTA

**Por qué es muy recomendada:**
- Valida coherencia entre todas las secciones
- Documenta el tono y estilo esperado
- Facilita mantenimiento futuro
- Funciona como **test de aceptación** del rol

**Debe reflejar:**
- ✅ El tono definido (formal/casual/mentor)
- ✅ El enfoque (solución/análisis/educativo)
- ✅ Los principios (validación, cuestionamiento, etc.)
- ✅ El formato preferido (markdown, listas, tablas)
- ✅ La aplicación del principio cardinal

**💡 Tip:** Escribe este ejemplo ANTES de escribir el rol completo.
Te ayudará a clarificar la personalidad.

---

### 🟡 **OPCIONALES AVANZADAS** (Según complejidad del rol)

#### 9. 🔄 Protocolos de Inicio
**Importancia:** ⭐⭐⭐ MEDIA

**Cuándo usar:**
- ✅ El rol necesita **verificar contexto automáticamente** al activarse
- ✅ Tiene comportamientos condicionales según el estado del proyecto
- ✅ Requiere inicialización específica

**Cuándo NO usar:**
- ❌ Roles simples sin necesidad de setup automático
- ❌ Cuando no hay comportamiento automático al activar

**Ejemplo de quién lo usa:** `arquitecto_onad.md` (verifica `contexto_proyecto.md`)

**⚠️ SI NO LO USAS:** Elimina la sección completa, no dejes el título vacío.

---

#### 10. 🎚️ Sistema de NIVELES de Complejidad
**Importancia:** ⭐⭐⭐⭐ ALTA (para roles versátiles)

**Cuándo usar:**
- ✅ El rol recibe **consultas de muy variada complejidad**
- ✅ Desde preguntas simples ("¿Qué es REST?") hasta tareas complejas ("Diseñar microservicios")
- ✅ Quieres **optimizar UX:** no bombardear con 10 preguntas para una consulta trivial
- ✅ Hay diferencia SIGNIFICATIVA en el flujo entre consultas simples y complejas

**Cuándo NO usar:**
- ❌ Roles específicos con UN SOLO tipo de tarea (ej: Artesano de Commits)
- ❌ Todas las consultas requieren la misma profundidad

**Ejemplo real:** `arquitecto_devops.md` implementa 3 niveles:
- 🟢 **NIVEL BAJO:** Consultas educativas (0-1 preguntas)
- 🟡 **NIVEL MEDIO:** Problemas específicos (3-5 preguntas)
- 🔴 **NIVEL ALTO:** Diseño arquitectónico (6-10+ preguntas)

**Beneficios:**
- ✅ Reduce sobrecarga cognitiva del usuario
- ✅ Acelera respuestas para problemas simples
- ✅ Mantiene profundidad para problemas complejos
- ✅ Mejora dramáticamente la UX

**⚠️ SI NO LO USAS:** Elimina la sección completa, no dejes el título vacío.

---

#### 11. ⚠️ Cuándo NO Usar Este Rol
**Importancia:** ⭐⭐⭐ MEDIA-ALTA (para roles especializados)

**Cuándo usar:**
- ✅ Tu rol es especializado y hay overlaps con otros roles
- ✅ Es importante clarificar fronteras (ej: Onad vs ArchDev Pro)
- ✅ Ayuda al orquestador a recomendar el rol correcto

**Cuándo NO usar:**
- ❌ El rol es único sin overlaps
- ❌ Las fronteras son obvias

**Ejemplo real:** `arquitecto_onad.md` clarifica:
- Usar ArchDev Pro para implementación de código
- Usar DevOps para pipelines CI/CD
- Onad es para decisiones arquitectónicas estratégicas

---

#### 12. 📚 Notas Adicionales
**Importancia:** ⭐⭐ BAJA

**Cuándo usar:**
- ✅ Hay limitaciones conocidas del rol
- ✅ Contextos específicos de aplicación óptima
- ✅ Historial de versiones del perfil
- ✅ Relaciones con otros roles

**Cuándo NO usar:**
- ❌ Para documentar cosas que ya están en otras secciones
- ❌ Como "cajón de sastre" de información desestructurada

---

## 🌟 Secciones Avanzadas Opcionales (Patrones Emergentes)

Estas secciones **NO están en la plantilla estándar**, pero han emergido en roles avanzados del proyecto y han demostrado valor. Úsalas cuando aporten claridad significativa.

### 🎭 Diferenciación con Otros Roles
**Importancia:** ⭐⭐⭐⭐ ALTA (para roles con overlaps)

**Cuándo usar:**
- ✅ Tu rol tiene **overlap funcional** con otro rol existente
- ✅ Es crítico explicar **cuándo usar cada uno**
- ✅ Los usuarios podrían confundir las responsabilidades

**Formato:**
```markdown
### 🎭 Diferenciación con [Otro Rol]

**[Tu Rol] ([Enfoque]):**
- 🎯 [Responsabilidad principal]
- 📊 [Tipo de análisis que hace]
- ⏱️ [Horizonte temporal]
- 💬 [Estilo de comunicación]
- 📦 Output: [Entregables típicos]

**[Otro Rol] ([Enfoque]):**
- 🎯 [Responsabilidad principal]
- 🛠️ [Tipo de trabajo que hace]
- ⏱️ [Horizonte temporal]
- 💬 [Estilo de comunicación]
- 📦 Output: [Entregables típicos]

**Flujo de trabajo conjunto:**
[Cómo se complementan ambos roles]
```

**Ejemplo real:** `arquitecto_onad.md` diferencia claramente Onad (estratega) vs ArchDev Pro (implementador)

**Valor:** Reduce confusión del usuario y mejora la selección del rol correcto.

---

### 📋 Flujos de Trabajo Estructurados
**Importancia:** ⭐⭐⭐⭐ ALTA (para roles con múltiples tipos de tareas)

**Cuándo usar:**
- ✅ El rol puede realizar **3+ tipos de tareas diferentes**
- ✅ Cada tipo de tarea tiene un **proceso estructurado único**
- ✅ Quieres garantizar **consistencia** en la ejecución

**Formato:**
```markdown
## 📋 Flujos de Trabajo Estructurados

### Flujo 1: [Nombre de la Tarea] (N Pasos)

**Activación:** Usuario dice "[frase gatillo]"

**Paso 1: [Nombre]**
> "[Acción específica que realiza]"

**Paso 2: [Nombre]**
> "[Acción específica que realiza]"

**Paso N: [Nombre]**
> "[Acción específica que realiza]"

---

### Flujo 2: [Nombre de la Tarea] (N Pasos)
[Mismo formato]
```

**Ejemplo real:** `archdev_pro.md` tiene 3 flujos:
1. Refactorizar Código (5 pasos)
2. Crear Pruebas (5 pasos)
3. Implementar Arquitectura (4 pasos)

**Valor:** Garantiza que el rol siga un proceso consistente y completo para cada tipo de tarea.

---

### 🔄 Protocolo/Mecanismo de Escalamiento
**Importancia:** ⭐⭐⭐ MEDIA-ALTA (para roles especializados)

**Cuándo usar:**
- ✅ El rol puede detectar que necesita **ayuda de otro rol especializado**
- ✅ Hay **límites claros** de expertise que requieren derivación
- ✅ Quieres que el rol sea proactivo sugiriendo el cambio

**Formato:**
```markdown
## 🔄 Mecanismo de Escalamiento

**Cuándo escalar a otros roles:**

**→ [Rol Destino]:** Si [condición específica]
> "[Mensaje que el rol diría al usuario]"

**→ [Rol Destino 2]:** Si [condición específica]
> "[Mensaje que el rol diría al usuario]"
```

**Ejemplo real:** `refinador_hu.md` escala a:
- **DevOps** si hay implicaciones de infraestructura complejas
- **ArchDev Pro** si emergen decisiones arquitectónicas estructurales
- **Onad** si se requiere refactoring profundo previo

**Valor:** Permite que los roles reconozcan sus límites y deriven proactivamente.

---

### 🛠️ Catálogo Priorizado de Herramientas
**Importancia:** ⭐⭐⭐⭐ ALTA (para roles con múltiples herramientas)

**Cuándo usar:**
- ✅ El rol tiene **5+ herramientas disponibles**
- ✅ Para ciertas tareas, **múltiples herramientas pueden aplicar**
- ✅ Quieres guiar al usuario en la **selección óptima**

**Formato:**
```markdown
## 🛠️ Herramientas Recomendadas (Catálogo Priorizado)

Para [tipo de tarea], te recomiendo estas herramientas en orden de prioridad:

1. **🥇 `herramienta_1`** (Más recomendada)
   - **Por qué:** [Razón principal]
   - **Cuándo usarla:** [Situación ideal]
   - **Output:** [Qué genera]

2. **🥈 `herramienta_2`**
   - **Por qué:** [Razón principal]
   - **Cuándo usarla:** [Situación ideal]
   - **Output:** [Qué genera]

3. **🥉 `herramienta_3`**
   - **Por qué:** [Razón principal]
   - **Cuándo usarla:** [Situación ideal]
   - **Output:** [Qué genera]

¿Cuál prefieres ejecutar primero?
```

**Ejemplo real:** `arquitecto_devops.md` presenta catálogo priorizado en consultas de NIVEL ALTO:
1. 🥇 `diagnosticar_devops` (análisis completo)
2. 🥈 `refinar_hu` (enriquecer historias)
3. 🥉 `generar_commit` (documentar cambios)

**Valor:** Reduce la parálisis por análisis y guía al usuario hacia la mejor herramienta.

---

### 📊 Formato de Respuesta Extensa Estándar
**Importancia:** ⭐⭐⭐ MEDIA (para roles con respuestas complejas)

**Cuándo usar:**
- ✅ El rol genera **respuestas largas y estructuradas**
- ✅ Quieres garantizar **consistencia en el formato**
- ✅ La respuesta tiene **múltiples secciones interdependientes**

**Formato:**
```markdown
## 📋 Formato de Respuesta Extensa Estándar

Toda respuesta completa debe seguir esta estructura:

### **1. [Sección 1]**
[Descripción de qué va en esta sección]

### **2. [Sección 2]**
[Descripción de qué va en esta sección]

### **N. [Sección N]**
[Descripción de qué va en esta sección]
```

**Ejemplo real:** `refinador_hu.md` define 6 secciones estándar:
1. 🔍 Preguntas de Clarificación
2. ✅ Criterios de Aceptación Refinados
3. 🔨 Desglose Técnico
4. 🎯 Estrategia de Desarrollo y Estimación
5. ⚠️ Riesgos y Mitigaciones
6. 💡 Observaciones y Recomendaciones

**Valor:** Garantiza que el rol no omita secciones críticas en respuestas complejas.

---

## 🎯 Recomendaciones para Usar Secciones Avanzadas

### ✅ **Cuándo SÍ agregar secciones avanzadas:**

1. **El rol ya funciona bien** con las secciones estándar
2. Detectas **un patrón repetitivo** que merece estructura
3. La sección **resuelve confusión real** de los usuarios
4. Aporta **claridad significativa** sin agregar complejidad

### ❌ **Cuándo NO agregar secciones avanzadas:**

1. **Eres nuevo creando roles** - Domina primero las secciones estándar
2. La sección sería **"por si acaso"** sin caso de uso claro
3. La información **ya está cubierta** en otras secciones
4. Agregaría **complejidad innecesaria** a un rol simple

### 💡 **Regla de oro:**

> "Una sección avanzada debe demostrar su valor resolviendo un problema real. Si no sabes para qué la usarías, no la agregues."

---

## 🎯 Matriz de Decisión: ¿Qué Secciones Usar?

### Para un **Rol Básico/Específico**
Ejemplo: *"Revisor de Código SQL"*, *"Validador de APIs REST"*

```
✅ USAR (Obligatorias):
├── 📋 Identificación
├── 🎯 Misión Principal
├── 💬 Estilo de Comunicación
├── 🎓 Áreas de Especialización
├── ⚖️ Principios y Restricciones
├── 🔧 Interacción con Herramientas
├── 🛠️ Herramientas Disponibles
└── 💡 Ejemplo de Interacción

⏭️ OMITIR (Opcionales):
├── 🔄 Protocolos de Inicio (no necesario)
├── 🎚️ Sistema de Niveles (tarea única)
├── ⚠️ Cuándo NO Usar (si no hay overlaps)
└── 📚 Notas Adicionales (si no aplica)
```

---

### Para un **Rol Intermedio/Versátil**
Ejemplo: *"Arquitecto DevOps"*, *"Desarrollador Full Stack"*

```
✅ USAR:
├── TODAS las secciones obligatorias (1-8)
├── 🎚️ Sistema de Niveles (⭐ CLAVE para UX)
├── 🔄 Protocolos de Inicio (si necesita setup)
└── ⚠️ Cuándo NO Usar (si hay overlaps con otros roles)

⏭️ EVALUAR:
└── 📚 Notas Adicionales (solo si hay limitaciones importantes)
```

---

### Para un **Rol Avanzado/Estratégico**
Ejemplo: *"Arquitecto ONAD"*, *"Lead Tech Architect"*

```
✅ USAR:
└── TODAS las secciones (sin excepción)

⭐ ÉNFASIS ESPECIAL EN:
├── 🎚️ Sistema de Niveles (diferencia dramática de UX)
├── 🔧 Interacción con Herramientas (personalización profunda)
├── 🔄 Protocolos de Inicio (setup automático)
└── ⚠️ Cuándo NO Usar (clarificar fronteras con otros roles)
```

---

## 📖 Ejemplos Reales del Proyecto

### Ejemplo 1: Rol Básico - `artesano_de_commits.md`
**Tipo:** Específico (una sola responsabilidad)

**Secciones usadas:**
- ✅ Identificación → Comando: `artesano`
- ✅ Misión → Crear mensajes de commit profesionales
- ✅ Estilo → Conciso, técnico, estructurado
- ✅ Especialización → Git, Conventional Commits, Semantic Versioning
- ✅ Principios → Siempre contextualizar, Nunca mensajes genéricos
- ✅ Interacción → `generar_commit` con proceso de 5 pasos
- ✅ Herramientas → `generar_commit`, `obtener_diff_git`, `analizar_diff_contextual`
- ✅ Ejemplo de Interacción
- ✅ Sistema de Niveles (3 niveles según complejidad del commit)
- ⏭️ NO usa Protocolos de Inicio (no necesita setup automático)

---

### Ejemplo 2: Rol Avanzado - `arquitecto_onad.md`
**Tipo:** Estratégico (múltiples niveles de complejidad)

**Secciones usadas:**
- ✅ TODAS las obligatorias
- ✅ TODAS las recomendadas
- ✅ Protocolos de Inicio (verifica y carga `contexto_proyecto.md`)
- ✅ Principio Cardinal: "No Comer Entero" (nunca aceptar propuestas sin análisis)
- ✅ Cuándo NO Usar (clarifica vs ArchDev Pro y DevOps)
- ✅ Notas Adicionales (evolución, complementariedad, anti-patrones)
- ⏭️ NO usa Sistema de Niveles (siempre hace análisis profundo)

**Resultado:** Rol altamente especializado con comportamiento automático y fronteras claras.

---

### Ejemplo 3: Rol Intermedio - `arquitecto_devops.md`
**Tipo:** Versátil (diferentes tipos de consultas)

**Secciones usadas:**
- ✅ TODAS las obligatorias
- ✅ Sistema de Niveles (3 niveles bien diferenciados):
  - 🟢 BAJO: Consultas educativas sobre conceptos
  - 🟡 MEDIO: Diagnóstico de problemas específicos
  - 🔴 ALTO: Diseño de pipelines completos
- ✅ Protocolos de Inicio para verificar contexto
- ✅ Interacción personalizada con `diagnosticar_devops`

**Resultado:** UX optimizada que no bombardea con preguntas para consultas simples.

---

## 🚀 Guía Paso a Paso: Crear un Nuevo Rol

### **Paso 1: Define el Tipo de Rol**
```
¿Es específico o versátil?
├─ Específico (una tarea) → Usa secciones básicas
└─ Versátil (múltiples tipos de consultas) → Considera Sistema de Niveles
```

### **Paso 2: Copia la Plantilla Limpia**
```bash
# Desde el directorio raíz del proyecto
cp plantillas/para_ia/rol_persona_clean.md personas/tu_nuevo_rol.md
```

### **Paso 3: Completa Secciones Obligatorias**
```
1. 📋 Identificación (comando único - verificar que no exista)
2. 🎯 Misión (1-2 líneas claras del propósito)
3. 💬 Estilo (define la personalidad única)
4. 🎓 Especialización (stack técnico específico)
5. ⚖️ Principios (Siempre/Nunca ESPECÍFICOS)
6. 🔧 Interacción (cómo usa CADA herramienta)
7. 🛠️ Herramientas (lista de comandos que existen)
8. 💡 Ejemplo (valida coherencia de todo lo anterior)
```

### **Paso 4: Evalúa Secciones Opcionales**
```
¿Necesita setup automático al activarse? 
└─ SÍ → Agrega 🔄 Protocolos de Inicio

¿Recibe consultas de complejidad MUY variada?
└─ SÍ → Agrega 🎚️ Sistema de Niveles

¿Hay overlap con otros roles similares?
└─ SÍ → Agrega ⚠️ Cuándo NO Usar

¿Tiene limitaciones o contexto especial?
└─ SÍ → Agrega 📚 Notas Adicionales
```

### **Paso 5: Elimina Secciones No Usadas**
```
⚠️ IMPORTANTE: Si no usas una sección opcional:
❌ NO dejes el título vacío
❌ NO pongas "No aplica"
✅ ELIMINA la sección completa
```

### **Paso 6: Valida con el Orquestador**
```
Verifica que:
- ✅ El comando de activación sea único (buscar en /personas/)
- ✅ Las herramientas existan en /herramientas/
- ✅ El ejemplo de interacción refleje el estilo definido
- ✅ Los principios sean específicos (no genéricos)
- ✅ La personalidad sea única (no copiada de otro rol)
- ✅ El archivo NO contenga hints tipo `> ℹ️` o `> 💡`
```

### **Paso 7: Prueba el Rol**
```
1. Activa el rol con el orquestador: /cochas switch tu_comando
2. Prueba con una consulta típica
3. Verifica que el comportamiento refleje lo definido
4. Ajusta si es necesario
```

---

## ⚡ Tips y Mejores Prácticas

### ✅ DO (Hacer)

**Principios Específicos:**
- ✅ "Usar inmutabilidad en entidades de dominio DDD"
- ❌ "Escribir buen código" (demasiado genérico)

**Personaliza Interacción con Herramientas:**
- ✅ Mismo comando, diferente filosofía entre roles
- ✅ Explica QUÉ prioriza cada rol al usar la herramienta

**Usa Sistema de Niveles en roles versátiles:**
- ✅ Mejora UX dramáticamente
- ✅ Evita frustración del usuario

**Mantén coherencia:**
- ✅ El Ejemplo de Interacción debe reflejar TODO lo definido
- ✅ El tono debe ser consistente en toda la plantilla

**Escribe el Ejemplo primero:**
- ✅ Te ayuda a clarificar la personalidad antes de escribir el resto

---

### ❌ DON'T (No hacer)

**No uses principios genéricos:**
- ❌ "Hacer las cosas bien"
- ❌ "Seguir mejores prácticas"
- ❌ "Escribir código limpio"

**No copies roles:**
- ❌ Cada rol debe tener personalidad única
- ❌ Diferencia clara en tono y enfoque

**No omitas Interacción con Herramientas:**
- ❌ Es lo que diferencia roles que comparten herramientas
- ❌ Sin esto, todos se comportan igual

**No crees comandos sin verificar:**
- ❌ Deben existir en `/herramientas/`
- ❌ Causa errores en el orquestador

**No dejes secciones vacías:**
- ❌ Si no usas una sección opcional, elimínala completamente
- ❌ No pongas "No aplica" o comentarios vacíos

**No incluyas hints en el archivo final:**
- ❌ Elimina todas las líneas `> ℹ️`, `> 💡`, `> ⚠️`
- ❌ El orquestador carga TODO el archivo como prompt

---

## 🔍 Checklist de Validación Final

Antes de considerar completo tu rol, verifica:

### **Verificaciones Obligatorias:**
- [ ] **Comando de activación único** - Buscado en `/personas/` y confirmado que no existe
- [ ] **Herramientas existen** - Todas las listadas están en `/herramientas/`
- [ ] **Ejemplo de Interacción completo** - Refleja tono, principios y formato
- [ ] **Principios específicos** - NO genéricos como "hacer las cosas bien"
- [ ] **Personalidad única** - NO copiado de otros roles
- [ ] **Interacción con Herramientas personalizada** - Enfoque único por herramienta
- [ ] **Misión Principal clara** - En 1-2 líneas define el propósito único

### **Si usaste Sistema de Niveles:**
- [ ] **Justificado** - El rol recibe consultas de complejidad MUY variada
- [ ] **3 niveles diferenciados** - Protocolos claramente distintos entre niveles
- [ ] **Indicadores claros** - Fácil para la IA clasificar consultas por nivel
- [ ] **Matriz de decisión** - Tabla resumen incluida

### **Limpieza final:**
- [ ] **Sin hints** - Eliminadas TODAS las líneas `> ℹ️`, `> 💡`, `> ⚠️`
- [ ] **Secciones opcionales eliminadas** - Si no se usan, borradas completamente
- [ ] **Sin placeholders** - Todos los `[campos]` están rellenados
- [ ] **Sin referencias externas** - No menciona "consulta README" o archivos externos

### **Validación con IA:**
- [ ] **Leer el archivo final** como si fueras la IA - ¿suena coherente?
- [ ] **Comparar con un rol existente** - ¿tiene la misma calidad?
- [ ] **Probar con el orquestador** - ¿se activa correctamente?
- [ ] **Probar comportamiento** - ¿responde según lo definido?

---

## 📞 Soporte y Referencias

### **Documentación:**
- **Este archivo:** Guía estratégica completa
- **`para_humanos/rol_persona_con_guias.md`:** Consulta con hints inline
- **`para_ia/rol_persona_clean.md`:** Template limpio para copiar

### **Ejemplos Reales:**
- **Rol Básico:** `/personas/artesano_de_commits.md`
- **Rol Intermedio:** `/personas/arquitecto_devops.md`
- **Rol Avanzado:** `/personas/arquitecto_onad.md`

### **Herramientas de Ayuda:**
- **Validación:** Usar checklist de este documento
- **Creación guiada:** `guia_creacion_roles.md`
- **Core del sistema:** `/core-cochas.md` (cómo funciona el orquestador)

---

## 🔄 Historial de Versiones

**v2.0** (13 oct 2025)
- Separación de plantillas: `para_ia/` y `para_humanos/`
- Agregada sección obligatoria: 🎯 Misión Principal
- Agregada sección recomendada: ⚠️ Cuándo NO Usar Este Rol
- Deprecada plantilla original `rol_persona_plantilla.md`
- Flujo de trabajo actualizado con nueva estructura
- Checklist de validación expandida
- Ejemplos reales actualizados

**v1.0** (13 oct 2025)
- Versión inicial con clasificación completa de secciones
- Matriz de decisión por tipo de rol
- Ejemplos reales del proyecto
- Guía de flujo de creación

---

**Última actualización:** 13 de octubre de 2025  
**Mantenedor:** Sistema de Orquestación de Agentes IA  
**Versión:** 2.0
