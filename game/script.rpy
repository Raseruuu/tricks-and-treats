# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    playername = "Sayako"

define p = Character("[playername]")
define a = Character("A")
define v = Character("Vampire")
define f = Character("Fox")
define s = Character("Slime")
define ?? = Character("??")

define narrator = Character("Narrator", type='narrator')

# The game starts here.

label start:

    scene bg room

    p "Hello!!"
    "World!"

    # This ends the game.

    return


label Vampire_1:
# Vampire
    a "Hey boss"
    a "What are you doing up there?"
    v "Don't you know? The higher the spot the easier it is to observe the battlefield."
    a "But it's dangerous up there."
    v "I'm the mighty Lord Vermillion the 4th, this little wind means absolutely nothing to me."
    a "Sure thing boss."
    v "I can see everything from here, this is perfect."
    v "From here I shall be able to plan my next move."
    v "Hmmmph?"
    v "Hey what's that kid doing here?"

    "*The vampire slides down from top of the slides and approaches the medjed.*"

    v "Hi."
    ?? "...."
    v "A quiet one huh? What's your name?"
    v "My name is [ ] and I'm going to get all the rare candies tonight."
    v  "Now, are you going up against us?"
    ?? "..."
    v "Or are you going to stay out of the way?"
    ?? "..."
    v "I see how this is."
    v "You don't have many candies so far in your basket…"
    v "hmmmph~!"
    v "I know!"
    v "yo guys, this one is coming with us!"
    a "What!??"
    v "You heard me, they are now one of our forces."
    v "Say hello to the new recruit"
    ?? "(no movements)"
    v "SEE."
    a "boss I don't think this is a good idea?"
    v "What do you mean by that?!"
    v "we need extra people so they're coming with us."
    v "Alright let's go--"
    "The hand she grabs is a bit colder than expected, and the kid refuses to budge."
    v "We are going now."
    "Another tug, and it's as stationary as a rock."
    v "ho~~~???"
    v "You coming or not?"
    "no response"
    "still no response."
    a "Come on boss, we need to get moving."
    v "Just a second."
    "*ruffle noises*"
    v "Aha!"
    v "There, we got plenty of candies here."
    v "So if you help us we can get a lot more."
    v "What says you? You in?"
    "slight nod from the Medjed."
    v "Alright that does it."
    "Another tug, nothing."
    v "Yo, give me the rope."
    a "Yes, here."
    v "Let's carry this one, don't drop it."
    a "I have a bad feeling about this…"
    v "Tie them up and put them on your shoulders, let's move out!"
    v "Heave! Ho! Heave! Ho!"
    a "Heave…."
    # System Message: +1 Agent
    return
label Fox_1:
    # Fox
    f "So...this is a playground?"
    a "yeah there's the slide, and the swings, and that's the seesaw over there."
    a "We come by to play whenever we want to."
    f "Sounds fun."
    a "Wanna try?"
    f "sure!"

    f "Ah!"
    # *medjed appears
    f "...hello?"
    # *fox hides behind the other kids*
    a "Hey! Hello there."
    a "You wanna play as well?"
    ?? "..."
    a "Oh come on~"
    f "Are you lost?"
    f "Ah I see."
    f "Er...we got candy with us."
    f "You want one?"
    # *small movement from medjed
    f ":D"
    f "Are you waiting for someone?"
    f "No?..."
    f "Would you like to join us?"
    a "Yeah, we are getting the candies. Let's do it together!"
    a "It's gonna be fun."
    "Fox reaches out to grab their hand, not moving."
    f "Ah yeah, here you can have one."
    # *Candy given

    f "Shall we?"
    ?? "..."
    a "Hurray! New friend!"
    f "hey keep it down please."
    a "But now we got more friends to share candies with."
    f "hmmmmm"
    f "what do you say?"
    ?? "..."
    f "ok then."
    a "Let's gooooo."
    return
label Slime_1:
    # Slime
    s "you sure this is the correct shortcut?"
    a "yeah we just need to cut through this playground and it'll be there in a hot minute."
    s "But there's not enough lights here..."
    s "Can we please go a bit faster? I don't like empty swings."
    a "It's going to be fineee."
    s "I surely hope so, I don't want to see any-- HEEEK!"
    # *medjed appears
    s "see!?"
    s "now we got something there."
    a "Huh?"
    a "Oh it's just another kid."
    s "Another kids my behind. They're not even moving!"
    s "let's get out of here asap."

    a "I think it's also collecting candies…"
    s "then let's give it one and leave them be."
    a "Sure thing."
    a "Hey here, you can have this."
    # *medjed
    "small reaction from the kid before a candy is thrown into their basket"
    a "See, nothing to worry about."
    s "Gosh I just don't like how eerie it feels."
    s "I got all the heebie jeebies."
    a "But I thought you like the ghost stu--"
    s "Not this kind! I am not good with those blanket ghosts."
    a "Okay…?"

    s "Let's just get out of here."
    s "We still need to get to--"
    # *medjed appears right behind slime
    s "Heeeeeek!"
    s "Why is it following me?"
    a "I dunno, maybe it wants more candies?"
    s "You were the one who gave them candy so why meee??"
    a "Hmm"
    a "iunno"
    s "That's not helping at all!"
    s "Please stop following me...heeee…"
    ?? "..."
    s "so...I'm just going...to leave now…"

    "Slime's coat is being tugged."
    s "AAAAAAAAHHHHHH"
    s "I'm so dead I'm so dead I'm so dead."
    s "I hate this I hate this I hate this."
    # *both quickly disappear."
    a "Hey, wait up, don't leave me here~~"

    # System Message: +1 Agent
    return
