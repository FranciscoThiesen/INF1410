from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
api_key = '' 

with open('.env') as f:
    api_key = f.readline()
    f.close()


GoogleMaps(app, key = api_key)

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "zIndex:999;"
        ),
        lat=-22.978993,
        lng=-43.233160,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': -22.97900,
             'lng': -43.232999,
             'infobox': "<b>Apartamento compartilhado ( 2 Vagas )</b>",
             'zIndex' : 999
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
             'lat': -22.97800,
             'lng': -43.234999,
             'infobox': "<b>República Feminina</b>",
             'zIndex' : 999
          }
        ],
        zoom="17"
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
