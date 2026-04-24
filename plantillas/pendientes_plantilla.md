# 📋 Registro de Pendientes y Hallazgos

> Registro de tareas pendientes: hallazgos de pruebas, verificaciones futuras, investigaciones y mejoras.  
> **Ownership:** Solo el Arquitecto registra y gestiona entradas.  
> Un pendiente puede evolucionar a HU funcional, reclasificarse como bug, o descartarse.

---

## Registro

| ID | Categoría | Descripción | Prioridad | HU Relacionada | Detectado en | Fecha | Estado |
|----|-----------|-------------|-----------|----------------|--------------|-------|--------|
| PND-001 | [🔧 Deuda Técnica / 🎨 Mejora UX / ⚡ Optimización / 🔍 Verificación / 🧪 Investigación / 📎 Con Evidencia] | [Descripción breve] | [🟡 Baja / 🟠 Media] | [HU-XXX / —] | [Contexto] | [YYYY-MM-DD] | [📝 Registrado / 🚀 Promovido a HU-XXX / 🐛 Reclasificado a BUG-XXX / ❌ Descartado] |

> **Detalle:** Pendientes con categoría 📎 **Con Evidencia** o que requieran contexto extenso tienen archivo individual en `{{artifacts.pendientes_folder}}/PND-NNN_descripcion.md`

---

## Notas

- Las entradas con prioridad Alta deben reclasificarse como bug vía `>registrar_bug`
- Al promover un pendiente a HU, actualizar la columna **Estado** con el ID de la HU creada
- Al reclasificar como bug, actualizar Estado y ejecutar `>registrar_bug` con la referencia
