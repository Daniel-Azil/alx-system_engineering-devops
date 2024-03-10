# Holberton School Project
## 0x10. HTTPS SSL

### 0. World wide web
The domain zone was configured so that the subdomain `www` points to the load-balancer IP (lb-01). Other subdomains were added to make life easier, and a Bash script was created to display information about subdomains.

File: [0-world_wide_web](0-world_wide_web)

### 1. HAproxy SSL termination
"Terminating SSL on HAproxy" means that HAproxy is configured to handle encrypted traffic, unencrypt it, and pass it on to its destination.

A certificate was created using certbot, and HAproxy was configured to accept encrypted traffic for the subdomain `www`.

- HAproxy is listening on port TCP 443
- HAproxy is accepting SSL traffic
- HAproxy is serving encrypted traffic that will return the root (`/`) of the web server
- When querying the root of the domain name, the page returned contains "Holberton School"
- The HAproxy configuration is shared as an answer file (`/etc/haproxy/haproxy.cfg`)

File: [1-haproxy_ssl_termination](1-haproxy_ssl_termination)

### 2. No loophole in your website traffic
To enforce HTTPS traffic and prevent unencrypted traffic, HAproxy was configured to automatically redirect HTTP traffic to HTTPS.

- This is transparent to the user
- HAproxy returns a 301 status code
- HAproxy redirects HTTP traffic to HTTPS
- The HAproxy configuration is shared as an answer file (`/etc/haproxy/haproxy.cfg`)

File: [100-redirect_http_to_https](100-redirect_http_to_https)