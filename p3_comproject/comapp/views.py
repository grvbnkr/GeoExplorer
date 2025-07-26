from django.shortcuts import render
from folium import *
import requests # Import the requests library for direct API calls

def home(request):
    if request.GET.get("city"):
        city = request.GET.get("city")
        try:
            # Nominatim API endpoint for search
            nominatim_url = "https://nominatim.openstreetmap.org/search"

            # Parameters for the API request
            params = {
                'q': city,
                'format': 'json', # Request JSON format
                'limit': 1,        # Limit to 1 result
                'addressdetails': 1 # Include address details
            }

            headers = {
                'User-Agent': 'CityMapLocator/1.0 (grvbnkr@example.com)',
                'Referer': 'https://github.com/grbnkr/GeoExplorer' # Or your actual app URL
            }

            # Make the GET request to Nominatim
            response = requests.get(nominatim_url, params=params, headers=headers)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

            data = response.json()

            if data and len(data) > 0:
                # Extract latitude and longitude from the first result
                lat = float(data[0].get('lat'))
                lon = float(data[0].get('lon'))
                loc = [lat, lon]

                f = Figure(width=500, height=500)
                # Create the map and add to the figure
                ct = Map(location=loc, zoom_start=13).add_to(f)
                Marker(loc, tooltip="<b>"+ city +"<b>").add_to(ct)
                ct_html = f._repr_html_() # Get HTML from the Figure object
                return render(request, "home.html", {"msg": ct_html})
            else:
                # No results found for the city
                return render(request, "home.html", {"msg": f"City '{city}' not found."})

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 403 Forbidden, 404 Not Found)
            return render(request, "home.html", {"msg": f"HTTP error occurred: {http_err} - Please check your User-Agent and Referer headers."})
        except requests.exceptions.ConnectionError as conn_err:
            # Handle connection errors (e.g., no internet connection)
            return render(request, "home.html", {"msg": f"Connection error occurred: {conn_err} - Could not connect to the geocoding service."})
        except requests.exceptions.Timeout as timeout_err:
            # Handle timeout errors
            return render(request, "home.html", {"msg": f"Timeout error occurred: {timeout_err} - The request to the geocoding service timed out."})
        except requests.exceptions.RequestException as req_err:
            # Handle any other request-related errors
            return render(request, "home.html", {"msg": f"An unexpected request error occurred: {req_err}"})
        except Exception as e:
            # Catch any other general exceptions during the process
            return render(request, "home.html", {"msg": "An unexpected error occurred: " + str(e)})
    else:
        # Initial load of the page without a city query
        return render(request, "home.html")
