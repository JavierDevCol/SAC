#!/bin/bash
# SAC - Sistema Agéntico COCHAS
# Comando global para Linux/Mac
#
# Este script se instala en ~/.local/bin/
# y debe estar en el PATH del usuario

PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

INSTALLER_PATH="$HOME/.local/share/SAC/repo/INSTALACION/instalar.py"

if [ -f "$INSTALLER_PATH" ]; then
    $PYTHON_CMD "$INSTALLER_PATH" "$@"
else
    echo "❌ Error: No se encontró el instalador de SAC"
    echo "   Ruta esperada: $INSTALLER_PATH"
    echo ""
    echo "   Para reinstalar SAC, ejecuta:"
    echo "   curl -fsSL https://raw.githubusercontent.com/JavierDevCol/SAC/main/INSTALACION/bootstrap/install.sh | bash"
    exit 1
fi
