citizens = {
    "2005-05-10": "Mokshith",
    "2004-08-15": "Rahul",
    "2003-12-20": "Arjun"
}

dob = input("Enter date of birth (YYYY-MM-DD): ")

if dob in citizens:
    print("Citizen Name:", citizens[dob])
else:
    print("Record not found")
