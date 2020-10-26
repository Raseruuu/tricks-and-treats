init -3 python:
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

            self.occupation_slots = 1
            self.occupation = [9]

        def place_hover_text(self,character):
            VC_amount = self.get_Victory_Candy()
            VC_amount = VC_amount * character.Victory_Candy_mod_place[self.ID][Turn]
            if(VC_amount != 0):
                VC_amount = VC_amount + character.Victory_Candy_ADD_place[self.ID][Turn]
                VC_amount = int(VC_amount)

            CC_amount = self.get_Candy_Corn()
            CC_amount = CC_amount * character.Candy_Corn_mod_place[self.ID][Turn]
            if(CC_amount != 0):
                CC_amount = CC_amount + character.Candy_Corn_ADD_place[self.ID][Turn]
                CC_amount = int(CC_amount)

            Choco_amount = self.get_Chocolate()
            Choco_amount = Choco_amount * character.Chocolate_mod_place[self.ID][Turn]
            if(Choco_amount != 0):
                Choco_amount = Choco_amount + character.Chocolate_ADD_place[self.ID][Turn]
                Choco_amount = int(Choco_amount)

            TS_amount = self.get_Trick_Supplies()
            TS_amount = TS_amount * character.Trick_Supplies_mod_place[self.ID][Turn]
            if(TS_amount != 0):
                TS_amount = TS_amount + character.Trick_Supplies_ADD_place[self.ID][Turn]
                TS_amount = int(TS_amount)
            
            #VC_amount , CC_amount , Choco_amount , TS_amount

            return "  {image=Victory_Candy_text_icon.png} " + str(VC_amount) + "   {image=Candy_Corn_text_icon.png} " + str(CC_amount) + "\n{image=Chocolate_text_icon.png} " + str(Choco_amount) + "   {image=Trick_Supplies_text_icon.png} " + str(TS_amount) + "\nOpen Slots: " + str(self.occupation.count(9))

        def can_be_occupied(self):
            return 9 in self.occupation
            
        def get_occupied(self,player):
            if 9 in self.occupation:
                self.occupation[self.occupation.index(9)] = player.ID

        def remove_occupant(self,player):
            if player.ID in self.occupation:
                self.occupation[self.occupation.index(player.ID)] = 9

        def remove_all_occupants(self):
            self.occupation = [9]

        # belongs to the place class
        def get_Victory_Candy(self):
            amount = self.Victory_Candy * self.Victory_Candy_mod[Turn]
            if(amount != 0):
                amount = amount + self.Victory_Candy_ADD[Turn]
                return amount
            return 0.1
        def get_Candy_Corn(self):
            amount = self.Candy_Corn * self.Candy_Corn_mod[Turn]
            if(amount != 0):
                amount = amount + self.Candy_Corn_ADD[Turn]
                return amount
            return 0.1
        def get_Chocolate(self):
            amount = self.Chocolate * self.Chocolate_mod[Turn]
            if(amount != 0):
                amount = amount + self.Chocolate_ADD[Turn]
                return amount
            return 0.1
        def get_Trick_Supplies(self):
            amount = self.Trick_Supplies * self.Trick_Supplies_mod[Turn]
            if(amount != 0):
                amount = amount + self.Trick_Supplies_ADD[Turn]
                return amount
            return 0.1
#############################################################################################
        def change_mod_Victory_Candy(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Victory_Candy_mod[i] =  amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Victory_Candy_mod[i] = amount
            else:
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount

        def change_mod_Candy_Corn(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Candy_Corn_mod[i] =  amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Candy_Corn_mod[i] = amount
            else:
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Candy_Corn_mod[i] = self.Candy_Corn_mod[i] * amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Candy_Corn_mod[i] = self.Candy_Corn_mod[i] * amount


        def change_mod_Chocolate(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Chocolate_mod[i] =  amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Chocolate_mod[i] = amount
            else:
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Chocolate_mod[i] = self.Chocolate_mod[i] * amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Chocolate_mod[i] = self.Chocolate_mod[i] * amount


        def change_mod_Trick_Supplies(self,amount,durration,instant,SET):
            if(SET == True):
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Trick_Supplies_mod[i] =  amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Trick_Supplies_mod[i] = amount
            else:
                if(instant == True):
                    for i in range(Turn,durration+Turn+1):
                        self.Trick_Supplies_mod[i] = self.Trick_Supplies_mod[i] * amount
                else:
                    for i in range(Turn+1,durration+Turn+2):
                        self.Trick_Supplies_mod[i] = self.Trick_Supplies_mod[i] * amount