init -1 python:

    # This is global Variables and Functions.
    global Turn 
    global place_ARRAY
    global Hotseat
    global current_player
    global player_ARRAY 
    Turn = 0
    #place_ARRAY = [place_1,place_2,place_3,place_4,place_5,place_6,place_7,place_8,place_9,place_10,place_11,place_12,place_13,place_14,place_15,place_16] 
 
    Hotseat = True

    global Max_Turns
    Max_Turns = 8
    global Player_count
    Player_count = 2
    global slots #possible values "Random" "Succubus" "Slime" "Vampire" "Kitsune"
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

    global taken_characters
    taken_characters = []
    def check_character_avalible(character_name):
        if "character_name" in slots:
            return False
        else :
            return True
    import random 
    random.seed()
    def assign_via_random():
        assign_i = random.randint(1, 4)
        print("Random Value:")
        print(assign_i)
        
        if(assign_i == 1):
            if check_character_avalible("Succubus"):
                return "Succubus"
            if check_character_avalible("Slime"):
                return "Slime"
            if check_character_avalible("Vampire"):
                return "Vampire"
            if check_character_avalible("Kitsune"):
                return "Kitsune"
        if(assign_i == 2):
            if check_character_avalible("Kitsune"):
                return "Kitsune"
            if check_character_avalible("Succubus"):
                return "Succubus"
            if check_character_avalible("Slime"):
                return "Slime"
            if check_character_avalible("Vampire"):
                return "Vampire"
        if(assign_i == 3):
            if check_character_avalible("Vampire"):
                return "Vampire"
            if check_character_avalible("Kitsune"):
                return "Kitsune"
            if check_character_avalible("Succubus"):
                return "Succubus"
            if check_character_avalible("Slime"):
                return "Slime"
        if(assign_i == 4):
            if check_character_avalible("Slime"):
                return "Slime"
            if check_character_avalible("Vampire"):
                return "Vampire"
            if check_character_avalible("Kitsune"):
                return "Kitsune"
            if check_character_avalible("Succubus"):
                return "Succubus"

    