init python :
    map_location_prefix = "Main_MAP_things/Resized/"
init:
    #image Area1_idle = im.Scale("Area1_dark.png", 1920,1080)
    #image Area1_selected = im.Scale("Area1_base.png", 1920,1080)
    #image Area2_idle = im.Scale("Area2_dark.png", 1920,1080)
    #image Area2_selected = im.Scale("Area2_base.png", 1920,1080)
    #image Area3_idle = im.Scale("Area3_dark.png", 1920,1080)
    #image Area3_selected = im.Scale("Area3_base.png", 1920,1080)
    #image Area4_idle = im.Scale("Area4_dark.png", 1920,1080)
    #image Area4_selected = im.Scale("Area4_base.png", 1920,1080)
    #image Area5_idle = im.Scale("Area5_dark.png", 1920,1080)
    #image Area5_selected = im.Scale("Area5_base.png", 1920,1080)
    #image Area6_idle = im.Scale("Area6_dark.png", 1920,1080)
    #image Area6_selected = im.Scale("Area6_base.png", 1920,1080)
    #image Area7_idle = im.Scale("Area7_dark.png", 1920,1080)
    #image Area7_selected = im.Scale("Area7_base.png", 1920,1080)
    #image Area8_idle = im.Scale("Area8_dark.png", 1920,1080)
    #image Area8_selected = im.Scale("Area8_base.png", 1920,1080)
    #image Area9_idle = im.Scale("Area9_dark.png", 1920,1080)
    #image Area9_selected = im.Scale("Area9_base.png", 1920,1080)
    #image Area10_idle = im.Scale("Area10_dark.png", 1920,1080)
    #image Area10_selected = im.Scale("Area10_base.png", 1920,1080)
    #image Area11_idle = im.Scale("Area11_dark.png", 1920,1080)
    #image Area11_selected = im.Scale("Area11_base.png", 1920,1080)
    #image Area12_idle = im.Scale("Area12_dark.png", 1920,1080)
    #image Area12_selected = im.Scale("Area12_base.png", 1920,1080)
    #image Area13_idle = im.Scale("Area13_dark.png", 1920,1080)
    #image Area13_selected = im.Scale("Area13_base.png", 1920,1080)

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

    image down_left = im.Scale("multiplayer down left.png",451,304)
    image down_right = im.Scale("multiplayer down right.png",451,304)
    image up_left = im.Scale("multiplayer up left.png",451,304)
    image up_right = im.Scale("multiplayer up right.png",451,304)

screen Base_UI():
    add "down_left" anchor(0.0,1.0) xalign 0.0 yalign 1.0
    add "down_right" anchor(1.0,1.0) xalign 1.0 yalign 1.0
    add "up_left"  anchor(0.0,0.0) xalign 0.0 yalign 0.0
    add "up_right" anchor(1.0,0.0) xalign 1.0 yalign 0.0

screen Agent_Placement():
    
    add map_location_prefix +"MAP_dark.png" 
    #add "weisses-bild.jpg"
    for each in range(1,14):
        imagebutton:
            insensitive ("Area"+str(each)+"_idle")
            idle ("Area"+str(each)+"_idle")
            hover "Area"+str(each)+"_selected"
            selected_idle "Area"+str(each)+"_selected"
            selected_hover "Area"+str(each)+"_selected"
            focus_mask True
            #Actions
            action NullAction()
            hovered NullAction()
            unhovered NullAction()
    use Base_UI
###########################################################




    