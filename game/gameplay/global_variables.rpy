init -1 python:

    # This is global Variables and Functions.
    global Turn 
    global place_ARRAY
    global Hotseat
    global current_player
    global player_ARRAY 
    Turn = 0
    #place_ARRAY = [place_1,place_2,place_3,place_4,place_5,place_6,place_7,place_8,place_9,place_10,place_11,place_12,place_13,place_14,place_15,place_16] 
    #player_ARRAY = [SwapPlayer,Player1,Player2,Player3,Player4]
    Hotseat = True

    global Max_Turns
    Max_Turns = 8
    global Player_count
    Player_count = 2
    global slots 
    slots = ["Random","Random","Random","Random"]
    global current_select
    current_select = -1
    slot_position_4 = []

    global single_player_lobby_loop 
    single_player_lobby_loop = True

    Choice_nummber = 0
    def character_change(slot_number,character_name):
        global slots
        slots[slot_number] = character_name

    