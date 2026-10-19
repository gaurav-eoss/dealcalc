MONTHS_PER_YEAR = 12

class Mortgage:

    """A fixed rate Canadian Mortgage Calculator"""    

    def __init__(self, purchase_price: float, down_payment: float, annual_rate: float, years: int):

        if purchase_price <=0:
            raise ValueError("Purchase price must be positive")
        
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.annual_rate = annual_rate
        self.years = years

    def monthly_payment(self) -> float :
        monthly_rate = (1+self.annual_rate/2) ** (1/6)-1
        n = self.years * MONTHS_PER_YEAR
        return self.loan_amount() * monthly_rate / (1-(1+monthly_rate) ** -n)

    def loan_amount(self) ->float:
        return self.purchase_price - self.down_payment




class InsuredMortgage(Mortgage):
    
    def premium_rate(self) -> float:
        pass

    def loan_amount(self) -> float:
        base = super().loan_amount()

        return base
    