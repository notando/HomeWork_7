import urllib.request, json

#openning a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=5d809c29233da8e068f7")

#decode responce to str
data = json.loads(url.read().decode())          #decoding a web request

#parcing results

results = data['results']
ILS_USD = results['ILS_USD']
currency = ILS_USD['val']

print("Welcome to currency converter")
try:
    amount = float(input("Please enter an amount of shekeles to convert:"))
    res = amount * currency
    print(round(res, 2))
except ValueError:
    print("Invalid Choice")
print('Thanks for using our currency converter')
