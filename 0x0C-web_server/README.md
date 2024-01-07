# ALX System Engineering & DevOps - Web Server Project

## Overview

In this project, I explored the fundamentals of web servers, file transfers, and configuration using Nginx. I had the opportunity to work with server setup, file transfer tools like `scp`, and Nginx configuration to serve web content. Additionally, I used Fabric to automate deployment tasks.

## Web Server Configuration

### 0. Transfer a file to your server

- [0-transfer_file](./0-transfer_file)
  - Bash script to transfer a file from a client to a server.
  - Accepts file path, server IP, username, and SSH key path as arguments.
  - Uses `scp` to transfer the file to the user's home directory on the server.

### 1. Install nginx web server

- [1-install_nginx_web_server](./1-install_nginx_web_server)
  - Bash script to configure a new Ubuntu machine with Nginx.
  - Nginx listens on port 80.
  - Returns "Hello World!" when querying Nginx at `/`.

### 2. Setup a domain name

- [2-setup_a_domain_name](./2-setup_a_domain_name)
  - Text file containing the domain name set up for the server through Gandi.

### 3. Redirection

- [3-redirection](./3-redirection)
  - Bash script to configure Nginx on Ubuntu with a redirection.
  - Similar to [1-install_nginx_web_server] with an additional redirection for `/redirect_me`.

### 4. Not found page 404

- [4-not_found_page_404](./4-not_found_page_404)
  - Bash script to configure Nginx on Ubuntu with a custom 404 page.
  - Similar to [1-install_nginx_web_server] with a custom 404 page.

