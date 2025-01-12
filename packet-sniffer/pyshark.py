import pyshark

# Start capturing packets from a network interface
capture = pyshark.LiveCapture(interface="eth0")

# Process each packet
for packet in capture.sniff_continuously():
    print(f"Packet: {packet}")
    if 'IP' in packet:
        print(f"Source IP: {packet.ip.src}, Destination IP: {packet.ip.dst}")
