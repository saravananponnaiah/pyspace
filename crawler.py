import requests

url = 'https://www.natgeokids.com/uk/discover/geography/general-geography/facts-about-diwali/'

response = requests.get(url)
if response.status_code == 200:
    print("Fetch the response content")
    print(response.text)
else:
    print("Error in fetching data from website")