from django.shortcuts import render, redirect
from .models import Farmer, LandOwner
from .forms import FarmerForm, LandOwnerForm
from django.http import JsonResponse
import json
def farmer_registration(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            farmer = form.save()
            return redirect('farmers:matching_landowners', farmer_id=farmer.id)
    else:
        form = FarmerForm()
    return render(request, 'farmers/farmer_registration.html', {'form': form})

def landowner_registration(request):
    if request.method == 'POST':
        form = LandOwnerForm(request.POST)
        if form.is_valid():
            landowner = form.save()
            return redirect('farmers:success')
    else:
        form = LandOwnerForm()
    return render(request, 'farmers/landowner_registration.html', {'form': form})



import logging

# def matching_landowners(request, farmer_id):
#     try:
#         farmer = Farmer.objects.get(id=farmer_id)
#         matching_landowners = farmer.matching_landowners()  # Call matching_landowners method
#         nearby_cities = farmer.nearby_cities()  # Get nearby cities

#         return render(request, 'farmers/matching_landowners.html', {'farmer': farmer, 'nearby_cities': nearby_cities, 'matching_landowners': matching_landowners})
#     except Exception as e:
#         logging.error("An error occurred while fetching matching landowners: %s", str(e))
#         return render(request, 'farmers/error.html', {'error_message': str(e)})
def matching_landowners(request, farmer_id):
    farmer = Farmer.objects.get(id=farmer_id)
    matching_landowners = farmer.matching_landowners()
    nearby_cities = farmer.nearby_cities()
    approx_nearby_cities = farmer.approx_nearby_cities_with_coordinates()
    print("matching_landowners")
    print(approx_nearby_cities)
    # Extract coordinates
    coordinates = [{'lat': city['coordinates']['lat'], 'lng': city['coordinates']['lon']} for city in approx_nearby_cities]

    # Prepare data to pass to the template
    data = {
        'farmer': farmer,
        'matching_landowners': matching_landowners,
        'nearby_cities': nearby_cities,
        'coordinates': json.dumps(coordinates)  # Convert coordinates to JSON string
    }
    print("data",data)
    return render(request, 'farmers/matching_landowners.html', data)

def registration_success(request):
    return render(request, 'farmers/registration_success.html')

# -------------------------------------------------------------------


