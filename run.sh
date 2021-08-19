#!/bin/bash

python3 --version &>/dev/null
if [ $? -eq 0 ]; then
    python3 src/main.py
else
    echo "Error: python3 no esta instalado"
fi