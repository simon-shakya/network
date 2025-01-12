from scapy.all import sniff, IP, TCP
from collections import defaultdict

# Dictionary to track TCP connections
connections = defaultdict(int)

def packet_handler(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        sport = pkt[TCP].sport
        dport = pkt[TCP].dport
        
        connection_key = (ip_src, sport, ip_dst, dport)
        connections[connection_key] += 1

# Start sniffing
print("Capturing packets...")
sniff(iface="eth0", prn=packet_handler, store=0, count=100)

# Display the connections and their packet counts
for connection, count in connections.items():
    print(f"Connection {connection}: {count} packets")
