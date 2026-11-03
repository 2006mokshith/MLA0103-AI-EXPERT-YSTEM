age = int(input("Enter age: "))
fever = input("Fever (yes/no): ")
cough = input("Cough (yes/no): ")

if fever == "yes" and cough == "yes":
    print("Possible respiratory infection")
elif fever == "yes":
    print("Possible fever-related illness")
else:
    print("No matching symptoms")

print("This is a basic demonstration, not a medical diagnosis.")
