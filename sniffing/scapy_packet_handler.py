from scapy.all import IP,TCP,IPSession,TCPSession,PacketList # type: ignore
from scapy.all import Packet as SCPacket
from sniffing.packet_class import Packet
from sniffing.packet_class import CSV_HEADER
from sniffing.config import SRO_PORT,PACKET_COUNT
from libraries.logger import debug, info, warn, error, fatal

incoming_packet_buffer:list[Packet] = [];
outgoing_packet_buffer:list[Packet] = [];

def packet_handler(dum_packet:SCPacket):
  global incoming_packet_buffer, outgoing_packet_buffer;
  try:
    # ok. it looks like i have to try unfortunately.
    # so i want a packet serializer effectively. i want something
    # that will handle packet buffering.
    # how am i gonna handle packet retransmits? i have no idea!
    # but point being i need a packet buffer. add a packet to the buffer
    # then test if it's too long. 
    # do i need two buffers for incoming/outgoing packets? probably. i don't want ack
    # packets polluting my buffers.
    # alright. time to program
    packet:Packet = Packet(dum_packet)
    # append_to_buffer:list[Packet] = outgoing_packet_buffer;
    # if packet.is_partial_packet:
    #   if packet.is_incoming:
    #     append_to_buffer = incoming_packet_buffer;
    #   append_to_buffer.append(packet)
    #   # ok. now i want to make sure that the flags match up.
    #   start_packet:Packet = append_to_buffer[0];
    #   if (start_packet.tcp.flags != packet.tcp.flags):
    #     # if the flags don't match up, throw an error. still append as usual but take the initial
    #     # flag as gospel
    #     pass;
    # else:
    #   if packet.is_incoming: # for complete packets, skip the buffer and empty
    #     incoming_packet_buffer = [];
    #   else:
    #     outgoing_packet_buffer = [];
    info(packet.print())
  except Exception as e:
    error("There was an error!")
    error("Error: " + str(e))
    error("Offending packet: " + dum_packet.summary())
    error("Load hex: " + dum_packet[IP][TCP].load.hex())