#!/bin/bash

# Automated Firewall Configuration Script
# This script configures firewall settings using iptables on Linux servers.
# It configures NAT, packet filtering, and basic security zones.
# Simon Shakya

# Exit on any error
set -e

# Define default chains and policies
DEFAULT_POLICY="DROP"
INPUT_CHAIN="INPUT"
OUTPUT_CHAIN="OUTPUT"
FORWARD_CHAIN="FORWARD"

# Define internal and external network interfaces
INTERNAL_IFACE="eth0"
EXTERNAL_IFACE="eth1"

# Flush existing rules
echo "Flushing existing iptables rules..."
iptables -F
iptables -t nat -F
iptables -X

# Set default policies
echo "Setting default policies..."
iptables -P INPUT $DEFAULT_POLICY
iptables -P OUTPUT ACCEPT
iptables -P FORWARD $DEFAULT_POLICY

# Allow loopback interface
echo "Allowing loopback interface..."
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow incoming SSH
echo "Allowing incoming SSH connections..."
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow incoming HTTP and HTTPS
echo "Allowing incoming HTTP and HTTPS..."
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Enable NAT for outgoing traffic on the external interface (SNAT)
echo "Enabling NAT on the external interface ($EXTERNAL_IFACE)..."
iptables -t nat -A POSTROUTING -o $EXTERNAL_IFACE -j MASQUERADE

# Forward traffic between internal and external interfaces
echo "Allowing traffic forwarding between internal ($INTERNAL_IFACE) and external interfaces..."
iptables -A FORWARD -i $INTERNAL_IFACE -o $EXTERNAL_IFACE -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i $EXTERNAL_IFACE -o $INTERNAL_IFACE -j ACCEPT

# Save the configuration (Debian/Ubuntu style)
echo "Saving iptables configuration..."
iptables-save > /etc/iptables/rules.v4

# Output current iptables configuration
echo "Current iptables configuration:"
iptables -L
iptables -t nat -L

echo "Firewall configuration complete."

