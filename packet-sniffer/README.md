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
```


### 2. Capture Network Traffic with Scapy
Scapy is a powerful Python library for packet manipulation and capture. Here’s a basic script to capture packets from a network interface:
[capture.py](https://github.com/simon-shakya/network/blob/main/packet-sniffer/capture.py)


### 3. Integrating with Wireshark Using Pyshark

To integrate with Wireshark, we can use the pyshark library, which acts as a wrapper around Wireshark’s tshark (the command-line version of Wireshark).
pyshark.py 

### 4. Analyzing Network Traffic
You can analyze packet data, such as IP addresses, protocols, and ports. Here’s an example that creates a simple histogram of the number of packets per protocol using matplotlib:
Matplotlib.py 

### 5. Advanced Traffic Analysis and Visualizations
You can use more advanced analysis, such as plotting the distribution of packet sizes, flow durations, or the count of unique source/destination IPs over time.

matplotlib-advance.py 

### 6. Enhancing the Analysis with Flow Monitoring
For deeper network flow analysis, you can monitor connections and traffic flow over time. Here’s a simple example for monitoring TCP connections:
flow.py


### Start sniffing
print("Capturing packets...")
sniff(iface="eth0", prn=packet_handler, store=0, count=100)

### Display the connections and their packet counts
for connection, count in connections.items():
    print(f"Connection {connection}: {count} packets")

### 7. Running Wireshark for Live Monitoring
If you prefer live monitoring similar to Wireshark's GUI, you can use pyshark to monitor the packets in real-time, or run Wireshark alongside your Python analyzer for more detailed inspection.

### Conclusion
This setup allows you to:
1. Capture and analyze network packets using Python.
2. Use scapy for deep packet inspection and analysis.
3. Use matplotlib to visualize network traffic.
4. Optionally integrate with Wireshark for additional packet capture and analysis.
You can extend this further by implementing more complex visualizations, logging, or exporting results to files for detailed traffic analysis.
