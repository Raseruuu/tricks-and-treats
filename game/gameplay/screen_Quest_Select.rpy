# We do not need a quest screen , USE the menu
# We make it here END OF STORY


screen Select_Quest_Screen(Character):

    add "sketch_" + Character.character  + "_small.png" zoom 0.3 yanchor 1.0 ypos 1.0 xpos 0.02


    style_prefix "choice"

    vbox:
        for i in range(Turn*2,Turn*2+2):
            textbutton Used_Town_Deck[i].name: 
                action Function(assign_quest_to_player,Character,Used_Town_Deck[i]) , Return()

        textbutton Character.Forest_Deck[Turn].name:
            action Function(assign_quest_to_player,Character,Character.Forest_Deck[Turn]) , Return()