animal = input("Enter animal: ").lower()

if animal in ["eagle", "parrot", "pigeon", "crow"]:
    print("Animal can fly")
elif animal in ["penguin", "ostrich", "emu"]:
    print("Animal cannot fly")
else:
    print("Unknown animal")
