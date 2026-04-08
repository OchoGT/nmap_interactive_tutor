# ðŸŽ¯ NMAP INTERACTIVE TUTOR ðŸŽ¯

## Un asistente educativo completo para dominar Nmap desde cero

---

## ðŸ“‹ Contenido

- [DescripciÃ³n](#descripciÃ³n)
- [CaracterÃ­sticas](#caracterÃ­sticas)
- [Requisitos](#requisitos)
- [InstalaciÃ³n](#instalaciÃ³n)
- [Uso](#uso)
- [Estructura del Programa](#estructura-del-programa)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Advertencia Legal](#advertencia-legal)

---

## ðŸ“– DescripciÃ³n

**NMAP Interactive Tutor** es un programa educativo interactivo en consola (CLI) para Linux que enseÃ±a a usar Nmap de forma progresiva y didÃ¡ctica.

### Â¿QuÃ© es Nmap?

Nmap (Network Mapper) es una herramienta de reconocimiento de redes que permite:
- Descubrir hosts activos en una red
- Escanear puertos
- Identificar servicios y versiones
- Detectar sistemas operativos
- Analizar vulnerabilidades
- Mapear redes complejas

### Â¿Para quÃ© sirve este programa?

Este tutor enseÃ±a a una persona sin experiencia a:
- Comprender quÃ© es Nmap y cÃ³mo funciona
- Entender cada opciÃ³n y bandera importante
- Construir comandos de forma interactiva
- Practicar de manera guiada
- Avanzar desde lo bÃ¡sico hasta tÃ©cnicas avanzadas

---

## âœ¨ CaracterÃ­sticas

### âœ… CaracterÃ­sticas Principales

1. **4 Niveles Educativos Progresivos**
   - ðŸ”° Nivel 1: BÃ¡sico (escaneos simples)
   - âš™ï¸ Nivel 2: Intermedio (detecciÃ³n de servicios)
   - ðŸ”¥ Nivel 3: Avanzado (scripts y evasiÃ³n)
   - ðŸ’¾ Nivel 4: Salida y reportes

2. **Interfaz Interactiva**
   - MenÃº navegable
   - Explicaciones detalladas para cada opciÃ³n
   - Sistema de ayuda integrado
   - ValidaciÃ³n de entradas

3. **ConstrucciÃ³n DinÃ¡mica de Comandos**
   - VisualizaciÃ³n en tiempo real del comando
   - Permite modificar antes de ejecutar
   - Constructor modular y flexible

4. **Sistema de Ejemplos**
   - 5+ ejemplos prÃ¡cticos listos para usar
   - Escaneo rÃ¡pido de red
   - AuditorÃ­a completa
   - Reconocimiento sigiloso
   - Y mÃ¡s...

5. **GestiÃ³n de Historial**
   - Guarda Ãºltimos 100 comandos ejecutados
   - VisualizaciÃ³n del historial
   - Archivos guardados organizados

6. **EjecuciÃ³n Integrada**
   - Ejecuta comandos de Nmap directamente
   - Muestra salida en tiempo real
   - Manejo de errores

7. **PresentaciÃ³n Visual**
   - Colores en consola (mejor legibilidad)
   - Barras de progreso
   - Formateo profesional

---

## ðŸ“¦ Requisitos

### Sistema Operativo
- **Linux** (Ubuntu, Debian, Fedora, Arch, etc.)
  
> El programa estÃ¡ diseÃ±ado especÃ­ficamente para Linux. Para Windows, considera usar WSL (Windows Subsystem for Linux).

### Software Requerido

1. **Python 3.7 o superior**
   ```bash
   python3 --version
   ```

2. **Nmap** (instalado en el sistema)
   ```bash
   nmap --version
   ```

3. **MÃ³dulos de Python** (opcional pero recomendado)
   - `colorama` (para colores en consola)

### Permisos Necesarios

- Para algunos escaneos necesitarÃ¡s **permisos de root** (sudo)
- El escaneo de SYN (-sS) requiere permisos elevados
- TCP Connect (-sT) funciona sin root

---

## ðŸ’¾ InstalaciÃ³n

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
# Si aÃºn no tienes el archivo, cÃ³pialo a tu sistema
# Por defecto deberÃ­a estar en: 
# /ruta/al/proyecto/nmap scanner/nmap_interactive_tutor.py
```

### Paso 5: Dar permisos de ejecuciÃ³n

```bash
chmod +x /path/to/nmap_interactive_tutor.py
```

---

## ðŸš€ Uso

### Ejecutar el programa

```bash
# Desde el directorio del archivo
python3 nmap_interactive_tutor.py

# O si tiene permisos de ejecuciÃ³n
./nmap_interactive_tutor.py

# O desde cualquier lugar
python3 /ruta/completa/nmap_interactive_tutor.py
```

### Primer lanzamiento

1. VerÃ¡s la **pantalla de bienvenida**
2. Se te presentarÃ¡n las **advertencias legales**
3. Debes **aceptar** para continuar
4. AccederÃ¡s al **menÃº principal**

### Opciones del MenÃº Principal

```
[1] Modo Aprendizaje Guiado (RECOMENDADO) â­
[2] ConstrucciÃ³n Libre de Comando
[3] Ver Ejemplos PrÃ¡cticos
[4] Ver Historial de Comandos
[5] Ayuda General
[0] Salir
```

### OpciÃ³n 1: Modo Aprendizaje Guiado â­ RECOMENDADO

**Flujo:**
1. Selecciona nivel (1-4)
2. Ingresa objetivo (IP o dominio)
3. Para cada opciÃ³n del nivel:
   - Lee la explicaciÃ³n completa
   - Practica escribiendo "info" o "ejemplo"
   - Responde sÃ­/no para agregar la opciÃ³n
   - Ingresa parÃ¡metros si es necesario
4. Ver comando final construido
5. Ejecutar, guardar o editar

### OpciÃ³n 2: ConstrucciÃ³n Libre

**Flujo:**
1. Ingresa IP objetivo
2. Agrega opciones manualmente (ej: -sS -p 80,443)
3. Ejecuta, guarda o edita el comando

### OpciÃ³n 3: Ejemplos PrÃ¡cticos

- Ver 5 ejemplos pre-configurados
- Entender casos de uso reales
- Copiar comandos para ejecutar

---

## ðŸ—ï¸ Estructura del Programa

```
nmap_interactive_tutor.py
â”‚
â”œâ”€ CONFIGURACIÃ“N
â”‚  â”œâ”€ Rutas de historial
â”‚  â”œâ”€ Rutas de comandos guardados
â”‚  â””â”€ Constantes
â”‚
â”œâ”€ BASE DE CONOCIMIENTO
â”‚  â”œâ”€ Nivel 1: BÃ¡sico
â”‚  â”œâ”€ Nivel 2: Intermedio
â”‚  â”œâ”€ Nivel 3: Avanzado
â”‚  â””â”€ Nivel 4: Salida y reportes
â”‚
â”œâ”€ FUNCIONES AUXILIARES
â”‚  â”œâ”€ Limpiar pantalla
â”‚  â”œâ”€ Validar entradas
â”‚  â”œâ”€ Manejo de colores
â”‚  â”œâ”€ EjecuciÃ³n de Nmap
â”‚  â””â”€ GestiÃ³n de historial
â”‚
â”œâ”€ CLASE ConstructorNmap
â”‚  â”œâ”€ Construir comandos dinÃ¡micamente
â”‚  â”œâ”€ Agregar opciones
â”‚  â”œâ”€ Usar validaciÃ³n
â”‚  â””â”€ Mostrar comando actual
â”‚
â”œâ”€ INTERFAZ PRINCIPAL
â”‚  â”œâ”€ MenÃº principal
â”‚  â”œâ”€ Modo aprendizaje guiado
â”‚  â”œâ”€ ConstrucciÃ³n libre
â”‚  â”œâ”€ Ejemplos
â”‚  â”œâ”€ Historial
â”‚  â””â”€ Ayuda
â”‚
â””â”€ PUNTO DE ENTRADA (main)
```

---

## ðŸ“š Contenido Educativo

### Nivel 1: BÃ¡sico

**AprenderÃ¡s:**
- QuÃ© es un escaneo
- Tipos de objetivos (IP, dominio, rango)
- Escaneo TCP SYN (-sS) - recomendado
- Escaneo TCP Connect (-sT) - sin root
- Ping Scan (-sn) - descubrimiento
- Especificar puertos (-p)
- Control de timing (-T)

**Tiempo estimado:** 20-30 minutos

### Nivel 2: Intermedio

**AprenderÃ¡s:**
- UDP Scan (-sU) - descubrimiento UDP
- DetecciÃ³n de versiones (-sV)
- DetecciÃ³n de SO (-O)
- Escaneo agresivo (-A)
- Filtros de salida (--open)
- Saltar ping (-Pn)
- Escaneo rÃ¡pido (-F)
- Modo verbose (-v, -vv)

**Tiempo estimado:** 30-40 minutos

### Nivel 3: Avanzado

**AprenderÃ¡s:**
- Scripts NSE (--script)
- Argumentos de scripts (--script-args)
- FragmentaciÃ³n de paquetes (-f)
- MTU customizado (--mtu)
- Spoofing de MAC (--spoof-mac)
- Decoys/seÃ±uelos (-D)
- Especificar interfaz (-e)
- Agregar datos aleatorios (--data-length)

**Tiempo estimado:** 40-60 minutos

### Nivel 4: Salida y Reportes

**AprenderÃ¡s:**
- Formato normal (-oN) - texto plano
- Formato XML (-oX) - para herramientas
- Formato grepable (-oG) - para shell
- Todos los formatos (-oA)

**Tiempo estimado:** 15-20 minutos

---

## ðŸŽ“ Ejemplos de Uso

### Ejemplo 1: Escaneo RÃ¡pido de Red

```bash
nmap -sn -T4 192.168.1.0/24
```

**Â¿QuÃ© hace?**
- Descubre quÃ© hosts estÃ¡n activos
- RÃ¡pido y sin intrusiÃ³n
- Ideal para mapeo inicial

### Ejemplo 2: AuditorÃ­a Completa

```bash
nmap -A -sV -sC -oA reporte 192.168.1.100
```

**Â¿QuÃ© hace?**
- AnÃ¡lisis profundo del servidor
- Identifica servicios, versiones, OS
- Ejecuta scripts de anÃ¡lisis
- Guarda en 3 formatos

### Ejemplo 3: Escaneo Sigiloso

```bash
nmap -sS -T2 -p- 192.168.1.100
```

**Â¿QuÃ© hace?**
- Escaneo discreto de TODOS los puertos
- Timing lento (menos detectable)
- Muy sigiloso

### Ejemplo 4: DetecciÃ³n de Vulnerabilidades

```bash
nmap --script vuln -sV 192.168.1.100
```

**Â¿QuÃ© hace?**
- Busca vulnerabilidades conocidas
- Tiempo: 1-2 minutos
- Muy evidente en logs

---

## ðŸ“ Archivos Generados

El programa crea/usa los siguientes archivos:

### Historial
```
~/.nmap_tutor_historial.json
```
- Guarda Ãºltimos 100 comandos
- JSON estructurado
- AutomÃ¡tico

### Comandos Guardados
```
~/.nmap_tutor_comandos/
â”œâ”€ comando1.txt
â”œâ”€ comando2.txt
â””â”€ comando3.txt
```
- Directorio de comandos personalizados
- Creado automÃ¡ticamente
- Para referencia futura

---

## âš™ï¸ Consejos PrÃ¡cticos

### Para Principiantes

1. âœ… **Inicia con Nivel 1** - Entiende lo bÃ¡sico
2. âœ… **Practica en tu propia mÃ¡quina** - Usa VM virtuales
3. âœ… **Lee todas las explicaciones** - Son muy detalladas
4. âœ… **Ejecuta los ejemplos** - Observa los resultados
5. âœ… **Haz mis comandos gradualmente** - No todo a la vez

### MÃ¡quinas Virtuales para Practicar

- **Vulnhub.com** - CTFs y mÃ¡quinas virtuales vulnerables
- **DVWA** - AplicaciÃ³n web deliberadamente insegura
- **VulnerableApp** - MÃ¡quinas diseÃ±adas para aprender
- **Local Lab** - Tu propia VM de Ubuntu en VirtualBox

### Seguridad

âš ï¸ **IMPORTANTE:**
- NUNCA escanees sistemas que no poseas
- ObtÃ©n **autorizaciÃ³n escrita** antes de escanear
- Los alumnos necesitan **consentimiento explÃ­cito**
- Documentar todo para defensa legal

---

## ðŸ”§ Troubleshooting

### "Nmap no encontrado"

```bash
# Verifica si estÃ¡ instalado
which nmap

# Si no aparece, instÃ¡lalo
sudo apt install nmap

# O verifica la versiÃ³n
nmap -V
```

### "colorama no estÃ¡ instalado"

El programa funciona sin colorama, pero se ve mejor con Ã©l:

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
# Verifica que Python 3 estÃ© instalado
python3 --version

# Verifica que el archivo sea ejecutable
chmod +x nmap_interactive_tutor.py

# Ejecuta con python3 explÃ­citamente
python3 /ruta/nmap_interactive_tutor.py
```

---

## ðŸ“– Recursos Adicionales

### DocumentaciÃ³n Oficial
- **Sitio de Nmap**: https://nmap.org
- **Manual de Nmap**: https://nmap.org/book/
- **Referencia de NSE**: https://nmap.org/nsedoc/

### Tutoriales en LÃ­nea
- **HackerOne**: GuÃ­as de bugging
- **TryHackMe**: Cursos interactivos
- **Udemy**: Cursos de Nmap

### Comunidades
- **Foros de Nmap**: https://nmap.org/community
- **Reddit r/netsec**: Red de seguridad
- **StackOverflow**: Preguntas tÃ©cnicas

---

## ðŸ“ VersiÃ³n

- **VersiÃ³n**: 1.0.0
- **Fecha**: 2026
- **Python mÃ­nimo**: 3.7
- **SO**: Linux

---

## ðŸ“„ Licencia

Este programa es educativo y de uso libre para propÃ³sitos de aprendizaje.

---

## âš ï¸ ADVERTENCIA LEGAL IMPORTANTE

### AVISO LEGAL

Este programa es **SOLO educativo**. Eres responsable de tus acciones.

### Legalidad

El escaneo de puertos **NO AUTORIZADO** es **ILEGAL** en muchas jurisdicciones:

- **USA**: ViolaciÃ³n del "Computer Fraud and Abuse Act (CFAA)"
- **UE**: ViolaciÃ³n del GDPR y leyes nacionales de ciberdelito
- **LATAM**: Leyes nacionales sobre acceso no autorizado
- **CONSECUENCIAS**: Multas y/o cÃ¡rcel

### Normas de Uso

âœ… **PERMITIDO:**
- Escanear tu propio hardware
- Escanear mÃ¡quinas virtuales propias
- Escanear laboratorios autorizados
- Penetration Testing CON PERMISO ESCRITO
- AuditorÃ­as de seguridad contratadas

âŒ **PROHIBIDO:**
- Escanear sistemas sin autorizaciÃ³n
- Escanear redes ajenas
- Buscar vulnerabilidades no autorizadas
- Hacer daÃ±o o acceso no autorizado
- Acuso pÃºblicamente de vulnerabilidades sin aviso privado

### Responsabilidad

```
AL USAR ESTE PROGRAMA ACEPTAS QUE:

- Entiendes que es solo para educaciÃ³n
- UsarÃ¡s Nmap responsablemente
- Solo escanearÃ¡s sistemas autorizados
- Eres responsable de tus acciones
- El autor NO es responsable del mal uso
- RespetarÃ¡s las leyes de tu paÃ­s
```

---

## ðŸ‘¨â€ðŸ« Autor

Creado como herramienta educativa para la comunidad de ciberseguridad.

---

## ðŸ™ Agradecimientos

- **Nmap.org**: Por la excelente herramienta
- **Comunidad Open Source**: Por el software libre
- **Educadores**: Por inspirar este proyecto

---

**Â¡Que disfrutes aprendiendo Nmap! ðŸš€**

*Recuerda: Solo eres "Ã©tico" si actÃºas con Ã©tica.*

"# nmap_interactive_tutor" 
