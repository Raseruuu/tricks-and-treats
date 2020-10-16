init:
    image lobby_slime = "Slime_lobby.png"
    image lobby_succubus = "Succubus_lobby.png"
    image lobby_vampire = "Vampire_lobby.png"
    image lobby_kitsune = "Kitsune_lobby.png"
    image lobby_random = "Random_lobby.png"
    image lobby_empty = "Empty.png"


init python:
    global Max_Turns
    Max_Turns = 8
    global Player_count
    Player_count = 2
    global slots 
    slots = ["Random","Random","Random","Random"]
    global current_select
    current_select = -1
    
    slot_position_4 = []
screen Lobby_single_player:
    for each in range(0,Player_count):
        imagebutton:
            idle slots[each]+"_lobby.png"
            insensitive slots[each]+"_lobby.png"
            hover slots[each]+"_lobby.png"
            selected_idle slots[each]+"_lobby.png"
            selected_hover slots[each]+"_lobby.png"
            action SetVariable("current_select", each), Show(Character_Selection)
            xpos 0.15 + (0.25 * each)
            ypos 0.5
            yanchor 0.5
            xanchor 0.5

    if Player_count < 3:
        imagebutton:
            yanchor 0.5
            xanchor 0.5
            xpos 0.15 + (0.25 * Player_count)
            ypos 0.5
            idle "Empty.png"
            insensitive "Empty.png"
            hover "Empty.png"
            selected_idle "Empty.png"
            selected_hover "Empty.png"
            action NullAction()