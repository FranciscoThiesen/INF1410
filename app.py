from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from home import Home
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api_key = ''

with open('.env') as f:
    api_key = f.readline()
    api_key = api_key.rstrip('\n')
    f.close()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base.db'

GoogleMaps(app, key = api_key)


def gen_markers(homes):
    keys = ['lat', 'lng', 'infobox', 'zIndex', 'icon']
    dft = [999, "http://maps.google.com/mapfiles/ms/icons/green-dot.png"]

    atts = []
    for  i in range(0, len(homes)):
        atts.append(homes[i].get_atts() + dft)
    
    mmarkers = []
    for i in range(0, len(homes)):
        mmarkers.append(dict(zip(keys, atts[i])))
    
    return mmarkers

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )


    h1 = Home(-22.97900, -43.232999, "apartamento", 2, "Apartamento compartilhado")
    h2 = Home(-22.97800,  -43.234999, "republica", 3, "República Feminina")
    h3 = Home(-22.97900,  -43.235000, "acampamento", 1, "morte")
    homes = [h1, h2, h3]
    rmarkers = gen_markers(homes)

    
    sndmap = Map(
        identifier="sndmap",
        style=(
            "height:75%;"
            "width:50%;"
            "top:100px;"
            "left:550px;"
            "position:absolute;"
            "zIndex:999;"
        ),
        lat=-22.978993,
        lng=-43.233160,
        markers= rmarkers,
        zoom="17"
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
