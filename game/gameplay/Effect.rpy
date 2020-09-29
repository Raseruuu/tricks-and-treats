init python:
    class Effect:
        def __init__(self,effect_number):
            self.effect_number = effect_number

        def one():
            #current player gains double Candy Corn and doubble Chocolate for 1 round
            current_player.change_mod_Candy_Corn(2,1,True,True)
            current_player.change_mod_Chocolate(2,1,True,True)            
            return 
  
        def two():
            return 
  
        def three():
            return 
  
        def four():
            return 
  
        def five():
            return 
  
        def six():
            return 
  
        def seven():
            return 
  
        def eight():
            return 
  
        def nine():
            return 
  
        def ten():
            return 
  
        def eleven():
            return 
  
        def twelve():
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


            