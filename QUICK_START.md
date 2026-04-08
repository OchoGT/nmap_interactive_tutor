# 🚀 GUÍA RÁPIDA DE INICIO

## ⚡ 5 MINUTOS PARA COMENZAR

---

## PASO 1: INSTALACIÓN (2 minutos)

### Opción A: Instalación Automática (RECOMENDADO)

```bash
# Dale permisos al script
chmod +x install.sh

# Ejecuta la instalación
./install.sh
```

Este script instalará automáticamente:
- ✓ Python 3
- ✓ Nmap
- ✓ Dependencias de Python

### Opción B: Instalación Manual

```bash
# 1. Instalar Python 3 y pip
sudo apt update
sudo apt install python3 python3-pip

# 2. Instalar Nmap
sudo apt install nmap

# 3. Instalar dependencias
pip3 install -r requirements.txt
```

---

## PASO 2: PRIMER LANZAMIENTO (1 minuto)

```bash
python3 nmap_interactive_tutor.py
```

O si le diste permisos:

```bash
./nmap_interactive_tutor.py
```

---

## PASO 3: PRIMERA SESIÓN (2 minutos)

### Pantalla de Bienvenida
- Lee la explicación sobre Nmap
- Revisa las advertencias legales
- Escribe **"s"** para aceptar

### Menú Principal
Selecciona **opción [1]**: "Modo Aprendizaje Guiado"

### Seleccionar Nivel
Elige **Nivel 1: Básico** (para principiantes)

### Aprender y Practicar
1. Ingresa una IP objetivo (tu máquina local: 127.0.0.1)
2. Para cada opción:
   - Lee la explicación
   - Escribe "s" para usarla
   - Responde preguntas
3. El programa costruye el comando
4. Elige "Ejecutar ahora"

---

## 📚 NIVELES DE APRENDIZAJE

Después de Nivel 1, continúa con:

| Nivel | Nombre | Tiempo | Para Quién |
|-------|--------|--------|-----------|
| 1 | 🔰 Básico | 20 min | Principiantes totales |
| 2 | ⚙️ Intermedio | 30 min | Usuarios con experiencia |
| 3 | 🔥 Avanzado | 40 min | Pentesters y auditors |
| 4 | 💾 Salida | 15 min | Todos (reportes) |

---

## 🎯 CASOS DE USO COMUNES

### Caso 1: Descobrir Máquinas en la Red
```
1. Menú → [3] Ejemplos
2. Selecciona "Escaneo rápido de red"
3. Modifica el rango IP
4. Ejecuta
```

### Caso 2: Auditar tu Propio Servidor
```
1. Menú → [1] Aprendizaje Guiado
2. Nivel 2
3. Agrega -sV para versiones
4. Agrega --open para ver solo abiertos
5. Ejecuta
```

### Caso 3: Practicar Técnicas Avanzadas
```
1. Menú → [1] Aprendizaje Guiado
2. Nivel 3
3. Experimenta con scripts (--script)
4. Practica con fragmentación (-f)
5. Observa y aprende
```

---

## ⌨️ CONTROLES Y COMANDOS

### En cualquier momento:
- **"info"** - Ver más detalles
- **"ejemplo"** - Ver comando de ejemplo
- **"saltar"** - Omitir esta opción
- **CTRL+C** - Salir del programa

### En el menú:
- Escritura números (0-5) para navegar
- ENTER para confirmar

---

## 🔧 TROUBLESHOOTING

### "Nmap no encontrado"
```bash
# Instálalo
sudo apt install nmap
# O verifica dónde está
which nmap
```

### "Permiso denegado al ejecutar script"
```bash
# Dale permisos
chmod +x nmap_interactive_tutor.py
chmod +x install.sh
```

### Colores extraños en consola
```bash
# Instala colorama
pip3 install colorama
```

### No puedo escanear ciertos puertos
```bash
# Algunos escaneos necesitan root
sudo python3 nmap_interactive_tutor.py
```

---

## 💡 CONSEJOS PARA APRENDER

✅ **HAZ ESTO:**
- [ ] Comienza por Nivel 1, aunque pienses que es fácil
- [ ] Lee TODAS las explicaciones, no saltes
- [ ] Practica en tu propia máquina primero
- [ ] Experimenta con ejemplos
- [ ] Toma notas mientras aprendes
- [ ] Repite los comandos varias veces

❌ **NO HAGAS ESTO:**
- ❌ Escanear sistemas ajenos sin permiso
- ❌ Saltar niveles
- ❌ Arrastrar cambios sin entender
- ❌ Ignorar las advertencias legales

---

## 📖 PRÓXIMOS PASOS

### Después de completar Nivel 1:

1. **Nivel 2** - Descubre detección de servicios
   - Detecta versiones de software
   - Identifica sistemas operativos
   - Aprende filtros útiles

2. **Nivel 3** - Técnicas avanzadas
   - Scripts NSE para vulnerabilidades
   - Técnicas de evasión
   - Reconocimiento sofisticado

3. **Nivel 4** - Generación de reportes
   - Exporta resultados
   - Integra con herramientas
   - Documentación profesional

### Además del programa:

- Practica pentesting en **VulnHub** o **TryHackMe**
- Lee el manual oficial: `man nmap`
- Únete a comunidades de ciberseguridad
- Participa en CTF (Capture The Flag)

---

## ⚠️ ADVERTENCIA IMPORTANTE

```
⚖️ RESPONSABILIDAD LEGAL

✓ LEGAL: Escanear tu propio hardware
✗ ILEGAL: Escanear sistemas sin autorización

Este programa es EDUCATIVO.
TÚ eres responsable de cómo lo uses.
```

**Si tienes duda, NO escanees.**

---

## 🆘 NECESITAS AYUDA?

### Dentro del programa:
- Opción [5] - Ayuda General
- "info" / "ejemplo" en cualquier opción
- Explicaciones completas para cada banderapieds

### Recursos externos:
- 📖 README.md - Documentación completa
- 🌐 nmap.org - Sitio oficial
- 🔍 Google - Busca "[tu error] nmap"
- 💬 Reddit - r/netsec, r/learnprogramming

---

## 🎓 EJERCICIOS PRÁCTICOS

### Ejercicio 1: Conoce tu red (Nivel 1)
```
Objetivo: Descubrir cuántas máquinas están activas en tu red local
Comando: nmap -sn 192.168.1.0/24
Tiempo: 5 min
```

### Ejercicio 2: Escanea tu propia máquina (Nivel 1-2)
```
Objetivo: Identificar todos los puertos abiertos
Comandos:
  - nmap localhost
  - nmap -sV localhost
  - nmap -p- localhost
Tiempo: 15 min
```

### Ejercicio 3: Trabaja con guiones (Nivel 3)
```
Objetivo: Ejecutar análisis automático con scripts
Comando: nmap --script default localhost
Tiempo: 20 min
```

---

## 📊 PROGRESO

Marca tus logros:

- [ ] Instalé el programa correctamente
- [ ] Ejecuté la primera lanzamiento
- [ ] Completé Nivel 1
- [ ] Entiendo -sS vs -sT
- [ ] Completé Nivel 2
- [ ] Sé cómo detectar versiones
- [ ] Completé Nivel 3
- [ ] Probé scripts NSE
- [ ] Completé Nivel 4
- [ ] He generado reportes
- [ ] Estoy listo para pentesting real

---

## 🎉 ¡FELICIDADES!

¡Has completado la guía rápida!

### Ahora:
1. Ejecuta el programa: `python3 nmap_interactive_tutor.py`
2. Sigue las instrucciones
3. ¡Aprende y practica!

**Recuerda:** La mejor forma de aprender es haciendo. 

No tengas miedo de experimentar (en tu propia máquina).

---

## 📞 RETROALIMENTACIÓN

Si tienes sugerencias o encuentras errores:
- Documenta el error
- Describe qué hiciste
- Reporta dónde sucedió
- ¡Las mejoras ayudan a todos!

---

**¡Bienvenido al mundo del reconocimiento de redes! 🚀**

*- El Tutor de Nmap*
