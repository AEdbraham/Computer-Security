import nmap

def scan_network(hosts, ports, arguments, sudo):
    nm = nmap.PortScanner()
    scan_args = f'-p {ports} {arguments}'
    if sudo:
        nm.scan(hosts, arguments=scan_args, sudo=True)
    else:
        nm.scan(hosts, arguments=scan_args)
    
    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print("State : %s" % nm[host].state())
        for proto in nm[host].all_protocols():
            print("Protocolo : %s" % proto)
    
            ports = nm[host][proto].keys()
            for port in ports:
                print("Puerto : %s\tState : %s" % (port, nm[host][proto][port]['state']))

def main():
    hosts = input("Ingresar host: ")
    ports = input("Ingresar puestos: ")
    arguments = input("Argumentos adicionales (opcional): ")
    sudo_input = input("Ejecutar como super user? (y/n): ")
    sudo = True if sudo_input.lower() == 'y' else False

    scan_network(hosts, ports, arguments, sudo)

if __name__ == "__main__":
    main()
