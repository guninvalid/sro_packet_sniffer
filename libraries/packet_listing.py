SERVER_PACKET_LIST = {
    1: {
        "desc": "Initial packet", 
        #"handler": _init_packet
    }, 
    2: {
        "desc": "Character position", 
        #"handler": _character_position_received
    }, 
    4: {
        "desc": "Character despawn", 
        #"handler": _character_despawn
    }, 
    5: {
        "desc": "Character spawn", 
        #"handler": _character_spawn
    }, 
    6: {
        "desc": "Character key pressed", 
        #"handler": _character_key_action
    }, 
    11: {
        "desc": "Character release skill", 
        #"handler": _character_release_skill
    }, 
    12: {
        "desc": "Chat message received", 
        #"handler": _chat_message_received
    }, 
    13: {
        "desc": "Enemy position update", 
        #"handler": _enemy_position_update
    }, 
    14: {
        "desc": "Enemy spawn", 
        #"handler": _enemy_spawn
    }, 
    15: {
        "desc": "Enemy death", 
        #"handler": _enemy_death
    }, 
    16: {
        "desc": "Enemy take damage", 
        #"handler": _enemy_take_damage
    }, 
    17: {
        "desc": "Player HP", 
        #"handler": _player_hp_update
    }, 
    18: {
        "desc": "Player take damage", 
        #"handler": _player_take_damage
    }, 
    19: {
        "desc": "EXP update", 
        #"handler": _player_exp_update
    }, 
    20: {
        "desc": "Set character (player) name", 
        #"handler": _set_character_name
    }, 
    21: {
        "desc": "Attributes update", 
        #"handler": _attribute_update
    }, 
    22: {
        "desc": "Inventory slot", 
        #"handler": _recieve_inventory_slot
    }, 
    23: {
        "desc": "Successful inventory item swap", 
        #"handler": _inventory_swap
    }, 
    24: {
        "desc": "Drop creation", 
        #"handler": _item_drop_created
    }, 
    26: {
        "desc": "Drop pick up success", 
        #"handler": _item_drop_picked_up
    }, 
    27: {
        "desc": "Destroy drop", 
        #"handler": _item_drop_destroyed
    }, 
    28: {
        "desc": "Money update", 
        #"handler": _receive_money_update
    }, 
    29: {
        "desc": "Enemy temporary animation (temporarily use attack anim/frame?)", 
        #"handler": _enemy_attack_animation
    }, 
    30: {
        "desc": "New enemy projectile", 
        #"handler": _enemy_projectile
    }, 
    31: {
        "desc": "Set position", 
        #"handler": _set_player_position
    }, 
    32: {
        "desc": "Set key count (Not used anymore)", 
        #"handler": null
    }, 
    33: {
        "desc": "Ping response received", 
        #"handler": _receive_ping
    }, 
    34: {
        "desc": "NPC shop item list update (not used anymore I think)", 
        #"handler": _NPC_shop_item_list
    }, 
    37: {
        "desc": "Player knockback", 
        #"handler": _player_knockback
    }, 
    38: {
        "desc": "Player run stat set", 
        #"handler": _character_run_stat
    }, 
    39: {
        "desc": "Player jump stat set", 
        #"handler": _character_jump_stat
    }, 
    41: {
        "desc": "Login successful", 
        #"handler": _login_success
    }, 
    42: {
        "desc": "Login failed", 
        #"handler": _login_fail
    }, 
    43: {
        "desc": "Enemy AI update (seems to not be used ever?)", 
        #"handler": null
    }, 
    44: {
        "desc": "Drop 'belongs to' info", 
        #"handler": _drop_belongsto_update
    }, 
    45: {
        "desc": "Ping (not needed)", 
        #"handler": null
    }, 
    46: {
        "desc": "Character info for character info UI (right click on player)", 
        #"handler": _character_inspected_info_received
    }, 
    47: {
        "desc": "Party list info update", 
        #"handler": _party_list_ui_update
    }, 
    48: {
        "desc": "Enemy HP received", 
        #"handler": _enemy_hp_received
    }, 
    49: {
        "desc": "Skill list update", 
        #"handler": _skills_update
    }, 
    50: {
        "desc": "Player MP", 
        #"handler": _player_mp_update
    }, 
    51: {
        "desc": "Player skill animation / use skill", 
        #"handler": _skill_used
    }, 
    52: {
        "desc": "Map data/info", 
        #"handler": _receive_map_data
    }, 
    53: {
        "desc": "Map portal", 
        #"handler": _create_map_portal
    }, 
    54: {
        "desc": "Map cleanup", 
        #"handler": _map_cleanup
    }, 
    56: {
        "desc": "Player buff status (active or not)", 
        #"handler": _receive_buff_status
    }, 
    57: {
        "desc": "Music", 
        #"handler": _music_set
    }, 
    58: {
        "desc": "Player set Y velocity", 
        #"handler": null
    }, 
    60: {
        "desc": "LEVEL UP! effect", 
        #"handler": _level_up_effect
    }, 
    61: {
        "desc": "Enemy hit by element particle effect", 
        #"handler": _elemental_hit_effect
    }, 
    62: {
        "desc": "Enemy exclamation point effect", 
        #"handler": _enemy_exclamation_effect
    }, 
    63: {
        "desc": "Player level", 
        #"handler": _character_level_received
    }, 
    64: {
        "desc": "Hotkey", 
        #"handler": _receive_hotkey
    }, 
    65: {
        "desc": "Scenery objects", 
        #"handler": _scenery_object_create
    }, 
    66: {
        "desc": "Map background", 
        #"handler": _map_background
    }, 
    67: {
        "desc": "Player chatbox message", 
        #"handler": _player_chat_message_received
    }, 
    68: {
        "desc": "Player is typing", 
        #"handler": _player_is_typing_received
    }, 
    69: {
        "desc": "Map light amount", 
        #"handler": _map_light_amount
    }, 
    70: {
        "desc": "Interactive object create", 
        #"handler": _map_object_create
    }, 
    71: {
        "desc": "Minigame start", 
        #"handler": _minigame_start
    }, 
    72: {
        "desc": "Interactive object availability update", 
        #"handler": _map_object_availability_update
    }, 
    73: {
        "desc": "Use herbalism (not used)", 
        #"handler": null
    }, 
    74: {
        "desc": "Use mining (not used)", 
        #"handler": null
    }, 
    76: {
        "desc": "Crafting success effect", 
        #"handler": _crafting_success_effect
    }, 
    77: {
        "desc": "+HP text effect", 
        #"handler": _add_hp_text_effect
    }, 
    78: {
        "desc": "Gathering minigame results + complete (unused)", 
        #"handler": null
    }, 
    79: {
        "desc": "Skill level up text", 
        #"handler": _skill_level_up_effect
    }, 
    80: {
        "desc": "Skill add EXP text", 
        #"handler": _skill_side_chat_exp
    }, 
    81: {
        "desc": "Equipment slot update", 
        #"handler": _equipment_slot_update
    }, 
    82: {
        "desc": "Nova effect", 
        #"handler": _nova_circle
    }, 
    83: {
        "desc": "Gravity well node creation", 
        #"handler": _gravity_well_node
    }, 
    84: {
        "desc": "Skill circle destroyed", 
        #"handler": _skill_node_destroyed
    }, 
    85: {
        "desc": "Ranking info", 
        #"handler": _ranking_info
    }, 
    86: {
        "desc": "Player shop items", 
        #"handler": _player_shop_items
    }, 
    87: {
        "desc": "Player shop creation", 
        #"handler": _player_shop_create
    }, 
    88: {
        "desc": "Player shop description changed", 
        #"handler": _player_shop_description_changed
    }, 
    89: {
        "desc": "Player shop deleted", 
        #"handler": _player_shop_delete
    }, 
    90: {
        "desc": "Crafting recipe list", 
        #"handler": _crafting_recipe_list
    }, 
    91: {
        "desc": "Crafting recipe materials list", 
        #"handler": _crafting_recipe_materials_list
    }, 
    92: {
        "desc": "Item dying completed (not used)", 
        #"handler": null
    }, 
    93: {
        "desc": "Map health (not used)", 
        #"handler": null
    }, 
    94: {
        "desc": "Receive enemy dark", 
        #"handler": null
    }, 
    95: {
        "desc": "Alert message", 
        #"handler": _message_box_ok
    }, 
    96: {
        "desc": "Guild battle guild list", 
        #"handler": _guild_battle_points_list
    }, 
    97: {
        "desc": "Guild battle stats", 
        #"handler": _guild_battle_stats
    }, 
    98: {
        "desc": "Player guild name", 
        #"handler": _player_guild_name
    }, 
    99: {
        "desc": "Guild stats", 
        #"handler": _guild_window_stats
    }, 
    100: {
        "desc": "Guild members list", 
        #"handler": _guild_window_members
    }, 
    101: {
        "desc": "Guild maps owned list", 
        #"handler": _guild_window_maps
    }, 
    102: {
        "desc": "Water set/update", 
        #"handler": _set_water
    }, 
    103: {
        "desc": "Show death screen", 
        #"handler": _handle_death_transition
    }, 
    104: {
        "desc": "Map object opened / Set chest to opened sprite", 
        #"handler": _map_object_opened
    }, 
    105: {
        "desc": "Gem upgrade success/fail effect", 
        #"handler": _gem_upgrade_success_fail_effect
    }, 
    106: {
        "desc": "Map dungeon data", 
        #"handler": _dungeon_map_data
    }, 
    107: {
        "desc": "You have been banned message", 
        #"handler": _banned
    }, 
    108: {
        "desc": "Center message", 
        #"handler": _center_message
    }, 
    109: {
        "desc": "Reaperfish attack state update", 
        #"handler": _reaperfish_attack_state_update
    }, 
    110: {
        "desc": "Reaperfish lunge attack (not used)", 
        #"handler": null
    }, 
    111: {
        "desc": "Reaperfish shoot attack (not used)", 
        #"handler": null
    }, 
    112: {
        "desc": "Storage item slot update", 
        #"handler": _storage_slot_item_update
    }, 
    113: {
        "desc": "Storage info", 
        #"handler": _storage_info
    }, 
    114: {
        "desc": "Earthquake sound", 
        #"handler": _earthquake_sound
    }, 
    115: {
        "desc": "Receive party member list info", 
        #"handler": _receive_party_member_list
    }, 
    116: {
        "desc": "Clear party member list info", 
        #"handler": _clear_party_member_list
    }, 
    117: {
        "desc": "Invitation to party/guild/trade/buddy/etc", 
        #"handler": _receive_invitation
    }, 
    118: {
        "desc": "Update individual skill (defunct)", 
        #"handler": null
    }, 
    119: {
        "desc": "Healing node creation", 
        #"handler": _healing_node
    }, 
    120: {
        "desc": "Set one terrain block on map", 
        #"handler": _update_map_terrain_block
    }, 
    121: {
        "desc": "Game time clock", 
        #"handler": _set_game_time
    }, 
    122: {
        "desc": "Player gathering state", 
        #"handler": _character_gathering_state
    }, 
    123: {
        "desc": "Night time start", 
        #"handler": _night_time_start
    }, 
    124: {
        "desc": "Bug position packet", 
        #"handler": _bug_position_update
    }, 
    125: {
        "desc": "Bug spawn packet", 
        #"handler": _bug_spawn
    }, 
    126: {
        "desc": "Bug destroy packet", 
        #"handler": _bug_destroy
    }, 
    127: {
        "desc": "Receive buff node", 
        #"handler": null
    }, 
    128: {
        "desc": "Destroy buff node", 
        #"handler": null
    }, 
    129: {
        "desc": "Fishing status", 
        #"handler": _character_fishing_status
    }, 
    130: {
        "desc": "Fishing trigger", 
        #"handler": _fishing_trigger
    }, 
    131: {
        "desc": "Interactive object discovery FX", 
        #"handler": _map_object_discovery_fx
    }, 
    132: {
        "desc": "Interactive object destroy", 
        #"handler": _map_object_destroy
    }, 
    133: {
        "desc": "Create aura", 
        #"handler": null
    }, 
    134: {
        "desc": "Destroy aura", 
        #"handler": null
    }, 
    135: {
        "desc": "Grapple hook launch", 
        #"handler": _grapple_hook_launch
    }, 
    136: {
        "desc": "Grapple hook touch", 
        #"handler": _grapple_hook_touch
    }, 
    137: {
        "desc": "Search skill result", 
        #"handler": _search_skill_result
    }, 
    138: {
        "desc": "Interactive object name", 
        #"handler": _map_object_name
    }, 
    139: {
        "desc": "Interactive object state", 
        #"handler": _map_object_state
    }, 
    140: {
        "desc": "Create/destroy light for player", 
        #"handler": _character_light
    }, 
    141: {
        "desc": "Set aura fuel required", 
        #"handler": null
    }, 
    142: {
        "desc": "Destroy scenery object", 
        #"handler": _scenery_object_destroy
    }, 
    143: {
        "desc": "Block health update", 
        #"handler": _block_health_update
    }, 
    144: {
        "desc": "Night reaper slash attack (not used anymore)", 
        #"handler": null
    }, 
    145: {
        "desc": "Clear building mode current selected block", 
        #"handler": _build_mode_clear_selected_item
    }, 
    146: {
        "desc": "Clear all portals on map", 
        #"handler": _clear_map_portals
    }, 
    147: {
        "desc": "Player charged element", 
        #"handler": _character_element_active
    }, 
    148: {
        "desc": "Altar options (not used)", 
        #"handler": null
    }, 
    149: {
        "desc": "Turn on world reset timer (not used)", 
        #"handler": null
    }, 
    150: {
        "desc": "Turn off world reset timer (not used)", 
        #"handler": null
    }, 
    151: {
        "desc": "Player rank info", 
        #"handler": _player_rank_received
    }, 
    152: {
        "desc": "Tamed monster update", 
        #"handler": null
    }, 
    153: {
        "desc": "Terrain chunk", 
        #"handler": _receive_map_terrain_chunk
    }, 
    154: {
        "desc": "Plant EXP udpate (not used)", 
        #"handler": null
    }, 
    155: {
        "desc": "Tamed monster list", 
        #"handler": null
    }, 
    156: {
        "desc": "Tamed monster info", 
        #"handler": null
    }, 
    157: {
        "desc": "Tamed monster level up text", 
        #"handler": null
    }, 
    158: {
        "desc": "Hiding monster hide status (not used anymore)", 
        #"handler": null
    }, 
    159: {
        "desc": "Tamed monster HP and MP update", 
        #"handler": null
    }, 
    160: {
        "desc": "Enemy MP update", 
        #"handler": _enemy_mp_received
    }, 
    161: {
        "desc": "Enemy HP and MP full setter", 
        #"handler": _enemy_hp_mp_received
    }, 
    162: {
        "desc": "Enemy size modifier", 
        #"handler": _enemy_size_received
    }, 
    163: {
        "desc": "Player link data", 
        #"handler": _characters_linked
    }, 
    164: {
        "desc": "Interactive object position update", 
        #"handler": _map_object_position_update
    }, 
    165: {
        "desc": "Open beginner skill choice UI (not used)", 
        #"handler": null
    }, 
    166: {
        "desc": "Alert message from server with restart", 
        #"handler": null
    }, 
    168: {
        "desc": "NPC dialogue box", 
        #"handler": _npc_dialogue_box
    }, 
    169: {
        "desc": "Player set premium", 
        #"handler": null
    }, 
    171: {
        "desc": "Global skill cooldown", 
        #"handler": _global_skill_cooldown_received
    }, 
    172: {
        "desc": "Side chat box message received", 
        #"handler": _side_chat_message_received
    }, 
    173: {
        "desc": "Done loading map", 
        #"handler": _done_loading_map
    }, 
    174: {
        "desc": "Reset UI positions", 
        #"handler": _reset_ui_command
    }, 
    175: {
        "desc": "Player death", 
        #"handler": _character_death
    }, 
    176: {
        "desc": "Admin center message", 
        #"handler": null
    }, 
    177: {
        "desc": "Warp particle", 
        #"handler": _warp_particle
    }, 
    178: {
        "desc": "Create player damage projectile", 
        #"handler": _player_damage_projectile
    }, 
    180: {
        "desc": "Enemy special effect", 
        #"handler": _enemy_special_effect
    }, 
    182: {
        "desc": "Medishot effect", 
        #"handler": _medishot_effect
    }, 
    183: {
        "desc": "Set skill cooldown", 
        #"handler": _set_skill_cooldown
    }, 
    184: {
        "desc": "Set player PVP status", 
        #"handler": null
    }, 
    185: {
        "desc": "Create test particle at point", 
        #"handler": _test_particle_at_point
    }, 
    186: {
        "desc": "Toggle build mode", 
        #"handler": _build_tool_mode_toggle
    }, 
    187: {
        "desc": "Create line particle", 
        #"handler": _line_effect_create
    }, 
    188: {
        "desc": "Open edit / inspect object menu", 
        #"handler": _inspect_map_object
    }, 
    190: {
        "desc": "Create enemy damage object", 
        #"handler": _enemy_damage_object
    }, 
    191: {
        "desc": "Enemy hurt animation (knockback)", 
        #"handler": _enemy_hurt_animation
    }, 
    192: {
        "desc": "Emote create", 
        #"handler": _emote_create
    }, 
    193: {
        "desc": "Guild creation cost", 
        #"handler": _guild_creation_cost
    }, 
    194: {
        "desc": "Drop position update", 
        #"handler": _item_drop_position_update
    }, 
    195: {
        "desc": "Build mode range", 
        #"handler": _build_mode_range
    }, 
    196: {
        "desc": "Research data update", 
        #"handler": _research_update
    }, 
    197: {
        "desc": "Receive instrument note", 
        #"handler": _instrument_note
    }, 
    198: {
        "desc": "Ready instrument", 
        #"handler": _instrument_ready
    }, 
    199: {
        "desc": "Receive housing info", 
        #"handler": _housing_portal_info
    }, 
    200: {
        "desc": "Add velocity to player", 
        #"handler": _character_add_velocity
    }, 
    201: {
        "desc": "Server run/jump mod", 
        #"handler": _server_run_jump_multipliers_update
    }, 
    202: {
        "desc": "Amount of unread mail", 
        #"handler": _amount_of_unread_mail
    }, 
    203: {
        "desc": "Mail list", 
        #"handler": _mail_list
    }, 
    204: {
        "desc": "Mail entry details", 
        #"handler": _mail_entry_details
    }, 
    205: {
        "desc": "Successful mail delete", 
        #"handler": _mail_deleted
    }, 
    206: {
        "desc": "Player name color", 
        #"handler": _player_name_color
    }, 
    207: {
        "desc": "Cash shop update", 
        #"handler": _cash_shop_update
    }, 
    208: {
        "desc": "Damage set up", 
        #"handler": null
    }, 
    209: {
        "desc": "New encryption key requested", 
        #"handler": _encryption_key_requested
    }, 
    210: {
        "desc": "Notice from server that we are switching to newest encryption key", 
        #"handler": _encryption_key_update
    }, 
    211: {
        "desc": "Effect on player", 
        #"handler": _effect_on_player
    }, 
    212: {
        "desc": "Christmas event status (not used atm)", 
        #"handler": null
    }, 
    213: {
        "desc": "Weather", 
        #"handler": _weather
    }, 
    214: {
        "desc": "Lightning strike", 
        #"handler": _lightning_strike
    }, 
    215: {
        "desc": "Dungeon event", 
        #"handler": _dungeon_event
    }, 
    216: {
        "desc": "Set countdown timer", 
        #"handler": _countdown_timer
    }, 
    217: {
        "desc": "Ok message box", 
        #"handler": _message_box_ok
    }, 
    218: {
        "desc": "Add/remove enemy buff", 
        #"handler": _enemy_buff
    }, 
    219: {
        "desc": "Enemy specific animation on", 
        #"handler": _enemy_specific_animation
    }, 
    220: {
        "desc": "Enemy specific animation off", 
        #"handler": _enemy_specific_animation_stop
    }, 
    221: {
        "desc": "Connect with string for puppet reaper", 
        #"handler": _puppet_reaper_string
    }, 
    222: {
        "desc": "Remove specific portal", 
        #"handler": _delete_map_portal
    }, 
    223: {
        "desc": "Clear all interactive objects", 
        #"handler": _map_object_clear_all
    }, 
    224: {
        "desc": "Memory create", 
        #"handler": null
    }, 
    225: {
        "desc": "Play SFX at location", 
        #"handler": _play_sfx_at_location
    }, 
    226: {
        "desc": "Play SFX (general)", 
        #"handler": _play_sfx_general
    }, 
    227: {
        "desc": "Player shop manager update", 
        #"handler": _player_shop_manager_update
    }, 
    228: {
        "desc": "Housing manager UI permission info", 
        #"handler": _housing_manager_permission_info
    }, 
    229: {
        "desc": "Monster research specific info", 
        #"handler": _monster_research_info
    }, 
    230: {
        "desc": "Create firework", 
        #"handler": _firework_create
    }, 
    231: {
        "desc": "Create indicator at point", 
        #"handler": _indicator_create
    }, 
    232: {
        "desc": "Jump warp particle", 
        #"handler": _jump_warp_particle
    }, 
    233: {
        "desc": "Player shop display items", 
        #"handler": _player_shop_update_display_items
    }, 
    234: {
        "desc": "Dungeon summary", 
        #"handler": _dungeon_summary
    }, 
    235: {
        "desc": "", 
        #"handler": null
    }, 
    236: {
        "desc": "Channel List", 
        #"handler": _channel_list
    }, 
    237: {
        "desc": "Change channel", 
        #"handler": _change_channel
    }, 
    238: {
        "desc": "Party options", 
        #"handler": _party_options_received
    }, 
    239: {
        "desc": "Trade start", 
        #"handler": _trade_start
    }, 
    240: {
        "desc": "Trade end", 
        #"handler": _trade_end
    }, 
    241: {
        "desc": "Trade player done", 
        #"handler": _trade_player_done
    }, 
    242: {
        "desc": "Trade money updated", 
        #"handler": _trade_money_updated
    }, 
    243: {
        "desc": "Trade items updated", 
        #"handler": _trade_items_updated
    }, 
    244: {
        "desc": "Trade player info", 
        #"handler": _trade_player_info
    }, 
    245: {
        "desc": "Skill points", 
        #"handler": _skill_points
    }, 
    246: {
        "desc": "Quest list", 
        #"handler": _quest_list
    }, 
    247: {
        "desc": "Quest details", 
        #"handler": _quest_details
    }, 
    248: {
        "desc": "Quest status", 
        #"handler": _quest_status
    }, 
    249: {
        "desc": "Quest progress notification", 
        #"handler": _quest_progress_notification
    }, 
    250: {
        "desc": "Pin quest", 
        #"handler": _pin_quest
    }, 
    251: {
        "desc": "Quest complete effect", 
        #"handler": _quest_complete_effect
    }, 
    252: {
        "desc": "Guild perk info", 
        #"handler": _guild_perk_info
    }, 
    253: {
        "desc": "Guild perk list", 
        #"handler": _guild_perk_list
    }, 
    254: {
        "desc": "Research overview", 
        #"handler": _research_overview
    }, 
    255: {
        "desc": "NPC dialogue box ended", 
        #"handler": _npc_dialogue_box_ended
    }, 
    256: {
        "desc": "Shop search results", 
        #"handler": _shop_search_results
    }, 
    257: {
        "desc": "NPC dialogue box closed", 
        #"handler": _npc_dialogue_box_close
    }, 
    258: {
        "desc": "Dialogue music", 
        #"handler": _dialogue_music_set
    }, 
    259: {
        "desc": "Inventory resize", 
        #"handler": _inventory_resize
    }, 
    260: {
        "desc": "Steam achievement set", 
        #"handler": _steam_achievement_set
    }, 
    261: {
        "desc": "World map search results", 
        #"handler": _world_map_search_results
    }, 
    262: {
        "desc": "World map map information", 
        #"handler": _world_map_map_information
    }, 
    263: {
        "desc": "World map overview", 
        #"handler": _world_map_overview
    }, 
    264: {
        "desc": "Skill window skill information", 
        #"handler": _skill_window_skill_information
    }, 
    265: {
        "desc": "Skill window skill tree overview", 
        #"handler": _skill_window_skill_tree_overview
    }, 
    266: {
        "desc": "NPC Quest Icon Info", 
        #"handler": _NPC_quest_icon_info
    }, 
    267: {
        "desc": "Gathering search started", 
        #"handler": _gathering_search_started
    }, 
    268: {
        "desc": "Buddy list received", 
        #"handler": _receive_buddy_list
    }, 
    269: {
        "desc": "Character appearance received", 
        #"handler": _character_appearance
    }, 
    270: {
        "desc": "Auction House Overview", 
        #"handler": _auction_house_overview
    }, 
    271: {
        "desc": "Auction House Search Result", 
        #"handler": _auction_house_search_result
    }, 
    272: {
        "desc": "Auction House My Listings", 
        #"handler": _auction_house_my_listings
    }, 
    273: {
        "desc": "Auction House Price History", 
        #"handler": _auction_house_price_history
    }, 
    274: {
        "desc": "Full Modifier List", 
        #"handler": _full_modifier_list
    }, 
    275: {
        "desc": "Auction House Item Recent Prices", 
        #"handler": _auction_house_recent_item_prices
    }, 
    276: {
        "desc": "Admin window player list", 
        #"handler": _admin_window_player_list
    }, 
    277: {
        "desc": "Creating resource database with skills", 
        #"handler": _create_skill_database
    }, 
    278: {
        "desc": "Admin window manage player info", 
        #"handler": _admin_window_manage_player_info
    }, 
    279: {
        "desc": "Open Appearance Editor Window", 
        #"handler": _open_appearance_editor_window
    }, 
    280: {
        "desc": "Skill EXP update", 
        #"handler": _skill_exp_update
    }, 
    281: {
        "desc": "Character stop grappling", 
        #"handler": _character_stop_grappling
    }, 
    282: {
        "desc": "Cash shop purchase history", 
        #"handler": _cash_shop_purchase_history
    }, 
    283: {
        "desc": "Macros received", 
        #"handler": _macros_received
    }, 
}

CLIENT_PACKET_LIST = 	{1: {"desc": "multiple,multiple",},
	2: {"desc": "multiple,multiple",},
	3: {"desc": "player_effect.gd,just_released",},
	7: {"desc": "chatbox.gd,_on_chat_entry_line_edit_text_submitted",},
	8: {"desc": "chatbox.gd,_on_chat_entry_line_edit_text_changed",},
	9: {"desc": "attribute_window.gd,send_attribute_add_point_packet",},
	10: {"desc": "mouse_item.gd,try_inventory_swap",},
	12: {"desc": "inventory_item_slot.gd,use",},
	14: {"desc": "client.gd,send_ping",},
	15: {"desc": "player_shop_item_listing.gd,_on_buy_button_pressed",},
	19: {"desc": "player.gd,_on_hurtbox_hurt",},
	21: {"desc": "world.gd,clean_up_map",},
	23: {"desc": "client.gd,send_login",},
	24: {"desc": "multiple,multiple",},
	25: {"desc": "multiple,multiple",},
	26: {"desc": "title_screen_ui.gd,_on_character_create_button_pressed",},
	27: {"desc": "title_screen_ui.gd,_on_name_availability_check_button_pressed",},
	28: {"desc": "multiple,multiple",},
	29: {"desc": "title_screen_ui.gd,request_character_creator_information",},
	30: {"desc": "enemy.gd,_on_hurtbox_hurt",},
	31: {"desc": "Skill.gd,send_skill_packet",},
	32: {"desc": "portal.gd,_process",},
	33: {"desc": "hot_slot.gd,send_hotslot_data_to_server",},
	34: {"desc": "map_object.gd,use_object",},
	35: {"desc": "crafting_window.gd,_on_craft_button_pressed",},
	37: {"desc": "Minigame.gd,end_minigame",},
	38: {"desc": "inventory_item_slot.gd,use",},
	38: {"desc": "mouse_item.gd,multiple",},
	39: {"desc": "multiple,multiple",},
	40: {"desc": "ranking_window.gd,request_ranking_info_for_option_menu_index",},
	41: {"desc": "player.gd,check_out_of_bounds",},
	42: {"desc": "player_shop_item_listing.gd,_on_buy_button_pressed",},
	44: {"desc": "player_shop.gd,use_object",},
	45: {"desc": "crafting_window.gd,request_crafting_recipes",},
	46: {"desc": "crafting_window.gd,request_crafting_recipe_materials",},
	48: {"desc": "guild_window.gd,_on_create_guild_button_pressed",},
	49: {"desc": "guild_window.gd,request_guild_info",},
	51: {"desc": "death_screen.gd,_on_death",},
	53: {"desc": "dungeon_entrance_window.gd,_on_enter_button_pressed",},
	54: {"desc": "player.gd,_on_hurtbox_hurt",},
	55: {"desc": "storage_window.gd,request_current_storage_page_items",},
	56: {"desc": "storage_window.gd,withdraw_item",},
	57: {"desc": "storage_window.gd,deposit_item",},
	58: {"desc": "mouse_item.gd,try_storage_swap",},
	59: {"desc": "party_window.gd,_on_button_invite_pressed",},
	59: {"desc": "character_info_window.gd,_on_add_to_party_button_pressed",},
	60: {"desc": "party_window.gd,message_server_party_action",},
	61: {"desc": "party_window.gd,request_party_member_list",},
	62: {"desc": "channel_packet_handler.gd,_receive_invitation",},
	63: {"desc": "bug.gd,_on_hurtbox_hurt",},
	64: {"desc": "fishing_bobber.gd,multiple",},
	65: {"desc": "fishing_trigger.gd,multiple",},
	67: {"desc": "grapple_projectile.gd,_on_body_entered",},
	68: {"desc": "character.gd,multiple",},
	69: {"desc": "building_tool.gd,handle_right_click",},
	70: {"desc": "Minigame.gd,early_quit",},
	71: {"desc": "building_tool.gd,handle_left_click",},
	84: {"desc": "npc_dialogue_window.gd,cancel_dialogue",},
	85: {"desc": "player_death_effect.gd,_ready",},
	88: {"desc": "medishot_player_projectile.gd,_on_contact_made_with_ground",},
	89: {"desc": "building_tool.gd,handle_left_click",},
	90: {"desc": "building_tool.gd,handle_right_click",},
	91: {"desc": "building_tool.gd,handle_left_click",},
	92: {"desc": "map_object_inspect_window.gd,send_new_permissions_packet",},
	94: {"desc": "player.gd,do_emote",},
	95: {"desc": "unlearn_skill_window.gd,_on_enter_button_pressed",},
	96: {"desc": "instrument_window.gd,play_instrument_note",},
	97: {"desc": "multiple,multiple",},
	98: {"desc": "inventory_item_slot.gd,_process",},
	99: {"desc": "mail_window.gd,open_window",},
	100: {"desc": "mail_window.gd,set_selected_mail_id",},
	101: {"desc": "mail_window.gd,_on_delete_mail_button_pressed",},
	102: {"desc": "mail_item_slot.gd,clicked",},
	103: {"desc": "housing_portal_window.gd,_on_set_home_button_pressed",},
	104: {"desc": "inventory_item_slot.gd,use",},
	105: {"desc": "cash_shop_window_item.gd,_on_buy_button_pressed",},
	106: {"desc": "cash_shop_window.gd,open_window",},
	107: {"desc": "client.gd,new_encryption_key",},
	108: {"desc": "guild_window.gd,_on_invite_button_pressed",},
	109: {"desc": "channel_packet_handler.gd,_receive_invitation",},
	110: {"desc": "guild_window.gd,_on_edit_ui_button_pressed",},
	111: {"desc": "guild_stat_window.gd,set_guild_stat",},
	112: {"desc": "guild_window.gd,_on_leave_button_pressed",},
	113: {"desc": "player_shop_manager_window.gd,_on_create_shop_button_pressed",},
	114: {"desc": "player_shop_manager_window.gd,open_window",},
	115: {"desc": "player_shop_manager_window.gd,_on_close_shop_button_pressed",},
	116: {"desc": "player_shop_manager_window.gd,_on_update_shop_message_button_pressed",},
	118: {"desc": "housing_manager_window.gd,open_window",},
	119: {"desc": "housing_manager_window.gd,send_edit_permission_update",},
	120: {"desc": "housing_manager_window.gd,send_enter_permission_update",},
	122: {"desc": "inventory_window.gd,window_middle_clicked",},
	123: {"desc": "storage_window.gd,window_middle_clicked",},
	124: {"desc": "research_window_info.gd,request_monster_info",},
	125: {"desc": "inventory_item_slot.gd,use",},
	127: {"desc": "housing_manager_window.gd,_on_exit_housing_button_pressed",},
	128: {"desc": "client.gd,send_channel_initial_packet",},
	129: {"desc": "channel_info.gd,_on_ui_button_pressed",},
	130: {"desc": "party_options_window.gd,open_window",},
	131: {"desc": "party_options_window.gd,send_item_sharing_options_update",},
	132: {"desc": "trading_window.gd,_on_money_button_pressed",},
	133: {"desc": "multiple,multiple",},
	134: {"desc": "trading_window.gd,multiple",},
	135: {"desc": "character_info_window.gd,_on_request_trade_button_pressed",},
	136: {"desc": "channel_packet_handler.gd,_receive_invitation",},
	137: {"desc": "trading_window.gd,close_window",},
	138: {"desc": "guild_emblem_edit_window.gd,_on_done_ui_button_pressed",},
	139: {"desc": "quest_window.gd,request_quest_details",},
	140: {"desc": "quest_window.gd,_on_complete_ui_button_pressed",},
	141: {"desc": "quest_window.gd,request_quest_list",},
	142: {"desc": "quest_helper_container.gd,request_pinned_quest_status",},
	143: {"desc": "guild_window.gd,_on_add_funds_ui_button_pressed",},
	144: {"desc": "guild_funds_window.gd,_on_purchase_ui_button_pressed",},
	144: {"desc": "guild_funds_window.gd,_on_deactivate_ui_button_pressed",},
	145: {"desc": "guild_funds_window.gd,request_perk_info",},
	146: {"desc": "guild_funds_window.gd,request_perk_list",},
	147: {"desc": "guild_window.gd,_on_edit_ui_button_pressed",},
	148: {"desc": "multiple,multiple",},
	149: {"desc": "shop_search_window.gd,_go_button_pressed",},
	150: {"desc": "steam_manager.gd,initiate_microtransaction",},
	151: {"desc": "steam_manager.gd,_on_microtransaction_auth_response",},
	152: {"desc": "inventory_item_slot.gd,sell_item_to_npc_shop",},
	153: {"desc": "world_map_window.gd,do_world_map_search",},
	154: {"desc": "world_map_window.gd,select_map",},
	155: {"desc": "world_map_window.gd,request_world_map_overview",},
	157: {"desc": "discord_manager.gd,_on_activity_join",},
	158: {"desc": "skill_window.gd,send_skill_upgrade_action",},
	159: {"desc": "skill_window.gd,request_skill_tree_overview",},
	160: {"desc": "change_channel_window.gd,request_channel_list",},
	161: {"desc": "world_map_window.gd,_on_warp_button_pressed",},
	162: {"desc": "gathering_node.gd,_process",},
	163: {"desc": "buddy_window.gd,request_buddy_list",},
	164: {"desc": "buddy_window.gd,_on_button_invite_pressed",},
	165: {"desc": "buddy_window.gd,message_server_buddy_action",},
	166: {"desc": "channel_packet_handler.gd,_receive_invitation",},
	167: {"desc": "auction_house_window.gd,send_search_request",},
	168: {"desc": "auction_house_window.gd,_on_buy_button_pressed",},
	169: {"desc": "auction_house_window.gd,_on_list_item_button_pressed",},
	170: {"desc": "auction_house_window.gd,request_ah_information",},
	171: {"desc": "auction_house_my_listing_entry.gd,_on_cancel_button_pressed",},
	172: {"desc": "auction_house_window.gd,send_price_history_request",},
	173: {"desc": "buff_slot.gd,remove_buff_manually",},
	174: {"desc": "character_info_window.gd,send_fame_request",},
	175: {"desc": "auction_house_window.gd,select_item_to_list",},
	176: {"desc": "admin_window.gd,request_player_list",},
	177: {"desc": "admin_window_player_info.gd,_on_ui_button_pressed",},
	178: {"desc": "admin_window_player_info.gd,_on_ui_button_pressed",},
	178: {"desc": "admin_window.gd,submit_manager_player_name",},
	179: {"desc": "admin_manager_item_slot.gd,_on_ui_button_pressed",},
	180: {"desc": "appearance_editor_window.gd,_on_done_button_pressed",},
	181: {"desc": "skill_window.gd,multiple",},
	182: {"desc": "skill_window.gd,_on_reset_skills_button_pressed",},
	183: {"desc": "cash_shop_window.gd,_on_history_button_pressed",},
	184: {"desc": "entity.gd,set_in_water",},
	185: {"desc": "macro_slot.gd,send_macro_settings_to_server"}
}