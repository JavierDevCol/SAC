# Herramienta: verifica-pruebas-unitarias

## Objetivo
(Ver descripción en Contenido Original.)

## Entradas Requeridas (Contexto)
(No especificadas en el original.)

## Parámetros del Usuario
(No especificados en el original.)

## Roles Autorizados
(No definidos en el original.)

## Proceso Paso a Paso
(Descrito en Contenido Original.)

## Manejo de Errores y Casos Borde
(Parcialmente descrito en reglas del modo autónomo.)

## Formato de Salida Esperado
(No definido en el original.)

---

## Contenido Original

### Herramienta: Verificación y Corrección de Pruebas (Comando: `verifica-pruebas-unitarias`)

*Al recibir este comando, iniciarás el siguiente proceso:*

#### **Paso 0: Configuración Inicial**
1.  **Solicitar Repositorio:** Preguntarás: **"Iniciando la verificación de pruebas. Por favor, proporciona el nombre del repositorio para construir la ruta de trabajo:"** y esperarás mi respuesta.
2.  **Solicitar Tipo de Prueba:** Luego, preguntarás por "Todas las pruebas" o "Pruebas de un paquete específico".

#### **Flujo de Trabajo**
1.  **Ejecución y Análisis:** Ejecuta `cd` y el comando `gradlew test` correspondiente.
2.  **Selección de Modo:**
    * **Pocos fallos (<=3):** Modo de Confirmación Individual.
    * **Muchos fallos (>3):** Modo de Corrección Autónoma.

#### **Modo de Corrección Autónoma**
-   **Reglas:** No asumir supuestos (consultar en caso de duda) y no tocar el código de producción sin permiso explícito.
-   **Proceso:** Itera sobre los fallos, aplica las correcciones a los tests y al final presenta un resumen de los cambios aplicados.