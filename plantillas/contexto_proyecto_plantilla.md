# Contexto del Proyecto: [Nombre del Proyecto Detectado]

> **Último Análisis:** [Fecha y Hora del Análisis]  
> **Analizado por:** [Herramienta y Rol ejecutor]  
> **Nivel de Confianza:** [Alto/Medio/Bajo] basado en información disponible

---

## 1. Resumen del Proyecto

[Descripción extraída del README o inferida del análisis]

**Estado de Documentación:** [Completo/Básico/Pobre/Inexistente] - [Comentario breve sobre el estado]

---

## 2. Stack Tecnológico

- **Lenguaje Principal:** [Java 17, JavaScript ES2022, Python 3.11, etc.]
- **Framework Principal:** [Spring Boot 3.1.5, React 18, Django 4.2, etc.]
- **Base de Datos:** [PostgreSQL, MongoDB, Redis, etc.]
- **Seguridad:** [Spring Security, JWT, OAuth2, etc.]
- **Framework de Pruebas:** [JUnit 5, Jest, PyTest, etc.]
- **Contenerización:** [Docker, Podman, sin containerización]

---

## 3. Gestión y Comandos

- **Gestor de Dependencias:** [Maven, Gradle, NPM, pip, etc.]
- **Comandos Clave:**
  - `[Comando de build]`: [Descripción]
  - `[Comando de ejecución]`: [Descripción]
  - `[Comando de testing]`: [Descripción]
  - `[Comando de containerización]`: [Descripción]

---

## 4. Arquitectura y Patrones

- **Estilo Arquitectónico:** [Hexagonal, Capas, Event-Driven, MVC, etc.]
- **Nivel de Confianza:** [Alto/Medio/Bajo]
- **Patrones de Diseño Detectados:**
  - **[Patrón 1]:** [Descripción de implementación]
  - **[Patrón 2]:** [Descripción de implementación]
  - **[Patrón 3]:** [Descripción de implementación]

**Capas Identificadas:**
```
[Representación visual de las capas detectadas]

Ejemplo para Arquitectura Hexagonal:
🏛️ Domain Layer (Core Business)
├── model/ (Entidades de negocio)
├── repository/ (Contratos de persistencia)
└── service/ (Lógica de dominio)

🔄 Application Layer (Use Cases)
├── usecase/ (Casos de uso de la aplicación)
└── dto/ (Objetos de transferencia)

🔌 Infrastructure Layer (Adaptadores)
├── rest/ (API REST controllers)
├── persistence/ (Implementaciones de repositorios)
└── config/ (Configuración técnica)
```

---

## 5. Componentes Clave

- **Entidades Core del Dominio:**
  - `[paquete.Entidad1]` - [Descripción]
  - `[paquete.Entidad2]` - [Descripción]
  - `[paquete.Entidad3]` - [Descripción]

- **Casos de Uso / Servicios Principales:**
  - `[paquete.CasoDeUso1]` - [Descripción]
  - `[paquete.CasoDeUso2]` - [Descripción]

- **Puntos de Entrada (Controllers/Handlers):**
  - `[paquete.Controller1]` - [Descripción de endpoints]
  - `[paquete.Controller2]` - [Descripción de endpoints]

- **Clase Principal:**
  - `[paquete.MainClass]` - [Descripción]

---

## 6. Integraciones Externas

- **Base de Datos Primaria:**
  - [Tipo de BD] (configurado en [archivo de configuración])
  - [Gestor de migraciones] detectado en `[ruta de migraciones]`

- **APIs Documentadas:**
  - [Tipo de documentación] en `[ruta del archivo]`
  - Endpoints principales: [lista de endpoints]

- **Integraciones Detectadas:**
  - [Integración 1]: [Descripción]
  - [Integración 2]: [Descripción]

- **Mensajería/Eventos:**
  - [Sistema de mensajería si existe]

---

## 7. Configuración DevOps

- **Containerización:**
  - `Dockerfile`: [Descripción breve]
  - `docker-compose.yml`: [Descripción breve]
  - Puerto(s) expuesto(s): [lista de puertos]

- **CI/CD Pipeline:**
  - [Plataforma CI/CD] configurado en `[ruta del archivo]`
  - Pipeline: [descripción de stages]
  - **Oportunidades de mejora:** [si aplica]

- **Configuración de Entorno:**
  - `[archivo de configuración]` para configuración principal
  - Profiles detectados: [lista de profiles]
  - **Recomendación:** [si aplica]

- **Infrastructure as Code:**
  - [Herramienta IaC si existe]: [descripción]

---

## 8. Historial de Análisis

| Fecha | Herramienta | Descripción | Observaciones |
|-------|-------------|-------------|---------------|
| [timestamp] | tomar_contexto | Análisis inicial del proyecto | [observaciones] |

---

## 📊 Métricas de Calidad del Proyecto

| Aspecto | Puntuación | Observación |
|---------|------------|-------------|
| Estructura arquitectónica | [X]/10 | [comentario] |
| Stack tecnológico | [X]/10 | [comentario] |
| DevOps maturity | [X]/10 | [comentario] |
| Documentación | [X]/10 | [comentario] |
| Mantenibilidad | [X]/10 | [comentario] |

**Nivel de Confianza General:** [Alto/Medio/Bajo] ([X]/10)

---

## 💡 Recomendaciones

### 🔴 Críticas (Hacer Ahora)
1. [Recomendación crítica 1]
2. [Recomendación crítica 2]

### 🟡 Importantes (Próximas 2 semanas)
1. [Recomendación importante 1]
2. [Recomendación importante 2]

### 🟢 Mejoras Futuras
1. [Mejora futura 1]
2. [Mejora futura 2]

---

> **Nota:** Este archivo fue generado automáticamente por la herramienta `tomar_contexto`.  
> Última actualización: [timestamp]
