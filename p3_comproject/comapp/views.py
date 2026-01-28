from django.shortcuts import render
import folium
import requests


def home(request):
    if request.GET.get("city"):
        city = request.GET.get("city").strip()

        try:
            response = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params={
                    "q": city,
                    "format": "json",
                    "limit": 1,
                    "polygon_geojson": 1
                },
                headers={
                    "User-Agent": "GeoExplorer/1.0 (contact: grvbnkr.com)"
                },
                timeout=15
            )
            response.raise_for_status()
            data = response.json()

            if not data:
                return render(request, "home.html", {"msg": f"City '{city}' not found."})

            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            geojson = data[0].get("geojson")

        except Exception as e:
            return render(request, "home.html", {"msg": f"Error: {e}"})

        # Create map
        location = [lat, lon]
        city_map = folium.Map(location=location, zoom_start=12)

        folium.Marker(
            location,
            tooltip=f"<b>{city.title()}</b>"
        ).add_to(city_map)

     
        if geojson:
            folium.GeoJson(
                geojson,
                name=f"{city.title()} boundary",
                style_function=lambda x: {
                    "fillColor": "#3186cc",
                    "color": "#3186cc",
                    "weight": 2,
                    "fillOpacity": 0.2
                }
            ).add_to(city_map)

        return render(request, "home.html", {
            "msg": city_map._repr_html_()
        })

    return render(request, "home.html")
