power = input("Is computer turning on? (yes/no): ")
display = input("Is display working? (yes/no): ")
internet = input("Is internet working? (yes/no): ")

if power == "no":
    print("Possible power supply problem")
elif display == "no":
    print("Possible monitor or display problem")
elif internet == "no":
    print("Possible network problem")
else:
    print("Computer is working normally")
