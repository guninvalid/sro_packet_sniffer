from sniffing.packet_class import Packet,packet_handler_class
from sniffing.packet_class import handlers,parse_bytes_to_num
from libraries.logger import debug,info,warn,error,fatal
from struct import unpack as convert_to_float

# it took me a lot of work to make this not import the packet class
# so no circular import fortunately
# but now it uses event based programming to do that
# more complicated but at least its easier to debug

# pyright: ignore[reportIncompatibleMethodOverride]

class datastream:
  def __init__(self, data_bytes:bytes):
    self.stream:bytes = data_bytes
  def read_byte(self) -> int:
    self.stream = self.read_bytes(1)
    return self.stream[0]
  def read_bool(self) -> bool:
    return self.read_byte() != None and self.read_byte() == 1
  def read_short(self) -> int:
    return parse_bytes_to_num(self.read_bytes(2))
  def read_int(self) -> int:
    return parse_bytes_to_num(self.read_bytes(4))
  def read_long(self) -> int:
    return parse_bytes_to_num(self.read_bytes(8))
  def read_float(self) -> float:
    return convert_to_float('f', self.read_bytes(4))[0]
  def read_bytes(self, buffer_size:int) -> bytes:
    if (buffer_size > len(self.stream)):
      # even if empty just return None
      # return None
      # makes my life easier to throw an exception
      raise IOError("No space left in stream!")
    out:bytes = self.stream[0:buffer_size]
    self.stream = self.stream[buffer_size:]
    return out

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

class EnemyHPHandler(packet_handler_class):
  def handle(self, packet:Packet) -> bool:
    if (packet.data_length != 14):
      return EnemyHurtboxHandler().handle(packet)
    data = packet.decrypted_data
    data = datastream(data)
    # debug(data.hex()) # ok ive figured it out its fine
    # debug_enemy_int_array = data[0:4]
    # debug_length = len(debug_enemy_int_array)
    # debug_length = len(data)
    # enemy_id:int = parse_bytes_to_num(data[0:4])
    # hp_int_array = data[6:14]
    # hp:int = parse_bytes_to_num(data[6:14])
    enemy_id:int = data.read_int()
    hp:int = data.read_long()
    packet.packet_addendum = f"HP Update: Enemy {enemy_id} at {hp} hp"
    packet.csv_trailer = packet.packet_addendum
    return True

# this took an embarassingly long amount of time to find
class EnemySpawnHandler(packet_handler_class):
  def handle(self, packet:Packet) -> bool:
    data = datastream(packet.decrypted_data)
    # var enemy_id = packet.read_int()
    enemy_id:int = data.read_int()
    # var monster_id = packet.read_short()
    monster_id:int = data.read_short()
    # var x = packet.read_short()
    x:int = data.read_short()
    # var y = packet.read_short()
    y:int = data.read_short()
    # var max_hp = packet.read_long()
    max_hp:int = data.read_long()
    # var is_boss = packet.read_byte() == 1
    is_boss:bool = data.read_bool()
    # var is_shiny_enemy = packet.read_byte()
    is_shiny_enemy:bool = data.read_bool()
    # var level = packet.read_short()
    level:int = data.read_short()
    # var size_mod = packet.read_float()
    size_mod:float = data.read_float()
    packet.packet_addendum = f"Enemy {enemy_id} spawned: type {monster_id} at {x},{y} with max hp {max_hp}"
    packet.csv_trailer = packet.packet_addendum
    return True

def populate_handlers():
  handlers[14] = PingHandler();
  handlers[-33] = PingHandler();
  # handlers[30] = EnemyHurtboxHandler()
  handlers[-16] = EnemyHurtboxHandler()
  handlers[-48] = EnemyHPHandler()
  handlers[-14] = EnemySpawnHandler()