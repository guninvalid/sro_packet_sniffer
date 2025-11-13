from scapy.all import Packet
from logger import info

info("Attempting packet processing...")
packet = sniff(offline="sample_packets/capture.pcap", count=1)
assert (packet != None)
info("Assertion passed!")