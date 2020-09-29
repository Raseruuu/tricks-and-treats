##screen Card_select:
#    #Need the card design
# USE THE BELOW FOR THE SCREEN

#image false_elegy = Resolution_append_front + "False Elegy.png"
#image shutter_stop = Resolution_append_front + "Shutter.jpg"
#image Episcava = Resolution_append_front + "Episcava.png"

#transform size_changer_button:
#    on idle:
#        linear 0.3 zoom 0.5
#    on hover:
#        linear 0.3 zoom 0.7


#screen image_desicion:
#    
#    
#    imagebutton at size_changer_button:
#        idle "false_elegy"
#        hover "false_elegy"
#        action SetVariable("Choice_nummber" , 1) , Return()
#        xanchor 0.5 yanchor 0.5
#        xpos 0.15 ypos 0.4
#        
#        hovered Function(Michael,"A dark fantasy VN about the currupting nature of particle effects.", False, False)
#        
#        unhovered Function(Michael, "Due to budget limitations I can only really chose one of them.", False, False)
#       
#    
#        
#    image#button at size_changer_button:
#        i#dle "shutter_stop"
#        h#over "shutter_stop"
#        action SetVariable("Choice_nummber" , 2) , Return()
#        
#        hovered Function(Michael, "A detective game about a retired detective fighting against a criminal from their past.", False, False)
#        
#        unhovered Function(Michael, "Due to budget limitations I can only really chose one of them.", False, False)
#        xanchor 0.5 yanchor 0.5
#        xpos 0.4 ypos 0.4
#        
#    
#    
#    imagebutton at size_changer_button:
#        idle "Episcava"
#        hover "Episcava"
#        action SetVariable("Choice_nummber" , 3) , Return()
#        xanchor 0.5 yanchor 0.5
#        xpos 0.65 ypos 0.4
#        
#        hovered Function(Michael,"A dungeon crawler with randomly generated floors and what they describe as organic skill growth.", False, False)
#        
#        unhovered Function(Michael, "Due to budget limitations I can only really chose one of them.", False, False)
#

#