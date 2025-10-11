# 🏗️ Herramienta: Definición de Arquitectura

> **Versión:** 2.0  
> **Fecha de Actualización:** 7 de octubre de 2025  
> **Autor:** Sistema de Herramientas ArchDev Pro  
> **Estado:** Activa

---

## 📋 Identificación

**Herramienta:** `define_arquitectura`

---

## 🎯 Objetivo

Guiar la selección y justificación de un estilo/enfoque arquitectónico óptimo para un nuevo sistema (o evolución de uno existente) mediante un proceso estructurado de descubrimiento, comparación y recomendación fundamentada.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`tomar_contexto`** | Al inicio (proyectos existentes) | Obtener stack tecnológico, dependencias, arquitectura actual |
| **`analizar_code_smells`** | Si existe código legacy (opcional) | Identificar deuda técnica que influye en decisión arquitectónica |
| **`diagnosticar_devops`** | Si se requiere (opcional) | Evaluar restricciones de infraestructura/deployment |
| **`generar_adr`** | Al finalizar análisis (si usuario aprueba) | Documentar formalmente la decisión arquitectónica |

### Herramientas que la Invocan

- **ArchDev Pro** (al iniciar proyectos nuevos o reestructuraciones)
- **Onad** (decisiones estratégicas de arquitectura empresarial)

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Resumen de los requisitos funcionales clave (qué debe lograr el sistema inicialmente)
- Tipo de proyecto (nuevo desde cero / evolución de existente / migración)

**Secundario (Opcional):**
- Requisitos no funcionales priorizados (disponibilidad, latencia, escalabilidad, seguridad, cumplimiento, observabilidad)
- Tamaño y experiencia del equipo de desarrollo/operaciones
- Presupuesto y horizonte de time-to-market
- Proyección de evolución (crecimiento esperado de dominios/módulos/tráfico)
- Contexto del proyecto existente (si aplica, puede obtenerse automáticamente vía `tomar_contexto`)

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `modo` | string | rapido\|profundo | profundo | Extensión del análisis comparativo |
| `max_opciones` | number | 2-4 | 3 | Número máximo de opciones arquitectónicas a comparar |
| `incluir_tabla` | boolean | true\|false | true | Incluir tabla comparativa consolidada |
| `incluir_tradeoffs` | boolean | true\|false | true | Explicitar trade-offs explícitos por opción |
| `contexto_inicial` | string | texto libre | - | Resumen previo si el usuario lo tiene |
| `ejecutar_tomar_contexto` | boolean | true\|false | true* | Ejecutar análisis automático del proyecto (*solo si es proyecto existente) |
| `analizar_codigo_existente` | boolean | true\|false | false | Ejecutar `analizar_code_smells` para evaluar deuda técnica |
| `considerar_devops` | boolean | true\|false | false | Ejecutar `diagnosticar_devops` para evaluar restricciones de infraestructura |
| `generar_adr` | boolean | true\|false | true | Invocar herramienta `generar_adr` al finalizar |
| `formato_adr` | string | nygard\|madr\|y-statement | nygard | Formato de ADR a usar (delegado a `generar_adr`) |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (principal)
- ✅ **Onad** (decisiones estratégicas)
- ✅ **Arquitecto DevOps** (consulta sobre restricciones de infraestructura)

---

## 🔄 Proceso Paso a Paso

### **Paso 1: Análisis Automático de Contexto** 🤖 (Si aplica)

**Solo para proyectos existentes con `ejecutar_tomar_contexto: true`**

```bash
# Si el proyecto ya existe
> tomar_contexto

# Si hay código legacy y usuario activó el parámetro
> analizar_code_smells (opcional)

# Si se requiere considerar restricciones de infraestructura
> diagnosticar_devops (opcional)
```

Presentar al usuario resumen del análisis automático con síntesis de contexto detectado.

---

### **Paso 2: Clarificación de Requisitos** 📋

Formular preguntas nucleares antes de sugerir arquitectura:

#### 2.1 Preguntas Sobre Requisitos Funcionales

> * "¿Cuáles son los **principales requisitos funcionales** (módulos/dominios iniciales del sistema)?"
> * "¿Cuántos dominios de negocio diferentes abarcará el sistema inicialmente? ¿Se espera que crezcan en el futuro?"

#### 2.2 Preguntas Sobre Requisitos No Funcionales

> * "¿Cuáles son los **requisitos no funcionales más críticos**?"
>   - Alta disponibilidad (¿qué % de uptime se requiere?)
>   - Baja latencia (¿qué tiempos de respuesta se esperan?)
>   - Escalabilidad (¿cuántos usuarios concurrentes? ¿picos de tráfico estacionales?)
>   - Seguridad/Cumplimiento (¿nivel bancario, GDPR, HIPAA?)
>   - Observabilidad (¿SLAs contractuales?)

#### 2.3 Preguntas Sobre Equipo y Organización

> * "¿Cuál es el **tamaño y experiencia del equipo** de desarrollo/operaciones?"
>   - Número de desarrolladores backend/frontend/DevOps
>   - Experiencia con arquitecturas distribuidas (microservicios, eventos, etc.)
>   - Capacidad de operar infraestructura compleja

#### 2.4 Preguntas Sobre Restricciones de Negocio

> * "¿Cuál es el **presupuesto y presión de time-to-market**?"
>   - ¿MVP en 3 meses o desarrollo a largo plazo?
>   - Restricciones de costos de infraestructura cloud

#### 2.5 Preguntas Sobre Evolución y Escalado

> * "¿Existe **previsión de escalado por dominios** o necesidad de aislar límites de despliegue pronto?"
> * "¿Cuál es el **horizonte de mantenimiento** (MVP de validación vs producto a largo plazo)?"

#### 2.6 Restricciones Fuertes

Detectar restricciones no negociables:
- Legales (GDPR, residencia de datos)
- Regulatorias (compliance bancario, salud)
- SLAs contractuales (99.9% uptime)
- Tecnológicas (vendor lock-in existente, legacy systems a integrar)

---

### **Paso 3: Análisis de Opciones Arquitectónicas** 🏛️

#### 3.1 Selección de Candidatos

Basado en las respuestas del usuario, seleccionar 2-3 estilos arquitectónicos viables (máx. `max_opciones`):

**Catálogo de opciones comunes:**
- **Monolito Modular** (bien estructurado con límites de dominio claros)
- **Arquitectura Hexagonal** (Puertos y Adaptadores)
- **Microservicios**
- **Arquitectura Orientada a Eventos** (Event-Driven)
- **CQRS** (Command Query Responsibility Segregation)
- **Serverless** (híbrido o completo)
- **Arquitectura en Capas** (tradicional MVC mejorado)

#### 3.2 Descarte Explícito

Si el usuario menciona opciones no adecuadas, descartarlas con justificación breve.

---

### **Paso 4: Comparación Detallada de Opciones** ⚖️

#### 4.1 Tabla Comparativa Consolidada (si `incluir_tabla: true`)

| Criterio | Opción A | Opción B | Opción C |
|----------|----------|----------|----------|
| **Complejidad Inicial** | 🟢/🟡/🔴 | ... | ... |
| **Complejidad Operativa** | 🟢/🟡/🔴 | ... | ... |
| **Velocidad Desarrollo Inicial** | 🟢/🟡/🔴 | ... | ... |
| **Escalabilidad Horizontal** | 🟢/🟡/🔴 | ... | ... |
| **Escalabilidad por Dominios** | 🟢/🟡/🔴 | ... | ... |
| **Coste Cambio Futuro** | 🟢/🟡/🔴 | ... | ... |
| **Observabilidad/Trazabilidad** | 🟢/🟡/🔴 | ... | ... |
| **Resiliencia/Aislamiento Fallos** | 🟢/🟡/🔴 | ... | ... |
| **Requisitos Mínimos Equipo** | X devs | ... | ... |
| **Experiencia Requerida** | Junior/Mid/Senior | ... | ... |
| **Tiempo Hasta Producción** | X meses | ... | ... |

#### 4.2 Detalle por Opción (si `incluir_tradeoffs: true`)

Para cada opción documentar:
- ✅ **Ventajas**
- ❌ **Desventajas**
- 🎯 **Cuándo Elegir**
- ⚙️ **Requisitos de Equipo**
- ⚠️ **Riesgos y Mitigaciones**
- 🛠️ **Stack Sugerido**

#### 4.3 Matriz de Trade-offs (si hay conflictos de requisitos)

Si el usuario tiene requisitos en conflicto, proponer estrategia de compromiso o arquitectura en fases.

---

### **Paso 5: Recomendación Fundamentada** 🎯

#### 5.1 Recomendación Principal

**Formato obligatorio:**
```markdown
## ✅ Recomendación Arquitectónica

### Opción Seleccionada: [Nombre de la Arquitectura]

**Recomiendo [Opción] porque:**
1. [Driver principal 1]
2. [Driver principal 2]
3. [Driver principal 3]

**A pesar de aceptar los siguientes trade-offs:**
- [Trade-off 1]
- [Trade-off 2]

**Alineación con requisitos:**
| Requisito | Prioridad Usuario | Soporte de Arquitectura |
|-----------|-------------------|------------------------|
| [Requisito 1] | 🔴 CRÍTICO | 🟢 EXCELENTE |
| [Requisito 2] | 🟡 MEDIO | 🟢 SUFICIENTE |
```

#### 5.2 Condiciones de Re-evaluación

Definir umbrales que dispararían revisión de la decisión arquitectónica:
- Crecimiento de usuarios
- Crecimiento de dominios
- Incremento de latencia
- Crecimiento de equipo
- Problemas de deployment

**Revisión programada:** Cada 6 meses o al alcanzar hitos clave del producto

---

### **Paso 6: Riesgos y Mitigaciones** ⚠️

Tabla con riesgos identificados, probabilidad, impacto y mitigaciones propuestas.

---

### **Paso 7: Roadmap Técnico Inicial** 🛣️

Proponer plan de implementación de los primeros 3 meses (sprints o fases).

---

### **Paso 8: Confirmación y Delegación a `generar_adr`** ✅

#### 8.1 Pregunta de Confirmación

> "✅ He completado el análisis arquitectónico. **¿Apruebas esta recomendación?**  
> Si es así, puedo invocar la herramienta `generar_adr` para documentar formalmente esta decisión en un Architecture Decision Record."

#### 8.2 Invocación de Herramienta ADR (si `generar_adr: true` y usuario aprueba)

```bash
> generar_adr
    titulo="Selección de Arquitectura Inicial"
    contexto="[Resumen del análisis]"
    decision="[Opción seleccionada]"
    consecuencias="[Trade-offs y beneficios]"
    formato=nygard  # o el formato especificado en parámetros
    archivo_salida="artefactos/adr/001-arquitectura-inicial.md"
```

**Mensaje al usuario:**
> "He invocado `generar_adr` para crear el ADR formal. Revisa el documento generado en `artefactos/adr/001-arquitectura-inicial.md`."

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| **Información insuficiente sobre requisitos** | Pausar análisis, enumerar datos faltantes exactos, solicitar al usuario |
| **Inconsistencias detectadas** | Advertir explícitamente sobre sobrecarga operativa, proponer alternativa |
| **Conflictos de prioridades irreconciliables** | Evidenciar conflicto, proponer compromiso temporal (arquitectura en fases) |
| **Ambigüedad persistente** | Sugerir spike técnico o prototipo exploratorio de 1-2 semanas |
| **Usuario rechaza recomendación principal** | Solicitar razones específicas, ajustar análisis, ofrecer segunda opción |
| **Proyecto existente con arquitectura deficiente** | Ejecutar `analizar_code_smells` obligatoriamente, proponer migración incremental |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Documento Markdown estructurado con análisis completo de decisión arquitectónica

**Estructura del output:**
1. Resumen de Contexto
2. Opciones Seleccionadas
3. Tabla Comparativa
4. Detalle por Opción
5. Recomendación
6. Riesgos y Mitigaciones
7. Roadmap / Próximos Pasos
8. Condiciones de Re-evaluación

**Nota:** El Architecture Decision Record (ADR) formal será generado por la herramienta `generar_adr` invocada al final del proceso.

---

## 💡 Ejemplo de Uso

**Para ver un ejemplo completo de uso de esta herramienta, consulta:**

📁 **`ejemplos/herramientas/ecommerce_mvp_completo.md`**

Este ejemplo muestra:
- Contexto inicial de un proyecto e-commerce
- Proceso completo de preguntas y respuestas
- Análisis comparativo de 3 opciones arquitectónicas
- Recomendación fundamentada con trade-offs
- Roadmap de implementación
- Invocación a `generar_adr`

---

## 📚 Referencias y Notas

### Relación con Otras Herramientas

**Herramientas que Invoca:**
- **`tomar_contexto`** → Análisis automático de proyecto existente
- **`analizar_code_smells`** → Evaluación de deuda técnica en código legacy
- **`diagnosticar_devops`** → Restricciones de infraestructura
- **`generar_adr`** → Documentación formal de decisión arquitectónica

**Herramientas que la Invocan:**
- **ArchDev Pro** → Decisiones arquitectónicas en proyectos nuevos
- **Onad** → Estrategia empresarial de arquitectura

### Patrones Arquitectónicos de Referencia

| Patrón | Cuándo Usar | Referencias |
|--------|-------------|-------------|
| **Monolito Modular** | MVP, equipos pequeños, presupuesto limitado | [Martin Fowler - MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html) |
| **Microservicios** | Escala alta, equipos grandes, dominios autónomos | [Sam Newman - Building Microservices](https://samnewman.io/books/building_microservices/) |
| **Arquitectura Hexagonal** | Desacoplamiento de infraestructura, testabilidad | [Alistair Cockburn - Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) |
| **Event-Driven** | Integración compleja, auditabilidad | [Martin Fowler - Event-Driven Architecture](https://martinfowler.com/articles/201701-event-driven.html) |

### Limitaciones Conocidas

- No considera arquitecturas altamente especializadas (Real-Time Systems, Embedded, Blockchain-based)
- Análisis de costos es estimación aproximada (varía por proveedor cloud)
- Requiere honestidad del usuario sobre capacidades reales del equipo

### Futuras Mejoras

- **v2.1:** Integración con herramientas de estimación de costos cloud
- **v2.2:** Machine Learning para predecir éxito de arquitectura basado en histórico
- **v2.3:** Soporte para arquitecturas híbridas (on-premise + cloud)

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | - | Versión inicial básica |
| 2.0 | 2025-10-07 | ✅ Reestructuración siguiendo `herramienta_plantilla.md`<br>✅ Integración con herramientas complementarias<br>✅ Delegación de generación de ADR a `generar_adr`<br>✅ Referencias a ejemplos en carpeta `ejemplos/`<br>✅ Matriz de trade-offs mejorada |