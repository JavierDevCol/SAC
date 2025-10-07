# herramienta_plantilla.md
El propósito de un archivo de "Herramienta" es definir un proceso algorítmico y secuencial. Es un plan de acción claro y paso a paso. Es el "qué hacer".

**Herramienta:** Generador de Mensajes de Commit Convencionales

**Objetivo**
[cite_start]Analizar un `git diff` y generar un mensaje de commit claro y estandarizado siguiendo el estándar de Conventional Commits.

**Entradas Requeridas (Contexto)**
- **Principal:** El resultado de un `git diff` con los cambios a analizar.
- [cite_start]**Secundario (Opcional):** El contexto de la tarea o historia de usuario para ayudar en el "Análisis Contextual (El 'Porqué')"[cite: 5].

**Roles Autorizados:**
- `artesano_commits`
- `archdev_pro` (Sugerido, ya que un arquitecto también se beneficia de esto)

**Proceso Paso a Paso**
1.  **Análisis Contextual (El "Porqué"):**
    -   [cite_start]Sumergirse en el diff para entender la intención.
    -   [cite_start]Definir si el cambio es un bug, feature, mejora, etc[cite: 5].
    -   [cite_start]Agrupar los cambios lógicos en temas principales[cite: 6].

2.  **Clasificación de Patrones (Conventional Commits):**
    -   [cite_start]Clasificar el cambio usando uno de los tipos estándar: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `style`, `ci`, `build`, `chore`[cite: 11, 12, 13, 14, 15, 16, 17].

3.  **Construcción del Título (Subject):**
    -   [cite_start]Seguir estrictamente el formato `tipo(alcance): descripción`[cite: 19].
    -   [cite_start]El `alcance` es opcional e indica la parte del código afectada[cite: 20].
    -   [cite_start]La descripción debe usar el modo imperativo, empezar con mayúscula, no terminar con punto y ser concisa[cite: 21, 22].

4.  **Redacción de la Narrativa (Body):**
    -   [cite_start]Para commits no triviales, separar el cuerpo del título con una línea en blanco[cite: 24].
    -   [cite_start]Iniciar con un párrafo que explique el "porqué" del cambio[cite: 25].
    -   [cite_start]Usar una lista con viñetas (-) para detallar los cambios específicos ("qué" y "cómo")[cite: 26].
    -   [cite_start]Etiquetar cambios secundarios importantes dentro del cuerpo (ej. **fix:**, **test:**)[cite: 28, 31, 32].

5.  **Formato y Entrega Final:**
    -   [cite_start]Utilizar Markdown para maximizar la legibilidad[cite: 33].
    -   [cite_start]Entregar únicamente el mensaje de commit formateado como una "Propuesta"[cite: 34].

**Formato de Salida Esperado**
- Un único bloque de texto formateado que contiene el mensaje de commit completo.

**Manejo de Errores y Casos Borde**
- Si el `diff` es ambiguo o carece de contexto, solicitar al usuario más información sobre el objetivo del cambio antes de proceder.