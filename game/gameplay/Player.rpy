
init python:

    class Player:

        def __init__(self,character):
            if character == "Random":
                self.character = assign_via_random()
                
            else :
                self.character = character
            self.Victory_Candy = 0
            self.Candy_Corn = 0
            self.Chocolate = 0
            self.Trick_Supplies = 0

            self.Forest_Deck = []

            self.Player_controlled = True
            self.CPU = False

            self.agent_count = 2
            self.agents_at_turn = [2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

            self.my_places = []
            
            self.Victory_Candy_mod_place = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]

            self.Victory_Candy_ADD_place = [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]
            self.quest_required_Victory_Candy_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_required_Victory_Candy_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.quest_reward_Victory_Candy_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_reward_Victory_Candy_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            self.Candy_Corn_mod_place=[
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]
            

            self.Candy_Corn_ADD_place =[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]

            self.quest_required_Candy_Corn_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_required_Candy_Corn_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.quest_reward_Candy_Corn_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_reward_Candy_Corn_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            self.Chocolate_mod_place = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]

            self.Chocolate_ADD_place = [
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]

            self.quest_required_Chocolate_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_required_Chocolate_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.quest_reward_Chocolate_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_reward_Chocolate_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
            self.Trick_Supplies_mod_place =[
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]
            self.Trick_Supplies_ADD_place =[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]
            self.quest_required_Trick_Supplies_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_required_Trick_Supplies_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.quest_reward_Trick_Supplies_mod = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            self.quest_reward_Trick_Supplies_ADD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
#################################################################################
        def receive_from_quest_Victory_Candy(self,amount):
            the_mod = self.quest_reward_Victory_Candy_mod[Turn]
            the_ADD = self.quest_reward_Victory_Candy_ADD[Turn]
            amount = amount * the_mod
            if(amount != 0):
                amount = amount + the_ADD
                self.Victory_Candy = self.Victory_Candy + int(amount)
        def receive_from_quest_Candy_Corn(self,amount):
            the_mod = self.quest_reward_Candy_Corn_mod[Turn]
            the_ADD = self.quest_reward_Candy_Corn_ADD[Turn]
            amount = amount * the_mod
            if(amount != 0):
                amount = amount + the_ADD
                self.Candy_Corn = self.Candy_Corn + int(amount)
        def receive_from_quest_Chocolate(self,amount):
            the_mod = self.quest_reward_Chocolate_mod[Turn]
            the_ADD = self.quest_reward_Chocolate_ADD[Turn]
            amount = amount * the_mod
            if(amount != 0):
                amount = amount + the_ADD
                self.Chocolate = self.Chocolate + int(amount)
        def receive_from_quest_Trick_Supplies(self,amount):
            the_mod = self.quest_reward_Trick_Supplies_mod[Turn]
            the_ADD = self.quest_reward_Trick_Supplies_ADD[Turn]
            amount = amount * the_mod
            if(amount != 0):
                amount = amount + the_ADD
                self.Trick_Supplies = self.Trick_Supplies + int(amount)
    #################################################################################
        def receive_from_place_Victory_Candy(self,VC_ammount,place_ID):
            VC_amount = VC_amount * self.Victory_Candy_mod_place[place_ID][Turn]
            if(VC_amount != 0):
                VC_amount = VC_amount + self.Victory_Candy_ADD_place[place_ID][Turn]
                self.Victory_Candy = self.Victory_Candy + int(VC_amount)
            
        def receive_from_place_Candy_Corn(self,Candy_Corn_amount,place_ID):
            Candy_Corn_amount = Candy_Corn_amount * self.Candy_Corn_mod_place[place_ID][Turn]
            if(Candy_Corn_amount != 0):
                Candy_Corn_amount = Candy_Corn_amount + self.Candy_Corn_ADD_place[place_ID][Turn]
                self.Candy_Corn = self.Candy_Corn + int(Candy_Corn_amount)
            


        def receive_from_place_Chocolate(self,Chocolate_amount,place_ID):
            Chocolate_amount = Chocolate_amount * self.Chocolate_mod_place[place_ID][Turn]
            if (Chocolate_amount != 0):
                Chocolate_amount = Chocolate_amount + self.Chocolate_ADD_place[place_ID][Turn]
                self.Chocolate = self.Chocolate + int(Chocolate_amount)
            

        def receive_from_place_Trick_Supplies(self,Trick_Supplies_amount,place_ID):
            Trick_Supplies_amount = Trick_Supplies_amount * self.Trick_Supplies_mod_place[place_ID][Turn]
            if(Trick_Supplies_amount != 0):
                Trick_Supplies_amount = Trick_Supplies_amount + self.Trick_Supplies_ADD_place[place_ID][Turn]
                self.Trick_Supplies = self.Trick_Supplies + int(Trick_Supplies_amount)
    #################################################################################
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
        
        
        # Turn is incremented before this function is called
        def player_turn_end(self):
            self.my_places.clear
            self.agent_count = agents_at_turn[Turn]
        

        def harvest(self):
            for each in self.my_places:
                self.receive_from_place_Victory_Candy(each.get_Victory_Candy,each.ID)
                self.receive_from_place_Candy_Corn(each.get_Candy_Corn,each.ID)
                self.receive_from_place_Chocolate(each.get_Chocolate,each.ID)
                self.receive_from_place_Trick_Supplies(each.get_Trick_Supplies,each.ID)

        def occupy(self,place_ID):
            self.agent_count = self.agent_count - 1
            self.my_places.append(place_ARRAY[place_ID])
            place_ARRAY[place_ID].occupied = True    
    ###############################################
        def Is_CPU(self):
            return self.CPU
        def Is_Player_controlled(self):
            return self.Player_controlled

