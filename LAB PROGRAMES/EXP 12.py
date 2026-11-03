income = float(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if income >= 30000 and credit >= 700:
    print("Loan Approved")
else:
    print("Loan Rejected")
