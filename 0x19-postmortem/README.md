# Apache 500 Internal Server Error Outage Postmortem

![Image](https://miro.medium.com/v2/resize:fit:800/0*DIk0-l87rZSrrqsv.jpg)

## Issue Summary
**Duration:** The outage started at 10:00 AM UTC and was resolved at 12:00 PM UTC on April 15, 2024.  
**Impact:** The Apache web server was returning a 500 Internal Server Error, causing the website and all associated services to be unavailable. This affected approximately 80% of our user base.  
**Root Cause:** A missing directory `/var/www/html/wp-content/uploads` required by WordPress for uploading media files.

## Timeline
- **10:00 AM:** Monitoring alerts indicated that Apache was returning 500 errors.
- **10:15 AM:** An engineer confirmed the issue by running `curl -sI 127.0.0.1` and observing the 500 error.
- **10:30 AM:** The engineer used `strace` to attach to the Apache process and investigate the issue.
- **11:00 AM:** After analyzing the `strace` output, the engineer identified a missing directory causing the issue.
- **11:15 AM:** The issue was escalated to the web team for further investigation.
- **11:45 AM:** The web team confirmed the missing directory and proposed creating it with the correct permissions.
- **12:00 PM:** The issue was resolved by creating the missing directory and restarting Apache.

## Root Cause and Resolution

![LinkedIn Image](https://media.licdn.com/dms/image/D5622AQFEBEo5g1RqFQ/feedshare-shrink_800/0/1681321049543?e=2147483647&v=beta&t=dvNc4gu9B-vUhwpFgk_Euz2ZLvWmszvyGvUEWUtpv40)


The root cause of the issue was a missing directory `/var/www/html/wp-content/uploads` required by WordPress for uploading media files. Without this directory, Apache could not serve requests properly, resulting in a 500 Internal Server Error.

The issue was fixed by creating the missing directory with the correct ownership and permissions, and then restarting the Apache service to ensure the changes took effect.

## Corrective and Preventative Measures
1. Improve documentation and checklists for WordPress installation and configuration to prevent missing critical directories.
2. Implement monitoring for critical directories and file permissions to detect issues proactively.
3. Automate the creation of required directories during WordPress installation or server provisioning using configuration management tools like Puppet or Ansible.
4. Conduct regular audits and testing of the WordPress installation and Apache configuration to identify potential issues.
5. Improve communication and escalation processes within the team to ensure issues are addressed promptly.

## Tasks
- Document the WordPress installation and configuration process, including a checklist for required directories and permissions.
- Implement monitoring for critical directories and file permissions, with alerts for missing or incorrect configurations.
- Create a Puppet manifest or Ansible playbook to automate the creation of the `/var/www/html/wp-content/uploads` directory during server provisioning or WordPress installation.
- Schedule regular audits and testing of the WordPress installation and Apache configuration to identify potential issues.
- Review and update the team's communication and escalation processes to improve incident response.

By implementing these corrective and preventative measures, we can minimize the risk of similar outages in the future and ensure a more reliable and robust web infrastructure.

