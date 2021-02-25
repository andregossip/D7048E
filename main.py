import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard as kb

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

keyboard = Controller()
currentDirection = ""
currentDirectionKey = []
isPaused = False
isPauseReleased = False
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
    #keyboard.release(key)

def realeseInput(currentdirection, currentDirectionKeys):
    if currentDirection != "":
        for buttons in currentDirectionKeys:
            keyboard.release(buttons)

def recognizeLeftHandGesture(landmarks):
    thumbState = 'UNKNOW'
    indexFingerState = 'UNKNOW'
    middleFingerState = 'UNKNOW'
    ringFingerState = 'UNKNOW'
    littleFingerState = 'UNKNOW'
    recognizedHandGesture = None

    pseudoFixKeyPoint = landmarks[2]['x']
    if (landmarks[3]['x'] < pseudoFixKeyPoint and landmarks[4]['x'] < landmarks[3]['x']):
        thumbState = 'CLOSE'    
    elif (pseudoFixKeyPoint < landmarks[3]['x'] and landmarks[3]['x'] < landmarks[4]['x']):
        thumbState = 'OPEN'    

    pseudoFixKeyPoint = landmarks[6]['y']
    if (landmarks[7]['y'] < pseudoFixKeyPoint and landmarks[8]['y'] < landmarks[7]['y']):
        indexFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[7]['y'] and landmarks[7]['y'] < landmarks[8]['y']):
        indexFingerState = 'CLOSE'    

    pseudoFixKeyPoint = landmarks[10]['y']
    if (landmarks[11]['y'] < pseudoFixKeyPoint and landmarks[12]['y'] < landmarks[11]['y']):
        middleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[11]['y'] and landmarks[11]['y'] < landmarks[12]['y']):
        middleFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[14]['y']
    if (landmarks[15]['y'] < pseudoFixKeyPoint and landmarks[16]['y'] < landmarks[15]['y']):
        ringFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[15]['y'] and landmarks[15]['y'] < landmarks[16]['y']):
        ringFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[18]['y']
    if (landmarks[19]['y'] < pseudoFixKeyPoint and landmarks[20]['y'] < landmarks[19]['y']):
        littleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[19]['y'] and landmarks[19]['y'] < landmarks[20]['y']):
        littleFingerState = 'CLOSE'

    if (thumbState == 'CLOSE' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 2 # "TWO"   
    elif (thumbState == 'CLOSE' and indexFingerState == 'OPEN' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 1 # "TWO"   
    else:
        recognizedHandGesture = 0 # "UNKNOW"
    return recognizedHandGesture

def getStructuredLandmarks(landmarks):
  structuredLandmarks = []
  for j in range(42):
    if( j %2 == 1):
      structuredLandmarks.append({ 'x': landmarks[j - 1], 'y': landmarks[j] })
  return structuredLandmarks

def recognizeRightHandGesture(landmarks):
    thumbState = 'UNKNOW'
    indexFingerState = 'UNKNOW'
    middleFingerState = 'UNKNOW'
    ringFingerState = 'UNKNOW'
    littleFingerState = 'UNKNOW'
    recognizedHandGesture = None

    pseudoFixKeyPoint = landmarks[2]['x']
    if (landmarks[3]['x'] > pseudoFixKeyPoint and landmarks[4]['x'] > landmarks[3]['x']):
        thumbState = 'CLOSE'    
    elif (pseudoFixKeyPoint > landmarks[3]['x'] and landmarks[3]['x'] > landmarks[4]['x']):
        thumbState = 'OPEN'    

    pseudoFixKeyPoint = landmarks[6]['y']
    if (landmarks[7]['y'] < pseudoFixKeyPoint and landmarks[8]['y'] < landmarks[7]['y']):
        indexFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[7]['y'] and landmarks[7]['y'] < landmarks[8]['y']):
        indexFingerState = 'CLOSE'    

    pseudoFixKeyPoint = landmarks[10]['y']
    if (landmarks[11]['y'] < pseudoFixKeyPoint and landmarks[12]['y'] < landmarks[11]['y']):
        middleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[11]['y'] and landmarks[11]['y'] < landmarks[12]['y']):
        middleFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[14]['y']
    if (landmarks[15]['y'] < pseudoFixKeyPoint and landmarks[16]['y'] < landmarks[15]['y']):
        ringFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[15]['y'] and landmarks[15]['y'] < landmarks[16]['y']):
        ringFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[18]['y']
    if (landmarks[19]['y'] < pseudoFixKeyPoint and landmarks[20]['y'] < landmarks[19]['y']):
        littleFingerState = 'OPEN'    
    elif (pseudoFixKeyPoint < landmarks[19]['y'] and landmarks[19]['y'] < landmarks[20]['y']):
        littleFingerState = 'CLOSE'

    if (thumbState == 'CLOSE' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 2 # "TWO"   
    elif (thumbState == 'CLOSE' and indexFingerState == 'OPEN' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 1 # "TWO"   
    else:
        recognizedHandGesture = 0 # "UNKNOW"
    return recognizedHandGesture

def getStructuredLandmarks(landmarks):
    structuredLandmarks = []
    for j in range(42):
        if( j %2 == 1):
            structuredLandmarks.append({ 'x': landmarks[j - 1], 'y': landmarks[j] })
    return structuredLandmarks

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
    for hand_landmarks in results.multi_hand_landmarks:
        x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width
        y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height
        #right
        if x > 420 and (y > 160 and y < 320) and currentDirection != "right":
            #print("Right")
            doInput([Key.right], currentDirection, currentDirectionKey)
            currentDirection = "right"
            currentDirectionKey = [Key.right]
        #left
        elif x < 210 and (y > 160 and y < 320) and currentDirection != "left":
            #print("Left")
            doInput([Key.left], currentDirection, currentDirectionKey)
            currentDirection = "left"
            currentDirectionKey = [Key.left]
        #up
        elif y < 160 and (x < 420 and x > 210) and currentDirection != "up":
            #print("up")
            doInput([Key.up], currentDirection, currentDirectionKey)
            currentDirection = "up"
            currentDirectionKey = [Key.up]
        #down
        elif y > 320 and (x < 420 and x > 210) and currentDirection != "down":
            #print("down")
            doInput([Key.down], currentDirection, currentDirectionKey)
            currentDirection = "down"
            currentDirectionKey = [Key.down]
        #up and right
        elif y < 160 and x > 420 and currentDirection != "upRight":
            #print("up and right")
            doInput([Key.up, Key.right], currentDirection, currentDirectionKey)
            currentDirection = "upRight"
            currentDirectionKey = [Key.up, Key.right]
        elif x < 210 and y < 160 and currentDirection != "upLeft":
            #print("up and left")
            doInput([Key.up, Key.left], currentDirection, currentDirectionKey)
            currentDirection = "upLeft"
            currentDirectionKey = [Key.up, Key.left]

        elif (x > 210 and x < 420) and (y > 160 and y < 320) and currentDirection != "":
            #print("Stop")
            realeseInput(currentDirection, currentDirectionKey)
            currentDirection = ""
            currentDirectionKey = []
        mp_drawing.draw_landmarks(
        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    keypoints = []
    for landmark in results.multi_hand_landmarks[0].landmark:
        keypoints.append(landmark.x)
        keypoints.append(landmark.y)
        currentDirection = ""
        currentDirectionKey = []
    if(recognizeRightHandGesture(getStructuredLandmarks(keypoints)) == 2):
        togglePause([Key.esc], isPaused)

    with kb.Events() as events:
        for event in events:
            if event.key == kb.Key.esc:
                break
            else:
                print('Received event {}'.format(event))

  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 9:
    break
hands.close()
cap.release()
