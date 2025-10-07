# 📚 Ejemplos y Guías de Uso

Esta carpeta contiene ejemplos completos de uso de las herramientas del sistema **ArchDev Pro**. Cada ejemplo muestra un caso de uso real con entradas, proceso y salidas esperadas.

---

## 📁 Estructura de Carpetas

### 📐 `arquitectura/`

Ejemplos completos de análisis y decisión arquitectónica usando la herramienta `define_arquitectura`.

| Archivo | Descripción | Caso de Uso |
|---------|-------------|-------------|
| `ecommerce_mvp_completo.md` | E-commerce MVP con Monolito Modular | Startup con equipo pequeño, presupuesto limitado, alta presión de time-to-market |
| `sistema_bancario_microservicios.md` | Sistema bancario con Microservicios | Empresa grande, alta disponibilidad crítica, equipos distribuidos |
| `startup_monolito_modular.md` | SaaS B2B con Monolito Modular | Validación de producto, evolución futura planificada |
| `saas_evento_driven.md` | Plataforma SaaS con EDA | Integración con múltiples sistemas externos, auditabilidad crítica |

### 📝 `adr/`

Ejemplos de Architecture Decision Records generados con la herramienta `generar_adr`.

| Archivo | Formato | Descripción |
|---------|---------|-------------|
| `adr_001_seleccion_microservicios.md` | Nygard | Decisión de migrar de monolito a microservicios |
| `adr_002_migracion_eventos.md` | MADR | Adopción de arquitectura orientada a eventos |
| `adr_003_adopcion_kubernetes.md` | Y-Statement | Migración de infraestructura a Kubernetes |
| `adr_004_deprecacion_monolito.md` | Nygard | Deprecación de monolito legacy (supersede ADR-001) |

### 🔍 `code_smells/`

Ejemplos de análisis de code smells usando `analizar_code_smells`.

| Archivo | Code Smell Principal | Stack |
|---------|---------------------|-------|
| `god_object_user_service.md` | God Object | Java Spring Boot |
| `feature_envy_payment_processor.md` | Feature Envy | Java Spring Boot |

### 🔧 `refactoring/`

Ejemplos de refactorización completa usando `refactorizar`.

| Archivo | Técnica Principal | Stack |
|---------|------------------|-------|
| `extract_class_complete.md` | Extract Class + SRP | Java Spring Boot |
| `repository_pattern_migration.md` | Repository Pattern | Java Spring Boot + JPA |

---

## 🚀 Cómo Usar Estos Ejemplos

### 1️⃣ **Encuentra un caso similar al tuyo**

Revisa la tabla de cada carpeta y selecciona el ejemplo que más se parezca a tu situación.

### 2️⃣ **Lee el ejemplo completo**

Cada ejemplo incluye:
- **Contexto inicial:** Descripción del proyecto y restricciones
- **Proceso paso a paso:** Preguntas, análisis, comparación
- **Decisión final:** Recomendación justificada
- **Artefactos generados:** ADRs, documentación, código

### 3️⃣ **Adapta a tu proyecto**

Usa el ejemplo como guía, pero ajusta según tus requisitos específicos.

### 4️⃣ **Invoca la herramienta correspondiente**

Ejecuta la herramienta (`define_arquitectura`, `generar_adr`, etc.) con tus propios parámetros.

---

## 💡 Contribuir con Nuevos Ejemplos

Si has utilizado una herramienta y crees que tu caso de uso puede ser útil para otros, considera documentarlo y agregarlo a esta carpeta.

**Formato sugerido:**
- Contexto claro del proyecto
- Restricciones y requisitos específicos
- Proceso completo ejecutado
- Resultado final con justificación

---

## 📞 Soporte

Si tienes dudas sobre cómo usar estos ejemplos o las herramientas, consulta:
- 📖 Documentación de herramientas: `/herramientas/`
- 👥 Documentación de personas/roles: `/personas/`
- 📋 Plantillas: `/plantillas/`
