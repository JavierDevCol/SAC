# Instrucciones globales del proyecto

## 🔹 Protocolo de Respuesta Estructurada (Obligatorio)
Para garantizar una interacción ágil, el agente debe seguir estas reglas al preguntar al usuario:
- **Opciones en Corchetes:** Toda pregunta debe incluir las opciones de respuesta rápida, mostrando en un **Snippet de Pregunta/Respuesta** en el chat: 
  > ** 🤷¿[Pregunta realizado por agente]?**
  > - [ICONO ACORDE] [Letra respuesta rapida] **Respuesta completa**
  Ejemplo:
  > ** 🤷¿Creo el archivo?**
  > - ✅ [S] **Sí **
  > - ❌ [N] **No **
  > - ✏️ [E] **Editar descripción.*

## Protocolo de modificación de archivos (Obligatorio)

### Rama de trabajo
- Crea una rama desde la última versión de `main` con el formato:
  `hu-[ID]-[breve-descripcion]` (kebab-case, solo minúsculas).
  Ejemplo: `hu-1234-agregar-login`.
- Realiza un commit inicial vacío con el mensaje:
  `chore: iniciar desarrollo de HU [ID]`.

### Commits (Conventional Commits)
Cada commit debe seguir el formato **Conventional Commits** con un mensaje claro y descriptivo:
- `feat:` — nueva funcionalidad (ejemplo: `feat: agregar validación de login`).
- `fix:` — corrección de errores (ejemplo: `fix: corregir redirección tras login`).
- `refactor:` — reestructuración sin cambio funcional.
- `docs:` — cambios en documentación.
- `chore:` — tareas de mantenimiento o configuración.

