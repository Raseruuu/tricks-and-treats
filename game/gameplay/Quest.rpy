init -2 python:
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
            n = self.required_Victory_Candy * player.quest_required_Victory_Candy_mod[Turn]
            if(n > 0):
                return int(n + player.quest_required_Victory_Candy_ADD[Turn])
            return 0
        def get_required_Candy_Corn(self,player):
            n = self.required_Candy_Corn * player.quest_required_Candy_Corn_mod[Turn]
            if(n > 0):
                return int(n + player.quest_required_Candy_Corn_ADD[Turn])
            return 0
        def get_required_Chocolate(self,player):
            n = self.required_Chocolate * player.quest_required_Chocolate_mod[Turn]
            if(n > 0):
                return int(n + player.quest_required_Chocolate_ADD[Turn])
            return 0
        def get_required_Trick_Supplies(self,player):
            n = self.required_Trick_Supplies * player.quest_required_Trick_Supplies_mod[Turn]
            if(n > 0):
                return int(n + player.quest_required_Trick_Supplies_ADD[Turn])
            return 0
#########################################################################################
        def get_reward_Victory_Candy(self,player):
            n = self.reward_Victory_Candy * player.quest_reward_Victory_Candy_mod[Turn]
            if(n > 0):
                return int(n + player.quest_reward_Victory_Candy_ADD[Turn])
            return 0
        def get_reward_Candy_Corn(self,player):
            n = self.reward_Candy_Corn * player.quest_reward_Candy_Corn_mod[Turn]
            if(n > 0):
                return int(n + player.quest_reward_Candy_Corn_ADD[Turn])
            return 0
        def get_reward_Chocolate(self,player):
            n = self.reward_Chocolate * player.quest_reward_Chocolate_mod[Turn]
            if(n > 0):
                return int(n + player.quest_reward_Chocolate_ADD[Turn])
            return 0
        def get_reward_Trick_Supplies(self,player):
            n = self.reward_Trick_Supplies * player.quest_reward_Trick_Supplies_mod[Turn]
            if(n > 0):
                return int(n + player.quest_reward_Trick_Supplies_ADD[Turn])
            return 0
########################################################################################
        def get_name(self):
            return self.name
        def get_description(self):
            return self.description
        def get_formated_info(self,player):
            the_string =  self.get_description() + "\nRequirements: " 
            if self.get_required_Victory_Candy(player) > 0.9: 
                the_string = the_string + "{image=Victory_Candy_text_icon.png}" + " " +  str(self.get_required_Victory_Candy(player))+ " "
            if(self.get_required_Candy_Corn(player) > 0.9): 
                the_string = the_string + "{image=Candy_Corn_text_icon.png}" + " " +  str(self.get_required_Candy_Corn(player))+ " "
            if(self.get_required_Chocolate(player) > 0.9): the_string = the_string + "{image=Chocolate_text_icon.png}" + " " +  str(self.get_required_Chocolate(player))+ " "
            if(self.get_required_Trick_Supplies(player) > 0.9): the_string = the_string + "{image=Trick_Supplies_text_icon.png}" + " " +  str(self.get_required_Trick_Supplies(player))+ " "
            the_string = the_string + "\nRewards: "
            if(self.get_reward_Victory_Candy(player) > 0.9): the_string = the_string + "{image=Victory_Candy_text_icon.png}" + " " +  str(self.get_reward_Victory_Candy(player)) + " "
            if(self.get_reward_Candy_Corn(player) > 0.9): the_string = the_string + "{image=Candy_Corn_text_icon.png}" + " " +  str(self.get_reward_Candy_Corn(player))+ " "
            if(self.get_reward_Chocolate(player) > 0.9): the_string = the_string + "{image=Chocolate_text_icon.png}" + " " +  str(self.get_reward_Chocolate(player))+ " "
            if(self.get_reward_Trick_Supplies(player) > 0.9): the_string = the_string + "{image=Trick_Supplies_text_icon.png}" + " " +  str(self.get_reward_Trick_Supplies(player))+ " "
            the_string = the_string + "\n"
            the_string = the_string + self.reward_effect_description
            return the_string
###############################################################################################
##########################################################################################################
#############################################################################################################
#                                      QUEST OBJECTS 
#############################################################################################################
##########################################################################################################
###############################################################################################
    # ID,name,description,requirements,FOREST,LABEL,rewards,reward_effect_description
    #rquirements[Victory_Candy , Candy_Corn , Chocolate , Trick_Supplies]
    #rewards[Victory_Candy , Candy_Corn , Chocolate , Trick_Supplies , Reward Effect Function]
    def do_nothing():
        return True

    q0 =  Quest(0 , "Investigate the Ghost House"       ,"Parents set up a ghost house can you get through?"  ,[0,0,8,0] ,False,"L1" ,[4,2,0,0,do_nothing],  "No effects in this version")
    q1 =  Quest(1 , "Lone kid at the playground?"       ,"The kid there hasn't moved for 3 hours now?!"       ,[4,6,6,0] ,False,"L2" ,[4,6,6,0,do_nothing],  "No effects in this version")
    q2 =  Quest(2 , "Odd Sightings at the train Station","No , it's not drunk people."                        ,[0,0,0,0] ,False,"L3" ,[2,0,0,0,do_nothing],  "No effects in this version")
    q3 =  Quest(3 , "Bribeing kids"                     ,"Give them Candy , to get more Candy."               ,[2,0,0,0] ,False,"L4" ,[0,4,4,0,do_nothing],  "No effects in this version")
    q4 =  Quest(4 , "School at Night"                   ,"Lot's of scarry stuff."                             ,[0,4,0,4] ,False,"L5" ,[3,0,3,0,do_nothing],  "No effects in this version")   
    q5 =  Quest(5 , "Placeholder Text"                  ,"Placeholder Description"                            ,[1,1,1,1] ,False,"L6" ,[1,1,1,1,do_nothing],  "No effects in this version")
    q6 =  Quest(6 , "Codeing Quests the true Horror"    ,"I want to get out."                                 ,[0,0,1,0] ,False,"L7" ,[0,0,1,0,do_nothing],  "No effects in this version")
    q7 =  Quest(7 , "Going EA headquaters"              ,"Explore Hell on earth."                             ,[0,0,0,10],False,"L8" ,[0,0,0,0,do_nothing],  "No effects in this version not even lootboxes")
    q8 =  Quest(8 , "Potatoe"                           ,"Why does Kisa need a server?"                       ,[0,0,0,0] ,False,"L9" ,[1,1,1,1,do_nothing],  "No effects in this version")
    q9 =  Quest(9 , "a"                                 ,"The cutest thing I have ever seen."                 ,[0,10,0,0],False,"L10",[5,0,1,0,do_nothing],  "No effects in this version")
    q10 = Quest(10, "Investigate Ghost Lights"          ,"Blueish lights dance arround at the Cemetary?"      ,[0,8,0,0] ,False,"L11",[3,4,2,0,do_nothing],  "No effects in this version")
    q11 = Quest(11, "Retive the Stolen Candy"           ,"How did it get stolen?!"                            ,[0,6,0,4] ,False,"L12",[5,0,0,0,do_nothing],  "No effects in this version")
    q12 = Quest(12, "Ghost Attack"                      ,"People can't punch ghosts but you are magical righ?",[0,3,0,3] ,False,"L13",[3,0,0,0,do_nothing],  "No effects in this version")
    q13 = Quest(13, "What lurks in the sewers"          ,"Greenish Slime? Clowns? Candy?"                     ,[0,12,0,2],False,"L14",[10,0,0,0,do_nothing], "No effects in this version")

    q14 = Quest(14, "Scareing Parents"                  ,"Let out the monster within you."                    ,[0,0,0,4] ,False,"L15",[2,0,2,0,do_nothing],  "No effects in this version")

    q15 = Quest(15,"Monster Ball"                      ,"Infiltrate a costume party, and steal the candy."   ,[0,0,0,0] ,False,"L16",[0,8,0,0,do_nothing],  "No effects in this version")
   
    q16 = Quest(16, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[0,8,2,0] ,True ,"L17",[7,0,0,0,do_nothing],  "No effects in this version") #1
    q17 = Quest(17, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[4,6,6,4] ,True ,"L18",[5,2,2,10,do_nothing], "No effects in this version") #2
    q18 = Quest(18, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[0,0,0,0] ,True ,"L19",[3,0,0,0,do_nothing],  "No effects in this version") #3
    q19 = Quest(19, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[0,12,0,0],True ,"L20",[5,4,2,2,do_nothing],  "No effects in this version") #4
    q20 = Quest(20, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[4,0,0,0] ,True ,"L21",[0,0,0,0,do_nothing],  "No effects in this version") #5
    q21 = Quest(21, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[0,0,12,0],True ,"L22",[5,3,1,1,do_nothing],  "No effects in this version") #6
    q22 = Quest(22, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[2,8,4,0] ,True ,"L23",[8,0,0,0,do_nothing],  "No effects in this version") #7
    q23 = Quest(23, "Forest Quest"                      ,"Wander off into the haunted(?) forest"              ,[1,2,0,0] ,True ,"L24",[2,1,1,1,do_nothing],  "No effects in this version") #8

    qList = [q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23]
    

