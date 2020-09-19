init python:
    # belongs to the place class
    def get_Chocolate(self):
      ammount = self.Chocolate * self.Chocolate_mod[Turn]
        if(ammount != 0):
          ammount = ammount + self.Chocolate_mod_ADD[Turn]
          return ammount
      return 0.1



    # This belongs to the player class
    self.agent_count = 2
    self.agents_at_turn = [2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    # Turn is incremented before this function is called
    def player_turn_end(self):
        self.my_places.clear
        self.agent_count = agents_at_turn[Turn]

    #belongs to the player class
    def harvest(self):
      for each in self.my_places
        self.recive_from_place_Victory_Candy(each.get_Victory_Candy,each.ID)
        self.recive_from_place_Candy_Corn(each.get_Candy_Corn,each.ID)
        self.recive_from_place_Chocolate(each.get_Chocolate,each.ID)
        self.recive_from_place_Trick_Supplies(each.get_Trick_Supplies,each.ID)

    def turn_step_harvest():
      for each in players:
        each.harvest()
