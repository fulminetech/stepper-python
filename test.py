from gpiozero import LED, PWMLED
import time

direction = LED(pin=19, active_high=False, initial_value=1)  # Black
enable = LED(pin=20, active_high=False, initial_value=1) # White
step = PWMLED(pin=21, active_high=False, initial_value=1, frequency=600) # Gray 

# Data format: Dictonary
payload = {
    'connection': True,
    'status': "IDLE",
    'direction': "Forward",
    'pps': 0,
    'timer1': 10,
    'timer2': 2
}

# Current time: print(time.strftime("%H:%M:%S", time.localtime()))

def runforward():
    print("Forward")
    direction.off()
    enable.on()
    step.value = 0.5  # 50% of frequency
    print(time.strftime("%H:%M:%S", time.localtime()))
    time.sleep(payload['timer1'])
    print(time.strftime("%H:%M:%S", time.localtime()))
    step.value = 0  # Off
    enable.off()


def runreverse():
    print("Reverse")
    direction.on()
    enable.on()
    step.value = 0.5  # 50% of frequency
    print(time.strftime("%H:%M:%S", time.localtime()))
    time.sleep(payload['timer1'])
    print(time.strftime("%H:%M:%S", time.localtime()))
    step.value = 0  # Off
    enable.off()
    direction.off()

# Main
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    runforward()
    print("Waiting for 10 seconds")
    time.sleep(payload['timer2'])
    runreverse()
    # print("Waiting for 10 seconds")
    # time.sleep(payload['timer2'])
