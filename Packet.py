from scapy.all import sniff
from scapy.all import IP,TCP
from hashlib import sha256
from config import DEBUG,TARGET_IP

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
  
  def __init__(self, ppacket):
    # initializers
    self.packet = ""
    self.tcp = ""
    self.src_ip = ""
    self.dst_ip = ""
    self.FIN_FLAG = ""; self.SYN_FLAG = ""; self.RST_FLAG = ""; self.PSH_FLAG = ""; self.ACK_FLAG = ""; self.URG_FLAG = ""; self.ECE_FLAG = ""; self.CWR_FLAG = "";
    self.data_length = 0; self.data_bytes = "";
    self.op_code = ""
    self.packet_addendum = ""
    self.decrypted_data = ""
    

    self.packet = ppacket
    if (self.packet.haslayer(TCP) == False):
      return self
    self.tcp = self.packet[IP][TCP]
    self.src_ip = self.packet[IP].src
    self.dst_ip = self.packet[IP].dst
    if self.src_ip == TARGET_IP or self.dst_ip == TARGET_IP:
      self.set_flags()
      self.parse_data()
  def set_flags(self):
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
  def parse_data(self):
    if (self.PSH_FLAG == False):
      return #if no data no bother
    raw_data_bytes = self.tcp.payload.load
    self.data_length = parse_bytes_to_num(raw_data_bytes[0:2]) # initial length
    self.data_bytes = raw_data_bytes[2:]
    self.op_code = parse_bytes_to_num(self.data_bytes[0:2])
    self.packet_addendum = f"[RAW] {self.data_bytes.hex()}"
    if (self.op_code == 107):
      num_bytes = (self.data_bytes[2] * 256) + self.data_bytes[3]
    #   print(num_bytes)
      code = 0
      OFFSET = 4; #const
      for i in range(0, num_bytes):
        code += (10 ** (num_bytes - i - 1)) * (self.data_bytes[OFFSET + i] - 48)
      Packet.encryption_num = code;
      Packet.encryption_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[code]
      sha_encoder = sha256()
      sha_encoder.update(str(Packet.encryption_raw).encode('ascii'))
      Packet.encryption_key = sha_encoder.hexdigest()[0:16] # i am surprised this works
      self.packet_addendum = f"Encryption key num passed! Caught num {code}."
      self.packet_addendum += f" (Raw: {Packet.encryption_raw}, key: {Packet.encryption_key})"
    else:
      # attempt to decrypt
      self.decrypt(Packet.encryption_key)
  def decrypt(self, encryption_key):
    if (encryption_key == ""): return
    debug("Decrypyting!")
    final_data: list[bytes] = [b"0"] * self.data_length
    for i in range(0, len(self.data_bytes)):
      byte = self.data_bytes[i];
      key_length = len(encryption_key)
      offset = encryption_key[(i % key_length)].encode('utf-8')[0]
      final_byte = byte - offset
      while final_byte < -128:
        final_byte += 256
      final_data[i] = final_byte
    self.decrypted_data : bytes = bytes(final_data)
    self.packet_addendum = f"[DEC]: {self.decrypted_data.hex()}"
  def print(self):
    # ok so what i want is
    # if there 
    # nvm
    return f"Packet {self.src_ip} -> {self.dst_ip}: [{self.data_length}B] {self.packet_addendum}"

def parse_bytes_to_num(byte_array):
  accumulator = 0
  N = len(byte_array)
  for i in range(0, N):
    accumulator += (256 ** (N - i - 1)) * byte_array[i]
  return accumulator

def encryption_code_lookup(num):
  key_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[num]
  # key_sha = str(sha256(key_raw))[0:15]
  # return (key_raw, key_sha)
  return (key_raw, None)
Packet.encryption_raw = ""
Packet.encryption_num = ""
Packet.encryption_key = ""

def debug(message):
  if (DEBUG == True):
    print(message)