import requests

def get_weather_desc_and_temp():
    api_key = "632617355ed24b15af9f2226ca8194df"
    city = "Spokane"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get('description')
    temp_min = json.get("main").get('temp_min')
    temp_max = json.get("main").get('temp_max')

    return {"description": description, 
        "temp_min": temp_min,
        "temp_max": temp_max}



weather_dict = get_weather_desc_and_temp()

print("Today's forecase is", weather_dict.get('desctiption'))
print("The low for today is", weather_dict.get('temp_min'))
print("The high for today is", weather_dict.get('temp_max')) 

