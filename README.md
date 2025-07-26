# GeoExplorer
A simple Django web application that allows users to enter a city name and see its location marked on an interactive map. This project uses folium to render maps and geocoder to convert city names into geographical coordinates.

Features
City Search: Users can input a city name on the homepage.

Interactive Map Display: If the city exists, an interactive map centered on the city's coordinates is displayed.

Marker: A marker is placed on the map at the specified city's location.

Error Handling: Provides feedback to the user if the city is not found or if there's an issue with the geocoding service.

Technologies Used
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

Folium: A powerful Python library that helps you visualize geospatial data. It builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library.

geocoder: A Python library that provides a simple way to geocode addresses and locations using various geocoding services.

HTML & CSS: For structuring and styling the web page.

Setup and Installation
Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

1. Clone the Repository
First, clone the project repository to your local machine:

git clone https://github.com/grvbnkr/GeoExplorer.git

cd GeoExplorer

2. Create a Virtual Environment (Recommended)
It's good practice to use a virtual environment to manage project dependencies:

python -m venv venv

3. Activate the Virtual Environment
On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

4. Install Dependencies
Install all the required Python packages using pip:

pip install Django folium geocoder

5. Run the Development Server
Navigate to the directory containing manage.py and run the Django development server:

python manage.py runserver

6. Access the Application
Open your web browser and navigate to the following URL:

http://127.0.0.1:8000/

Usage
Upon opening the application, you will see an input field labeled "enter city name".

Type the name of a city into this field (e.g., "London", "New York", "Paris").

Click the "Show on Map" button.

If the city is successfully located, an interactive map will appear below the form, showing the city's location with a marker.

If the city cannot be found or there's an error, a "city not found" message will be displayed.

Project Structure
GeoExplorer/
├── p3_comproject/         
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home_app/                
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── templates/
│       └── home.html
├── manage.py               
├── .gitignore              
└── README.md               
