from scapy.all import sniff
from scapy.all import IP,TCP
from hashlib import sha256
from Packet import Packet,TARGET_IP

def main():
  print(f"Starting packet capture for {TARGET_IP}...")
  # ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)
  packets = sniff(filter=f"host {TARGET_IP}", prn=packet_handler, count=20)

def packet_handler(dum_packet):
  packet = Packet(dum_packet)
  print(packet.print())


main()