import numpy as np
NU_P = 0.17259029
PHI = 1.6180339887

class StomachionState:
    def __init__(self, seed: float):
        self.seed = seed % 1.0
        self.pieces = self._gen()
    def _gen(self):
        return np.array([[np.cos(self.seed*np.pi*(i+1)*PHI)*self.seed,
                          np.sin(self.seed*np.pi*(i+1)*PHI)*self.seed] for i in range(14)])
def boot_states(count=536):
    return [StomachionState((i*NU_P)%1.0) for i in range(count)]
