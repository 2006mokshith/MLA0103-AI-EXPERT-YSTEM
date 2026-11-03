symptoms = input("Enter symptoms separated by spaces: ").lower().split()

if "fever" in symptoms and "cough" in symptoms:
    print("Possible respiratory infection")
elif "headache" in symptoms and "fever" in symptoms:
    print("Possible fever-related illness")
elif "sneezing" in symptoms and "runny_nose" in symptoms:
    print("Possible common cold")
else:
    print("Disease not identified")

print("Consult a healthcare professional.")
