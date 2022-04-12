import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RPS_Game:

    def __init__(self, choice_list):
        pass

    def check_Winner(self, user_Choice):
        pass

    def ask_Choice_Webcam(self):
        pass

    def ask_Choice(self):
        pass

def play_RPS(choice_list):
    pass
    
if __name__ == '__main__':
    pass