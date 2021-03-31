from gpiozero import LED, PWMLED
import time

direction = LED(19)
enable = LED(20)
step = PWMLED(pin=21, active_high=True, initial_value=0, frequency=500)

# Data format: Dictonary
payload = {
    'connection': True,
    'status': "IDLE",
    'direction': "Forward",
    'pps': 0,
    'timer1': 20,
    'timer2': 0
}

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def runforward():
    print("Forward "+payload['timer1'])
    direction.off()
    enable.on()
    time.sleep(1)
    step.value = 0.5  # 50% of frequency
    print(current_time)
    time.sleep(payload['timer1'])
    step.value = 0  # Off
    enable.off()


# Start Server
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    runforward()
