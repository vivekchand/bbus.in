import requests

def clean(text):
    if text == 'Route Numbers':
        return 'bus_nos'
    return text

def table2json(rows):
    table_data = [[clean(cell.text) for cell in (row("td") or row("th"))]
                             for row in rows]

    keys = table_data[0]
    values = table_data[1:]
    hops = []
    for value in values:
        json_dict = {}
        c = 0
        for ele in value:
            json_dict[keys[c]] = ', '.join(ele.split(','))
            c+=1
        _from = u'{} Bus Stop, Bangalore'.format(json_dict['From'])
        _to = u'{} Bus Stop, Bangalore'.format(json_dict['To'])
        resp = requests.get(
            'https://maps.googleapis.com/maps/api/directions/json?'
            'origin={origin}&destination={destination}&key={key}&'
            'departure_time=now&mode=transit'.format(
                origin=_from,destination=_to,
                key='AIzaSyCNxasSekURQXrJ8eOlPEhQK8foxJ__WqE')).json()
        if resp['status'] == 'OK' and resp['routes'] \
                and resp['routes'][0]['legs'] and resp['routes'][0]['legs'][0]['distance']:
            json_dict['distance'] = resp['routes'][0]['legs'][0]['distance']['text']
            json_dict['duration'] = resp['routes'][0]['legs'][0]['duration']['text']
        else:
            json_dict['distance'] = None
            json_dict['duration'] = None
        hops.append(json_dict)
    return hops


