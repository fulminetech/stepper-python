from gpiozero import LED, PWMLED
import time

direction = LED(pin=19, active_high=False, initial_value=1)  # Black
enable = LED(pin=20, active_high=False, initial_value=1) # White
step = PWMLED(pin=21, active_high=False, initial_value=1, frequency=2000) # Gray 

# Data format: Dictonary
payload = {
    'connection': True,
    'status': "IDLE",
    'direction': "Forward",
    'pps': 0,
    'timer1': 20,
    'timer2': 10
}

current_time = time.strftime("%H:%M:%S", time.localtime())

def runforward():
    print("Forward")
    direction.off()
    enable.on()
    time.sleep(1)
    step.value = 0.5  # 50% of frequency
    print(current_time)
    time.sleep(payload['timer1'])
    print(current_time)
    step.value = 0  # Off
    enable.off()


def runreverse():
    print("Reverse")
    direction.on()
    enable.on()
    time.sleep(1)
    step.value = 0.5  # 50% of frequency
    print(current_time)
    time.sleep(payload['timer1'])
    print(current_time)
    step.value = 0  # Off
    enable.off()
    direction.off()

# Main
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    # runforward()
    # time.sleep(payload['timer2'])
    runreverse()
    # time.sleep(payload['timer2'])
