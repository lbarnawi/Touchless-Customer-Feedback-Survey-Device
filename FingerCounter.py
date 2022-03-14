import cv2
import time
import os
import HandTrackingModule as htm
import numpy as np
from playsound import playsound
import datetime

satisfied = []


def fcf():
    # last_line_sub = 0
    # last_lineFive_sub = 0
    # wCam, hCam = 176, 120
    # wCam, hCam = 352, 240
    # wCam, hCam = 704, 480
    # This had the highest average fps: 15.39477
    wCam, hCam = 960, 480
    # wCam, hCam = 1280, 720
    # wCam, hCam = 1920, 1080
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    # folderPath = "FingerImages"
    # myList = os.listdir(folderPath)
    # overlayList = []
    # for imPath in myList:

    # image = cv2.imread(f'{folderPath}/{imPath}')
    # overlayList.append(image)
    pTime = 0
    detector = htm.handDetector()  # htm.handDetector(detectionCon=0.5)
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        ts = time.time()
        if len(lmList) != 0:
            neutral = []
            unsatisfied = []
            if lmList[4][2] < lmList[2][2] and lmList[8][2] > lmList[4][2] and lmList[12][2] > lmList[4][2] and \
                    lmList[16][2] > lmList[4][2] and lmList[20][2] > lmList[4][2]:
                satisfied.append(1)
                satisfied.append(ts)

                fsat_0 = open("sat.txt", "a")
                fsat_0.writelines(str(satisfied[1]) + '\n')
                fsat_0.close()

                # open and read the file after the appending:
                with open("sat.txt", 'r') as fsat_1:
                    for count, line in enumerate(fsat_1):
                        pass
                    counter = count + 1
                # print(counter)
                with open('sat.txt', 'r') as fsat_2:
                    last_line_sat = fsat_2.readlines()
                    fsat_2.close()

                    last_line_sub_sat = float(last_line_sat[counter - 1])
                    last_lineFive_sub_sat = float(last_line_sat[counter - 10])
                    # print(float(last_line[counter-1]))
                    # print(last_line_sub-last_lineFive_sub)
                    if (last_line_sub_sat) - (last_lineFive_sub_sat) < 10:
                        playsound('beeb.mp3')
                        with open("okSat.txt", "w") as fsat_3:
                            fsat_3.write(str("ok"))
                            fsat_3.close()
                            # print('Ok')
                        time.sleep(2)
                        ffsat = open("feedback_sat.txt", "a")
                        ffsat.writelines(str("المدخل_الرئيسي") + str("^") + str("راضي") + str("^") + str(
                            datetime.datetime.now()) + '\n')
                        # f.writelines(str("راضي") + '\n')
                        # f.writelines(str(datetime.datetime.now()) + '\n')
                        # f.writelines( str(ts) + '\n')
                        ffsat.close()
                # If the four other fingers are open apart from the thumb
            elif lmList[4][2] < lmList[2][2] and lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and \
                    lmList[16][2] < lmList[14][2] and lmList[20][2] < lmList[18][2]:
                neutral.append(1)
                neutral.append(ts)
                # print(neutral)
                # print('محايد')
                fneut_0 = open("neut.txt", "a")
                fneut_0.writelines(str(neutral[1]) + '\n')
                fneut_0.close()
                # open and read the file after the appending:
                with open("neut.txt", 'r') as fneut_1:
                    for count, line in enumerate(fneut_1):
                        pass
                    counter = count + 1
                    fneut_1.close()
                # print(counter)
                with open('neut.txt', 'r') as fneut_2:
                    last_line_neut = fneut_2.readlines()
                    fneut_2.close()
                    last_line_sub_neut = float(last_line_neut[counter - 1])
                    last_lineFive_sub_neut = float(last_line_neut[counter - 10])
                    # print(float(last_line[counter-1]))
                    #print(last_line_sub_neut - last_lineFive_sub_neut)

                    if (last_line_sub_neut) - (last_lineFive_sub_neut) < 1 :#and (last_line_sub_neut) - (last_lineFive_sub_neut) > 1.5 :
                        # print('Ok') #and time.sleep(10)
                        playsound('beeb.mp3')
                        with open("okNeut.txt", "w") as fneut_3:
                            fneut_3.write(str("ok"))
                            fneut_3.close()
                        #time.sleep(2)
                        ffneut = open("feedback_neut.txt", "a")
                        ffneut.writelines(str("المدخل_الرئيسي") + str("^") + str("محايد") + str("^") + str(
                            datetime.datetime.now()) + '\n')
                        # f.writelines(str("محايد") + '\n')
                        # f.writelines(str(datetime.datetime.now()) + '\n')
                        # f.writelines( str(ts) + '\n')
                        ffneut.close()
            elif lmList[4][2] > lmList[2][2] and lmList[8][2] < lmList[4][2] and lmList[12][2] < lmList[4][2] and \
                    lmList[16][2] < lmList[4][2] and lmList[20][2] < lmList[4][2]:
                unsatisfied.append(1)
                unsatisfied.append(ts)
                funs_0 = open("unsat.txt", "a")
                funs_0.writelines(str(unsatisfied[1]) + '\n')
                funs_0.close()
                # open and read the file after the appending:
                with open("unsat.txt", 'r') as funs_1:
                    for count, line in enumerate(funs_1):
                        pass
                    counter = count + 1
                    funs_1.close()
                # print(counter)
                with open('unsat.txt', 'r') as funs_2:
                    last_line_uns = funs_2.readlines()
                    funs_2.close()
                    last_line_sub_uns = float(last_line_uns[counter - 1])
                    last_lineFive_sub_uns = float(last_line_uns[counter - 10])
                    # print(float(last_line[counter-1]))
                    # print(last_line_sub - last_lineFive_sub)
                    if (last_line_sub_uns) - (last_lineFive_sub_uns) < 10:
                        # print('Ok') #and time.sleep(10)
                        playsound('beeb.mp3')
                        with open("okUnsat.txt", "w") as funs_3:
                            funs_3.write(str("ok"))
                            funs_3.close()
                        time.sleep(2)
                        ffuns = open("feedback.txt", "a")
                        ffuns.writelines(str("المدخل_الرئيسي") + str("^") + str("غير_راضي") + str("^") + str(
                            datetime.datetime.now()) + '\n')
                        # f.writelines(str("غير راضي") + '\n')
                        # f.writelines(str(datetime.datetime.now()) + '\n')
                        # f.writelines( str(ts) + '\n')
                        ffuns.close()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        print(fps)
        ffps = open("fpscalc.txt", "a")
        ffps.writelines(str(fps) + '\n')
        # f.writelines(str("راضي") + '\n')
        # f.writelines(str(datetime.datetime.now()) + '\n')
        # f.writelines( str(ts) + '\n')
        ffps.close()

        # cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
        # 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == 'main':
    fcf()

#fcf()
