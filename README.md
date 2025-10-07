# Sistema de Personalidades y Herramientas para IA

Este repositorio organiza los prompts de IA de forma modular. Para iniciar una sesión, debes combinar una **personalidad** con una o más **herramientas**.

## Cómo Usarlo

1.  **Elige una Personalidad:** Selecciona un archivo del directorio `/personas/`. Este definirá el rol, tono y conocimiento base de la IA.
2.  **Elige las Herramientas:** Selecciona uno o más archivos del directorio `/herramientas/`. Estas son las funcionalidades específicas que la personalidad podrá ejecutar.
3.  **Construye el Prompt Inicial:** Copia y pega el contenido de la personalidad seleccionada y, a continuación, el contenido de todas las herramientas elegidas en un único prompt para iniciar la sesión con la IA.

**Ejemplo de Prompt Inicial:**
> (Contenido de `personas/archdev_pro.md`)
>
> ---
>
> **HERRAMIENTAS DISPONIBLES:**
>
> (Contenido de `herramientas/verifica_pruebas.md`)
>
> (Contenido de `herramientas/define_arquitectura.md`)

Una vez cargado este prompt, puedes empezar a usar los comandos definidos en las herramientas.