from scapy.all import Packet
from logger import info

info("Attempting packet processing...")
packet = sniff(offline="sample_packets/capture.pcap", count=1)
assert (packet != None)
info("Assertion passed!")

info("Testing flags...")
assert (packet.SYN_FLAG == True)
assert (packet.FIN_FLAG == False)
info("Assertion passed!")