import subprocess
import sys

def ping_host(ip):
    """Realiza un ping a la dirección IP especificada."""
    try:
        output = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return output.returncode == 0
    except Exception as e:
        print(f"Error al hacer ping a {ip}: {e}")
        return False

def main(subnet):
    """Realiza un barrido de ping en la subred especificada."""
    print(f"Barrido de ping en la subred: {subnet}.0/24")
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        if ping_host(ip):
            print(f"Host {ip} está activo")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 barrido_ping.py <subred>")
        print("Ejemplo: python3 barrido_ping.py 192.168.1")
        sys.exit(1)

    subnet = sys.argv[1]
    main(subnet)
