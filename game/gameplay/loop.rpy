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