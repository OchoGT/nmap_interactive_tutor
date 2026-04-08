#!/bin/bash

# ═══════════════════════════════════════════════════════════════
# SCRIPT DE INSTALACIÓN - NMAP INTERACTIVE TUTOR
# ═══════════════════════════════════════════════════════════════

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║      INSTALADOR - NMAP INTERACTIVE TUTOR                     ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Detectar distro Linux
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
else
    echo "❌ No se puede detectar el SO Linux"
    exit 1
fi

echo "📋 Sistema detectado: $OS $VER"
echo ""

# ═══════════════════════════════════════════════════════════════
# PASO 1: VERIFICAR PYTHON 3
# ═══════════════════════════════════════════════════════════════

echo "📦 PASO 1: Verificando Python 3..."

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    echo "✓ Python 3 encontrado: $PYTHON_VERSION"
else
    echo "❌ Python 3 no está instalado."
    echo "📥 Instalando Python 3..."
    
    if [[ "$OS" == *"Ubuntu"* ]] || [[ "$OS" == *"Debian"* ]]; then
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [[ "$OS" == *"Fedora"* ]] || [[ "$OS" == *"CentOS"* ]] || [[ "$OS" == *"RHEL"* ]]; then
        sudo dnf install -y python3 python3-pip
    elif [[ "$OS" == *"Arch"* ]]; then
        sudo pacman -S --noconfirm python
    else
        echo "⚠️  No se pudo instalar automáticamente. Instálalo manualmente."
        exit 1
    fi
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# PASO 2: VERIFICAR NMAP
# ═══════════════════════════════════════════════════════════════

echo "📦 PASO 2: Verificando Nmap..."

if command -v nmap &> /dev/null; then
    NMAP_VERSION=$(nmap --version | head -n1)
    echo "✓ Nmap encontrado: $NMAP_VERSION"
else
    echo "❌ Nmap no está instalado."
    echo "📥 Instalando Nmap..."
    
    if [[ "$OS" == *"Ubuntu"* ]] || [[ "$OS" == *"Debian"* ]]; then
        sudo apt update
        sudo apt install -y nmap
    elif [[ "$OS" == *"Fedora"* ]] || [[ "$OS" == *"CentOS"* ]] || [[ "$OS" == *"RHEL"* ]]; then
        sudo dnf install -y nmap
    elif [[ "$OS" == *"Arch"* ]]; then
        sudo pacman -S --noconfirm nmap
    else
        echo "⚠️  No se pudo instalar automáticamente."
        echo "   Instálalo manualmente: https://nmap.org/download.html"
        exit 1
    fi
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# PASO 3: INSTALAR DEPENDENCIAS DE PYTHON
# ═══════════════════════════════════════════════════════════════

echo "📦 PASO 3: Instalando dependencias de Python..."

if [ -f "requirements.txt" ]; then
    echo "📥 Instalando desde requirements.txt..."
    pip3 install -r requirements.txt
else
    echo "📥 Instalando colorama..."
    pip3 install colorama
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# PASO 4: CONFIGURAR PERMISOS
# ═══════════════════════════════════════════════════════════════

echo "📦 PASO 4: Configurando permisos..."

if [ -f "nmap_interactive_tutor.py" ]; then
    chmod +x nmap_interactive_tutor.py
    echo "✓ Permisos configurados"
else
    echo "⚠️  No se encontró nmap_interactive_tutor.py"
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# PASO 5: VERIFICACIÓN FINAL
# ═══════════════════════════════════════════════════════════════

echo "✅ VERIFICACIÓN FINAL"
echo "─────────────────────────────────────────────────────────"

echo ""
echo "📋 Estado del sistema:"
echo ""

python3_check=$(python3 --version)
echo "  ✓ Python 3:  $python3_check"

nmap_check=$(nmap --version | head -n1)
echo "  ✓ Nmap:      $nmap_check"

colorama_check=$(python3 -c "import colorama; print('v' + colorama.__version__)" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "  ✓ Colorama:  $colorama_check"
else
    echo "  ⚠️  Colorama: No instalado (opcional)"
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# FINALIZACIÓN
# ═══════════════════════════════════════════════════════════════

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║           ✅ INSTALACIÓN COMPLETADA                          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"

echo ""
echo "🚀 PARA EJECUTAR EL PROGRAMA:"
echo ""
echo "   Opción 1: Desde este directorio"
echo "   $ python3 nmap_interactive_tutor.py"
echo ""
echo "   Opción 2: Con permisos de ejecución"
echo "   $ ./nmap_interactive_tutor.py"
echo ""
echo "   Opción 3: Con sudo (para algunos escaneos)"
echo "   $ sudo python3 nmap_interactive_tutor.py"
echo ""
echo "📖 Lee README.md para más información"
echo ""
echo "📚 PRIMERA VEZ?"
echo "   1. Ejecuta el programa"
echo "   2. Elige 'Modo Aprendizaje Guiado'"
echo "   3. Selecciona 'Nivel 1: Básico'"
echo "   4. ¡Sigue las instrucciones!"
echo ""
