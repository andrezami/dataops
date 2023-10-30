import requests

urls = ['https://swapi.dev/api/films/', 'https://swapi.dev/api/people/', 'https://swapi.dev/api/planets/']

for url in urls:
        response = requests.get(url)
        assert response.status_code == requests.codes.ok