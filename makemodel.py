import pickle
from linearreg import linearreg

class makemodel():
    def __init__(self):
        self.reg = linearreg().makemodel()

    def lrmodel(self):
        filename = 'LinReg.sav'
        pickle.dump(self.reg, open(filename, "wb"))


makemodel().lrmodel()
