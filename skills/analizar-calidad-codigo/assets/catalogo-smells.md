# Catálogo de Code Smells

> Referencia para el sub-agente de análisis de code smells.

## Bloaters (Encrespadores)

### Long Method
- **Indicador:** Método con más de 20 líneas
- **Solución:** Extract Method
- **Ejemplo:**
  ```java
  // ANTES (45 líneas)
  void procesarPedido() { ... }
  
  // DESPUÉS
  void procesarPedido() {
      validarDatos();
      calcularTotal();
      aplicarDescuentos();
      guardarEnBD();
  }
  ```

### Large Class / God Object
- **Indicador:** Clase con más de 300 líneas o más de 10 métodos
- **Solución:** Extract Class
- **Categoría:** SRP violado

### Long Parameter List
- **Indicador:** Método con más de 3 parámetros
- **Solución:** Parameter Object
- **Ejemplo:**
  ```java
  // ANTES
  void crear(String nombre, String email, String telefono, String direccion, String ciudad)
  
  // DESPUÉS
  void crear(DatosContacto datos)
  ```

### Data Clumps
- **Indicador:** Mismos 3+ campos aparecen juntos en múltiples clases
- **Solución:** Extract Class

## OO Abusers (Abusadores de POO)

### Feature Envy
- **Indicador:** Método usa más datos de otra clase que de la suya
- **Solución:** Move Method

### Inappropriate Intimacy
- **Indicador:** Clase accede a internals de otra clase
- **Solución:** Move Method/Field

### Refused Bequest
- **Indicador:** Subclase no usa herencia recibida
- **Solución:** Replace Inheritance with Delegation

## Change Preventers (Impedimentos de Cambio)

### Divergent Change
- **Indicador:** Clase cambia por múltiples razones distintas
- **Solución:** Extract Class (SRP)

### Shotgun Surgery
- **Indicador:** Un cambio requiere modificar múltiples clases
- **Solución:** Move Method/Field

### Parallel Inheritance
- **Indicador:** Crear subclase requiere crear otra subclase
- **Solución:** Move Method/Field

## Dispensables (Prescindibles)

### Dead Code
- **Indicador:** Código que nunca se ejecuta
- **Solución:** Remove Dead Code

### Speculative Generality
- **Indicador:** Abstracciones que nunca se usan
- **Solución:** Collapse Hierarchy

### Duplicate Code
- **Indicador:** Mismo código repetido en 2+ lugares
- **Solución:** Extract Method + Pull Up

## Couplers (Acopladores)

### Message Chains
- **Indicador:** a.getB().getC().getD()
- **Solución:** Hide Delegate

### Middle Man
- **Indicador:** Clase que solo delega a otra
- **Solución:** Remove Middle Man

## Severidad

| Nivel | Criterio |
|-------|----------|
| **Crítica** | Afecta múltiples clases, bloquea testing |
| **Alta** | Viola SOLID críticos, afecta mantenibilidad |
| **Media** | Dificulta comprensión del código |
| **Baja** | Mejora cosmética, convenciones de estilo |
