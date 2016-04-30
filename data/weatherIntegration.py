import pyowm
import matplotlib.pyplot as plt
import json
from energyPerTemp import getRegressionAt

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

def getRegressionEnergy():
    mean_temperatures = getMeanTemperatures()
    extrapol_energies = []
    for t in mean_temperatures:
        extrapol_energy = getRegressionAt(t)
        extrapol_energies.append(extrapol_energy)
    return extrapol_energies

    
def getJSON():
    dump = []
    temps = getMeanTemperatures()
    energies = getRegressionEnergy()
    for i in range(0,len(temps)):
        dump.append({"temperature" : temps[i], "energy" : energies[i]})
    return dump

def main():
    print getJSON()

if __name__ == "__main__":
    main()
