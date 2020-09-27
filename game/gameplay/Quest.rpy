init python:
    class Quest:
        
        def __init__(self,ID,name,description,requirements,FOREST,LABEL,rewards,reward_effect_description):
            
            self.ID = ID
            self.forest = FOREST
            self.name = name
            self.description = description
            self.LABEL = LABEL
            self.required_Victory_Candy = requirements[0]
            self.required_Candy_Corn = requirements[1]
            self.required_Chocolate = requirements[2]
            self.required_Trick_Supplies = requirements[3]

            self.reward_Victory_Candy = rewards[0]
            self.reward_Candy_Corn = rewards[1]
            self.reward_Chocolate = rewards[2]
            self.reward_Trick_Supplies = rewards[3]
            self.reward_function = rewards [4]
            self.reward_effect_description = reward_effect_description
######################################################################################
        def give_quest_rewards(self,player):
            player.receive_from_quest_Victory_Candy(self.reward_Victory_Candy)
            player.receive_from_quest_Candy_Corn(self.reward_Candy_Corn)
            player.receive_from_quest_Chocolate(self.reward_Chocolate)
            player.receive_from_quest_Trick_Supplies(self.reward_Trick_Supplies)
            self.reward_function(self,player)

######################################################################################
        def get_required_Victory_Candy(self,player):
            n = self.required_Victory_Candy * player.quest_required_Victory_Candy_mod
            if(n > 0):
                return (int)(n + player.quest_required_Victory_Candy_ADD)
            return 0
        def get_required_Candy_Corn(self,player):
            n = self.required_Candy_Corn * player.quest_required_Candy_Corn_mod
            if(n > 0):
                return (int)(n + player.quest_required_Candy_Corn_ADD)
            return 0
        def get_required_Chocolate(self,player):
            n = self.required_Chocolate * player.quest_required_Chocolate_mod
            if(n > 0):
                return (int)(n + player.quest_required_Chocolate_ADD)
            return 0
        def get_required_Trick_Supplies(self,player):
            n = self.required_Trick_Supplies * player.quest_required_Trick_Supplies_mod
            if(n > 0):
                return (int)(n + player.quest_required_Trick_Supplies_ADD)
            return 0
#########################################################################################
        def get_reward_Victory_Candy(self,player):
            n = self.reward_Victory_Candy * player.quest_reward_Victory_Candy_mod
            if(n > 0):
                return (int)(n + player.quest_reward_Victory_Candy_ADD)
            return 0
        def get_reward_Candy_Corn(self,player):
            n = self.reward_Candy_Corn * player.quest_reward_Candy_Corn_mod
            if(n > 0):
                return (int)(n + player.quest_reward_Candy_Corn_ADD)
            return 0
        def get_reward_Chocolate(self,player):
            n = self.reward_Chocolate * player.quest_reward_Chocolate_mod
            if(n > 0):
                return (int)(n + player.quest_reward_Chocolate_ADD)
            return 0
        def get_reward_Trick_Supplies(self,player):
            n = self.reward_Trick_Supplies * player.quest_reward_Trick_Supplies_mod
            if(n > 0):
                return (int)(n + player.quest_reward_Trick_Supplies_ADD)
            return 0
########################################################################################
        def get_name(self):
            return self.name
        def get_description(self):
            return self.description
        def get_formated_info(self,player):
            the_string = self.get_name() + "|" + self.get_description() + "\n" 
            if self.get_required_Victory_Candy(player) > 0.9: 
                the_string = the_string + "{image=Victory_Candy_text_icon.png}" + " " +  self.get_required_Victory_Candy(player)
            if(self.get_required_Candy_Corn(player) > 0.9): 
                the_string = the_string + "{image=Candy_Corn_text_icon.png}" + " " +  self.get_required_Candy_Corn(player)
            if(self.get_required_Chocolate(player) > 0.9): the_string = the_string + "{image=Chocolate_text_icon.png}" + " " +  self.get_required_Chocolate(player)
            if(self.get_required_Trick_Supplies(player) > 0.9): the_string = the_string + "{image=Trick_Supplies_text_icon.png}" + " " +  self.get_required_Trick_Supplies(player)
            the_string = the_string + "\n"
            if(self.get_reward_Victory_Candy(player) > 0.9): the_string = the_string + "{image=Victory_Candy_text_icon.png}" + " " +  self.get_reward_Victory_Candy(player)
            if(self.get_reward_Candy_Corn(player) > 0.9): the_string = the_string + "{image=Candy_Corn_text_icon.png}" + " " +  self.get_reward_Candy_Corn(player)
            if(self.get_reward_Chocolate(player) > 0.9): the_string = the_string + "{image=Chocolate_text_icon.png}" + " " +  self.get_reward_Chocolate(player)
            if(self.get_reward_Trick_Supplies(player) > 0.9): the_string = the_string + "{image=Trick_Supplies_text_icon.png}" + " " +  self.get_reward_Trick_Supplies(player)
            the_string = the_string + "\n"
            the_string = the_string + self.reward_effect_description
            return the_string