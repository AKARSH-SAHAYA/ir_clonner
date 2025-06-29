from machine import Pin #type:ignore
import time 


ir_signal=[]
time_stamp=[]
def counter(Pin):
  time_stamp.append(time.ticks_us())
  
ir = Pin(18,Pin.IN)
ir.irq(trigger= Pin.IRQ_FALLING | Pin.IRQ_RISING,handler= counter)


while True:
    if time_stamp:
       
        for i in range(len(time_stamp)-1):
           ir_signal.append(time_stamp[i+1]-time_stamp[i])
       
        print("Captured IR timings (in microseconds):", ir_signal)
        ir_signal.clear()
        time_stamp.clear()
    time.sleep(1)