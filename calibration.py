from machine import Pin, ADC
import utime
import time

step1 = Pin(17, Pin.OUT)
direction1 = Pin(16, Pin.OUT)
step2 = Pin(19, Pin.OUT)
direction2 = Pin(18, Pin.OUT)
hall= Pin(22, Pin.IN)

#step_count=2000
#step_count2=2000
delay1=0.001
delay2=0.0005
delay1=0.005
delay2=0.001
is_tripped = False
list_o_time = []
ma_count = 5
magnet_count = 4
trip_count = 0
target_rpm = 10
rpm_error_bound = 2
motoruplimit = 500
motorlowlimit = -500
limitcount = 0

start_time=time.ticks_us()

def runCounterClockwise():
    direction1.low()
    direction2.low()
    step1.high()
    step2.high()
    time.sleep(delay2)
    step1.low()
    step2.low()
    time.sleep(delay1)

def runClockwise():
    direction1.high()
    direction2.high()
    step1.high()
    step2.high()
    time.sleep(delay2)
    step1.low()
    step2.low()
    time.sleep(delay1)



def calibrate():
    total_steps = 0
    mainDelay = 0.0001  #this is the main speed I think
    daInput = 0
    mynamejeff = input("clockwise/counterclockwise: ")
    while daInput != "end":
        daInput = input("How many steps: ")
        for x in range(int(daInput)):
            total_steps += 1
            
            if mynamejeff == "clockwise":
                runClockwise()
            elif mynamejeff == "counterclockwise":
                runCounterClockwise()
            if mynamejeff == "cw":
                runClockwise()
            elif mynamejeff == "ccw":
                runCounterClockwise()
                
            time.sleep(mainDelay)
    print(total_steps)
            
calibrate()
                
        
        
        
        
