def diagnose(disease):
    if disease == "flu":
        fever = input("Does patient have fever? ")
        cough = input("Does patient have cough? ")

        if fever == "yes" and cough == "yes":
            return True

    return False

goal = "flu"

if diagnose(goal):
    print("Possible flu detected")
else:
    print("Flu rule not satisfied")
