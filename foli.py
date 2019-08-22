import folium 

#darle locacion al mapa
map = folium.Map(location=[42.3601, -71.0589],zoom_start=12)

#crear un tooltip
tooltip = "click for more info"

folium.Marker([42.363600, -71.099500],
                popup="<strong>Location one</strong>",
                tooltip=tooltip).add_to(map)




#guardar el mapa
map.save("folium.html")
