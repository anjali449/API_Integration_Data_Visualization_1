import requests
import matplotlib.pyplot as plt

#Replace this with your actual OpenWeatherMap API key
API_KEY = '75786a60b2ddf6fe11912b390f7547d6'  # 🔴 Get from https://openweathermap.org/api
CITY = 'Hyderabad'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

#Fetch data
response = requests.get(URL)
data = response.json()

# Check if the API call was successful
if response.status_code == 200:
    #Extract temperature and time
    temperatures = []
    timestamps = []

    for item in data['list'][:10]:  #Get data for first 10 time slots
        temp = item['main']['temp']
        time = item['dt_txt']
        temperatures.append(temp)
        timestamps.append(time)

    #Visualize using matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', color='blue')
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print(f"Error: API call failed with status code {response.status_code}. Message: {data.get('message', 'Unknown error')}")
