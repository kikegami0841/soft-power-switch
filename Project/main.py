from machine import Pin
import time

def main():
    # ピン番号定義
    LED_PIN = 25      #OnBoard
    RELAY_PIN = 20    #26
    SW_PIN = 22       #29
    PI_ZERO_SENS_PIN = 21 #27
    VIRTUAL_VDD_PIN = 18
    
    # スリープ時間定義
    SLEEP_SHORT = 0.5
    SLEEP_LONG = 1.0
    
    DEC_TIME = 10
    LED_OFF = 0
    LED_ON = 1
    RELAY_OFF = 0
    RELAY_ON = 1
    VIRTUALVDD_OFF = 0
    VIRTUALVDD_ON = 1
    led = Pin(LED_PIN, Pin.OUT) #25
    Relay = Pin(RELAY_PIN, Pin.OUT) #26
    Sw = Pin(SW_PIN, Pin.IN, Pin.PULL_DOWN) #29
    PiZeroSens = Pin(PI_ZERO_SENS_PIN, Pin.IN, Pin.PULL_DOWN) #27
    VirtualVDD = Pin(VIRTUAL_VDD_PIN, Pin.OUT) #24
    VirtualVDD.value(VIRTUALVDD_ON)
    
    VirtualVDD.value(VIRTUALVDD_ON)
    Relay.value(RELAY_OFF)
    
    while True:
        Sw_BK = 0
        s = 0
        led.value(LED_OFF)
        time.sleep(SLEEP_SHORT)
        print('State 0')
        while True:
            if (s == 1) & (Sw_BK == s):
                break
            #print(s, Sw_BK)
            time.sleep(SLEEP_SHORT)
            Sw_BK = s
            s = Sw.value()
            
        Relay.value(RELAY_ON)
        print('State 1')
        while True:
            if (PiZeroSens.value() == 1):
                break
            led.value(LED_ON)
            time.sleep(SLEEP_SHORT)
            led.value(LED_OFF)
            time.sleep(SLEEP_SHORT)
            print(PiZeroSens.value())
            
        led.value(LED_ON)
        print('State 2')
        while True:
            if (PiZeroSens.value() == 0):
                break
            led.value(LED_ON)
            time.sleep(SLEEP_LONG)
            print(PiZeroSens.value())
            
        print('State 3')
        Timer = DEC_TIME
        while True:
            if (Timer == 0):
                led.value(LED_OFF)
                break
            led.value(LED_ON)
            time.sleep(SLEEP_SHORT)
            led.value(LED_OFF)
            time.sleep(SLEEP_SHORT)
            print(PiZeroSens.value(), Timer)
            Timer -= 1
            
        Relay.value(RELAY_OFF)


if __name__ == "__main__":
    main()

