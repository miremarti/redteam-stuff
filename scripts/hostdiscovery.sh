#!/bin/bash

# Verifica si se ha proporcionado una subred
if [ -z "$1" ]; then
    echo "Uso: $0 <subred>"
    echo "Ejemplo: $0 192.168.1"
    exit 1
fi

# Subred especificada (por ejemplo, 192.168.1)
subred=$1

# Rango de IPs (de 1 a 254)
for ip in $(seq 1 254); do
    # Direccion IP completa
    direccion="$subred.$ip"
    
    # Realiza el ping y verifica si hay respuesta
    ping -c 1 -W 1 $direccion &> /dev/null
    
    if [ $? -eq 0 ]; then
        echo "Host $direccion está activo"
    fi
done
