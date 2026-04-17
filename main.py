import random

prompt = input("Talk to Jay")

random_responses = [":neocat-floof-explode:", "yep", "ok got it", "oo", "hehe", "LMAO", "oop why?", "bruh" ]


if "hcb" in prompt.lower():
    print("hmm, i'll talk to alfie")


elif "blueprint" in prompt.lower():
    print("debt... debt... DEBT")

elif "jay dont" or "jay don't" in prompt.lower():
    print("Leo taught me how to mute that")

elif "unc" in prompt.lower():
    print("i'm not dev sob")

else:
    print(random.choice(random_responses))
    


