# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    playername = "Sayako"
    game_loop=True

define p = Character("[playername]")
define a = Character("A")
define v = Character("Vampire")
define f = Character("Fox")
define s = Character("Slime")
define Michael = Character("")
define u = Character("??")



define narrator = Character("Narrator", type='narrator')

# The game starts here.



label start:
    $taken_characters = [] 
    #call screen Agent_Placement

    while single_player_lobby_loop == True:
        call screen Lobby_single_player()
    $single_player_lobby_loop = True
    
    python: 
        global slots
        player_1 = Player(slots[0])
        print (player_1.character)
        
        player_2 = Player(slots[1])
        player_ARRAY = [player_1,player_2]
        print(player_ARRAY[0].character)
        print(player_ARRAY[0].character)
        print(player_ARRAY[0].character)
        print(player_ARRAY[0].character)
        if Player_count > 2:
            player_3 = Player(slots[2])
            player_ARRAY.append(player_3)
        if Player_count > 3:
            player_4 = Player(slots[3])
            player_ARRAY.append(player_4)

        Forest_decks = []
        import copy 
        Forest_decks = []
        Fd1 = copy.deepcopy(qDeck_Forest)
        Forest_decks.append(Fd1)
        Fd2 = copy.deepcopy(qDeck_Forest)
        Forest_decks.append(Fd2)
        if Player_count > 3:
            Fd3 = copy.deepcopy(qDeck_Forest)
            Forest_decks.append(Fd3)
        if Player_count > 4:
            Fd4 = copy.deepcopy(qDeck_Forest)
            Forest_decks.append(Fd4)
        print("Decks:")
        for each in Forest_decks:
            random.shuffle(each)

        for each in Forest_decks:
            for x in each:
            
                print(x.ID,end = '')
                print(" ", end = '')
            print("Next deck")
           
        player_1.Forest_Deck = Fd1
        player_2.Forest_Deck = Fd2
        if Player_count > 3:
            player_3.Forest_Deck = Fd3
        if Player_count > 4:
            player_4.Forest_Deck = Fd4

        Used_Town_Deck = copy.deepcopy(qDeck_Town)
        random.shuffle(Used_Town_Deck)


    

    python:
        if(Hotseat):
            for each in player_ARRAY:
                if (each.Is_CPU()):
                    #do CPU things
                    print("do Cpu things")
                if each.Is_Player_controlled():
                    renpy.call_screen("Select_Quest_Screen",each)
                    Hotseat=False
    
        

    call screen Agent_Placement()

    scene bg room


    p "Hello!!"
    "World!"
    jump gamestart
    # This ends the game.

    return
