from scapy.all import sniff,wrpcap
from scapy.all import IP,TCP,IPSession,TCPSession,PacketList # type: ignore
from scapy.all import Packet as SCPacket
from hashlib import sha256
from sniffing.packet_class import Packet
from sniffing.packet_class import CSV_HEADER
from libraries.config import TARGET_IP,PACKET_COUNT
from libraries.logger import debug, info, warn, error, fatal
from libraries.logger import print_csv,clear_csv
from sniffing.known_packet_handler import populate_handlers

def main():
  populate_handlers()
  clear_csv()
  print_csv(CSV_HEADER)
  info(f"Starting packet capture for {TARGET_IP}...")
  packets = sniff(session=TCPSession, filter=f"host {TARGET_IP}", prn=packet_handler, count=PACKET_COUNT)
  # debug(str(packets.hexdump()))
  # wrpcap(filename="this is my cool file!!",pkt=packets)
  info("Packet capture completed!")

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