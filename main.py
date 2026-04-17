import random
import time

print("This in no way shape or form is supposed to make fun of, or hurt Jay (jay is the East Coast RM if you didn't know btw.)")

time.sleep(1)


random_responses = [":neocat-floof-explode:", "yep", "ok got it", "oo", "hehe", "LMAO", "oop why?", "bruh", "ik ik", "LOL", "ayyy", "lmao" ]

if __name__ == "__main__":
    for i in "iiiiiiiiiiiiiiiiiiiiiiiiii":
        prompt = input("Talk to Jay")

        if "hcb" in prompt.lower():
            print("hmm, i'll talk to alfie")


        elif "blueprint" in prompt.lower():
            print("debt... debt... DEBT")

        elif "jay dont" in prompt.lower() or "jay don't" in prompt.lower():
            print("Leo taught me how to mute that")

        elif "unc" in prompt.lower():
            print("i'm not dev sob")

        else:
            print(random.choice(random_responses))