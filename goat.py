import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cam = cv2.VideoCapture(0)
mycoordinatedata = {}
i=1
while i==1:
    data,image = cam.read()
    image = cv2.flip(image,1)
    results = hands.process(image)
    height,width = image.shape[:2]
    if results.multi_hand_landmarks:
        for handid,hand_landmarks in enumerate(results.multi_hand_landmarks): #for hands
            
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            for id,lms in enumerate(hand_landmarks.landmark):
                x_cord = lms.x * width
                y_cord = lms.y * height
                mycoordinatedata[id] = (x_cord,y_cord)
                try:
                    if mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] > mycoordinatedata[9][1]:
                        print("Type of Plastic is PET")
                        w=float(input("enter weight of plastics bottles(in gms): "))
                        p=25*(w/1000)
                        print("Number of points earned: ",p)
                        break
                    elif mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] < mycoordinatedata[9][1]:
                        print("Type of Plastic is HDPE")
                        w=float(input("enter weight of plastics bottles(in gms): "))
                        p=60*(w/1000)
                        print("Number of points earned: ",p)
                        break
                    elif mycoordinatedata[8][1] < mycoordinatedata[5][1] and mycoordinatedata[12][1] < mycoordinatedata[9][1] and mycoordinatedata[16][1]<mycoordinatedata[13][1] and mycoordinatedata[20][1]<mycoordinatedata[17][1]:
                        print("Type of Plastic is PS")
                        w=float(input("enter weight of plastics bottles(in gms): "))
                        p=50*(w/1000)
                        print("Number of points earned: ",p)
                        break
                except KeyError:
                    pass
                 
            

    cv2.imshow("Project",image)
    cv2.waitKey(1)  

    
cam.release()
cv2.destroyAllWindows()
