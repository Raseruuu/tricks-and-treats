init python:
    class Effect:
        def __init__(self,effect_number):
            self.effect_number = effect_number

        def stealPlaceSuccessfull(Place):
            for player in player_ARRAY :
                if player != current_player:
                    if Place in player.my_places:
                        player.my_places.remove(Place)
                        current_player.my_places.append(Place)
                        return True
            return False

        def one():
            #current player gains double Candy Corn and doubble Chocolate for 1 round
            current_player.change_mod_Candy_Corn(2,1,True,False)
            current_player.change_mod_Chocolate(2,1,True,False)            
            return 
  
        def two():
            #Earn 2 Candy Corn and every other player gains 1 Candy Corn
            current_player.Candy_Corn = current_player.Candy_Corn + 2
            for player in player_ARRAY :
                if player != current_player:
                    player.Candy_Corn = player.Candy_Corn + 1
            return 
  
        def three():
            #Earn 2 Chocolate and every other player gains 1 Chocolate
            current_player.Chocolate = current_player.Chocolate + 2
            for player in player_ARRAY :
                if player != current_player:
                    player.Candy_Corn = player.Chocolate + 1
            return 
  
        def four():
            #Earn 2 Chocolate and select a player that gains 1 Chocolate
            current_player.Chocolate = current_player.Chocolate + 2
            selected_player = renpy.callScreen(selectPlayer)
            selected_player.Chocolate = selected_player.Chocolate + 1
            return 
  
        def five():
            #Earn 2 Candy Corn and select a player that gains 1 Candy Corn
            current_player.Candy_Corn = current_player.Candy_Corn + 2
            selected_player = renpy.callScreen(selectPlayer)
            selected_player.Candy_Corn = selected_player.Candy_Corn +1
            return 
  
        def six():
            #Earn 4 Trick Supplies and select a player that gains 2 Trick Supplies
            current_player.Trick_Supplies = current_player.Trick_Supplies + 4
            selected_player = renpy.callScreen(selectPlayer)
            selected_player.Trick_Supplies = selected_player.Trick_Supplies + 2
            return 
  
        def seven():
            #Steal a place from a other player
            selected_place = renpy.callScreen(selectedPlace)
            if stealPlaceSuccessfull(selected_place):
                return
            else:
                seven() 
  
        def eight():
            #Steal 2 Victory Candys from a selected player
            selected_player = renpy.callScreen(selectPlayer)
            if selected_player.Victory_Candy >= 2:
                selected_player.Victory_Candy = selected_player.Victory_Candy - 2
            else:
                selected_player.Victory_Candy = 0
            current_player.Victory_Candy = current_player.Victory_Candy + 2
            return 
  
        def nine():
            #Earn two random ressources
            Random_Array = []
            Random_Array.append(randrange(3))
            Random_Array.append(randrange(3))
            for number in Random_Array:
                if number == 0:
                    current_player.Chocolate = current_player.Chocolate + 3
                if number == 1:
                    current_player.Candy_Corn = current_player.Candy_Corn + 3
                if number == 2:
                    current_player.Trick_Supplies = current_player.Trick_Supplies + 4
            Random_Array.clear()
            return 
  
        def ten():
            #pay 3 Victory Candy and your quest has no requirements
            if current_player.Victory_Candy < 3:
                return -1 #Card can not be played
            current_player.Victory_Candy = current_player.Victory_Candy - 3
            current_player.quest_required_Chocolate_mod[Turn] = 0
            current_player.quest_required_Candy_Corn_mod[Turn] = 0
            current_player.quest_required_Trick_Supplies_mod[Turn] = 0
            current_player.quest_required_Victory_Candy_mod[Turn] = 0

            return 
  
        def eleven():
            #Select 3 Places that should give no ressources for this turn
            firstPlace = renpy.callScreen(selectedPlace)
            firstPlace.Victory_Candy_mod[Turn] = 0
            firstPlace.Candy_Corn_mod[Turn] = 0
            firstPlace.Chocolate_mod[Turn] = 0
            firstPlace.Trick_Supplies_mod[Turn] = 0
            secondPlace = renpy.callScreen(selectedPlace)
            secondPlace.Victory_Candy_mod[Turn] = 0
            secondPlace.Candy_Corn_mod[Turn] = 0
            secondPlace.Chocolate_mod[Turn] = 0
            secondPlace.Trick_Supplies_mod[Turn] = 0
            thirdPlace = renpy.callScreen(selectedPlace)
            thirdPlace.Victory_Candy_mod[Turn] = 0
            thirdPlace.Candy_Corn_mod[Turn] = 0
            thirdPlace.Chocolate_mod[Turn] = 0
            thirdPlace.Trick_Supplies_mod[Turn] = 0
            return 
  
        def twelve():
            #Earn 6 Trick Supplies and select a player that gains 1 Trick Supplies
            current_player.Trick_Supplies = current_player.Trick_Supplies + 6
            for player in player_ARRAY :
                if player != current_player:
                    player.Trick_Supplies = player.Trick_Supplies + 1
            return 
        
        def playEffect(self):
            switcher = {
                1: one,
                2: two,
                3: three,
                4: four,
                5: five,
                6: six,
                7: seven,
                8: eight,
                9: nine,
                10: ten,
                11: eleven,
                12: twelve
            }
            # Get the function from switcher dictionary
            func = switcher.get(self.effect_number, lambda: "No Effect")
            # Execute the function
            print func()           