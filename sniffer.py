from scapy.all import sniff
from scapy.all import IP,TCP
from hashlib import sha256

def gen_lookup_array(N):
  # if it doesnt exist then generate the array
  lookup = [-1] * N
  for i in range(0, N):
    key_raw = i
    key_num = (key_raw ** 3) % N
    lookup[key_num] = key_raw
  return lookup

TARGET_IP = "167.99.6.174"
ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)

class Packet:
  def __init__(self, ppacket):
    self.packet = ppacket
    if (self.packet.haslayer(TCP)):
      self.tcp = self.packet[IP][TCP]
    src_ip = self.packet[IP].src
    dst_ip = self.packet[IP].dst
    if src_ip == TARGET_IP or dst_ip == TARGET_IP:
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
  def parse_data(self):
    if (not self.PSH_FLAG):
      return #if no data no bother
    data_bytes = self.tcp.payload.load
    packet_preamble = data_bytes[0:2].hex() # initial length
    data_bytes = data_bytes[2:]
    packet_addendum = data_bytes.hex()
    if (data_bytes[0] == 0 and data_bytes[1] == 107):
      num_bytes = (data_bytes[2] * 256) + data_bytes[3]
      print(num_bytes)
      code = 0;
      OFFSET = 4; #const
      for i in range(0, num_bytes):
        code += (10 ** (num_bytes - i - 1)) * (data_bytes[OFFSET + i] - 48)
      raw = ENCRYPTION_NUM_LOOKUP_ARRAY[code]
      packet_string += f"[{packet_preamble}] {packet_addendum}"
def main():
  print(f"Starting packet capture for {TARGET_IP}...")
  # ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)
  packets = sniff(filter=f"host {TARGET_IP}", prn=packet_handler, count=20)

def parse_bytes_to_num(byte_array):
  accumulator = 0
  N = len(byte_array)
  for i in range(0, N):
    accumulator += (256 ** (N - i - 1)) * byte_array[i]
  return accumulator

def packet_handler(dum_packet):
  packet = Packet(dum_packet)

def encryption_code_lookup(num):
  key_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[num]
  # key_sha = str(sha256(key_raw))[0:15]
  # return (key_raw, key_sha)
  return (key_raw, None)

def decrypt(key, data):
  if (key == ""): return

  final_data = []

  for i in range(0, len(data)):
    byte = data[i];
    offset = key[(i % len(key)):(i % len(key))].encode('utf-8')[0]
    final_byte = byte - offset
    while final_byte < -128:
      final_byte += 256
    final_data[i] = final_byte
  return final_data


main()