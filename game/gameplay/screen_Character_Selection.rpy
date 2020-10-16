image select_vampire_img =  "sketch_vampire_small.png"
image select_succubus_img =  "sketch_succubus_small.png"
image select_kitsune_img =  "sketch_kitsune_small.png"
image select_slime_img =  "sketch_slime_small.png"

init python:
    Choice_nummber = 0
    def character_change(slot_number,character_name):
        global slots
        slots[slot_number] = character_name

transform size_changer_button:
    on idle:
        linear 0.3 zoom 0.3
    on hover:
        linear 0.3 zoom 0.4



screen Character_Selection():
    add "Black_image.png"

    imagebutton at size_changer_button:
        idle "select_kitsune_img"
        hover "select_kitsune_img"
        action Function(character_change,[current_select,"Kitsune"]) , Return()
        
        hovered Function(Michael, "A sheltered Girl living in the forest, desireing to share the candy she gathers with everyone.", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)
        xanchor 0.5 yanchor 1.0
        xpos 0.14 ypos 1.0

    
    imagebutton at size_changer_button:
        idle "select_succubus_img"
        hover "select_succubus_img"
        action SetVariable("Choice_nummber" , 2) , Return()
        xanchor 0.5 yanchor 1.0
        xpos .38 ypos 1.0
        
        hovered Function(Michael,"Succubus wanting to do succubus things Jroz you can change that text btw.", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)
       
    
    imagebutton at size_changer_button:
        idle "select_slime_img"
        hover "select_slime_img"
        action SetVariable("Choice_nummber" , 4) , Return()
        xanchor 0.5 yanchor 1.0
        xpos 0.62 ypos 1.0
        
        hovered Function(Michael,"A slime girl interested in the occult, also easily frightened, she is here to check out the town special candy", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)

    imagebutton at size_changer_button:
        idle "select_vampire_img"
        hover "select_vampire_img"
        action SetVariable("Choice_nummber" , 1) , Return()
        xanchor 0.5 yanchor 1.0
        xpos 0.84 ypos 1.0
        
        hovered Function(Michael,"A Vampire with the goal performing a dangerous Summoning ritual the main ingredient needed? Candy. ", False, False)
        
        unhovered Function(Michael, "Choose a character", False, False)