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

def main():
  print(f"Starting packet capture for {TARGET_IP}...")
  # ENCRYPTION_NUM_LOOKUP_ARRAY = gen_lookup_array(121243)
  packets = sniff(filter=f"host {TARGET_IP}", prn=packet_handler, count=20)

def packet_handler(packet):
  if packet.haslayer(TCP):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    if src_ip == TARGET_IP or dst_ip == TARGET_IP:
      flag_depreciator = packet[IP][TCP].flags.value;
      FIN_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      SYN_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      RST_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      PSH_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      ACK_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      URG_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      ECE_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      CWR_FLAG = flag_depreciator % 2 == 1;
      flag_depreciator = flag_depreciator >> 1;
      flag_string = "";
      # if (CWR_FLAG):
      #   flag_string += "C"
      # else: flag_string += " "
      # if (ECE_FLAG):
      #   flag_string += "E"
      # else: flag_string += " "
      # if (URG_FLAG):
      #   flag_string += "U"
      # else: flag_string += " "
      if (ACK_FLAG):
        flag_string += "A"
      else: flag_string += " "
      if (PSH_FLAG):
        flag_string += "P"
      else: flag_string += " "
      if (RST_FLAG):
        flag_string += "R"
      else: flag_string += " "
      if (SYN_FLAG):
        flag_string += "S"
      else: flag_string += " "
      if (FIN_FLAG):
        flag_string += "F"
      else: flag_string += " "
      packet_string = f"Packet: {src_ip} -> {dst_ip} {flag_string}"

      if (PSH_FLAG):
        data_bytes = packet[IP][TCP].payload.load
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
          packet_addendum = f"Encryption key num passed! Caught num {code}."
          # print(packet_addendum)
          # print(ENCRYPTION_NUM_LOOKUP_ARRAY[0:30])
          # print(f"Of length {len(ENCRYPTION_NUM_LOOKUP_ARRAY)}")
          raw = ENCRYPTION_NUM_LOOKUP_ARRAY[code]
          packet_addendum += f" (Raw: {raw})"
        packet_string += f"[{packet_preamble}] {packet_addendum}"

      print(packet_string)

def encryption_code_lookup(num):
  key_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[num]
  # key_sha = str(sha256(key_raw))[0:15]
  # return (key_raw, key_sha)
  return (key_raw, None)

def decrypt(key, data):
  if (key == ""): return

  var final_data = []

  for i in range(0, len(data)):
    byte = data[i];
    offset = key[(i % len(key)):(i % len(key))].encode('utf-8')[0]
    final_byte = byte - offset
    while final_byte < -128:
      final_byte += 256
    final_data[i] = final_byte
  return final_data


main()