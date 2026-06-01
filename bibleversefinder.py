import requests
verse = input("Enter a verse you are looking for ?")

url = f"https://bible-api.com/{verse}"

response = requests.get(url)

data = response.json()

print(data["reference"])
print(data["text"])