# PLEASE USE THIS FOR ETHICAL PURPOSES ONLY!
# Unauthorized port scanning may violate applicable laws, policies and terms of service. Use this tool responsibly.

The IP address is where the tool is pointed at and it is pretty much the equivalent of walking up to someone's house and testing the doors and windows to see whether they are locked or not.

It is maybe not breaking in but it is the first step that malicious actors take.

# Only scan systems you own or have explicit permission to test.

# Port-Scanner-Python-Open-Source
A Open Source Port Scanner written in Python that scans mainly for the ports 1337, 4444 and 8080 but also shows other open ports.

The IP Address 127.0.0.1 stands for "This PC" / "My PC" so you can just start scanning your PC without having to change the IP and see whether port 1337, 4444 and/or 8080 have a connection with your PC and see if there are any other ports open.

A text editor like Visual Studio Code is needed to run this port scanner.

# What each Ports mean:
4444: This is the default port for Metasploit listeners. Metasploit is a penetration testing framework that security professionals use but also attackers use. That is why the port gets flagged.

1337: This is a “leet” (hacker slang) port and its a classic choice for backdoors. It is associated with malware and exploit tooling however there is nothing technical that makes it special and any different from the other ports.

8080: This is mostly legitimate. It is an alternate web server and proxy port used by dev servers, proxies and admin panels, However it can be abused which is why it is worth a cautious flag rather than a hard warning like the other two.
