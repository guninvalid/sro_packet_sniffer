from scapy.all import sniff
from scapy.all import IP,TCP
from scapy.all import Packet as SCPacket
from scapy.all import PacketList
from hashlib import sha256
from Packet import Packet
from config import TARGET_IP,PACKET_COUNT
from logger import debug, info, warn, error, fatal

def main():
  print(f"Starting packet capture for {TARGET_IP}...")
  # ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)
  packets:PacketList = sniff(filter=f"host {TARGET_IP}", prn=packet_handler, count=PACKET_COUNT)

def packet_handler(dum_packet:SCPacket):
  try:
    packet:Packet = Packet(dum_packet)
    info(packet.print())
  except Exception as e:
    error("There was an error!")
    error("Error: " + str(e))
    error("Offending packet: " + dum_packet.summary())
    error("Load hex: " + dum_packet[IP][TCP].load.hex())


main()