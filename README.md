# D7048E, Interactive systems design
### Project in an advanced interface/interaction technology 

## 1. Introduction
This is a program consisting of 2D games that you play on your computer. Instead of using the keyboard or mouse to control the character you use hand motions. In order to play a game in this manner only a webcam is required to be connected to the computer.

The target audience for this is anyone with a computer and webcam that wants to try a different way of playing a game. What we wish to achieve with this game is a fun experience for anyone that wants to try it. The goal is that it should be easy to understand and learn how to play and navigate through the game. We want to make a game that is fun for everyone to play alone as well as together with their friends!
## 2. Requirements
Python 3.7 or higher
Pip
## 3. Installing and running the program
###  Set up environment
Use for example Anaconda or similar to create a new environment.

### Open the terminal and do the following steps to start the program:

```bash
git clone https://github.com/andregossip/D7048E.git
```

```bash
cd D7048E
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```
After running the last command the menu interface and the camera interface will open. In order to navigate through the menu with your hand movements the menu has to be the active window. The same goes for when you play a game, the game has to be the active window for it to work.

## 4. Current errors
- Super Mario & Flappy Bird: Not possible to use the hand movements corresponding to the enter and escape key. When playing the game you therefore have to use the escape key to pause and enter key to select an option in the game menu.
- Two hands may create unwanted actions
- Other hand gestures than shown in the tutorial may create unwanted actions
- Menu may close randomly
- Game window can not be closed with hand gesture

## 5. References
### Hand recognition: 
https://gist.github.com/TheJLifeX/74958cc59db477a91837244ff598ef4a
https://github.com/google/mediapipe

### Super Mario game: 
https://github.com/mx0c/super-mario-python

### Snake game: 
https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900

### Flappy Bird game:
https://github.com/Marishwaran99/Flappy-bird
