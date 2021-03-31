from gpiozero import LED, PWMLED

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


direction = LED(19)
enable = LED(20)
step = PWMLED(pin=21, active_high=True, initial_value=0, frequency=500)

# Data format: Dictonary
payload = {
    'connection': True,
    'status': "IDLE",
    'direction': "Forward",
    'pps': 0,
    'timer1': 0, 
    'timer2': 0 
}

def runforward():
    direction.off()
    enable.on()
    sleep(1)
    step.value = 0.5 # 50% of frequency
    sleep(payload['timer1'])
    step.value = 0 # Off
    enable.off()

def runreverse():
    direction.on()
    enable.on()
    sleep(1)
    step.value = 0.5 # 50% of frequency
    sleep(payload['timer1'])
    step.value = 0 # Off
    enable.off()
    direction.off()

def loop(count):
    if count == 777:
        direction.off()
        enable.on()
        sleep(2)
        step.value = 0.5 # 50% of frequency
        sleep(payload['timer1'])
        step.value = 0 # Off
        direction.on()
        sleep(2)
        step.value = 0.5 # 50% of frequency
        sleep(payload['timer2'])
        step.value = 0 # Off
        enable.off()
    elif count > 0:
        direction.off()
        enable.on()
        sleep(2)
        step.value = 0.5 # 50% of frequency
        sleep(payload['timer1'])
        step.value = 0 # Off
        direction.on()
        sleep(2)
        step.value = 0.5 # 50% of frequency
        sleep(payload['timer2'])
        step.value = 0 # Off
        enable.off()
        # -count

        
class Set(Resource):
    def get(self, parameter, frequency, timer1):
        if parameter == "forward":
            payload['status'] = parameter
            payload['frequency'] = frequency
            payload['timer1'] = timer1
            return "Status: "+payload['status']+" frequency: "+payload['frequency']+" timer1: "+payload['timer1']
            runforward()
        elif parameter == "stop":
            return value
        else:
            return "Invalid Command"


# Class for Payload API
class Payload(Resource):
    def get(self, subsection):
        if subsection == "status":
            return payload
        else:
            return "Invalid Command"

# API Declaration
api.add_resource(Payload, '/stepper/<subsection>')

api.add_resource(Set, '/set/<parameter>/<frequency>/<timer1>')


# Start Server
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    app.run(debug=True)