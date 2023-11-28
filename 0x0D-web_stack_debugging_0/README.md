# Project: 0x0D-web_stack_debugging_0
##Give Me a Page!
Welcome to the first debugging project in the web stack specialization. In this project, the goal is to get Apache to run on the Docker container and return a page containing "Hello Holberton" when querying the root.

###Task Description:
- Start the Docker container with the provided command:
```
docker run -p 8080:80 -d -it holbertonschool/265-047ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021

```
- Check the status of the Docker container:
```
docker ps
```
- Use curl to query the container on port 8080:
```
curl 0:8080

```
#### Observe any error messages and debug the container to ensure it returns the expected page.

##### Example:
After starting the Docker container, the initial curl command might return an error message or an empty reply from the server. Your mission is to fix the issue and make the following curl command return a page containing "Hello Holberton":
```
curl 0:8080
```

##### Solution:
Connect to the container and fix any issues preventing Apache from serving the expected page. After fixing the issue, the curl command should return "Hello Holberton."

Include the command(s) you used to fix the issue in your answer file (0-give_me_a_page). Your solution should demonstrate the debugging steps taken to achieve the desired outcome.

##### Repository:
- GitHub repository: alx-system_engineering-devops

- Directory: 0x0D-web_stack_debugging_0
