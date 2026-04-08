# ❓ PREGUNTAS FRECUENTES (FAQ)

---

## 📦 INSTALACIÓN Y REQUISITOS

### P: ¿En qué sistemas funciona?
**R:** Este programa está diseñado para **Linux**:
- Ubuntu 18.04+
- Debian 9+
- Fedora 30+
- CentOS 7+
- Arch Linux
- Cualquier distribución Linux

Para Windows, usa **WSL (Windows Subsystem for Linux)**.

---

### P: ¿Necesito Windows/macOS?
**R:** No. Este programa es para Linux.

**Alternativas:**
- **Windows**: Instala WSL 2 y Ubuntu
- **macOS**: Instala con Homebrew (`brew install nmap`)

---

### P: ¿Qué versión de Python necesito?
**R:** **Python 3.7 o superior**.

Verifica con:
```bash
python3 --version
```

Si tienes Python 2, no será suficiente.

---

### P: ¿Es obligatorio instalar colorama?
**R:** **No**, es opcional. El programa funciona sin colores, pero se ve mejor con colorama.

Sin colorama: Salida en blanco/gris
Con colorama: Salida colorida (mejor legibilidad)

---

### P: El script install.sh no funciona
**R:** Intenta los siguientes pasos:

```bash
# 1. Verifica que sea ejecutable
chmod +x install.sh

# 2. Ejecuta con bash explícitamente
bash install.sh

# 3. Si aún no funciona, instalación manual:
sudo apt update
sudo apt install python3 python3-pip nmap
pip3 install colorama
```

---

### P: ¿Qué pasa si no tengo Nmap instalado?
**R:** El programa detectará que Nmap no está y te lo dirá. Puedes:

1. Usar la instalación automática: `./install.sh`
2. Instalar manualmente:
   ```bash
   sudo apt install nmap
   ```
3. El programa seguirá funcionando, pero solo podrás usar el modo construcción de comandos (no ejecución)

---

## 🚀 USO BÁSICO

### P: ¿Por dónde empiezo?
**R:** Sigue estos pasos:

1. Ejecuta: `python3 nmap_interactive_tutor.py`
2. Lee la bienvenida (importante)
3. Acepta las advertencias
4. En el menú, elige **[1] Modo Aprendizaje Guiado**
5. Selecciona **Nivel 1: Básico**
6. ¡Sigue las instrucciones!

---

### P: ¿Cuánto tiempo tarda en aprender Nmap?
**R:** Depende de tu experiencia:

| Experiencia | Tiempo |
|-------------|--------|
| Principiante total | 2-4 horas |
| Con conocimientos de redes | 1-2 horas |
| Pentester experimentado | 30-60 minutos |

Cada nivel tarda aproximadamente:
- Nivel 1: 20 min
- Nivel 2: 30 min
- Nivel 3: 40 min
- Nivel 4: 15 min
**Total: ~105 minutos**

---

### P: ¿Tengo que completar todos los niveles?
**R:** **No es obligatorio**, pero recomendado:

- **Mínimo**: Nivel 1 (conceptos básicos)
- **Recomendado**: Nivel 1 + 2 (uso práctico)
- **Completo**: Todos los niveles

Puedes volver atrás en cualquier momento.

---

### P: ¿Qué pasa si cometo un error?
**R:** **No hay problema.** El programa:

- Valida entradas (rechaza entradas inválidas)
- Permite editar el comando antes de ejecutar
- No te dejaría ejecutar comandos malos
- Muestra por qué un comando no es válido

---

## 🛡️ SEGURIDAD Y LEGALIDAD

### P: ¿Es legal usar Nmap?
**R:** **Depende**:

✅ **LEGAL:**
- Escanear tu propio hardware
- Escanear máquinas virtuales propias
- Con permiso explícito del propietario
- Pentesting contratado
- Labs de educación autorizados

❌ **ILEGAL:**
- Escanear sin autorización
- Acceso no autorizado a sistemas
- Violar leyes de ciberseguridad

**CONSECUENCIAS de uso ilegal:**
- Multas (a menudo miles de euros/dólares)
- Cargos criminales
- Prisión (en casos graves)

---

### P: ¿Cómo obtengo autorización?
**R:** Depende del caso:

**Para tu propia red:**
- Solo necesitas permiso de ti mismo
- Asegúrate de que sea realmente tuya

**Para redes de clientes:**
- Obtén **consentimiento escrito**
- Especifica alcance exacto
- Documenta todo
- Usa NDA (Non-Disclosure Agreement)

**Para aprendizaje:**
- Usa máquinas virtuales
- Usa plataformas de práctica (TryHackMe, HackTheBox)
- Pide permiso a profesores

---

### P: ¿Qué debo hacer si encuentro una vulnerabilidad?
**R:** Responsablemente:

1. **NO la publiques públicamente**
2. **NO accedas a datos**
3. **Documenta la vulnerabilidad**
4. Contacta al propietario en privado
5. Dale tiempo para que la corrijan
6. Solo luego publica responsablemente

---

## 🎯 EJECUCIÓN

### P: ¿Por qué algunos escaneos piden sudo?
**R:** Ciertos escaneos necesitan permisos de root:

✅ Sin root:
- `nmap -sT` (TCP Connect)
- Detección de servicios básica
- Escaneos lentos

❌ Necesitan root (sudo):
- `nmap -sS` (TCP SYN - crea sockets raw)
- `nmap -O` (Detección de SO)
- Algunos scripts

**Solución:**
```bash
sudo python3 nmap_interactive_tutor.py
```

**O ejecuta comando specific:**
```bash
sudo nmap -sS 192.168.1.100
```

---

### P: ¿Puedo escanear desde Windows?
**R:** Sí, usando **WSL (Windows Subsystem for Linux)**:

1. Abre PowerShell como administrador
2. Instala WSL 2:
   ```powershell
   wsl --install
   ```
3. Abre Ubuntu desde la Microsoft Store
4. Dentro de Ubuntu, instala Nmap:
   ```bash
   sudo apt install nmap python3-pip
   ```
5. Instala el programa y úsalo normalmente

---

### P: La ejecución es muy lenta
**R:** Intenta estos ajustes:

```bash
# Aumenta el timing
nmap -T5 192.168.1.100

# Escanea menos puertos
nmap -F 192.168.1.100

# Solo puertos específicos
nmap -p 80,443 192.168.1.100

# Reduce el número de scripts
nmap --script default 192.168.1.100
```

---

### P: ¿Cómo ejecuto en segundo plano?
**R:** Usa `&` o `screen`:

```bash
# En segundo plano
nmap -oA reporte 192.168.1.100 &

# Con screen (mejor)
screen -S nmap
nmap -oA reporte 192.168.1.100
# Presiona Ctrl+A, luego D para desconectar
# Para reconectar: screen -r nmap
```

---

## 🔧 TROUBLESHOOTING

### P: "Nmap: command not found"
**R:** Nmap no está instalado.

```bash
# Verificar
which nmap

# Instalar
sudo apt install nmap

# Verificar instalación
nmap --version
```

---

### P: "Permission denied" al ejecutar script
**R:** Dale permisos ejecutables:

```bash
chmod +x nmap_interactive_tutor.py
chmod +x install.sh

# Luego ejecuta
python3 nmap_interactive_tutor.py
```

---

### P: Error de conexión a localhost
**R:** Localhost (127.0.0.1) debería funcionar siempre.

Si no funciona:
```bash
# Verifica que tu máquina esté activa
ping localhost

# Intenta otro objetivo
nmap 127.0.0.1

# Con más verbosidad
nmap -v localhost
```

---

### P: "Colorama no encontrado"
**R:** Instálalo:

```bash
pip3 install colorama

# O con sudo
sudo pip3 install colorama

# O de requirements.txt
pip3 install -r requirements.txt
```

---

### P: El programa se cuelga/congela
**R:** Presiona **CTRL+C** para cancelar.

Si sigue:
1. Abre otra terminal
2. Mata el proceso:
   ```bash
   pkill -f nmap_interactive_tutor
   pkill -f nmap
   ```

---

### P: "Invalid IP" aunque la IP es correcta
**R:** El programa valida IPs simple.

IPs válidas:
- ✅ 192.168.1.100 (correcta)
- ✅ 10.0.0.1 (correcta)
- ✅ 127.0.0.1 (localhost, correcta)
- ✅ example.com (dominio, correcto)

IPs inválidas:
- ❌ 999.999.999.999 (números fuera de rango)
- ❌ 192.168.1 (falta octeto)
- ❌ 192.168.1.100.200 (demasiados octetos)

---

## 📊 RESULTADOS Y ANÁLISIS

### P: ¿Qué significan los estados de puerto?
**R:** Los estados comunes son:

| Estado | Significado | Ejemplo |
|--------|------------|---------|
| **open** | Puerto abierto, servicio escuchando | 80 (HTTP) |
| **closed** | Puerto cerrado, rechaza conexiones | 1234 |
| **filtered** | Puerto bloqueado por firewall | Inaccesible |
| **unfiltered** | Puerto accesible pero desconocido | Raro |
| **open\|filtered** | No se puede determinar | Ambiguo |

---

### P: ¿Cómo interpretto los resultados?
**R:** Un resultado típico:

```
22/tcp   open     ssh     OpenSSH 7.4
80/tcp   open     http    Apache httpd 2.4.6
443/tcp  open     https   nginx
3306/tcp closed   mysql   
```

**Interpretación:**
- Port 22: SSH abierto (acceso remoto)
- Port 80: HTTP abierto (web)
- Port 443: HTTPS abierto (web seguro)
- Port 3306: MySQL cerrado (no accesible)

---

### P: Cómo guardo los resultados?
**R:** El programa ofrece varias opciones:

1. **En el programa:**
   - Elige "Guardar en archivo"
   - Se guarda en `~/.nmap_tutor_comandos/`

2. **Con Nmap:**
   - `-oN archivo.txt` (texto normal)
   - `-oX archivo.xml` (XML)
   - `-oG archivo.gnmap` (grepable)
   - `-oA archivo` (todos los formatos)

3. **Manualmente:**
   ```bash
   nmap 192.168.1.100 > resultado.txt
   ```

---

### P: ¿Cómo analizo múltiples resultados?
**R:** Usa herramientas Unix:

```bash
# Comparar dos escaneos
diff reporte1.txt reporte2.txt

# Buscar puertos abiertos
grep "open" reporte.txt

# Contar puertos
grep "open" reporte.txt | wc -l

# Extraer información
awk '{print $1, $2}' reporte.gnmap
```

---

## 💡 CONSEJOS AVANZADOS

### P: ¿Cómo automatizo escaneos?
**R:** Crea scripts bash:

```bash
#!/bin/bash

# Escanear lista de hosts
for host in 192.168.1.100 192.168.1.101 192.168.1.102; do
    echo "Escaneando $host..."
    nmap -oA reporte_$host $host
done
```

---

### P: ¿Cómo integro con otras herramientas?
**R:** Usa XML output:

```bash
# Exporta a XML
nmap -oX resultado.xml 192.168.1.100

# Luego procesa con Python
python3 procesar_xml.py resultado.xml
```

---

### P: ¿Cuál es la mejor práctica?
**R:** Sigue este flujo:

1. **Reconocimiento inicial**: `nmap -sn` (ping sweep)
2. **Escaneo rápido**: `nmap -F` (puertos comunes)
3. **Escaneo completo**: `nmap -p-` (todos los puertos)
4. **Detección**: `nmap -sV -O` (versiones y SO)
5. **Análisis**: `nmap --script` (vulnerabilidades)
6. **Documentación**: `-oA` (guardar resultados)

---

## 🎓 APRENDIZAJE ADICIONAL

### P: ¿Dónde puedo practicar?
**R:** Plataformas de práctica:

- **TryHackMe**: Cursos interactivos
- **HackTheBox**: CTFs y máquinas
- **VulnHub**: Máquinas virtuales
- **OverTheWire**: Wargames
- **PicoCTF**: CTFs educativos

---

### P: ¿Cómo avanzo a Penetration Testing real?
**R:** Pasos sugeridos:

1. Domina Nmap (este programa)
2. Aprende otros análisis: `nessus`, `burp`
3. Obtén certificación: CEH, OSCP
4. Practica en CTFs
5. Comienza pequeños trabajos de pentesting
6. Aumenta gradualmente

---

### P: ¿Se puede vivir de Penetration Testing?
**R:** **Sí**, es una carrera real:

**Salarios típicos:**
- Junior: $50k - $80k
- Mid-level: $80k - $120k
- Senior: $120k - $200k+

**Requisitos:**
- Sólidos conocimientos técnicos
- Certificaciones (CEH, OSCP)
- Experiencia real
- Ética profesional

---

## ❌ ERRORES COMUNES

### Errror 1: Olvidar sudo
```bash
# ❌ Incorrecto (fallará si usas -sS)
nmap -sS 192.168.1.100

# ✅ Correcto
sudo nmap -sS 192.168.1.100
```

---

### Error 2: IP inválida
```bash
# ❌ Incorrecto
nmap 999.999.999.999

# ✅ Correcto
nmap 192.168.1.100
```

---

### Error 3: Escanear sin autorización
```bash
# ❌ ILEGAL
nmap 8.8.8.8  # Google DNS (sin permiso)

# ✅ LEGAL
nmap 192.168.1.100  # Tu red
```

---

### Error 4: No guardar resultados
```bash
# ❌ Pierde información
nmap 192.168.1.100

# ✅ Guarda para referencia
nmap -oA reporte 192.168.1.100
```

---

## 📞 SOPORTE

### ¿Tengo otros problemas?

1. **Revisa README.md** - Documentación completa
2. **Revisa QUICK_START.md** - Instalación rápida
3. **Lee COMANDOS_REFERENCIA.md** - Comandos
4. **Ejecuta el programa** - Sistema de ayuda integrado
5. **Busca online** - r/netsec, GitHub Issues

---

## 📝 FEEDBACK

¿Encontraste un error? ¿Tienes sugerencias?

- Documenta el problema
- Describe los pasos para reproducirlo
- Sugiere una solución
- ¡Contribuye a mejorar!

---

**Última actualización: 2026**

*Preguntas más frecuentes sobre el Tutor de Nmap*
