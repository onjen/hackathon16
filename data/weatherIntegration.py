import pyowm
import matplotlib.pyplot as plt
import json

def getMeanTemperatures():
    owm = pyowm.OWM('d95b2187ecedb799b74c2697226b234e')
    observation = owm.weather_at_place('aachen,de')
    w = observation.get_weather()
    forecaster = owm.daily_forecast('aachen,de',limit=7)
    forecast = forecaster.get_forecast()
    mean_temperatures = []
    for weather in forecast:
        temperature = weather.get_temperature('celsius')
        mean_temp = (temperature['min']+temperature['max'])/2
        mean_temperatures.append(mean_temp)
    return mean_temperatures
    
def getJSONMeanTemperatures():
    dump = json.dumps(getMeanTemperatures())
    return dump

def main():
    mean_temperatures = getMeanTemperatures()
    plt.plot(mean_temperatures)
    plt.show()

if __name__ == "__main__":
    main()
