from django.shortcuts import render
from folium import *
from geocoder import *

def home(request):
	if request.GET.get("city"):
		city = request.GET.get("city")
		try:
			data = osm(city )
			loc = [data.lat, data.lng]
			f = Figure(width=500, height=500)
			ct = Map(location=loc, zoom_start=13).add_to(f)
			Marker(loc, tooltip="<b>"+ city +"<b>").add_to(ct)
			ct_html = ct._repr_html_()
			return render(request, "home.html", {"msg":ct_html})
		except Exception as e:
			return render(request, "home.html", {"msg":"city not found " + str(e)})
	else:
		return render(request,"home.html")
