from scapy.all import sniff, IP, TCP

# Define a packet processing function
def packet_handler(pkt):
    if pkt.haslayer(IP):
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        print(f"Source: {ip_src}, Destination: {ip_dst}")
    
    if pkt.haslayer(TCP):
        print(f"TCP Packet - Source Port: {pkt[TCP].sport}, Destination Port: {pkt[TCP].dport}")

# Capture packets from the specified interface (e.g., eth0 or wlan0)
print("Starting packet capture...")
sniff(iface="eth0", prn=packet_handler, store=0)
