# Guia de modulos del menu principal

Este documento explica las opciones principales del programa `Nmap Interactive Tutor` para que cualquier usuario entienda que hace cada modulo antes de usarlo.

Archivo principal del proyecto:

- `nmap_interactive_tutor.py`

## Menu principal

Cuando ejecutas el programa, el menu principal muestra estos modulos:

1. `Modo Aprendizaje Guiado (RECOMENDADO)`
2. `Construccion Libre de Comando`
3. `Ver Ejemplos Practicos`
4. `Ver Historial de Comandos`
5. `Ayuda General`
6. `Retos de Nmap`
0. `Salir`

---

## 1. Modo Aprendizaje Guiado

Este es el modulo principal del sistema y el mas importante para principiantes.

### Para que sirve

Sirve para aprender Nmap paso a paso, como si el programa fuera un tutor. No solo construye comandos: tambien explica que hace cada opcion antes de agregarla.

### Como funciona

1. El usuario elige un nivel.
2. Ingresa un objetivo, por ejemplo una IP o dominio.
3. El programa va mostrando cada opcion del nivel.
4. Explica:
   - que hace la bandera
   - cuando se usa
   - ejemplo real
   - nivel de ruido o riesgo en varios casos
5. Pregunta si deseas usarla.
6. Si la agregas, la incorpora al comando final.
7. Al terminar, deja ejecutar, guardar o editar.

### Niveles que contiene

- `Nivel 1: Basico`
- `Nivel 2: Intermedio`
- `Nivel 3: Avanzado`
- `Nivel 4: Salida y reportes`

### Cuando usarlo

- Cuando nunca has usado Nmap
- Cuando quieres aprender mientras construyes comandos reales
- Cuando quieres evitar errores por banderas incompatibles

### Ventaja principal

Convierte el aprendizaje en una experiencia guiada y no en una simple lista de comandos.

---

## 2. Construccion Libre de Comando

Este modulo esta pensado para usuarios que ya tienen una idea de lo que quieren hacer.

### Para que sirve

Permite escribir opciones de Nmap manualmente y ver el comando final sin pasar por toda la explicacion pedagógica del modo guiado.

### Como funciona

1. El usuario ingresa el objetivo.
2. Va escribiendo banderas y opciones de forma libre.
3. El programa va actualizando el comando actual.
4. Luego permite:
   - ejecutar
   - guardar
   - editar
   - cancelar

### Cuando usarlo

- Cuando ya conoces Nmap
- Cuando quieres probar una combinacion especifica
- Cuando deseas construir un comando rapido

### Ventaja principal

Da mas velocidad y libertad sin perder la ayuda basica del programa.

---

## 3. Ver Ejemplos Practicos

Este modulo funciona como biblioteca de ejemplos reales.

### Para que sirve

Muestra comandos ya preparados para situaciones comunes, junto con una explicacion de su uso.

### Que tipo de ejemplos incluye

- escaneo rapido
- auditoria basica
- deteccion de servicios
- descubrimiento de hosts
- otros escenarios comunes de Nmap

### Como funciona

1. El programa lista varios ejemplos.
2. El usuario elige uno.
3. El sistema muestra:
   - titulo
   - comando
   - explicacion detallada

### Cuando usarlo

- Cuando quieres aprender viendo casos reales
- Cuando necesitas una referencia rapida
- Cuando quieres copiar ideas para tus propios comandos

### Ventaja principal

Ayuda a relacionar teoria con casos practicos.

---

## 4. Ver Historial de Comandos

Este modulo muestra los comandos que ya se usaron antes en el programa.

### Para que sirve

Permite revisar comandos anteriores sin tener que reconstruirlos desde cero.

### Como funciona

- El programa lee el historial guardado.
- Muestra los ultimos comandos usados.
- Sirve como referencia o recordatorio.

### Cuando usarlo

- Cuando quieres repetir un escaneo anterior
- Cuando deseas revisar que comandos has practicado
- Cuando quieres documentar tu progreso

### Ventaja principal

Te ayuda a no perder trabajo previo.

---

## 5. Ayuda General

Este modulo es la seccion de soporte interna del programa.

### Para que sirve

Resume como usar el sistema, que requisitos tiene y que recomendaciones seguir.

### Que explica

- como usar el modo guiado
- como usar la construccion libre
- recomendaciones para principiantes
- instalacion de Nmap
- advertencias legales
- recursos adicionales

### Cuando usarlo

- Si es tu primera vez en el programa
- Si olvidaste como se usa una parte del sistema
- Si necesitas orientacion general

### Ventaja principal

Concentra la ayuda esencial dentro de la misma aplicacion.

---

## 6. Retos de Nmap

Este modulo agrega una parte practica estilo ejercicio o evaluacion.

### Para que sirve

Permite comprobar si el usuario entendio como construir comandos de Nmap, planteando retos por dificultad.

### Como funciona

1. El usuario elige dificultad:
   - facil
   - medio
   - dificil
2. El sistema muestra un reto.
3. El usuario escribe un comando Nmap.
4. El programa verifica si el comando contiene las opciones esperadas.
5. Al final muestra puntaje y calificacion.

### Cuando usarlo

- Cuando ya estudiaste con el modo guiado
- Cuando quieres practicar sin ejecutar necesariamente un escaneo real
- Cuando quieres medir tu avance

### Ventaja principal

Transforma el aprendizaje en practica activa.

---

## 7. Salir

Es la opcion para cerrar el programa de forma normal.

### Para que sirve

- terminar la sesion
- salir de la aplicacion de forma segura

### Que hace

- muestra mensaje final
- recuerda el uso autorizado y etico de Nmap

---

## Recomendacion de uso

Para un usuario nuevo, el orden recomendado es este:

1. `Ayuda General`
2. `Modo Aprendizaje Guiado`
3. `Ver Ejemplos Practicos`
4. `Retos de Nmap`
5. `Construccion Libre de Comando`
6. `Historial de Comandos`

---

## Resumen corto de cada modulo

- `Modo Aprendizaje Guiado`: enseña paso a paso y construye comandos contigo.
- `Construccion Libre de Comando`: deja escribir comandos manualmente.
- `Ver Ejemplos Practicos`: muestra casos reales listos para estudiar.
- `Ver Historial de Comandos`: enseña lo que ya ejecutaste o guardaste.
- `Ayuda General`: explica el uso general del sistema.
- `Retos de Nmap`: evalua si ya aprendiste.
- `Salir`: cierra el programa.

---

## Conclusion

El menu principal esta diseñado para cubrir todo el ciclo de aprendizaje:

- primero entender
- luego practicar
- despues probar
- finalmente recordar y repetir

Por eso el programa no es solo un ejecutor de comandos, sino un asistente educativo completo para aprender Nmap en consola.


