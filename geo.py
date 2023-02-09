import requests

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def geocode(address):
    geocoder_request = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        'apikey': API_KEY,
        'geocode': address,
        'format': 'json'
    }

    response = requests.get(geocoder_request, params=geocoder_params)
    json_response = response.json()
    features = json_response['response']['GeoObjectCollection']['featureMember']
    return features[0]['GeoObject']


def get_ll_span(address):
    toponym = geocode(address)
    toponym_coord = toponym['Point']['pos']
    long, lat = toponym_coord.split(' ')
    ll = ','.join((long, lat))
    envelope = toponym['boundedBy']['Envelope']
    l, b = envelope['lowerCorner'].split(' ')
    r, t = envelope['upperCorner'].split(' ')
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0
    span = f'{dx},{dy}'

    return ll, span


def get_coordinates(address):
    toponym = geocode(address)
    toponym_coord = toponym['Point']['pos']
    long, lat = toponym_coord.split(' ')
    return float(long), float(lat)
