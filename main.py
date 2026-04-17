import random

prompt = input("Talk to Jay")

random_responses = [":neocat-floof-explode:", "yep", "ok got it", "oo", "hehe", "LMAO", "oop why?", "bruh" ]


if "hcb" in prompt.lower():
    print("hmm, i'll talk to alfie")


elif "blueprint" in prompt.lower:
    print("debt... debt... DEBT")

else:
    print(random.choice(random_responses))
    


