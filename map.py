import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
type = list(data["TYPE"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[19.246127, 72.863755], zoom_start=6, tiles = "Mapbox Bright")   #base Layer

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,ty,el in zip(lat,lon,type,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6,fill=1, popup=str(el)+" m",
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))   #marker Layer

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else
'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))     #polygon Layer

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl()) #add after adding fg; gives 2 options as there are 2 add_child

map.save("Map1.html")
