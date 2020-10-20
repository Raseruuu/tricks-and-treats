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
                if each.is_CPU():
                    #do CPU things
                    print("do Cpu things")
                if each.Is_Player_controlled():
                    renpy.call_screen(Select_Quest_Screen)
                    Hotseat=False
                    shuffle(player_ARRAY) 
        if(!Hotseat):
            #if playerammount < 2 :
                #for each player player Agentammount = 3
            #if Turn < 1 :
                #for each player in player_Array:
                    #playersquestattribut = renpy.call_screen(Select_Quest_Screen)
            #for each player in player_Array:
                #player.takeCard()        
            #for each player in player_Array:
                #current_player = player
                #renpy.call_screen(Place_Agent_Screen)

            
        
        
