MONTHS_PER_YEAR = 12

class Mortgage:

    """A fixed rate Canadian Mortgage Calculator"""    

    def __init__(self, purchase_price: float, down_payment: float, annual_rate: float, years: int):

        if purchase_price <=0:
            raise ValueError("Purchase price must be positive")

        if annual_rate <=0 or annual_rate >= 1:
            raise ValueError('Annual rate should be between 0 and 1') 
        
        if down_payment < 0 or down_payment > purchase_price:
            raise ValueError('Down payment is less than 0 or greater than purchase price') 
        
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.annual_rate = annual_rate
        self.years = years

    def __repr__(self) -> str:
        return (f'{type(self).__name__}(price=${self.purchase_price:,.0f}, '
                f"down=${self.down_payment:,.0f}, "
                f"rate={self.annual_rate:.2%}, years={self.years})")            

    def monthly_payment(self) -> float :
        monthly_rate = (1+self.annual_rate/2) ** (1/6)-1
        n = self.years * MONTHS_PER_YEAR
        return self.loan_amount() * monthly_rate / (1-(1+monthly_rate) ** -n)

    def loan_amount(self) ->float:
        return self.purchase_price - self.down_payment

    def schedule(self) -> list[dict]:
        monthly_rate = (1+self.annual_rate/2) ** (1/6)-1
        payment = self.monthly_payment()
        balance = self.loan_amount()
        rows = []

        for month in range(1, self.years * MONTHS_PER_YEAR + 1):
            interest = balance * monthly_rate
            principal = payment - interest
            balance = balance - principal
            rows.append({"month":month, "interest": interest, "principal": principal, "balance": balance})

        return rows
    
class InsuredMortgage(Mortgage):
    
    def premium_rate(self) -> float:
        pass

    def loan_amount(self) -> float:
        base = super().loan_amount()

        return base
    