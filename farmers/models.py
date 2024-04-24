# farmers/models.py
from django.db import models
from django.db.models import Q
import requests

class Farmer(models.Model):
    mobile_number = models.CharField(max_length=20)
    land_quantity_sq_ft = models.PositiveIntegerField()
    city = models.CharField(max_length=100)

    def matching_landowners(self):
        return LandOwner.objects.filter(city=self.city, land_quantity_sq_ft=self.land_quantity_sq_ft, full_name=self.full_name)

    def approx_nearby_cities(self):
        city_data = self.get_city_geolocation(self.city)
        if city_data:
            lat = city_data['lat']
            lon = city_data['lon']
            print("approx_nearby_cities")
            print(lat)
            print(lon)
            api_url = f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=10&appid=cbf75fe89a1cce4844462c1b094da096"
            response = requests.get(api_url)
            if response.status_code == 200:
                nearby_cities = response.json()['list']
                nearby_cities_with_land_owners = []
                for city in nearby_cities:
                    city_name = city['name']
                    land_owners = LandOwner.objects.filter(city=city_name)
                    for owner in land_owners:
                        if owner.land_quantity_sq_ft < 500 or owner.land_quantity_sq_ft > 500:
                            city_info = {
                                'name': city_name,
                                'lat': city['coord']['lat'],  # Collect latitude
                                'lon': city['coord']['lon'],
                                'land_owners': [{'mobile_number': owner.mobile_number, 'quantity_of_land': owner.land_quantity_sq_ft,'Name':owner.full_name}]
                            }
                            nearby_cities_with_land_owners.append(city_info)
                            
                            break  # No need to check other land owners for this city
                return nearby_cities_with_land_owners
        return []
    def nearby_cities(self):
        # Get latitude and longitude for the current city
        city_data = self.get_city_geolocation(self.city)
        if city_data:
            lat = city_data['lat']
            lon = city_data['lon']
            print("lop",lat)
            print(lon)
            # Query the API to get nearby cities within 100km radius
            api_url = f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=10&appid=cbf75fe89a1cce4844462c1b094da096"
            response = requests.get(api_url)
            if response.status_code == 200:
                nearby_cities = response.json()['list']
                nearby_cities_with_owners = []
                for city in nearby_cities:
                    city_name = city['name']
                    city_coordinates = {'lat': city['coord']['lat'], 'lon': city['coord']['lon']}
                    # Check if land owners exist for this city
                    land_owners = LandOwner.objects.filter(city=city_name)
                    if land_owners.exists():
                        city_info = {
                            'name': city_name,
                            'coordinates': city_coordinates,
                            'land_owners': [{'mobile_number': owner.mobile_number, 'quantity_of_land': owner.land_quantity_sq_ft,'Name':owner.full_name} for owner in land_owners]
                        }
                        nearby_cities_with_owners.append(city_info)
                return nearby_cities_with_owners
        return []
    def nearby(self):
        city_data = self.get_city_geolocation(self.city)
        if city_data:
            lat = city_data['lat']
            lon = city_data['lon']
            api_url = f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=10&appid=cbf75fe89a1cce4844462c1b094da096"
            response = requests.get(api_url)
            if response.status_code == 200:
                nearby_cities = response.json()['list']
                print( [{'name': city['name']} for city in nearby_cities])
                return [{'name': city['name']} for city in nearby_cities]
        return []
    def get_city_geolocation(self, city):
        # Query the API to get geolocation data for the city
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cbf75fe89a1cce4844462c1b094da096"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if 'coord' in data:
                return {'lat': data['coord']['lat'], 'lon': data['coord']['lon']}
        return None
    # def approx_nearby_cities_with_coordinates(self):
    #     nearby_cities = self.approx_nearby_cities()
    #     cities_with_coordinates = []
    #     for city in nearby_cities:
    #         city_name = city.get('name')
    #         if city_name:
    #             coordinates = self.get_city_coordinates(city_name)
    #             if coordinates:
    #                 city_info = {
    #                     'name': city_name,
    #                     'lat': coordinates['lat'],
    #                     'lng': coordinates['lng']
    #                 }
    #                 cities_with_coordinates.append(city_info)
    #     return cities_with_coordinates
# -------------------------------------------------------------------
    def approx_nearby_cities_with_coordinates(self):
        # Get latitude and longitude for the current city
        city_data = self.get_city_geolocation(self.city)
        if city_data:
            lat = city_data['lat']
            lon = city_data['lon']
            print("lop",lat)
            print(lon)
            # Query the API to get nearby cities within 100km radius
            api_url = f"https://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt=10&appid=cbf75fe89a1cce4844462c1b094da096"
            response = requests.get(api_url)
            if response.status_code == 200:
                nearby_cities = response.json()['list']
                cities_with_coordinates = []
                for city in nearby_cities:
                    city_name = city['name']
                    city_coordinates = {'lat': city['coord']['lat'], 'lon': city['coord']['lon']}
                    # Check if land owners exist for this city
                    land_owners = LandOwner.objects.filter(city=city_name)
                    if land_owners.exists():
                        city_info = {
                            
                            'coordinates': city_coordinates
                            
                        }
                        cities_with_coordinates.append(city_info)
                return cities_with_coordinates
        return []
# ----------------------------------------------------------------
    def get_city_coordinates(self, city):
        # Use a geocoding service to get coordinates for the given city
        api_key = 'AIzaSyCubrkDsRSs9uBIKtDIbnrU5es7V23H6zA'  # Replace with your Google Maps API key
        geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={api_key}'
        response = requests.get(geocode_url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                print({'lat': location['lat'], 'lng': location['lng']})
                return {'lat': location['lat'], 'lng': location['lng']}
        return None
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LandOwner(models.Model):
    full_name = models.CharField(max_length=100,default='DEFAULT VALUE')
    mobile_number = models.CharField(max_length=20)
    land_quantity_sq_ft = models.PositiveIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    document = models.FileField(upload_to='landowner_documents/',null=True)

    def __str__(self):
        return self.full_name

