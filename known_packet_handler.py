# # from packet_class import Packet

# def handle_known_packet(packet) -> bool:
#   match packet.op_code:
#     case 0x000e:
#       handle_as_ping(packet)
#       return True
#     case _:
#       return False

# def handle_as_ping(packet):
#   packet.packet_addendum = "Ping!"