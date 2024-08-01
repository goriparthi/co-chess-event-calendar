#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the path to the virtual environment and the script
VENV_DIR="./venv"
SCRIPT="script.py"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
  echo "Error: Virtual environment directory '$VENV_DIR' not found."
  exit 1
fi

# Check if the script exists
if [ ! -f "$SCRIPT" ]; then
  echo "Error: Script '$SCRIPT' not found."
  exit 1
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Run the Python script
python "$SCRIPT"

# Deactivate the virtual environment
deactivate
