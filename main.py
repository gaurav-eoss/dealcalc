from mortgage import Mortgage, InsuredMortgage

try:
    bad = InsuredMortgage(-780000,70000,0.0549,25)

except ValueError as e:
    print("Error:", e)  

insured = InsuredMortgage(780000,70000,0.0549,25)
print(insured.loan_amount(), insured.monthly_payment())

m = Mortgage(780_000, 70_000, 0.0549, 25)
rows = m.schedule()
print(rows[0])     # first month
print(rows[-1])    # last month; -1 means "the last item"