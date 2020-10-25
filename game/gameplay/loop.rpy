label gamestart:
    menu:
        "Select Label"
        "Vampire":
            call Vampire_1
        "Slime":
            call Slime_1
        "Fox":
            call Fox_1
    if game_loop:
        jump gamestart
    return

init python:
    def turn_step_harvest():
        for each in players:
            each.harvest()

init python:
    def game_loop():
        #Step I Chose a Quest
        if(Hotseat):
            for each in range(1,5):
                if each.Is_CPU() :
                    #do CPU things
                    print("do Cpu things")
                if each.Is_Player_controlled():
                    renpy.call_screen(Select_Quest_Screen,each)

        

            
        
        
