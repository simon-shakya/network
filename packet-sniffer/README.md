# Python-Based Network Traffic Analyzer Setup

This guide walks you through setting up a Python-based network traffic analyzer that captures and analyzes packet data from live network interfaces. We'll use libraries like `scapy` for packet capture and analysis, and `matplotlib` for data visualization. Optionally, we’ll also cover `pyshark` for integration with Wireshark to provide a Wireshark-like interface.

## Steps to Set Up

### 1. Install Required Libraries

You'll need to install the following Python libraries:

- **scapy**: Used for packet capturing and analysis.
- **matplotlib**: Used for creating visualizations of the captured network data.
- **pyshark** (optional): Provides integration with Wireshark, enabling you to use it like a Wireshark interface for Python.

To install these libraries, run the following command:

```bash
pip install scapy matplotlib pyshark
