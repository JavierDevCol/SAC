# Reglas de Detección: Arquitectura

```yaml
descripcion: "Detección rápida de patrones arquitectónicos por estructura de carpetas"

# =============================================================================
# PATRONES ARQUITECTÓNICOS
# =============================================================================

patrones:

  hexagonal:
    nombre: "Hexagonal / Ports & Adapters"
    buscar:
      - "domain/ + infrastructure/"
      - "ports/ + adapters/"
      - "application/ + adapters/"
    archivos: ["*Port.*", "*Adapter.*"]
    regla: "Domain aislado, sin dependencias externas"

  clean:
    nombre: "Clean Architecture"
    buscar:
      - "entities/ + usecases/"
      - "usecases/ + adapters/ + frameworks/"
    archivos: ["*UseCase.*", "*Interactor.*", "*Presenter.*"]
    regla: "Capas concéntricas, dependencias hacia el centro"

  layered:
    nombre: "Arquitectura en Capas"
    buscar:
      - "controllers/ + services/ + repositories/"
      - "api/ + business/ + data/"
      - "handlers/ + services/ + store/"
    archivos: ["*Controller.*", "*Service.*", "*Repository.*"]
    regla: "Capas horizontales, típico MVC"

  ddd:
    nombre: "Domain-Driven Design"
    buscar:
      - "aggregates/ + valueobjects/"
      - "domain/events/ + domain/entities/"
      - "bounded-contexts/"
    archivos: ["*Aggregate.*", "*ValueObject.*", "*DomainEvent.*"]
    regla: "Modelo rico, aggregates como unidad de consistencia"

  modular:
    nombre: "Modular Monolith"
    buscar:
      - "modules/ con subcarpetas independientes"
      - "Cada módulo tiene api/ + internal/"
    archivos: ["*Module.*", "module.ts", "module.py"]
    regla: "Módulos con boundaries claros, deployment único"

  microservices:
    nombre: "Microservicios"
    buscar:
      - "services/ con múltiples subcarpetas"
      - "Múltiples Dockerfile"
      - "docker-compose.yml con varios servicios"
      - "k8s/ | kubernetes/"
    archivos: ["Dockerfile (múltiples)", "docker-compose.yml"]
    regla: "Servicios independientes, deployment separado"

  cqrs:
    nombre: "CQRS"
    buscar:
      - "commands/ + queries/"
      - "write/ + read/"
    archivos: ["*Command.*", "*Query.*", "*Handler.*"]
    regla: "Lectura y escritura separadas"

  vertical_slice:
    nombre: "Vertical Slice"
    buscar:
      - "features/ con subcarpetas por caso de uso"
      - "slices/"
    archivos: ["*Feature.*", "Handler + Request + Response juntos"]
    regla: "Organización por feature, no por capa"

# =============================================================================
# DETECCIÓN RÁPIDA
# =============================================================================

deteccion:
  pasos:
    1: "Buscar carpetas en src/ o raíz"
    2: "Comparar con patrones.buscar"
    3: "Si match ≥ 2 indicadores → patrón identificado"
    4: "Si no hay match claro → 'Arquitectura Personalizada'"

  combinaciones_frecuentes:
    - "Hexagonal + DDD"
    - "Clean + CQRS"
    - "Microservices + Event Sourcing"

# =============================================================================
# OUTPUT
# =============================================================================

output:
  formato: |
    **Arquitectura:** [nombre]
    **Indicadores:** [carpetas encontradas]
    **Confianza:** [Alta|Media|Baja]
```
