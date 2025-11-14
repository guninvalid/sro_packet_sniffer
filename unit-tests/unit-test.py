from scapy.all import sniff
# from libraries.logger import info
from sniffing.packet_class import Packet

info("Attempting packet processing...")
packet = sniff(offline="sample_packets/capture.pcap", count=1)
assert (packet != None)
info("Assertion passed!")

info("Creating Packet object...")
packet = Pacet(packet)
assert packet != None
info ("Assesstion passed!")

info("Testing flags...")
assert (packet.SYN_FLAG == True)
assert (packet.FIN_FLAG == False)
info("Assertion passed!")