init python :
    map_location_prefix = "Main_MAP_things/Resized/"
init:

    image Area1_idle = map_location_prefix + "Area1_dark.png"
    image Area1_selected = map_location_prefix + "Area1_base.png"
    image Area2_idle = map_location_prefix + "Area2_dark.png"
    image Area2_selected = map_location_prefix + "Area2_base.png"
    image Area3_idle = map_location_prefix + "Area3_dark.png"
    image Area3_selected = map_location_prefix + "Area3_base.png"
    image Area4_idle = map_location_prefix + "Area4_dark.png"
    image Area4_selected = map_location_prefix + "Area4_base.png"
    image Area5_idle = map_location_prefix + "Area5_dark.png"
    image Area5_selected = map_location_prefix + "Area5_base.png"
    image Area6_idle = map_location_prefix + "Area6_dark.png"
    image Area6_selected = map_location_prefix + "Area6_base.png"
    image Area7_idle = map_location_prefix + "Area7_dark.png"
    image Area7_selected = map_location_prefix + "Area7_base.png"
    image Area8_idle = map_location_prefix + "Area8_dark.png"
    image Area8_selected = map_location_prefix + "Area8_base.png"
    image Area9_idle = map_location_prefix + "Area9_dark.png"
    image Area9_selected = map_location_prefix + "Area9_base.png"
    image Area10_idle = map_location_prefix + "Area10_dark.png"
    image Area10_selected = map_location_prefix + "Area10_base.png"
    image Area11_idle = map_location_prefix + "Area11_dark.png"
    image Area11_selected = map_location_prefix + "Area11_base.png"
    image Area12_idle = map_location_prefix + "Area12_dark.png"
    image Area12_selected = map_location_prefix + "Area12_base.png"
    image Area13_idle = map_location_prefix + "Area13_dark.png"
    image Area13_selected = map_location_prefix + "Area13_base.png"

init python:
    xds = 0.05
    yds = -0.05
    SDx = 0.81 - 0.125
    SDy = 1 - 0.11
    LDx = 0.025
    Card_x = 0.52
    Card_y = 0.94

screen Base_UI():
    
    add player_ARRAY[0].character+" "+"up left.png"  anchor(0.0,0.0) xalign 0.0 yalign 0.0

    add "golden lollipop small_thin line.png" xalign 0.125 yalign 0.08 + yds size(30,40) anchor(0.5,0.5)
    label "[player_ARRAY[0].Victory_Candy]" xalign 0.125 + LDx yalign 0.08 +yds anchor(0.5,0.5)

    add "candy corn small_thin line.png" xalign 0.125 + xds yalign 0.08 +yds size(40,40) anchor(0.5,0.5)
    label "[player_ARRAY[0].Candy_Corn]" xalign 0.125 + xds + LDx yalign 0.08 +yds anchor(0.5,0.5)

    add "candy corn small_thin line.png" xalign 0.125 yalign 0.08 size(40,40) anchor(0.5,0.5)
    label "[player_ARRAY[0].Trick_Supplies]" xalign 0.125 + LDx yalign 0.08 anchor(0.5,0.5)

    add "chocolate small_thin line.png" xalign 0.125 + xds yalign 0.08 size(50,40) anchor(0.5,0.5)
    label "[player_ARRAY[0].Chocolate]" xalign 0.125 + xds + LDx yalign 0.08 anchor(0.5,0.5)

    add "Agents_icon.png" xalign 0.125 + xds  yalign 0.135 size(50,50) anchor(0.5,0.5)
    label "[player_ARRAY[0].agent_count]" xalign 0.134 + xds + LDx yalign 0.145 anchor(0.5,0.5) 

    add "1st Turn icon.png" xalign 0.084 + xds  yalign 0.13 size(70,70) anchor(0.5,0.5)

    add "Cards_icon.png" xalign 0.2 + xds  yalign 0.03 size(100,100) anchor(0.5,0.5)
    label "0" xalign 0.19 + xds  yalign 0.06 anchor(0.5,0.5) 

    

    ###########################################################################
    add player_ARRAY[1].character+" "+"up right.png" anchor(1.0,0.0) xalign 1.0 yalign 0.0

    add "golden lollipop small_thin line.png" xalign 0.125 + SDx yalign 0.08 + yds size(30,40) anchor(0.5,0.5)
    label "[player_ARRAY[1].Victory_Candy]" xalign 0.125 + LDx + SDx yalign 0.08 +yds anchor(0.5,0.5)

    add "candy corn small_thin line.png" xalign 0.125 + xds + SDx yalign 0.08 +yds size(40,40) anchor(0.5,0.5)
    label "[player_ARRAY[1].Candy_Corn]" xalign 0.125 + xds + LDx + SDx yalign 0.08 +yds anchor(0.5,0.5)

    add "candy corn small_thin line.png" xalign 0.125 + SDx yalign 0.08 size(40,40) anchor(0.5,0.5)
    label "[player_ARRAY[1].Trick_Supplies]" xalign 0.125 + LDx + SDx yalign 0.08 anchor(0.5,0.5)

    add "chocolate small_thin line.png" xalign 0.125 + xds + SDx yalign 0.08 size(50,40) anchor(0.5,0.5)
    label "[player_ARRAY[1].Chocolate]" xalign 0.125 + xds + LDx + SDx yalign 0.08 anchor(0.5,0.5)

    add "1st Turn icon.png" xalign 0.165 + xds + SDx - 0.035  yalign 0.13 size(70,70) anchor(0.5,0.5)

    add "Agents_icon.png" xalign 0.125 + xds + SDx - 0.035   yalign 0.135 size(50,50) anchor(0.5,0.5)
    label "[player_ARRAY[1].agent_count]" xalign 0.134 + xds + LDx + SDx - 0.105         yalign 0.145 anchor(0.5,0.5) 

    add "Cards_icon.png" xalign 0.2 + xds + Card_x  yalign 0.03 size(100,100) anchor(0.5,0.5)
    label "0" xalign 0.19 + xds + Card_x  yalign 0.06 anchor(0.5,0.5) 
    
    ############################################################################
    if Player_count > 2:
        add player_ARRAY[2].character+" "+"down left.png" anchor(0.0,1.0) xalign 0.0 yalign 1.0
        

        add "golden lollipop small_thin line.png" xalign 0.125 yalign 0.08 + yds + SDy size(30,40) anchor(0.5,0.5)
        label "[player_ARRAY[2].Victory_Candy]" xalign 0.125 + LDx yalign 0.08 +yds + SDy anchor(0.5,0.5)

        add "candy corn small_thin line.png" xalign 0.125 + xds yalign 0.08 +yds + SDy size(40,40) anchor(0.5,0.5)
        label "[player_ARRAY[2].Candy_Corn]" xalign 0.125 + xds + LDx yalign 0.08 +yds + SDy anchor(0.5,0.5)

        add "candy corn small_thin line.png" xalign 0.125 yalign 0.08 + SDy size(40,40) anchor(0.5,0.5)
        label "[player_ARRAY[2].Trick_Supplies]" xalign 0.125 + LDx yalign 0.08 + SDy anchor(0.5,0.5)

        add "chocolate small_thin line.png" xalign 0.125 + xds yalign 0.08 + SDy size(50,40) anchor(0.5,0.5)
        label "[player_ARRAY[2].Chocolate]" xalign 0.125 + xds + LDx yalign 0.08 + SDy anchor(0.5,0.5)

        add "1st Turn icon.png" xalign 0.084 + xds  yalign 0.145 + SDy - 0.155 size(70,70) anchor(0.5,0.5)

        add "Agents_icon.png" xalign 0.125 + xds  yalign 0.135 + SDy - 0.155 size(50,50) anchor(0.5,0.5)
        label "[player_ARRAY[2].agent_count]" xalign 0.134 + xds + LDx yalign 0.145 + SDy - 0.17 anchor(0.5,0.5) 

        add "Cards_icon.png" xalign 0.2 + xds  yalign 0.03 + Card_y size(100,100) anchor(0.5,0.5)
        label "0" xalign 0.19 + xds  yalign Card_y anchor(0.5,0.5) 
    ############################################################################

    if Player_count > 3:
        add player_ARRAY[3].character+" "+"down right.png" anchor(1.0,1.0) xalign 1.0 yalign 1.0
    

        add "golden lollipop small_thin line.png" xalign 0.125 + SDx yalign 0.08 + yds + SDy size(30,40) anchor(0.5,0.5)
        label "[player_ARRAY[3].Victory_Candy]" xalign 0.125 + LDx + SDx yalign 0.08 +yds + SDy anchor(0.5,0.5)

        add "candy corn small_thin line.png" xalign 0.125 + xds + SDx yalign 0.08 +yds + SDy size(40,40) anchor(0.5,0.5)
        label "[player_ARRAY[3].Candy_Corn]" xalign 0.125 + xds + LDx + SDx yalign 0.08 +yds + SDy anchor(0.5,0.5)

        add "candy corn small_thin line.png" xalign 0.125 + SDx yalign 0.08 + SDy size(40,40) anchor(0.5,0.5)
        label "[player_ARRAY[3].Trick_Supplies]" xalign 0.125 + LDx + SDx yalign 0.08 + SDy anchor(0.5,0.5)

        add "chocolate small_thin line.png" xalign 0.125 + xds + SDx yalign 0.08 + SDy size(50,40) anchor(0.5,0.5)
        label "[player_ARRAY[3].Chocolate]" xalign 0.125 + xds + LDx + SDx yalign 0.08 + SDy anchor(0.5,0.5)

        add "1st Turn icon.png" xalign 0.084 + xds  yalign 0.145 + SDy - 0.155 size(70,70) anchor(0.5,0.5)

        add "Agents_icon.png" xalign 0.09 + xds + SDx  yalign 0.135 + SDy - 0.155 size(50,50) anchor(0.5,0.5)
        label "[player_ARRAY[3].agent_count]" xalign 0.03 + xds + LDx + SDx yalign 0.145 + SDy - 0.17 anchor(0.5,0.5) 

        add "Cards_icon.png" xalign 0.2 + xds + Card_x  yalign 0.03 + Card_y size(100,100) anchor(0.5,0.5)
        label "0" xalign 0.19 + xds + Card_x  yalign  Card_y  anchor(0.5,0.5) 
    

    
    

    
    
    
init python:    
    def place_agent(player,place):
        place.get_occupied(player)
        player.occupy(place)
    
#place_ARRAY = [place_1,place_2,place_3,place_4,place_5,place_6,place_7,place_8,place_9,place_10,place_11,place_12,place_13] 
screen Agent_Placement(Character):
    
    add map_location_prefix +"MAP_dark.png" 
    #add "weisses-bild.jpg"
    for each in range(1,len(place_ARRAY)+1):
        imagebutton:
            insensitive ("Area"+str(each)+"_idle")
            idle ("Area"+str(each)+"_idle")
            hover "Area"+str(each)+"_selected"
            selected_idle "Area"+str(each)+"_selected"
            selected_hover "Area"+str(each)+"_selected"
            focus_mask True
            #Actions
            if place_ARRAY[each - 1].can_be_occupied():
                action Function(place_agent,Character,place_ARRAY[each - 1]) , Return()
                hovered Function(Michael,place_ARRAY[each - 1].place_hover_text(Character), False, False)
                unhovered NullAction()
            else :
                action NullAction()
                hovered Function(Michael,place_ARRAY[each - 1].place_hover_text(Character), False, False)
                unhovered NullAction()

    label "Current TURN: [Turn]" xalign 0.5 yalign 0.05 xanchor 0.5 yanchor 0.5 
    use Base_UI
###########################################################




    