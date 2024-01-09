# Load Balancer Project

## 0-custom_http_response_header
This script configures web-02 to mirror the settings of web-01 and introduces a custom HTTP header named X-Served-By, populated with the hostname of the Nginx server.

* Purpose:
- Install Nginx on web-02.
- Create necessary directories and set permissions.
- Set up a basic Nginx configuration.
- Add a custom HTTP header.
- Configure a redirect if the path contains "redirect_me."
- Create a custom error page.
- Restart Nginx.


## 1-install_load_balancer
This script installs and configures HAProxy as a load balancer.

* Purpose:
- Install HAProxy.
- Modify HAProxy configuration to define a frontend and backend.
- Specify servers to balance requests between.
- Configure HAProxy to start on boot.
- Restart HAProxy.


## 2-puppet_custom_http_response_header.pp
This Puppet manifest accomplishes the same configuration as the first script using Puppet for configuration management.

* Purpose:
- Update packages.
- Ensure Nginx is installed.
- Create or update the index.html file.
- Set up a 301 redirection in the Nginx configuration.
- Add a custom X-Served-By header to the Nginx configuration.
- Restart Nginx.
