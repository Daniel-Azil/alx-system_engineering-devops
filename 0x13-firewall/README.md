# Firewall

## 0-block_all_incoming_traffic_but
The provided commands use Uncomplicated Firewall (UFW) to allow incoming traffic on ports 22 (SSH), 443 (HTTPS), and 80 (HTTP), ensuring secure remote connections and enabling web traffic on the specified ports.

## 100-port_forwarding
Configured ufw on web-01 to redirect inbound TCP traffic from port 8080 to port 80 where the nginx web server is listening by adding a prerouting rule to /etc/ufw/before.rules and reloading ufw.