# Guía Completa de Creación de Agentes Personalizados en VS Code Copilot

> **Fecha de actualización:** Enero 2026  
> **Versión de VS Code:** 1.96+  
> **Fuente:** Documentación oficial de VS Code Copilot Customization

## 📋 Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Visión General de Personalización](#2-visión-general-de-personalización)
3. [Instrucciones Personalizadas](#3-instrucciones-personalizadas-custom-instructions)
4. [Archivos de Prompt Reutilizables](#4-archivos-de-prompt-reutilizables-prompt-files)
5. [Agentes Personalizados](#5-agentes-personalizados-custom-agents)
6. [Habilidades de Agentes (Agent Skills/Tools)](#6-habilidades-de-agentes-agent-skillstools)
7. [Modelos de Lenguaje](#7-modelos-de-lenguaje-language-models)
8. [Servidores MCP](#8-servidores-mcp-model-context-protocol)
9. [Chat Participants (Extensiones Avanzadas)](#9-chat-participants-extensiones-avanzadas)
10. [Ejemplos Prácticos](#10-ejemplos-prácticos)
11. [Mejores Prácticas](#11-mejores-prácticas)

---

## 1. Introducción

VS Code Copilot ofrece múltiples niveles de personalización para adaptar la experiencia de IA a tus necesidades específicas. Desde simples instrucciones de texto hasta agentes completamente personalizados con herramientas y servidores MCP.

### Niveles de Personalización

```
┌─────────────────────────────────────────────────────────────┐
│                    PERSONALIZACIÓN COPILOT                  │
├─────────────────────────────────────────────────────────────┤
│  Nivel 1: Custom Instructions (.md)      → Fácil           │
│  Nivel 2: Prompt Files (.prompt.md)      → Fácil           │
│  Nivel 3: Custom Agents (.agent.md)      → Intermedio      │
│  Nivel 4: MCP Servers                    → Intermedio      │
│  Nivel 5: Chat Participants (Extension)  → Avanzado        │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Visión General de Personalización

### 2.1 Estructura de Archivos Recomendada

```
mi-proyecto/
├── .github/
│   ├── copilot-instructions.md      # Instrucciones globales del proyecto
│   └── prompts/                      # Prompts reutilizables
│       ├── code-review.prompt.md
│       ├── testing.prompt.md
│       └── documentation.prompt.md
├── .vscode/
│   ├── settings.json                 # Configuración de Copilot
│   └── mcp.json                      # Configuración de servidores MCP
├── agentes/
│   ├── backend-dev.agent.md          # Agente personalizado
│   ├── qa-engineer.agent.md
│   └── devops.agent.md
└── src/
    └── ...
```

### 2.2 Habilitación de Características Experimentales

Algunas características requieren habilitación manual en `settings.json`:

```json
{
  "chat.promptFiles": true,
  "chat.agent.enabled": true,
  "github.copilot.chat.experimental.agent.enabled": true
}
```

---

## 3. Instrucciones Personalizadas (Custom Instructions)

Las instrucciones personalizadas permiten definir reglas y preferencias que Copilot seguirá al generar código.

### 3.1 Archivo `.github/copilot-instructions.md`

Este archivo se carga automáticamente para todo el workspace:

```markdown
# Instrucciones para Copilot

## Contexto del Proyecto
Este es un proyecto de microservicios bancarios desarrollado en Java 21 con Spring Boot 3.x.

## Arquitectura
- Arquitectura Hexagonal (Ports & Adapters)
- Domain-Driven Design (DDD)
- Event-Driven con Apache Kafka

## Convenciones de Código

### Nomenclatura
- Clases: PascalCase (ej: `TransferenciaService`)
- Métodos: camelCase (ej: `procesarTransferencia`)
- Constantes: UPPER_SNAKE_CASE (ej: `MONTO_MAXIMO`)
- Paquetes: lowercase (ej: `com.banco.transferencias`)

### Estructura de Paquetes
```
src/main/java/com/banco/[modulo]/
├── domain/
│   ├── model/          # Entidades y Value Objects
│   ├── port/           # Interfaces (in/out)
│   └── service/        # Servicios de dominio
├── application/
│   ├── usecase/        # Casos de uso
│   └── dto/            # DTOs de aplicación
└── infrastructure/
    ├── adapter/        # Implementaciones de puertos
    ├── config/         # Configuración Spring
    └── persistence/    # Repositorios JPA
```

## Patrones Obligatorios
- Usar Records para DTOs inmutables
- Aplicar Builder pattern para objetos complejos
- Implementar Circuit Breaker en llamadas externas
- Validar entradas con Bean Validation (@Valid)

## Testing
- Framework: JUnit 5 + Mockito + AssertJ
- Cobertura mínima: 80%
- Usar Testcontainers para tests de integración
- Nombrar tests: should_[resultado]_when_[condicion]

## Seguridad
- NUNCA loguear datos sensibles (passwords, tokens, PII)
- Usar @PreAuthorize para control de acceso
- Sanitizar todas las entradas de usuario
```

### 3.2 Configuración en `settings.json`

Puedes especificar instrucciones adicionales por tipo de tarea:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/copilot-instructions.md"
    },
    {
      "text": "Siempre usar Optional en lugar de null para valores opcionales"
    },
    {
      "text": "Preferir composición sobre herencia"
    }
  ],
  
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Usar el patrón AAA (Arrange-Act-Assert) en todos los tests"
    },
    {
      "text": "Incluir tests para casos: feliz, borde, error"
    },
    {
      "text": "Usar @DisplayName con descripciones legibles"
    }
  ],
  
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "text": "Revisar: seguridad, rendimiento, mantenibilidad, SOLID"
    },
    {
      "text": "Identificar code smells y sugerir refactorings"
    }
  ],
  
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Usar Conventional Commits: tipo(scope): descripción"
    },
    {
      "text": "Tipos: feat, fix, refactor, test, docs, chore"
    }
  ]
}
```

### 3.3 Instrucciones por Lenguaje/Framework

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/copilot-instructions.md"
    },
    {
      "file": ".github/instructions/java-spring.md",
      "applyTo": "**/*.java"
    },
    {
      "file": ".github/instructions/typescript-react.md", 
      "applyTo": "**/*.{ts,tsx}"
    },
    {
      "file": ".github/instructions/python-fastapi.md",
      "applyTo": "**/*.py"
    }
  ]
}
```

---

## 4. Archivos de Prompt Reutilizables (Prompt Files)

Los `.prompt.md` son prompts reutilizables y bajo demanda. Pueden ser de workspace (se guardan en `.github/prompts`) o de usuario (en el perfil actual) y se ejecutan con `/nombre` o desde comandos de chat.

### 4.1 Alcance y ubicación
- Workspace: visibles solo en el proyecto, ruta recomendada `.github/prompts/` (configurable con `chat.promptFilesLocations`).
- Usuario (perfil): disponibles en todos los workspaces; se sincronizan opcionalmente con Settings Sync.

### 4.2 Estructura (frontmatter opcional)
```markdown
---
name: "create-react-form"          # si falta, usa el nombre de archivo
description: "Genera un formulario React tipado"
argument-hint: "formName=MyForm"
agent: agent                        # ask | edit | agent | <agente-personalizado>
model: gpt-4o                       # opcional; si falta usa el modelo seleccionado
tools:                              # herramientas disponibles; admite sets y MCP
  - codebase
  - terminal
  - azure-devops/*                 # todas las tools de un servidor MCP
---
```
Campos clave según la doc oficial:
- `description`: texto corto visible en sugerencias.
- `name`: comando tras `/` (por defecto el nombre del archivo).
- `argument-hint`: pista que aparece en la caja de entrada.
- `agent`: modo ask/edit/agent o el nombre de un agente custom. Si se listan herramientas y el agente actual es ask/edit, se usa `agent` por defecto.
- `model`: fuerza un modelo específico para este prompt.
- `tools`: lista de herramientas (integradas, sets, MCP o de extensiones). Un tool no disponible se ignora.

### 4.3 Cuerpo del prompt
- El cuerpo es el texto que se envía al modelo. Usa Markdown y enlaces relativos a archivos del workspace.
- Referencia herramientas en el cuerpo con `#tool:<nombre>`.
- Variables disponibles: `${workspaceFolder}`, `${workspaceFolderBasename}`, `${selection}`, `${selectedText}`, `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}`.
- Variables de entrada desde el chat: `${input:variable}` o `${input:variable:placeholder}`.

### 4.4 Crear un prompt file
1. Chat > Configure Chat (⚙️) > Prompt Files > New prompt file, o comandos `Chat: New Prompt File` / `Chat: New Untitled Prompt File`.
2. Elegir ubicación (workspace o perfil).
3. Nombrar el archivo (`.prompt.md`).
4. Rellenar frontmatter y cuerpo.

### 4.5 Ejecutar un prompt file
- En chat, escribir `/` y elegir el nombre; se pueden pasar argumentos (`/create-react-form formName=MyForm`).
- Comando `Chat: Run Prompt` desde la paleta.
- Botón play en el editor del prompt (en la barra de título) para correrlo en la sesión actual o nueva.
- Sugerencias automáticas configurables con `chat.promptFilesRecommendations`.

### 4.6 Prioridad de herramientas
Orden de disponibilidad:
1. `tools` declarados en el prompt file.
2. `tools` del agente custom referenciado en `agent` (si aplica).
3. `tools` por defecto del agente seleccionado.

### 4.7 Sincronización
Settings Sync puede sincronizar prompt files de usuario (perfil) si habilitas la opción de Prompts e Instructions.

### 4.8 Tips rápidos
- Describe claramente objetivo y formato de salida; incluye ejemplos de input/output.
- Usa variables `${selection}` e inputs `${input:var}` para hacer el prompt flexible.
- Prefiere enlazar instrucciones comunes en lugar de duplicarlas.
- Prueba el prompt con el botón play y ajusta según resultados.
### 🔴 Crítico (Debe corregirse)
[Lista de issues críticos]

### 🟡 Importante (Debería corregirse)
[Lista de mejoras importantes]

### 🟢 Sugerencias (Nice to have)
[Lista de sugerencias menores]

### ✅ Aspectos Positivos
[Lo que está bien implementado]
```

### 4.4 Uso de Prompt Files

En el chat de Copilot:

```
# Referenciar un prompt file
@workspace /code-review.prompt.md analiza este archivo

# O usando la sintaxis de archivo
#file:.github/prompts/code-review.prompt.md
```

---

## 5. Agentes Personalizados (Custom Agents)

Los agentes personalizados (`.agent.md`) son la forma más poderosa de crear asistentes especializados sin escribir código.

### 5.1 Estructura Básica de un Agente

```markdown
---
name: "Backend Developer"
description: "Experto en desarrollo backend con Java/Spring Boot"
tools:
  - codebase
  - terminal
  - fetch
model: gpt-4o
---

# Backend Developer Agent

Eres un desarrollador backend senior especializado en Java y Spring Boot.

## Tu Rol
- Implementar código limpio y mantenible
- Seguir principios SOLID y Clean Architecture
- Aplicar TDD en el desarrollo

## Instrucciones
[Instrucciones detalladas del agente]
```

### 5.2 Frontmatter del Agente

El frontmatter YAML define la configuración del agente:

```yaml
---
# Nombre del agente (requerido)
name: "Mi Agente"

# Descripción corta (requerido)
description: "Descripción de lo que hace el agente"

# Herramientas disponibles (opcional)
tools:
  - codebase      # Búsqueda en el código
  - terminal      # Ejecución de comandos
  - fetch         # Peticiones HTTP
  - useFetch      # Alias de fetch
  - visionTool    # Análisis de imágenes

# Modelo de lenguaje preferido (opcional)
model: gpt-4o    # o claude-sonnet, etc.

# Modo de operación (opcional)
mode: agent      # agent | ask | edit
---
```

### 5.3 Herramientas Disponibles para Agentes

| Herramienta | Descripción | Uso Común |
|-------------|-------------|-----------|
| `codebase` | Búsqueda semántica en el código | Encontrar implementaciones, referencias |
| `terminal` | Ejecutar comandos en terminal | Build, tests, scripts |
| `fetch` | Realizar peticiones HTTP | APIs, documentación externa |
| `useFetch` | Alias de fetch | - |
| `visionTool` | Análisis de imágenes | Diagramas, mockups |
| `githubRepo` | Acceso a repositorios GitHub | Buscar código en repos externos |
| `extensions` | Herramientas de extensiones | MCP tools, custom tools |

### 5.4 Ejemplo Completo: Agente de Arquitectura

Archivo: `agentes/arquitecto-software.agent.md`

```markdown
---
name: "Arquitecto de Software"
description: "Diseña arquitecturas robustas y escalables"
tools:
  - codebase
  - terminal
  - fetch
model: gpt-4o
---

# 🏛️ Arquitecto de Software

## Identidad

Soy un arquitecto de software senior con más de 15 años de experiencia 
diseñando sistemas distribuidos de alta disponibilidad.

## Especialización

### Patrones Arquitectónicos
- Microservicios y arquitectura orientada a eventos
- Clean Architecture / Hexagonal
- CQRS y Event Sourcing
- Domain-Driven Design (DDD)

### Tecnologías
- **Backend:** Java, Spring Boot, Kotlin
- **Mensajería:** Kafka, RabbitMQ
- **Bases de datos:** PostgreSQL, MongoDB, Redis
- **Cloud:** AWS, Azure, Kubernetes

## Proceso de Trabajo

### Al Recibir un Requerimiento

1. **Entender el Contexto**
   - ¿Cuál es el problema de negocio?
   - ¿Cuáles son los requisitos no funcionales?
   - ¿Qué restricciones técnicas existen?

2. **Analizar Opciones**
   - Evaluar al menos 3 alternativas arquitectónicas
   - Documentar trade-offs de cada opción
   - Considerar: escalabilidad, mantenibilidad, costo

3. **Proponer Solución**
   - Diagrama de arquitectura (C4 Model)
   - Justificación técnica de decisiones
   - Plan de implementación por fases

4. **Documentar**
   - Generar ADR (Architecture Decision Record)
   - Actualizar documentación del sistema

## Restricciones

### NUNCA
- Proponer soluciones sin entender el contexto completo
- Ignorar requisitos no funcionales
- Diseñar sin considerar la operación (DevOps)
- Crear acoplamientos innecesarios entre módulos

### SIEMPRE
- Preguntar antes de asumir
- Justificar decisiones con principios y evidencia
- Considerar el costo total de propiedad (TCO)
- Diseñar para el cambio (extensibilidad)

## Formato de Respuestas

### Para Decisiones Arquitectónicas

```
## 📋 Contexto
[Descripción del problema]

## 🎯 Decisión
[Solución elegida]

## ✅ Consecuencias Positivas
- [Beneficio 1]
- [Beneficio 2]

## ⚠️ Consecuencias Negativas
- [Trade-off 1]
- [Trade-off 2]

## 🔄 Alternativas Consideradas
1. [Alternativa 1] - Descartada porque...
2. [Alternativa 2] - Descartada porque...
```

## Comandos Especiales

- `/analizar` - Analiza la arquitectura actual del proyecto
- `/proponer` - Propone mejoras arquitectónicas
- `/adr` - Genera un Architecture Decision Record
- `/diagrama` - Genera diagrama de arquitectura (C4)
```

### 5.5 Invocación de Agentes

```
# En el chat de VS Code
@arquitecto-software analiza la arquitectura actual del módulo de pagos

@arquitecto-software /proponer cómo escalar el sistema para 10x usuarios

@arquitecto-software /adr migración de monolito a microservicios
```

---

## 6. Habilidades de Agentes (Agent Skills/Tools)

Las herramientas permiten a los agentes interactuar con el entorno de desarrollo.

### 6.1 Herramientas Integradas

#### `codebase` - Búsqueda en Código
```markdown
tools:
  - codebase
```
Permite al agente:
- Buscar definiciones de funciones/clases
- Encontrar referencias y usos
- Analizar dependencias
- Navegar la estructura del proyecto

#### `terminal` - Ejecución de Comandos
```markdown
tools:
  - terminal
```
Permite al agente:
- Ejecutar comandos de build
- Correr tests
- Ejecutar scripts
- Interactuar con Git

#### `fetch` - Peticiones HTTP
```markdown
tools:
  - fetch
```
Permite al agente:
- Consultar documentación externa
- Acceder a APIs
- Descargar recursos

### 6.2 Herramientas de Extensiones (MCP)

Los agentes pueden usar herramientas proporcionadas por servidores MCP:

```markdown
---
name: "DevOps Agent"
tools:
  - codebase
  - terminal
  - mcp: azure-devops  # Herramientas del servidor MCP
---
```

### 6.3 Creación de Herramientas Personalizadas (via Extensión)

Para herramientas más avanzadas, puedes crear una extensión VS Code:

```typescript
import * as vscode from 'vscode';

// Definir la herramienta
const analizadorCodigo: vscode.LanguageModelTool<{ 
  filePath: string;
  analysisType: string;
}> = {
  async invoke(options, token) {
    const { filePath, analysisType } = options.input;
    
    // Lógica de análisis
    const resultado = await analizarArchivo(filePath, analysisType);
    
    return new vscode.LanguageModelToolResult([
      new vscode.LanguageModelTextPart(JSON.stringify(resultado))
    ]);
  },

  async prepareInvocation(options, token) {
    return {
      invocationMessage: `Analizando ${options.input.filePath}...`
    };
  }
};

// Registrar la herramienta
export function activate(context: vscode.ExtensionContext) {
  const tool = vscode.lm.registerTool(
    'mi-extension.analizador-codigo', 
    analizadorCodigo
  );
  context.subscriptions.push(tool);
}
```

---

## 7. Modelos de Lenguaje (Language Models)

### 7.1 Modelos Disponibles

VS Code Copilot soporta múltiples modelos de lenguaje:

| Modelo | Vendor | Características |
|--------|--------|-----------------|
| `gpt-4o` | copilot | Más capaz, mejor razonamiento |
| `gpt-4o-mini` | copilot | Más rápido, menor costo |
| `gpt-3.5-turbo` | copilot | Rápido, casos simples |
| `claude-3.5-sonnet` | copilot | Alternativa de Anthropic |
| `o1-preview` | copilot | Razonamiento avanzado |
| `o1-mini` | copilot | Razonamiento, más rápido |

### 7.2 Selección de Modelo en Agentes

```markdown
---
name: "Agente de Análisis Complejo"
model: gpt-4o
---
```

### 7.3 Selección Programática de Modelos

```typescript
// Seleccionar modelo específico
const [model] = await vscode.lm.selectChatModels({
  vendor: 'copilot',
  family: 'gpt-4o'
});

// Seleccionar cualquier modelo disponible
const models = await vscode.lm.selectChatModels({
  vendor: 'copilot'
});

// Verificar disponibilidad
if (models.length === 0) {
  console.log('No hay modelos disponibles');
  return;
}

// Usar el modelo
const response = await model.sendRequest(messages, {}, token);
```

### 7.4 Propiedades del Modelo

```typescript
interface LanguageModelChat {
  readonly name: string;           // Nombre legible
  readonly id: string;             // Identificador único
  readonly vendor: string;         // Proveedor (copilot, etc.)
  readonly family: string;         // Familia (gpt-4o, etc.)
  readonly version: string;        // Versión específica
  readonly maxInputTokens: number; // Límite de tokens de entrada
  
  sendRequest(...): Promise<LanguageModelChatResponse>;
  countTokens(text: string): Promise<number>;
}
```

---

## 8. Servidores MCP (Model Context Protocol)

MCP permite conectar Copilot con servicios externos para ampliar sus capacidades.

### 8.1 ¿Qué es MCP?

El Model Context Protocol es un estándar abierto que permite:
- Conectar herramientas externas a Copilot
- Proporcionar contexto adicional al modelo
- Ejecutar acciones en sistemas externos

### 8.2 Configuración de Servidores MCP

Archivo: `.vscode/mcp.json`

```json
{
  "servers": {
    "azure-devops": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-azure-devops"],
      "env": {
        "AZURE_DEVOPS_ORG": "mi-organizacion",
        "AZURE_DEVOPS_PAT": "${env:AZURE_DEVOPS_PAT}"
      }
    },
    "github": {
      "type": "stdio", 
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "${env:DATABASE_URL}"
      }
    },
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y", 
        "@modelcontextprotocol/server-filesystem",
        "/ruta/permitida/1",
        "/ruta/permitida/2"
      ]
    }
  }
}
```

### 8.3 Tipos de Servidores MCP

#### Servidor stdio (más común)
```json
{
  "mi-servidor": {
    "type": "stdio",
    "command": "node",
    "args": ["./mi-servidor-mcp.js"],
    "env": {
      "API_KEY": "${env:MI_API_KEY}"
    }
  }
}
```

#### Servidor SSE (Server-Sent Events)
```json
{
  "mi-servidor-sse": {
    "type": "sse",
    "url": "http://localhost:3000/mcp",
    "headers": {
      "Authorization": "Bearer ${env:TOKEN}"
    }
  }
}
```

### 8.4 Servidores MCP Populares

| Servidor | Descripción | Instalación |
|----------|-------------|-------------|
| `@modelcontextprotocol/server-github` | Operaciones en GitHub | `npx -y @modelcontextprotocol/server-github` |
| `@modelcontextprotocol/server-postgres` | Consultas PostgreSQL | `npx -y @modelcontextprotocol/server-postgres` |
| `@modelcontextprotocol/server-filesystem` | Acceso a archivos | `npx -y @modelcontextprotocol/server-filesystem` |
| `@modelcontextprotocol/server-slack` | Integración Slack | `npx -y @modelcontextprotocol/server-slack` |
| `@anthropic/mcp-server-azure-devops` | Azure DevOps | `npx -y @anthropic/mcp-server-azure-devops` |

### 8.5 Crear un Servidor MCP Personalizado

Estructura básica de un servidor MCP en Node.js:

```typescript
// mi-servidor-mcp.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server({
  name: 'mi-servidor-mcp',
  version: '1.0.0'
}, {
  capabilities: {
    tools: {}
  }
});

// Registrar herramientas
server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'buscar_usuarios',
      description: 'Busca usuarios en el sistema',
      inputSchema: {
        type: 'object',
        properties: {
          query: {
            type: 'string',
            description: 'Término de búsqueda'
          }
        },
        required: ['query']
      }
    }
  ]
}));

// Implementar herramientas
server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  if (name === 'buscar_usuarios') {
    const resultado = await buscarUsuarios(args.query);
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(resultado)
        }
      ]
    };
  }
  
  throw new Error(`Herramienta desconocida: ${name}`);
});

// Iniciar servidor
const transport = new StdioServerTransport();
server.connect(transport);
```

### 8.6 Uso de MCP en Agentes

```markdown
---
name: "DevOps Manager"
description: "Gestiona Azure DevOps y GitHub"
tools:
  - codebase
  - terminal
  - mcp: azure-devops
  - mcp: github
---

# DevOps Manager

Soy un agente especializado en gestión de DevOps.

## Capacidades

### Azure DevOps
- Gestionar Work Items
- Consultar Pipelines
- Revisar Pull Requests
- Gestionar Repositorios

### GitHub
- Crear Issues
- Gestionar PRs
- Consultar Actions
- Gestionar Releases
```

---

## 9. Chat Participants (Extensiones Avanzadas)

Para máxima flexibilidad, puedes crear Chat Participants como extensiones VS Code.

### 9.1 Estructura del Proyecto

```
mi-chat-participant/
├── package.json
├── tsconfig.json
├── src/
│   ├── extension.ts
│   ├── participant.ts
│   └── prompts/
│       └── base-prompt.ts
└── assets/
    └── icon.png
```

### 9.2 Configuración del `package.json`

```json
{
  "name": "mi-chat-participant",
  "displayName": "Mi Asistente de Desarrollo",
  "version": "1.0.0",
  "engines": {
    "vscode": "^1.96.0"
  },
  "categories": ["Chat"],
  "activationEvents": [
    "onChatParticipant:mi-extension.asistente"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "chatParticipants": [
      {
        "id": "mi-extension.asistente",
        "fullName": "Asistente de Desarrollo",
        "name": "dev",
        "description": "Tu asistente de desarrollo personalizado",
        "isSticky": true,
        "commands": [
          {
            "name": "review",
            "description": "Realiza code review del código seleccionado"
          },
          {
            "name": "test",
            "description": "Genera tests para el código seleccionado"
          },
          {
            "name": "refactor",
            "description": "Sugiere refactorizaciones"
          },
          {
            "name": "explain",
            "description": "Explica el código seleccionado"
          }
        ]
      }
    ]
  },
  "dependencies": {
    "@vscode/prompt-tsx": "^0.2.0"
  }
}
```

### 9.3 Implementación del Chat Participant

```typescript
// src/extension.ts
import * as vscode from 'vscode';

const BASE_PROMPT = `Eres un asistente de desarrollo experto. 
Ayudas a los desarrolladores a escribir código limpio, testeable y mantenible.
Sigues las mejores prácticas de la industria y los principios SOLID.`;

const REVIEW_PROMPT = `Realiza un code review exhaustivo. Evalúa:
1. Seguridad - vulnerabilidades potenciales
2. Rendimiento - posibles cuellos de botella
3. Mantenibilidad - código limpio y legible
4. SOLID - cumplimiento de principios
5. Testing - cobertura y calidad de tests`;

const TEST_PROMPT = `Genera tests completos usando:
- JUnit 5 para tests unitarios
- Mockito para mocks
- AssertJ para assertions fluidas
- Patrón AAA (Arrange-Act-Assert)
Incluye: casos felices, casos de borde, casos de error.`;

const REFACTOR_PROMPT = `Analiza el código e identifica oportunidades de refactoring:
- Code smells y cómo eliminarlos
- Patrones de diseño aplicables
- Simplificación de lógica compleja
- Mejora de nombres y estructura`;

const handler: vscode.ChatRequestHandler = async (
  request: vscode.ChatRequest,
  context: vscode.ChatContext,
  stream: vscode.ChatResponseStream,
  token: vscode.CancellationToken
) => {
  // Seleccionar prompt según comando
  let systemPrompt = BASE_PROMPT;
  
  switch (request.command) {
    case 'review':
      systemPrompt = REVIEW_PROMPT;
      break;
    case 'test':
      systemPrompt = TEST_PROMPT;
      break;
    case 'refactor':
      systemPrompt = REFACTOR_PROMPT;
      break;
  }

  // Construir mensajes
  const messages: vscode.LanguageModelChatMessage[] = [
    vscode.LanguageModelChatMessage.User(systemPrompt),
  ];

  // Agregar historial de conversación
  for (const turn of context.history) {
    if (turn instanceof vscode.ChatRequestTurn) {
      messages.push(vscode.LanguageModelChatMessage.User(turn.prompt));
    } else if (turn instanceof vscode.ChatResponseTurn) {
      let responseText = '';
      for (const part of turn.response) {
        if (part instanceof vscode.ChatResponseMarkdownPart) {
          responseText += part.value.value;
        }
      }
      messages.push(vscode.LanguageModelChatMessage.Assistant(responseText));
    }
  }

  // Agregar referencias (código seleccionado, archivos)
  if (request.references.length > 0) {
    let referencesText = '\n\n## Contexto proporcionado:\n';
    for (const ref of request.references) {
      if (ref.value instanceof vscode.Uri) {
        referencesText += `\nArchivo: ${ref.value.fsPath}`;
      } else if (typeof ref.value === 'string') {
        referencesText += `\n${ref.value}`;
      }
    }
    messages.push(vscode.LanguageModelChatMessage.User(referencesText));
  }

  // Agregar mensaje del usuario
  messages.push(vscode.LanguageModelChatMessage.User(request.prompt));

  try {
    // Enviar solicitud al modelo
    const chatResponse = await request.model.sendRequest(messages, {}, token);

    // Transmitir respuesta con streaming
    for await (const fragment of chatResponse.text) {
      stream.markdown(fragment);
    }
  } catch (err) {
    handleError(err, stream);
  }
};

function handleError(err: unknown, stream: vscode.ChatResponseStream) {
  if (err instanceof vscode.LanguageModelError) {
    console.error(`Error del modelo: ${err.message}`, err.code);
    
    if (err.cause instanceof Error && err.cause.message.includes('off_topic')) {
      stream.markdown('Lo siento, esa pregunta está fuera de mi área de especialización.');
    } else if (err.code === 'quota_exceeded') {
      stream.markdown('Se ha excedido la cuota. Por favor, intenta más tarde.');
    } else {
      stream.markdown('Ocurrió un error al procesar tu solicitud.');
    }
  } else {
    throw err;
  }
}

export function activate(context: vscode.ExtensionContext) {
  // Crear el chat participant
  const participant = vscode.chat.createChatParticipant(
    'mi-extension.asistente',
    handler
  );

  // Configurar icono
  participant.iconPath = vscode.Uri.joinPath(
    context.extensionUri,
    'assets',
    'icon.png'
  );

  context.subscriptions.push(participant);
  
  console.log('Chat Participant "Asistente de Desarrollo" activado');
}

export function deactivate() {}
```

### 9.4 Uso de Herramientas en Chat Participants

```typescript
const handlerWithTools: vscode.ChatRequestHandler = async (
  request, context, stream, token
) => {
  // Obtener herramientas disponibles
  const tools = vscode.lm.tools.filter(
    tool => tool.tags.includes('mi-extension')
  );

  // Verificar si el usuario quiere usar herramientas
  if (request.toolReferences.length > 0) {
    for (const toolRef of request.toolReferences) {
      stream.progress(`Ejecutando ${toolRef.name}...`);
      
      try {
        const result = await vscode.lm.invokeTool(
          toolRef.name,
          { input: { query: request.prompt } },
          token
        );
        
        stream.markdown(`**Resultado de ${toolRef.name}:**\n`);
        // Procesar resultado...
      } catch (err) {
        stream.markdown(`Error al ejecutar ${toolRef.name}`);
      }
    }
  }

  // Enviar al modelo con herramientas disponibles
  const response = await request.model.sendRequest(messages, {
    tools: tools.map(t => ({
      name: t.name,
      description: t.description,
      inputSchema: t.inputSchema
    })),
    toolMode: vscode.LanguageModelChatToolMode.Auto
  }, token);

  // Procesar respuesta...
};
```

### 9.5 Uso con prompt-tsx

```tsx
// src/prompts/my-prompt.tsx
import {
  UserMessage,
  AssistantMessage,
  PromptElement,
  BasePromptElementProps,
  PrioritizedList,
} from '@vscode/prompt-tsx';

interface MyPromptProps extends BasePromptElementProps {
  history: ChatContext['history'];
  userQuery: string;
  systemPrompt: string;
}

export class MyPrompt extends PromptElement<MyPromptProps> {
  render() {
    return (
      <>
        {/* Instrucciones base - máxima prioridad */}
        <UserMessage priority={100}>
          {this.props.systemPrompt}
        </UserMessage>
        
        {/* Historial - prioridad media */}
        <PrioritizedList priority={50} descending={false}>
          {this.renderHistory()}
        </PrioritizedList>
        
        {/* Query del usuario - alta prioridad */}
        <UserMessage priority={90}>
          {this.props.userQuery}
        </UserMessage>
      </>
    );
  }

  private renderHistory() {
    return this.props.history.map((turn, i) => {
      if (turn instanceof ChatRequestTurn) {
        return <UserMessage key={i}>{turn.prompt}</UserMessage>;
      } else if (turn instanceof ChatResponseTurn) {
        return (
          <AssistantMessage key={i} name={turn.participant}>
            {this.extractMarkdown(turn)}
          </AssistantMessage>
        );
      }
    });
  }

  private extractMarkdown(turn: ChatResponseTurn): string {
    return turn.response
      .filter(r => r instanceof ChatResponseMarkdownPart)
      .map(r => (r as ChatResponseMarkdownPart).value.value)
      .join('');
  }
}
```

---

## 10. Ejemplos Prácticos

### 10.1 Agente Completo: Backend Developer

Archivo: `agentes/backend-dev.agent.md`

```markdown
---
name: "Backend Developer Pro"
description: "Desarrollador backend experto en Java/Spring Boot con enfoque TDD"
tools:
  - codebase
  - terminal
model: gpt-4o
---

# 🔧 Backend Developer Pro

## Identidad

Soy un desarrollador backend senior con experiencia en sistemas distribuidos 
de alta disponibilidad. Mi enfoque principal es escribir código limpio, 
testeable y mantenible.

## Stack Tecnológico

### Principal
- **Lenguaje:** Java 21 (Records, Pattern Matching, Virtual Threads)
- **Framework:** Spring Boot 3.x, Spring Framework 6.x
- **Build:** Maven/Gradle
- **Testing:** JUnit 5, Mockito, AssertJ, Testcontainers

### Secundario
- **Mensajería:** Apache Kafka, RabbitMQ
- **BD:** PostgreSQL, MongoDB, Redis
- **Cloud:** AWS (ECS, Lambda, RDS), Kubernetes

## Principios de Trabajo

### Arquitectura
1. **Clean Architecture / Hexagonal**
   - Dominio en el centro, sin dependencias externas
   - Puertos y adaptadores para infraestructura
   - Inversión de dependencias estricta

2. **Domain-Driven Design**
   - Bounded Contexts bien definidos
   - Agregados con invariantes protegidas
   - Eventos de dominio para comunicación

### Código
1. **SOLID siempre**
   - Single Responsibility: una razón para cambiar
   - Open/Closed: abierto a extensión, cerrado a modificación
   - Liskov Substitution: subtipos intercambiables
   - Interface Segregation: interfaces específicas
   - Dependency Inversion: depender de abstracciones

2. **Clean Code**
   - Nombres descriptivos y auto-explicativos
   - Funciones pequeñas (< 20 líneas)
   - Sin comentarios obvios (el código se explica solo)
   - DRY: no repetir lógica

### Testing
1. **TDD Estricto**
   - 🔴 Red: Escribir test que falla
   - 🟢 Green: Código mínimo para pasar
   - 🔵 Refactor: Mejorar sin romper tests

2. **Pirámide de Tests**
   - 70% Unitarios (rápidos, aislados)
   - 20% Integración (Testcontainers)
   - 10% E2E (flujos críticos)

## Proceso de Implementación

### Al Recibir una Tarea

```
1. ENTENDER
   ├── ¿Cuál es el requisito de negocio?
   ├── ¿Qué casos de uso cubre?
   └── ¿Hay restricciones técnicas?

2. DISEÑAR
   ├── Identificar entidades y value objects
   ├── Definir interfaces (puertos)
   └── Planificar estructura de paquetes

3. IMPLEMENTAR (TDD)
   ├── Escribir test del caso feliz
   ├── Implementar código mínimo
   ├── Escribir tests de borde y error
   ├── Refactorizar si es necesario
   └── Verificar cobertura (>80%)

4. REVISAR
   ├── Code review mental (SOLID, Clean Code)
   ├── Verificar manejo de errores
   └── Confirmar que es testeable
```

## Comandos

- `/impl [descripción]` - Implementar funcionalidad con TDD
- `/test [clase/método]` - Generar tests para código existente
- `/review [código]` - Code review con sugerencias
- `/refactor [código]` - Proponer refactorizaciones

## Formato de Respuestas

### Para Implementaciones

```
## 📋 Análisis del Requisito
[Entendimiento del problema]

## 🧪 Tests (TDD - Red)
[Código de tests]

## 💻 Implementación (Green)
[Código de producción]

## 🔄 Refactoring (si aplica)
[Mejoras al código]

## ✅ Verificación
- [ ] Tests pasan
- [ ] Cobertura > 80%
- [ ] SOLID cumplido
- [ ] Sin code smells
```

## Restricciones

### ❌ NUNCA
- Escribir código sin test primero
- Acoplar dominio con infraestructura
- Ignorar casos de error
- Usar null (preferir Optional)
- Crear God classes (> 200 líneas)
- Hardcodear configuración

### ✅ SIEMPRE
- Test first (TDD)
- Validar inputs
- Manejar excepciones explícitamente
- Usar inyección de dependencias
- Documentar decisiones no obvias
- Considerar concurrencia
```

### 10.2 Servidor MCP: Azure DevOps

Archivo: `.vscode/mcp.json`

```json
{
  "servers": {
    "azure-devops": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-azure-devops"],
      "env": {
        "AZURE_DEVOPS_ORG_URL": "https://dev.azure.com/mi-organizacion",
        "AZURE_DEVOPS_PAT": "${env:AZURE_DEVOPS_PAT}",
        "AZURE_DEVOPS_DEFAULT_PROJECT": "MiProyecto"
      }
    }
  }
}
```

Agente que usa el servidor MCP:

```markdown
---
name: "Azure DevOps Manager"
description: "Gestiona work items, PRs y pipelines en Azure DevOps"
tools:
  - codebase
  - mcp: azure-devops
---

# Azure DevOps Manager

## Capacidades

Puedo ayudarte a gestionar tu proyecto en Azure DevOps:

### Work Items
- Crear y actualizar User Stories, Tasks, Bugs
- Consultar backlog y sprints
- Asignar y priorizar trabajo

### Pull Requests
- Listar PRs activos
- Revisar cambios y comentarios
- Aprobar o solicitar cambios

### Pipelines
- Consultar estado de builds
- Disparar pipelines
- Revisar logs de ejecución

## Comandos

- `/workitems` - Listar work items del sprint actual
- `/prs` - Listar Pull Requests activos
- `/pipelines` - Estado de pipelines recientes
- `/create-task [título]` - Crear nueva tarea
```

---

## 11. Mejores Prácticas

### 11.1 Para Instrucciones Personalizadas

✅ **Hacer:**
- Ser específico sobre convenciones de código
- Incluir ejemplos de patrones preferidos
- Documentar la estructura del proyecto
- Especificar frameworks y versiones

❌ **Evitar:**
- Instrucciones demasiado genéricas
- Contradicciones entre instrucciones
- Información desactualizada
- Exceso de restricciones que limiten la utilidad

### 11.2 Para Agentes Personalizados

✅ **Hacer:**
- Definir un rol claro y específico
- Incluir proceso de trabajo detallado
- Especificar formato de respuestas
- Documentar comandos disponibles
- Establecer restricciones claras

❌ **Evitar:**
- Agentes demasiado genéricos (hacen todo)
- Prompts excesivamente largos
- Falta de estructura en las instrucciones
- Ignorar casos de error

### 11.3 Para Servidores MCP

✅ **Hacer:**
- Usar variables de entorno para secrets
- Documentar las herramientas disponibles
- Manejar errores gracefully
- Limitar permisos al mínimo necesario

❌ **Evitar:**
- Hardcodear credenciales
- Dar acceso excesivo a recursos
- Ignorar timeouts y límites
- Falta de logging

### 11.4 Para Chat Participants

✅ **Hacer:**
- Implementar streaming para respuestas largas
- Manejar todos los tipos de error
- Usar el historial de conversación
- Respetar tokens de cancelación

❌ **Evitar:**
- Bloquear la UI con operaciones largas
- Ignorar errores del modelo
- Prompts hardcodeados sin flexibilidad
- Falta de feedback al usuario

---

## Referencias

### Documentación Oficial
- [VS Code Copilot Customization Overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Language Models](https://code.visualstudio.com/docs/copilot/customization/language-models)
- [MCP Servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

### APIs y SDKs
- [VS Code Chat Extension API](https://code.visualstudio.com/api/extension-guides/chat)
- [Language Model API](https://code.visualstudio.com/api/extension-guides/language-model)
- [MCP SDK](https://github.com/modelcontextprotocol/sdk)
- [prompt-tsx](https://github.com/microsoft/vscode-prompt-tsx)

### Ejemplos
- [Chat Participant Sample](https://github.com/microsoft/vscode-extension-samples/tree/main/chat-sample)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

---

> **Última actualización:** Enero 2026  
> **Versión de VS Code:** 1.96+  
> **Autor:** Generado con información de la documentación oficial de VS Code
