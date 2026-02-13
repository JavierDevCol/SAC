# Contexto del Proyecto: [Nombre]

> **Generado:** [timestamp]  
> **Confianza:** [Alto|Medio|Bajo]

---

##  Scorecard Ejecutivo

| Aspecto | Puntuación | Estado |
|---------|------------|--------|
| Arquitectura | [X]/10 | [] |
| Stack | [X]/10 | [] |
| Testing | [X]/10 | [] |
| DevOps | [X]/10 | [] |
| Documentación | [X]/10 | [] |

---

## 1. Identificación

- **Nombre:** [nombre del proyecto]
- **Descripción:** [1-2 líneas]
- **Tipo:** [API|Web|CLI|Librería|Monolito|Microservicio|Script]
- **Estado:** [Desarrollo|Producción|Mantenimiento|Legacy]

---

## 2. Stack Tecnológico

### Resumen
| Categoría | Tecnología | Versión |
|-----------|------------|---------|
| Lenguaje | [Java/Python/JS/Go/etc.] | [versión] |
| Framework | [Spring/Django/React/Gin/etc.] | [versión] |
| Base de Datos | [PostgreSQL/MongoDB/etc.] | [versión] |
| Testing | [JUnit/Jest/PyTest/etc.] | [versión] |
| Build | [Maven/Gradle/NPM/etc.] | [versión] |

### Dependencias Core
| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| [dependencia_1] | [versión] | [propósito] |
| [dependencia_2] | [versión] | [propósito] |

### Herramientas de Desarrollo
| Herramienta | Propósito | Config |
|-------------|-----------|--------|
| [linter] | Análisis estático | [archivo] |
| [formatter] | Formateo | [archivo] |

---

## 3. Comandos Clave

```bash
# Build
[comando de build]

# Ejecutar
[comando de ejecución]

# Tests
[comando de tests]

# Docker (si aplica)
[comando de docker]
```

---

## 4. Arquitectura

- **Estilo:** [Hexagonal|Capas|MVC|Event-Driven|Microservicios|Script|Monolito]
- **Patrón Principal:** [DDD|CQRS|Repository|MVC|Funcional|etc.]

### Estructura del Proyecto
```
[carpeta-1]/     # [Propósito]
[carpeta-2]/     # [Propósito]
[carpeta-3]/     # [Propósito]
```

### Componentes Principales
| Componente | Ubicación | Responsabilidad |
|------------|-----------|-----------------|
| [componente] | [ruta] | [descripción breve] |

---

## 5. Integraciones

| Tipo | Tecnología | Configuración |
|------|------------|---------------|
| BD Principal | [tipo] | [archivo config] |
| Cache | [tipo o N/A] | [archivo config] |
| Mensajería | [tipo o N/A] | [archivo config] |
| APIs Externas | [lista o N/A] | [archivo config] |

---

## 6. DevOps

| Aspecto | Estado | Archivo |
|---------|--------|---------|
| Dockerfile | [/] | [ruta] |
| Docker Compose | [/] | [ruta] |
| CI/CD | [/] | [ruta] |
| IaC | [/] | [ruta] |

**Puertos:** [lista de puertos expuestos]  
**Profiles:** [lista de profiles/entornos]

---

## 7. Convenciones

### Código
| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Clases/Tipos | [PascalCase/snake_case/etc.] | [ejemplo] |
| Funciones | [camelCase/snake_case/etc.] | [ejemplo] |
| Variables | [camelCase/snake_case/etc.] | [ejemplo] |

### Proyecto
- **Commits:** [Conventional|Angular|Otro]
- **Branching:** [GitFlow|Trunk|Feature Branch]
- **Estructura:** [por capa|por feature|híbrido]

---

## 8. Puntos de Atención

###  Críticos
- [Punto crítico 1]

###  Importantes
- [Punto importante 1]

###  Sugerencias
- [Sugerencia 1]

---

## 9. Artefactos Relacionados

| Artefacto | Ubicación | Estado | Fecha |
|-----------|-----------|--------|-------|
| Reglas Arquitectónicas | {{archivos.reglas_arquitectonicas}} | [⏳ Pendiente / ✅ Configurado] | [fecha] |
| Backlog | {{archivos.backlog}} | [⏳ Pendiente / ✅ Configurado] | [fecha] |
| ADRs | {{artifacts.adr_folder}} | [⏳ Pendiente / ✅ Configurado] | [fecha] |

> 💡 Para configurar reglas arquitectónicas: `>init_reglas_arquitectonicas`

---

## 📜 Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| [timestamp] | Análisis inicial | Generado por >tomar_contexto |

---

> **Archivo generado automáticamente.** Editar solo si hay correcciones manuales necesarias.
