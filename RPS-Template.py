import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RPS_Game:

    def __init__(self, choice_list):
        self.computerChoice = choice_list[random.randint(0, len(choice_list)-1)]
        self.computerScore = 0
        self.userScore = 0

    def check_Winner(self, user_Choice):
        pass

    def ask_Choice_Webcam(self):
        pass

    def ask_Choice(self):
        while True:
            user_Choice = input("Enter a choice of: r - rock, p - paper, s - scissors").lower()
            lengthOfChoice = len(user_Choice)
            if lengthOfChoice > 1:
                print("Please, enter just one character")
                continue
            asciiChar = ord(user_Choice)
            choices_ToAscii = [112, 114, 115] #Ascii codes for p, r, s (rock paper scissors)
            if not asciiChar in choices_ToAscii:
                continue
            else:
                break
        self.check_Winner(user_Choice)

def play_RPS(choice_list):
    game = RPS_Game(choice_list)
    
if __name__ == '__main__':
    choice_list = ['rock', 'paper', 'scissors']
    play_RPS(choice_list)