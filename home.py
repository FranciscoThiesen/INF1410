#!/bin/python3

class Home:
    def __init__(self, latitude, longitude, _type, vagas, description):
        self.lat = latitude
        self.lng = longitude
        self._type = _type
        self.vagas = vagas
        self.description = description

    def update_vagas(self):
        self.vagas -= 1
        return self.vagas

    def get_atts(self):
        lst = [self.lat, self.lng, self.description]
        return lst
      

""" if __name__ == "__main__":
    h1 = Home(-22.97900, -43.232999, "apartamento", 2, "Apartamento compartilhado")
    h2 = Home(-22.97800,  -43.234999, "republica", 3, "República Feminina")
    homes = [h1, h2]
    keys = ['lat', 'lng', 'infobox', 'zIndex', 'icon']
    dft = [999, "http://maps.google.com/mapfiles/ms/icons/green-dot.png"]
    atts = [h1.get_atts() + dft, h2.get_atts() + dft]
    mmarkers = []
    for i in range(0, len(homes)):
        mmarkers.append(dict(zip(keys, atts[i])))
    print(mmarkers) """
