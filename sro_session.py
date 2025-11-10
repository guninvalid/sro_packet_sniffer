# from scapy.all import DefaultSession
# from scapy.all import Packet as SCPacket


# # borrowed from DefaultSession
# class SRO_Session(DefaultSession):
#   def __init__(self, supersession = None):
#     if supersession != None and not isinstance(supersession, DefaultSession):
#       supersession = supersession()
#     self.supersession = supersession

#   def process(self, pkt:SCPacket):
#     # Called to pre-process the packet
#     # Optionally handle supersession
#     if self.supersession:
#       return self.supersession.process(pkt)
#     return pkt

#   def recv(self, sock):
#     packet = sock.recv()
#     if packet == None:
#       return None
#     pkt = self.process(pkt)z
#     if pkt:
#       yield pkt