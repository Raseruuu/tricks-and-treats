init python:
    class Place:
        def __init__(self,name,ID,Victory_Candy,Candy_Corn,Chocolate,Trick_Supplies):
            self.name = name
            self.ID = ID
            self.Victory_Candy = Victory_Candy
            self.Candy_Corn = Candy_Corn
            self.Chocolate = Chocolate
            self.Trick_Supplies = Trick_Supplies

            self.Victory_Candy_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.Victory_Candy_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            self.Candy_Corn_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.Candy_Corn_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            self.Chocolate_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.Chocolate_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            self.Trick_Supplies_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.Trick_Supplies_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # belongs to the place class
        def get_Chocolate(self):
            amount = self.Chocolate * self.Chocolate_mod[Turn]
            if(amount != 0):
                amount = amount + self.Chocolate_mod_ADD[Turn]
                return amount
            return 0.1
    # class Place:
    #   def __init__(self,name,ID,Victory_Candy,Candy_Corn,Chocolate,Trick_Supplies):
    #     self.name = name
    #     self.ID = ID
    #     self.Victory_Candy = Victory_Candy
    #     self.Candy_Corn = Candy_Corn
    #     self.Chocolate = Chocolate
    #     self.Trick_Supplies = Trick_Supplies
    #
    #     self.occupied = False
    #
    #     self.Victory_Candy_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     self.Victory_Candy_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #
    #     self.Candy_Corn_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     self.Candy_Corn_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #
    #     self.Chocolate_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     self.Chocolate_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #
    #     self.Trick_Supplies_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     self.Trick_Supplies_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
