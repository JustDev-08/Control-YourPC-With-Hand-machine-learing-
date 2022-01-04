import cv2
import mediapipe as mp
import time
import os

def get_data():
    DATA =  {'right': [] , 'left' : [] , 'up' : [] , 'down' : [] ,  'normal' : [] , 'click' : []}
            # left : [ x ,y ,z ] , right : [x,y,z]
    left_path = os.listdir('./Data/left/')
    right_path = os.listdir('./Data/right/')
    down_path = os.listdir('./Data/down')
    up_path = os.listdir('./Data/up')
    normal_path = os.listdir('./Data/normal')
    click_path = os.listdir('./Data/click')

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils

    pTime = 0
    cTime = 0
    # left
    for i in left_path :
        img = cv2.imread('./Data/left/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    print(id)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['left'].append(xyz)
        cv2.waitKey(1)

    # right
    for i in right_path :
        img = cv2.imread('./Data/right/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['right'].append(xyz)
        cv2.waitKey(1)
    # Down
    for i in down_path :
        img = cv2.imread('./Data/down/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    print(id)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['down'].append(xyz)
        cv2.waitKey(1)
    # Up
    for i in up_path :
        img = cv2.imread('./Data/up/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    print(id)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['up'].append(xyz)
        cv2.waitKey(1)
        # Click
    for i in click_path :
        img = cv2.imread('./Data/click/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    print(id)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['click'].append(xyz)
        cv2.waitKey(1)
        # normal 
    for i in normal_path :
        img = cv2.imread('./Data/normal/'+i)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        xyz = list()
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    xyz.append([lm.x, lm.y , lm.z])
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    print(id)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        DATA['normal'].append(xyz)
        cv2.waitKey(1)
    return DATA

