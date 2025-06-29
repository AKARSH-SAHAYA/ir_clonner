
import math
ir_signal =[ ]
ls=[2,5,9,12,18,25,35]
for i in range(len(ls)-1):
    ir_signal.append(abs(ls[i]-ls[i+1]))

print(ir_signal)    