# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    playername = "Sayako"

define p = Character("[playername]")
define narrator = Character("Narrator", type='narrator')

# The game starts here.

label start:

    scene bg room

    p "Hello!!"
    "World!"

    # This ends the game.

    return
