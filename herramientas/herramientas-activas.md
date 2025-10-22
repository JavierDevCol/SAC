# Herramientas Activas del Sistema

Esta es la lista oficial de herramientas disponibles en el orquestador. Cada herramienta indica qué roles pueden activarla.

| Nombre de la Herramienta | Comando | Roles que Pueden Activarla | Ruta del Archivo |
|---------------------------|---------|----------------------------|------------------|
| Tomar Contexto | tomar_contexto | ONAD, ARCHDEV, DEVOPS, REFINADOR | herramientas/tomar_contexto.md |
| Definir Arquitectura | define_arquitectura | ONAD | herramientas/define_arquitectura.md |
| Generar ADR | generar_adr | ONAD, ARCHDEV | herramientas/generar_adr.md |
| Refactorizar | refactorizar | ARCHDEV | herramientas/refactorizar.md |
| Analizar Code Smells | analizar_code_smells | ARCHDEV | herramientas/analizar_code_smells.md |
| Solucionar Smells | solucionar_smells | ARCHDEV | herramientas/solucionar_smells.md |
| Crear Pruebas | crear_pruebas | ARCHDEV | herramientas/crear_pruebas.md |
| Verificar Pruebas | verifica_pruebas | ARCHDEV | herramientas/verifica_pruebas.md |
| Ejecutar Plan | ejecutar_plan | ARCHDEV | herramientas/ejecutar_plan.md |
| Generar Commit | generar_commit | ARTESANO | herramientas/generar_commit.md |
| Diagnosticar DevOps | diagnosticar_devops | DEVOPS | herramientas/diagnosticar_devops.md |
| Refinar HU | refinar_hu | REFINADOR | herramientas/refinar_hu.md |
| Validar HU | validar_hu | ONAD | herramientas/validar_hu.md |
| Planificar HU | planificar_hu | ONAD | herramientas/planificar_hu.md |
| Asignar Responsable | asignar_responsable | ORQUESTADOR | herramientas/asignar_responsable.md |

---

## Uso

Para activar una herramienta, usa cualquiera de estos formatos (con un rol activo, validando en el archivo `artefactos/session_state.json`):
- `> <nombre_herramienta>`
- `-> <nombre_herramienta>`

**Ejemplos:**
- `> tomar_contexto`
- `-> refactorizar`

---

## Validaciones

### Herramienta sin Rol Activo

Si se intenta activar una herramienta **SIN tener un rol activo** en la sesión:

1. **Mostrar error:**
   ```
   ❌ No hay ningún rol activo. Las herramientas solo pueden ejecutarse cuando un rol está cargado.
   ```

2. **Buscar roles compatibles:**
   - Leer la tabla anterior
   - Buscar la herramienta en la columna "Nombre de la Herramienta"
   - Obtener la lista de roles de la columna "Roles que Pueden Activarla"

3. **Sugerir roles compatibles:**
   ```
   💡 La herramienta '[nombre_herramienta]' puede ser activada por los siguientes roles:
   
   • [ROL_1] - Usar: /cochas +[COMANDO_1]
   • [ROL_2] - Usar: /cochas +[COMANDO_2]
   ```

4. **Abortar ejecución:**
   - No se ejecuta la herramienta
   - Se espera a que el usuario active un rol apropiado

**Ejemplo:**
```
Usuario: > refactorizar

Sistema: ❌ No hay ningún rol activo. Las herramientas solo pueden ejecutarse cuando un rol está cargado.

         💡 La herramienta 'refactorizar' puede ser activada por los siguientes roles:
         
         • ArchDev Pro - Usar: /cochas +ARCHDEV
```

---

### Herramienta No Compatible con Rol Activo

Si se intenta activar una herramienta **con un rol activo incompatible**:

1. **Mostrar error:**
   ```
   ❌ El rol activo '[nombre_rol]' no puede ejecutar la herramienta '[nombre_herramienta]'.
   ```

2. **Sugerir roles compatibles:**
   ```
   💡 La herramienta '[nombre_herramienta]' puede ser activada por:
   
   • [ROL_1] - Usar: /cochas +[COMANDO_1]
   • [ROL_2] - Usar: /cochas +[COMANDO_2]
   
   ¿Deseas cambiar de rol?
   ```

**Ejemplo:**
```
Usuario: > diagnosticar_devops
(Rol activo: ArchDev Pro)

Sistema: ❌ El rol activo 'ArchDev Pro' no puede ejecutar la herramienta 'diagnosticar_devops'.

         💡 La herramienta 'diagnosticar_devops' puede ser activada por:
         
         • Arquitecto DevOps - Usar: /cochas +DEVOPS
         
         ¿Deseas cambiar de rol?
```

---

### Herramienta No Encontrada

Si la herramienta solicitada **NO existe** en la tabla:

1. **Mostrar error:**
   ```
   ❌ La herramienta '[nombre_herramienta]' no existe en el sistema.
   ```

2. **Listar herramientas disponibles para el rol activo:**
   ```
   💡 Herramientas disponibles para '[nombre_rol]':
   
   • herramienta_1
   • herramienta_2
   • herramienta_3
   ```

**Ejemplo:**
```
Usuario: > compilar_proyecto
(Rol activo: ArchDev Pro)

Sistema: ❌ La herramienta 'compilar_proyecto' no existe en el sistema.

         💡 Herramientas disponibles para 'ArchDev Pro':
         
         • refactorizar
         • analizar_code_smells
         • solucionar_smells
         • crear_pruebas
         • verifica_pruebas
         • generar_adr
         • tomar_contexto
```

---

## Notas Importantes

- **Herramientas Universales:** Algunas herramientas como `tomar_contexto` pueden ser usadas por múltiples roles
- **Herramientas Especializadas:** Otras como `diagnosticar_devops` son exclusivas de un rol específico
- **Herramienta del Orquestador:** `asignar_responsable` es una herramienta especial que solo el orquestador puede ejecutar mediante el comando `/cochas assign <tarea>`
