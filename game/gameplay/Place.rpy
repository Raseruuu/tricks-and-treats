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
        def get_Victory_Candy(self):
            amount = self.Victory_Candy * self.Victory_Candy_mod[Turn]
            if(amount != 0):
                amount = amount + self.Victory_Candy_mod_ADD[Turn]
                return amount
            return 0.1
        def get_Candy_Corn(self):
            amount = self.Candy_Corn * self.Candy_Corn_mod[Turn]
            if(amount != 0):
                amount = amount + self.Candy_Corn_mod_ADD[Turn]
                return amount
            return 0.1
        def get_Chocolate(self):
            amount = self.Chocolate * self.Chocolate_mod[Turn]
            if(amount != 0):
                amount = amount + self.Chocolate_mod_ADD[Turn]
                return amount
            return 0.1
        def get_Trick_Supplies(self):
            amount = self.Trick_Supplies * self.Trick_Supplies_mod[Turn]
            if(amount != 0):
                amount = amount + self.Trick_Supplies_mod_ADD[Turn]
                return amount
            return 0.1
#############################################################################################
        def change_mod_Victory_Candy(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Victory_Candy_mod[i] =  amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Victory_Candy_mod[i] = amount
            else:
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount

        def change_mod_Candy_Corn(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Candy_Corn_mod[i] =  amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Candy_Corn_mod[i] = amount
            else:
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Candy_Corn_mod[i] = self.Candy_Corn_mod[i] * amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Candy_Corn_mod[i] = self.Candy_Corn_mod[i] * amount


        def change_mod_Chocolate(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Chocolate_mod[i] =  amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Chocolate_mod[i] = amount
            else:
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Chocolate_mod[i] = self.Chocolate_mod[i] * amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Chocolate_mod[i] = self.Chocolate_mod[i] * amount


        def change_mod_Trick_Supplies(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Trick_Supplies_mod[i] =  amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Trick_Supplies_mod[i] = amount
            else:
                if(instant == True):
                    for(i = Turn,i <= durration+Turn , i++):
                        self.Trick_Supplies_mod[i] = self.Trick_Supplies_mod[i] * amount
                else:
                    for(i = Turn+1,i <= durration+Turn+1 , i++):
                        self.Trick_Supplies_mod[i] = self.Trick_Supplies_mod[i] * amount