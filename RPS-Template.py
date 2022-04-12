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
        if (user_Choice == self.computerChoice[0]):
            print("The result is a draw, you both chose {}!".format(self.computerChoice))
        else:
            if user_Choice == 'r':
                if self.computerChoice[0] == 's':
                    print('User wins! The computer Chose {}!'.format(self.computerChoice))
                    self.userScore += 1
                else:
                    print('Computer wins! The computer Chose {}!'.format(self.computerChoice))
                    self.computerScore += 1
            elif user_Choice == 'p':
                if self.computerChoice[0] == 'r':
                    print('User wins! The computer Chose {}!'.format(self.computerChoice))
                    self.userScore += 1
                else:
                    print('Computer wins! The computer Chose {}!'.format(self.computerChoice))
                    self.computerScore += 1
            elif user_Choice == 's':
                if self.computerChoice[0] == 'p':
                    print('User wins! The computer Chose {}!'.format(self.computerChoice))
                    self.userScore += 1
                else:
                    print('Computer wins! The computer Chose {}!'.format(self.computerChoice))
                    self.computerScore += 1

    def ask_Choice_Webcam(self):
        cap = cv2.VideoCapture(0)
        flag = False
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            if prediction[0][0] > 0.5:
                user_Choice = 'r'
            elif prediction[0][1] > 0.5:
                user_Choice = 'p'
            elif prediction[0][2] > 0.5:
                user_Choice = 's'
            else:
                user_Choice = 'n'
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('r') and flag == False:
                flag = True
                time_start = time.time()
            if flag == True:
                break

        cap.release()
        cv2.destroyAllWindows()
        self.check_Winner(user_Choice)

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

    while True:
        game.ask_Choice()
        game.computerChoice = choice_list[random.randint(0, len(choice_list)-1)]
    
if __name__ == '__main__':
    choice_list = ['rock', 'paper', 'scissors']
    play_RPS(choice_list)