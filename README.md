# 🎯 NMAP INTERACTIVE TUTOR 🎯

## Un asistente educativo completo para dominar Nmap desde cero

---

## 📋 Contenido

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Programa](#estructura-del-programa)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Advertencia Legal](#advertencia-legal)

---

## 📖 Descripción

**NMAP Interactive Tutor** es un programa educativo interactivo en consola (CLI) para Linux que enseña a usar Nmap de forma progresiva y didáctica.

### ¿Qué es Nmap?

Nmap (Network Mapper) es una herramienta de reconocimiento de redes que permite:
- Descubrir hosts activos en una red
- Escanear puertos
- Identificar servicios y versiones
- Detectar sistemas operativos
- Analizar vulnerabilidades
- Mapear redes complejas

### ¿Para qué sirve este programa?

Este tutor enseña a una persona sin experiencia a:
- Comprender qué es Nmap y cómo funciona
- Entender cada opción y bandera importante
- Construir comandos de forma interactiva
- Practicar de manera guiada
- Avanzar desde lo básico hasta técnicas avanzadas

---

## ✨ Características

### ✅ Características Principales

1. **4 Niveles Educativos Progresivos**
   - 🔰 Nivel 1: Básico (escaneos simples)
   - ⚙️ Nivel 2: Intermedio (detección de servicios)
   - 🔥 Nivel 3: Avanzado (scripts y evasión)
   - 💾 Nivel 4: Salida y reportes

2. **Interfaz Interactiva**
   - Menú navegable
   - Explicaciones detalladas para cada opción
   - Sistema de ayuda integrado
   - Validación de entradas

3. **Construcción Dinámica de Comandos**
   - Visualización en tiempo real del comando
   - Permite modificar antes de ejecutar
   - Constructor modular y flexible

4. **Sistema de Ejemplos**
   - 5+ ejemplos prácticos listos para usar
   - Escaneo rápido de red
   - Auditoría completa
   - Reconocimiento sigiloso
   - Y más...

5. **Gestión de Historial**
   - Guarda últimos 100 comandos ejecutados
   - Visualización del historial
   - Archivos guardados organizados

6. **Ejecución Integrada**
   - Ejecuta comandos de Nmap directamente
   - Muestra salida en tiempo real
   - Manejo de errores

7. **Presentación Visual**
   - Colores en consola (mejor legibilidad)
   - Barras de progreso
   - Formateo profesional

---

## 📦 Requisitos

### Sistema Operativo
- **Linux** (Ubuntu, Debian, Fedora, Arch, etc.)
  
> El programa está diseñado específicamente para Linux. Para Windows, considera usar WSL (Windows Subsystem for Linux).

### Software Requerido

1. **Python 3.7 o superior**
   ```bash
   python3 --version
   ```

2. **Nmap** (instalado en el sistema)
   ```bash
   nmap --version
   ```

3. **Módulos de Python** (opcional pero recomendado)
   - `colorama` (para colores en consola)

### Permisos Necesarios

- Para algunos escaneos necesitarás **permisos de root** (sudo)
- El escaneo de SYN (-sS) requiere permisos elevados
- TCP Connect (-sT) funciona sin root

---

## 💾 Instalación

### Paso 1: Instalar Python 3

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip

# Fedora/CentOS/RHEL
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python
```

### Paso 2: Instalar Nmap

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install nmap

# Fedora/CentOS/RHEL
sudo dnf install nmap

# Arch Linux
sudo pacman -S nmap
```

### Paso 3: Instalar dependencias de Python

```bash
# Instalar colorama para colores (recomendado)
pip3 install colorama

# O instalar con sudo si es necesario
sudo pip3 install colorama
```

### Paso 4: Descargar el programa

```bash
# Si aún no tienes el archivo, cópialo a tu sistema
# Por defecto debería estar en: 
# /ruta/al/proyecto/nmap scanner/nmap_interactive_tutor.py
```

### Paso 5: Dar permisos de ejecución

```bash
chmod +x /path/to/nmap_interactive_tutor.py
```

---

## 🚀 Uso

### Ejecutar el programa

```bash
# Desde el directorio del archivo
python3 nmap_interactive_tutor.py

# O si tiene permisos de ejecución
./nmap_interactive_tutor.py

# O desde cualquier lugar
python3 /ruta/completa/nmap_interactive_tutor.py
```

### Primer lanzamiento

1. Verás la **pantalla de bienvenida**
2. Se te presentarán las **advertencias legales**
3. Debes **aceptar** para continuar
4. Accederás al **menú principal**

### Opciones del Menú Principal

```
[1] Modo Aprendizaje Guiado (RECOMENDADO) ⭐
[2] Construcción Libre de Comando
[3] Ver Ejemplos Prácticos
[4] Ver Historial de Comandos
[5] Ayuda General
[0] Salir
```

### Opción 1: Modo Aprendizaje Guiado ⭐ RECOMENDADO

**Flujo:**
1. Selecciona nivel (1-4)
2. Ingresa objetivo (IP o dominio)
3. Para cada opción del nivel:
   - Lee la explicación completa
   - Practica escribiendo "info" o "ejemplo"
   - Responde sí/no para agregar la opción
   - Ingresa parámetros si es necesario
4. Ver comando final construido
5. Ejecutar, guardar o editar

### Opción 2: Construcción Libre

**Flujo:**
1. Ingresa IP objetivo
2. Agrega opciones manualmente (ej: -sS -p 80,443)
3. Ejecuta, guarda o edita el comando

### Opción 3: Ejemplos Prácticos

- Ver 5 ejemplos pre-configurados
- Entender casos de uso reales
- Copiar comandos para ejecutar

---

## 🏗️ Estructura del Programa

```
nmap_interactive_tutor.py
│
├─ CONFIGURACIÓN
│  ├─ Rutas de historial
│  ├─ Rutas de comandos guardados
│  └─ Constantes
│
├─ BASE DE CONOCIMIENTO
│  ├─ Nivel 1: Básico
│  ├─ Nivel 2: Intermedio
│  ├─ Nivel 3: Avanzado
│  └─ Nivel 4: Salida y reportes
│
├─ FUNCIONES AUXILIARES
│  ├─ Limpiar pantalla
│  ├─ Validar entradas
│  ├─ Manejo de colores
│  ├─ Ejecución de Nmap
│  └─ Gestión de historial
│
├─ CLASE ConstructorNmap
│  ├─ Construir comandos dinámicamente
│  ├─ Agregar opciones
│  ├─ Usar validación
│  └─ Mostrar comando actual
│
├─ INTERFAZ PRINCIPAL
│  ├─ Menú principal
│  ├─ Modo aprendizaje guiado
│  ├─ Construcción libre
│  ├─ Ejemplos
│  ├─ Historial
│  └─ Ayuda
│
└─ PUNTO DE ENTRADA (main)
```

---

## 📚 Contenido Educativo

### Nivel 1: Básico

**Aprenderás:**
- Qué es un escaneo
- Tipos de objetivos (IP, dominio, rango)
- Escaneo TCP SYN (-sS) - recomendado
- Escaneo TCP Connect (-sT) - sin root
- Ping Scan (-sn) - descubrimiento
- Especificar puertos (-p)
- Control de timing (-T)

**Tiempo estimado:** 20-30 minutos

### Nivel 2: Intermedio

**Aprenderás:**
- UDP Scan (-sU) - descubrimiento UDP
- Detección de versiones (-sV)
- Detección de SO (-O)
- Escaneo agresivo (-A)
- Filtros de salida (--open)
- Saltar ping (-Pn)
- Escaneo rápido (-F)
- Modo verbose (-v, -vv)

**Tiempo estimado:** 30-40 minutos

### Nivel 3: Avanzado

**Aprenderás:**
- Scripts NSE (--script)
- Argumentos de scripts (--script-args)
- Fragmentación de paquetes (-f)
- MTU customizado (--mtu)
- Spoofing de MAC (--spoof-mac)
- Decoys/señuelos (-D)
- Especificar interfaz (-e)
- Agregar datos aleatorios (--data-length)

**Tiempo estimado:** 40-60 minutos

### Nivel 4: Salida y Reportes

**Aprenderás:**
- Formato normal (-oN) - texto plano
- Formato XML (-oX) - para herramientas
- Formato grepable (-oG) - para shell
- Todos los formatos (-oA)

**Tiempo estimado:** 15-20 minutos

---

## 🎓 Ejemplos de Uso

### Ejemplo 1: Escaneo Rápido de Red

```bash
nmap -sn -T4 192.168.1.0/24
```

**¿Qué hace?**
- Descubre qué hosts están activos
- Rápido y sin intrusión
- Ideal para mapeo inicial

### Ejemplo 2: Auditoría Completa

```bash
nmap -A -sV -sC -oA reporte 192.168.1.100
```

**¿Qué hace?**
- Análisis profundo del servidor
- Identifica servicios, versiones, OS
- Ejecuta scripts de análisis
- Guarda en 3 formatos

### Ejemplo 3: Escaneo Sigiloso

```bash
nmap -sS -T2 -p- 192.168.1.100
```

**¿Qué hace?**
- Escaneo discreto de TODOS los puertos
- Timing lento (menos detectable)
- Muy sigiloso

### Ejemplo 4: Detección de Vulnerabilidades

```bash
nmap --script vuln -sV 192.168.1.100
```

**¿Qué hace?**
- Busca vulnerabilidades conocidas
- Tiempo: 1-2 minutos
- Muy evidente en logs

---

## 📁 Archivos Generados

El programa crea/usa los siguientes archivos:

### Historial
```
~/.nmap_tutor_historial.json
```
- Guarda últimos 100 comandos
- JSON estructurado
- Automático

### Comandos Guardados
```
~/.nmap_tutor_comandos/
├─ comando1.txt
├─ comando2.txt
└─ comando3.txt
```
- Directorio de comandos personalizados
- Creado automáticamente
- Para referencia futura

---

## ⚙️ Consejos Prácticos

### Para Principiantes

1. ✅ **Inicia con Nivel 1** - Entiende lo básico
2. ✅ **Practica en tu propia máquina** - Usa VM virtuales
3. ✅ **Lee todas las explicaciones** - Son muy detalladas
4. ✅ **Ejecuta los ejemplos** - Observa los resultados
5. ✅ **Haz mis comandos gradualmente** - No todo a la vez

### Máquinas Virtuales para Practicar

- **Vulnhub.com** - CTFs y máquinas virtuales vulnerables
- **DVWA** - Aplicación web deliberadamente insegura
- **VulnerableApp** - Máquinas diseñadas para aprender
- **Local Lab** - Tu propia VM de Ubuntu en VirtualBox

### Seguridad

⚠️ **IMPORTANTE:**
- NUNCA escanees sistemas que no poseas
- Obtén **autorización escrita** antes de escanear
- Los alumnos necesitan **consentimiento explícito**
- Documentar todo para defensa legal

---

## 🔧 Troubleshooting

### "Nmap no encontrado"

```bash
# Verifica si está instalado
which nmap

# Si no aparece, instálalo
sudo apt install nmap

# O verifica la versión
nmap -V
```

### "colorama no está instalado"

El programa funciona sin colorama, pero se ve mejor con él:

```bash
pip3 install colorama
# O con sudo
sudo pip3 install colorama
```

### "Permiso denegado"

Algunos escaneos necesitan root:

```bash
# Ejecuta con sudo
sudo python3 nmap_interactive_tutor.py
```

### "Comando no inicia"

```bash
# Verifica que Python 3 esté instalado
python3 --version

# Verifica que el archivo sea ejecutable
chmod +x nmap_interactive_tutor.py

# Ejecuta con python3 explícitamente
python3 /ruta/nmap_interactive_tutor.py
```

---

## 📖 Recursos Adicionales

### Documentación Oficial
- **Sitio de Nmap**: https://nmap.org
- **Manual de Nmap**: https://nmap.org/book/
- **Referencia de NSE**: https://nmap.org/nsedoc/

### Tutoriales en Línea
- **HackerOne**: Guías de bugging
- **TryHackMe**: Cursos interactivos
- **Udemy**: Cursos de Nmap

### Comunidades
- **Foros de Nmap**: https://nmap.org/community
- **Reddit r/netsec**: Red de seguridad
- **StackOverflow**: Preguntas técnicas

---

## 📝 Versión

- **Versión**: 1.0.0
- **Fecha**: 2026
- **Python mínimo**: 3.7
- **SO**: Linux

---

## 📄 Licencia

Este programa es educativo y de uso libre para propósitos de aprendizaje.

---

## ⚠️ ADVERTENCIA LEGAL IMPORTANTE

### AVISO LEGAL

Este programa es **SOLO educativo**. Eres responsable de tus acciones.

### Legalidad

El escaneo de puertos **NO AUTORIZADO** es **ILEGAL** en muchas jurisdicciones:

- **USA**: Violación del "Computer Fraud and Abuse Act (CFAA)"
- **UE**: Violación del GDPR y leyes nacionales de ciberdelito
- **LATAM**: Leyes nacionales sobre acceso no autorizado
- **CONSECUENCIAS**: Multas y/o cárcel

### Normas de Uso

✅ **PERMITIDO:**
- Escanear tu propio hardware
- Escanear máquinas virtuales propias
- Escanear laboratorios autorizados
- Penetration Testing CON PERMISO ESCRITO
- Auditorías de seguridad contratadas

❌ **PROHIBIDO:**
- Escanear sistemas sin autorización
- Escanear redes ajenas
- Buscar vulnerabilidades no autorizadas
- Hacer daño o acceso no autorizado
- Acuso públicamente de vulnerabilidades sin aviso privado

### Responsabilidad

```
AL USAR ESTE PROGRAMA ACEPTAS QUE:

- Entiendes que es solo para educación
- Usarás Nmap responsablemente
- Solo escanearás sistemas autorizados
- Eres responsable de tus acciones
- El autor NO es responsable del mal uso
- Respetarás las leyes de tu país
```

---

## 👨‍🏫 Autor

Creado como herramienta educativa para la comunidad de ciberseguridad.

---

## 🙏 Agradecimientos

- **Nmap.org**: Por la excelente herramienta
- **Comunidad Open Source**: Por el software libre
- **Educadores**: Por inspirar este proyecto

---

**¡Que disfrutes aprendiendo Nmap! 🚀**

*Recuerda: Solo eres "ético" si actúas con ética.*

"# nmap_interactive_tutor" 
