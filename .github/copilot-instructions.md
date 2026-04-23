# Instrucciones globales del proyecto
siempre que se realice un commit rectificar la version de SAC en SYSTEM_CONFIG y actualizar donde sea correspondiente, para esto se debe seguir el siguiente formato: `SAC_VERSION_X.Y.Z` donde X es la versión mayor, Y la menor y Z el parche. Ejemplo: `SAC_VERSION_1.0.0`
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

### Cuando modifiques un archivo, sigue estos pasos:
  - Crea una rama desde la última versión de `main` con el formato:
    `[breve-descripcion]` (kebab-case, solo minúsculas).
    Ejemplo: `agregar-login`.
  - Realiza un commit inicial vacío con el mensaje:
    `chore: iniciar desarrollo de HU [ID]`.
  - Si ya existe una rama distinta a main, haz un pull de main para mantener tu rama actualizada.
  - Realiza commits pequeños y frecuentes con mensajes claros siguiendo el formato de Conventional Commits.

### Commits (Conventional Commits)
Cada commit debe seguir el formato **Conventional Commits** con un mensaje claro y descriptivo:
- `feat:` — nueva funcionalidad (ejemplo: `feat: agregar validación de login`).
- `fix:` — corrección de errores (ejemplo: `fix: corregir redirección tras login`).
- `refactor:` — reestructuración sin cambio funcional.
- `docs:` — cambios en documentación.
- `chore:` — tareas de mantenimiento o configuración.

