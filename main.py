# Importing the Flask class along with the request and Response Objects
from flask import Flask, request, Response
# Importing the BolT modules
from boltiot import Bolt
# Importing the configuration file
import conf 
# Importing the request module to send http requests
import requests
# Importing the json object to read the data received from the bolt cloud(As the data format is JSON)
import json

# Instantiate Flask class with a name of __name__ before assignment it to the app variable
app = Flask(__name__)
# Instantiating the BoLT object using API KEY and Device Id
mybolt = Bolt(conf.BOLT_API_KEY, conf.DEVICE_ID)


def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if request fails"""
    try:
        # Requesting the BoLT cloud to send the data from the cloud about the specified PIN
        response = mybolt.analogRead(pin)
        # Converting the response into JSON object
        data = json.loads(response)
        # Returning the sensor value
        return int(data["value"])
    except Exception as e: # If some problem occur I have setup exception handler
        print("Something went wrong when reading the sensor value")
        print(e)
        return -999

# app.route is a decorator to listen for POST requests made against the /temperatureRead path
# The decorator calls the function that immediately follows it when a request is made to the route
# In this case the function is respond that will be called
@app.route('/temperatureRead', methods=['POST']) # change it to post for getting request from ifttt
def respond():
    print(request.json)

    # Retrieving the A0 sensor value
    sensor_value = get_sensor_value_from_pin("A0")
    if sensor_value == -999:
        print("Request was unsuccessfull from sensor")
        return Response(status=200)

    # Converting the value obtained in Degree Celcius
    sensor_value = (100 * sensor_value) / 1024
    print("Value from sensor is: " + str(sensor_value))

    # Making an JSON object to be sent to IFTTT containg the information about the temperature
    dataToBeSend = {"value1":str(sensor_value), "value2":"", "value3":""}
    requests.post("https://maker.ifttt.com/trigger/receiveTemperature/with/key/" + conf.IFTTT_API_KEY, data=dataToBeSend)
    

    # This response tells that the sender that we received the hook
    return Response(status=200)