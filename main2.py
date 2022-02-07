def get_spn(json_response):
    spn = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
    upperCorner = spn['upperCorner'].split(' ')
    lowerCorner = spn['lowerCorner'].split(' ')
    return [str(float(upperCorner[0]) - float(lowerCorner[0])),
            str(float(upperCorner[1]) - float(lowerCorner[1]))]
