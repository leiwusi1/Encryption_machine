from set import *
import main_produce
import main_decoding
class text():
    def __init__(self):
        self.txt = ""

    def input_txt(self,z):
        self.txt = z
    def produce(self):
        self.txt = main_produce.produce(self)
    def decoding(self):
        self.txt = main_decoding.decoding(self)





