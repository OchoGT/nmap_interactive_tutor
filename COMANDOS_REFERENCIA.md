# 📋 REFERENCIA DE COMANDOS NMAP

Una guía rápida de los comandos más comunes de Nmap.

---

## 🔰 NIVEL 1: BÁSICO

### Escaneos Simples

```bash
# Escaneo básico (1000 puertos comunes)
nmap 192.168.1.100

# Lo mismo pero con nombre de dominio
nmap example.com

# Escaneo de una red (subnet)
nmap 192.168.1.0/24
```

### Tipos de Escaneo

```bash
# TCP SYN Scan (recomendado, requiere root)
nmap -sS 192.168.1.100

# TCP Connect Scan (sin root, más lento)
nmap -sT 192.168.1.100

# UDP Scan (servicios UDP)
nmap -sU 192.168.1.100

# Ping Scan (solo descubre hosts activos)
nmap -sn 192.168.1.0/24

# Null Scan (avanzado)
nmap -sN 192.168.1.100

# FIN Scan (avanzado)
nmap -sF 192.168.1.100

# Xmas Scan (avanzado)
nmap -sX 192.168.1.100
```

### Especificar Puertos

```bash
# Puerto específico
nmap -p 80 192.168.1.100

# Múltiples puertos
nmap -p 80,443,3306 192.168.1.100

# Rango de puertos
nmap -p 1-1000 192.168.1.100

# Todos los puertos (65535)
nmap -p- 192.168.1.100

# Puertos comunes (top 100)
nmap -F 192.168.1.100

# Puertos por servicio
nmap -p http,https,ssh 192.168.1.100
```

### Timing (velocidad)

```bash
# Timing paranoico (muy lento, máximo sigilo)
nmap -T0 192.168.1.100

# Timing sigiloso (lento)
nmap -T1 192.168.1.100

# Timing educado (lento)
nmap -T2 192.168.1.100

# Timing normal (defecto, equilibrado)
nmap -T3 192.168.1.100

# Timing agresivo (rápido)
nmap -T4 192.168.1.100

# Timing muy agresivo (muy rápido, puede perder datos)
nmap -T5 192.168.1.100
```

---

## ⚙️ NIVEL 2: INTERMEDIO

### Detectión de Información

```bash
# Detección de versiones
nmap -sV 192.168.1.100

# Detección de SO
nmap -O 192.168.1.100

# Escaneo agresivo (versión + SO + scripts + traceroute)
nmap -A 192.168.1.100

# Combinación común: versión + SO
nmap -sV -O 192.168.1.100

# Ejecutar scripts de categoría
nmap -sC 192.168.1.100
```

### Opciones de Host

```bash
# Saltar ping (tratar como activo)
nmap -Pn 192.168.1.100

# No resolver DNS
nmap -n 192.168.1.100

# Resolver DNS inverso
nmap -R 192.168.1.100

# Saltar descubrimiento de hosts
nmap -Pn 192.168.1.100
```

### Filtros de Salida

```bash
# Solo mostrar puertos abiertos
nmap --open 192.168.1.100

# Mostrar todos los puertos
nmap 192.168.1.100

# Mostrar razón de cada puerto
nmap --reason 192.168.1.100
```

### Verbosidad

```bash
# Modo verbose (información adicional)
nmap -v 192.168.1.100

# Modo muy verbose
nmap -vv 192.168.1.100

# Modo quiet (mínima salida)
nmap -q 192.168.1.100
```

---

## 🔥 NIVEL 3: AVANZADO

### Scripts NSE

```bash
# Ejecutar scripts por defecto
nmap --script default 192.168.1.100

# Ejecutar scripts de vulnerabilidades
nmap --script vuln 192.168.1.100

# Ejecutar scripts de descubrimiento
nmap --script discovery 192.168.1.100

# Ejecutar scripts específicos
nmap --script http-title 192.168.1.100

# Script específico con argumentos
nmap --script http-brute --script-args userdb=users.txt, passdb=pass.txt 192.168.1.100

# Excluir categoría de scripts
nmap --script "not http" 192.168.1.100

# Usar wildcards
nmap --script ssl* 192.168.1.100

# Listar scripts disponibles
nmap --script-help <nombre_script>
```

### Técnicas de Evasión

```bash
# Fragmentación de paquetes
nmap -f 192.168.1.100

# Fragmentación más agresiva (2 bytes por fragmento)
nmap -ff 192.168.1.100

# MTU personalizado
nmap --mtu 24 192.168.1.100

# Decoys (señuelos con IPs aleatorias)
nmap -D RND:10 192.168.1.100

# Decoys específicos
nmap -D 192.168.1.1,192.168.1.2,ME 192.168.1.100

# Spoofing de MAC address
nmap --spoof-mac 0 192.168.1.100

# MAC de fabricante conocido
nmap --spoof-mac Cisco 192.168.1.100

# Agregar datos aleatorios
nmap --data-length 100 192.168.1.100

# Source port personalizado
nmap -g 53 192.168.1.100

# Delay entre paquetes (en ms)
nmap --delay 100 192.168.1.100

# Timeout personalizado
nmap --host-timeout 300000 192.168.1.100
```

### Opciones de Control

```bash
# Interfaz de red específica
nmap -e eth0 192.168.1.100

# Source IP específica
nmap -S 192.168.1.50 192.168.1.100

# Source port específico
nmap -g 1234 192.168.1.100

# Batch de hosts
nmap --min-parallelism 10 192.168.1.100

# Máximo parallelismo
nmap --max-parallelism 1 192.168.1.100

# Min rate (paquetes/segundo mínimo)
nmap --min-rate 100 192.168.1.100

# Max rate (paquetes/segundo máximo)
nmap --max-rate 1000 192.168.1.100
```

### Entrada y Listas

```bash
# Leer IPs desde archivo
nmap -iL lista_ips.txt

# Leer IPs aleatorias desde archivo
nmap -iR 10 (escanea 10 hosts aleatorios en Internet)

# Excluir hosts específicos
nmap --exclude 192.168.1.50 192.168.1.0/24

# Excluir desde archivo
nmap --excludefile exclusiones.txt 192.168.1.0/24
```

---

## 💾 NIVEL 4: SALIDA Y REPORTES

### Formatos de Salida

```bash
# Formato normal (texto plano)
nmap -oN reporte.txt 192.168.1.100

# Formato XML (para procesar con herramientas)
nmap -oX reporte.xml 192.168.1.100

# Formato grepable (para procesar con grep/awk)
nmap -oG reporte.gnmap 192.168.1.100

# TODOS los formatos simultáneamente
nmap -oA reporte 192.168.1.100
# Genera: reporte.nmap, reporte.xml, reporte.gnmap

# Append a archivo existente
nmap -oN reporte.txt --append-output 192.168.1.100

# Salida en pantalla + archivo
nmap -oN reporte.txt 192.168.1.100 | tee salida.txt
```

### Procesamiento de Resultados

```bash
# Buscar puertos abiertos (usando grepable)
grep "open" reporte.gnmap

# Contar hosts activos
grep "Status: Up" reporte.gnmap | wc -l

# Extraer IPs de archivo grepable
awk '{print $2}' reporte.gnmap

# Convertir XML a HTML (si tienes xsltproc)
xsltproc /usr/share/nmap/nmap.xsl reporte.xml > reporte.html
```

---

## 🎯 COMBINACIONES COMUNES

### Escaneo Rápido
```bash
nmap -F -T4 192.168.1.100
```
- Rápido
- Solo puertos comunes
- Timing agresivo

### Escaneo Completo
```bash
nmap -A -sV -sC -p- -T4 -oA reporte 192.168.1.100
```
- Análisis profundo
- Todos los puertos
- Scripts ejecutados
- Resultado guardado

### Escaneo Sigiloso
```bash
nmap -sS -T2 -p- -Pn 192.168.1.100
```
- TCP SYN (sigiloso)
- Timing lento
- Todos los puertos
- No verifica ping

### Auditoría de Vulnerabilidades
```bash
nmap --script vuln -sV -oA vulns 192.168.1.100
```
- Busca vulnerabilidades
- Detecta versiones
- Guarda resultados

### Descubrimiento de Red
```bash
nmap -sn -T4 192.168.1.0/24
```
- Ping scan
- Rápido
- Sin escaneo de puertos

### Reconocimiento Profundo
```bash
nmap -A -sV -sC --script discovery,vuln -oA recon 192.168.1.100
```
- Muy completo
- Descubrimiento + vulnerabilidades
- Mucha información

---

## 🔄 PROCESAMIENTO DE SALIDA

### Con grep

```bash
# Buscar líneas con "open"
cat reporte.txt | grep "open"

# Contar puertos abiertos
cat reporte.txt | grep "open" | wc -l

# Puertos con servicio específico
cat reporte.txt | grep "http"
```

### Con awk

```bash
# Extraer puerto y estado
awk '{print $1, $2}' reporte.gnmap

# Extraer solo puertos
awk -F'/' '{print $1}' reporte.gnmap

# Contar puertos abiertos
awk '/open/ {count++} END {print count}' reporte.txt
```

### Con sed

```bash
# Extraer líneas entre dos patrones
sed -n '/Nmap scan/,/Nmap done/p' reporte.txt

# Reemplazar texto
sed 's/open/OPEN/g' reporte.txt
```

---

## 💡 CASOS DE USO REALES

### Caso 1: Exploración Inicial
```bash
# Descubre qué está activo
nmap -sn -T4 192.168.1.0/24

# Luego enfócate en host específico
nmap -A -sV -p- 192.168.1.100
```

### Caso 2: Búsqueda de Vulnerabilidades
```bash
# Análisis rápido
nmap --script vuln -sV 192.168.1.100

# Análisis profundo
nmap --script "vuln or default" -sV -p- 192.168.1.100
```

### Caso 3: Monitoreo Regular
```bash
# Escaneo periódico con timestamp
nmap -oA reporte_$(date +%Y%m%d) 192.168.1.100

# Comparar con anterior
diff reporte_20260405.gnmap reporte_20260406.gnmap
```

### Caso 4: Auditoría Completa
```bash
# Escaneo exhaustivo
nmap -A -sV -sC -p 1-65535 -T4 \
  --script vuln,discovery,default \
  -oA auditoria_completa \
  192.168.1.100
```

### Caso 5: Pentesting Sigiloso
```bash
# Bajo ruido
nmap -sS -T1 \
  -f \
  --data-length 100 \
  -D RND:5 \
  --spoof-mac Cisco \
  -p 1-10000 \
  192.168.1.100
```

---

## ⚠️ ADVERTENCIAS Y NOTAS

### Permisos

```bash
# Algunos escaneos necesitan root
sudo nmap -sS 192.168.1.100

# -sT funciona sin root
nmap -sT 192.168.1.100

# -A puede necesitar root
sudo nmap -A 192.168.1.100
```

### Legalidad

⚠️ **IMPORTANTE:**
- ✅ Legal: Escanear tu propio hardware
- ❌ Ilegal: Escanear sistemas sin autorización
- ⚖️ Repercusiones: Multas y/o prisión

### Rendimiento

```bash
# Si se congela o tarda demasiado:

# Aumenta el timing
nmap -T5 192.168.1.100

# Reduce el número de puertos
nmap -F 192.168.1.100

# Usa -Pn si no responde a ping
nmap -Pn 192.168.1.100
```

---

## 📚 MÁS INFORMACIÓN

### Documentación Oficial
```bash
# Ver manual completo
man nmap

# Ver opciones de scripts
nmap --script-help

# Ver versión
nmap --version
```

### Recursos en Línea
- **Sitio oficial**: https://nmap.org
- **Manual en línea**: https://nmap.org/book/
- **NSE Scripts**: https://nmap.org/nsedoc/

### Libros y Tutoriales
- "Zen of Nmap" - Página oficial
- "Mastering Nmap" - Libros.io
- "TCPDump and WireShark" - Análisis de red

---

## 🆘 DEBUGGING

### Comando no funciona

```bash
# Verificar sintaxis
nmap -h <opción>

# Ejecutar en modo verbose
nmap -vv 192.168.1.100

# Ver información detallada
nmap --reason 192.168.1.100
```

### Verificar instalación

```bash
# ¿Está Nmap instalado?
which nmap

# ¿Qué versión?
nmap --version

# ¿Puede acceder a la red?
ping 192.168.1.100
```

---

**Última actualización: 2026**

*Esta referencia incluye Nmap 7.x y posteriores*
