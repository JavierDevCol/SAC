# 🛠️ Plantilla de Herramienta

> El propósito de un archivo de "Herramienta" es definir un proceso algorítmico y secuencial. Es un plan de acción claro y paso a paso. Es el "qué hacer".

---

## 📋 Identificación

**Herramienta:** `[nombre_slug]`

---

## 🎯 Objetivo

[Descripción clara y concisa del propósito de la herramienta en 1-2 líneas. Qué problema resuelve o qué capacidad otorga.]

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- [Ej: El contenido del archivo activo o el código seleccionado en el editor (#selection o #file).]

**Secundario (Opcional):**
- [Ej: Dependencias externas, requisitos de cobertura, contexto arquitectónico.]
- [Ej: Metadatos del proyecto, convenciones internas.]

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `param_ejemplo` | string | valor1\|valor2 | valor1 | [Ej: El nombre de un método específico a probar, si se proporciona.] |
| `nivel_detalle` | string | basico\|completo | completo | Nivel de detalle de la salida |

---

## 👥 Roles Autorizados

- ✅ [Rol/Persona 1]
- ✅ [Rol/Persona 2]
- ✅ [Rol/Persona 3] *(modo específico si aplica)*

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Análisis Inicial

- Identifica la clase principal y sus dependencias (anotaciones @Autowired, @Service, etc.) en el contexto de entrada.
- Lista todos los métodos públicos de la clase que deben ser probados.

### 2️⃣ Preparación del Entorno de Prueba

- Determina la ruta correcta para el archivo de prueba (ej. src/test/java/...).
- Prepara la estructura base de la clase de prueba usando JUnit 5 y Mockito.
- Genera los campos para los mocks (@Mock) y la instancia bajo prueba (@InjectMocks).

### 3️⃣ Generación de Casos de Prueba (Iterativo)

- Para cada método público identificado en el paso 1:
  - a. Genera un método de prueba para el "camino feliz" (happy path).
  - b. Genera al menos un método de prueba para un caso de error o borde (ej. entrada nula, excepción esperada).
  - c. Estructura cada prueba claramente usando el patrón Arrange-Act-Assert (AAA) con comentarios.

### 4️⃣ Finalización y Entrega

- Ensambla todo el código generado en un único archivo.
- Utiliza la herramienta #createFile para crear el archivo de prueba en la ruta determinada en el paso 2.
- Informa al usuario de la acción completada y la ubicación del nuevo archivo.

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| El contexto de entrada no contiene una clase de Java válida | Informa al usuario y detén la ejecución |
| Una dependencia no puede ser mockeada | Informa al usuario y sugiere una solución manual |
| [Otro caso borde específico] | [Estrategia de manejo] |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Un único archivo Java (.java) creado directamente en el sistema de archivos del proyecto.

**Notificación:**
- Un mensaje de confirmación en el chat.

**Estructura del output:**
```
[Ejemplo de estructura o plantilla de salida si aplica]
```

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/[nombre-herramienta]_ejemplo.md`

---

## 📚 Referencias y Notas

- [Links a documentación relevante si aplica]
- [Consideraciones adicionales o limitaciones conocidas]

