# recommendation/views.py
import requests

def get_weather_data(city):
    api_key = 'cbf75fe89a1cce4844462c1b094da096'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()
# recommendation/utils.py
# recommendation/utils.py

# recommendation/utils.py

def extract_features(weather_data, soil_content):
    if weather_data and soil_content:
        # Extract weather features
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        # Extract soil content features
        nitrogen = soil_content.nitrogen
        phosphorus = soil_content.phosphorus
        potassium = soil_content.potassium
        ph_level = soil_content.ph_level
        # Add more features as needed
        return temperature, humidity, wind_speed, nitrogen, phosphorus, potassium, ph_level
    else:
        return None


# Example usage:
# temperature, humidity, wind_speed = extract_features(weather_data)

# recommendation/utils.py

import csv

import csv

# recommendation/utils.py
import csv

def recommend_crop(weather_data):
    optimal_conditions = {}
    with open('crop_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            crop = row['crop']
            optimal_conditions[crop] = {
                'optimal_temperature': int(row['optimal_temperature']),
                'optimal_humidity': int(row['optimal_humidity']),
                'optimal_nitrogen': float(row['optimal_nitrogen']),  # Assuming nitrogen is a column in the CSV
                'optimal_phosphorus': float(row['optimal_phosphorus']),  # Assuming phosphorus is a column in the CSV
                'optimal_potassium': float(row['optimal_potassium']),  # Assuming potassium is a column in the CSV
                'optimal_ph_level': float(row['optimal_ph_level'])  # Assuming ph_level is a column in the CSV
            }

    current_temperature = weather_data['main']['temp']
    current_humidity = weather_data['main']['humidity']

    # Assuming you have weather data but not soil content data
    # You should modify this part to fetch soil content data if available
    nitrogen = None
    phosphorus = None
    potassium = None
    ph_level = None

    best_crop = None
    min_difference = float('inf')

    for crop, conditions in optimal_conditions.items():
        temp_difference = abs(current_temperature - conditions['optimal_temperature'])
        humidity_difference = abs(current_humidity - conditions['optimal_humidity'])
        nitrogen_difference = abs(nitrogen - conditions['optimal_nitrogen']) if nitrogen is not None else 0
        phosphorus_difference = abs(phosphorus - conditions['optimal_phosphorus']) if phosphorus is not None else 0
        potassium_difference = abs(potassium - conditions['optimal_potassium']) if potassium is not None else 0
        ph_level_difference = abs(ph_level - conditions['optimal_ph_level']) if ph_level is not None else 0

        total_difference = temp_difference + humidity_difference + nitrogen_difference + phosphorus_difference + potassium_difference + ph_level_difference

        if total_difference < min_difference:
            best_crop = crop
            min_difference = total_difference

    return best_crop



# recommendation/views.py

from django.shortcuts import render
from .forms import LocationForm


def indexrec(request):
    form = LocationForm()
    recommended_crop = None
    weather_data = None

    if request.method == 'POST':
        form = LocationForm(request.POST) 
        if form.is_valid():
            city = form.cleaned_data['location']
            weather_data = get_weather_data(city)
            recommended_crop = recommend_crop(weather_data)

    return render(request, 'crop/index.html', {'form': form, 'recommended_crop': recommended_crop, 'weather_data': weather_data})
# fertilizer recommendations
from django.shortcuts import render
import pandas as pd

def fert_recommend(request):
    title = 'Harvestify - Fertilizer Suggestion'

    if request.method == 'POST':
        crop_name = request.POST.get('cropname')
        N = int(request.POST.get('nitrogen'))
        P = int(request.POST.get('phosphorous'))
        K = int(request.POST.get('pottasium'))
        
        df = pd.read_csv('fertilizer.csv')

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":  
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        recommendation = fertilizer_dic[key]

        return render(request, 'crop/fertilizer-result.html', {'recommendation': recommendation, 'title': title})
    # , {'recommendation': recommendation, 'title': title}

    return render(request, 'crop/fertilizer-predict.html', {'title': title})

fertilizer_dic = {
    # Define your fertilizer recommendations here as in the Flask code
    'NHigh': """The N value of soil is high and might give rise to weeds.
        <br/> Please consider the following suggestions:

        <br/><br/> 1. <i> Manure </i> – adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.

        <br/> 2. <i>Coffee grinds </i> – use your morning addiction to feed your gardening habit! Coffee grinds are considered a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious, delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also help provide increased drainage to your soil.

        <br/>3. <i>Plant nitrogen fixing plants</i> – planting vegetables that are in Fabaceae family like peas, beans and soybeans have the ability to increase nitrogen in your soil

        <br/>4. Plant ‘green manure’ crops like cabbage, corn and brocolli

        <br/>5. <i>Use mulch (wet grass) while growing crops</i> - Mulch can also include sawdust and scrap soft woods""",

        'Nlow': """The N value of your soil is low.
        <br/> Please consider the following suggestions:
        <br/><br/> 1. <i>Add sawdust or fine woodchips to your soil</i> – the carbon in the sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.

        <br/>2. <i>Plant heavy nitrogen feeding plants</i> – tomatoes, corn, broccoli, cabbage and spinach are examples of plants that thrive off nitrogen and will suck the nitrogen dry.

        <br/>3. <i>Water</i> – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving less for your plants to use.

        <br/>4. <i>Sugar</i> – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar concept to adding sawdust/woodchips which are high in carbon content.

        <br/>5. Add composted manure to the soil.

        <br/>6. Plant Nitrogen fixing plants like peas or beans.

        <br/>7. <i>Use NPK fertilizers with high N value.

        <br/>8. <i>Do nothing</i> – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.""",

        'PHigh': """The P value of your soil is high.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Avoid adding manure</i> – manure contains many key nutrients for your soil but typically including high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.

        <br/>2. <i>Use only phosphorus-free fertilizer</i> – if you can limit the amount of phosphorous added to your soil, you can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.

        <br/>3. <i>Water your soil</i> – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.

        <br/>4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).

        <br/>5. Use crop rotations to decrease high phosphorous levels""",

        'Plow': """The P value of your soil is low.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Bone meal</i> – a fast acting source that is made from ground animal bones which is rich in phosphorous.

        <br/>2. <i>Rock phosphate</i> – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.

        <br/>3. <i>Phosphorus Fertilizers</i> – applying a fertilizer with a high phosphorous content in the NPK ratio (example: 10-20-10, 20 being phosphorous percentage).

        <br/>4. <i>Organic compost</i> – adding quality organic compost to your soil will help increase phosphorous content.

        <br/>5. <i>Manure</i> – as with compost, manure can be an excellent source of phosphorous for your plants.

        <br/>6. <i>Clay soil</i> – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.

        <br/>7. <i>Ensure proper soil pH</i> – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.

        <br/>8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.

        <br/>9. If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH""",

        'KHigh': """The K value of your soil is high</b>.
        <br/> Please consider the following suggestions:

        <br/><br/>1. <i>Loosen the soil</i> deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.

        <br/>2. <i>Sift through the soil</i>, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.

        <br/>3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and to begin using only organic matter to enrich the soil.

        <br/>4. Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.

        <br/>5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.

        <br/>6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.
        """,

        'Klow': """The K value of your soil is low.
        <br/>Please consider the following suggestions:

        <br/><br/>1. Mix in muricate of potash or sulphate of potash
        <br/>2. Try kelp meal or seaweed
        <br/>3. Try Sul-Po-Mag
        <br/>4. Bury banana peels an inch below the soils surface
        <br/>5. Use Potash fertilizers since they contain high values potassium
        """
}

