import socket
import sys

def scan_ports(ip, start_port, end_port):
    """Escanea los puertos en el rango especificado en la IP dada."""
    print(f"Escaneando puertos del {start_port} al {end_port} en {ip}...")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Establece un tiempo de espera de 1 segundo
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Puerto {port} está abierto")
        
        sock.close()
    
    print("Escaneo completo.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 port_scan.py <IP> <rango de puertos>")
        print("Ejemplo: python3 port_scan.py 192.168.1.1 1-1024")
        sys.exit(1)
    
    ip = sys.argv[1]
    port_range = sys.argv[2]
    
    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        print("Rango de puertos no válido. Debe ser en el formato inicio-fin (ejemplo: 1-1024).")
        sys.exit(1)
    
    scan_ports(ip, start_port, end_port)
