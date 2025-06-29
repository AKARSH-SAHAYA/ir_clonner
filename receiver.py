from machine import Pin #type:ignore
import time 

ir_signal=[]
def counter(Pin):
  ir_signal.append(time.ticks_us())
  
ir= Pin(18,Pin.IN)
ir.irq(trigger= Pin.IRQ_FALLING | Pin.IRQ_RISING,handler= counter())


while True:
    if ir_signal:
        print("Captured IR timings (in microseconds):", ir_signal)
       
    time.sleep(1)