# Rock, Paper, Scissors - A Computer Vision Introdcution Project

> Classic game of Rock Paper Scissors, with a best of 3 Winner!

> UML Diagram of Rock Paper Scissors Design
> ![image](https://user-images.githubusercontent.com/78024243/163031403-d4ffdd4b-d30a-41c6-af94-9e3903b1291d.png)

## Milestone 1: Create The model

For the Computer Vision aspect of the project, we will be using Teachable-Machine picture project to create a 4-class trained model. The 4 classes are;
Rock, Paper, Scissors and Nothing. Each of the 4 classes will then be filled with training images which consist of images captured through our webcam of me posing the 4 choices.
The Model is then trained on the input data images captured, where we then are given a fully trained model that can distinguish between Rock, Paper, Scissors by our webcam, thanks to Machine learning.

> ![image](https://user-images.githubusercontent.com/78024243/163061029-485921b7-1fff-4a0d-a279-2c94c20659b3.png)

With this, we then export it as a keras model, which we will use later, as the zip contains 2 files, the keras model, and it's corresponding labels txt file.

## Milestone 2: Install The dependencies

Next step before I could continue, I had to first create a new conda virtual environment for developing the project in, where the only packages/libraries needed were;
- Tensorflow: To run our keras model
- Opencv-python: To use and display our webcam
- ipykernel: To use python interactive notebooks

I used python v='3.8' for the sake of not running into any problems with newer versions. A template code was provided (below) to play around with and learn, but essentially this code loads up our webcam, takes the live images as input and runs predictions on it having learnt already from the training data which we created on Teachable-Machine.
I added the printing to the screen so that we know what the model is predicting from what it sees captured on our webcam.


```python
        import cv2
        from keras.models import load_model
        import numpy as np
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            if prediction[0][0] > 0.5:
                print('Rock')
            elif prediction[0][1] > 0.5:
                print('Paper')
            elif prediction[0][2] > 0.5:
                print('Scissors')
            else:
                print('Nothing')
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
```
## Milestone 3: Create a Rock, Paper, Scissors Game

Next we need to implement a Rock, Paper, Scissors game. So I started with getting the basic layout of the RPS class, much of which is essentially a carbon copy
from our Hangman project class layout. Following that, the implementation goes from;

Getting the both the users and computers choices, ask_Choice() for users input, computers input is a random choice from a set of the 3 choices.
The user inputs a letter, r-rock, p-paper, s-scissors, all other input is validated.
```python
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
```

The next thing to do is to check who won, with another function check_winner(). To avoid even more repeated code, I checked for a draw as the first condition,
so that we could remove checking for draws separately for each choice. Then we just simply see who beat who and then increment the winners score. 

```python
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
```

Lastly, to put it all together we need to add to the play_RPS() function in which will simulate the playing of Rock, Paper, Scissors. Simply initiates a new RPS_game,
then calls the user to ask for a letter to guess in a loop indefinitely, updating the computers random guess after each round. (later this is changed to conditional of first to 3 wins)

```python
    game = RPS_Game(choice_list)

    while True:
        game.ask_Choice()
        game.computerChoice = choice_list[random.randint(0, len(choice_list)-1)]
```
Sample game of me playing with manual input
> ![image](https://user-images.githubusercontent.com/78024243/163067255-438bea8d-4edf-4942-a9cd-c82cbf9d9866.png)


## Milestone 4: Adapt the Rock, Paper, Scissors Game to use Camera

The last step in the project was to combine the Rock, Paper, Scissors simulated game and the computer vision template code so that user input is then captured through the webcame, rather than manually.
Along with that, adding stuff to take it further and UI friendly, we added a timer that displays to the user so they know when their guess will be taken. This webcam input was programmed as a separate ask_Choice_Webcam() function so we can easily switch between the 2 inputs.

```python
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
                time_end = 2 - (time.time() - time_start)
                blank_image = 255 * np.ones(shape=[100, 100, 3], dtype=np.uint8)
                cv2.putText(blank_image, str(time_end), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 2)
                cv2.imshow("Timer", blank_image)
                if time_end < 0:
                    if user_Choice == 'n':
                        time_start = time.time()
                        flag = False
                        cv2.destroyWindow("Timer")
                    else:
                        break

        cap.release()
        cv2.destroyAllWindows()
        self.check_Winner(user_Choice)
```

Lastly to update the simulated game to end on the first to 3 wins (best of 5 essentially but draws can happen) so we change the main play_RPS() function

```python
    game = RPS_Game(choice_list)

    while True:
        if game.userScore == 3:
            print("The user wins the battle! You were the first to 3 victories!")
            break
        if game.computerScore == 3:
            print("The Computer wins the battle! They were the first to 3 victories!")
            break
        #game.ask_Choice()
        game.ask_Choice_Webcam()
        game.computerChoice = choice_list[random.randint(0, len(choice_list)-1)]
```
Sample game of me playing with webcam input

> ![image](https://user-images.githubusercontent.com/78024243/163068798-718e951b-b8bf-44e7-8f45-393ee038673c.png)

## Conclusions

A round off to the python introduction by creating a Rock, Paper, Scissors simulated game. It was fun to explore the computer vision aspect capturing the users input,
which is an introduction to tensorflow, and keras model training. The game is simple but works well with the webcam.
