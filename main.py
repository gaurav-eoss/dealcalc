from mortgage import Mortgage, InsuredMortgage

try:
    bad = InsuredMortgage(-780000,70000,0.0549,25)

except ValueError as e:
    print("Error:", e)  

insured = InsuredMortgage(780000,70000,0.0549,25)
print(insured.loan_amount(), insured.monthly_payment())