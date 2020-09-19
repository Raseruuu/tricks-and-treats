init python:
    global Turn = 0
    # global place_ARRAY = [
    #     place_1,place_2,place_3,place_4,place_5,place_6,place_7,
    #     place_8,place_9,place_10,place_11,place_12,place_13,place_14,
    #     place_15,place_16]


    class Player:
      def __init__(self):
        self.Victory_Candy = 0
        self.Candy_Corn = 0
        self.Chocolate = 0
        self.Trick_Supplies = 0
        # a modifier for double , half or other calculations
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


      def receive_from_place_Victory_Candy(self,VC_ammount,place_ID):
        VC_amount = VC_amount * self.Victory_Candy_mod_place[place_ID][Turn]
        if(VC_amount != 0):
          VC_amount = VC_amount + self.Victory_Candy_ADD_place[place_ID][Turn]
          self.Victory_Candy = self.Victory_Candy + int(VC_amount)

# this segment in the player class:

  # self.agent_base = 2
  # self.agent_count = 2
  #
  # self.my_places = []
  #
  # def occupy(self,place_ID):
  #     self.agent_count--
  #     self.my_places.append(place_ARRAY[place_ID])
  #     place_ARRAY[place_ID].occupied = True
  #
### THIS TYPE OF FUNCTION NEEDS TO BE IN PLAYER TOO and for all resources
  # def change_mod_Victory_Candy(self,amount,durration,instant,SET):
  #   if(SET == True):
  #     if(instant == True):
  #       for(i = Turn,i <= durration+Turn , i++):
  #         self.Victory_Candy_mod[i] =  amount
  #     else:
  #       for(i = Turn+1,i <= durration+Turn+1 , i++):
  #         self.Victory_Candy_mod[i] = amount
  #   else:
  #     if(instant == True):
  #       for(i = Turn,i <= durration+Turn , i++):
  #         self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount
  #     else:
  #       for(i = Turn+1,i <= durration+Turn+1 , i++):
  #         self.Victory_Candy_mod[i] = self.Victory_Candy_mod[i] * amount
