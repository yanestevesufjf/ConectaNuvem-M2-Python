import requests

response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=ea6521fa2ea884d4671f8174ff9cf46f')

filme_550 = response.json()

print(filme_550['homepage'])