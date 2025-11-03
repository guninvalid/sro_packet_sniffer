from scapy.all import sniff
from scapy.all import IP,TCP
from hashlib import sha256
from Packet import Packet

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

def parse_bytes_to_num(byte_array):
  accumulator = 0
  N = len(byte_array)
  for i in range(0, N):
    accumulator += (256 ** (N - i - 1)) * byte_array[i]
  return accumulator

def packet_handler(dum_packet):
  packet = Packet(dum_packet)
  print(packet.print())

def encryption_code_lookup(num):
  key_raw = ENCRYPTION_NUM_LOOKUP_ARRAY[num]
  # key_sha = str(sha256(key_raw))[0:15]
  # return (key_raw, key_sha)
  return (key_raw, None)


main()