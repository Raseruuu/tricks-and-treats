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

        

    call screen Agent_Placement()

    scene bg room


    p "Hello!!"
    "World!"
    jump gamestart
    # This ends the game.

    return
