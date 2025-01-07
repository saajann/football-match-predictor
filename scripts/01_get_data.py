import requests
import json
import csv

with open('config.json', 'r') as file:
    config = json.load(file)
api_key = config.get('API_KEY')

url = 'https://api.football-data.org/v4/competitions/SA/matches'
headers = {'X-Auth-Token': api_key}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    matches = response.json()
    
    # Save JSON data
    with open('data/serie_a_matches.json', 'w') as jsonfile:
        json.dump(matches, jsonfile, indent=4)
    
    # Save CSV data
    with open('data/serie_a_matches.csv', 'w', newline='') as csvfile:
        fieldnames = matches['matches'][0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for match in matches['matches']:
            writer.writerow(match)
else:
    print(f"Failed to retrieve data: {response.status_code}")