import cv2
import time
import mediapipe as mp
from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard as kb
from handRecognition import recognizeLeftHandGesture, recognizeRightHandGesture, getStructuredLandmarks
import subprocess

subprocess.Popen("python menu.py")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
keyboard = Controller()
currentDirection = ""
currentDirectionKey = []
isPressingEnter = False
isPressingEscape= False
# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)



image_width = cap.get(3)
image_height = cap.get(4)

print("image_width", image_width)
print("image_height", image_height)

overlay = cv2.imread('overlay3.png')
overlay = cv2.resize(overlay, (int(image_width), int(image_height)))
overlay = cv2.bitwise_not(overlay)

def doInput(key, currentDirection, currentDirectionKeys):
    if currentDirection != "":
        for buttons in currentDirectionKeys:
            keyboard.release(buttons)
    for button in key:
        keyboard.press(button)

def realeseInput(currentdirection, currentDirectionKeys):
    if currentDirection != "":
        for buttons in currentDirectionKeys:
            keyboard.release(buttons)

def togglePause():
    global isPressingEscape
    if isPressingEscape:
        keyboard.press(Key.esc)
    else:
        keyboard.release(Key.esc)

def quitPause():
    global isPressingEnter
    if isPressingEnter:
        keyboard.press(Key.enter)
    else:
        keyboard.release(Key.enter)

while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    # If loading a video, use 'break' instead of 'continue'.
    continue

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

  #overlay = cv2.invert(overlay, overlay)
  image = cv2.add(image,overlay)

  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = False
  results = hands.process(image)

  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks:
    keypoints = []
    for hand_landmarks in results.multi_hand_landmarks:
        x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width
        y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height
        #right
        if x > (image_width * 2/3) and (y > image_height/3 and y < image_height * 2/3) and currentDirection != "right":
            #print("Right")
            doInput([Key.right], currentDirection, currentDirectionKey)
            currentDirection = "right"
            currentDirectionKey = [Key.right]
        #left
        elif x < (image_width/3) and (y > image_height/3 and y < image_height * 2/3) and currentDirection != "left":
            #print("Left")
            doInput([Key.left], currentDirection, currentDirectionKey)
            currentDirection = "left"
            currentDirectionKey = [Key.left]
        #up
        elif y < image_height/3 and (x < image_width*2/3 and x > image_width/3) and currentDirection != "up":
            #print("up")
            doInput([Key.up], currentDirection, currentDirectionKey)
            currentDirection = "up"
            currentDirectionKey = [Key.up]
        #down
        elif y > (image_height * 2/3) and (x < image_width*2/3 and x > image_width/3) and currentDirection != "down":
            #print("down")
            doInput([Key.down], currentDirection, currentDirectionKey)
            currentDirection = "down"
            currentDirectionKey = [Key.down]
        #up and right
        elif y < image_height/3 and x > (image_width * 2/3) and currentDirection != "upRight":
            #print("up and right")
            doInput([Key.up, Key.right], currentDirection, currentDirectionKey)
            currentDirection = "upRight"
            currentDirectionKey = [Key.up, Key.right]
        #up and left
        elif x < image_width/3 and y < image_height/3 and currentDirection != "upLeft":
            #print("up and left")
            doInput([Key.up, Key.left], currentDirection, currentDirectionKey)
            currentDirection = "upLeft"
            currentDirectionKey = [Key.up, Key.left]
        #down and left
        elif(x < image_width/3 and y > image_height * 2/3 and currentDirection != "downLeft"):
            #print("down and left")
            doInput([Key.down, Key.left], currentDirection, currentDirectionKey)
            currentDirection = "downLeft"
            currentDirectionKey = [Key.down, Key.left]
        #down and right
        elif(x > image_width * 2/3 and y > image_height * 2/3 and currentDirection !="downRight"):
            #print("down and left")
            doInput([Key.down, Key.right], currentDirection, currentDirectionKey)
            currentDirection = "downRight"
            currentDirectionKey = [Key.down, Key.right]
        #Stop
        elif (x > image_width/3 and x < image_width * 2/3) and (y > image_height/3 and y < image_height*2/3) and currentDirection != "":
            #print("Stop")
            realeseInput(currentDirection, currentDirectionKey)
            currentDirection = ""
            currentDirectionKey = []
        for landmark in hand_landmarks.landmark:
            keypoints.append(landmark.x)
            keypoints.append(landmark.y)

        mp_drawing.draw_landmarks(
        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    if(recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 2):
        isPressingEscape = True
        togglePause()
    elif(recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 1):
        isPressingEnter = True
        quitPause()
    else:
        isPressingEnter = False
        isPressingEscape = False
    

  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 9:
    break
hands.close()
cap.release()
