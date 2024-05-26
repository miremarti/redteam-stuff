# -*- coding: utf-8 -*-
import subprocess
import sys

def ping_host(ip):
    """Realiza un ping a la dirección IP especificada."""
    try:
        output = subprocess.Popen(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, err = output.communicate()
        return output.returncode == 0
    except Exception, e:
        print "Error al hacer ping a " + ip + ": " + str(e)
        return False

def main(subnet):
    """Realiza un barrido de ping en la subred especificada."""
    print "Barrido de ping en la subred: " + subnet + ".0/24"
    for i in range(1, 255):
        ip = subnet + "." + str(i)
        if ping_host(ip):
            print "Host " + ip + " está activo"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Uso: python barrido_ping.py <subred>"
        print "Ejemplo: python barrido_ping.py 192.168.1"
        sys.exit(1)

    subnet = sys.argv[1]
    main(subnet)
