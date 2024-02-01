import requests

url = "https://football-pro.p.rapidapi.com/api/v2.0/fixtures/11867339"

querystring = {"include":"stats","tz":"Europe/Amsterdam"}

headers = {
	"X-RapidAPI-Key": "e4813eefc4msh22f23665b1c6eabp14e427jsna2d1b1e61863",
	"X-RapidAPI-Host": "football-pro.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())