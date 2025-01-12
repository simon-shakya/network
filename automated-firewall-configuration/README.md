# Automated Firewall Configuration Script

This repository contains a **Bash script** to automate the configuration of firewalls on Linux-based servers using `iptables`. The script sets up rules for **NAT**, **packet filtering**, and **security zones**, making it easier to deploy consistent firewall configurations across multiple environments.

## Features

- Automates the configuration of `iptables` firewall rules.
- Configures NAT (Network Address Translation) for outgoing traffic.
- Sets up basic security zones (e.g., allows SSH, HTTP, and HTTPS traffic).
- Configures packet filtering to secure the server.
- Saves the configuration for persistence across reboots.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/simon-shakya/network.git
   cd network/automated-firewall-configuration
   ```


2. **Make the script executable:**

   ```bash
   chmod +x firewall_setup.sh
   ```
3. **Run the script with sudo:**

```bash
sudo ./firewall_setup.sh
```
  This will apply the firewall rules and save the configuration.


## How It Works 

**Firewall Rules Setup:**

Configures default policies for incoming and outgoing traffic.
Allows incoming SSH, HTTP, and HTTPS traffic.
Sets up NAT (Masquerading) for outgoing traffic.
Configures basic forwarding rules between the internal and external network interfaces.

**Security Zones:**

The script sets up basic zones by controlling which ports are open (SSH, HTTP, HTTPS).

**Persistence:**

The script saves the iptables configuration to ensure rules persist after reboot (specific to Debian-based systems).
Version Control and Collaboration
This repository uses GitHub for version control and collaboration.
Team members can fork the repository, make improvements or fixes, and create pull requests for review.
Each environment (test, staging, production) can have different versions or configurations managed through Git branches.

## Contributing
If you'd like to contribute to this project:

Fork the repository.
Create a new branch for your feature or bug fix.
Write your code and add tests if necessary.
Submit a pull request with a description of your changes.
