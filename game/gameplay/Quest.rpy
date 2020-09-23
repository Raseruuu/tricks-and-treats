init python:
    class Quest():
        
        def __init__(self,name,description,requirements,rewards,FOREST,LABEL):
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
            the_string = get_name + "|" + get_description + "\n" 
            if(get_required_Victory_Candy(self,player) > 0.9): the_string = the string + "{image=Victory_Candy_text_icon.png}" + " " +  (int)get_required_Victory_Candy(self,player)
            if(get_required_Candy_Corn(self,player) > 0.9): the_string = the string + "{image=Candy_Corn_text_icon.png}" + " " +  (int)get_required_Candy_Corn(self,player)
            if(get_required_Chocolate(self,player) > 0.9): the_string = the string + "{image=Chocolate_text_icon.png}" + " " +  (int)get_required_Chocolate(self,player)
            if(get_required_Trick_Supplies(self,player) > 0.9): the_string = the string + "{image=Trick_Supplies_text_icon.png}" + " " +  (int)get_required_Trick_Supplies(self,player)
            the_string = the_string + "\n"
            if(get_reward_Victory_Candy(self,player) > 0.9): the_string = the string + "{image=Victory_Candy_text_icon.png}" + " " +  (int)get_reward_Victory_Candy(self,player)
            if(get_reward_Candy_Corn(self,player) > 0.9): the_string = the string + "{image=Candy_Corn_text_icon.png}" + " " +  (int)get_reward_Candy_Corn(self,player)
            if(get_reward_Chocolate(self,player) > 0.9): the_string = the string + "{image=Chocolate_text_icon.png}" + " " +  (int)get_reward_Chocolate(self,player)
            if(get_reward_Trick_Supplies(self,player) > 0.9): the_string = the string + "{image=Trick_Supplies_text_icon.png}" + " " +  (int)get_reward_Trick_Supplies(self,player)
            the_string = the_string + "\n"
            the_string = the_string + self.reward_effect_description
            return the_string