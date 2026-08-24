from scapy.all import sniff,wrpcap
from scapy.all import IP,TCP,IPSession,TCPSession,PacketList # type: ignore
from scapy.all import Packet as SCPacket
from hashlib import sha256
from sniffing.packet_class import Packet
from sniffing.packet_class import CSV_HEADER
from sniffing.config import SRO_PORT,PACKET_COUNT
from libraries.logger import debug, info, warn, error, fatal
from libraries.logger import print_csv,clear_csv
# from sniffing.known_packet_handler import populate_handlers

def main():
  # populate_handlers()
  clear_csv()
  print_csv(CSV_HEADER)
  info(f"Starting packet capture...")
  packets = sniff(session=TCPSession, filter=f"tcp port {SRO_PORT}", prn=packet_handler, count=PACKET_COUNT)
  # debug(str(packets.hexdump()))
  # wrpcap(filename="this is my cool file!!",pkt=packets)
  info("Packet capture completed!")
  return packets

def debug_offline():
  info(f"Debugging packet capture...")
  packets = sniff(offline="sample_packets/capture.pcap", session=TCPSession, filter=f"tcp port {SRO_PORT}", prn=packet_handler, count=PACKET_COUNT)
  info(f"Debug complete!");
  return packets;

if (__name__ == "__main__"):
  debug_offline();