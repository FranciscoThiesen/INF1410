from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map
from home import Home
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect
import database
import googlemaps
from datetime import datetime

app = Flask(__name__)
api_key = ''

with open('.env') as f:
    api_key = f.readline()
    api_key = api_key.rstrip('\n')
    f.close()

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

    homes = database.get_homes_list()
    rmarkers = gen_markers(homes)

    mymap = Map(
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
        markers = rmarkers,
        zoom="16"
    )
    
    return render_template('map.html', sndmap=mymap)

@app.route("/", methods=["POST"])
def get_form():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        tel = request.form['telefone']
        email = request.form['_email']
        vagas = int(request.form['vagas'])
        rua = request.form['rua']
        cep = request.form['cep']
        num = int(request.form['num'])
        apt = int(request.form['apt'])
        dscp = request.form['descricao']
        tipo = request.form['_type']

    gmaps = googlemaps.Client(key=api_key)
    try:
        geocode_result = gmaps.geocode(str(num)+' '+ rua +', Rio de Janeiro, '+ 'RJ')
        #print(geocode_result[0]['geometry']['location'])
        lat = float (geocode_result[0]['geometry']['location']['lat'])
        lng = float (geocode_result[0]['geometry']['location']['lng'])
    except:
        print("Unable to get latitude and longitude from address")
        raise(ValueError)
    
    h = Home(lat, lng, tipo, vagas, dscp, nome, cpf, tel, cep, rua, tipo, num)

    database.insert_data(h)       

    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)

