# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colorProducer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:<h4>
        Height: %s m
        """

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Vocanoes")
fgp = folium.FeatureGroup(name="Populations")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=1000)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + "m", 
                                     radius=6, fill_color=colorProducer(el), color="grey", fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                                  style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
                                                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                            else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
