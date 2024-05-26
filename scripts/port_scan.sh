#!/bin/bash

# Verifica si se ha proporcionado una IP y un rango de puertos
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: $0 <IP> <rango de puertos>"
    echo "Ejemplo: $0 192.168.1.1 1-1024"
    exit 1
fi

# IP y rango de puertos especificados
ip=$1
port_range=$2

# Extrae los puertos de inicio y fin del rango
start_port=$(echo $port_range | cut -d '-' -f 1)
end_port=$(echo $port_range | cut -d '-' -f 2)

# Verifica que los puertos sean números válidos
if ! [[ "$start_port" =~ ^[0-9]+$ ]] || ! [[ "$end_port" =~ ^[0-9]+$ ]]; then
    echo "Rango de puertos no válido. Debe ser en el formato inicio-fin (ejemplo: 1-1024)."
    exit 1
fi

# Realiza el escaneo de puertos
echo "Escaneando puertos del $start_port al $end_port en $ip..."

for port in $(seq $start_port $end_port); do
    nc -zv -w 1 $ip $port &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Puerto $port está abierto"
    fi
done

echo "Escaneo completo."
