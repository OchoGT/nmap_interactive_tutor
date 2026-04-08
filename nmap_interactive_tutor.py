#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════╗
║                  NMAP INTERACTIVE TUTOR                      ║
║               Aprende Nmap desde cero hasta avanzado         ║
║                                                               ║
║  Un asistente educativo interactivo en consola que enseña    ║
║  a usar Nmap de forma progresiva y práctica                  ║
╚═══════════════════════════════════════════════════════════════╝

Autor: Tutor de Nmap
Fecha: 2026
Descripción: Programa educativo interactivo para aprender Nmap
Python: 3.7+
SO: Linux
"""

import argparse
import os
import re
import sys
import subprocess
import json
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Intentar importar colorama para colores en consola
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False
    print("⚠️  colorama no está instalado. Ejecuta: pip install colorama")
    print("   El programa funcionará sin colores.\n")

    class Fore:
        RED = ''
        GREEN = ''
        YELLOW = ''
        CYAN = ''
        MAGENTA = ''
        WHITE = ''
        BLUE = ''

    class Back:
        BLACK = ''

    class Style:
        RESET_ALL = ''
        BRIGHT = ''


# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN Y CONSTANTES
# ═══════════════════════════════════════════════════════════════

HISTORIAL_FILE = Path.home() / ".nmap_tutor_historial.json"
COMANDOS_GUARDADOS = Path.home() / ".nmap_tutor_comandos"
DEFAULT_SAVE_PATH: Optional[Path] = None

# Crear directorio para comandos guardados
COMANDOS_GUARDADOS.mkdir(exist_ok=True)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Nmap Interactive Tutor - herramienta educativa interactiva para Nmap'
    )
    parser.add_argument(
        '--ruta-guardado',
        dest='ruta_guardado',
        help='Ruta completa de carpeta donde se guardarán los archivos. Si se usa, evita la solicitud interactiva de ruta base.',
        default=None
    )
    return parser.parse_args()


def obtener_ruta_guardado(ruta_destino: Optional[str] = None) -> Optional[Path]:
    """Obtiene ruta de guardado: usa ruta destino si se pasa, o pide ruta base y nombre de carpeta."""
    from pathlib import Path

    if ruta_destino:
        carpeta_guardado = Path(ruta_destino).expanduser()
        if carpeta_guardado.exists() and carpeta_guardado.is_file():
            print(f"{Fore.RED}❌ La ruta especificada es un archivo, no una carpeta: {carpeta_guardado}{Style.RESET_ALL}")
            return None

        try:
            carpeta_guardado.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.GREEN}✓ Carpeta de guardado establecida: {carpeta_guardado}{Style.RESET_ALL}")
            return carpeta_guardado
        except Exception as e:
            print(f"{Fore.RED}❌ Error creando carpeta: {e}{Style.RESET_ALL}")
            return None

    # Si hay una ruta predeterminada configurada en la línea de comandos, usarla
    if DEFAULT_SAVE_PATH:
        try:
            DEFAULT_SAVE_PATH.mkdir(parents=True, exist_ok=True)
            print(f"{Fore.GREEN}✓ Carpeta de guardado predeterminada: {DEFAULT_SAVE_PATH}{Style.RESET_ALL}")
            return DEFAULT_SAVE_PATH
        except Exception as e:
            print(f"{Fore.RED}❌ Error creando carpeta predeterminada: {e}{Style.RESET_ALL}")
            return None

    # Ruta por defecto: Desktop
    default_ruta = Path.home() / "Desktop"

    print(f"\n{Fore.CYAN}CONFIGURACIÓN DE GUARDADO{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ruta base (ENTER para Desktop): {Style.RESET_ALL}", end="")
    ruta_base_str = input().strip()

    if not ruta_base_str:
        ruta_base = default_ruta
    else:
        ruta_base = Path(ruta_base_str).expanduser()

    # Verificar que la ruta base existe
    if not ruta_base.exists():
        print(f"{Fore.RED}❌ La ruta no existe. Creando: {ruta_base}{Style.RESET_ALL}")
        try:
            ruta_base.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"{Fore.RED}❌ Error creando ruta: {e}{Style.RESET_ALL}")
            return None

    # Pedir nombre de carpeta
    while True:
        nombre_carpeta = input(f"{Fore.YELLOW}Nombre de la carpeta: {Style.RESET_ALL}").strip()
        if nombre_carpeta:
            break
        print(f"{Fore.RED}❌ Nombre requerido.{Style.RESET_ALL}")

    # Crear carpeta
    carpeta_guardado = ruta_base / nombre_carpeta
    try:
        carpeta_guardado.mkdir(parents=True, exist_ok=True)
        print(f"{Fore.GREEN}✓ Carpeta creada: {carpeta_guardado}{Style.RESET_ALL}")
        return carpeta_guardado
    except Exception as e:
        print(f"{Fore.RED}❌ Error creando carpeta: {e}{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}❌ Error creando carpeta: {e}{Style.RESET_ALL}")
        return None


# ═══════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════════

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('clear' if os.name == 'posix' else 'cls')


def esperar(segundos: float = 1):
    """Pausa la ejecución."""
    time.sleep(segundos)


def imprimir(
    texto: str,
    color: str = Fore.WHITE,
    fondo: str = '',
    titulo: bool = False,
    error: bool = False
):
    """Imprime texto con formato y colores."""
    if error:
        print(f"{Fore.RED}❌ ERROR: {texto}{Style.RESET_ALL}")
    elif titulo:
        print(f"\n{Style.BRIGHT}{color}{'='*60}")
        print(f"{texto}")
        print(f"{'='*60}{Style.RESET_ALL}\n")
    else:
        print(f"{color}{texto}{Style.RESET_ALL}")


def imprimir_titulo(texto: str):
    """Imprime un título destacado."""
    imprimir(texto, Fore.CYAN, titulo=True)


def pregunta_si_no(prompt: str, permitir_info: bool = True) -> str:
    """
    Realiza una pregunta sí/no/info con validación.
    
    Returns:
        str: 's', 'n', 'info', 'ejemplo' o 'saltar'
    """
    while True:
        opciones = "(s/n"
        if permitir_info:
            opciones += "/info/ejemplo/saltar"
        opciones += "): "

        respuesta = input(f"{Fore.YELLOW}{prompt} {opciones}{Style.RESET_ALL}").strip().lower()

        if respuesta in ['s', 'n', 'info', 'ejemplo', 'saltar']:
            return respuesta
        print(f"{Fore.RED}❌ Opción no válida. Intenta de nuevo.{Style.RESET_ALL}")


def validar_ip_dominio(objetivo: str) -> bool:
    """Valida si es una IP válida, dominio o rango de red."""
    import re
    # Patrón simple para IPv4
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    # Patrón para rango de red CIDR (ej: 192.168.1.0/24)
    cidr_pattern = r'^(\d{1,3}\.){3}\d{1,3}/(1[0-9]|2[0-9]|3[0-2]|[1-9])$'
    # Patrón simple para dominio
    dominio_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'

    if re.match(ipv4_pattern, objetivo):
        partes = objetivo.split('.')
        return all(0 <= int(p) <= 255 for p in partes)
    elif re.match(cidr_pattern, objetivo):
        # Validar que la IP base sea válida
        ip_base = objetivo.split('/')[0]
        partes = ip_base.split('.')
        if not all(0 <= int(p) <= 255 for p in partes):
            return False
        # Validar que el prefijo sea válido (1-32)
        prefijo = int(objetivo.split('/')[1])
        return 1 <= prefijo <= 32
    elif re.match(dominio_pattern, objetivo):
        return True
    return False


def validar_puertos(puerto_str: str) -> bool:
    """Valida formato de puertos de Nmap."""
    import re
    # Aceptar: "80", "80,443", "80-100", "80,443,8000-9000"
    pattern = r'^(\d+(-\d+)?)(,\d+(-\d+)?)*$'
    return bool(re.match(pattern, puerto_str)) if puerto_str else False


def guardar_historial(comando: str):
    """Guarda comandos en historial."""
    try:
        historial = []
        if HISTORIAL_FILE.exists():
            with open(HISTORIAL_FILE, 'r') as f:
                historial = json.load(f)
        
        historial.append({
            'comando': comando,
            'timestamp': datetime.now().isoformat()
        })
        
        # Mantener solo los últimos 100 comandos
        historial = historial[-100:]
        
        with open(HISTORIAL_FILE, 'w') as f:
            json.dump(historial, f, indent=2)
    except Exception as e:
        print(f"{Fore.YELLOW}⚠️  No se pudo guardar el historial: {e}{Style.RESET_ALL}")


def cargar_historial() -> List[str]:
    """Carga historial de comandos."""
    try:
        if HISTORIAL_FILE.exists():
            with open(HISTORIAL_FILE, 'r') as f:
                data = json.load(f)
                return [item['comando'] for item in data]
        return []
    except:
        return []


def instancia_barra_progreso(duracion: int = 3):
    """Simula una barra de progreso."""
    pasos = 30
    for i in range(pasos + 1):
        porcentaje = (i / pasos) * 100
        barra = '█' * i + '░' * (pasos - i)
        print(f"\r{Fore.GREEN}Cargando... [{barra}] {porcentaje:.0f}%{Style.RESET_ALL}", end='')
        time.sleep(duracion / pasos)
    print()


def verificar_nmap_instalado() -> bool:
    """Verifica si Nmap está instalado en el sistema."""
    resultado = subprocess.run(['which', 'nmap'], capture_output=True)
    return resultado.returncode == 0


def diagnosticar_error_nmap(error_texto: str) -> str:
    """Identifica qué bandera causó el error."""
    error_lower = error_texto.lower()
    
    if "skip port scan" in error_lower and "-sn" in error_lower:
        return "\n🔍 DIAGNÓSTICO: -sn no se puede combinar con otros escaneos.\n💡 SOLUCIÓN: Usa -sn SOLO o usa -sS/-sT con -p.\n"
    
    if "not valid with any other scan types" in error_lower:
        return "\n🔍 DIAGNÓSTICO: Combínaste tipos de escaneo incompatibles.\n💡 SOLUCIÓN: Usa solo UN tipo: -sS, -sT, -sU, -sn, etc.\n"
    
    if "invalid" in error_lower and "t" in error_lower:
        return "\n🔍 DIAGNÓSTICO: Timing (-T) inválido.\n💡 SOLUCIÓN: Usa -T0, -T1, -T2, -T3, -T4 o -T5.\n"
    
    if "permission denied" in error_lower:
        return "\n🔍 DIAGNÓSTICO: Necesitas permisos de administrador.\n💡 SOLUCIÓN: Ejecuta con sudo o usa -sT en lugar de -sS.\n"
    
    return f"\n🔍 ERROR: {error_texto}\n"


def validar_banderas_compatibles(comando: str) -> Tuple[bool, str]:
    """Valida que las banderas del comando sean compatibles."""
    tipos_escaneo = ['-sS', '-sT', '-sA', '-sW', '-sM', '-sU', '-sN', '-sF', '-sX', '-sn']
    tipos_encontrados = [t for t in tipos_escaneo if f" {t}" in f" {comando}"]
    
    if len(tipos_encontrados) > 1:
        return False, f"❌ No puedes combinar: {', '.join(tipos_encontrados)}\n💡 Usa solo UN tipo de escaneo.\n"
    
    if '-sn' in comando and any(opt in comando for opt in ['-p ', '-p-', '-F', '-sV', '-sC', '-O', '-A']):
        return False, "❌ -sn no se puede combinar con -p, -sV, -O o -A.\n💡 Usa -sn SOLO para ping scan.\n"
    
    import re
    timings = re.findall(r'-T\d', comando)
    if timings and len(timings) > 1:
        return False, "❌ Solo puedes usar UN timing (-T0 a -T5).\n"
    
    for timing in timings:
        if timing not in ['-T0', '-T1', '-T2', '-T3', '-T4', '-T5']:
            return False, f"❌ Timing inválido: {timing}. Usa -T0 a -T5.\n"
    
    return True, ""


def ejecutar_nmap(comando: str) -> Tuple[bool, str]:
    """Ejecuta un comando de Nmap con validación y diagnóstico."""
    valido, msg_error = validar_banderas_compatibles(comando)
    if not valido:
        return False, msg_error
    
    try:
        proceso = subprocess.Popen(
            comando,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        salida = ""
        print(f"\n{Fore.CYAN}Ejecutando Nmap...{Style.RESET_ALL}\n")
        
        while True:
            linea = proceso.stdout.readline()
            if not linea:
                break
            print(linea.rstrip())
            salida += linea

        proceso.wait()

        if proceso.returncode == 0:
            return True, salida
        else:
            error_output = proceso.stderr.read() if proceso.stderr else "Error desconocido"
            return False, error_output

    except Exception as e:
        return False, f"Excepción: {str(e)}"


# ═══════════════════════════════════════════════════════════════
# BASE DE DATOS EDUCATIVA
# ═══════════════════════════════════════════════════════════════

BASE_CONOCIMIENTO = {
    # NIVEL 1: BÁSICO
    'nivel1': {
        'nombre': '🔰 NIVEL 1: BÁSICO',
        'descripcion': 'Fundamentos de escaneo con Nmap',
        'opciones': {
            'objetivo': {
                'titulo': 'Especificar objetivo (IP, dominio o rango de red)',
                'explicacion': '''
El objetivo es la dirección IP o nombre de dominio que deseas escanear.

EJEMPLOS:
- IP única: nmap 192.168.1.100
- Dominio: nmap example.com
- Rango de IPs: nmap 192.168.1.0/24
- Múltiples: nmap 192.168.1.1 192.168.1.2

⚠️  IMPORTANTE: Solo escanea sistemas propios o con autorización explícita.
El escaneo no autorizado es ilegal en muchas jurisdicciones.
                ''',
                'ejemplo': 'nmap 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'objetivo'
            },
            '-sS': {
                'titulo': 'TCP SYN Scan (Escaneo sigiloso)',
                'explicacion': '''
El escaneo SYN es el más popular y eficiente.

¿QUÉ HACE?
- Envía paquetes SYN a cada puerto
- Si recibe SYN-ACK, el puerto está abierto
- Finaliza la conexión sin completarla (por eso es sigiloso)

VENTAJAS:
✓ Más rápido que TCP Connect
✓ Más sigiloso (no completa conexiones)
✓ Por defecto en Nmap

CUÁNDO USAR:
→ Escaneos generales
→ Cuando necesitas velocidad y precisión
→ Requiere permisos de root

NIVEL DE RIESGO: Bajo
NIVEL DE RUIDO: Bajo-Medio
                ''',
                'ejemplo': 'nmap -sS 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-sT': {
                'titulo': 'TCP Connect Scan (Conexión completa)',
                'explicacion': '''
Completa la conexión TCP de tres vías (three-way handshake).

¿QUÉ HACE?
- Completa la conexión TCP completa
- Más lento pero funciona sin permisos de root
- Registra más eventos en logs

VENTAJAS:
✓ No requiere permisos especiales
✓ Funciona detrás de firewalls complejos

DESVENTAJAS:
✗ Más lento
✗ Más evidente en logs

CUÁNDO USAR:
→ Cuando no tienes permisos de root
→ Sistemas con restricciones
→ Escaneos menos agresivos

NIVEL DE RIESGO: Bajo
NIVEL DE RUIDO: Medio-Alto
                ''',
                'ejemplo': 'nmap -sT 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-sn': {
                'titulo': 'Ping Scan (Descubrimiento de hosts)',
                'explicacion': '''
Solo detecta qué hosts están activos, sin escanear puertos.

¿QUÉ HACE?
- Envía pings ICMP
- Identifica hosts activos
- NO escanea puertos

VENTAJAS:
✓ Muy rápido
✓ Útil para mapeo de red
✓ Bajo impacto

DESVENTAJAS:
✗ Sin información de puertos
✗ Algunos hosts pueden bloquearlo

CUÁNDO USAR:
→ Descubrir qué máquinas están activas
→ Mapeo inicial de red
→ Reconocimiento previo

NIVEL DE RIESGO: Muy bajo
NIVEL DE RUIDO: Bajo
                ''',
                'ejemplo': 'nmap -sn 192.168.1.0/24',
                'parametro_requerido': False,
                'bandera': True
            },
            '-p': {
                'titulo': 'Especificar puertos a escanear',
                'explicacion': '''
Define qué puertos deseas escanear.

FORMATOS:
- Puertos específicos: -p 80,443,3306
- Rango: -p 1-1000
- Combinado: -p 80,443,8000-9000
- Todos: -p-
- Servicios: -p http,https,ssh

PUERTOS COMUNES:
- 21: FTP
- 22: SSH
- 80: HTTP
- 443: HTTPS
- 3306: MySQL
- 5432: PostgreSQL
- 3389: RDP

CUÁNDO USAR:
→ Cuando conoces qué puertos necesitas verificar
→ Para escaneos más rápidos
→ Auditorías enfocadas

NOTA: Sin -p, Nmap escanea los 1000 puertos más comunes
                ''',
                'ejemplo': 'nmap -p 80,443,22,3306 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'puertos'
            },
            '-T': {
                'titulo': 'Plantilla de timing (velocidad)',
                'explicacion': '''
Controla la velocidad del escaneo. Va de T0 (muy lento) a T5 (muy rápido).

OPCIONES BÁSICAS:
- T3: Normal (por defecto, equilibrado)
- T4: Agresivo (más rápido, requiere red e)
- T5: Muy agresivo (máxima velocidad, puede perder datos)

OTRAS OPCIONES:
- T0: Paranoico (muy lento, máxima sigilo)
- T1: Sigiloso (lento)
- T2: Educado (lento)

CUÁNDO USAR:
→ T3: Escaneos normales, redes estables
→ T4: Redes rápidas
→ T5: Redes muy rápidas o contras el tiempo

ADVERTENCIA:
⚠️  Timing más agresivo = más evidente
⚠️  Timing más lento = menos detectable pero más lento
                ''',
                'ejemplo': 'nmap -T4 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'timing'
            },
        }
    },

    # NIVEL 2: INTERMEDIO
    'nivel2': {
        'nombre': '⚙️  NIVEL 2: INTERMEDIO',
        'descripcion': 'Técnicas avanzadas de escaneo',
        'opciones': {
            '-sU': {
                'titulo': 'UDP Scan (Escaneo de puertos UDP)',
                'explicacion': '''
Escanea protocolos UDP (diferentes a TCP).

¿QUÉ HACE?
- Busca servicios UDP abiertos
- Más lento que TCP
- Algunos servicios solo usan UDP

SERVICIOS UDP COMUNES:
- 53: DNS
- 123: NTP
- 161: SNMP
- 500: IPSec
- 67-68: DHCP

VENTAJAS:
✓ Encuentra servicios UDP
✓ Detección más completa

DESVENTAJAS:
✗ Mucho más lento
✗ Menos fiable (algunos hosts ignoran UDP)

CUÁNDO USAR:
→ Cuando necesitas auditar servicios UDP
→ Auditorías completas
→ Análisis de configuración

CONSEJO: Combina con -sS: nmap -sU -sS
NIVEL DE RIESGO: Bajo
NIVEL DE RUIDO: Medio
                ''',
                'ejemplo': 'nmap -sU 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-sV': {
                'titulo': 'Detección de versiones de servicios',
                'explicacion': '''
Identifica qué versión específica de cada servicio se ejecuta.

¿QUÉ HACE?
- Conecta a puertos abiertos
- Analiza los banners de respuesta
- Identifica programas y versiones
- Busca vulnerabilidades conocidas

EJEMPLO DE SALIDA:
80/tcp open http	Apache httpd 2.4.41
22/tcp open ssh	OpenSSH 7.4

VENTAJAS:
✓ Información detallada de servicios
✓ Base para auditoría de vulnerabilidades

DESVENTAJAS:
✗ Más lento (más conexiones)
✗ Puede desencadenar alertas IDS

CUÁNDO USAR:
→ Evaluación de vulnerabilidades
→ Inventario de software
→ Auditorías de seguridad

NIVEL DE RIESGO: Bajo-Medio
NIVEL DE RUIDO: Medio-Alto
                ''',
                'ejemplo': 'nmap -sV 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-O': {
                'titulo': 'Detección de sistema operativo',
                'explicacion': '''
Intenta identificar el sistema operativo del objetivo.

¿QUÉ HACE?
- Envía paquetes especiales
- Analiza las respuestas
- Compara con base de datos
- Identifica OS, versión, dispositivo

EJEMPLO DE SALIDA:
Device type: general purpose
OS: Linux 4.15 - 5.6

REQUISITOS:
- Requiere permisos de root en Linux
- Funciona mejor con al menos un puerto abierto

VENTAJAS:
✓ Información del OS
✓ Mejor entendimiento del objetivo

DESVENTAJAS:
✗ Requiere permisos elevados
✗ Puede no ser 100% exacto

CUÁNDO USAR:
→ Auditorías completas
→ Reconocimiento del objetivo
→ Contextualización de vulnerabilidades

CONSEJO: Usa -O con -sV para mejores resultados
NIVEL DE RIESGO: Medio
NIVEL DE RUIDO: Alto
                ''',
                'ejemplo': 'nmap -O 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-A': {
                'titulo': 'Escaneo agresivo (todo combinado)',
                'explicacion': '''
Combina -sV, -O, --script=default, --traceroute

¿QUÉ HACE?
- Detect versión (-sV)
- Detect SO (-O)
- Ejecuta scripts por defecto
- Traza ruta hasta objetivo
- Equivalente a: -sV -O --script=default --traceroute

VENTAJAS:
✓ Información muy completa
✓ Análisis profundo en un comando
✓ Ideal para evaluar objetivos desconocidos

DESVENTAJAS:
✗ Muy lento
✗ Muy evidente en logs
✗ Puede desencadenar alarmas IDS/IPS

CUÁNDO USAR:
→ Auditoría completa de penal-testing
→ Análisis profundo con autorización
→ Evaluación de seguridad integral

⚠️  USAR CON PRECAUCIÓN - PUEDE DESPERTAR DEFENSAS

NIVEL DE RIESGO: Alto
NIVEL DE RUIDO: Muy Alto
                ''',
                'ejemplo': 'nmap -A 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '--open': {
                'titulo': 'Mostrar solo puertos abiertos',
                'explicacion': '''
Filtra la salida para mostrar SOLO puertos abiertos.

¿QUÉ HACE?
- Oculta puertos cerrados
- Oculta puertos filtrados
- Solo muestra abiertos

SALIDA SIN --open:
80/tcp   open     http
443/tcp  closed   https
3306/tcp filtered mysql

SALIDA CON --open:
80/tcp   open     http

VENTAJAS:
✓ Salida más limpia
✓ Fácil de leer
✓ Menos ruido visual

CUÁNDO USAR:
→ Cuando ya conoces qué puertos te interesan
→ Informes ejecutivos
→ Automatización de scripts

NIVEL DE RIESGO: Ninguno (solo filtrado de salida)
NIVEL DE RUIDO: No aplica
                ''',
                'ejemplo': 'nmap --open 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-Pn': {
                'titulo': 'Saltar ping (tratar host como activo)',
                'explicacion': '''
Asume que el objetivo está activo sin verificar con ping.

¿QUÉ HACE?
- Omite la etapa de ping
- Escanea aunque ping no responda
- Algunos hosts bloquean ICMP

CASOS DE USO:
- Hosts que bloquean ping pero tienen puertos abiertos
- Hosts detrás de firewalls que filtran ICMP
- Redes con respuestas ICMP lentas

SIN -Pn:
1. Nmap ping
2. Si no responde, asume offline
3. Salta el escaneo

CON -Pn:
1. Nmap escanea directamente
2. Ignora respuesta a ping

VENTAJAS:
✓ Encuentra hosts silenciosos
✓ Evita falsos negativos

DESVENTAJAS:
✗ Puede ser más lento si el host no existe
✗ Escanea incluso objetivos offline

CUÁNDO USAR:
→ Cuando ping no funciona
→ Hosts en redes restrictivas
→ Escaneos exhaustivos

NIVEL DE RIESGO: Bajo
NIVEL DE RUIDO: Bajo
                ''',
                'ejemplo': 'nmap -Pn 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-F': {
                'titulo': 'Fast scan (escaneo rápido)',
                'explicacion': '''
Escanea solo los 100 puertos más comunes en lugar de 1000.

¿QUÉ HACE?
- Reduce el número de puertos a escanear
- Mucho más rápido
- Cubre puertos más frecuentes

PUERTOS ESCANEADOS:
100 puertos más comunes (HTTP, SSH, SMTP, DNS, etc.)

TIEMPO COMPARADA:
- Escaneo normal: 10-30 segundos
- Con -F: 2-5 segundos (5-6 veces más rápido)

VENTAJAS:
✓ Mucho más rápido
✓ Ideal para reconocimiento rápido
✓ Bajo costo de recursos

DESVENTAJAS:
✗ Puede perder puertos abiertos menos comunes
✗ Información limitada

CUÁNDO USAR:
→ Reconocimiento inicial rápido
→ Búsqueda exploratoria
→ Cuando la velocidad es crítica

CONSEJO: Combina con -A para análisis rápido completo
NIVEL DE RIESGO: Muy bajo
NIVEL DE RUIDO: Bajo
                ''',
                'ejemplo': 'nmap -F 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '-v': {
                'titulo': 'Modo verbose (información detallada)',
                'explicacion': '''
Aumenta el nivel de detalle en la salida de Nmap.

NIVELES:
-v:    Verbose (información adicional)
-vv:   Muy verbose (información muy detallada)
-vvv:  Super verbose (máximo detalle - a veces muy ruidoso)

SIN VERBOSE:
Nmap 7.80 ( https://nmap.org )
Starting Nmap
Nmap scan report for 192.168.1.100

CON -v:
Nmap 7.80 ( https://nmap.org )
Starting Nmap at Wed Apr 5 2026
Nmap scan report for 192.168.1.100
Host is up (0.0034s latency)
Not shown: 997 closed ports

CON -vv:
[Mucho más detalle: estadísticas, tiempos, servicios, etc.]

VENTAJAS:
✓ Mejor entendimiento del proceso
✓ Información de diagnóstico
✓ Útil para debugging

DESVENTAJAS:
✗ Salida más grande
✗ Puede ser abrumador

CUÁNDO USAR:
→ Debugging de escaneos
→ Análisis detallado
→ Cuando necesitas entender qué hace Nmap

CONSEJO: Usa -v o -vv según lo necesites
NIVEL DE RIESGO: Ninguno (solo salida)
NIVEL DE RUIDO: No aplica
                ''',
                'ejemplo': 'nmap -v 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
        }
    },

    # NIVEL 3: AVANZADO
    'nivel3': {
        'nombre': '🔥 NIVEL 3: AVANZADO',
        'descripcion': 'Técnicas sofisticadas y evasión',
        'opciones': {
            '--script': {
                'titulo': 'Ejecutar scripts NSE (Nmap Scripting Engine)',
                'explicacion': '''
Ejecuta scripts especializados para pruebas adicionales.

¿QUÉ HACE?
- Ejecuta scripts Lua especializados
- Detección de vulnerabilidades
- Análisis de configuración
- Extracción de información

EJEMPLOS DE SCRIPTS:
- default: Categoría por defecto
- vuln: Detecta vulnerabilidades
- safe: Scripts seguros
- discovery: Descubrimiento de información
- auth: Pruebas de autenticación

SINTAXIS:
--script vuln           (ejecuta todos los scripts de vulnerabilidades)
--script http-title     (ejecuta script específico)
--script not vuln       (ejecuta todos MENOS vulnerabilidades)
--script vuln,ssl*      (wildcards permitidos)

VENTAJAS:
✓ Detección automatizada de vulnerabilidades
✓ Información muy detallada
✓ Pruebas especializadas

DESVENTAJAS:
✗ Muy lento
✗ Muy evidente
✗ Puede ser intrusivo

CUÁNDO USAR:
→ Auditorías de vulnerabilidades
→ Penetration testing
→ Evaluación de seguridad completa

⚠️  MUY INTRUSIVO - USAR SOLO CON AUTORIZACIÓN
NIVEL DE RIESGO: Alto
NIVEL DE RUIDO: Muy Alto
                ''',
                'ejemplo': 'nmap --script vuln 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'script'
            },
            '--script-args': {
                'titulo': 'Argumentos para scripts NSE',
                'explicacion': '''
Pasa argumentos específicos a los scripts NSE.

SINTAXIS:
--script-args creds=db:pass

EJEMPLOS:
--script-args timeout=10000
--script-args http.useragent="Mozilla/5.0"
--script-args user=admin,pass=password

CASOS DE USO:
- Pasar credenciales
- Ajustar timeouts
- Especificar parámetros personalizados

CUÁNDO USAR:
→ Cuando necesitas personalizar scripts
→ Pruebas de autenticación
→ Ajustes de rendimiento

NOTA: Combina con --script

NIVEL DE RIESGO: Medio-Alto
NIVEL DE RUIDO: Alto
                ''',
                'ejemplo': '--script-args timeout=10000',
                'parametro_requerido': True,
                'tipo': 'args_script'
            },
            '-f': {
                'titulo': 'Fragmentación de paquetes (evasión)',
                'explicacion': '''
Fragmenta paquetes para evadir detección de IDS/IPS.

¿QUÉ HACE?
- Divide paquetes en fragmentos más pequeños
- Dificulta la detección de patrones
- Técnica stealth/evasión

NIVELES:
-f:     Fragmentación básica (8 bytes)
-ff:    Fragmentación agresiva

VENTAJAS:
✓ Evasión de detección
✓ Pasa algunos firewalls

DESVENTAJAS:
✗ Puede afectar velocidad
✗ Algunos firewalls pueden rechazarlo
✗ Puede no funcionar contra sistemas modernos

ADVERTENCIA:
⚠️  Técnica sofisticada
⚠️  Solo con autorización explícita
⚠️  Cuidado: puede parecer ataque

CUÁNDO USAR:
→ Evasión de IDS
→ Pentesting autorizado
→ Labs/entrenamiento

NIVEL DE RIESGO: Muy Alto
NIVEL DE RUIDO: Bajo (propósito: ser sigiloso)
                ''',
                'ejemplo': 'nmap -f 192.168.1.100',
                'parametro_requerido': False,
                'bandera': True
            },
            '--mtu': {
                'titulo': 'Ajustar MTU (Max Transmission Unit)',
                'explicacion': '''
Especifica el tamaño máximo de paquetes (evasión).

VALORES COMUNES:
- MTU estándar: 1500 bytes
- Redes Jumbo: 9000 bytes
- Para evasión: 24, 32, 40 (múltiplos de 8)

SINTAXIS:
--mtu 24

¿QUÉ HACE?
- Reduce tamaño de paquetes
- Evasión de firewalls/IDS
- Fragmenta automáticamente

VENTAJAS:
✓ Evasión efectiva
✓ Funciona con muchos sistemas

DESVENTAJAS:
✗ Más lento
✗ Puede fallar en conexiones
✗ Detectable por sistemas avanzados

CUÁNDO USAR:
→ Técnica de evasión avanzada
→ Pentesting autorizado
→ Cuando otros métodos fallan

NIVEL DE RIESGO: Muy Alto
NIVEL DE RUIDO: Bajo (propósito: ser sigiloso)
                ''',
                'ejemplo': 'nmap --mtu 24 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'mtu'
            },
            '--spoof-mac': {
                'titulo': 'Spoofing de dirección MAC',
                'explicacion': '''
Falsifica la dirección MAC origen en paquetes.

SINTAXIS:
--spoof-mac 0            (MAC aleatoria)
--spoof-mac AA:BB:CC:DD:EE:FF  (MAC específica)
--spoof-mac Cisco        (MAC conocida de fabricante)

FABRICANTES DISPONIBLES:
Apple, Cisco, Dell, HP, Lenovo, Microsoft, Nokia, etc.

VENTAJAS:
✓ Evasión basada en MAC
✓ Útil para proteger identidad en LAN

DESVENTAJAS:
✗ Solo funciona en redes locales
✗ Sistemas avanzados pueden detectarlo
✗ Requiere permiso root en Linux

CUÁNDO USAR:
→ Ocultación en redes locales
→ Testing de ACLs basadas en MAC
→ Investigaciones forenses

⚠️  TÉCNICA AVANZADA - REQUIERE PERMISOS ROOT

NIVEL DE RIESGO: Muy Alto
NIVEL DE RUIDO: Medio (puede activar alertas)
                ''',
                'ejemplo': 'nmap --spoof-mac 0 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'mac'
            },
            '-D': {
                'titulo': 'Decoys (escaneo con señuelos)',
                'explicacion': '''
Utiliza direcciones IP señuelo para ocultar tu verdadera IP.

SINTAXIS:
-D RND:10               (10 IPs aleatorias + la tuya)
-D 192.168.1.1,192.168.1.5,ME  (IPs específicas, ME = tu IP)

EJEMPLO:
nmap -D RND:5,ME,192.168.1.1 192.168.1.100

¿QUÉ HACE?
- Mezcla tu tráfico con otros
- Confunde análisis de logs
- IDS ve múltiples fuentes

VENTAJAS:
✓ Esconde tu IP real
✓ Dificulta atribución

DESVENTAJAS:
✗ No funciona con conexiones TCP completas
✗ IDS moderno puede detectarlo
✗ Solo funciona en redes locales
✗ Admin puede ver todos los orígenes

CUÁNDO USAR:
→ Evasión de detección básica
→ Testing de seguridad
→ Labs educativos

⚠️  FÁCILMENTE DETECTABLE POR SISTEMAS MODERNOS

NIVEL DE RIESGO: Muy Alto
NIVEL DE RUIDO: Medio
                ''',
                'ejemplo': 'nmap -D RND:5,ME 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'decoys'
            },
            '-e': {
                'titulo': 'Especificar interfaz de red',
                'explicacion': '''
Define la interfaz de red a usar para escaneo.

SINTAXIS:
-e eth0     (Linux)
-e en0      (macOS)

USOS:
- Máquinas con múltiples interfaces
- Fuerza uso de interfaz específica
- Debugging de problemas de red

VENTAJAS:
✓ Control específico
✓ Útil en máquinas multi-interfaz

CUÁNDO USAR:
→ Máquinas con múltiples NICs
→ VPNs/Proxy específicos
→ Testing de red

NIVEL DE RIESGO: Bajo
NIVEL DE RUIDO: Ninguno
                ''',
                'ejemplo': 'nmap -e eth0 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'interfaz'
            },
            '--data-length': {
                'titulo': 'Agregar datos aleatorios a paquetes',
                'explicacion': '''
Añade bytes aleatorios a paquetes para evasión.

SINTAXIS:
--data-length 100   (agrega 100 bytes aleatorios)

¿QUÉ HACE?
- Cambia el tamaño de paquetes
- Evade firewalls basados en signaturas
- Paquetes más normales

VENTAJAS:
✓ Evasión de firewalls
✓ Parece tráfico más ordinario

DESVENTAJAS:
✗ Ralentiza escaneo
✗ Sistemas modernos pueden detectarlo

CUÁNDO USAR:
→ Evasión de IDS
→ Pentesting autorizado

NIVEL DE RIESGO: Alto
NIVEL DE RUIDO: Bajo (propósito: ser sigiloso)
                ''',
                'ejemplo': 'nmap --data-length 100 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'datos'
            },
        }
    },

    # NIVEL 4: SALIDA Y REPORTES
    'nivel4': {
        'nombre': '💾 NIVEL 4: SALIDA Y REPORTES',
        'descripcion': 'Exportación y generación de reportes',
        'opciones': {
            '-oN': {
                'titulo': 'Salida normal a archivo',
                'explicacion': '''
Guarda salida en formato de texto plano normal.

SINTAXIS:
-oN nombre_archivo.txt
-oN /ruta/archivo.txt

EJEMPLO:
nmap -oN escaneo.txt 192.168.1.100

CARACTERÍSTICAS:
- Formato legible para humanos
- Contiene toda la salida de consola
- Fácil de leer después
- Tamaño moderado de archivo

VENTAJAS:
✓ Fácil de leer
✓ Compatible con búsqueda de texto

CUÁNDO USAR:
→ Reportes básicos
→ Archivos de referencia
→ Documentación

EJEMPLO DE CONTENIDO:
Starting Nmap 7.80
Nmap scan report for 192.168.1.100
Host is up (0.0034s latency)
Not shown: 997 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
443/tcp  open     https
                ''',
                'ejemplo': 'nmap -oN escaneo.txt 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'archivo'
            },
            '-oX': {
                'titulo': 'Salida XML',
                'explicacion': '''
Guarda salida en formato XML (máchina legible).

SINTAXIS:
-oX nombre_archivo.xml

EJEMPLO:
nmap -oX escaneo.xml 192.168.1.100

CARACTERÍSTICAS:
- Formato XML estructurado
- Ideal para procesamiento automatizado
- Herramientas pueden parsear fácilmente
- Contiene toda la información

VENTAJAS:
✓ Ideal para scripts/herramientas
✓ Estructura clara
✓ Fácil de procesar programáticamente

DESVENTAJAS:
✗ No legible para humanos sin herramienta
✗ Archivo más grande

CUÁNDO USAR:
→ Automatización
→ Integración con otras herramientas
→ Procesamiento de datos
→ Reportes generados automáticamente

USOS:
- Parsear con Python/scripts
- Importar en herramientas de BI
- Integración con SIEM
                ''',
                'ejemplo': 'nmap -oX escaneo.xml 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'archivo'
            },
            '-oG': {
                'titulo': 'Salida Grepable (formato especial)',
                'explicacion': '''
Salida optimizada para búsqueda con grep/herramientas.

SINTAXIS:
-oG nombre_archivo.gnmap

EJEMPLO:
nmap -oG escaneo.gnmap 192.168.1.100

CARACTERÍSTICAS:
- Una línea por host
- Campos separados por tabulaciones
- Optimizada para grep y awk
- Fácil de procesar

FORMATO:
Host: 192.168.1.100	Ports: 22/open/tcp//ssh///,80/open/tcp//http///

VENTAJAS:
✓ Muy fácil de procesar con comandos Unix
✓ Legible en una línea
✓ Ideal para shell scripts

CUÁNDO USAR:
→ Procesamiento con grep/awk
→ Scripts Unix/Linux
→ Análisis rápido
→ Historiales de escaneo

EJEMPLO DE USO:
grep "Ports:" escaneo.gnmap | grep "open"
                ''',
                'ejemplo': 'nmap -oG escaneo.gnmap 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'archivo'
            },
            '-oA': {
                'titulo': 'Salida en TODOS los formatos',
                'explicacion': '''
Guarda automáticamente en TRES formatos simultáneamente.

SINTAXIS:
-oA nombre_base
(crea: nombre_base.nmap, nombre_base.xml, nombre_base.gnmap)

EJEMPLO:
nmap -oA escaneo
Genera:
- escaneo.nmap (Normal)
- escaneo.xml (XML)
- escaneo.gnmap (Grepable)

VENTAJAS:
✓ Cubre todos los casos de uso
✓ Solo un comando
✓ Máxima compatibilidad
✓ Comodidad

DESVENTAJAS:
✗ Usa 3x espacio en disco
✗ Crea 3 archivos

CUÁNDO USAR:
→ SIEMPRE que necesites reportes
→ Cuando no sabes qué formato necesitarás
→ Documentación completa
→ Mejor práctica

RECOMENDACIÓN:
✓ Este es el modo recomendado para reportes

EJEMPLO COMPLETO:
nmap -A -oA reporte_completo 192.168.1.100
                ''',
                'ejemplo': 'nmap -oA escaneo 192.168.1.100',
                'parametro_requerido': True,
                'tipo': 'archivo'
            },
        }
    }
}

EJEMPLOS_PRACTICOS = {
    'escaneo_rapido': {
        'titulo': '⚡ Escaneo rápido de red',
        'descripcion': 'Identifica hosts activos en una red',
        'comando': 'nmap -sn -T4 192.168.1.0/24',
        'explicacion': '''
Este comando:
- Realiza ping scan (-sn): solo identifica hosts activos
- Timing agresivo (-T4): más rápido
- Escanea rango: 192.168.1.0 a 192.168.1.255

Tiempo estimado: 5-10 segundos
Información: Hosts activos
Ruido: Bajo
        '''
    },
    'escaneo_completo': {
        'titulo': '🔍 Escaneo completo con detalles',
        'descripcion': 'Análisis profundo de un servidor',
        'comando': 'nmap -A -sV -sC -oA reporte 192.168.1.100',
        'explicacion': '''
Este comando:
- -A: Escaneo agresivo completo
- -sV: Detección de versiones
- -sC: Scripts por defecto
- -oA: Exporta en 3 formatos
- Objetivo: 192.168.1.100

Tiempo estimado: 30-60 segundos
Información: Muy completa (servicios, versiones, OS, scripts)
Ruido: Muy alto (evidente en logs)
        '''
    },
    'audit_basica': {
        'titulo': '🛡️  Auditoría de seguridad básica',
        'descripcion': 'Escaneo enfocado en vulnerabilidades',
        'comando': 'nmap --script vuln -sV 192.168.1.100',
        'explicacion': '''
Este comando:
- --script vuln: Ejecuta scripts de vulnerabilidades
- -sV: Detección de versiones
- Busca vulnerabilidades conocidas

Tiempo estimado: 60-120 segundos
Información: Vulnerabilidades detectadas
Ruido: Muy alto (muy intrusivo)
        '''
    },
    'reconocimiento': {
        'titulo': '🕵️  Reconocimiento sigiloso',
        'descripcion': 'Escaneo discreto y rápido',
        'comando': 'nmap -sS -T2 -p- 192.168.1.100',
        'explicacion': '''
Este comando:
- -sS: TCP SYN scan (sigiloso)
- -T2: Timing lento (evita detección)
- -p-: Escanea TODOS los puertos
- Objetivo: 192.168.1.100

Tiempo estimado: 2-5 minutos
Información: Todos los puertos abiertos
Ruido: Bajo (propósito: ser sigiloso)
        '''
    },
    'escaneo_rapido_puertos': {
        'titulo': '⚡ Escaneo rápido de puertos comunes',
        'descripcion': 'Rápido escaneo de puertos usuales',
        'comando': 'nmap -F -T4 192.168.1.100',
        'explicacion': '''
Este comando:
- -F: Fast scan (solo 100 puertos comunes)
- -T4: Timing agresivo (rápido)
- Objetivo: 192.168.1.100

Tiempo estimado: 2-5 segundos
Información: Puertos comunes abiertos
Ruido: Bajo
        '''
    }
}


# ═══════════════════════════════════════════════════════════════
# CLASE PRINCIPAL: CONSTRUCTOR DE COMANDOS
# ═══════════════════════════════════════════════════════════════

class ConstructorNmap:
    """Construye comandos de Nmap de forma interactiva."""

    def __init__(self):
        """Inicializa el constructor."""
        self.comando_actual = "nmap"
        self.objetivo = ""
        self.opciones = []
        self.parametros = {}
        self.historial = cargar_historial()

    def limpiar(self):
        """Limpia el comando actual."""
        self.comando_actual = "nmap"
        self.objetivo = ""
        self.opciones = []
        self.parametros = {}

    def agregar_opcion(self, opcion: str, valor: Optional[str] = None):
        """Agrega una opción al comando."""
        if valor:
            self.comando_actual += f" {opcion} {valor}"
        else:
            self.comando_actual += f" {opcion}"

    def establecer_objetivo(self, objetivo: str):
        """Establece el objetivo del escaneo."""
        if validar_ip_dominio(objetivo):
            self.objetivo = objetivo
            self.comando_actual += f" {objetivo}"
            return True
        return False

    def mostrar_comando_actual(self):
        """Muestra el comando actual de forma legible."""
        imprimir(f"\n{'━'*60}", Fore.CYAN)
        imprimir(f"COMANDO ACTUAL:", Fore.GREEN, titulo=False)
        imprimir(f"{self.comando_actual}", Fore.YELLOW)
        imprimir(f"{'━'*60}\n", Fore.CYAN)

    def validar_comando(self) -> bool:
        """Valida que el comando tenga los elementos mínimos."""
        return bool(self.objetivo) and self.comando_actual != "nmap"


# ═══════════════════════════════════════════════════════════════
# FUNCIONES DE INTERFAZ PRINCIPAL
# ═══════════════════════════════════════════════════════════════

def pantalla_bienvenida():
    """Muestra la pantalla de bienvenida."""
    limpiar_pantalla()

    bienvenida = """
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║              🎯 NMAP INTERACTIVE TUTOR 🎯                     ║
║                                                                ║
║         Tu asistente educativo para dominar Nmap              ║
║                                                                ║
║                    (Aprende desde cero)                        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────┐
│ ¿QUÉ ES NMAP?                                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Nmap (Network Mapper) es una herramienta de código abierto    │
│  para exploración de redes y auditoría de seguridad.           │
│                                                                 │
│  FUNCIONES PRINCIPALES:                                        │
│  ✓ Descubrimiento de hosts en la red                          │
│  ✓ Escaneo de puertos                                         │
│  ✓ Identificación de servicios y versiones                    │
│  ✓ Detección del sistema operativo                            │
│  ✓ Análisis de vulnerabilidades                               │
│  ✓ Mapeo de redes complejas                                   │
│                                                                 │
│  USOS LEGALES:                                                 │
│  ✓ Pentesting (con autorización)                              │
│  ✓ Auditorías de seguridad                                    │
│  ✓ Administración de redes                                    │
│  ✓ Análisis forense                                           │
│  ✓ HackingEtico y CTF                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

    """

    print(bienvenida)

    advertencia = f"""
┌─────────────────────────────────────────────────────────────────┐
│ ⚠️  ADVERTENCIA LEGAL E ÉTICA                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  {Fore.RED}IMPORTANTE:{Style.RESET_ALL}                                                │
│                                                                 │
│  • {Fore.YELLOW}SOLO escanea sistemas que POSEAS o que AUTORICES{Style.RESET_ALL}       │
│  • El escaneo no autorizado es ILEGAL en la mayoría de         │
│    jurisdicciones                                              │
│  • Violar leyes puede resultar en cargos criminales            │
│  • USA: Computer Fraud and Abuse Act (CFAA)                   │
│  • UE: Reglamento General de Protección de Datos (GDPR)        │
│  • LATAM: Leyes nacionales de ciberseguridad                   │
│                                                                 │
│  {Fore.GREEN}RESPONSABILIDAD:{Style.RESET_ALL}                                         │
│  Este programa es educativo. Eres responsable de tus acciones. │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
    """

    print(advertencia)

    # Preguntar aceptación
    while True:
        respuesta = input(f"{Fore.YELLOW}¿Entiendes y aceptas estas advertencias? (s/n): {Style.RESET_ALL}").strip().lower()
        if respuesta == 's':
            break
        elif respuesta == 'n':
            print(f"{Fore.RED}Programa cancelado.{Style.RESET_ALL}")
            sys.exit(0)

    limpiar_pantalla()


def menu_principal() -> str:
    """Muestra el menú principal y retorna la opción seleccionada."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"              📋 MENÚ PRINCIPAL")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    opciones = {
        '1': 'Modo Aprendizaje Guiado (RECOMENDADO)',
        '2': 'Construcción Libre de Comando',
        '3': 'Ver Ejemplos Prácticos',
        '4': 'Ver Historial de Comandos',
        '5': 'Ayuda General',
        '6': 'Retos de Nmap',
        '0': 'Salir'
    }

    for key, value in opciones.items():
        if key == '1':
            print(f"{Fore.GREEN}[{key}] {value} ⭐{Style.RESET_ALL}")
        else:
            print(f"[{key}] {value}")

    print()
    while True:
        opcion = input(f"{Fore.YELLOW}Selecciona una opción (0-6): {Style.RESET_ALL}").strip()
        if opcion in opciones:
            return opcion
        print(f"{Fore.RED}❌ Opción no válida.{Style.RESET_ALL}")


def seleccionar_nivel() -> str:
    """Permite seleccionar nivel de aprendizaje."""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"           📚 SELECCIONA TU NIVEL DE APRENDIZAJE")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    niveles = [
        ('nivel1', BASE_CONOCIMIENTO['nivel1']['nombre']),
        ('nivel2', BASE_CONOCIMIENTO['nivel2']['nombre']),
        ('nivel3', BASE_CONOCIMIENTO['nivel3']['nombre']),
        ('nivel4', BASE_CONOCIMIENTO['nivel4']['nombre']),
    ]

    for i, (key, titulo) in enumerate(niveles, 1):
        desc = BASE_CONOCIMIENTO[key]['descripcion']
        print(f"[{i}] {titulo}")
        print(f"    {desc}\n")

    while True:
        opcion = input(f"{Fore.YELLOW}Elige nivel (1-4): {Style.RESET_ALL}").strip()
        if opcion in ['1', '2', '3', '4']:
            return ['nivel1', 'nivel2', 'nivel3', 'nivel4'][int(opcion) - 1]
        print(f"{Fore.RED}❌ Opción no válida.{Style.RESET_ALL}")


def modo_aprendizaje_guiado(constructor: ConstructorNmap):
    """Modo interactivo de aprendizaje."""
    while True:
        nivel = seleccionar_nivel()
        nivel_info = BASE_CONOCIMIENTO[nivel]

        limpiar_pantalla()
        imprimir_titulo(nivel_info['nombre'])
        imprimir(nivel_info['descripcion'], Fore.CYAN)

        constructor.limpiar()

        # Solicitar objetivo
        print(f"\n{Fore.CYAN}PASO 1: ESPECIFICAR OBJETIVO{Style.RESET_ALL}\n")
        while True:
            objetivo = input(f"{Fore.YELLOW}Ingresa IP, dominio o rango de red a escanear: {Style.RESET_ALL}").strip()
            if validar_ip_dominio(objetivo):
                constructor.establecer_objetivo(objetivo)
                print(f"{Fore.GREEN}✓ Objetivo aceptado: {objetivo}{Style.RESET_ALL}\n")
                break
            else:
                print(f"{Fore.RED}❌ IP, dominio o rango de red inválido. Intenta de nuevo.{Style.RESET_ALL}\n")

        # Enseñar opciones del nivel
        print(f"\n{Fore.CYAN}PASO 2: CONFIGURE LAS OPCIONES DEL NIVEL{Style.RESET_ALL}\n")

        for opcion_key, opcion_info in nivel_info['opciones'].items():
            if opcion_key == 'objetivo':
                continue  # Ya configurado

            print(f"\n{Fore.MAGENTA}{'─'*60}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{opcion_info['titulo']}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}{'─'*60}{Style.RESET_ALL}\n")

            # Mostrar explicación
            print(f"{Fore.WHITE}{opcion_info['explicacion']}{Style.RESET_ALL}")

            # Preguntar si usar
            respuesta = pregunta_si_no(f"\n¿Quieres usar {opcion_key}?")

            if respuesta == 'info':
                # Ya mostró la explicación
                respuesta = pregunta_si_no(f"\n¿Agregar {opcion_key}?")

            if respuesta == 'ejemplo':
                imprimir(f"Ejemplo: {opcion_info['ejemplo']}", Fore.CYAN)
                respuesta = pregunta_si_no(f"\n¿Agregar {opcion_key}?")

            if respuesta == 'saltar':
                continue

            if respuesta == 's':
                # Pedir parámetros si es necesario
                if 'parametro_requerido' in opcion_info and opcion_info['parametro_requerido']:
                    tipo = opcion_info.get('tipo', 'generico')

                    if tipo == 'puertos':
                        while True:
                            puertos = input(f"{Fore.YELLOW}Ingresa puerto(s) (ej: 80,443,3306 o 1-1000): {Style.RESET_ALL}").strip()
                            if validar_puertos(puertos):
                                constructor.agregar_opcion(f"{opcion_key} {puertos}")
                                break
                            print(f"{Fore.RED}❌ Formato de puertos inválido.{Style.RESET_ALL}")

                    elif tipo == 'timing':
                        while True:
                            timing = input(f"{Fore.YELLOW}Ingresa timing (T0-T5): {Style.RESET_ALL}").strip()
                            if timing in ['T0', 'T1', 'T2', 'T3', 'T4', 'T5']:
                                constructor.agregar_opcion(f"{opcion_key}{timing}")
                                break
                            print(f"{Fore.RED}❌ Timing inválido (usa T0-T5).{Style.RESET_ALL}")

                    elif tipo == 'script':
                        script = input(f"{Fore.YELLOW}Ingresa nombre de script (ej: vuln, default): {Style.RESET_ALL}").strip()
                        if script:
                            constructor.agregar_opcion(f"{opcion_key} {script}")

                    elif tipo == 'args_script':
                        args = input(f"{Fore.YELLOW}Ingresa argumentos de script: {Style.RESET_ALL}").strip()
                        if args:
                            constructor.agregar_opcion(f"{opcion_key} {args}")

                    elif tipo == 'mtu':
                        mtu = input(f"{Fore.YELLOW}Ingresa valor MTU (múltiplo de 8): {Style.RESET_ALL}").strip()
                        if mtu:
                            constructor.agregar_opcion(f"{opcion_key} {mtu}")

                    elif tipo == 'mac':
                        mac = input(f"{Fore.YELLOW}Ingresa MAC (0, FABRICANTE, o AA:BB:CC:DD:EE:FF): {Style.RESET_ALL}").strip()
                        if mac:
                            constructor.agregar_opcion(f"{opcion_key} {mac}")

                    elif tipo == 'decoys':
                        decoys = input(f"{Fore.YELLOW}Ingresa decoys (ej: RND:5,ME): {Style.RESET_ALL}").strip()
                        if decoys:
                            constructor.agregar_opcion(f"{opcion_key} {decoys}")

                    elif tipo == 'interfaz':
                        interfaz = input(f"{Fore.YELLOW}Ingresa nombre interfaz (eth0, en0, etc): {Style.RESET_ALL}").strip()
                        if interfaz:
                            constructor.agregar_opcion(f"{opcion_key} {interfaz}")

                    elif tipo == 'datos':
                        datos = input(f"{Fore.YELLOW}Ingresa longitud de datos: {Style.RESET_ALL}").strip()
                        if datos:
                            constructor.agregar_opcion(f"{opcion_key} {datos}")

                    elif tipo == 'archivo':
                        archivo = input(f"{Fore.YELLOW}Ingresa nombre de archivo: {Style.RESET_ALL}").strip()
                        if archivo:
                            constructor.agregar_opcion(f"{opcion_key} {archivo}")

                else:
                    # Solo agregar la flag
                    constructor.agregar_opcion(opcion_key)

        # Mostrar comando final
        constructor.mostrar_comando_actual()

        # Preguntar qué hacer
        print(f"\n{Fore.CYAN}PASO 3: FINALIZAR{Style.RESET_ALL}\n")

        while True:
            accion = input(f"{Fore.YELLOW}¿Qué deseas hacer?\n[1] Ejecutar ahora\n[2] Guardar en archivo\n[3] Editar comando\n[4] Volver atrás\n\nOpción: {Style.RESET_ALL}").strip()

            if accion == '1':
                if not verifica_nmap_instalado():
                    print(f"{Fore.RED}❌ Nmap no está instalado.{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}Instala con: sudo apt install nmap{Style.RESET_ALL}")
                    break

                guardar_historial(constructor.comando_actual)
                exito, salida = ejecutar_nmap(constructor.comando_actual)

                if exito:
                    print(f"{Fore.GREEN}\n✓ Escaneo completado exitosamente.{Style.RESET_ALL}")
                    guardar_res = input(f"\n{Fore.YELLOW}¿Guardar resultado en archivo? (s/n): {Style.RESET_ALL}").strip().lower()
                    if guardar_res == 's':
                        carpeta = obtener_ruta_guardado()
                        if carpeta:
                            try:
                                # Guardar comando
                                ruta_comando = carpeta / "comando.txt"
                                with open(ruta_comando, 'w') as f:
                                    f.write(f"Comando: {constructor.comando_actual}\n")
                                    f.write(f"Ejecutado: {datetime.now().isoformat()}\n")
                                
                                # Guardar resultado
                                ruta_resultado = carpeta / "resultado.txt"
                                with open(ruta_resultado, 'w') as f:
                                    f.write(f"Comando: {constructor.comando_actual}\n")
                                    f.write(f"Ejecutado: {datetime.now().isoformat()}\n")
                                    f.write("="*60 + "\n")
                                    f.write(salida)
                                
                                print(f"{Fore.GREEN}✓ Archivos guardados en: {carpeta}{Style.RESET_ALL}")
                                print(f"  - comando.txt")
                                print(f"  - resultado.txt")
                            except Exception as e:
                                print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}\n❌ ERROR{Style.RESET_ALL}")
                    print(diagnosticar_error_nmap(salida))
                    
                    opt_error = input(f"\n{Fore.YELLOW}[1]Editar [2]Guardar [3]Ver error [4]Volver: {Style.RESET_ALL}").strip()
                    
                    if opt_error == '1':
                        nueva_cmd = input(f"{Fore.YELLOW}Nuevo comando: {Style.RESET_ALL}").strip()
                        if nueva_cmd:
                            constructor.comando_actual = nueva_cmd
                            constructor.mostrar_comando_actual()
                            continue
                    
                    elif opt_error == '2':
                        carpeta = obtener_ruta_guardado()
                        if carpeta:
                            try:
                                # Guardar comando y error
                                ruta_error = carpeta / "error.txt"
                                with open(ruta_error, 'w') as f:
                                    f.write(f"Comando: {constructor.comando_actual}\n")
                                    f.write(f"Guardado: {datetime.now().isoformat()}\n")
                                    f.write(f"Error: {salida}\n")
                                print(f"{Fore.GREEN}✓ Archivo guardado: {ruta_error}{Style.RESET_ALL}")
                            except Exception as e:
                                print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
                    
                    elif opt_error == '3':
                        print(f"\n{Fore.RED}Error: {salida}{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}ENTER...{Style.RESET_ALL}")

                input(f"\n{Fore.YELLOW}Presiona ENTER para continuar...{Style.RESET_ALL}")
                break

            elif accion == '2':
                carpeta = obtener_ruta_guardado()
                if carpeta:
                    try:
                        ruta_comando = carpeta / "comando.txt"
                        with open(ruta_comando, 'w') as f:
                            f.write(f"# Comando Nmap\n")
                            f.write(f"Comando: {constructor.comando_actual}\n")
                            f.write(f"Guardado: {datetime.now().isoformat()}\n")
                        print(f"{Fore.GREEN}✓ Comando guardado en: {ruta_comando}{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
                break

            elif accion == '3':
                print(f"\n{Fore.CYAN}Comando actual:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{constructor.comando_actual}{Style.RESET_ALL}\n")
                comando_editado = input(f"{Fore.YELLOW}Nuevo comando: {Style.RESET_ALL}").strip()
                if comando_editado:
                    constructor.comando_actual = comando_editado
                    constructor.mostrar_comando_actual()

            elif accion == '4':
                break

        # Preguntar si continuar o volver
        continuar = input(f"\n{Fore.YELLOW}¿Quieres hacer otro escaneo? (s/n): {Style.RESET_ALL}").strip().lower()
        if continuar != 's':
            break


def modo_construccion_libre(constructor: ConstructorNmap):
    """Modo libre para construir comandos personalizados."""
    limpiar_pantalla()
    imprimir_titulo("🛠️  CONSTRUCCIÓN LIBRE DE COMANDO")

    constructor.limpiar()

    # Objetivo
    while True:
        objetivo = input(f"{Fore.YELLOW}IP, dominio o rango de red objetivo: {Style.RESET_ALL}").strip()
        if validar_ip_dominio(objetivo):
            constructor.establecer_objetivo(objetivo)
            break
        print(f"{Fore.RED}❌ IP, dominio o rango de red inválido.{Style.RESET_ALL}")

    # Opciones libres
    print(f"\n{Fore.CYAN}Ingresa opciones de Nmap (O solo ENTER para terminar):{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ejemplos: -sS -p 80,443 -sV -O{Style.RESET_ALL}\n")

    while True:
        opcion = input(f"{Fore.YELLOW}Opción: {Style.RESET_ALL}").strip()
        if not opcion:
            break
        constructor.agregar_opcion(opcion)
        constructor.mostrar_comando_actual()

    # Ejecutar o guardar
    constructor.mostrar_comando_actual()

    while True:
        accion = input(f"{Fore.YELLOW}\n[1] Ejecutar [2] Guardar [3] Editar [0] Cancelar: {Style.RESET_ALL}").strip()

        if accion == '1':
            if verificar_nmap_instalado():
                guardar_historial(constructor.comando_actual)
                exito, salida = ejecutar_nmap(constructor.comando_actual)
                
                if not exito:
                    print(diagnosticar_error_nmap(salida))
                    opt_reintentar = input(f"\n{Fore.YELLOW}¿Editar e intentar de nuevo? (s/n): {Style.RESET_ALL}").strip().lower()
                    if opt_reintentar == 's':
                        nueva = input(f"{Fore.YELLOW}Nuevo comando: {Style.RESET_ALL}").strip()
                        if nueva:
                            constructor.comando_actual = nueva
                            constructor.mostrar_comando_actual()
                            continue
                else:
                    print(f"{Fore.GREEN}\n✓ Éxito{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Nmap no instalado.{Style.RESET_ALL}")
            break

        elif accion == '2':
            carpeta = obtener_ruta_guardado()
            if carpeta:
                try:
                    ruta_comando = carpeta / "comando.txt"
                    with open(ruta_comando, 'w') as f:
                        f.write(f"# Comando Nmap\n")
                        f.write(f"Comando: {constructor.comando_actual}\n")
                        f.write(f"Guardado: {datetime.now().isoformat()}\n")
                    print(f"{Fore.GREEN}✓ Comando guardado en: {ruta_comando}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            break

        elif accion == '3':
            nuevo = input(f"{Fore.YELLOW}Nuevo comando: {Style.RESET_ALL}").strip()
            if nuevo:
                constructor.comando_actual = nuevo
                constructor.mostrar_comando_actual()

        elif accion == '0':
            break


def mostrar_ejemplos():
    """Muestra ejemplos prácticos de comandos."""
    limpiar_pantalla()
    imprimir_titulo("🎓 EJEMPLOS PRÁCTICOS")

    print(f"{Fore.WHITE}Aquí hay ejemplos de comandos reales para diferentes situaciones:{Style.RESET_ALL}\n")

    for key, (titulo, info) in enumerate(EJEMPLOS_PRACTICOS.items(), 1):
        print(f"\n{Fore.GREEN}[{key}] {info['titulo']}{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}{info['descripcion']}{Style.RESET_ALL}")
        print(f"    {Fore.YELLOW}$ {info['comando']}{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}{'─'*60}{Style.RESET_ALL}\n")

    while True:
        seleccion = input(f"{Fore.YELLOW}Ver detalles de ejemplo (1-5) o 0 para menú principal: {Style.RESET_ALL}").strip()

        if seleccion == '0':
            break

        ejemplos_list = list(EJEMPLOS_PRACTICOS.values())
        try:
            idx = int(seleccion) - 1
            if 0 <= idx < len(ejemplos_list):
                ejemplo = ejemplos_list[idx]
                print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}{ejemplo['titulo']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
                print(f"{Fore.YELLOW}Comando:{Style.RESET_ALL}")
                print(f"$ {ejemplo['comando']}\n")
                print(f"{Fore.YELLOW}Explicación:{Style.RESET_ALL}")
                print(f"{ejemplo['explicacion']}\n")
        except:
            print(f"{Fore.RED}Opción inválida.{Style.RESET_ALL}")


def mostrar_historial(historial: List[str]):
    """Muestra historial de comandos."""
    limpiar_pantalla()
    imprimir_titulo("📜 HISTORIAL DE COMANDOS")

    if not historial:
        print(f"{Fore.YELLOW}No hay historial aún.{Style.RESET_ALL}\n")
        return

    for i, cmd in enumerate(historial[-20:], 1):  # Últimos 20
        print(f"{Fore.CYAN}[{i}]{Style.RESET_ALL} {cmd}")

    print()


def mostrar_ayuda():
    """Muestra información de ayuda."""
    limpiar_pantalla()
    imprimir_titulo("❓ AYUDA GENERAL")

    ayuda = f"""
{Fore.YELLOW}¿CÓMO USAR ESTE PROGRAMA?{Style.RESET_ALL}

1. {Fore.GREEN}Modo Aprendizaje Guiado:{Style.RESET_ALL}
   - Selecciona un nivel (Básico a Avanzado)
   - Aprende sobre cada opción de Nmap
   - Construye comandos paso a paso
   - El programa explica de forma didáctica

2. {Fore.GREEN}Construcción Libre:{Style.RESET_ALL}
   - Crea comandos personalizados
   - Ingresa opciones manualmente
   - Ejecútalas inmediatamente

3. {Fore.GREEN}Ejemplos Prácticos:{Style.RESET_ALL}
   - Ve ejemplos listos para usar
   - Entiende casos de uso reales

{Fore.YELLOW}RECOMENDACIONES:{Style.RESET_ALL}

✓ Si eres nuevo: Comienza en NIVEL 1 - BÁSICO
✓ Lee las explicaciones completamente
✓ Practica con máquinas virtuales primero
✓ Aumenta los niveles gradualmente
✓ Respeta las leyes de tu país

{Fore.YELLOW}REQUISITOS:{Style.RESET_ALL}

- Python 3.7+
- Nmap instalado (en sistemas Linux: sudo apt install nmap)
- Permisos elevados para algunos escaneos

{Fore.YELLOW}INSTALACIÓN DE NMAP:{Style.RESET_ALL}

{Fore.CYAN}# Debian/Ubuntu{Style.RESET_ALL}
sudo apt update
sudo apt install nmap

{Fore.CYAN}# RedHat/CentOS{Style.RESET_ALL}
sudo yum install nmap

{Fore.CYAN}# Arch{Style.RESET_ALL}
sudo pacman -S nmap

{Fore.YELLOW}MÁS INFORMACIÓN:{Style.RESET_ALL}

- Sitio oficial: https://nmap.org
- Manual: man nmap (en terminal Linux)
- Wiki: https://nmap.org/book/

{Fore.RED}ADVERTENCIA:{Style.RESET_ALL}
Solo usa Nmap en sistemas que autorices.
El escaneo no autorizado es ilegal.

    """
    print(ayuda)


def obtener_retos_nmap() -> List[Dict[str, object]]:
    """Define 25 retos organizados por dificultad."""
    return [
        {
            'nivel': 'facil',
            'titulo': 'Escaneo ping básico',
            'enunciado': 'Realiza un escaneo ping a 192.168.1.10 usando Nmap.',
            'requisitos': [
                {'descripcion': '-sn', 'pattern': r'\b-sn\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Escaneo SYN simple',
            'enunciado': 'Haz un escaneo TCP SYN a 192.168.1.10 en los puertos 22 y 80.',
            'requisitos': [
                {'descripcion': '-sS', 'pattern': r'\b-sS\b'},
                {'descripcion': '-p', 'pattern': r'\b-p\b'},
                {'descripcion': 'Puerto 22', 'pattern': r'\b22\b'},
                {'descripcion': 'Puerto 80', 'pattern': r'\b80\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Detección de versión',
            'enunciado': 'Realiza un escaneo con detección de versión en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-sV', 'pattern': r'\b-sV\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Detección de sistema operativo',
            'enunciado': 'Realiza un escaneo con detección de sistema operativo en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-O', 'pattern': r'\b-O\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Escaneo UDP de DNS',
            'enunciado': 'Escanea el puerto UDP 53 en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-sU', 'pattern': r'\b-sU\b'},
                {'descripcion': '-p 53', 'pattern': r'-p[^\n]*\b53\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Timing rápido',
            'enunciado': 'Realiza un escaneo rápido en 192.168.1.10 con timing T4.',
            'requisitos': [
                {'descripcion': '-T4', 'pattern': r'\b-T4\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Escaneo de rango básico',
            'enunciado': 'Escanea los puertos de 1 a 100 en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-p 1-100', 'pattern': r'-p[^\n]*\b1-100\b'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Escaneo con scripts default',
            'enunciado': 'Realiza un escaneo con los scripts default en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '--script default', 'pattern': r'--script\s+default'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Traceroute por comando',
            'enunciado': 'Realiza un escaneo que incluya traceroute a 192.168.1.10.',
            'requisitos': [
                {'descripcion': '--traceroute', 'pattern': r'--traceroute'}
            ]
        },
        {
            'nivel': 'facil',
            'titulo': 'Listado de hosts',
            'enunciado': 'Realiza un escaneo de listado de hosts (-sL) para 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-sL', 'pattern': r'\b-sL\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo SYN en red /24',
            'enunciado': 'Escanea 192.168.1.0/24 con un escaneo SYN.',
            'requisitos': [
                {'descripcion': '-sS', 'pattern': r'\b-sS\b'},
                {'descripcion': '/24', 'pattern': r'\b192\.168\.1\.0/24\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo rápido de puertos frecuentes',
            'enunciado': 'Escanea los puertos frecuentes y detecta versiones en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-F', 'pattern': r'\b-F\b'},
                {'descripcion': '-sV', 'pattern': r'\b-sV\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo sin ping',
            'enunciado': 'Realiza un escaneo de puerto en 192.168.1.10 sin enviar ping previo.',
            'requisitos': [
                {'descripcion': '-Pn', 'pattern': r'\b-Pn\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo mixto TCP y UDP',
            'enunciado': 'Escanea puertos TCP y UDP en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-sS o -sT', 'pattern': r'(\b-sS\b|\b-sT\b)'},
                {'descripcion': '-sU', 'pattern': r'\b-sU\b'},
                {'descripcion': '-p', 'pattern': r'\b-p\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo furtivo con fragmentación',
            'enunciado': 'Realiza un escaneo furtivo con fragmentación (-f) en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-f', 'pattern': r'\b-f\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo con scripts de vulnerabilidad',
            'enunciado': 'Usa el script vuln en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '--script vuln', 'pattern': r'--script\s+vuln'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo lento con detección de servicios',
            'enunciado': 'Escanea 192.168.1.10 con timing T2 y detección de versión.',
            'requisitos': [
                {'descripcion': '-T2', 'pattern': r'\b-T2\b'},
                {'descripcion': '-sV', 'pattern': r'\b-sV\b'}
            ]
        },
        {
            'nivel': 'medio',
            'titulo': 'Escaneo de puertos abiertos solamente',
            'enunciado': 'Realiza un escaneo y muestra solo puertos abiertos en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '--open', 'pattern': r'--open'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo completo de versión y OS',
            'enunciado': 'Escanea 192.168.1.10 con detección de versión y sistema operativo.',
            'requisitos': [
                {'descripcion': '-sV', 'pattern': r'\b-sV\b'},
                {'descripcion': '-O', 'pattern': r'\b-O\b'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo UDP de 1000 puertos',
            'enunciado': 'Escanea los primeros 1000 puertos UDP en 10.0.0.5.',
            'requisitos': [
                {'descripcion': '-sU', 'pattern': r'\b-sU\b'},
                {'descripcion': '-p 1-1000', 'pattern': r'-p[^\n]*\b1-1000\b'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo con señuelos',
            'enunciado': 'Realiza un escaneo con decoys RND:3 a 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-D RND:3', 'pattern': r'-D\s*RND:3'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo furtivo y lento',
            'enunciado': 'Escanea el puerto 80 en 192.168.1.10 con fragmentación y timing T0.',
            'requisitos': [
                {'descripcion': '-f', 'pattern': r'\b-f\b'},
                {'descripcion': '-T0', 'pattern': r'\b-T0\b'},
                {'descripcion': '-p 80', 'pattern': r'-p[^\n]*\b80\b'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo de scripts HTTP vulnerables',
            'enunciado': 'Escanea 192.168.1.10 usando scripts http-vuln* y timing T4.',
            'requisitos': [
                {'descripcion': '--script http-vuln', 'pattern': r'--script\s+http-vuln'},
                {'descripcion': '-T4', 'pattern': r'\b-T4\b'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo de todos los puertos TCP',
            'enunciado': 'Escanea todos los puertos TCP en 192.168.1.10.',
            'requisitos': [
                {'descripcion': '-p-', 'pattern': r'-p\s*-'},
                {'descripcion': 'o -p 1-65535', 'pattern': r'-p[^\n]*\b1-65535\b'}
            ]
        },
        {
            'nivel': 'dificil',
            'titulo': 'Escaneo con MAC spoofing',
            'enunciado': 'Escanea 192.168.1.10 aplicando suplantación de MAC.',
            'requisitos': [
                {'descripcion': '--spoof-mac', 'pattern': r'--spoof-mac'}
            ]
        }
    ]


def seleccionar_dificultad_retos() -> str:
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"             🧩 RETOS DE NMAP")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    print(f"[1] Fácil   - 10 retos")
    print(f"[2] Medio   - 8 retos")
    print(f"[3] Difícil - 7 retos")

    while True:
        opcion = input(f"{Fore.YELLOW}Selecciona dificultad (1-3): {Style.RESET_ALL}").strip()
        if opcion == '1':
            return 'facil'
        if opcion == '2':
            return 'medio'
        if opcion == '3':
            return 'dificil'
        print(f"{Fore.RED}❌ Opción no válida.{Style.RESET_ALL}")


def evaluar_requisitos_comando(comando: str, requisitos: List[Dict[str, str]]) -> Tuple[bool, List[str]]:
    comando_normalizado = re.sub(r'\s+', ' ', comando.strip())
    faltantes = []
    for req in requisitos:
        if not re.search(req['pattern'], comando_normalizado, re.IGNORECASE):
            faltantes.append(req['descripcion'])
    return (len(faltantes) == 0, faltantes)


def calificar_puntaje(puntos: int, total: int) -> str:
    porcentaje = int((puntos / total) * 100)
    if porcentaje >= 90:
        return f"Excelente ({porcentaje}%)"
    if porcentaje >= 75:
        return f"Bien ({porcentaje}%)"
    if porcentaje >= 50:
        return f"Suficiente ({porcentaje}%)"
    return f"Necesita práctica ({porcentaje}%)"


def modo_retos():
    limpiar_pantalla()
    imprimir_titulo("🏆 RETOS DE NMAP")
    retos = obtener_retos_nmap()

    while True:
        nivel = seleccionar_dificultad_retos()
        retos_nivel = [reto for reto in retos if reto['nivel'] == nivel]

        limpiar_pantalla()
        imprimir_titulo(f"🏅 RETOS - {nivel.upper()}")
        print(f"Tienes {len(retos_nivel)} retos. Ingresa el comando Nmap para cada enunciado.")
        print(f"No seas estricto con el orden: solo valida las banderas principales y puertos.\n")

        aciertos = 0
        for index, reto in enumerate(retos_nivel, 1):
            print(f"{Fore.CYAN}Reto {index}/{len(retos_nivel)}: {reto['titulo']}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}{reto['enunciado']}{Style.RESET_ALL}\n")
            respuesta = input(f"{Fore.YELLOW}Comando Nmap: {Style.RESET_ALL}").strip()

            if not respuesta:
                print(f"{Fore.RED}❌ No ingresaste ningún comando. Se registra como incorrecto.{Style.RESET_ALL}\n")
                continue

            valido, faltantes = evaluar_requisitos_comando(respuesta, reto['requisitos'])
            if valido:
                aciertos += 1
                print(f"{Fore.GREEN}✓ Correcto{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}✗ Falta una o más opciones esperadas:{Style.RESET_ALL}")
                for falta in faltantes:
                    print(f"  - {falta}")
                print(f"{Fore.YELLOW}Puedes intentar otro comando dentro del mismo reto si lo deseas.{Style.RESET_ALL}\n")

        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"Has completado los retos de nivel {nivel}.\n")
        print(f"Aciertos: {Fore.GREEN}{aciertos}{Style.RESET_ALL} de {len(retos_nivel)}")
        print(f"Calificación: {Fore.MAGENTA}{calificar_puntaje(aciertos, len(retos_nivel))}{Style.RESET_ALL}\n")

        repetir = input(f"{Fore.YELLOW}¿Quieres intentar otro nivel de retos? (s/n): {Style.RESET_ALL}").strip().lower()
        if repetir != 's':
            break


def verifica_nmap_instalado() -> bool:
    """Verifica si Nmap está instalado."""
    if not verificar_nmap_instalado():
        print(f"""
{Fore.RED}⚠️  Nmap no está instalado en tu sistema{Style.RESET_ALL}

Para instalar Nmap:

{Fore.CYAN}# Debian/Ubuntu/Linux Mint{Style.RESET_ALL}
sudo apt update
sudo apt install nmap

{Fore.CYAN}# RedHat/CentOS/Fedora{Style.RESET_ALL}
sudo yum install nmap

# Después de instalar, puedes usar este programa normalmente
        """)
        return False
    return True


# ═══════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════════

def main():
    """Función principal de ejecución."""
    try:
        args = parse_arguments()

        global DEFAULT_SAVE_PATH
        if args.ruta_guardado:
            DEFAULT_SAVE_PATH = Path(args.ruta_guardado).expanduser()
            if DEFAULT_SAVE_PATH.exists() and DEFAULT_SAVE_PATH.is_file():
                print(f"{Fore.RED}❌ La ruta de guardado especificada es un archivo, no una carpeta: {DEFAULT_SAVE_PATH}{Style.RESET_ALL}")
                sys.exit(1)

        # Verificar dependencias
        if not HAS_COLORAMA:
            print(f"{Fore.YELLOW}⚠️  Se recomienda instalar colorama: pip install colorama{Style.RESET_ALL}\n")

        # Pantalla de bienvenida
        pantalla_bienvenida()

        # Constructor de comandos
        constructor = ConstructorNmap()

        # Loop principal
        while True:
            opcion = menu_principal()

            if opcion == '1':
                limpiar_pantalla()
                instancia_barra_progreso(2)
                modo_aprendizaje_guiado(constructor)

            elif opcion == '2':
                modo_construccion_libre(constructor)

            elif opcion == '3':
                mostrar_ejemplos()

            elif opcion == '4':
                mostrar_historial(constructor.historial)
                input(f"{Fore.YELLOW}Presiona ENTER...{Style.RESET_ALL}")

            elif opcion == '5':
                mostrar_ayuda()
                input(f"{Fore.YELLOW}Presiona ENTER...{Style.RESET_ALL}")

            elif opcion == '6':
                modo_retos()

            elif opcion == '0':
                print(f"\n{Fore.GREEN}¡Gracias por usar Nmap Interactive Tutor!{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Recuerda: Solo escanea sistemas autorizados.{Style.RESET_ALL}\n")
                break

            limpiar_pantalla()

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\n❌ Programa interrumpido por el usuario.{Style.RESET_ALL}\n")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}\n❌ Error inesperado: {str(e)}{Style.RESET_ALL}\n")
        sys.exit(1)


# ═══════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
