import requests
from bs4 import BeautifulSoup
class currency:
    def __init__(self,find_country):
        self.find_country = find_country
    def find(self,find_country):
        url='https://www.iban.com/currency-codes'
        user_agent = { 'User-agent': 'Chrome/58.0.3029.110' }
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        currency_table = soup.find('tbody')
        currency_codes = ['INR','CHF',]
        currency_names = []
        countries = ['INDIA','SWITZERLAND',]
        for row in currency_table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 4:
                currency_code = columns[2].text.strip()
                currency_name = columns[1].text.strip()
                country = columns[0].text.strip()
                currency_codes.append(currency_code)
                currency_names.append(currency_name)
                countries.append(country)
        find_country = find_country.lower()
        country_found = False
        currency_code_found=""
        for i,country in enumerate(countries):
            if find_country in country.lower():
                currency_code_found=currency_codes[i]
                country_found=True
                break
        return currency_code_found
class convertor:
    def __init__(self,base_url):
        data=requests.get(base_url).json()
        self.conversion_rates = data["conversion_rates"]
    def convert(self,from_currency,to_currency,amount):
        if from_currency != 'EUR':
            amount = self.conversion_rates[to_currency]*amount
        return amount
from_currency=input("Please specify the country from which you wish to convert currency:\n")
b=currency(from_currency)
from_code=(b.find(from_currency))
to_currency = input("Please specify the country to which you wish to convert currency:\n")
s=currency(to_currency)
to_code=s.find(to_currency)
amount=float(input("Enter the amount you wish to convert:"))
url = str.__add__('https://v6.exchangerate-api.com/v6/c45ae5d3c4f82967446cb736/latest/', from_code)
c=convertor(url)
converted_amount=c.convert(from_code,to_code,amount)
print(f"{amount} {from_code} = {converted_amount} {to_code}")


