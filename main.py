import machine
import utime
import random

in1_pin = machine.Pin(1, machine.Pin.OUT)  
in2_pin = machine.Pin(2, machine.Pin.OUT)  

in3_pin = machine.Pin(4, machine.Pin.OUT)  
in4_pin = machine.Pin(5, machine.Pin.OUT)  

ena_pin = machine.Pin(3, machine.Pin.OUT)
enb_pin = machine.Pin(6, machine.Pin.OUT)  

trig_pin = machine.Pin(19, machine.Pin.OUT)  
echo_pin = machine.Pin(20, machine.Pin.IN)  

enb_pin.value(1)  
ena_pin.value(1)

def girar_motores_frente():
    in1_pin.value(1)  
    in2_pin.value(0)  
    in3_pin.value(1)  
    in4_pin.value(0)  

def girar_motores_tras():
    in1_pin.value(0)  
    in2_pin.value(1)  
    in3_pin.value(0)  
    in4_pin.value(1)  

def medir_distancia():
    trig_pin.value(0)
    utime.sleep_us(2)
    trig_pin.value(1)
    utime.sleep_us(10)
    trig_pin.value(0)
    
    while echo_pin.value() == 0:
        pass
    pulse_start = utime.ticks_us()
    
    while echo_pin.value() == 1:
        pass
    pulse_end = utime.ticks_us()
    
    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    distancia = (pulse_duration * 0.0343) / 2  
    return distancia

def parar_motor_aleatoriamente():
    if random.choice([True, False]):
        in1_pin.value(0)
        utime.sleep(0.5)
        in1_pin.value(1)
    else:
        in3_pin.value(0)
        utime.sleep(0.5)
        in3_pin.value(1)
    
    enb_pin.value(1)  
    utime.sleep(0.8)  
    enb_pin.value(1)  
    girar_motores_frente()

def controle_robo():
    girar_motores_frente()  
    
    while True:
        distancia = medir_distancia()
        print("Distância:", distancia)
        if distancia <= 16:  
            girar_motores_tras()
        elif distancia <= 30:  
            parar_motor_aleatoriamente()
        else:
            girar_motores_frente()
        
        utime.sleep(0.05)  

controle_robo()
