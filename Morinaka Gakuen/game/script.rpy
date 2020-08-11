# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Junko")


# The game starts here.

label start:
    # Opens on Junko chained up in a police van

    scene bg van

    "When people say \"How did I get here,\" I'm pretty sure they mean philosophically."

    "They're thinking about all the choices they made to get to some big moment, either good or bad."

    "Funny enough in this case, I do know how I got here, philosophically speaking. I know exactly where my shit choices brought me."
    "I've spent the last four years in juvie because of them."

    "However, physically speaking, I have no idea how I got here, in this van."
    "Well, that's not quite true, I know that the guards took my out of my cell, put me in handcuffs and tossed me in the back of said van..."
    "But after that I'm fucking baffled."
    "There's absolutely no reason I should be here. My sentence isn't remotely over, I'm not twenty, so no adult facility for me..."
    "...and I was never given the option of parole."
    "If something in my situation changed, I assume someone would tell me, not put a sack over my head and throw me into a car."

    menu:

        "Where are you taking me?":
            jump nosass

        "You taking me to the gallows or something?":
            jump sass

    label nosass:

        j "Where are you taking me?"
        j "No one told me about a transfer."

        jump van

    label sass:

        j "Finally taking the rabid old dog out back, huh?"
        j "I mean, in dog years I made it pretty far..."

        jump van

    label van:
    "Prison Guard" "Can it, kid!"

    "I don't bother asking anything else. Getting information out of guards is like getting blood from a stone."
    "And the last thing I want is to give this guy another excuse to rough me up."
    "I sit in silence for the rest of the ride."
    "..."
    "..."

    scene bg forest 01
    with fade
    "The door slams open, and I'm dragged out into the dappled sunlight of a forest."
    "The van I just came out of is on a dirt road, and a little ways away I can see a concrete path leading deeper into the wood."
    "Beside me, I hear the guard dial on his phone. Whoever he's calling picks up on the first ring, but I can't hear what he says."
    "Prison Guard" "Come get her."
    "He hangs up."



    return
