from scapy.all import sniff,TCPSession
# from libraries.logger import info
from sniffing.packet_class import Packet
from sniffer import packet_handler
from sniffing.config import TARGET_IP

def test_exists():
    # just testing imports at the very least
    assert Packet != None
    # assert info != None
    assert sniff != None

def read_packets(count=9999):
    packets = sniff(offline="sample_packets/capture.pcap",
                    session=TCPSession, filter=f"host {TARGET_IP}", 
                    count=count)

def test_encryption_lookup_exists():
    from sniffing.packet_class import ENCRYPTION_NUM_LOOKUP_ARRAY
    assert ENCRYPTION_NUM_LOOKUP_ARRAY != None
    assert len(ENCRYPTION_NUM_LOOKUP_ARRAY) == 121243
    assert ENCRYPTION_NUM_LOOKUP_ARRAY[0] == 0
    assert ENCRYPTION_NUM_LOOKUP_ARRAY[1] == 1
    assert ENCRYPTION_NUM_LOOKUP_ARRAY[69] == 328509
    assert ENCRYPTION_NUM_LOOKUP_ARRAY[4666] == 86643
    for i in range(0, 121243):
        assert ENCRYPTION_NUM_LOOKUP_ARRAY[i] != -1