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
define u = Character("??")

define narrator = Character("Narrator", type='narrator')

# The game starts here.

label start:

    call screen Agent_Placement()

    scene bg room

    p "Hello!!"
    "World!"
    jump gamestart
    # This ends the game.

    return
