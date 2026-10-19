from mortgage import Mortgage, InsuredMortgage


def main () -> None:
    try:
        bad = InsuredMortgage(-780000,70000,0.0549,25)

    except ValueError as e:
        print("Error:", e)  

    insured = InsuredMortgage(780000,70000,0.0549,25)
    print(insured.loan_amount(), insured.monthly_payment())

    m = Mortgage(780_000, 70_000, 0.0549, 25)
    rows = m.schedule()
    for row in rows:
        if row["month"] % 12 == 0:
            print("Year :",row["month"] //12 , ' Balance ', row["balance"])


if __name__ == "__main__":
    main()