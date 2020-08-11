# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Junko")


# The game starts here.

label start:
    # Opens on Junko chained up in a police van

    scene bg van

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "When people say \"How did I get here,\" I'm pretty sure they mean philosophically."

    "They're thinking about all the choices they made to get to some big moment, either good or bad."

    "Funny enough in this case, I do know how I got here, philosophically speaking. I know exactly where my shit choices brought me."

    "However, physically speaking, I have no idea how I got here."

    j "Where are you taking me?"

    "Prison Guard" "Can it, kid!"

    "I don't bother asking anything else. Getting information out of guards is like getting blood from a stone."


    return
