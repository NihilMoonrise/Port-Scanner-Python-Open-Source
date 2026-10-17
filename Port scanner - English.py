#Open source Python port scanner written fully by Nihil
#MIT LICENSED
#"THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND... IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY..."

#A simple port scanner that scans for the ports 1337, 4444 and 8080
#port 1337 and 4444 are usually used by malware

#Unauthorized port scanning may violate applicable laws, policies and terms of service. Use this tool responsibly.
#The IP address is where the tool is pointed at and it is pretty much the equivalent of walking up to someone's house and testing the doors and windows to see whether they are locked or not.
#It is maybe not breaking in but it is the first step that malicious actors take.

#Only scan systems you own or have explicit permission to test.

import socket

def scan_port(host, port):
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(0.5) #Timeout so the script doesnt get stuck
    c = a.connect_ex((host, port)) #Instead of connect i used connect_ex so the number 0 would appear instead of crashing, try/except is no longer needed thanks to connect_ex
    a.close()
    if c == 0:
        return True
    else:
        return False

targeted_ports_scan = [1337, 4444, 8080]

flagged_ports = {
    1337: "Suspicious port",
    4444: "A suspicious port",
    8080: "Possible suspicious port but also usually used by servers"
}

open_ports = []

#Scanning
for port in targeted_ports_scan:
    result = scan_port("127.0.0.1", port) #The IP address 127.0.0.1 literally means "This PC" / "My PC"
    #print(port, result) Used as a test and no longer needed
    if result:
        open_ports.append(port)
#print(open_ports) Used as a test and no longer needed

#Report
if not open_ports:
    print("No open ports found")
else:
    for port in open_ports:
        if port in flagged_ports:
            print(f"[!] Port {port} open - {flagged_ports[port]}") #If port 1337, 4444 and/or 8080 have a connection with your PC
        else:
            print(f"Port {port} open") #Ports that are not flagged but are open