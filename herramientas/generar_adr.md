# 📝 Herramienta: Generar Architecture Decision Record (ADR)

> **Versión:** 1.0  
> **Fecha de Creación:** 7 de octubre de 2025  
> **Autor:** Sistema de Herramientas ArchDev Pro  
> **Estado:** Activa

---

## 📋 Identificación

**Herramienta:** `generar_adr`

---

## 🎯 Objetivo

Generar documentación formal de decisiones arquitectónicas siguiendo estándares de Architecture Decision Records (ADR), soportando múltiples formatos y plantillas, para mantener trazabilidad y contexto de decisiones técnicas críticas a lo largo del ciclo de vida del proyecto.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

*Esta herramienta funciona de manera independiente y no invoca otras herramientas del sistema.*

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **`define_arquitectura`** | Al finalizar análisis arquitectónico y obtener aprobación del usuario | Documentar formalmente la decisión arquitectónica en un ADR |
| **ArchDev Pro** | Cuando se toma una decisión técnica importante | Documentar decisiones arquitectónicas significativas del proyecto |
| **Arquitecto Onad** | Para decisiones estratégicas de alto nivel | Registrar decisiones que afectan múltiples proyectos o la organización |
| **Arquitecto DevOps** | Para decisiones de infraestructura críticas | Documentar elecciones de tecnologías de infraestructura y deployment |

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- **Título de la decisión:** Nombre descriptivo de la decisión arquitectónica
- **Contexto:** Descripción del problema o necesidad que motivó la decisión
- **Decisión:** Opción arquitectónica seleccionada con justificación
- **Consecuencias:** Trade-offs, beneficios y riesgos aceptados

**Secundario (Opcional):**
- **Opciones consideradas:** Alternativas evaluadas y razones de descarte
- **Estado:** Propuesto / Aceptado / Rechazado / Deprecado / Supersedido
- **Fecha:** Fecha de la decisión (default: fecha actual)
- **Autores/Decisores:** Equipo o personas involucradas en la decisión
- **Referencias:** Links a documentos relacionados (análisis, benchmarks, RFCs)
- **ADRs relacionados:** Si supersede o complementa a otro ADR

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `titulo` | string | texto libre | - | Título de la decisión (requerido) |
| `contexto` | string | texto libre | - | Descripción del contexto (requerido) |
| `decision` | string | texto libre | - | Decisión tomada con justificación (requerido) |
| `consecuencias` | string | texto libre | - | Trade-offs y consecuencias (requerido) |
| `formato` | string | nygard\|madr\|y-statement\|custom | nygard | Formato de ADR a usar |
| `estado` | string | propuesto\|aceptado\|rechazado\|deprecado\|supersedido | aceptado | Estado de la decisión |
| `opciones_consideradas` | string | texto libre | - | Alternativas evaluadas (opcional) |
| `fecha` | string | YYYY-MM-DD | fecha_actual | Fecha de la decisión |
| `autores` | string | lista separada por comas | - | Autores/decisores |
| `referencias` | string | lista de URLs/paths | - | Links a documentos relacionados |
| `archivo_salida` | string | ruta relativa | artefactos/adr/NNN-titulo.md | Ruta donde guardar el ADR |
| `numero_adr` | number | 001-999 | auto | Número secuencial del ADR (auto-detecta siguiente disponible) |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (principal)
- ✅ **Onad** (decisiones estratégicas)
- ✅ **Arquitecto DevOps** (decisiones de infraestructura)
- ✅ **`define_arquitectura`** (invocación automática)

---

## 🔄 Proceso Paso a Paso

### **Paso 1: Validación de Entradas** ✅

- Verificar que todos los parámetros requeridos estén presentes (titulo, contexto, decision, consecuencias)
- Si falta información crítica, solicitar al usuario antes de continuar
- Validar que el formato seleccionado sea soportado

---

### **Paso 2: Determinación de Número ADR** 🔢

- Si `numero_adr` es "auto", escanear carpeta `artefactos/adr/` para determinar el siguiente número secuencial
- Formato: `001`, `002`, `003`, etc.
- Si la carpeta no existe, crearla y comenzar con `001`

---

### **Paso 3: Selección de Plantilla** 📋

Según el parámetro `formato`, seleccionar la plantilla correspondiente:

#### **Formato Nygard (Por Defecto)**

Creado por Michael Nygard, es el formato más popular y simple.

**Estructura:**
```markdown
# ADR [número]: [Título]

**Estado:** [Propuesto | Aceptado | Deprecado | Supersedido]  
**Fecha:** [YYYY-MM-DD]  
**Autores:** [Lista de autores]

## Contexto

[Descripción del contexto y el problema]

## Decisión

[Decisión tomada y justificación]

## Consecuencias

[Trade-offs, beneficios, riesgos]

## Referencias

[Links a documentos relacionados]
```

#### **Formato MADR (Markdown Any Decision Records)**

Formato más estructurado con secciones expandidas.

**Estructura:**
```markdown
# [Título corto]

- **Estado:** [propuesto | rechazado | aceptado | deprecado | ... | supersedido por [ADR-0005](0005-ejemplo.md)]
- **Decisores:** [lista de personas involucradas en la decisión]
- **Fecha:** [YYYY-MM-DD cuando se actualizó por última vez]

## Contexto y Problema

[Descripción del contexto y problema en 2-3 párrafos]

## Drivers de Decisión

- [driver 1, ej: necesidad de reducir time-to-market]
- [driver 2, ej: equipo pequeño sin experiencia en sistemas distribuidos]
- [driver 3, ej: presupuesto limitado]

## Opciones Consideradas

- [opción 1]
- [opción 2]
- [opción 3]

## Decisión

Opción elegida: "[opción 1]", porque [justificación resumida]

### Consecuencias Positivas

- [ej: reducción de complejidad operativa]
- [ej: velocidad de desarrollo aumentada]

### Consecuencias Negativas

- [ej: escalabilidad horizontal limitada]
- [ej: deployment acoplado]

## Validación

[Cómo se validará que esta decisión fue correcta - métricas, umbrales]

## Pros y Contras de las Opciones

### [opción 1]

[descripción breve]

- ✅ Bueno, porque [argumento a]
- ✅ Bueno, porque [argumento b]
- ❌ Malo, porque [argumento c]

### [opción 2]

[descripción breve]

- ✅ Bueno, porque [argumento a]
- ❌ Malo, porque [argumento b]

## Más Información

[enlaces, referencias, documentos relacionados]
```

#### **Formato Y-Statement**

Formato ultra-conciso enfocado en la esencia de la decisión.

**Estructura:**
```markdown
# ADR [número]: [Título]

**En el contexto de** [contexto o caso de uso],  
**enfrentando** [problema o necesidad],  
**decidimos** [opción arquitectónica seleccionada]  
**para lograr** [consecuencia o beneficio deseado],  
**aceptando** [trade-off o desventaja aceptada].

---

## Detalles Adicionales

[Información complementaria si es necesaria]
```

#### **Formato Custom**

Permite al usuario definir una estructura personalizada.

---

### **Paso 4: Generación del Contenido** 📝

- Rellenar la plantilla seleccionada con los datos proporcionados por el usuario
- Aplicar formato Markdown correcto (títulos, listas, tablas, énfasis)
- Asegurar que las secciones obligatorias estén completas
- Agregar metadatos (fecha, versión, autores)

---

### **Paso 5: Creación del Archivo** 💾

- Generar el nombre del archivo: `[numero_adr]-[titulo-slug].md`
  - Ejemplo: `001-seleccion-arquitectura-monolito-modular.md`
- Crear la estructura de carpetas si no existe (`artefactos/adr/`)
- Guardar el archivo en la ruta especificada
- Actualizar índice de ADRs si existe (`artefactos/adr/README.md`)

---

### **Paso 6: Confirmación y Entrega** ✅

Notificar al usuario:

```markdown
✅ **ADR Generado Exitosamente**

- **Archivo:** `artefactos/adr/001-seleccion-arquitectura-monolito-modular.md`
- **Formato:** Nygard
- **Estado:** Aceptado
- **Fecha:** 2025-10-07

📄 **Vista Previa:**
[Mostrar primeras líneas del ADR generado]

🔗 **Próximos Pasos:**
- Revisar el ADR generado
- Compartir con el equipo para validación
- Commitear al repositorio con mensaje descriptivo
```

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| **Parámetros requeridos faltantes** | Solicitar explícitamente cada dato faltante antes de generar |
| **Carpeta de destino no existe** | Crear estructura de carpetas automáticamente |
| **Número ADR duplicado** | Advertir al usuario y sugerir siguiente número disponible |
| **Formato no soportado** | Listar formatos disponibles y solicitar selección válida |
| **Archivo ya existe** | Preguntar si sobrescribir o crear nueva versión |
| **Título muy largo** | Truncar slug del archivo a 50 caracteres máximo |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Archivo Markdown (.md) con el ADR formateado según plantilla seleccionada

**Ubicación por defecto:**
- `artefactos/adr/[numero]-[titulo-slug].md`

**Contenido adicional:**
- Actualización de `artefactos/adr/README.md` (índice de todos los ADRs)

---

## 💡 Ejemplo de Uso

**Para ver ejemplos completos de ADRs generados con esta herramienta, consulta:**

📁 **`ejemplos/herramientas/adr/`**
- `adr_001_seleccion_microservicios.md` (Formato Nygard)
- `adr_002_migracion_eventos.md` (Formato MADR)
- `adr_003_adopcion_kubernetes.md` (Formato Y-Statement)

---

### Ejemplo de Invocación

```bash
> generar_adr
    titulo="Selección de Arquitectura Monolito Modular para E-Commerce MVP"
    contexto="Necesitamos lanzar un MVP de e-commerce en 3 meses con equipo pequeño (2 devs backend, 1 frontend) y presupuesto limitado ($300/mes infraestructura). Volumen esperado: 500 usuarios concurrentes en picos."
    decision="Monolito Modular con Arquitectura Hexagonal. Permite velocidad de desarrollo alta, complejidad operativa baja, y evolutividad futura a microservicios si es necesario."
    consecuencias="Positivas: Time-to-market reducido, coste optimizado, curva de aprendizaje suave. Negativas: Escalabilidad horizontal limitada, deployment acoplado. Trade-offs aceptables para fase de validación MVP."
    opciones_consideradas="1. Microservicios (descartado por sobrecarga operativa). 2. Serverless (descartado por vendor lock-in y complejidad inicial). 3. Monolito Modular (seleccionado)."
    formato=nygard
    autores="ArchDev Pro, Tech Lead, Product Owner"
    estado=aceptado
```

**Salida:**
```markdown
✅ ADR Generado: `artefactos/adr/001-seleccion-arquitectura-monolito-modular-ecommerce-mvp.md`

📄 Vista Previa:

# ADR 001: Selección de Arquitectura Monolito Modular para E-Commerce MVP

**Estado:** Aceptado  
**Fecha:** 2025-10-07  
**Autores:** ArchDev Pro, Tech Lead, Product Owner

## Contexto

Necesitamos lanzar un MVP de e-commerce en 3 meses con equipo pequeño (2 devs backend, 1 frontend) y presupuesto limitado ($300/mes infraestructura). Volumen esperado: 500 usuarios concurrentes en picos.

## Decisión

Monolito Modular con Arquitectura Hexagonal. Permite velocidad de desarrollo alta, complejidad operativa baja, y evolutividad futura a microservicios si es necesario.

## Consecuencias

**Positivas:**
- Time-to-market reducido (MVP en 3 meses vs 5-6 con microservicios)
- Coste optimizado (~$150/mes vs $500+ con arquitectura distribuida)
- Curva de aprendizaje suave para equipo junior-mid

**Negativas:**
- Escalabilidad horizontal limitada (aceptable para 500 usuarios)
- Deployment acoplado (mitigado con feature flags y tests automatizados)

Trade-offs aceptables para fase de validación MVP.

## Opciones Consideradas

1. **Microservicios:** Descartado por sobrecarga operativa excesiva para equipo de 2 devs
2. **Serverless:** Descartado por vendor lock-in y complejidad de debugging
3. **Monolito Modular:** ✅ Seleccionado

## Referencias

- Análisis completo: `ejemplos/arquitectura/ecommerce_mvp_completo.md`
- Contexto del proyecto: `artefactos/contexto_proyecto.md`
```

---

## 📚 Referencias y Notas

### Recursos sobre ADRs

- [Architecture Decision Records (ADR)](https://adr.github.io/)
- [MADR - Markdown Any Decision Records](https://adr.github.io/madr/)
- [Michael Nygard - Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [ThoughtWorks Technology Radar - ADRs](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

### Relación con Otras Herramientas

**Herramientas que la Invocan:**
- **`define_arquitectura`** → Al finalizar análisis arquitectónico
- **ArchDev Pro** → Para documentar cualquier decisión técnica importante
- **Onad** → Para decisiones estratégicas de alto nivel

### Mejores Prácticas

1. **Un ADR por decisión:** No mezclar múltiples decisiones en un solo ADR
2. **Inmutabilidad:** Una vez creado, un ADR no se modifica, se crea uno nuevo que lo supersede
3. **Contexto suficiente:** Incluir suficiente información para entender la decisión en el futuro
4. **Lenguaje simple:** Evitar jerga innecesaria, escribir para que cualquiera del equipo entienda
5. **Actualizar índice:** Mantener `artefactos/adr/README.md` actualizado con lista de todos los ADRs

### Limitaciones Conocidas

- Solo genera ADRs en formato Markdown (no Word, PDF, etc.)
- No valida automáticamente la calidad del contenido (depende del input del usuario)
- No integra con herramientas de gestión de decisiones externas (ADR-tools, Log4brains)

### Futuras Mejoras

- **v1.1:** Integración con Git para auto-commit del ADR generado
- **v1.2:** Generación de gráficos de relaciones entre ADRs
- **v1.3:** Exportación a formatos adicionales (PDF, HTML)
- **v1.4:** Validación de calidad del contenido con AI (detectar ADRs incompletos)

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | 2025-10-07 | ✅ Creación inicial<br>✅ Soporte para formatos Nygard, MADR y Y-Statement<br>✅ Auto-numeración de ADRs<br>✅ Integración con `define_arquitectura` |
