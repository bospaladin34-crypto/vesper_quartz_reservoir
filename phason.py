import time, math
NU_P = 0.17259029
F0 = 15.965
def tick(t: float):
    angle = 2*math.pi*F0*t
    return complex(NU_P*math.cos(angle), NU_P*math.sin(angle))
