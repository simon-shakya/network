import matplotlib.pyplot as plt
from scapy.all import sniff, IP, TCP

# Variables to hold data for visualization
packet_sizes = []
timestamps = []

# Packet handler to capture size and timestamp
def packet_handler(pkt):
    if pkt.haslayer(IP):
        size = len(pkt)
        timestamp = pkt.time
        packet_sizes.append(size)
        timestamps.append(timestamp)

# Start sniffing for a defined number of packets
print("Capturing packets...")
sniff(iface="eth0", prn=packet_handler, store=0, count=100)

# Create a time-series plot for packet sizes
plt.plot(timestamps, packet_sizes)
plt.xlabel('Timestamp')
plt.ylabel('Packet Size (Bytes)')
plt.title('Packet Size Over Time')
plt.show()
