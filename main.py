import cv2
import time
import mediapipe as mp
from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard as kb
from handRecognition import recognizeLeftHandGesture, recognizeRightHandGesture, getStructuredLandmarks
import subprocess

menuStarted = False
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
keyboard = Controller()
currentKey = ""
currentKeyLabels = []
menuStarted = False
show = True
childProcess = None

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

def doInput(key, currentKey, currentKeyLabels):
    if currentKey != "":
        for buttons in currentKeyLabels:
            keyboard.release(buttons)
    for button in key:
        keyboard.press(button)

def realeseInput(currentDirection, currentKeyLabels):
    if currentDirection != "":
        for buttons in currentKeyLabels:
            keyboard.release(buttons)

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

        for landmark in hand_landmarks.landmark:
            keypoints.append(landmark.x)
            keypoints.append(landmark.y)

        if recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 2 and currentKey != "esc":
            doInput([Key.esc], currentKey, currentKeyLabels)
            currentKey = "esc"
            currentKeyLabels = [Key.esc]
        elif recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 1 and currentKey != "enter":
            doInput([Key.enter], currentKey, currentKeyLabels)
            currentKey = "enter"
            currentKeyLabels = [Key.enter]
        elif recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 9:
            cap.release()
        else:
            #right
            if x > (image_width * 2/3) and (y > image_height/3 and y < image_height * 2/3) and currentKey != "right":
                #print('right')
                doInput([Key.right], currentKey, currentKeyLabels)
                currentKey = "right"
                currentKeyLabels = [Key.right]
            #left
            elif x < (image_width/3) and (y > image_height/3 and y < image_height * 2/3) and currentKey != "left":
                #print('left')
                doInput([Key.left], currentKey, currentKeyLabels)
                currentKey = "left"
                currentKeyLabels = [Key.left]
            #up
            elif y < image_height/3 and (x < image_width*2/3 and x > image_width/3) and currentKey != "up":
                #print('up')
                doInput([Key.up], currentKey, currentKeyLabels)
                currentKey = "up"
                currentKeyLabels = [Key.up]
            #down
            elif y > (image_height * 2/3) and (x < image_width*2/3 and x > image_width/3) and currentKey != "down":
                #print('down')
                doInput([Key.down], currentKey, currentKeyLabels)
                currentKey = "down"
                currentKeyLabels = [Key.down]
            #up and right
            elif y < image_height/3 and x > (image_width * 2/3) and currentKey != "upRight":
                doInput([Key.up, Key.right], currentKey, currentKeyLabels)
                currentKey = "upRight"
                currentKeyLabels = [Key.up, Key.right]
            #up and left
            elif x < image_width/3 and y < image_height/3 and currentKey != "upLeft":
                doInput([Key.up, Key.left], currentKey, currentKeyLabels)
                currentKey = "upLeft"
                currentKeyLabels = [Key.up, Key.left]
            #down and left
            elif x < image_width/3 and y > image_height * 2/3 and currentKey != "downLeft":
                doInput([Key.down, Key.left], currentKey, currentKeyLabels)
                currentKey = "downLeft"
                currentKeyLabels = [Key.down, Key.left]
            #down and right
            elif x > image_width * 2/3 and y > image_height * 2/3 and currentKey != "downRight":
                doInput([Key.down, Key.right], currentKey, currentKeyLabels)
                currentKey = "downRight"
                currentKeyLabels = [Key.down, Key.right]
            #Stop
            elif (image_width / 3 < x < image_width * 2 / 3) and (y > image_height / 3 and y < image_height * 2 / 3) and currentKey != ("" or "enter" or "esc"):
                realeseInput(currentKey, currentKeyLabels)
                currentKey = ""
                currentKeyLabels = []

        mp_drawing.draw_landmarks(
        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

  cv2.imshow('MediaPipe Hands', image)

  #Open the menu after the hand is shown (This is to ensure that the menu allways is selected)
  if menuStarted == False:
      menuStarted = True
      childProcess = subprocess.Popen("python menu.py")

  poll = childProcess.poll()
  if poll is not None:
    break

  if cv2.waitKey(5) & 0xFF == 110:
    break


hands.close()
cap.release()
