from packet_class import Packet,packet_handler_class
from packet_class import handlers,parse_bytes_to_num

# pyright: ignore[reportIncompatibleMethodOverride]

class PingHandler(packet_handler_class):
  def handle(self, packet:Packet) -> bool: 
    # first make sure it's actually a ping
    if (packet.data_length != 2):
      return False
    else:
      packet.packet_addendum = "Ping!"
      packet.csv_trailer = "ping"
      return True

class EnemyHurtboxHandler(packet_handler_class):
  def handle(self, packet:Packet) -> bool:
    data = packet.data_bytes
    packet.packet_addendum = "Hit: " + packet.packet_addendum
    return True
    

def populate_handlers():
  handlers[14] = PingHandler();
  handlers[-33] = PingHandler();
  # handlers[30] = EnemyHurtboxHandler()
  handlers[-16] = EnemyHurtboxHandler()
  handlers[-48] = EnemyHurtboxHandler()