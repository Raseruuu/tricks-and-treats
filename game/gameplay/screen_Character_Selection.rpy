
init:
    image lobby_slime = "Slime_lobby.png"
    image lobby_succubus = "Succubus_lobby.png"
    image lobby_vampire = "Vampire_lobby.png"
    image lobby_kitsune = "Kitsune_lobby.png"
    image lobby_random = "Random_lobby.png"
    image lobby_empty = "Empty.png"
    image select_vampire_img =  "sketch_vampire_small.png"
    image select_succubus_img =  "sketch_succubus_small.png"
    image select_kitsune_img =  "sketch_kitsune_small.png"
    image select_slime_img =  "sketch_slime_small.png"

transform size_changer_button:
    on idle:
        linear 0.3 zoom 0.3
    on hover:
        linear 0.3 zoom 0.4


######################################## Character_Selection ###########################################
screen Character_Selection():
    add "Black_image.png"

    imagebutton at size_changer_button:
        idle "select_kitsune_img"
        hover "select_kitsune_img"
        action Function(character_change,current_select,"Kitsune") ,Hide("Character_Selection"), Return()
        
        hovered Function(Michael, "A sheltered Girl living in the forest, desireing to share the candy she gathers with everyone.", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)
        xanchor 0.5 yanchor 1.0
        xpos 0.14 ypos 1.0

    
    imagebutton at size_changer_button:
        idle "select_succubus_img"
        hover "select_succubus_img"
        action Function(character_change,current_select,"Succubus") ,Hide("Character_Selection"), Return()
        xanchor 0.5 yanchor 1.0
        xpos .38 ypos 1.0
        
        hovered Function(Michael,"Succubus wanting to do succubus things Jroz you can change that text btw.", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)
       
    
    imagebutton at size_changer_button:
        idle "select_slime_img"
        hover "select_slime_img"
        action Function(character_change,current_select,"Slime") ,Hide("Character_Selection"), Return()
        xanchor 0.5 yanchor 1.0
        xpos 0.62 ypos 1.0
        
        hovered Function(Michael,"A slime girl interested in the occult, also easily frightened, she is here to check out the town special candy", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)

    imagebutton at size_changer_button:
        idle "select_vampire_img"
        hover "select_vampire_img"
        action Function(character_change,current_select,"Vampire") ,Hide("Character_Selection"), Return()
        xanchor 0.5 yanchor 1.0
        xpos 0.84 ypos 1.0
        
        hovered Function(Michael,"A Vampire with the goal performing a dangerous Summoning ritual the main ingredient needed? Candy. ", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)


####################################################################################################################
############################################## SINGLE PLAYER LOBBY #################################################
####################################################################################################################
screen Lobby_single_player:
    add "Black_image.png"

    textbutton "Start Game":

        
        action SetVariable("single_player_lobby_loop", False),Return()
        xpos 0.5
        ypos 0.8
        yanchor 0.5
        xanchor 0.5
        #size 1000,200


    for each in range(0,Player_count):

        

        imagebutton:
            idle slots[each]+"_lobby.png"
            insensitive slots[each]+"_lobby.png"
            hover slots[each]+"_lobby.png"
            selected_idle slots[each]+"_lobby.png"
            selected_hover slots[each]+"_lobby.png"
            action SetVariable("current_select", each), Show("Character_Selection")
            xpos 0.125 + (0.25 * each)
            ypos 0.5
            yanchor 0.5
            xanchor 0.5

        text "Ready":
            xpos 0.085 + (0.25 * each)
            ypos 0.65
            yanchor 0.5
            xanchor 0.5
            size 60
    
        add "Player ready.png":
            xpos 0.19 + (0.25 * each)
            ypos 0.63
            yanchor 0.5
            xanchor 0.5
        

    for each in range(2,Player_count):
        imagebutton:
            idle "remove button.png"
            insensitive "remove button.png"
            hover "remove button.png"
            selected_idle "remove button.png"
            selected_hover "remove button.png"
            action SetVariable("Player_count", Player_count-1)
            xpos 0.19 + (0.25 * each)
            ypos 0.3
            yanchor 0.5
            xanchor 0.5
    

    if Player_count < 4:
        imagebutton:
            yanchor 0.5
            xanchor 0.5
            xpos 0.125 + (0.25 * Player_count)
            ypos 0.5
            idle "Empty.png"
            insensitive "Empty.png"
            hover "Empty.png"
            selected_idle "Empty.png"
            selected_hover "Empty.png"
            action SetVariable("Player_count", Player_count+1)