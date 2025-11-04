from scapy.all import sniff
from scapy.all import IP,TCP
from hashlib import sha256
from Packet import Packet
from config import DEBUG,TARGET_IP,PACKET_COUNT

def main():
  print(f"Starting packet capture for {TARGET_IP}...")
  # ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)
  packets = sniff(filter=f"host {TARGET_IP}", prn=packet_handler, count=PACKET_COUNT)

def packet_handler(dum_packet):
  try:
    packet = Packet(dum_packet)
    print(packet.print())
  except Exception as e:
    print("There was an error!")
    print("Erorr: " + str(e))
    print("Offending packet: " + dum_packet.summary() + dum_packet[IP][TCP].load.hex())


main()