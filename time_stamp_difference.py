
import math
ir_signal =[ ]
ls=[2,5,9,12,18,25,35]
for i in range(len(ls)-1):
    ir_signal.append(ls[i+1]-ls[i])

print(ir_signal)    