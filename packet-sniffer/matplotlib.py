import matplotlib.pyplot as plt
from scapy.all import sniff

# Dictionary to store packet counts per protocol
protocol_counts = {}

# Packet handler function to count protocols
def packet_handler(pkt):
    if pkt.haslayer('IP'):
        protocol = pkt.proto
        if protocol not in protocol_counts:
            protocol_counts[protocol] = 1
        else:
            protocol_counts[protocol] += 1

# Start sniffing
print("Capturing packets...")
sniff(iface="eth0", prn=packet_handler, store=0, count=100)

# Plot the data
plt.bar(protocol_counts.keys(), protocol_counts.values())
plt.xlabel('Protocol')
plt.ylabel('Packet Count')
plt.title('Packet Count by Protocol')
plt.show()
