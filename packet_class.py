from scapy.all import sniff
from scapy.all import IP,TCP
from scapy.all import Packet as ScapyPacket
# from GameSession import GameSession
from hashlib import sha256
from config import TARGET_IP
from logger import debug,info,warning,error,fatal,warn
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
  
  def __init__(self, scapyPacket:ScapyPacket):
    # initializers"""  """
    self.packet:ScapyPacket
    self.tcp:ScapyPacket
    self.src_ip:str
    self.dst_ip:str
    self.FIN_FLAG:bool; self.SYN_FLAG:bool; self.RST_FLAG:bool; self.PSH_FLAG:bool; self.ACK_FLAG:bool; self.URG_FLAG:bool; self.ECE_FLAG:bool; self.CWR_FLAG:bool;
    self.data_length:int = -1; self.data_bytes:bytes;
    self.op_code:int
    self.packet_addendum:str; self.packet_type:str = "";
    self.decrypted_data:bytes
    
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
    self.op_code = parse_bytes_to_num(self.data_bytes[0:2])
    self.packet_addendum = f"{self.data_bytes.hex()}"
    self.packet_type = "RAW"
    if (self.op_code == 107):
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
        self.decrypt(Packet.encryption_key)
        is_decrypted:bool = (self.decrypted_data != "")
        if (is_decrypted == True):
          self.op_code = parse_bytes_to_num(self.decrypted_data[0:2])
          handle_known_packet(self)
  def decrypt(self, encryption_key) -> None:
    if (encryption_key == ""): return
    final_data:bytes = decrypt(self.data_bytes, encryption_key)
    self.decrypted_data : bytes = bytes(final_data)
    self.packet_addendum = f"{self.decrypted_data.hex()}"
    self.packet_type = "DEC"
  def print(self) -> str:
    # ok so what i want is
    # if there 
    # nvm
    return f"Packet {self.src_ip} -> {self.dst_ip}: [{self.data_length}B] [{self.packet_type}]: {self.packet_addendum}"

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

Packet.encryption_raw = -1
Packet.encryption_num = -1
Packet.encryption_key = ""


###################################
#                                 #
# THIS USED TO BE A SEPARATE FILE #
# BUT PYTHON COMPLAINED           #
#                                 #
###################################
def handle_known_packet(packet:Packet) -> bool:
  match packet.op_code:
    case 1:
      # multiple,multiple
      return False
    case 2:
      # multiple,multiple
      return False
    case 3:
      # player_effect.gd,just_released
      return False
    case 7:
      # chatbox.gd,_on_chat_entry_line_edit_text_submitted
      return False
    case 8:
      # chatbox.gd,_on_chat_entry_line_edit_text_changed
      return False
    case 9:
      # attribute_window.gd,send_attribute_add_point_packet
      return False
    case 10:
      # mouse_item.gd,try_inventory_swap
      return False
    case 12:
      # inventory_item_slot.gd,use
      return False
    case 14:
      # client.gd,send_ping
      return handle_as_ping(packet)
    case 15:
      # player_shop_item_listing.gd,_on_buy_button_pressed
      return False
    case 19:
      # player.gd,_on_hurtbox_hurt
      return False
    case 21:
      # world.gd,clean_up_map
      return False
    case 23:
      # client.gd,send_login
      return False
    case 24:
      # multiple,multiple
      return False
    case 25:
      # multiple,multiple
      return False
    case 26:
      # title_screen_ui.gd,_on_character_create_button_pressed
      return False
    case 27:
      # title_screen_ui.gd,_on_name_availability_check_button_pressed
      return False
    case 28:
      # multiple,multiple
      return False
    case 29:
      # title_screen_ui.gd,request_character_creator_information
      return False
    case 30:
      # enemy.gd,_on_hurtbox_hurt
      return False
    case 31:
      # Skill.gd,send_skill_packet
      return False
    case 32:
      # portal.gd,_process
      return False
    case 33:
      # hot_slot.gd,send_hotslot_data_to_server
      return False
    case 34:
      # map_object.gd,use_object
      return False
    case 35:
      # crafting_window.gd,_on_craft_button_pressed
      return False
    case 37:
      # Minigame.gd,end_minigame
      return False
    case 38:
      # inventory_item_slot.gd,use
      return False
    case 38:
      # mouse_item.gd,multiple
      return False
    case 39:
      # multiple,multiple
      return False
    case 40:
      # ranking_window.gd,request_ranking_info_for_option_menu_index
      return False
    case 41:
      # player.gd,check_out_of_bounds
      return False
    case 42:
      # player_shop_item_listing.gd,_on_buy_button_pressed
      return False
    case 44:
      # player_shop.gd,use_object
      return False
    case 45:
      # crafting_window.gd,request_crafting_recipes
      return False
    case 46:
      # crafting_window.gd,request_crafting_recipe_materials
      return False
    case 48:
      # guild_window.gd,_on_create_guild_button_pressed
      return False
    case 49:
      # guild_window.gd,request_guild_info
      return False
    case 51:
      # death_screen.gd,_on_death
      return False
    case 53:
      # dungeon_entrance_window.gd,_on_enter_button_pressed
      return False
    case 54:
      # player.gd,_on_hurtbox_hurt
      return False
    case 55:
      # storage_window.gd,request_current_storage_page_items
      return False
    case 56:
      # storage_window.gd,withdraw_item
      return False
    case 57:
      # storage_window.gd,deposit_item
      return False
    case 58:
      # mouse_item.gd,try_storage_swap
      return False
    case 59:
      # party_window.gd,_on_button_invite_pressed
      return False
    case 59:
      # character_info_window.gd,_on_add_to_party_button_pressed
      return False
    case 60:
      # party_window.gd,message_server_party_action
      return False
    case 61:
      # party_window.gd,request_party_member_list
      return False
    case 62:
      # channel_packet_handler.gd,_receive_invitation
      return False
    case 63:
      # bug.gd,_on_hurtbox_hurt
      return False
    case 64:
      # fishing_bobber.gd,multiple
      return False
    case 65:
      # fishing_trigger.gd,multiple
      return False
    case 67:
      # grapple_projectile.gd,_on_body_entered
      return False
    case 68:
      # character.gd,multiple
      return False
    case 69:
      # building_tool.gd,handle_right_click
      return False
    case 70:
      # Minigame.gd,early_quit
      return False
    case 71:
      # building_tool.gd,handle_left_click
      return False
    case 84:
      # npc_dialogue_window.gd,cancel_dialogue
      return False
    case 85:
      # player_death_effect.gd,_ready
      return False
    case 88:
      # medishot_player_projectile.gd,_on_contact_made_with_ground
      return False
    case 89:
      # building_tool.gd,handle_left_click
      return False
    case 90:
      # building_tool.gd,handle_right_click
      return False
    case 91:
      # building_tool.gd,handle_left_click
      return False
    case 92:
      # map_object_inspect_window.gd,send_new_permissions_packet
      return False
    case 94:
      # player.gd,do_emote
      return False
    case 95:
      # unlearn_skill_window.gd,_on_enter_button_pressed
      return False
    case 96:
      # instrument_window.gd,play_instrument_note
      return False
    case 97:
      # multiple,multiple
      return False
    case 98:
      # inventory_item_slot.gd,_process
      return False
    case 99:
      # mail_window.gd,open_window
      return False
    case 100:
      # mail_window.gd,set_selected_mail_id
      return False
    case 101:
      # mail_window.gd,_on_delete_mail_button_pressed
      return False
    case 102:
      # mail_item_slot.gd,clicked
      return False
    case 103:
      # housing_portal_window.gd,_on_set_home_button_pressed
      return False
    case 104:
      # inventory_item_slot.gd,use
      return False
    case 105:
      # cash_shop_window_item.gd,_on_buy_button_pressed
      return False
    case 106:
      # cash_shop_window.gd,open_window
      return False
    case 107:
      # client.gd,new_encryption_key
      return False
    case 108:
      # guild_window.gd,_on_invite_button_pressed
      return False
    case 109:
      # channel_packet_handler.gd,_receive_invitation
      return False
    case 110:
      # guild_window.gd,_on_edit_ui_button_pressed
      return False
    case 111:
      # guild_stat_window.gd,set_guild_stat
      return False
    case 112:
      # guild_window.gd,_on_leave_button_pressed
      return False
    case 113:
      # player_shop_manager_window.gd,_on_create_shop_button_pressed
      return False
    case 114:
      # player_shop_manager_window.gd,open_window
      return False
    case 115:
      # player_shop_manager_window.gd,_on_close_shop_button_pressed
      return False
    case 116:
      # player_shop_manager_window.gd,_on_update_shop_message_button_pressed
      return False
    case 118:
      # housing_manager_window.gd,open_window
      return False
    case 119:
      # housing_manager_window.gd,send_edit_permission_update
      return False
    case 120:
      # housing_manager_window.gd,send_enter_permission_update
      return False
    case 122:
      # inventory_window.gd,window_middle_clicked
      return False
    case 123:
      # storage_window.gd,window_middle_clicked
      return False
    case 124:
      # research_window_info.gd,request_monster_info
      return False
    case 125:
      # inventory_item_slot.gd,use
      return False
    case 127:
      # housing_manager_window.gd,_on_exit_housing_button_pressed
      return False
    case 128:
      # client.gd,send_channel_initial_packet
      return False
    case 129:
      # channel_info.gd,_on_ui_button_pressed
      return False
    case 130:
      # party_options_window.gd,open_window
      return False
    case 131:
      # party_options_window.gd,send_item_sharing_options_update
      return False
    case 132:
      # trading_window.gd,_on_money_button_pressed
      return False
    case 133:
      # multiple,multiple
      return False
    case 134:
      # trading_window.gd,multiple
      return False
    case 135:
      # character_info_window.gd,_on_request_trade_button_pressed
      return False
    case 136:
      # channel_packet_handler.gd,_receive_invitation
      return False
    case 137:
      # trading_window.gd,close_window
      return False
    case 138:
      # guild_emblem_edit_window.gd,_on_done_ui_button_pressed
      return False
    case 139:
      # quest_window.gd,request_quest_details
      return False
    case 140:
      # quest_window.gd,_on_complete_ui_button_pressed
      return False
    case 141:
      # quest_window.gd,request_quest_list
      return False
    case 142:
      # quest_helper_container.gd,request_pinned_quest_status
      return False
    case 143:
      # guild_window.gd,_on_add_funds_ui_button_pressed
      return False
    case 144:
      # guild_funds_window.gd,_on_purchase_ui_button_pressed
      return False
    case 144:
      # guild_funds_window.gd,_on_deactivate_ui_button_pressed
      return False
    case 145:
      # guild_funds_window.gd,request_perk_info
      return False
    case 146:
      # guild_funds_window.gd,request_perk_list
      return False
    case 147:
      # guild_window.gd,_on_edit_ui_button_pressed
      return False
    case 148:
      # multiple,multiple
      return False
    case 149:
      # shop_search_window.gd,_go_button_pressed
      return False
    case 150:
      # steam_manager.gd,initiate_microtransaction
      return False
    case 151:
      # steam_manager.gd,_on_microtransaction_auth_response
      return False
    case 152:
      # inventory_item_slot.gd,sell_item_to_npc_shop
      return False
    case 153:
      # world_map_window.gd,do_world_map_search
      return False
    case 154:
      # world_map_window.gd,select_map
      return False
    case 155:
      # world_map_window.gd,request_world_map_overview
      return False
    case 157:
      # discord_manager.gd,_on_activity_join
      return False
    case 158:
      # skill_window.gd,send_skill_upgrade_action
      return False
    case 159:
      # skill_window.gd,request_skill_tree_overview
      return False
    case 160:
      # change_channel_window.gd,request_channel_list
      return False
    case 161:
      # world_map_window.gd,_on_warp_button_pressed
      return False
    case 162:
      # gathering_node.gd,_process
      return False
    case 163:
      # buddy_window.gd,request_buddy_list
      return False
    case 164:
      # buddy_window.gd,_on_button_invite_pressed
      return False
    case 165:
      # buddy_window.gd,message_server_buddy_action
      return False
    case 166:
      # channel_packet_handler.gd,_receive_invitation
      return False
    case 167:
      # auction_house_window.gd,send_search_request
      return False
    case 168:
      # auction_house_window.gd,_on_buy_button_pressed
      return False
    case 169:
      # auction_house_window.gd,_on_list_item_button_pressed
      return False
    case 170:
      # auction_house_window.gd,request_ah_information
      return False
    case 171:
      # auction_house_my_listing_entry.gd,_on_cancel_button_pressed
      return False
    case 172:
      # auction_house_window.gd,send_price_history_request
      return False
    case 173:
      # buff_slot.gd,remove_buff_manually
      return False
    case 174:
      # character_info_window.gd,send_fame_request
      return False
    case 175:
      # auction_house_window.gd,select_item_to_list
      return False
    case 176:
      # admin_window.gd,request_player_list
      return False
    case 177:
      # admin_window_player_info.gd,_on_ui_button_pressed
      return False
    case 178:
      # admin_window_player_info.gd,_on_ui_button_pressed
      return False
    case 178:
      # admin_window.gd,submit_manager_player_name
      return False
    case 179:
      # admin_manager_item_slot.gd,_on_ui_button_pressed
      return False
    case 180:
      # appearance_editor_window.gd,_on_done_button_pressed
      return False
    case 181:
      # skill_window.gd,multiple
      return False
    case 182:
      # skill_window.gd,_on_reset_skills_button_pressed
      return False
    case 183:
      # cash_shop_window.gd,_on_history_button_pressed
      return False
    case 184:
      # entity.gd,set_in_water
      return False
    case 185:
      # macro_slot.gd,send_macro_settings_to_server
      return False

def handle_as_ping(packet:Packet) -> bool:
  packet.packet_addendum = "Ping!"
  return True