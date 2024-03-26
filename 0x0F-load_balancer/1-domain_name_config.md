Domain name config for web server 1, web server 2 and load balancer server 

main domain name is the main web server web 1 server eg. azil.tech
subdomain name for load balancer with www. eg. www.azil.tech
subdomain name for web 1 server again. eg web-01.azil.tech
subdomain name for web 2 server eg web-02.azil.tech
subdomain name for load balancer again eg lb-01.azil.tech


The DNS records are set up as follows:

azil.tech: This is the main domain name, and it points to the IP address of the primary web server (web-01.azil.tech).
www.azil.tech: This is a subdomain that points to the IP address of the load balancer server (lb-01.azil.tech). This subdomain is typically used as the main entry point for website visitors, and their requests are directed to the load balancer.
web-01.azil.tech: This is a subdomain that points to the IP address of the primary web server. This server is likely the same server as the one pointed to by the main domain (azil.tech).
web-02.azil.tech: This is a subdomain that points to the IP address of the secondary web server.
lb-01.azil.tech: This is a subdomain that points to the IP address of the load balancer server. This server receives incoming traffic from the www.azil.tech subdomain and distributes the load across the primary (web-01.azil.tech) and secondary (web-02.azil.tech) web servers.
This setup follows a common pattern for configuring DNS records for a load-balanced and highly available web infrastructure:

The main domain (azil.tech) points directly to the primary web server (web-01.azil.tech), allowing direct access to that server if needed.
The www subdomain (www.azil.tech) points to the load balancer (lb-01.azil.tech), serving as the main entry point for website visitors and distributing traffic across the web servers.
Separate subdomains are created for the primary (web-01.azil.tech) and secondary (web-02.azil.tech) web servers, allowing direct access to these servers if needed (e.g., for maintenance, testing, or separating different parts of the application).
The load balancer subdomain (lb-01.azil.tech) is used to manage the load balancer server directly if needed.
This configuration provides flexibility, load balancing, high availability, and separation of concerns between the different components of the web infrastructure.
