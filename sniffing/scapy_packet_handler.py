from scapy.all import sniff,wrpcap
from scapy.all import IP,TCP,IPSession,TCPSession,PacketList # type: ignore
from scapy.all import Packet as SCPacket
from hashlib import sha256
from sniffing.packet_class import Packet
from sniffing.packet_class import CSV_HEADER
from sniffing.config import SRO_PORT,PACKET_COUNT
from libraries.logger import debug, info, warn, error, fatal
from libraries.logger import print_csv,clear_csv

def packet_handler(dum_packet:SCPacket):
  try:
    packet:Packet = Packet(dum_packet)
    info(packet.print())
  except Exception as e:
    error("There was an error!")
    error("Error: " + str(e))
    error("Offending packet: " + dum_packet.summary())
    error("Load hex: " + dum_packet[IP][TCP].load.hex())