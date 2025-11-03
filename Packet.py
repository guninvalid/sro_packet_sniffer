class Packet:
  def __init__(self, ppacket):
    self.packet = ppacket
    if (self.packet.haslayer(TCP)):
      self.tcp = self.packet[IP][TCP]
    self.src_ip = self.packet[IP].src
    self.dst_ip = self.packet[IP].dst
    self.decrypted_data == ""
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
  def parse_data(self):
    if (not self.PSH_FLAG):
      return #if no data no bother
    raw_data_bytes = self.tcp.payload.load
    self.data_length = parse_bytes_to_num(raw_data_bytes[0:2]) # initial length
    self.data_bytes = raw_data_bytes[2:]
    self.op_code = parse_bytes_to_num(self.data_bytes[0:2])
    if (self.op_code == 107):
      num_bytes = (self.data_bytes[2] * 256) + self.data_bytes[3]
      print(num_bytes)
      code = 0
      OFFSET = 4; #const
      for i in range(0, num_bytes):
        code += (10 ** (num_bytes - i - 1)) * (self.data_bytes[OFFSET + i] - 48)
      Packet.encryption_num = code;
      Packet.encryption_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[code]
      self.packet_addendum = f"Encryption key num passed! Caught num {code}."
      self.packet_addendum += f" (Raw: {Packet.encryption_raw})"
    else:
      # attempt to decrypt
      self.decrypt(Packet.encryption_raw)
  def decrypt(self, encryption_key):
    if (encryption_key == ""): return
    final_data = []
    for i in range(0, len(self.data_bytes)):
      byte = self.data_bytes[i];
      offset = encryption_key[(i % len(encryption_key)):(i % len(encryption_key))].encode('utf-8')[0]
      final_byte = byte - offset
      while final_byte < -128:
        final_byte += 256
      final_data[i] = final_byte
    self.decrypted_data = final_data
  def print(self):
    if (self.decrypted_data != ""):
      self.packet_addendum = self.decrypted_data.hex()
    return f"Packet: {self.src_ip} -> {self.dst_ip}: {self.packet_addendum}"