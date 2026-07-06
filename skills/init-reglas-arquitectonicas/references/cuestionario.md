# Cuestionario de Reglas Arquitectónicas

> Referencia completa de preguntas para la skill `init-reglas-arquitectonicas`.
> Cada pregunta tiene: id, texto, tipo, opciones, sugerido, y aplica_a (opcional).

---

## Sección 1: Nomenclatura y Convenciones de Nombres

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| nom_01 | ¿Convención para nombres de **CLASES/TIPOS**? | selección | A: PascalCase, B: snake_case, C: Otro | Según stack |
| nom_02 | ¿Convención para nombres de **MÉTODOS/FUNCIONES**? | selección | A: camelCase, B: snake_case, C: PascalCase | Según stack |
| nom_03 | ¿Convención para nombres de **VARIABLES**? | selección | A: camelCase, B: snake_case | Según stack |
| nom_04 | ¿Convención para **CONSTANTES**? | selección | A: UPPER_SNAKE_CASE, B: PascalCase, C: Igual que variables | A |
| nom_05 | ¿Patrón para nombres de **INTERFACES**? | selección | A: Sin prefijo, B: Prefijo I, C: Sufijo Port | Java=A, C#=B, Hexagonal=C |
| nom_06 | ¿Patrón para nombres de **IMPLEMENTACIONES**? | selección | A: Sufijo Impl, B: Prefijo descriptivo, C: Sin sufijo | B |

## Sección 2: Arquitectura y Estructura

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| arq_01 | ¿Estilo arquitectónico principal? | selección | A: Hexagonal, B: Clean Architecture, C: Layered, D: Modular Monolith, E: Microservicios, F: Serverless, G: MVC, H: Otro | Detectar del contexto |
| arq_02 | ¿Estructura de carpetas/paquetes? | selección | A: Por capas, B: Por features, C: Híbrido | A para Hexagonal/Clean, B para Microservicios |
| arq_03 | ¿Regla de dependencias entre capas? | selección | A: Estricta (infra→app→domain), B: Flexible | A |
| arq_04 | ¿Uso de Domain-Driven Design (DDD)? | selección | A: DDD Completo, B: DDD Táctico parcial, C: Solo Repository/Service, D: No usar DDD | Según complejidad |

## Sección 3: Patrones de Diseño

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| pat_01 | ¿Patrones **OBLIGATORIOS**? | multiselección | A: Repository, B: Factory/Builder, C: Strategy, D: Observer/Event, E: Adapter, F: Decorator, G: CQRS, H: Circuit Breaker | A, B según stack |
| pat_02 | ¿Patrones **PROHIBIDOS**? | multiselección | A: Singleton, B: Service Locator, C: God Object, D: Anemic Domain, E: Ninguno | B, C siempre |
| pat_03 | ¿Creación de objetos complejos? | selección | A: Builder obligatorio, B: Factory methods, C: Constructores con validación, D: Libre elección | A para >3 parámetros |

## Sección 4: Principios y Paradigmas

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| pri_01 | ¿Nivel de aplicación de **SOLID**? | selección | A: Estricto, B: Flexible, C: Solo SRP y DIP | A |
| pri_02 | ¿Preferencia de **inmutabilidad**? | selección | A: Por defecto (final/readonly/const), B: Solo en dominio, C: Sin preferencia | A |
| pri_03 | ¿Manejo de **valores nulos**? | selección | A: Prohibir null (Optional), B: Permitido con @Nullable, C: Null Object, D: Sin restricción | A |
| pri_04 | ¿Paradigma predominante? | selección | A: OOP, B: Funcional, C: Híbrido | C |
| pri_05 | ¿Composición vs Herencia? | selección | A: Composición siempre, B: Composición preferida, C: Sin preferencia | B |

## Sección 5: Dependencias y Librerías

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| dep_01 | ¿Librerías **APROBADAS** para testing? | texto libre | Placeholder: JUnit 5, Mockito, AssertJ... | Según stack |
| dep_02 | ¿Librerías **APROBADAS** para logging? | selección_o_texto | A: SLF4J+Logback, B: Winston/Pino, C: logging+structlog, D: Serilog, E: Otro | Según stack |
| dep_03 | ¿Librerías **PROHIBIDAS**? | texto libre | Placeholder: Lombok @Data, Apache Commons... | Dependencias obsoletas |
| dep_04 | ¿Política de actualización? | selección | A: Siempre última, B: LTS preferidas, C: Solo por seguridad, D: Fijar versiones | B |

## Sección 6: Testing y Calidad

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| test_01 | ¿Metodología de testing? | selección | A: TDD estricto, B: TDD flexible, C: Test después, D: BDD | A o B |
| test_02 | ¿Cobertura mínima? | selección | A: 90%+, B: 80%+, C: 70%+, D: Sin mínimo | B |
| test_03 | ¿Convención de nombres para tests? | selección | A: should_when, B: test_method_scenario, C: given_when_then, D: Descriptivo con @DisplayName | A o C |
| test_04 | ¿Tests de integración con? | selección | A: Testcontainers, B: Mocks/Stubs, C: BD en memoria, D: Ambiente dedicado | A |

## Sección 7: Documentación

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| doc_01 | ¿Documentación de código obligatoria en? | multiselección | A: Clases públicas, B: Métodos públicos, C: Métodos complejos, D: Solo excepciones, E: Auto-documentado | A, B, C |
| doc_02 | ¿Decisiones arquitectónicas documentadas en? | selección | A: ADRs, B: Wiki, C: README por módulo, D: Comentarios en código | A |
| doc_03 | ¿Formato de ADRs? | selección | A: MADR, B: Nygard, C: Y-Statement, D: Personalizado | A |

## Sección 8: Seguridad y Calidad de Código

| ID | Pregunta | Tipo | Opciones | Sugerido |
|----|----------|------|----------|----------|
| seg_01 | ¿Reglas de logging para datos sensibles? | selección | A: NUNCA loguear PII/passwords/tokens, B: Con enmascaramiento, C: Sin restricción | A |
| seg_02 | ¿Validación de entradas? | selección | A: Obligatoria en todos los puntos, B: Solo en API pública, C: Solo en dominio | A |
| seg_03 | ¿Límites de tamaño de código? | texto estructurado | max_líneas_método: 20-30, max_líneas_clase: 200-300, max_parámetros: 4-5 | — |
| seg_04 | ¿Herramientas de análisis estático? | texto libre | Placeholder: SonarQube, ESLint, Checkstyle... | Según stack |
