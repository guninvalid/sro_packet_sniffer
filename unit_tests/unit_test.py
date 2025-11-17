from scapy.all import sniff
from libraries.logger import info
from sniffing.packet_class import Packet
# from sniffing.packet_class import 

def test_exists():
    # just testing imports at the very least
    assert Packet != None
    assert info != None
    assert sniff != None