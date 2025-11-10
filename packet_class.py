from typing import Any
from scapy.all import sniff
from scapy.all import IP,TCP #type:ignore
from scapy.all import Packet as ScapyPacket
# from GameSession import GameSession
from hashlib import sha256
from config import TARGET_IP,PRINT_CSV,CSV_DELIMETER
from logger import debug,info,warning,error,fatal,warn,print_csv
from packet_listing import SERVER_PACKET_LIST,CLIENT_PACKET_LIST
# from known_packet_handler import handle_known_packet

def gen_lookup_array(N):
  # if it doesnt exist then generate the array
  lookup = [-1] * N
  for i in range(0, N):
    key_raw = i
    key_num = (key_raw ** 3) % N
    lookup[key_num] = key_raw
  return lookup

ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)

class Packet:
  def __getattr__(self, name: str) -> Any:
    # PLEASE WORK
    #partially helped by deepseek
    #then fixed by stackoverflow
    return None
  
  def __init__(self, scapyPacket:ScapyPacket):
    # initializers"""  """
    self.packet:ScapyPacket
    self.tcp:ScapyPacket
    self.src_ip:str
    self.dst_ip:str
    self.FIN_FLAG:bool; self.SYN_FLAG:bool; self.RST_FLAG:bool; self.PSH_FLAG:bool; self.ACK_FLAG:bool; self.URG_FLAG:bool; self.ECE_FLAG:bool; self.CWR_FLAG:bool;
    self.data_length:int = -1; self.data_bytes:bytes;
    self.op_code:int
    self.packet_addendum:str; self.packet_type:str = ""; self.csv_trailer:str;
    self.decrypted_data:bytes
    self.is_incoming:bool; self.is_outgoing:bool; self.dir_flag:str;
    
    self.packet = scapyPacket
    if (self.packet.haslayer(TCP) == False):
      return self
    self.tcp = self.packet[IP][TCP]
    self.src_ip = self.packet[IP].src
    self.dst_ip = self.packet[IP].dst
    if self.src_ip == TARGET_IP or self.dst_ip == TARGET_IP:
      self.set_flags()
      self.parse_data()
  def set_flags(self) -> None:
    if (self.dst_ip == TARGET_IP):
      self.is_outgoing = True
      self.dir_flag = "OUT"
    if (self.src_ip == TARGET_IP):
      self.is_incoming = True
      self.dir_flag = " IN"
    flag_depreciator = self.tcp.flags.value;
    self.FIN_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.SYN_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.RST_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.PSH_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.ACK_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.URG_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.ECE_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.CWR_FLAG = flag_depreciator % 2 == 1;
    flag_depreciator = flag_depreciator >> 1;
    self.packet_addendum = self.tcp.flags
  def parse_data(self) -> None:
    if (self.PSH_FLAG == False):
      self.data_length = 0
      self.packet_type = self.packet_addendum
      self.packet_addendum = ""
      return #if no data no bother
    raw_data_bytes:bytes = self.tcp.payload.load
    self.data_length = parse_bytes_to_num(raw_data_bytes[0:2]) # initial length
    self.data_bytes = raw_data_bytes[2:]
    if (self.data_length != len(self.data_bytes)):
      # # allegedly in some cases the length will be in ascii not hex
      # if (30 <= raw_data_bytes[0] and raw_data_bytes[0] <= 39
      #     and 30 <= raw_data_bytes[1] and raw_data_bytes[1] <= 39):
      #   # attempt to process as ascii length
      #   ascii_int:int = raw_data_bytes[1] - 30
      #   ascii_int += 10 * (raw_data_bytes[0] - 30)
      #   self.data_length = ascii_int
      #   # test again
      #   if (self.data_length != len(self.data_bytes)):
      #     warn("Malformed packet! Lengths in hex and ascii do not match!")
      # else:
      warn("Malformed packet! Lengths in hex do not match! Skipping potential fragmented packet.")
    # # if (self.data_length != len(self.data_bytes)):
    #   warn("Attempting to auto assign to len(data_length).")
    #   old_length:int = self.data_length
    #   self.data_length = len(self.data_bytes)
    #   warn(f"Problematic packet payload: {self.tcp.payload.load.hex()}")
    #   warn(f"Changed datalength from {old_length} to {self.data_length}")
    outer_op_code = self.negate_incoming_packets(parse_bytes_to_num(self.data_bytes[0:2]))
    self.packet_addendum = f"{self.data_bytes.hex()}"
    self.packet_type = "RAW"
    if (outer_op_code == 107):
      self.clear_text = True
      num_bytes = parse_bytes_to_num(self.data_bytes[2:4])
    #   print(num_bytes)
      code:int = 0
      OFFSET:int = 4; #const
      for i in range(0, num_bytes):
        code += (10 ** (num_bytes - i - 1)) * (self.data_bytes[OFFSET + i] - 48)
      Packet.encryption_num:int = code;
      Packet.encryption_raw:int = ENCRYPTION_NUM_LOOKUP_ARRAY[code]
      sha_encoder = sha256()
      sha_encoder.update(str(Packet.encryption_raw).encode('ascii'))
      Packet.encryption_key:str = sha_encoder.hexdigest()[0:16] # i am surprised this works
      encryption_key_message:str = f"Caught num {code}."
      encryption_key_message += f" (Raw: {Packet.encryption_raw}, key: {Packet.encryption_key})"
      self.packet_addendum = f"Encryption key num passed! "
      self.packet_addendum += encryption_key_message
      # warn(encryption_key_message)
    else:
      
      # attempt to decrypt
      if (self.data_length == len(self.data_bytes)):
        # incorrect lengths are usually because of fragmented packets
        # im gonna be lazy and just ignore them
        is_decrypted:bool = self.decrypt(Packet.encryption_key)
        if (is_decrypted == True):
          self.op_code = self.negate_incoming_packets(parse_bytes_to_num(self.decrypted_data[0:2]))
          self.decrypted_data = self.decrypted_data[2:]
          self.csv_trailer = self.retrieve_packet_desc()
          handle_known_packet(self)
          self.packet_type = f"OP{abs(self.op_code)}"
        else:
          # void the op_code if nonexistent
          # self.op_code = 0
          pass
    if (self.packet_type == "RAW" and self.data_length > 20):
      self.packet_addendum = f"{self.packet_addendum[0:20]}..."
  def decrypt(self, encryption_key) -> bool:
    if (encryption_key == ""): return False
    final_data:bytes = decrypt(self.data_bytes, encryption_key)
    self.decrypted_data : bytes = bytes(final_data)
    self.packet_addendum = f"{self.decrypted_data.hex()}"
    self.packet_type = "DEC"
    return True
  def retrieve_packet_desc(self) -> str:
    if (self.op_code < 0):
      #search for associated server packet
      server_op_code:int = abs(self.op_code)
      if (server_op_code in SERVER_PACKET_LIST):
        return str(SERVER_PACKET_LIST[server_op_code].get("desc"))
    else:
      #search for associated client packet
      client_op_code:int = self.op_code
      if (client_op_code in CLIENT_PACKET_LIST):
        return str(CLIENT_PACKET_LIST[client_op_code].get("desc"))
    return ""
      
  def print(self) -> str:
    # ok so what i want is
    # if there 
    # nvm
    print_csv(csv_line(self))
    return f"Packet {self.src_ip} -> {self.dst_ip}: [{self.dir_flag}{self.data_length}B] [{self.packet_type}]: {self.packet_addendum}"
  def negate_incoming_packets(self, op_code:int) -> int:
    #uses negative op codes for packets from server
    if (self.is_incoming):
      return -1 * op_code
    else:
      return op_code

def none_to_blank(object) -> str:
  if (object is None):
    return ""
  else:
    return str(object)

def csv_elem(object, last_elem=False) -> str:
  if (object != "" and isinstance(object, bytes)):
    object = object.hex()
  elem:str = none_to_blank(object)
  if (last_elem == True):
    return elem
  else:
    return elem + CSV_DELIMETER

def csv_normalize(line:str) -> str:
  return line.replace('\t', CSV_DELIMETER)

CSV_HEADER = csv_normalize("src_ip\tdst_ip\tdata_length\top_code\ttcp.flags\tdata_bytes\tdecrypted_data\tcsv_trailer")
def csv_line(packet:Packet) -> str:
  csv_line:str = csv_elem(packet.src_ip)
  csv_line += csv_elem(packet.dst_ip)
  csv_line += csv_elem(packet.data_length)
  csv_line += csv_elem(packet.op_code)
  csv_line += csv_elem(packet.tcp.flags)
  csv_line += csv_elem(packet.data_bytes)
  csv_line += csv_elem(packet.decrypted_data)
  csv_line += csv_elem(packet.csv_trailer, last_elem=True)
  return csv_line

def handle_known_packet(packet:Packet) -> bool:
  if (packet.op_code in handlers.keys()):
    handler = handlers[packet.op_code]
    return handler.handle(packet)
  else:
    return False

def decrypt(data_bytes:bytes, encryption_key:str) -> bytes:
  debug("Decrypyting!")
  data_length:int = len(data_bytes)
  final_data:list[bytes] = [b'0'] * data_length
  key_length:int = len(encryption_key)
  for i in range(0, data_length):
    byte = data_bytes[i];
    offset = encryption_key[(i % key_length)].encode('utf-8')[0]
    final_byte = byte - offset
    while final_byte < 0:
      final_byte += 256
    final_data[i] = int.to_bytes(final_byte)
  return b''.join(final_data)

def parse_bytes_to_num(byte_array):
  accumulator = 0
  N = len(byte_array)
  for i in range(0, N):
    accumulator += (256 ** (N - i - 1)) * byte_array[i]
  return accumulator

# def encryption_code_lookup(num):
#   key_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[num]
#   # key_sha = str(sha256(key_raw))[0:15]
#   # return (key_raw, key_sha)
#   return key_raw

class packet_handler_class:
  def handle(self, packet:Packet) -> bool:
    return False

Packet.encryption_raw = -1
Packet.encryption_num = -1
Packet.encryption_key = ""
handlers:dict[int,packet_handler_class] = {}
# automatically populated by the sniffer class