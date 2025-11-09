from packet_class import Packet,packet_handler_class
from packet_class import handlers,parse_bytes_to_num


class PingHandler(packet_handler_class):
  def handle(self, packet:Packet): # pyright: ignore[reportIncompatibleMethodOverride]
    packet.packet_addendum = "Ping!"
    return True

class EnemyHurtboxHandler(packet_handler_class):
  def handle(self, packet:Packet):
    data = packet.data_bytes
    self.packet_addendum = "Hit: " + self.packet_addendum
    return True
    

def populate_handlers():
  handlers[14] = PingHandler();
  handlers[30] = EnemyHurtboxHandler()