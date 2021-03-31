from gpiozero import LED, PWMLED
import time

# pps to rpm conversion
# Full Step 1.8° → 1000 pps / 200 Steps = 5 Rev. per Second x 60 = 300 RPM

payload = {
    'connection': True,
    'status': "IDLE",
    'pps_fwd': 500, # forward speed
    'pps_rev': 1000,  # reverse speed
    'fwd_timer': 10, # forward run
    'rev_timer': 10, # reverse run
    'fwd_halt': 2, # wait after running forward
    'rev_halt': 20,  # wait after running reverse
    'counter': 5
}

# GPIO config
global step

direction = LED(pin=19, active_high=False, initial_value=1)  # Black
enable = LED(pin=20, active_high=False, initial_value=1)  # White
step = PWMLED(pin=21, active_high=False, initial_value=1,
              frequency=payload['pps_fwd'])  # Gray

# Current time: print(time.strftime("%H:%M:%S", time.localtime()))

def forward():
    payload['status'] = "forward"
    step.frequency = payload['pps_fwd']
    direction.off()
    enable.on()
    step.value = 0.5  # 50% of frequency

def stop():
    step.value = 0  # Off
    enable.off()
    direction.off()
    payload['status'] = "IDLE"

def reverse():
    if payload['status'] == "IDLE":
        step.frequency = payload['pps_rev']
        payload['status'] = "reverse"
        direction.on()
        enable.on()
        step.value = 0.5  # 50% of frequency

def runforward():
    forward()
    time.sleep(payload['fwd_timer'])
    stop()
    payload['status'] = "IDLE"

def runreverse():
    reverse()
    time.sleep(payload['rev_timer'])
    stop()
    payload['status'] = "IDLE"

def loop():
    payload['status'] = "looping"
    counter = payload['counter']
    while counter > 0:
        print(counter)
        counter -= 1
        runforward()
        time.sleep(payload['fwd_halt'])
        runreverse()
        time.sleep(payload['rev_halt'])
    else:
        payload['status'] = "IDLE"

# Main
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    loop()
    
    # print("forward")
    # # stop()
    # print("stop")
    # time.sleep(5)
    # reverse()
    # print("reverse")
    # time.sleep(10)
    # stop()
    # print("stop")
    
    
