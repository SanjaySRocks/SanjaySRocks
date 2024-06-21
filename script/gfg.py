import requests

url = "https://geeks-for-geeks-api.vercel.app/sanjaysinghg2u"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data['info']['totalProblemsSolved'])
else:
    print(f"Failed to retrieve data: {response.status_code}")
