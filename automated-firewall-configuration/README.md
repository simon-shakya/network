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
