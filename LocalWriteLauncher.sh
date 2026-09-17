#!/bin/bash
# LocalWrite Launcher
# Activates the virtual environment and runs LocalWrite

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="/Users/amre/Projects/LocalWrite"

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Set Qt platform to offscreen if no display
if [ -z "$DISPLAY" ]; then
    export QT_QPA_PLATFORM=offscreen
fi

# Run LocalWrite
cd "$PROJECT_DIR"
exec python main.py
