# Nmap Interactive Tutor

Herramienta educativa en Python para aprender a usar Nmap desde nivel básico hasta avanzado mediante una interfaz interactiva en consola.

## Descripción

Este proyecto no reemplaza a Nmap. Funciona como un asistente CLI que:

- explica opciones y banderas importantes
- construye comandos paso a paso
- permite practicar con ejemplos reales
- ayuda a detectar combinaciones inválidas comunes
- facilita el aprendizaje progresivo

Está pensado principalmente para usuarios principiantes, aunque también puede servir como apoyo rápido para quienes ya conocen Nmap.

## Características principales

- aprendizaje guiado por niveles
- construcción libre de comandos
- ejemplos prácticos
- historial de comandos
- ayuda integrada
- retos para practicar
- ejecución directa de comandos Nmap

## Contenido del aprendizaje

### Nivel 1: Básico

- `-sS`
- `-sT`
- `-sn`
- `-p`
- `-T`

### Nivel 2: Intermedio

- `-sU`
- `-sV`
- `-O`
- `-A`
- `--open`
- `-Pn`
- `-F`
- `-v`, `-vv`

### Nivel 3: Avanzado

- `--script`
- `--script-args`
- `-f`
- `--mtu`
- `--data-length`
- `--spoof-mac`
- `-D`
- rangos de red
- `-iL`

### Nivel 4: Salida y reportes

- `-oN`
- `-oX`
- `-oG`
- `-oA`

## Requisitos

- Linux
- Python 3.7 o superior
- Nmap instalado
- `colorama` opcional para mejorar la salida en consola

## Instalación

### Opción rápida

```bash
chmod +x install.sh
./install.sh
```

### Opción manual

```bash
sudo apt update
sudo apt install -y python3 python3-pip nmap
pip3 install -r requirements.txt
chmod +x nmap_interactive_tutor.py
```

## Uso

```bash
python3 nmap_interactive_tutor.py
```

O:

```bash
./nmap_interactive_tutor.py
```

Para algunos escaneos será necesario usar `sudo`.

## Menú principal

- `Modo Aprendizaje Guiado`
- `Construcción Libre de Comando`
- `Ver Ejemplos Prácticos`
- `Ver Historial de Comandos`
- `Ayuda General`
- `Retos de Nmap`

## Archivos principales

- `nmap_interactive_tutor.py`: programa principal
- `QUICK_START.md`: guía rápida
- `COMANDOS_REFERENCIA.md`: referencia de comandos
- `FAQ.md`: preguntas frecuentes
- `INDEX.md`: resumen de archivos

## Verificación rápida

```bash
python3 -m py_compile nmap_interactive_tutor.py
python3 nmap_interactive_tutor.py --help
```

## Advertencia legal

Este proyecto es solo educativo. Usa Nmap únicamente sobre sistemas propios o para los que tengas autorización explícita.

El uso no autorizado de herramientas de reconocimiento puede ser ilegal según la jurisdicción.

