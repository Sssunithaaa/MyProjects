import tkinter
class convertor:
    conversion_rates = {
        "USD":1,
        "INR":83
    }
    def convert(self,from_currency,to_currency,amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = self.conversion_rates[to_currency]*amount
        return amount
c=convertor()
print(c.convert('USD','INR',1))

